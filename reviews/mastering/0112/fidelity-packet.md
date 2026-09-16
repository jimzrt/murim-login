# Fidelity Gate — Chapter 112

Audit the complete assembled English chapter against the Korean source.
Report only genuine source-fidelity defects: wrong action, subject, object,
causality, quantity, mechanism, terminology, ambiguity, joke logic, register,
or physical detail. Check repeated UI labels and counters against how they
behave across the whole scene. Interpret idioms by their function, not by
translating their component words. Do not report optional stylistic rewrites.
Do not invent `current` spans that are absent from the assembled English.
Do not report a glossary-correct rendering as a defect merely because the
baseline used an older synonym.

Return exactly one JSON object and no Markdown fence:

{
  "summary": "brief assessment",
  "findings": [
    {
      "id": "F01",
      "severity": "critical|major|minor",
      "source": "source location",
      "current": "exact uniquely occurring English span",
      "defect": "specific fidelity defect",
      "replacement": "finished replacement only when necessary",
      "rationale": "source-grounded reason",
      "confidence": 0.0
    }
  ]
}

Use an empty findings array when the chapter is faithful. A critical or major
finding blocks promotion; minor findings are recorded for human inspection.

## Korean source

```text
  1|＃112화
  2|
  3|
  4|
  5|마적이 백주대낮에 대로를 활보한다?
  6|
  7|평소라면 결코 있을 수 없는 일이다. 가장 먼저 인근의 무림 문파가 나설 것이고 그다음은 관아의 병졸들이 제압할 것이다.
  8|
  9|그러나 마적들의 숫자가 수백에 달한다면, 그들을 토벌해야 할 무림 문파조차 압도한다면 관아의 벼슬아치도 눈을 감고 귀를 막을 수밖에 없다.
 10|
 11|바로 지금처럼.
 12|
 13|“저, 저놈들 마적 아니여?”
 14|
 15|“놈이라니, 자네 목숨이 세 개쯤 되나? 그 악명 높다는 적풍단이잖아.”
 16|
 17|“그 적풍단? 얼마 전에 항산검문이랑 붙어서 깨진 것 아니었나?”
 18|
 19|“그런 줄 알았지. 한데 이번에는 좀 다른가 보더라고. 벌써 저잣거리에 항산검문이 멸문지화를 면치 못할 거라는 소문이 파다해.”
 20|
 21|“그래도 깜냥이 있는데 설마하니 마적들 따위한테…….”
 22|
 23|“어허, 그 입! 맨 앞에 가는 저 사내가 풍양이라고, 적풍단 두목인데 절정 고수라더군.”
 24|
 25|“뭣이, 절정 고수?”
 26|
 27|“그래, 마적이라고 무시할 게 못 된다니까. 듣기로는 무공만 강한 게 아니라 머리도 아주 비상하다던데.”
 28|
 29|양민들의 두려움 섞인 웅성거림이 풍양과 휘하 마적들의 귓속을 파고들었다.
 30|
 31|풍양의 오른편에서 말을 몰던 수하가 넌지시 말을 건넸다.
 32|
 33|“저놈들의 주둥이를 찢어 놓을까요?”
 34|
 35|“그리하고 싶으냐?”
 36|
 37|“단주께서 허락해 주신다면 저 두 놈부터 처리한 다음 마을 전체를 불바다로 만들지요.”
 38|
 39|“늙은이들은 죽이고, 젊은 놈들은 사로잡고, 여인들은 겁탈하겠다?”
 40|
 41|“흐흐, 저 같은 놈들한테야 늘 하던 일 아닙니까. 어차피 항산검문 놈들은 지금쯤 겁을 잔뜩 집어먹고 담벼락 뒤에 숨어 있을 터인데.”
 42|
 43|“그렇겠지. 모든 힘을 끌어모은 일전을 준비 중일 것이다.”
 44|
 45|“그래 봤자 계란으로 바위 치깁니다. 단주께서 항산검문 놈들을 쓸어 버리고 그 자리를 차지하시는 건 기정사실이죠.”
 46|
 47|“그래서 허락하지 않는 것이다.”
 48|
 49|“예?”
 50|
 51|풍양은 어리둥절한 수하의 반응에 너털웃음을 터트렸다.
 52|
 53|하나같이 생각이 짧고 천성이 잔인하다. 그래서 마적이 된 것이고, 풍양이 그들을 곁에 두는 이유이기도 했다.
 54|
 55|‘다루기가 쉬우니까.’
 56|
 57|웃음을 그친 그가 입을 뗐다.
 58|
 59|“대동지부를 몰살시킨 것은 전쟁의 일부다. 그러나 지금 양민들을 건드렸다가는 태원진가가 끼어들 구실을 만들어 주는 것밖에 안 돼.”
 60|
 61|“그놈들이 산서성의 주인이라도 된답니까?”
 62|
 63|“아직은 아니지만 머지않아 그리되겠지. 그전에 항산검문을 집어삼키고 개처럼 넙죽 엎드려 있어야 하지 않겠느냐?”
 64|
 65|“저어, 단주님 말씀을 의심하는 건 아닙니다만…… 태원진가 같은 정파 놈들이 우리 같은 마적들을 좋게 보겠습니까?”
 66|
 67|“마적? 누가 마적이냐?”
 68|
 69|“예?”
 70|
 71|“지난번에 보니 항산검문주의 미색(美色)이 대단하더구나.”
 72|
 73|눈을 껌뻑거리던 풍양의 수하는 마침내 뜻을 알아차리고 입꼬리를 말아 올렸다.
 74|
 75|“혼기가 꽉 찼으니 지아비를 맞이해야 하겠군요.”
 76|
 77|“멸문지화와 혼인. 둘 중 하나를 택해야겠지.”
 78|
 79|“그럼 적풍단은……?”
 80|
 81|“알맹이를 취하고 껍데기는 뒤집어써야지. 어디 보자, 다른 놈들에 비해 네가 그나마 얼굴이 멀쩡하니 수문각주를 시켜 주마.”
 82|
 83|“으하하! 목숨을 다 바쳐 충성하겠습니다.”
 84|
 85|수하의 웃음소리를 들으며 풍양은 고삐를 움켜쥐었다.
 86|
 87|‘마침내 여기까지 왔다.’
 88|
 89|냉철한 성격의 소유자인 그였지만 야망을 향해 한 걸음 다가섰다는 생각에 가슴이 뛰었다.
 90|
 91|오래전의 기억이 새록새록 떠올라 눈앞을 스친다.
 92|
 93|‘벌써 이십 년이 훌쩍 넘었군.’
 94|
 95|마적이 되는 길은 생각 이상으로 쉽고 간단했다. 제 발로 찾아가거나, 잡히거나. 풍양의 경우에는 후자였다.
 96|
 97|어린 시절 죄를 지어 관아로 압송되어 가던 도중에 마적단의 습격을 받은 것이 인생의 전환점이었다.
 98|
 99|
100|
101|‘두목, 여기 어린놈도 있는데요?’
102|
103|‘응? 비쩍 곯아서 팔아 봤자 몇 푼 받지도 못하겠네. 꼬마야, 소매치기라도 하다가 걸렸냐?’
104|
105|‘아뇨. 사람을 죽여서요.’
106|
107|‘사람을 죽였다고? 네 나이가 몇인데?’
108|
109|‘열셋이요.’
110|
111|‘죽인 이유는?’
112|
113|‘사흘 동안 굶었는데 왕초가 만두를…….’
114|
115|‘만두? 동냥질한 걸 뺏긴 거냐? 그럼 눈 돌아갈 만하지.’
116|
117|‘그게 아니라요. 배는 고프고, 동냥질할 힘도 없고. 앞에서는 만두를 먹으니까.’
118|
119|‘……그래서 죽였다?’
120|
121|‘뺏어 먹는 게 빠를 것 같아서요.’
122|
123|‘야, 이놈 풀어 주고 뭐라도 먹여. 오늘부터 우리 식구다.’
124|
125|
126|
127|풍양은 그날부로 마적이 됐다. 천애 고아로 유리걸식하던 그는 눈치가 비상했고 머리 회전도 빨랐다.
128|
129|사흘에 한 끼를 먹을까 말까 했던 과거에 비하면 마적 생활은 풍요로웠다.
130|
131|약탈? 살인? 고작 열세 살에 만두를 먹고 싶다는 이유로 살인을 저질렀던 풍양에게는 당연히 해야 할 일에 불과했다.
132|
133|
134|
135|‘허 참, 내가 마적질만 십 년 넘게 했는데 너 같은 놈은 처음 본다. 죄책감이라는 게 없는 놈 같아.’
136|
137|‘왜요? 전 마적이잖아요.’
138|
139|‘자식이. 보통은 그게 아니라니까. 차차 익숙해지는 거지, 처음부터 능숙한 놈은 없다고.’
140|
141|‘두목도 그러셨어요? 전 쉽던데.’
142|
143|‘쉽다, 쉽다라……. 이거 범 새끼를 키우는 게 아닌가 싶긴 한데, 나한테 무공 한 수 배워 볼 테냐?’
144|
145|‘무공이요?’
146|
147|‘그래, 무공. 너야 아직 어린 나이니까 근골과 무재만 좀 받쳐 준다면 충분히 고수가 될 수 있을 게다.’
148|
149|‘그럼 오늘부터 사부라고 부를게요.’
150|
151|‘사제지간은 염병, 됐으니까 지금처럼만 해.’
152|
153|
154|
155|사제지간을 맺지 않은 건 잘한 일이었다. 일 년 후, 두목은 일류 고수에게 목이 잘려 죽었고 풍양은 새로운 마적단에 둥지를 틀었다.
156|
157|
158|
159|‘광칠이 밑에 있었다고?’
160|
161|‘예. 배불리 먹여 주시기만 하면 충성을 바치겠습니다.’
162|
163|‘눈치는 제법 있어 보이는군. 어린놈이라고 봐주는 거 없으니까 알아서 잘 따라와라.’
164|
165|
166|
167|고원은 치열했다. 상단을 잘못 건드렸다가 마적단 전체가 몰살되는 일도 있었고 마적단들끼리의 알력 다툼도 끊이질 않았다. 그러나 풍양은 매번 살아남았고, 점점 강해졌다.
168|
169|그의 나이 이립(而立)이 되었을 때, 무공은 일류에 접어들었고 제법 규모 있는 마적단의 조장 자리를 꿰찰 수 있었다.
170|
171|‘하지만 딱 거기까지였지.’
172|
173|힘의 법칙은 어디에나 적용되는 법.
174|
175|고원도 결국 강자가 지배하는 무림의 일부분이었다.
176|
177|풍양에게는 원대한 야망과 뛰어난 머리가 있었지만, 우두머리에 걸맞은 무력을 갖추지는 못했다.
178|
179|‘삼류 무공의 한계.’
180|
181|풍양의 무재는 뛰어났다.
182|
183|어린 시절 명문 정파에 입문하여 훌륭한 내공심법과 무공을 익혔다면 진즉 절정의 벽을 넘어섰을지도 모른다.
184|
185|그러나 거지 소굴에서 자라고 고원의 마적들에게 삼류 무공을 배운 그의 한계는 명확했다.
186|
187|‘천운(天運)이 따르지 않았다면 지금도 제자리걸음이었겠지.’
188|
189|풍양의 입가에 진한 웃음이 맺혔다.
190|
191|삼 년 전, 그날을 기점으로 풍양의 인생은 송두리째 바뀌었다. 마적단의 일개 조장에서 고원의 한 축을 움직이는 적풍단의 단주, 그리고 이제는 무림 문파를 집어삼킬 차례다.
192|
193|“단주!”
194|
195|수하의 외침에 풍양은 상념에서 깨어났다. 저 멀리, 성벽처럼 높게 쌓아 올린 돌담이 마침내 모습을 드러내고 있었다.
196|
197|‘항산검문.’
198|
199|자신과 적풍단의 새로운 보금자리를 바라보던 풍양의 시선에 한 사람이 들어왔다. 멀리 떨어진 거리에서도 느껴지는 불같은 기세.
200|
201|‘항산호 철무백.’
202|
203|항산검문을 취하기 위해서는 반드시 넘어야 할 벽.
204|
205|비록 지난번에는 약간의 손해를 보고 물러났지만…….
206|
207|‘오늘은 다르지.’
208|
209|풍양은 무의식적으로 품 안을 더듬었다. 단단한 목갑을 확인한 그의 웃음이 더더욱 진해졌다.
210|
211|“단주, 명령을.”
212|
213|“포위해라. 개미 새끼 한 마리 빠져나가지 못하도록. 그다음에 사자를 보내.”
214|
215|멸문과 혼인.
216|
217|항산검문에게 주어진 선택지는 두 개뿐이다.
218|
219|“오늘 해가 지기 전에 항산검문을 손에 넣을 것이다.”
220|
221|
222|
223|* * *
224|
225|
226|
227|“놈들이 본 문을 빈틈없이 에워쌌습니다!”
228|
229|“그 숫자가 이백이 훌쩍 넘어갑니다!”
230|
231|“문주, 부디 결단을.”
232|
233|상석에 앉아 있던 이소월은 침착한 얼굴로 입을 열었다.
234|
235|“병력 배치는 끝났나요?”
236|
237|“백여 명 중 절반은 문을 막고 나머지는 방패와 활로 무장시켰습니다.”
238|
239|말이 백여 명이지, 실은 그것에 한참 못 미친다는 사실을 대전의 모두가 알고 있었다.
240|
241|지난밤 항산검문의 중진 몇이 가족과 자신들을 따르는 수하들을 데리고 줄행랑을 쳤기 때문이다.
242|
243|“철 숙부, 제가 따로 말씀드린 건 어떻게 됐나요?”
244|
245|“네 말대로 조치해 두었다.”
246|
247|이소월의 계책은 다름 아닌 기름이었다. 장원 곳곳에 마차 열 대 분량의 기름을 골고루 뿌려 놓았다.
248|
249|잘 마른 건초 더미로 덮어 두었으니 불이 닿기만 해도 사방이 불바다로 변할 것은 자명했다.
250|
251|‘동귀어진이라도 할 셈인가?’
252|
253|철무백은 걱정스러웠지만 말을 아꼈다. 그가 오랜 세월 지켜봤던 이소월은 아주 어린 시절부터 언제나 침착하고 총명한 아이였다.
254|
255|“하루, 딱 하루만 버티면 됩니다. 태원진가의 지원군이 오고 있으니 그때까지만 시간을 끌면 충분히 승산이 있어요.”
256|
257|“태, 태원진가에서 지원군을 보냈습니까?”
258|
259|“산서잠룡과 진천검이 직접 오고 있다는군요.”
260|
261|대전에 모인 이들의 얼굴이 한층 밝아졌다. 진천검 진무경이야 이미 중원에서도 명성이 자자한 무공의 천재고, 산서잠룡 진태경은 떠오르는 샛별이다.
262|
263|그가 항산검문과의 전쟁을 통해서 명성을 얻었다는 사실은 껄끄럽지만 한 편이라고 생각하니 천군만마가 따로 없다.
264|
265|무엇보다…….
266|
267|“풍양이 아무리 간 큰 놈이라고 해도 태원진가의 직계를 상대로 검을 겨누진 못할 겁니다.”
268|
269|“……그렇겠죠.”
270|
271|이소월은 내심 씁쓸했다. 얼마 전만 하더라도 태원진가와 어깨를 나란히 하던 항산검문이다.
272|
273|산서 북부를 호령하던 무림 문파가 이제는 마적단을 상대로도 버티는 것에 주력해야 한다니.
274|
275|‘오늘 일은 결코 잊지 않는다.’
276|
277|입술을 질끈 깨문 그 순간이었다.
278|
279|대전 문이 열리고 수문각의 무사가 헐레벌떡 뛰어와 외쳤다.
280|
281|“문주님, 적들이 사자를 보내왔습니다!”
282|
283|“사자?”
284|
285|“예. 직접 만나 뵙고 전해 드릴 말이 있다고…….”
286|
287|이소월은 망설임 없이 고개를 끄덕였다.
288|
289|일각이라도 전투를 늦출 수 있다면 뭐든지 해야 한다.
290|
291|“들여라.”
292|
293|수문각 무사가 물러난 지 얼마 되지 않아 적풍단의 사자가 대전으로 안내되었다. 썩은 이를 드러내며 히죽 웃은 그가 과장되게 허리를 굽혔다.
294|
295|“대항산검문의 문주님을 뵙소.”
296|
297|다분히 조롱 섞인 태도였지만 중진들은 물론이고 불같은 성격인 철무백도 분노를 참았다. 앞서 이소월의 신신당부가 있었기 때문이다.
298|
299|“무슨 일로 사자를 보냈지?”
300|
301|“거, 먼 길 온 사람한테 탁주라도 한 사발 주고 물어봐야 하는 것 아니…… 헉.”
302|
303|적풍단의 사자는 말을 잇지 못하고 몸을 부르르 떨었다.
304|
305|분노를 참지 못한 철무백이 한 걸음 앞으로 나서며 엄청난 기세를 내뿜었기 때문이다.
306|
307|“탁주가 그리 먹고 싶더냐?”
308|
309|깊게 가라앉은 음성에 사자가 정신없이 고개를 흔들었다.
310|
311|“아, 아닙니다. 목이 말라서 허, 헛소리를 그만.”
312|
313|“철 숙부. 그만하세요.”
314|
315|“……흥, 헛소리 그만하고 말이나 전해라.”
316|
317|간신히 철무백의 기세에서 풀려난 사자가 더듬더듬 입을 열었다.
318|
319|“다, 단주께서 말씀하시길, 무익한 전쟁은 멈추고 이제 우의를 다지자 하십니다.”
320|
321|“우의?”
322|
323|항산검문의 중진들은 자신의 귀를 의심했다.
324|
325|전대 문주인 이천백을 배신하고 소문주 이소광마저 죽인 것이 누구인가? 심지어 바로 얼마 전에는 대동지부의 식솔들을 몰살시키기까지 하지 않았던가.
326|
327|그러나 이소월의 반응은 달랐다. 그녀는 놀란 기색도 없이 사자를 똑바로 응시했다.
328|
329|“거절한다면?”
330|
331|“멸문지화를 면치 못할 거라 하셨습니다.”
332|
333|“사람들을 살리고 싶으면 혼인 예물로 항산검문을 통째로 바치라는 뜻이군.”
334|
335|“저, 저는 거기까지는 잘…….”
336|
337|이쯤 되니 대전 안의 사람들도 풍양이 전한 ‘우의’의 의미를 알아차릴 수 있었다. 모두가 분노했지만 그중 가장 빠르게 움직인 사람은 항산호 철무백이었다.
338|
339|퍽!
340|
341|말 그대로 찰나의 순간, 십여 장의 거리를 뛰어넘은 철무백의 일 권이 사자의 가슴에 박혔다. 가공할 열기를 머금은 붉은 권기(拳氣)가 가슴뼈를 박살 내고 피와 살을 태웠다.
342|
343|“꺼허어어.”
344|
345|마지막 단말마와 함께 사자의 눈동자에서 빛이 사라졌다.
346|
347|놈의 가슴에서 주먹을 뽑아낸 철무백이 이소월을 향해 몸을 돌렸다.
348|
349|“백번 죽어 마땅한 놈이었다.”
350|
351|“저도 같은 생각이에요. 다만…….”
352|
353|천천히 자리에서 일어난 이소월이 말을 이었다.
354|
355|“이제 싸움을 피할 수 없겠군요.”
356|
357|반 시진 후, 항산검문의 모두는 사방에서 울리는 뿔피리 소리를 들을 수 있었다.
```

## Assembled English

```markdown
[P1]
# Chapter 112

[P2]
Mounted bandits riding openly down the main road in broad daylight?

[P3]
Under normal circumstances, it would be unthinkable. The nearest Murim sect would be the first to act, followed by soldiers from the local authorities.

[P4]
But if the mounted bandits numbered in the hundreds—enough to overwhelm even the Murim sect responsible for suppressing them—the officials could only close their eyes and cover their ears.

[P5]
Just like now.

[P6]
“Ar-aren’t those mounted bandits?”

[P7]
“Watch what you call them. Do you have three lives or something? That’s the infamous Red Wind Band.”

[P8]
“The Red Wind Band? Weren’t they defeated by the Mount Heng Sword Sect not long ago?”

[P9]
“That’s what we thought. But this time seems different. The marketplace is already rife with rumors that the Mount Heng Sword Sect won’t escape total destruction.”

[P10]
“Still, the sect has some ability. Surely they won’t lose to mere mounted bandits…”

[P11]
“Hey, watch your mouth! The man riding at the front is Pung Yang, the leader of the Red Wind Band. They say he’s a Peak master.”

[P12]
“What? A Peak master?”

[P13]
“Yeah. You can’t dismiss them just because they’re mounted bandits. I hear he isn’t merely strong in martial arts—he’s exceptionally clever, too.”

[P14]
The commoners’ fearful whispers wormed their way into Pung Yang’s ears and those of his mounted bandits.

[P15]
A subordinate riding on Pung Yang’s right spoke casually.

[P16]
“Shall I rip those bastards’ mouths apart?”

[P17]
“Do you want to?”

[P18]
“If the Leader permits it, I’ll deal with those two first, then turn the entire village into a sea of flames.”

[P19]
“You’ll kill the old, capture the young men, and rape the women?”

[P20]
“Heh heh. Isn’t that what men like us always do? The Mount Heng Sword Sect bastards must be cowering behind their walls by now, scared out of their wits.”

[P21]
“They probably are. They’ll be gathering all their strength for one final battle.”

[P22]
“It won’t matter. It’ll be like throwing an egg against a rock. It’s a foregone conclusion that you’ll wipe out the Mount Heng Sword Sect and take its place.”

[P23]
“That is why I won’t permit it.”

[P24]
“What?”

[P25]
Pung Yang burst into hearty laughter at his subordinate’s bewildered reaction.

[P26]
Every one of them was shortsighted and cruel by nature. That was why they had become mounted bandits—and why Pung Yang kept them close.

[P27]
*Because they’re easy to handle.*

[P28]
When his laughter subsided, he spoke.

[P29]
“Wiping out the Datong Branch was part of the war. But if we harm commoners now, all we’ll accomplish is giving the Jin Family of Taiyuan an excuse to intervene.”

[P30]
“Are they the rulers of Shanxi Province or something?”

[P31]
“Not yet. But they will be soon enough. Before that happens, shouldn’t we swallow the Mount Heng Sword Sect and lie flat like dogs?”

[P32]
“Um, Leader, I’m not doubting you, but… would orthodox factions like the Jin Family of Taiyuan really look favorably on mounted bandits like us?”

[P33]
“Mounted bandits? Who’s a mounted bandit?”

[P34]
“What?”

[P35]
“Last time, I noticed that the Sect Leader of the Mount Heng Sword Sect was quite beautiful.”

[P36]
Pung Yang’s subordinate blinked several times before finally catching his meaning. The corners of his mouth curled upward.

[P37]
“She’s of marriageable age. I suppose it’s time she took a husband.”

[P38]
“She has two choices: total destruction or marriage.”

[P39]
“Then what will happen to the Red Wind Band…?”

[P40]
“We’ll take the heart of it and wear the outer shell. Let’s see… Compared to the others, your face is at least presentable. I’ll make you Master of the Gatekeeper Pavilion.”

[P41]
“Ha ha ha! I’ll devote my life to serving you!”

[P42]
As he listened to his subordinate’s laughter, Pung Yang tightened his grip on the reins.

[P43]
*At last, I’ve made it this far.*

[P44]
He was a cold and levelheaded man, but his heart pounded at the thought that he had taken another step toward his ambition.

[P45]
Memories from long ago surfaced one after another, flickering before his eyes.

[P46]
*It’s already been well over twenty years.*

[P47]
Becoming a mounted bandit had been easier and simpler than he had expected. There were only two ways: go looking for them yourself or get caught by them. In Pung Yang’s case, it had been the latter.

[P48]
When he was young, he had committed a crime and was being taken to the local authorities when a mounted-bandit group attacked. That had been the turning point of his life.

[P49]
*“Boss, there’s a kid here too.”*

[P50]
*“Hm? He’s so scrawny we wouldn’t get more than a few coins for him even if we sold him. Kid, did you get caught pickpocketing?”*

[P51]
*“No. I killed someone.”*

[P52]
*“You killed someone? How old are you?”*

[P53]
*“Thirteen.”*

[P54]
*“Why did you kill him?”*

[P55]
*“I hadn’t eaten for three days, and the boss had dumplings…”*

[P56]
*“Dumplings? Did he take away what you begged for? That would be enough to make anyone snap.”*

[P57]
*“No. I was hungry, and I didn’t have the strength to beg. He was eating dumplings right in front of me.”*

[P58]
*“…So you killed him?”*

[P59]
*“I thought it would be faster to take them and eat them.”*

[P60]
*“Hey, let this kid go and feed him something. He’s one of us from today.”*

[P61]
Pung Yang became a mounted bandit that day.

[P62]
An orphan with no one in the world, he had wandered from place to place begging for food. He was exceptionally perceptive and quick-witted.

[P63]
Compared to his past, when he had barely eaten a meal every three days, life as a mounted bandit was lavish.

[P64]
Robbery? Murder?

[P65]
To Pung Yang, who had committed murder at the age of thirteen simply because he wanted to eat dumplings, such things were nothing more than what had to be done.

[P66]
*“Good grief. I’ve been a mounted bandit for more than ten years, but I’ve never seen anyone like you. It’s like you don’t have a conscience.”*

[P67]
*“Why? I’m a mounted bandit.”*

[P68]
*“Kid, that’s not how it usually works. You get used to it little by little. No one is skilled from the very beginning.”*

[P69]
*“Were you like that too, Boss? It was easy for me.”*

[P70]
*“Easy, easy… I’m starting to wonder if I’m raising a tiger cub. How about learning a thing or two about martial arts from me?”*

[P71]
*“Martial arts?”*

[P72]
*“Yes, martial arts. You’re still young, so if your bones and martial talent are up to the task, you could become a master.”*

[P73]
*“Then I’ll call you Master from today onward.”*

[P74]
*“Master and disciple, my ass. Forget it. Just keep doing what you’re doing now.”*

[P75]
Not forming a master-disciple relationship had been the right decision.

[P76]
A year later, his boss was beheaded by a First Rate master, and Pung Yang found a new nest in another mounted-bandit group.

[P77]
*“You were under Gwangchil?”*

[P78]
*“Yes. As long as you feed me well, I’ll swear my loyalty to you.”*

[P79]
*“You seem reasonably sharp. I won’t go easy on you just because you’re young, so keep up on your own.”*

[P80]
Gaoyuan was brutal.

[P81]
Entire mounted-bandit groups were sometimes wiped out after attacking the wrong merchant caravan, and power struggles between the groups never ceased.

[P82]
But Pung Yang survived every time, growing stronger with each passing year.

[P83]
By the time he turned thirty, his martial arts had entered the First Rate realm, and he managed to seize the position of squad leader in a mounted-bandit group of considerable size.

[P84]
*But that was as far as I got.*

[P85]
The law of strength applied everywhere.

[P86]
Gaoyuan was ultimately just another part of the Murim, where the strong ruled.

[P87]
Pung Yang possessed grand ambitions and an exceptional mind, but he lacked the martial power befitting a leader.

[P88]
*The limit of Third Rate martial arts.*

[P89]
Pung Yang’s martial talent was extraordinary.

[P90]
Had he entered a prestigious orthodox sect as a child and learned an excellent internal cultivation technique and martial arts, he might have crossed the wall to Peak long ago.

[P91]
But he had grown up in a beggars’ den and learned Third Rate martial arts from the mounted bandits of Gaoyuan. His limits were clear.

[P92]
*If heaven’s fortune hadn’t favored me, I’d probably still be stuck in the same place.*

[P93]
A deep smile settled over Pung Yang’s lips.

[P94]
Three years ago, on that day, his life had changed completely. He had gone from being a mere squad leader in a mounted-bandit group to the leader of the Red Wind Band, one of the powers moving Gaoyuan—and now it was time to swallow a Murim sect.

[P95]
“Leader!”

[P96]
His subordinate’s shout snapped Pung Yang out of his thoughts.

[P97]
Far in the distance, stone walls piled high like a fortress had finally come into view.

[P98]
*The Mount Heng Sword Sect.*

[P99]
As Pung Yang gazed at his and the Red Wind Band’s new home, one person entered his sight. Even from this distance, he could feel the man’s fiery aura.

[P100]
*The Tiger of Mount Heng, Cheol Mubaek.*

[P101]
The wall he had to overcome to take the Mount Heng Sword Sect.

[P102]
Although he had withdrawn after suffering a slight loss last time…

[P103]
*Today will be different.*

[P104]
Pung Yang unconsciously felt inside his robes. After confirming the hard wooden case there, his smile deepened.

[P105]
“Leader, your orders?”

[P106]
“Surround them. Don’t let so much as a single ant escape. Then send an envoy.”

[P107]
Total destruction or marriage.

[P108]
The Mount Heng Sword Sect had only two choices.

[P109]
“I’ll have the Mount Heng Sword Sect in my hands before sunset.”

[P110]
* * *

[P111]
“They’ve surrounded our sect without leaving a gap!”

[P112]
“Their numbers are well over two hundred!”

[P113]
“Sect Leader, please make a decision!”

[P114]
Seated in the place of honor, Lee Seowol spoke calmly.

[P115]
“Are the troops deployed?”

[P116]
“Of the hundred or so men, half are blocking the sect entrance. The rest have been armed with shields and bows.”

[P117]
Everyone in the main hall knew that “a hundred or so” was a generous estimate. In truth, they fell well short of that number.

[P118]
Several of the Mount Heng Sword Sect’s senior figures had fled the previous night, taking their families and the subordinates who followed them.

[P119]
“Uncle Cheol, what happened with what I asked you to do?”

[P120]
“I took care of it as you instructed.”

[P121]
Lee Seowol’s plan involved oil.

[P122]
They had spread enough oil to fill ten wagons evenly throughout the estate.

[P123]
They had covered it with piles of well-dried hay, so it was obvious that the entire area would turn into a sea of flames the moment fire touched it.

[P124]
*Does she intend to take them down with us?*

[P125]
Cheol Mubaek was worried, but he kept his thoughts to himself. In all the years he had watched Lee Seowol, she had always been calm and clever, even from a very young age.

[P126]
“We only need to hold out for one day. Just one day. Reinforcements from the Jin Family of Taiyuan are on their way. If we can delay the enemy until then, we have a good chance of winning.”

[P127]
“R-reinforcements from the Jin Family of Taiyuan?”

[P128]
“I hear the Sleeping Dragon of Shanxi and the Heaven Shaking Sword are coming in person.”

[P129]
The faces of everyone gathered in the main hall brightened.

[P130]
The Heaven Shaking Sword, Jin Mukyung, was already renowned throughout the Central Plains as a martial arts genius, while the Sleeping Dragon of Shanxi, Jin Taekyung, was a rising star.

[P131]
It was uncomfortable that he had earned his fame through a war against the Mount Heng Sword Sect, but knowing that he was now on their side made it feel as though they had gained a thousand troops.

[P132]
Above all else…

[P133]
“No matter how bold Pung Yang is, he won’t dare raise his sword against a direct descendant of the Jin Family of Taiyuan.”

[P134]
“…I suppose not.”

[P135]
Lee Seowol felt bitter inside.

[P136]
Not long ago, the Mount Heng Sword Sect had stood shoulder to shoulder with the Jin Family of Taiyuan.

[P137]
Now, a Murim sect that had once commanded northern Shanxi had to focus all its strength on merely holding out against a mounted-bandit group.

[P138]
*I will never forget what happened today.*

[P139]
Just as she bit down hard on her lip, the doors to the main hall opened, and a martial artist from the Gatekeeper Pavilion came running in, shouting.

[P140]
“Sect Leader, the enemy has sent an envoy!”

[P141]
“An envoy?”

[P142]
“Yes. He says there’s something he wishes to tell you in person…”

[P143]
Lee Seowol nodded without hesitation.

[P144]
If they could delay the battle by even a single moment, they had to do everything they could.

[P145]
“Bring him in.”

[P146]
Not long after the Gatekeeper Pavilion martial artist withdrew, the Red Wind Band’s envoy was escorted into the main hall.

[P147]
Flashing his rotten teeth in a crooked grin, he bowed deeply in an exaggerated manner.

[P148]
“I pay my respects to the Sect Leader of the great Mount Heng Sword Sect.”

[P149]
His attitude was clearly mocking, but the senior figures—and even the fiery-tempered Cheol Mubaek—suppressed their anger. Lee Seowol had repeatedly warned them beforehand.

[P150]
“Why did you send an envoy?”

[P151]
“Well, shouldn’t you offer a man who has traveled so far a bowl of rice wine before you start asking—gasp!”

[P152]
The Red Wind Band’s envoy broke off and began trembling violently.

[P153]
Unable to contain his anger, Cheol Mubaek had taken one step forward and unleashed an overwhelming aura.

[P154]
“Do you want rice wine that badly?”

[P155]
At the deep, heavy voice, the envoy frantically shook his head.

[P156]
“N-no, sir. I was thirsty and said something stu—stupid.”

[P157]
“Uncle Cheol. That’s enough.”

[P158]
“…Hmph. Stop talking nonsense and deliver your message.”

[P159]
Barely freed from Cheol Mubaek’s aura, the envoy stammered.

[P160]
“T-the Leader says we should end this pointless war and cement our friendship.”

[P161]
“Friendship?”

[P162]
The senior figures of the Mount Heng Sword Sect doubted their own ears.

[P163]
Who had betrayed the previous Sect Leader, Lee Cheonbaek, and killed even the Young Sect Leader, Lee Seogwang? And hadn’t they massacred the families and dependents of the Datong Branch only a short while ago?

[P164]
But Lee Seowol reacted differently. Without the slightest hint of surprise, she stared straight at the envoy.

[P165]
“And if we refuse?”

[P166]
“He said you won’t escape total destruction.”

[P167]
“So he means that if we want to save our people, we must offer the Mount Heng Sword Sect in its entirety as a wedding gift.”

[P168]
“I-I don’t know anything beyond that…”

[P169]
By now, everyone in the main hall understood what Pung Yang had meant by “friendship.”

[P170]
They were all furious, but the first to act was the Tiger of Mount Heng, Cheol Mubaek.

[P171]
*Thud!*

[P172]
In the literal blink of an eye, Cheol Mubaek crossed more than ten *jang* and drove his fist into the envoy’s chest.

[P173]
The red fist aura carrying horrifying heat shattered his chest bones and burned his blood and flesh.

[P174]
“Ghuuuh…”

[P175]
With one final death rattle, the light vanished from the envoy’s eyes.

[P176]
Cheol Mubaek pulled his fist from the man’s chest and turned toward Lee Seowol.

[P177]
“He deserved to die a hundred times over.”

[P178]
“I agree. But…”

[P179]
Lee Seowol slowly rose from her seat and continued.

[P180]
“Now there’s no avoiding the fight.”

[P181]
One hour later, everyone in the Mount Heng Sword Sect heard the sound of horn calls ringing out from all directions.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source, RULES.md, or the exact
glossary requires the change. Exact glossary English wins over an older baseline
synonym for the same Korean key.

```markdown
[P1]
# Chapter 112

[P2]
Mounted bandits openly riding down the main road in broad daylight?

[P3]
Under normal circumstances, it would be unthinkable. The nearest Murim sect would be the first to act, followed by the soldiers from the local authorities.

[P4]
But if there were hundreds of mounted bandits—enough to overwhelm even the Murim sect that was supposed to suppress them—the officials could only close their eyes and cover their ears.

[P5]
Just like now.

[P6]
“Ar-aren’t those mounted bandits?”

[P7]
“Don’t call them ‘those guys.’ Do you have three lives or something? They’re the infamous Red Wind Band.”

[P8]
“The Red Wind Band? Weren’t they defeated by the Mount Heng Sword Sect not long ago?”

[P9]
“That’s what we thought. But this time seems different. Rumors are already spreading through the marketplace that the Mount Heng Sword Sect won’t escape total destruction.”

[P10]
“Still, the sect has some ability. Surely they won’t lose to mere mounted bandits…”

[P11]
“Hey, watch your mouth! The man riding at the front is Pung Yang, the leader of the Red Wind Band. They say he’s a Peak master.”

[P12]
“What? A Peak master?”

[P13]
“Yeah. You can’t dismiss them just because they’re mounted bandits. I hear he isn’t merely strong in martial arts—he’s exceptionally clever, too.”

[P14]
The commoners’ fearful whispers wormed their way into Pung Yang’s ears and those of his mounted bandits.

[P15]
A subordinate riding on Pung Yang’s right spoke softly.

[P16]
“Shall I rip those bastards’ mouths apart?”

[P17]
“Do you want to?”

[P18]
“If the Leader permits it, I’ll deal with those two first, then turn the entire village into a sea of flames.”

[P19]
“You’ll kill the old men, capture the young men, and rape the women?”

[P20]
“Heh heh. Isn’t that what men like us always do? The Mount Heng Sword Sect bastards are probably cowering behind their walls by now, scared out of their wits.”

[P21]
“They probably are. They’ll be preparing for a final battle by gathering every bit of strength they have.”

[P22]
“It won’t matter. That’ll just be eggs thrown at a rock. It’s a foregone conclusion that the Leader will wipe out the Mount Heng Sword Sect and take its place.”

[P23]
“That is why I won’t permit it.”

[P24]
“What?”

[P25]
Pung Yang burst into a hearty laugh at his subordinate’s bewildered reaction.

[P26]
They were all shallow-minded and cruel by nature. That was why they had become mounted bandits—and why Pung Yang kept them close.

[P27]
*Because they’re easy to handle.*

[P28]
When his laughter subsided, he spoke.

[P29]
“Destroying the Datong Branch was part of the war. But if we harm commoners now, all we’ll accomplish is giving the Jin Family of Taiyuan an excuse to intervene.”

[P30]
“Are they the rulers of Shanxi or something?”

[P31]
“Not yet. But they will be soon enough. Before that happens, shouldn’t we swallow the Mount Heng Sword Sect and lie flat like dogs?”

[P32]
“Um, Leader, I’m not doubting your judgment, but… would orthodox factions like the Jin Family of Taiyuan really look favorably on mounted bandits like us?”

[P33]
“Mounted bandits? Who’s a mounted bandit?”

[P34]
“What?”

[P35]
“Last time, I noticed that the Sect Leader of the Mount Heng Sword Sect was quite beautiful.”

[P36]
Pung Yang’s subordinate blinked several times before finally understanding. The corners of his mouth curled upward.

[P37]
“She’s of marriageable age, so she’ll need to take a husband.”

[P38]
“She has two choices: total destruction or marriage.”

[P39]
“Then what will happen to the Red Wind Band…?”

[P40]
“We’ll take the heart of it and wear the outer shell. Let’s see… Compared to the others, your face is at least presentable. I’ll make you Master of the Gatekeeper Pavilion.”

[P41]
“Ha ha ha! I’ll devote my life to serving you!”

[P42]
As he listened to his subordinate’s laughter, Pung Yang tightened his grip on the reins.

[P43]
*At last, I’ve made it this far.*

[P44]
He was a cold and levelheaded man, but his heart pounded at the thought that he had taken another step toward his ambition.

[P45]
Memories from long ago flickered before his eyes.

[P46]
*It’s been well over twenty years already.*

[P47]
Becoming a mounted bandit had been easier and simpler than he had expected. There were only two ways: go looking for them or get caught by them. In Pung Yang’s case, it had been the latter.

[P48]
When he was young, he had committed a crime and was being taken to the local authorities when a mounted-bandit group attacked. That had been the turning point of his life.

[P49]
*“Boss, there’s a little one here, too.”*

[P50]
*“Hm? He’s so skinny that we wouldn’t get more than a few coins for him even if we sold him. Kid, did you get caught pickpocketing?”*

[P51]
*“No. I killed someone.”*

[P52]
*“You killed someone? How old are you?”*

[P53]
*“Thirteen.”*

[P54]
*“Why did you kill him?”*

[P55]
*“I hadn’t eaten for three days, and the boss had dumplings…”*

[P56]
*“Dumplings? Did he take away what you begged for? That would be enough to make anyone snap.”*

[P57]
*“No. I was hungry, and I didn’t have the strength to beg. He was eating dumplings right in front of me.”*

[P58]
*“…So you killed him?”*

[P59]
*“I thought it would be faster to take them and eat them.”*

[P60]
*“Hey, let this kid go and feed him something. He’s one of us from today.”*

[P61]
Pung Yang became a mounted bandit that day.

[P62]
An orphan abandoned by the world, he had wandered from place to place begging for food. He was exceptionally perceptive and quick-witted.

[P63]
Compared to his past, when he had barely eaten a meal every three days, life as a mounted bandit was lavish.

[P64]
Robbery? Murder?

[P65]
To Pung Yang, who had committed murder at the age of thirteen simply because he wanted to eat dumplings, such things were nothing more than what had to be done.

[P66]
*“Good grief. I’ve been a mounted bandit for more than ten years, but I’ve never seen anyone like you. It’s as if you don’t have a conscience.”*

[P67]
*“Why? I’m a mounted bandit.”*

[P68]
*“Kid, that’s not how it works. You gradually get used to it. No one is skilled from the very beginning.”*

[P69]
*“Were you like that too, Boss? It was easy for me.”*

[P70]
*“Easy, easy… I’m starting to wonder if I’m raising a tiger cub. How about learning a thing or two about martial arts from me?”*

[P71]
*“Martial arts?”*

[P72]
*“Yes, martial arts. You’re still young, so if your bones and martial talent are up to the task, you could become a master.”*

[P73]
*“Then I’ll call you Master from today onward.”*

[P74]
*“Master and disciple, my ass. Forget it. Just keep doing what you’re doing now.”*

[P75]
Not forming a master-disciple relationship had been a wise decision.

[P76]
A year later, his boss was beheaded and killed by a First Rate master, and Pung Yang found a new nest in another mounted-bandit group.

[P77]
*“You were under Gwangchil?”*

[P78]
*“Yes. If you feed me well, I’ll swear my loyalty to you.”*

[P79]
*“You seem reasonably sharp. I won’t go easy on you because you’re young, so keep up on your own.”*

[P80]
The plateau was brutal.

[P81]
There were times when an entire mounted-bandit group was wiped out after attacking the wrong merchant caravan. The struggles for power between mounted-bandit groups never stopped, either.

[P82]
But Pung Yang survived every time, growing stronger with each passing year.

[P83]
By the time he turned thirty, his martial arts had entered the First Rate realm, and he managed to seize the position of squad leader in a mounted-bandit group of considerable size.

[P84]
*But that was as far as I got.*

[P85]
The law of strength applied everywhere.

[P86]
The plateau was ultimately just another part of the Murim, where the strong ruled.

[P87]
Pung Yang possessed grand ambitions and an exceptional mind, but he lacked the martial power befitting a leader.

[P88]
*The limit of Third Rate martial arts.*

[P89]
Pung Yang’s martial talent was extraordinary.

[P90]
If he had entered a prestigious orthodox sect as a child and learned an excellent internal cultivation technique and martial arts, he might have crossed the wall to Peak long ago.

[P91]
But he had grown up in a beggar’s den and learned Third Rate martial arts from the mounted bandits of the plateau. His limitations were clear.

[P92]
*If heaven’s fortune hadn’t favored me, I’d probably still be standing in the same place.*

[P93]
A deep smile settled over Pung Yang’s lips.

[P94]
Three years ago, on that day, his life had changed completely. He had gone from being a mere squad leader in a mounted-bandit group to the leader of the Red Wind Band, one of the powers moving the plateau—and now it was time to swallow a Murim sect.

[P95]
“Leader!”

[P96]
Pung Yang snapped out of his thoughts at his subordinate’s shout.

[P97]
Far in the distance, stone walls piled high like a fortress had finally come into view.

[P98]
*The Mount Heng Sword Sect.*

[P99]
As Pung Yang gazed at his and the Red Wind Band’s new home, one person entered his sight. Even from this distance, he could feel the man’s fiery aura.

[P100]
*The Tiger of Mount Heng, Cheol Mubaek.*

[P101]
A wall he would have to overcome in order to take the Mount Heng Sword Sect.

[P102]
Although he had withdrawn after suffering a slight loss last time…

[P103]
*Today will be different.*

[P104]
Pung Yang unconsciously felt inside his robes. After confirming the hard wooden case there, his smile deepened.

[P105]
“Leader, your orders?”

[P106]
“Surround them. Don’t let even a single ant escape. Then send an envoy.”

[P107]
Total destruction or marriage.

[P108]
The Mount Heng Sword Sect had only two choices.

[P109]
“I’ll have the Mount Heng Sword Sect in my hands before sunset.”

[P110]
* * *

[P111]
“They’ve surrounded our sect without leaving a gap!”

[P112]
“Their numbers are well over two hundred!”

[P113]
“Sect Leader, please make a decision!”

[P114]
Seated in the place of honor, Lee Seowol calmly opened her mouth.

[P115]
“Are the troops deployed?”

[P116]
“Of the hundred or so men, half are blocking the sect entrance. The rest have been armed with shields and bows.”

[P117]
Everyone in the main hall knew that “a hundred or so” was a generous estimate. In truth, they had far fewer than that.

[P118]
Several of the Mount Heng Sword Sect’s senior figures had fled the previous night, taking their families and the subordinates who followed them.

[P119]
“Uncle Cheol, what happened with what I asked you to do?”

[P120]
“It has been arranged as you instructed.”

[P121]
Lee Seowol’s plan involved oil.

[P122]
They had spread enough oil to fill ten wagons evenly throughout the estate.

[P123]
They had covered it with piles of well-dried hay, so it was obvious that the entire area would turn into a sea of flames the moment fire touched it.

[P124]
*Does she intend for us to perish together with them?*

[P125]
Cheol Mubaek was worried, but he kept his thoughts to himself. In all the years he had watched Lee Seowol, she had always been calm and clever, even from a very young age.

[P126]
“We only need to hold out for one day. Exactly one day. Reinforcements from the Jin Family of Taiyuan are on their way, so we have a good chance of winning if we can stall them until then.”

[P127]
“R-reinforcements from the Jin Family of Taiyuan?”

[P128]
“I hear the Sleeping Dragon of Shanxi and the Heaven Shaking Sword are coming in person.”

[P129]
The faces of everyone gathered in the main hall brightened.

[P130]
The Heaven Shaking Sword, Jin Mukyung, was already renowned throughout the Central Plains as a martial arts genius, while the Sleeping Dragon of Shanxi, Jin Taekyung, was a rising star.

[P131]
It was uncomfortable that he had earned his fame through a war against the Mount Heng Sword Sect, but knowing that he was now on their side made it feel as though they had gained a thousand troops.

[P132]
Above all else…

[P133]
“No matter how bold Pung Yang is, he won’t dare raise his sword against a direct descendant of the Jin Family of Taiyuan.”

[P134]
“…That’s true.”

[P135]
Lee Seowol felt bitter inside.

[P136]
Not long ago, the Mount Heng Sword Sect had stood shoulder to shoulder with the Jin Family of Taiyuan.

[P137]
Now, a Murim sect that had once commanded northern Shanxi had to focus all its strength on merely holding out against a mounted-bandit group.

[P138]
*I will never forget what happened today.*

[P139]
Just then, she bit down hard on her lip.

[P140]
The doors to the main hall opened, and a martial artist from the Gatekeeper Pavilion came running in, shouting.

[P141]
“Sect Leader, the enemy has sent an envoy!”

[P142]
“An envoy?”

[P143]
“Yes. He says there’s something he wishes to tell you in person…”

[P144]
Lee Seowol nodded without hesitation.

[P145]
If they could delay the battle by even a single moment, they had to do everything they could.

[P146]
“Bring him in.”

[P147]
Not long after the Gatekeeper Pavilion martial artist withdrew, the Red Wind Band’s envoy was escorted into the main hall.

[P148]
He exposed his rotten teeth in a crooked grin and bowed deeply in an exaggerated manner.

[P149]
“I pay my respects to the Sect Leader of the great Mount Heng Sword Sect.”

[P150]
His attitude was clearly mocking, but the senior figures—and even Cheol Mubaek, whose temper was as fierce as fire—suppressed their anger. Lee Seowol had repeatedly warned them to do so beforehand.

[P151]
“Why did you send an envoy?”

[P152]
“Well, shouldn’t you give someone who has come such a long way a bowl of rice wine before asking—gasp.”

[P153]
The Red Wind Band’s envoy was unable to finish his sentence and began trembling violently.

[P154]
Cheol Mubaek, unable to contain his anger, had taken one step forward and released an overwhelming aura.

[P155]
“Do you want rice wine that badly?”

[P156]
At the deep, heavy voice, the envoy frantically shook his head.

[P157]
“N-no, sir. I was thirsty, so I said something stu—stupid.”

[P158]
“Uncle Cheol. That’s enough.”

[P159]
“…Hmph. Stop talking nonsense and deliver your message.”

[P160]
Barely freed from Cheol Mubaek’s aura, the envoy stammered.

[P161]
“T-the Leader says we should stop this pointless war and now cement our friendship.”

[P162]
“Friendship?”

[P163]
The senior figures of the Mount Heng Sword Sect doubted their own ears.

[P164]
Who had betrayed the previous Sect Leader, Lee Cheonbaek, and killed even the Young Sect Leader, Lee Seogwang? And hadn’t they massacred the families and dependents of the Datong Branch only a short while ago?

[P165]
But Lee Seowol’s reaction was different. Without the slightest hint of surprise, she stared straight at the envoy.

[P166]
“And if we refuse?”

[P167]
“He said you won’t escape total destruction.”

[P168]
“So he means that if we want to save our people, we must offer the Mount Heng Sword Sect in its entirety as a wedding gift.”

[P169]
“I-I don’t know about anything beyond that…”

[P170]
At this point, everyone in the main hall understood the meaning of the “friendship” Pung Yang had offered.

[P171]
All of them were furious, but Cheol Mubaek was the quickest to act.

[P172]
*Thud!*

[P173]
In the literal blink of an eye, Cheol Mubaek crossed more than ten *jang* and drove one punch into the envoy’s chest.

[P174]
The red fist aura carrying horrifying heat shattered his chest bones and burned his blood and flesh.

[P175]
“Ghuuuh…”

[P176]
With one final death rattle, the light vanished from the envoy’s eyes.

[P177]
Cheol Mubaek pulled his fist from the man’s chest and turned toward Lee Seowol.

[P178]
“He deserved to die a hundred times over.”

[P179]
“I think so, too. But…”

[P180]
Lee Seowol slowly rose from her seat and continued.

[P181]
“We can no longer avoid the fight.”

[P182]
One hour later, everyone in the Mount Heng Sword Sect heard the sound of horn calls ringing out from all directions.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 이천백    | **Lee Cheonbaek**  |
| 이소광    | **Lee Seogwang**   |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 내공     | **internal energy**                              |                                                       |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 정파     | **orthodox faction**                             |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 사제     | **Junior Brother**                           |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 광칠이 | **Gwangchil** | Former mounted-bandit boss who took in Pung Yang and was later killed by a First Rate master. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 대동지부 | **Datong Branch** | Mount Heng Sword Sect branch in Datong. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 수문각 | **Gate Guard Pavilion** | Jin Family gate complex at the main entrance. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 112,
  "passed": true,
  "metrics": {
    "source_characters": 6113,
    "translation_characters": 14561,
    "length_ratio": 2.382,
    "source_paragraphs": 170,
    "translation_paragraphs": 181
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "내공",
        "preferred": "internal energy"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "사제",
        "preferred": "Junior Brother"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진태",
        "preferred": "Jintae"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "조장",
        "preferred": "Captain"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "시진",
        "preferred": "shichen"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "주신",
        "preferred": "God of Drinking"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "수문각",
        "preferred": "Gate Guard Pavilion"
      }
    }
  ]
}
```

## Binding editorial rules

# Translation Rules

## Fidelity

- Translate the Korean source—not the wiki, manhwa, fan translations, or expected plot.
- Semantic fidelity outranks elegance. Never improve rhythm, humor, or localization by changing a physical action, negation, relationship, hierarchy, mechanism, quantity, or causal detail.
- Preserve every fact, causal link, joke, emotional beat, repetition, and intentional omission. Add nothing.
- Preserve small action verbs and pragmatic cues exactly: nodding versus shaking one's head, pretending nothing happened, and mild or approachable impressions are characterization, not expendable texture.
- Preserve viewpoint and tense. Resolve omitted subjects only when context supports it; retain genuine ambiguity.
- Match each speaker's hierarchy, intimacy, humor, and profanity naturally. Do not mechanically retain every honorific or classical self-reference.
- Do not censor or soften content.

## Terminology

- `compendium.md` and `docs/NAMES.md` are binding for established names, titles, ranks, techniques, organizations, system terms, items, and locations. Profile headings and aliases join that ledger.
- Search only exact Korean terms already present in the current chapter; the compendium contains future-sensitive entries.
- Never re-romanize established names or invent grand names for uncertain terms. First use of an unlisted name or title almost always needs a footnote or a mapped ledger term.
- Use `qi` for Murim energy and `mana` for the modern Hunter system when the source distinguishes them. Preserve an established chapter-specific rendering such as `internal energy` when the exact glossary and surrounding Korean distinguish accumulated `공력` from resulting `기운`.
- In System panels, render `등급` as `**Grade:**` for quest, item, skill, and martial-art classifications. Reserve `rank` for Hunter classifications or ordinary prose; never replace a System `Grade` field with `Rank`.

## English and Markdown

- Use contemporary US English and natural action-comedy prose; avoid Korean syntax calques and generic cultivation MTL phrasing.
- File: `translations/NNNN.md`; heading: `# Chapter N`.
- Speech: curly double quotes. Direct thoughts: italics without quotes.
- Use em dashes without spaces, the ellipsis character `…`, and `* * *` for source scene breaks.
- Format each actual game System-message panel as one Markdown blockquote window headed `> **System**`. Keep all consecutive notices, fields, and lines inside that same blockquote; separate windows when prose intervenes. Do not enclose System notices or UI terms in square brackets; the `System` heading and framed blockquote identify the panel. Do not label manuals, ordinary quotations, warnings printed in a manual, or other non-System material as `System`; use a normal blockquote or a specific heading instead. Do not wrap each complete notice in outer `**`; retain bold only for meaningful labels or emphasis inside the panel.
- Keep the final file English-only reading copy: no audit notes, Korean text, summaries, or model metadata.

### Tone and Style

- Write like a polished commercial webnovel: brisk, vivid, accessible, and easy to read aloud.
- Preserve the series’ contrast between danger and comedy. Let absurdity, bad timing, blunt reactions, and grim situations create dark humor without adding jokes absent from the Korean.
- Jin Taekyung’s narration is conversational, observant, self-mocking, and occasionally profane. It may be irreverent even when the situation is serious.
- Keep deadpan punchlines short and well-timed. Do not explain a joke after delivering it.
- Preserve the source's level of explicitness. A euphemism may remain euphemistic even when its meaning is sexual or crude; do not replace it with more graphic English merely for impact.
- Make dialogue spontaneous and character-specific. Preserve hierarchy and intimacy through word choice, address, rhythm, and restraint—not archaic wuxia English.
- Use strong profanity when the Korean is strong, but neither intensify nor sanitize it. Do not make ordinary lines uniformly vulgar. Profanity should reveal mood or relationship.
- Keep action and injury vivid but clear rather than purple. Do not make violence funny unless the source’s framing does.
- Avoid stiff literalism, translator-added melodrama, dated internet slang, and quippy superhero-style banter.
- On the second pass, correct awkward English collocations and word choices without changing meaning or voice. Prefer ordinary, spoken English over stiff Latinate or ceremonial wording when the scene is brisk or comic: “goose bumps” rather than “gooseflesh,” and “laid into them” rather than “launched into a solemn denunciation.” Read the prose aloud and replace any phrase that sounds like a formal essay, legal document, or literal dictionary gloss unless the source deliberately calls for that register.

## Footnotes

Use `[^1]` Markdown footnotes when a brief, factual, spoiler-free explanation materially helps an English reader understand:

- a Korean institution, living arrangement, food, holiday, myth, historical reference, or local custom;
- a Korean word, phrase, idiom, wordplay, or culturally specific image that cannot be conveyed fully by the best natural English analogy;
- a deliberately literal rendering whose cultural or linguistic force would otherwise be lost.

For example, render `고시원` as “goshiwon” when the setting or connotations matter, with a concise footnote explaining that it is a very small, inexpensive room-for-rent housing arrangement. Prefer the best natural English analogy in the prose. Use a literal translation plus a concise footnote when the Korean wording itself matters. Define a term at its first meaningful occurrence and do not repeat the note unnecessarily. Footnotes must be rare, useful, and non-spoiling; do not footnote ordinary vocabulary, fully preserved jokes, or uncertainty. Record consequential uncertainty in `docs/STATE.md`.

## Spoilers and Scope

- Safe profiles contain only facts revealed through the latest completed chapter.
- Never read `characters/spoilers/` during drafting. Reviewers may consult one relevant sealed profile only for a specific unresolved continuity issue after the draft is complete.
- Future knowledge may prevent contradiction but may not add early names, pronouns, certainty, motives, or foreshadowing.
- Translate exactly one requested chapter unless the user explicitly requests a batch. Never modify Korean source files under `source/`.

# Master Editorial Brief

You are the final English-language editor of an existing Korean-to-English novel translation.

The Korean source is the authority for meaning. The existing English is the baseline you are editing, not a draft to discard. Your task is to make the chapter read like professionally written native English commercial fiction while preserving the author's exact story, characterization, humor, register, pacing, ambiguity, and cultural texture.

## Editorial authority

You may freely recast sentences and paragraphs when the English is stiff, literal, repetitive for accidental reasons, awkwardly collocated, over-explained, or syntactically shaped by Korean. You may tighten dialogue, improve rhythm, repair transitions, and make action easier to follow. A technically correct sentence may still need rewriting if a fluent English novelist would not naturally phrase it that way.

Do not change text merely to make it different. If the baseline is already strong, leave it alone.

The accepted baseline is also the project's style and terminology anchor. Do not
replace an established rendering, cultural term, System label, Markdown form, or
recurring phrase with a synonym merely because the synonym sounds smoother.
Make that change only when the Korean source, `RULES.md`, or the exact glossary
requires it. In particular, do not turn a source-specific image into a nearby
English image, or change a gold-spoon joke, item name, technique name, or UI
label into a different expression without source support.

## Fidelity constraints

Never invent, omit, explain away, generalize, intensify, soften, or reinterpret source-supported content. In particular, preserve:

- exact actions, subjects, objects, directionality, causality, quantities, and physical details;
- deliberate ambiguity, euphemism, implication, profanity level, repetition, and withheld information;
- jokes and comic specificity, even when a more generic English joke would sound smoother;
- hierarchy, kinship, forms of address, characterization, and speaker attitude;
- System mechanics, Murim concepts, names, ranks, techniques, items, organizations, and established terminology.
- chapter-level logical consistency: interpret labels, counters, notifications, and repeated facts from how they behave across the scene, not from an isolated surface gloss;
- idioms by their narrative function rather than their component words, and jokes with their setup, recognition, and punchline timing intact;
- cross-sentence implications: do not create a claim that contradicts “again,” an increasing value, an earlier action, or the explanation immediately around it;
- repeated terminology and formatting: once the baseline or glossary establishes a rendering, keep it consistent throughout the chapter unless the source clearly changes the sense;

Do not add jokes, metaphors, explanations, emotional conclusions, or colorful details that are absent from the Korean. Do not replace a specific source image with a generic equivalent merely because the generic version is smoother.

When natural English and literal form conflict, preserve the source meaning and pragmatic effect while changing the English form as much as necessary.

Before returning the chapter, perform a silent continuity pass: trace every
counter, quantity, repeated System label, item or technique name, joke setup and
payoff, and physical cause-and-effect sequence from the Korean through the
finished English. Correct any local sentence that contradicts the sequence.

## Relationship to project files

`RULES.md` is binding. `POLISH.md` describes known translation-English failure modes and should guide the edit. Exact glossary matches are binding unless the packet explicitly marks them otherwise. Character/continuity material is context only and must never override the chapter's Korean source.

## Output

Return only the complete edited English Markdown chapter. Preserve the required chapter heading and project Markdown conventions. Do not provide commentary, a change log, explanations, or a Markdown code fence.
