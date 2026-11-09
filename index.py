from http.server import BaseHTTPRequestHandler


PAGE = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fitcal - Steps and Time Estimator</title>
<style>
:root{color-scheme:dark;--bg:#07111f;--card:#102238;--card2:#152b44;--text:#f5f8fc;--muted:#a9b9ca;--accent:#ff3da8;--blue:#54a8ff;--line:#29445f;--danger:#ff7d9f;}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(circle at 15% 0,#183553 0,transparent 34%),var(--bg);color:var(--text);font:16px/1.5 Inter,ui-sans-serif,system-ui,sans-serif}.shell{max-width:960px;margin:0 auto;padding:44px 20px 64px}header{margin-bottom:28px}h1{font-size:clamp(2rem,5vw,3.4rem);line-height:1.05;margin:0 0 14px;letter-spacing:-.04em}h2{margin:0 0 16px;font-size:1.35rem}p{color:var(--muted);max-width:730px}.card{background:linear-gradient(145deg,rgba(21,43,68,.96),rgba(13,29,48,.96));border:1px solid var(--line);border-radius:20px;padding:24px;margin-top:20px;box-shadow:0 18px 55px #0003}.grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}.field{display:flex;flex-direction:column;gap:8px}label{font-weight:700}input,select{width:100%;border:1px solid #40617e;border-radius:10px;background:#081725;color:var(--text);padding:12px 13px;font:inherit}input:focus,select:focus{outline:3px solid #54a8ff55;border-color:var(--blue)}.modes{display:flex;gap:10px;margin-bottom:18px}.mode{flex:1;border:1px solid #40617e;border-radius:10px;padding:11px;text-align:center;color:var(--muted);cursor:pointer}.mode:has(input:checked){border-color:var(--accent);color:var(--text);background:#ff3da814}.mode input{width:auto;margin-right:8px;accent-color:var(--accent)}button{border:0;border-radius:10px;padding:12px 16px;font:700 1rem inherit;cursor:pointer;background:var(--accent);color:#190a16;margin-top:20px}button.secondary{background:#243e5b;color:var(--text)}button:hover{filter:brightness(1.1)}.actions{display:flex;gap:12px;flex-wrap:wrap}.result{border-left:4px solid var(--accent)}.result dl{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin:0}.result dt{color:var(--muted);font-size:.9rem}.result dd{font-size:1.25rem;font-weight:800;margin:2px 0 0}.notice{padding:12px 14px;border-radius:10px;background:#ff3da814;color:#ffd4eb;margin-top:16px}.error{color:var(--danger);font-weight:700}.empty{color:var(--muted)}table{width:100%;border-collapse:collapse}th,td{text-align:left;padding:11px 8px;border-bottom:1px solid var(--line)}th{color:var(--muted);font-size:.85rem} .summary{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}.metric{background:#0a1b2d;border-radius:12px;padding:14px}.metric small{display:block;color:var(--muted)}.metric strong{display:block;margin-top:4px;font-size:1.1rem}@media(max-width:680px){.grid,.result dl{grid-template-columns:1fr}.summary{grid-template-columns:repeat(2,1fr)}.shell{padding:28px 14px 48px}.card{padding:18px}table{font-size:.82rem;display:block;overflow-x:auto;white-space:nowrap}}
</style>
</head>
<body><main class="shell">
<header><h1>Fitcal - Steps and Time Estimator</h1><p>Fitcal estimates steps, time, and calories for walking, jogging, and running. Add as many activities as you like and review your daily totals.</p></header>
<section class="card"><h2>Plan an activity</h2>
<div class="modes"><label class="mode"><input type="radio" name="mode" value="Distance" checked>Distance</label><label class="mode"><input type="radio" name="mode" value="Calories">Calories</label></div>
<div class="grid"><div class="field"><label id="value-label" for="value">Distance (km)</label><input id="value" type="number" min="0" step=".1" value="5"></div><div class="field"><label for="activity">Activity type</label><select id="activity"><option>Walking</option><option>Jogging</option><option>Running</option></select></div></div><div id="error" class="error" role="alert"></div><button id="add">Add activity</button></section>
<section id="latest" class="card result" hidden><h2>Activity result</h2><div id="latest-content"></div></section>
<section class="card"><h2>Your activities</h2><div id="activities" class="empty">No activities yet.</div><div class="actions"><button id="finish">Finish and show daily summary</button><button id="clear" class="secondary">Clear all activities</button></div></section>
<section id="summary" class="card" hidden><h2>Daily Summary</h2><div id="metrics" class="summary"></div><div class="notice">Thank you for using Fitcal! Have a great workout.</div></section>
</main>
<script>
const rules={Walking:{step:0.75,speed:5,cal:50},Jogging:{step:1,speed:8,cal:70},Running:{step:1.2,speed:12,cal:90}};let activities=[];
const $=id=>document.getElementById(id);const mode=()=>document.querySelector('input[name="mode"]:checked').value;
document.querySelectorAll('input[name="mode"]').forEach(input=>input.addEventListener('change',()=>{$('value-label').textContent=mode()==='Distance'?'Distance (km)':'Target calories (kcal)';$('value').step=mode()==='Distance'?'.1':'10';$('value').value=mode()==='Distance'?5:300;}));
function time(n){return n<60?`${n} minutes`:`${Math.floor(n/60)} ${Math.floor(n/60)===1?'hour':'hours'} ${n%60} minutes`}
function render(){const box=$('activities');if(!activities.length){box.className='empty';box.textContent='No activities yet.'}else{box.className='';box.innerHTML='<table><thead><tr><th>#</th><th>Activity</th><th>Mode</th><th>Distance</th><th>Steps</th><th>Time</th><th>Calories</th></tr></thead><tbody>'+activities.map((a,i)=>`<tr><td>${i+1}</td><td>${a.activity}</td><td>${a.mode}</td><td>${a.distance.toFixed(2)} km</td><td>${a.steps.toLocaleString()}</td><td>${a.time}</td><td>${a.calories.toLocaleString()} kcal</td></tr>`).join('')+'</tbody></table>'}}
$('add').onclick=()=>{const m=mode(),v=Number($('value').value),name=$('activity').value,max=m==='Distance'?100:5000;$('error').textContent='';if(!Number.isFinite(v)||v<=0||v>max){$('error').textContent=`${m} must be more than 0 and at most ${max}${m==='Distance'?' km':' kcal'}.`;return}const r=rules[name],distance=m==='Distance'?v:v/r.cal,steps=Math.round(distance*1000/r.step),minutes=Math.round(distance/r.speed*60),a={activity:name,mode:m,distance,steps,time:time(minutes),minutes,calories:Math.round(distance*r.cal)};activities.push(a);$('latest').hidden=false;$('latest-content').innerHTML=`<p><strong>${name} session</strong></p><dl><div><dt>Mode</dt><dd>${m}</dd></div><div><dt>Distance</dt><dd>${distance.toFixed(2)} km</dd></div><div><dt>Estimated steps</dt><dd>${steps.toLocaleString()}</dd></div><div><dt>Estimated time</dt><dd>${a.time}</dd></div><div><dt>Estimated calories</dt><dd>${a.calories.toLocaleString()} kcal</dd></div></dl>`;render();$('summary').hidden=true};
$('finish').onclick=()=>{if(!activities.length){$('error').textContent='Add at least one activity before finishing.';return}const d=activities.reduce((n,a)=>n+a.distance,0),s=activities.reduce((n,a)=>n+a.steps,0),t=activities.reduce((n,a)=>n+a.minutes,0),c=activities.reduce((n,a)=>n+a.calories,0);$('metrics').innerHTML=[['Activities',activities.length],['Distance',d.toFixed(2)+' km'],['Steps',s.toLocaleString()],['Time',time(t)],['Calories',c.toLocaleString()+' kcal']].map(x=>`<div class="metric"><small>${x[0]}</small><strong>${x[1]}</strong></div>`).join('');$('summary').hidden=false};$('clear').onclick=()=>{activities=[];$('latest').hidden=true;$('summary').hidden=true;$('error').textContent='';render()};
</script></body></html>'''


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(PAGE.encode("utf-8"))
