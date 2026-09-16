# Fidelity Gate — Chapter 113

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
  1|＃113화
  2|
  3|
  4|
  5|항산검문으로 사자를 보낸 뒤 반 시진. 풍양은 망설임 없이 명령을 내렸다.
  6|
  7|“쳐라.”
  8|
  9|속전속결.
 10|
 11|시간을 끌수록 그에게는 불리했다. 적풍단이 항산검문을 포위했다는 소문은 빠르게 퍼져 나갈 것이고 외부 세력, 특히 태원진가가 개입한다면 골치 아파진다.
 12|
 13|‘어차피 무혈입성은 기대하지도 않았다.’
 14|
 15|여인의 몸이라고는 하나 혈랑검 이천백의 핏줄이다.
 16|
 17|대화와 손짓으로 길들일 수 없다면 폭력으로 굴복시켜야 한다. 풍양이 지금까지 해 왔던 방식 그대로.
 18|
 19|부우우우.
 20|
 21|힘찬 뿔피리의 울림이 곳곳에서 울려 퍼졌다. 고원의 마적단들이 사용하는 진격 신호에 항산검문을 에워싼 적풍단의 마적들이 일제히 말의 옆구리를 걷어찼다.
 22|
 23|“돌겨어억!”
 24|
 25|“한 놈도 남김없이 죽여라!”
 26|
 27|두두두두두!
 28|
 29|수백 개의 말발굽이 눈 덮인 지면을 짓밟으며 달렸다.
 30|
 31|뿔피리 소리는 끊이지 않고 힘차게, 멀리 퍼져 나갔다.
 32|
 33|
 34|
 35|* * *
 36|
 37|
 38|
 39|띠링.
 40|
 41|
 42|
 43|- [운기조식]을 성공적으로 완료했습니다.
 44|
 45|- 피로와 체력이 소량 회복됩니다.
 46|
 47|
 48|
 49|시스템 알림음이 들리고 눈을 뜨자마자 주위를 둘러봤다.
 50|
 51|“방금 무슨 소리 못 들었어요?”
 52|
 53|말에게 건초를 먹이고 있던 월화와 혁무진이 영문을 모르겠다는 얼굴로 묻는다.
 54|
 55|“진 공자, 무슨 소리예요?”
 56|
 57|“소리야 항상 나죠. 들어 보세요. 말들이 건초 씹는 소리, 바람 소리…….”
 58|
 59|“그딴 거 말고, 이 자식아.”
 60|
 61|“그럼 뭔데요?”
 62|
 63|“부, 부부젤라?”
 64|
 65|“부부, 뭐요?”
 66|
 67|“스포츠 응원할 때 쓰는…… 됐다. 그런 게 있어.”
 68|
 69|나는 설명하는 것을 포기하고 소리가 들려온, 아니 들려왔다고 생각한 방향을 응시했다. 우연의 일치인지 마침 우리가 향하고 있던, 항산검문이 있을 북쪽이다.
 70|
 71|‘내가 잘못 들었나?’
 72|
 73|월화의 말대로라면 앞으로 세 시진(여섯 시간)은 더 달려야 항산검문에 도착할 수 있다. 무슨 일이 벌어졌다 해도 여기까지 들릴 만한 거리가 아니다.
 74|
 75|‘대포 소리라면 모를까.’
 76|
 77|때마침 운기조식을 끝마친 진무경도 한마디를 보탰다.
 78|
 79|“아무 소리도 안 들렸다.”
 80|
 81|“그런데 분명히 뭔가 들은 것 같단 말이지.”
 82|
 83|“착각이야.”
 84|
 85|“혹시 항산검문에 무슨 일이 난 걸 수도 있잖아.”
 86|
 87|“그럴 수도 있지. 하지만 나한테는 아무 소리도 안 들렸다.”
 88|
 89|“근데 나는 들은 것 같다니까?”
 90|
 91|“그러니까 착각이라는 거다.”
 92|
 93|“무슨 근거로?”
 94|
 95|“간단하지. 네가 들은 걸 내가 못 들었을 리 없으니까.”
 96|
 97|“…….”
 98|
 99|이거 상당히 열받는데 맞는 말이라 반박할 수가 없네.
100|
101|말문이 막힌 나를 보며 진무경이 혀를 찼다.
102|
103|“눈먼 칼에 죽고 싶지 않다면 심신을 다스리는 것에 집중해라. 전장은 무슨 일이 벌어질지 모르는 곳이니까.”
104|
105|누가 누굴 가르쳐?
106|
107|전투 경험으로는 이 중에서 나를 따라갈 사람이 없을 것이다.
108|
109|워낙 익숙해졌기에 평소와 다름없어 보일 뿐, 전투를 준비하고 참여하는 것에 있어서는 이미 닳고 닳았다.
110|
111|“적의 숫자가 많으니 공력을 최대한 아끼고 움직임을 최소화해라. 내가 앞장설 테니 뒤따르기만 하면 문제없다.”
112|
113|그래도 한 핏줄이라고 걱정해 주는 건가?
114|
115|생각해 보면 지금까지 진무경은 싫어하는 티를 팍팍 내면서도 내게 상당한 도움을 주었다.
116|
117|수련도 도와주고, 이번에 항산검문도 함께 가 주고, 어린 시절에는 게을러터진 아우를 갱생시키고자 제법 노력도 했다고 들었다.
118|
119|아무리 진위경의 부탁이 있었다고 해도 정말 나를 싫어했다면 할 수 없는 일들이다.
120|
121|‘알고 보면 정 많은 놈일지도.’
122|
123|이런 성격의 사람을 츤데레라고 하나?
124|
125|새삼 약간 감동이 밀려올 것도 같아 감성적인 눈빛으로 진무경을 바라보는데, 시선이 딱 마주쳤다.
126|
127|“뭘 봐? 눈 깔아.”
128|
129|“…….”
130|
131|“마적 놈들 따위한테 상처 하나라도 입었다가는 내 손에 죽을 줄 알아라.”
132|
133|“……어, 그래.”
134|
135|그럼 그렇지. 츤데레는 개뿔. 내가 잠깐 미쳐서 정신 나간 상상을 했구나.
136|
137|현실을 인정하고 앞서 빼앗은 여분의 말로 안장을 옮기려는데, 어느새 슬쩍 다가온 혁무진이 근심 가득한 얼굴로 입을 열었다.
138|
139|“이공자님이 저도 죽이는 건 아니겠죠?”
140|
141|“……난 죽어도 된다는 소리냐?”
142|
143|“아, 아니 말씀을 왜 그렇게 하세요?”
144|
145|“넌 반드시 내가 죽이고 죽을 테니까 닥치고 출발 준비나 해.”
146|
147|뭐라 구시렁거리는 혁무진의 엉덩이를 걷어차 주고 말에 올라탔다.
148|
149|항산검문까지는 앞으로 세 시진. 이제부터는 정말 일체의 휴식 없이 빡세게 달려야 한다.
150|
151|
152|
153|제한 시간 : 6:25:19
154|
155|
156|
157|* * *
158|
159|
160|
161|항산검문은 하나의 요새 같았다. 높게 쌓아 올린 돌담은 성벽이라 불러도 될 만큼 견고했고 수성(守城)을 위한 각종 방어 시설이 설치되어 있었다.
162|
163|초대 문주인 이천백의 강경한 의지로 세워진 그것들은 삼십여 년 만에 비로소 제 역할을 발휘했다.
164|
165|“쏴라!”
166|
167|쉬쉬쉬쉭!
168|
169|일제히 쏘아진 수십 발의 화살이 돌진하는 기마를 향해 내리꽂혔다.
170|
171|그러나 고원에서 가장 흔히 찾아볼 수 있는 병기가 창과 도, 그리고 활이다. 고원의 전투에 익숙한 적풍단의 마적들은 누군가의 명령이 떨어지기도 전에 각자 한 손에 낀 방패를 치켜세웠다.
172|
173|투둑, 퍼버벅!
174|
175|낙마한 이는 고작 십여 명.
176|
177|바짝 마른 나무에 늙은 말의 엉덩이 가죽을 덧대어 만든 방패는 훌륭히 화살들을 막아 냈다.
178|
179|“크하하핫! 이놈들이 어르신들을 몰라뵙고 감히……!”
180|
181|적풍단의 조장 하나가 웃음을 터트린 그 순간이었다.
182|
183|쐐애애액, 퍼걱!
184|
185|강맹한 기세로 날아온 무언가가 말의 목을 뚫고 조장의 가슴팍에 꽂혔다. 이제 막 일류 초입에 든 그는 믿을 수 없다는 듯 삐죽 튀어나온 화살을 바라보다가 애마와 함께 고꾸라졌다.
186|
187|뒤따라 달려오던 기마 중 몇 기가 그 때문에 대열이 흐트러져 줄줄이 쓰러진다.
188|
189|“쇠뇌, 쇠뇌를 조심해라!”
190|
191|“응사하라!”
192|
193|쉬쉬쉬쉭!
194|
195|앞서 항산검문의 공격이 소낙비였다면 적풍단의 화살 세례는 장대비다. 말을 탄 상태에서도 연거푸 시위를 당기는 그들의 화살은 정확하고 빨랐다.
196|
197|푸푸푸푹!
198|
199|“크아악!”
200|
201|“방패 뒤로 몸을 숨겨라! 고개를 내밀지 마!”
202|
203|그 틈을 타 박차를 가한 마적들은 십여 장 높이의 성벽에 갈고리와 급조한 사다리를 대고 침투를 시도했다.
204|
205|백병전이 시작된 성벽 위에선 비명과 피가 터져 나왔다.
206|
207|“크하하! 모두 죽여라!”
208|
209|“놈들이 올라오지 못하게 막아!”
210|
211|이소월은 가장 높은 망루에서 이 모든 광경을 지켜보고 있었다. 입술이 파르르 떨리고 얼굴에는 핏기가 사라졌다.
212|
213|‘이것이 무림.’
214|
215|죽어 가는 자의 비명, 살고 싶은 자의 몸부림.
216|
217|마침내 맞닥트린 약육강식의 세계는 그녀가 생각했던 것 이상으로 잔혹하고 두려웠다.
218|
219|그러나…….
220|
221|‘물러날 수 없어.’
222|
223|이미 수많은 이들이 죽었다. 떠날 이들은 떠났고, 남은 이들은 목숨을 걸고 싸우고 있다.
224|
225|이소월은 이제 그들을 이끌어야 할 문주이며 항산검문과 운명을 함께해야 하는 몸이다.
226|
227|“문주! 성벽이 위태롭습니다. 지원을 보내야 합니다!”
228|
229|“놈들이 충차(充車)로 문을 부수고 있습니다!”
230|
231|“문주! 어서 조치를!”
232|
233|“문주!”
234|
235|그 순간, 사방에서 빗발치는 급보를 전해 듣던 이소월이 입을 열었다.
236|
237|“내가 신호하면 성벽을 향해 화시(火矢)를 한 발, 문을 향해 두 발을 쏘아 올려라. 그리고 철 숙부.”
238|
239|이소월의 옆을 지키고 있던 철무백이 대답했다.
240|
241|“뭐든 말하거라.”
242|
243|“곧 문이 뚫릴 거예요. 잠시 시간을 벌어 주실 수 있나요?”
244|
245|“나 혼자 말이냐?”
246|
247|“어려운 부탁을 드려 송구할 따름입니다.”
248|
249|“일당백(一當百)이라. 언젠가 꼭 해 보고 싶었지.”
250|
251|“제가 아는 숙부께선 만인적(萬人敵)의 고수십니다. 허나 부디 몸조심하세요.”
252|
253|“오냐, 내 저런 놈들에게 당할 성싶으냐?”
254|
255|껄껄 웃은 철무백이 훌쩍 뛰어내렸다. 항산호, 완숙한 절정 고수인 그가 갔으니 풍양이 나서지 않는 한 아무도 문을 넘을 수 없을 것이다.
256|
257|‘더, 조금만 더.’
258|
259|치열한 전장을 내려다보던 이소월이 돌연 벼락같은 외침을 토해 냈다.
260|
261|“지금!”
262|
263|그녀의 명령을 기다리고 있던 무인 둘이 각각 활시위를 당겼다.
264|
265|다음 순간, 어느새 어둡게 물든 겨울 하늘 위로 날아오른 불화살이 모두의 머리 위에서 환하게 빛났다.
266|
267|
268|
269|* * *
270|
271|
272|
273|유성처럼 떨어지는 불화살은 백 장 너머에 있는 풍양의 눈에도 똑똑히 보였다. 그는 내심 중얼거렸다.
274|
275|“숨겨 둔 한 수가 있었군.”
276|
277|짐작이 확신으로 바뀌는 데까지는 그리 오랜 시간이 걸리지 않았다. 잠시 후, 성벽 둘레에서 엄청난 불길이 솟구쳤기 때문이다.
278|
279|화륵, 화아아악!
280|
281|“끄아아아악!”
282|
283|불에 타 죽는 것은 가장 고통스러운 죽음 중 하나다. 성벽 밑에 개미 떼처럼 몰려 있던 적풍단의 마적들이 끔찍한 비명과 함께 몸부림쳤다.
284|
285|성벽에 걸어 놓은 갈고리의 줄이 끊기고, 목제 사다리가 화염에 휩싸였다.
286|
287|“쳐라!”
288|
289|“마적 놈들을 전부 죽여라!”
290|
291|성벽 밑에서 올라가기를 기다리던 자, 올라가던 자는 불에 타 죽고 이미 올라간 자들은 사방에서 짓쳐 들어오는 병장기에 찔리고 베였다.
292|
293|“나름 준비를 했다 이거지…….”
294|
295|덤덤하게 전장을 응시하는 풍양의 시선에 숯검정처럼 곳곳이 까맣게 그을린 채 돌아오는 마적 하나가 들어왔다.
296|
297|“무슨 일인가?”
298|
299|“다, 단주님. 피해가 너무 큽니다!”
300|
301|마적은 그의 앞에 섬과 동시에 넙죽 엎드려 헐떡거리는 목소리로 말을 이었다.
302|
303|“첫 공격부터 지금까지 족히 일백은 죽은 것 같습니다. 무엇보다 방금 화공(火攻) 때문에 형제들의 사기가…….”
304|
305|“문은?”
306|
307|“예?”
308|
309|“문은 어찌 되었지?”
310|
311|“뚫긴 했습니다만 항산호 철무백이 홀로 버티고 있어서…….”
312|
313|“혼자란 말이냐?”
314|
315|“예. 하지만 워낙 무공이 고강한지라 아무도 나서지 못하고 있습니다.”
316|
317|“그럼 되었다.”
318|
319|풍양은 말과 동시에 손을 내밀었다. 무심코 그 손을 맞잡으려던 마적의 신형이 기우뚱 쓰러진다.
320|
321|어리둥절한 표정으로 굳어 가는 그의 미간에는 비수 한 자루가 깊숙이 박혀 있었다.
322|
323|“병력은 얼마나 남아 있지?”
324|
325|풍양의 오른팔 격인 수하에게는 이런 광경이 익숙했다. 시체를 흘끗 바라본 그가 대답했다.
326|
327|“어림잡아 백오십은 약간 넘고, 이백이 조금 못 됩니다. 우리 측 희생이 더 큰 건 사실입니다.”
328|
329|“적들은 오죽하겠느냐? 지금 성벽 위에 있는 놈들이 항산검문의 마지막 보루다.”
330|
331|“저 얼마 안 되는 놈들이 전부란 말씀이십니까?”
332|
333|“그래.”
334|
335|“단주님을 못 믿는 건 아닙니다만 방금의 화공처럼 또 다른 함정을…….”
336|
337|“그걸 노린 게지.”
338|
339|풍양은 실소를 흘렸다. 누구 머리에서 나온 계략인지는 모르겠지만 제법 머리를 잘 굴렸다.
340|
341|아마 지금보다 경륜이 부족했다면 풍양 역시 또 다른 함정을 의심하고 병력을 뒤로 물렸을 것이다.
342|
343|‘시간을 벌기 위해 애쓰는군. 누군가의 지원을 기다리나?’
344|
345|그렇다면 더욱 망설일 이유가 없다.
346|
347|중과부적(衆寡不敵). 적풍단이 상당한 피해를 입었다고는 해도 항산검문을 쓸어 버리는 것은 일도 아니다.
348|
349|거기에 더해…….
350|
351|“내가 직접 간다.”
352|
353|“단주님께서 직접 말씀이십니까?”
354|
355|“그래, 호랑이를 잡아야 하지 않겠느냐?”
356|
357|너털웃음을 터트린 풍양은 습관적으로 품 안을 더듬었다.
358|
359|단단한 목곽, 그 안에 호랑이를 단숨에 거꾸러트릴 물건이 들어 있었다.
```

## Assembled English

```markdown
[P1]
# Chapter 113

[P2]
Half a shichen after sending an envoy to the Mount Heng Sword Sect, Pung Yang gave the order without hesitation.

[P3]
“Attack.”

[P4]
A swift, decisive battle.

[P5]
The longer it dragged on, the worse it would be for him. Word that the Red Wind Band had surrounded the Mount Heng Sword Sect would spread quickly, and if outside forces—especially the Jin Family of Taiyuan—intervened, things would become troublesome.

[P6]
*I never expected to enter without bloodshed in the first place.*

[P7]
She might be a woman, but she carried the blood of the Blood Wolf Sword, Lee Cheonbaek.

[P8]
If words and gestures couldn’t tame her, he would have to subdue her with violence—the same method Pung Yang had always used.

[P9]
Bwooooooong!

[P10]
Powerful horn calls rang out from every direction. At the advance signal used by the mounted-bandit groups of Gaoyuan, the mounted bandits of the Red Wind Band surrounding the Mount Heng Sword Sect kicked their horses in the ribs as one.

[P11]
“Chaaaarge!”

[P12]
“Kill every last one of them!”

[P13]
Rumble, rumble, rumble!

[P14]
Hundreds of hooves raced forward, trampling the snow-covered ground.

[P15]
The horn calls continued without pause, strong and carrying far into the distance.

[P16]
* * *

[P17]
Ding!

[P18]
> **System**
> 
> **Circulate Qi** was successfully completed.
> 
> A small amount of Fatigue and Stamina has been restored.

[P19]
The moment I heard the System notification and opened my eyes, I looked around.

[P20]
“Did you guys just hear something?”

[P21]
Wolhwa and Hyuk Mujin, who had been feeding hay to the horses, looked at me in confusion.

[P22]
“Young Master Jin, what sound?”

[P23]
“There's always sound. Listen—the horses chewing hay, the wind…”

[P24]
“Not that crap, you idiot.”

[P25]
“Then what?”

[P26]
“A-a vuvuzela?”

[P27]
“Vuvu… what?”

[P28]
“The thing people use to cheer at sporting events… Never mind. It’s a thing.”

[P29]
I gave up trying to explain and stared in the direction the sound had come from—or rather, the direction I thought it had come from.

[P30]
Coincidentally, it was north, toward the Mount Heng Sword Sect—the very direction we were heading.

[P31]
*Did I hear it wrong?*

[P32]
According to Wolhwa, we still had another three shichen—six hours—of riding before we reached the Mount Heng Sword Sect. Whatever had happened, we were too far away to hear it from here.

[P33]
*Unless it was cannon fire.*

[P34]
Jin Mukyung, who had just finished circulating his qi, added his opinion.

[P35]
“I didn’t hear anything.”

[P36]
“But I could’ve sworn I heard something.”

[P37]
“You imagined it.”

[P38]
“Something might have happened at the Mount Heng Sword Sect.”

[P39]
“That’s possible. But I didn’t hear anything.”

[P40]
“But I’m telling you, I think I heard something.”

[P41]
“So I’m telling you that you imagined it.”

[P42]
“Based on what?”

[P43]
“It’s simple. There’s no way you heard something I couldn’t.”

[P44]
“…”

[P45]
That was incredibly irritating, but he was right, so I couldn’t argue.

[P46]
Seeing me at a loss for words, Jin Mukyung clicked his tongue.

[P47]
“If you don’t want to die to a stray blade, focus on keeping your mind and body under control. You never know what might happen on a battlefield.”

[P48]
*Look who’s lecturing whom.*

[P49]
When it came to combat experience, no one here could match me.

[P50]
I only looked the same as usual because I had grown so accustomed to it. When it came to preparing for and taking part in battle, I was already thoroughly battle-hardened.

[P51]
“There are a lot of enemies, so conserve as much internal energy as possible and keep your movements to a minimum. I’ll take the lead. Just follow me, and you’ll be fine.”

[P52]
*Was he worried about me because we shared the same blood?*

[P53]
Come to think of it, Mukyung had made his dislike painfully obvious, yet he had still helped me a great deal.

[P54]
He had helped with my training, agreed to accompany me to the Mount Heng Sword Sect, and, I’d heard, had even put considerable effort into reforming his lazy little brother when they were children.

[P55]
Even if Jin Wikyung had asked him to, he couldn’t have done all that if he truly hated me.

[P56]
*Maybe he’s actually a soft-hearted guy.*

[P57]
Was this what people called a tsundere?

[P58]
I gazed at Jin Mukyung sentimentally, almost feeling a little moved.

[P59]
Our eyes met.

[P60]
“What are you looking at? Eyes down.”

[P61]
“…”

[P62]
“If you take even a single wound from those mounted-bandit bastards, I’ll kill you myself.”

[P63]
“…Yeah, sure.”

[P64]
*That’s more like it. Tsundere, my ass.*

[P65]
I must have lost my mind for a moment to imagine something so ridiculous.

[P66]
Accepting reality, I was about to transfer my saddle to one of the spare horses we had taken earlier when Hyuk Mujin sidled over with a deeply worried expression.

[P67]
“Second Young Master, you aren’t going to kill me too, are you?”

[P68]
“…Are you saying it’s okay if I die?”

[P69]
“Ah, no! Why would you put it like that?”

[P70]
“I’ll make sure to kill you before I die, so shut up and get ready to leave.”

[P71]
I kicked Hyuk Mujin in the rear as he grumbled under his breath, then mounted my horse.

[P72]
The Mount Heng Sword Sect was still three shichen away.

[P73]
From here on, we had to ride hard without taking a single break.

[P74]
> **System**
> 
> **Time Limit:** 6:25:19

[P75]
* * *

[P76]
The Mount Heng Sword Sect was like a fortress. Its towering stone walls were sturdy enough to be called castle walls, and they were fitted with all manner of defensive structures for withstanding a siege.

[P77]
Built more than thirty years ago under the uncompromising will of the founding Sect Leader, Lee Cheonbaek, those defenses were finally serving their purpose.

[P78]
“Fire!”

[P79]
Whoosh—whoosh—whoosh!

[P80]
Dozens of arrows loosed in unison rained down on the charging cavalry.

[P81]
But the most common weapons in Gaoyuan were spears, sabers, and bows. Accustomed to fighting in Gaoyuan, the mounted bandits of the Red Wind Band raised the shields strapped to one arm before anyone even gave the order.

[P82]
Thud! Thump!

[P83]
Only a dozen or so men fell from their horses.

[P84]
The shields, made from bone-dry wood faced with hide from an old horse’s rump, stopped the arrows admirably.

[P85]
“Ha ha ha! These punks don’t know their elders when they see them, and they dare—!”

[P86]
That was when it happened.

[P87]
Fwoosh—crack!

[P88]
Something hurtled through the air with ferocious momentum, pierced the horse’s neck, and buried itself in the Captain’s chest.

[P89]
Having only just entered the early stages of First Rate, he stared at the arrow protruding from his chest as though he couldn’t believe it, then toppled over together with his prized horse.

[P90]
Several of the riders behind him lost formation and fell one after another.

[P91]
“Crossbows! Watch for the crossbows!”

[P92]
“Return fire!”

[P93]
Whoosh—whoosh—whoosh!

[P94]
If the Mount Heng Sword Sect’s attack had been a passing shower, the Red Wind Band’s barrage was a torrential downpour.

[P95]
Even on horseback, they drew and loosed without pause. Their arrows flew fast and true.

[P96]
Thwack! Thwack! Thwack!

[P97]
“Aaargh!”

[P98]
“Hide behind your shields! Don’t stick your heads out!”

[P99]
Taking advantage of the opening, the mounted bandits spurred their horses forward and set grappling hooks and makeshift ladders against the walls, which stood more than ten *jang* high. They began attempting to breach the fortress.

[P100]
A melee erupted atop the walls.

[P101]
Screams and blood burst forth.

[P102]
“Ha ha! Kill them all!”

[P103]
“Don’t let them climb up!”

[P104]
Lee Seowol watched it all from the highest watchtower. Her lips trembled, and the color had drained from her face.

[P105]
*So this is the Murim.*

[P106]
The screams of the dying. The desperate struggles of those who wanted to live.

[P107]
The world of the strong preying on the weak that she had finally encountered was more brutal and frightening than she had imagined.

[P108]
But…

[P109]
*I can’t retreat.*

[P110]
Countless people had already died. Those who were going to leave had left, while those who remained were fighting with their lives on the line.

[P111]
Lee Seowol was now the Sect Leader who had to lead them, and she was bound to share her fate with the Mount Heng Sword Sect.

[P112]
“Sect Leader! The walls are in danger! We need to send reinforcements!”

[P113]
“They’re breaking down the gate with a battering ram!”

[P114]
“Sect Leader! You must do something!”

[P115]
“Sect Leader!”

[P116]
As urgent reports rained down from every direction, Lee Seowol spoke.

[P117]
“When I give the signal, fire one fire arrow toward the walls and two toward the gate. And, Uncle Cheol.”

[P118]
Cheol Mubaek, who had been standing guard beside her, answered.

[P119]
“Tell me what you need.”

[P120]
“The gate will be breached soon. Can you buy us a little time?”

[P121]
“By myself?”

[P122]
“I can only apologize for making such a difficult request.”

[P123]
“One against a hundred. I’ve always wanted to try that.”

[P124]
“The uncle I know is a master who can face ten thousand men. Still, please be careful.”

[P125]
“All right. Do you really think those bastards could get the better of me?”

[P126]
Cheol Mubaek laughed heartily and leaped down.

[P127]
With the Tiger of Mount Heng—a consummate Peak master—guarding the gate, no one would get through unless Pung Yang himself stepped forward.

[P128]
*More. Just a little longer.*

[P129]
Lee Seowol gazed down at the fierce battle before suddenly shouting like a thunderclap.

[P130]
“Now!”

[P131]
The two martial artists who had been waiting for her command each drew their bowstrings.

[P132]
The next moment, the fire arrows soared into the darkening winter sky and shone brightly above everyone’s heads.

[P133]
* * *

[P134]
The fire arrows falling like meteors were clearly visible even to Pung Yang, more than a hundred *jang* away.

[P135]
He muttered to himself.

[P136]
*So they had a move hidden up their sleeve.*

[P137]
It didn’t take long for his guess to become certainty.

[P138]
A moment later, enormous flames erupted around the walls.

[P139]
Fwoosh! Fwoooosh!

[P140]
“Aaargh!”

[P141]
Burning alive was one of the most painful ways to die.

[P142]
The mounted bandits of the Red Wind Band, massed beneath the walls like a swarm of ants, writhed and screamed horribly.

[P143]
The ropes attached to the grappling hooks snapped, and the wooden ladders were engulfed in flames.

[P144]
“Attack!”

[P145]
“Kill every last one of those mounted-bandit bastards!”

[P146]
Those waiting below to climb and those still climbing burned to death, while those who had already reached the top were stabbed and slashed by weapons converging from every direction.

[P147]
“So they did make some preparations…”

[P148]
As Pung Yang stared impassively at the battlefield, a mounted bandit returned, his body blackened in patches like charcoal.

[P149]
“What happened?”

[P150]
“L-Leader. Our losses are too great!”

[P151]
The moment he reached Pung Yang, the mounted bandit threw himself flat on the ground and continued breathlessly.

[P152]
“From the first assault until now, at least a hundred men must have died. More importantly, after that fire attack, our brothers’ morale is…”

[P153]
“The gate?”

[P154]
“Pardon?”

[P155]
“What happened to the gate?”

[P156]
“We broke through, but the Tiger of Mount Heng, Cheol Mubaek, is holding it alone…”

[P157]
“Alone?”

[P158]
“Yes. His martial arts are so formidable that no one dares step forward.”

[P159]
“Then that’s enough.”

[P160]
As he spoke, Pung Yang held out his hand.

[P161]
The mounted bandit instinctively reached to take it, only for his body to tilt and collapse.

[P162]
A dagger was buried deep between his brows, his expression frozen in confusion.

[P163]
“How many troops do we have left?”

[P164]
The subordinate who served as Pung Yang’s right hand was accustomed to such sights. He glanced at the corpse and answered.

[P165]
“By a rough count, a little over a hundred and fifty but not quite two hundred. It’s true that our losses are heavier.”

[P166]
“How much worse do you think theirs are? The men on those walls are the Mount Heng Sword Sect’s final bulwark.”

[P167]
“You mean those few men are all they have left?”

[P168]
“Yes.”

[P169]
“It isn’t that I doubt you, Leader, but what if they have another trap like that fire attack…?”

[P170]
“That’s what they’re counting on.”

[P171]
Pung Yang let out a derisive laugh. He didn’t know whose strategy it had been, but they had played it quite cleverly.

[P172]
*If I had been less experienced, I would have suspected another trap and pulled our forces back.*

[P173]
*They’re struggling to buy time. Are they waiting for someone’s support?*

[P174]
If so, there was even less reason to hesitate.

[P175]
The few could not stand against the many. Even after suffering considerable losses, the Red Wind Band would have no trouble wiping out the Mount Heng Sword Sect.

[P176]
And besides…

[P177]
“I’m going myself.”

[P178]
“You’re going yourself, Leader?”

[P179]
“Yes. We have a tiger to catch, don’t we?”

[P180]
Pung Yang burst into a hearty laugh and felt inside his robes out of habit.

[P181]
A hard wooden case rested there.

[P182]
Inside was something that could bring down a tiger in one go.
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
# Chapter 113

[P2]
Half a shichen after sending an envoy to the Mount Heng Sword Sect, Pung Yang gave the order without hesitation.

[P3]
“Attack.”

[P4]
A quick, decisive battle.

[P5]
The longer it dragged on, the worse it would be for him. Word that the Red Wind Band had surrounded the Mount Heng Sword Sect would spread quickly, and if outside forces—especially the Jin Family of Taiyuan—intervened, things would become troublesome.

[P6]
*I never expected to enter without bloodshed in the first place.*

[P7]
She might be a woman, but she carried the blood of the Blood Wolf Sword, Lee Cheonbaek.

[P8]
If words and gestures couldn’t tame her, he would have to subdue her with violence. It was the same method Pung Yang had always used.

[P9]
Bwooooooong!

[P10]
The powerful sound of horns rang out from every direction. At the advance signal used by the mounted-bandit groups of the plateau, the mounted bandits surrounding the Mount Heng Sword Sect simultaneously kicked their horses in the ribs.

[P11]
“Chaaaarge!”

[P12]
“Kill every last one of them!”

[P13]
Thundering hooves shook the ground.

[P14]
Hundreds of horses raced forward, trampling the snow-covered earth.

[P15]
The horn calls continued without pause, strong and carrying far into the distance.

[P16]
* * *

[P17]
Ding!

[P18]
> **System**
> 
> **Circulate Qi** was successfully completed.
> 
> A small amount of Fatigue and Stamina has been restored.

[P19]
The moment I opened my eyes at the sound of the System notification, I looked around.

[P20]
“Did you guys just hear something?”

[P21]
Wolhwa and Hyuk Mujin, who had been feeding hay to the horses, looked at me in confusion.

[P22]
“Young Master Jin, what sound?”

[P23]
“Sounds are always happening. Listen. The horses chewing hay, the wind…”

[P24]
“Not that crap, you idiot.”

[P25]
“Then what?”

[P26]
“A-a vuvuzela?”

[P27]
“Vuvu… what?”

[P28]
“The thing people use to cheer at sporting events… Never mind. It’s something.”

[P29]
I gave up explaining and stared in the direction the sound had come from—or rather, the direction I thought it had come from.

[P30]
By coincidence, it was the north, where the Mount Heng Sword Sect lay—the very direction we were heading.

[P31]
*Did I hear it wrong?*

[P32]
According to Wolhwa, we still had to ride for another three shichen—six hours—before we could reach the Mount Heng Sword Sect. Whatever had happened, it wasn’t something that should have been audible from this distance.

[P33]
*Unless it was cannon fire.*

[P34]
Jin Mukyung, who had just finished circulating his qi, added his opinion.

[P35]
“I didn’t hear anything.”

[P36]
“But I could have sworn I heard something.”

[P37]
“You imagined it.”

[P38]
“Something might have happened at the Mount Heng Sword Sect.”

[P39]
“That’s possible. But I didn’t hear anything.”

[P40]
“But I’m telling you, I think I heard something.”

[P41]
“So I’m telling you that you imagined it.”

[P42]
“On what grounds?”

[P43]
“It’s simple. There’s no way I could fail to hear what you heard.”

[P44]
“…”

[P45]
That was incredibly irritating, but he was right, so I couldn’t argue.

[P46]
Seeing me rendered speechless, Jin Mukyung clicked his tongue.

[P47]
“If you don’t want to die to a stray blade, focus on mastering your mind and body. You never know what might happen on a battlefield.”

[P48]
*Look who’s lecturing whom.*

[P49]
When it came to combat experience, no one here could match me.

[P50]
I only seemed no different from usual because I had grown so accustomed to it. When it came to preparing for and taking part in battle, I was already thoroughly battle-hardened.

[P51]
“There are a lot of enemies, so conserve your internal energy as much as possible and minimize your movements. I’ll take the lead. Just follow me, and there won’t be a problem.”

[P52]
*Was he worried about me because we shared the same blood?*

[P53]
Come to think of it, Mukyung had made his dislike painfully obvious, yet he had still helped me a great deal.

[P54]
He had helped with my training, agreed to accompany me to the Mount Heng Sword Sect, and, I’d heard, had even made a considerable effort to reform his lazy little brother when they were children.

[P55]
Even if Jin Wikyung had asked him to, those weren’t things he could have done if he truly hated me.

[P56]
*Maybe he’s actually a soft-hearted guy.*

[P57]
Was this what people called a tsundere?

[P58]
I looked at Jin Mukyung with a sentimental gaze, feeling as though I might actually be moved.

[P59]
Our eyes met.

[P60]
“What are you looking at? Lower your eyes.”

[P61]
“…”

[P62]
“If you take even a single wound from those mounted-bandit bastards, I’ll kill you myself.”

[P63]
“…Yeah, sure.”

[P64]
*That’s more like it. Tsundere, my ass.*

[P65]
I had briefly lost my mind and imagined something ridiculous.

[P66]
Accepting reality, I was about to transfer my saddle to one of the spare horses we had taken earlier when Hyuk Mujin approached and spoke with a deeply worried expression.

[P67]
“Second Young Master, you aren’t going to kill me too, are you?”

[P68]
“…Are you saying it’s okay if I die?”

[P69]
“Ah, no! Why are you putting it that way?”

[P70]
“I’ll kill you before I die, so shut up and prepare to leave.”

[P71]
I kicked Hyuk Mujin in the rear while he grumbled under his breath, then mounted my horse.

[P72]
The Mount Heng Sword Sect was still three shichen away.

[P73]
From this point onward, we had to ride hard without taking a single break.

[P74]
> **System**
> 
> **Time Limit:** 6:25:19

[P75]
* * *

[P76]
The Mount Heng Sword Sect was like a fortress. The stone walls piled high around it were sturdy enough to be called castle walls, and all kinds of defensive facilities had been installed to hold the fortress.

[P77]
Built more than thirty years ago under the uncompromising will of the founding Sect Leader, Lee Cheonbaek, those defenses were finally serving their intended purpose.

[P78]
“Fire!”

[P79]
Whoosh—whoosh—whoosh!

[P80]
Dozens of arrows launched at once rained down on the charging cavalry.

[P81]
But the weapons most commonly found on the plateau were spears, swords, and bows. Accustomed to fighting on the plateau, the mounted bandits of the Red Wind Band raised the shields strapped to one arm before anyone even gave the order.

[P82]
Thud! Thump!

[P83]
Only a dozen or so men were knocked from their horses.

[P84]
The shields, made of bone-dry wood faced with hide from an old horse’s rump, did an excellent job of stopping the arrows.

[P85]
“Ha ha ha! These punks don’t know their elders when they see them, and they dare—!”

[P86]
That was when it happened.

[P87]
Fwoosh—crack!

[P88]
Something came flying with ferocious force. It pierced through a horse’s neck and buried itself in the squad leader’s chest.

[P89]
He had only just entered the early stages of First Rate. He stared at the arrow protruding from his chest as though he couldn’t believe it, then toppled over together with his prized horse.

[P90]
Several of the riders behind him lost formation and fell one after another.

[P91]
“Crossbows! Watch for the crossbows!”

[P92]
“Return fire!”

[P93]
Whoosh—whoosh—whoosh!

[P94]
If the Mount Heng Sword Sect’s attack had been a passing shower, the Red Wind Band’s arrow barrage was a torrential downpour.

[P95]
Even while mounted, they drew their bowstrings again and again. Their arrows were fast and accurate.

[P96]
Thwack! Thwack! Thwack!

[P97]
“Aaargh!”

[P98]
“Hide behind your shields! Don’t stick your heads out!”

[P99]
Taking advantage of the opening, the mounted bandits spurred their horses forward and set grappling hooks and makeshift ladders against the walls, which stood more than ten *jang* high. They began attempting to breach the fortress.

[P100]
A melee erupted atop the walls.

[P101]
Screams and blood poured forth.

[P102]
“Ha ha! Kill them all!”

[P103]
“Stop them from climbing up!”

[P104]
Lee Seowol watched the entire scene from the highest watchtower. Her lips trembled, and the color had drained from her face.

[P105]
*So this is the Murim.*

[P106]
The screams of those dying.

[P107]
The desperate struggles of those who wanted to live.

[P108]
The world of the strong preying on the weak that she had finally encountered was more brutal and frightening than she had imagined.

[P109]
But…

[P110]
*I can’t retreat.*

[P111]
Countless people had already died. Those who were going to leave had left, while those who remained were fighting with their lives on the line.

[P112]
Lee Seowol was now the Sect Leader who had to lead them. She was bound to share her fate with the Mount Heng Sword Sect.

[P113]
“Sect Leader! The walls are in danger! We need to send reinforcements!”

[P114]
“They’re breaking down the gate with a battering ram!”

[P115]
“Sect Leader! You need to take action!”

[P116]
“Sect Leader!”

[P117]
As urgent reports rained down from every direction, Lee Seowol opened her mouth.

[P118]
“When I give the signal, fire one fire arrow toward the walls and two toward the gate. And, Uncle Cheol.”

[P119]
Cheol Mubaek, who had been standing beside her, answered.

[P120]
“Tell me what you need.”

[P121]
“The gate will be breached soon. Can you buy us a little time?”

[P122]
“By myself?”

[P123]
“I’m sorry to ask you to do something so difficult.”

[P124]
“One against a hundred. I’ve always wanted to try that.”

[P125]
“The uncle I know is a master who can face ten thousand men. But please be careful.”

[P126]
“All right. Do you think those bastards can get the better of me?”

[P127]
Cheol Mubaek laughed heartily, then leaped down.

[P128]
With the Tiger of Mount Heng—a consummate Peak master—there, no one would be able to get through the gate unless Pung Yang himself stepped forward.

[P129]
*Just a little longer. A little more.*

[P130]
Lee Seowol watched the fierce battlefield below, then suddenly let out a thunderous shout.

[P131]
“Now!”

[P132]
The two martial artists who had been waiting for her command each drew their bowstrings.

[P133]
The next moment, the fire arrows soared into the darkening winter sky and shone brightly above everyone’s heads.

[P134]
* * *

[P135]
The fire arrows falling like meteors were clearly visible even to Pung Yang, who stood more than a hundred *jang* away.

[P136]
He thought to himself.

[P137]
*They had a hidden ace.*

[P138]
It didn’t take long for his suspicion to become certainty.

[P139]
A moment later, enormous flames erupted around the walls.

[P140]
Fwoosh! Fwoooosh!

[P141]
“Aaargh!”

[P142]
Burning to death was one of the most painful ways to die.

[P143]
The mounted bandits of the Red Wind Band, massed beneath the walls like a swarm of ants, writhed and screamed horribly.

[P144]
The ropes attached to the grappling hooks snapped, and the wooden ladders were engulfed in flames.

[P145]
“Attack!”

[P146]
“Kill every last one of those mounted-bandit bastards!”

[P147]
Those waiting below to climb and those still making their way up burned to death. Those who had already reached the top were stabbed and slashed by weapons converging from every direction.

[P148]
“So they did make some preparations…”

[P149]
As Pung Yang stared impassively at the battlefield, one of the mounted bandits came back with parts of his body blackened like charcoal.

[P150]
“What happened?”

[P151]
“L-Leader. The casualties are too high!”

[P152]
The moment he reached Pung Yang, the mounted bandit threw himself flat on the ground and continued in a breathless voice.

[P153]
“From the first assault until now, at least a hundred men must have died. More importantly, after that fire attack, our brothers’ morale is…”

[P154]
“The gate?”

[P155]
“Pardon?”

[P156]
“What happened to the gate?”

[P157]
“We broke through, but the Tiger of Mount Heng, Cheol Mubaek, is holding it alone…”

[P158]
“Alone?”

[P159]
“Yes. His martial arts are so formidable that no one dares step forward.”

[P160]
“Then it’s settled.”

[P161]
At the same time, Pung Yang held out his hand.

[P162]
The mounted bandit instinctively reached to take it, only for his body to list and collapse.

[P163]
A dagger was buried deep between his brows.

[P164]
“How many troops do we have left?”

[P165]
This sort of scene was familiar to the subordinate who served as Pung Yang’s right hand. After glancing at the corpse, he answered.

[P166]
“By a rough count, somewhere between a little over a hundred and fifty and just under two hundred. It’s true that our losses are greater.”

[P167]
“Then imagine theirs. The men on those walls are the Mount Heng Sword Sect’s final bulwark.”

[P168]
“You mean those few men are all they have left?”

[P169]
“Yes.”

[P170]
“I’m not doubting you, Leader, but couldn’t there be another trap like that fire attack?”

[P171]
“That’s what they’re counting on.”

[P172]
Pung Yang let out a derisive laugh. He didn’t know whose strategy it had been, but they had played it quite cleverly.

[P173]
*If I had been less experienced, I would have suspected another trap and pulled our forces back.*

[P174]
*They’re struggling to buy time. Are they waiting for someone’s support?*

[P175]
If so, there was even less reason to hesitate.

[P176]
The few couldn’t stand against the many. Even if the Red Wind Band had suffered considerable losses, wiping out the Mount Heng Sword Sect would be easy.

[P177]
And besides…

[P178]
“I’m going myself.”

[P179]
“You’re going yourself, Leader?”

[P180]
“Yes. We have to catch the tiger, don’t we?”

[P181]
Pung Yang burst into a hearty laugh and habitually felt inside his robes.

[P182]
A hard wooden case rested there.

[P183]
Inside was something that could bring down a tiger in one go.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 월화     | **Wolhwa**         |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 마적     | **mounted bandits**                              |                                                       |
| 문주     | **Sect Leader**                              |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 체력               | **Stamina**                    |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 공자      | **Young Master**                                                |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 113,
  "passed": true,
  "metrics": {
    "source_characters": 5435,
    "translation_characters": 12284,
    "length_ratio": 2.26,
    "source_paragraphs": 170,
    "translation_paragraphs": 182
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "운기조식",
        "preferred": "circulate one's qi"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "상태",
        "preferred": "Status"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "고자",
        "preferred": "eunuch"
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
