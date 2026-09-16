# Fidelity Gate — Chapter 101

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
  1|＃101화
  2|
  3|
  4|
  5|‘뭐야, 이거.’
  6|
  7|어안이 벙벙했다. 김 집사의 등장도 뜻밖이지만 그가 임춘수를 향해 건넨 말에 비하면 아무것도 아니다.
  8|
  9|‘춘수? 자네?’
 10|
 11|두 사람 아는 사이였어?
 12|
 13|생각해 보면 김 집사와 임춘수는 공통점이 많았다. 나이도 엇비슷하고 헌터 경력도 오래됐다.
 14|
 15|‘그러고 보니 김 집사도 대격변 때 헌터로 활동했지.’
 16|
 17|당사자의 입으로 직접 들은 건 아니지만 내심 짐작하고 있었던 사실이다. 두 사람을 번갈아 쳐다보던 나는 조심스럽게 물었다.
 18|
 19|“두 분, 친하세요?”
 20|
 21|임춘수의 눈동자가 파르르 떨렸다.
 22|
 23|
 24|
 25|* * *
 26|
 27|
 28|
 29|처음 평화 길드에 관한 보고서를 받았을 때, 임춘수는 자신의 눈을 의심했다.
 30|
 31|흐릿한 기억 속에 남아 있는 얼굴, 다시는 볼 수 없을 거라 확신했던 얼굴이 보고서 속 사진에 있었기 때문이었다.
 32|
 33|
 34|
 35|‘이, 이 자가 누구라고?’
 36|
 37|‘평화 길드 마스터 김화종. 나이는 55세. B급 헌터입니다.’
 38|
 39|‘김화종? B급 헌터?’
 40|
 41|‘예. 혹시 무슨 문제라도?’
 42|
 43|‘아, 아니야. 전에 알던 사람이랑 닮아서 착각했어.’
 44|
 45|
 46|
 47|그럼 그렇지. 임춘수는 안도의 한숨을 내쉬었다.
 48|
 49|얼굴이 약간 닮긴 했지만 그것뿐이다. 무엇보다 그자는 이미 30여 년 전 죽지 않았나.
 50|
 51|아무리 세상이 요지경이 됐다지만 죽은 자가 살아 돌아올 수는 없다.
 52|
 53|‘설령 그 인간이 살아 돌아왔어도 이런 곳에서 썩고 있진 않겠지. 늙다리 B급 헌터랑 착각한 것뿐이야.’
 54|
 55|그날, 임춘수는 오랜만에 소주를 한 잔 걸치며 찜찜한 마음을 털어 냈다. 50이 넘도록 그의 발목을 붙잡고 있는 끔찍한 기억들을 떨치려는 시도였다.
 56|
 57|‘어후, 이 나이 먹고도 아직 이러고 있다니.’
 58|
 59|이후 김화종의 정보에 철통같은 보안이 걸려 있다는 얘길 들었을 때는 등줄기가 서늘하기까지 했었다.
 60|
 61|‘설마? 아냐. 그럴 리가 없지.’
 62|
 63|하지만…… 왜 불길한 예감은 틀리는 법이 없을까?
 64|
 65|“솟구쳐라. 파이어 월.”
 66|
 67|주문을 영창하는 나직한 목소리가 들림과 동시에 솟아오른 불의 장벽.
 68|
 69|화륵, 화아악!
 70|
 71|초고온의 청염(靑炎)이 강철보다 단단한 얼음송곳을 흔적도 없이 증발시켰다.
 72|
 73|그리고…….
 74|
 75|“늦지 않아서 다행입니다. 춘수, 자네도.”
 76|
 77|꿈에서도 잊을 수 없던 목소리를 듣는 순간, 임춘수는 떠올렸다. 놈에게 지배당했던 공포를. 살기 위해 굴렀던 굴욕을.
 78|
 79|‘시발…… 좆 됐다.’
 80|
 81|돌처럼 굳은 그에게 진태경이 묻는다.
 82|
 83|“두 분, 친하세요?”
 84|
 85|뭐? 친하냐고?
 86|
 87|임춘수는 폐부 깊숙한 곳에서 올라오려는 쌍욕을 꿀꺽 삼키고 돌아섰다. 오래전 죽었다고 생각했던 한 사람이 그곳에 있었다.
 88|
 89|“교, 교관님.”
 90|
 91|김 집사가 부드럽게 웃었다. 시간이 흐른 지금까지도 임춘수의 뇌리 깊숙이 새겨진 악마의 웃음.
 92|
 93|“28연대 1대대 2중대. 임춘수. 그래, 처음 보자마자 알았지.”
 94|
 95|그것은 영혼의 울림이었다.
 96|
 97|임춘수의 구부정했던 허리가 펴지고 바짝 붙인 발은 45도. 시선은 전방 15도 위를 향한다.
 98|
 99|번개처럼 빠른 동작 끝에 천둥 같은 외침이 터져 나왔다.
100|
101|“1번 훈련생! 이임! 추운! 수우!”
102|
103|30년 만에 외치는 관등성명에 산이 들썩였다.
104|
105|
106|
107|* * *
108|
109|
110|
111|산 위로 올라간 1팀장이 발견한 것은 핏물이 군데군데 튄 풀숲과 마법 밧줄로 꽁꽁 묶인 보안팀이었다.
112|
113|‘정말 가관이군, 가관이야.’
114|
115|내심 혀를 찬 그가 검을 꺼내 밧줄을 끊었다.
116|
117|다들 피는 좀 흘렸어도 심각한 부상을 입은 것 같아 보이지는 않는다. 진태경이라는 놈이 최소한의 신경은 써 준 모양이었다.
118|
119|‘이 정도면 B급 최상위. 혹은 A급 헌터.’
120|
121|1팀장의 판단으로 진태경의 실력은 그 정도 되는 듯했다.
122|
123|그 후 산에서 내려오는 길은 누군가에게는 지옥 같은 시간이었다.
124|
125|“왜 그랬습니까? 감시 정도야 어떻게 넘기겠지만 오늘 일은 살인미수까지 갈 수도 있어요. 뒷일은 생각하고 일을 벌인 겁니까?”
126|
127|“……죄송합니다.”
128|
129|1팀장의 말에 보안팀장이 고개를 푹 숙였다.
130|
131|무리수까지 둬 가며 무력행사에 나섰는데 도리어 진태경에게 탈탈 털렸다. 입이 열 개라도 할 말이 없는 상황이다.
132|
133|“길드장님께서 단단히 실망하셨습니다.”
134|
135|“그, 그럼?”
136|
137|“시말서에 감봉은 당연한 거고 그 이상까지 각오해 두세요.”
138|
139|“사직, 입니까?”
140|
141|“그거야 길드장님 뜻에 달린 거죠.”
142|
143|“……저, 팀장님. 혹시.”
144|
145|“미리 말해 두는데, 괜한 청탁 같은 건 하지 않길 바랍니다. 내가 다니는 직장 이름에 똥칠한 사람을 편드는 취미는 없어서요. 길드장님 뜻에 반대할 생각도 없고.”
146|
147|“…….”
148|
149|“후우.”
150|
151|1팀장이 짜증 섞인 한숨을 내쉰 그때였다.
152|
153|저 멀리서 울려 퍼지는 쩌렁쩌렁한 외침.
154|
155|- 1번 훈련생! 이임! 추운! 수우!
156|
157|“……?”
158|
159|“……?”
160|
161|뭐지? 환청인가?
162|
163|1팀장은 물론이고 죽을상을 하고 있던 보안팀원들까지 화들짝 놀랐다. 가장 먼저 정신을 수습한 건 보안팀장이었다.
164|
165|“저기, 1팀장님. 이런 분위기에서 죄송합니다만, 방금 길드장님 목소리를 들은 것 같은데요.”
166|
167|귀를 후비고 있던 1팀장이 눈을 동그랗게 떴다.
168|
169|“……보안팀장도 들었어요?”
170|
171|“저희도 들었는데요.”
172|
173|“근데 길드장님 목소리인지는 잘 구분을 못 하겠고…… 성함은 들은 것 같습니다.”
174|
175|“그게 사람 이름이었어? 난 그냥 악쓰는 소리 같던데.”
176|
177|“그런가? 나는 관등성명 대는 것처럼 들렸는데.”
178|
179|보안팀의 쑥덕거림을 듣던 1팀장이 정색했다.
180|
181|“방금 말한 사람 누굽니까? 뭐, 관등성명?”
182|
183|그에게 있어 임춘수는 존경하는 선배이자 상관이었다.
184|
185|대격변 때부터 활동한 불세출의 헌터이자 전쟁 영웅이 난데없이 관등성명이라니?
186|
187|상상한 적도 없고 상상할 수도 없다.
188|
189|“아직도 그런 헛소리를 할 여유가 있습니까? 이게 도대체 정신이 똑바로 박힌 사람들이 할 얘기냔 말이야!”
190|
191|“죄, 죄송합니다.”
192|
193|“저희가 잘못 들은 것 같습니다.”
194|
195|“다들 정신 똑바로 차려요. 알겠습니까?”
196|
197|으름장을 놓은 1팀장이 다시 걸음을 뗀 그 순간이었다.
198|
199|- 아닙니다아아악!
200|
201|“…….”
202|
203|- 시정하겠습니다아악!
204|
205|“…….”
206|
207|그것은 영혼이 실린 이등병의 외침.
208|
209|꾹 닫혀 있던 1팀장의 입이 열린 것은 잠시 후였다.
210|
211|“지금부터 전속력으로 뛰어간다. 실시.”
212|
213|“시, 실시!”
214|
215|이 자리에 모인 이들은 최소 C급 헌터. 이미 일반인의 한계를 훌쩍 뛰어넘은 초인들이다.
216|
217|폭주 기관차처럼 내달린 그들은 5분이 채 지나기도 전에 등산로 입구에 도착했다.
218|
219|“느려 터졌군. 이제야 왔나?”
220|
221|“길드장님!”
222|
223|“목소리 줄여, 귀청 떨어져.”
224|
225|여느 때와 다름없는 임춘수의 모습에 1팀장이 안도의 한숨을 내쉬었다.
226|
227|“전 또 혹시 무슨 일이 난 줄 알고…….”
228|
229|“일이라니? 뭐 이상한 일 있었나?”
230|
231|“아, 아닙니다. 그런데 진태경 그놈은 어디 갔습니까?”
232|
233|“적당히 타일러서 보냈어. 이야기를 나눠 보니 생각보다 괜찮은 놈이더군. 그런데 왜?”
234|
235|“놈이 무슨 소란을 피웠나 해서요.”
236|
237|“아, 혹시 아까 어떤 놈이 소리 지른 거 말하는 거야?”
238|
239|“네, 맞습니다. 그런데 목소리가 꼭…….”
240|
241|길드장님 같아서요. 차마 뒷말을 잇지 못하는 1팀장을 향해 임춘수가 눈을 부라렸다.
242|
243|“목소리가 뭐?”
244|
245|“아, 아무것도 아닙니다.”
246|
247|“싱겁기는. 새파란 놈들이 저 아래서 군대놀이 하길래 쫓아내고 왔다. 아니, 요즘도 대학에 군기 문화가 있어?”
248|
249|“아, 그렇군요.”
250|
251|“거 뭐야. PT 체조로 잠깐 굴렸더니 아주 죽으려고 하데?”
252|
253|1팀장은 마음에 품고 있던 의혹이 말끔하게 사라지는 것을 느꼈다.
254|
255|‘내가 미쳤던 거지. 감히 무슨 생각을.’
256|
257|그가 한쪽에서 마음 깊이 반성하고 있을 때 임춘수는 보안팀을 탈탈 털고 있었다.
258|
259|“보안팀장.”
260|
261|“예, 옛!”
262|
263|“어쭈. 대답은 잘하네. 이런 일을 벌이고도 아직 팀장은 팀장이라 이건가?”
264|
265|“죄, 죄송합니다!”
266|
267|“다른 놈들은 잘해서 입 다물고 있나? 오늘 칼춤 한번 춰?”
268|
269|“죄송합니다, 길드장님!”
270|
271|1팀장은 흐뭇하게 웃으며 그 광경을 지켜봤다.
272|
273|간혹 임춘수의 성격이 지랄 맞다는 유언비어를 퍼트리는 놈들이 있다. 그러나 직접 옆에서 지켜본 그는 카리스마가 뛰어난 상관이며 훌륭한 인생의 선배였다.
274|
275|‘길드장님. 영원히 따르겠습니다.’
276|
277|무한한 존경의 눈빛으로 임춘수의 뒷모습을 바라보던 1팀장이 문득 고개를 갸웃했다.
278|
279|‘……그런데 왜 길드장님 등에 흙이 묻어 있지?’
280|
281|애들을 좀, 격하게 혼내셨나 보다.
282|
283|
284|
285|* * *
286|
287|
288|
289|“도착했습니다.”
290|
291|김 집사의 말에 조수석에 앉아 있던 나는 화들짝 정신을 차리며 주변을 두리번거렸다. 창밖으로 아파트 입구가 보였다. 언제 여기까지 왔지?
292|
293|“가, 감사합니다.”
294|
295|“별말씀을요.”
296|
297|멋있게 주름진 얼굴에 미소가 떠오른다. 왕년에 한 시대를 주름잡던 중년 배우가 생각나는 모습이다.
298|
299|‘아니, 이 사람도 한 시대를 주름잡긴 했구나.’
300|
301|지금까지는 그저 까마득한 선배 헌터 정도로 생각했는데, 그건 김 집사를 몰라도 한참 몰랐던 거다.
302|
303|‘A급 마법사를, 그것도 임춘수를 개처럼 굴리다니.’
304|
305|옛 전쟁 영웅한테 PT 8번 100세트를 시키더니, 나중에는 구둣발로 쪼인트를 깠다. 나긋나긋한 목소리로 임춘수를 갈구던 모습은 지금 생각해도 소름 그 자체다.
306|
307|
308|
309|‘훈련생, 누가 PT 체조에 마나를 씁니까?’
310|
311|빡!
312|
313|‘1번 훈련생 임춘수. 죄, 죄송합니다.’
314|
315|‘아픕니까? 나이 먹더니 목소리도 작아진 겁니까?’
316|
317|‘아닙니다아아악!’
318|
319|‘차렷. 열중쉬어. 차렷. 열중쉬어.’
320|
321|파바바바박!
322|
323|‘뒤로 취침. 앞으로 취침. 뒤로 취침. 뒤로 취침.’
324|
325|‘헉.’
326|
327|‘훈련생, 본 교관이 뒤로 취침이라고 하는 말 못 들었습니까? 정신 똑바로 차립니다.’
328|
329|‘시정하겠습니다아악!’
330|
331|‘그리고 왜 선량한 후배를 괴롭힙니까? 본 교관이 누누이 강조하지 않았습니까. 선후배끼리 서로 도우며 살라고.’
332|
333|‘죄, 죄송합니다.’
334|
335|‘복명복창합니다. 앉으면서 후배를, 일어나면서 아끼자. 하나. 둘.’
336|
337|‘후배를, 아끼자!’
338|
339|‘훈련생, 25기로 기억하는데 맞습니까?’
340|
341|‘1번 훈련생 임춘수. 예, 그렇습니다.’
342|
343|‘본 교관은 3기입니다. 만약 오늘 있었던 일이 밖으로 새어 나가거나 다시 반복된다면 4기부터 24기까지 열외 없이 집합입니다.’
344|
345|‘…….’
346|
347|‘왜 대답이 없습니까. 쪼그려 뛰기 준비.’
348|
349|‘주, 준비…….’
350|
351|
352|
353|굴리고, 굴리고, 또 굴리고.
354|
355|그야말로 돈 주고도 못 보는 광경. 만약 상동 길드원들이 봤다면 오늘 부로 길드 문 닫을 뻔했다.
356|
357|‘김 집사, 이 양반 도대체 정체가 뭐야?’
358|
359|헌터 훈련소 3기면 전국 길드장들을 연병장에 모아 놓고 줄 빠따를 쳐도 된다. 게다가 무려 교관 출신이라니.
360|
361|어지간한 대격변 초창기 마법사들은 전부 그의 손을 거쳤다고 해도 과언이 아니다.
362|
363|‘마법사로서의 역량도 최소 A급.’
364|
365|임춘수가 찍소리도 못하고 얼차려를 당하는 것만 봐도 알 수 있다. 김 집사가 짬으로도, 실력으로도 앞선다.
366|
367|얼음과 화염. 마법의 상성도 있겠지만 임춘수를 가르쳐서 지금의 위치까지 오르게 한 것도 김 집사라고 볼 수 있다.
368|
369|‘그런데…….’
370|
371|그 정도씩이나 되는 사람이 왜 집사 노릇을 하고 있냐 이거지. 슬쩍 김 집사를 곁눈질하다가 시선이 딱 부딪쳤다.
372|
373|“묻고 싶은 게 많아 보이는군요.”
374|
375|“솔직히 말씀드리면 그렇습니다.”
376|
377|궁금해서 도저히 못 참겠다.
378|
379|생각이 고스란히 드러나는 내 표정에 김 집사가 입꼬리를 말아 올렸다.
380|
381|“말하자면 깁니다.”
382|
383|“괜찮습니다. 휴가 중이라 시간 넉넉해요.”
384|
385|“아, 그럼 이참에 진태경 씨 얘기도 들을 수 있겠군요. 안 그래도 궁금한 점이 한두 가지가 아닌데.”
386|
387|“생각해 보니까 벌써 저녁 시간이네요. 내일은 휴가 마지막 날이라 부동산 계약도 해야 하고. 허허허.”
388|
389|“…….”
```

## Assembled English

```markdown
[P1]
# Chapter 101

[P2]
*What the hell is this?*

[P3]
I was dumbfounded. Butler Kim’s appearance was unexpected, but that was nothing compared to the words he had directed at Im Chunsoo.

[P4]
*Chunsoo? You?*

[P5]
*Did these two know each other?*

[P6]
Come to think of it, Butler Kim and Im Chunsoo had a lot in common. They were around the same age, and both had long careers as Hunters.

[P7]
*Now that I think about it, Butler Kim was active as a Hunter during the Great Cataclysm, too.*

[P8]
I had never heard it directly from him, but I had suspected as much. Looking back and forth between the two men, I carefully asked,

[P9]
“Are you two close?”

[P10]
Im Chunsoo’s pupils quivered.

[P11]
* * *

[P12]
When Im Chunsoo first received the report on the Peace Guild, he had doubted his own eyes.

[P13]
There, in the photograph, was a face from his hazy memories—a face he had been certain he would never see again.

[P14]
*Wh-who did you say this man was?*

[P15]
*Peace Guild Master Kim Hwajong. He’s fifty-five years old and a B-rank Hunter.*

[P16]
*Kim Hwajong? A B-rank Hunter?*

[P17]
*Yes. Is something wrong?*

[P18]
*No, no. He looks like someone I used to know. I mistook him for that person.*

[P19]
*That figures.*

[P20]
Im Chunsoo let out a sigh of relief.

[P21]
The face did resemble him a little, but that was all. More importantly, hadn’t that man died over thirty years ago?

[P22]
No matter how bizarre the world had become, the dead could not come back to life.

[P23]
*Even if that bastard had come back to life, he wouldn’t be rotting away in a place like this. I simply mistook him for some washed-up old B-rank Hunter.*

[P24]
That day, Im Chunsoo drank a glass of soju for the first time in a long while and tried to shake off his uneasy feelings. It was an attempt to cast off the terrible memories that had clung to his ankles even after he turned fifty.

[P25]
*Damn. I’m this old, and I’m still like this.*

[P26]
Later, when he heard that Kim Hwajong’s information was protected by airtight security, he had even felt a chill run down his spine.

[P27]
*Could it be? No. There’s no way.*

[P28]
But then… why did ominous premonitions never turn out to be wrong?

[P29]
“Rise up. Fire Wall.”

[P30]
A quiet voice chanting a spell rang out, and a wall of fire surged upward.

[P31]
*Fwoosh! Fwoosh!*

[P32]
Blue flames burning at an extreme temperature vaporized the ice spikes, which were harder than steel, without leaving a trace.

[P33]
And then—

[P34]
“I’m glad I’m not too late. You too, Chunsoo.”

[P35]
The moment he heard the voice he could never forget, not even in his dreams, Im Chunsoo remembered.

[P36]
The terror of being under that man’s thumb.

[P37]
The humiliation of rolling around on the ground just to survive.

[P38]
*Fuck… I’m screwed.*

[P39]
As he stood frozen like a stone, Jin Taekyung asked him,

[P40]
“Are you two close?”

[P41]
What? *Close?*

[P42]
Im Chunsoo swallowed the torrent of curses rising from deep in his lungs and turned around.

[P43]
There stood the man he had believed long dead.

[P44]
“I-Instructor.”

[P45]
Butler Kim smiled gently. It was the smile of a demon still deeply engraved in Im Chunsoo’s mind, even after all these years.

[P46]
“Twenty-eighth Regiment, First Battalion, Second Company. Im Chunsoo. Yes, I recognized you the moment I saw you.”

[P47]
The words resonated in his very soul.

[P48]
Im Chunsoo’s hunched back straightened. His heels came together at a forty-five-degree angle, and his gaze turned fifteen degrees upward toward the front.

[P49]
After a series of movements as fast as lightning, a thunderous shout burst out.

[P50]
“Trainee Number One! Im! Chun! Soo!”

[P51]
The mountain shook as he bellowed out his military identification for the first time in thirty years.

[P52]
* * *

[P53]
When Team Leader 1 reached the top of the mountain, he found grass splattered with blood in several places and the Security Team trussed up in magical ropes.

[P54]
*What a disgraceful sight.*

[P55]
Clicking his tongue inwardly, he drew his sword and cut them loose.

[P56]
They had all shed some blood, but none of them appeared seriously injured. Jin Taekyung seemed to have shown them at least the bare minimum of consideration.

[P57]
*At this level, he’s either a top-tier B-rank… or an A-rank Hunter.*

[P58]
That was Team Leader 1’s assessment of Jin Taekyung’s strength.

[P59]
For one man, the walk back down the mountain was sheer hell.

[P60]
“Why did you do it? We might have been able to smooth over the surveillance, but what happened today could amount to attempted murder. Did you even consider the consequences before resorting to violence?”

[P61]
“…I’m sorry.”

[P62]
At Team Leader 1’s words, the Security Team Leader hung his head.

[P63]
He had gone so far as to make a reckless show of force, only to have Jin Taekyung wipe the floor with them. Even if he had ten mouths, he would have had nothing to say.

[P64]
“The Guild Master is deeply disappointed.”

[P65]
“Th-then?”

[P66]
“A written apology and a pay cut are a given. Be prepared for worse.”

[P67]
“Are you talking about resignation?”

[P68]
“That’s up to the Guild Master.”

[P69]
“Team Leader, perhaps…”

[P70]
“Let me tell you up front: don’t ask me for any favors. I don’t have any interest in taking the side of someone who smeared the name of the company I work for. And I have no intention of going against the Guild Master’s wishes.”

[P71]
“…”

[P72]
“Whew.”

[P73]
Team Leader 1 let out an irritated sigh.

[P74]
That was when a booming shout echoed from far away.

[P75]
—Trainee Number One! Im! Chun! Soo!

[P76]
“……”

[P77]
“……”

[P78]
What was that? Were they hearing things?

[P79]
Team Leader 1 and even the Security Team members, who had all looked ready to die, jumped in surprise. The first to recover his composure was the Security Team Leader.

[P80]
“Team Leader 1, I’m sorry to bring this up in this kind of atmosphere, but I think I just heard the Guild Master’s voice.”

[P81]
Team Leader 1, who had been cleaning out his ears, opened his eyes wide.

[P82]
“…You heard it too?”

[P83]
“We heard it, too.”

[P84]
“We couldn’t tell whether it was the Guild Master’s voice, though… I think we heard his name.”

[P85]
“That was a person’s name? I thought it was just someone screaming.”

[P86]
“Really? I thought it sounded like someone giving their name and rank.”

[P87]
Team Leader 1’s face hardened as he listened to the Security Team whispering among themselves.

[P88]
“Who just said that? What was that about giving a name and rank?”

[P89]
To him, Im Chunsoo was a respected Senior as well as his superior.

[P90]
He was a peerless Hunter who had been active since the Great Cataclysm—a war hero. And they were saying he had suddenly reported his military identification?

[P91]
Team Leader 1 had never imagined such a thing. He *couldn’t* imagine it.

[P92]
“Do you still have the leisure to spout this kind of nonsense? Do you think this is something people in their right minds would say?”

[P93]
“S-sorry.”

[P94]
“We must have misheard.”

[P95]
“Get a grip, all of you. Understood?”

[P96]
Team Leader 1 had just resumed walking after delivering the warning when it happened again.

[P97]
—No, sirrrrr!

[P98]
“……”

[P99]
—I’ll correct it, sirrrr!

[P100]
“……”

[P101]
It was the soul-deep roar of a private second class.

[P102]
A moment later, Team Leader 1’s tightly sealed mouth finally opened.

[P103]
“From this moment on, we run at full speed. Move!”

[P104]
“M-Move!”

[P105]
Everyone gathered there was at least a C-rank Hunter. They were superhuman beings who had already far surpassed the limits of ordinary people.

[P106]
They thundered downhill like runaway locomotives and reached the hiking-trail entrance in under five minutes.

[P107]
“Slow as hell. You’re only getting here now?”

[P108]
“Guild Master!”

[P109]
“Keep it down. You’ll burst my eardrums.”

[P110]
Team Leader 1 sighed in relief when he saw Im Chunsoo looking the same as ever.

[P111]
“I thought something might have happened…”

[P112]
“Something? Was there anything strange?”

[P113]
“N-no, sir. But where did that Jin Taekyung bastard go?”

[P114]
“I gave him a talking-to and sent him on his way. After speaking with him, I found out he was a better fellow than I expected. Why?”

[P115]
“I thought he might have caused some kind of disturbance.”

[P116]
“Oh, you mean the guy who was shouting earlier?”

[P117]
“Yes, that’s right. But the voice sounded exactly…”

[P118]
He couldn’t bring himself to finish.

[P119]
*Exactly like yours, Guild Master.*

[P120]
Im Chunsoo glared at him.

[P121]
“Exactly like what?”

[P122]
“Oh, it was nothing.”

[P123]
“How bland. Some greenhorns were playing army down there, so I chased them away. Do colleges still have hazing culture these days?”

[P124]
“Ah, I see.”

[P125]
“What was it? I made them do some PT exercises for a while, and they looked ready to die.”

[P126]
Team Leader 1 felt the suspicions he had been harboring vanish completely.

[P127]
*I must have been out of my mind. How dare I even think such a thing?*

[P128]
While he reflected deeply on his mistake, Im Chunsoo laid into the Security Team.

[P129]
“Security Team Leader.”

[P130]
“Y-yes, sir!”

[P131]
“Well, look at that. You certainly know how to answer. After causing this mess, are you still a Team Leader just because you’re technically still a Team Leader?”

[P132]
“I’m sorry, Guild Master!”

[P133]
“Are the others keeping their mouths shut because they did such a good job? Do you want me to make my sword dance today?”

[P134]
“We’re sorry, Guild Master!”

[P135]
Team Leader 1 watched the scene with a pleased smile.

[P136]
Every so often, there were people who spread the rumor that Im Chunsoo had a godawful personality. But after watching him up close, Team Leader 1 knew better. He was a charismatic superior and an outstanding Senior in life.

[P137]
*Guild Master. I’ll follow you forever.*

[P138]
As he gazed at Im Chunsoo’s back with boundless respect, Team Leader 1 suddenly cocked his head.

[P139]
*…But why is there dirt on the Guild Master’s back?*

[P140]
He must have scolded those kids rather intensely.

[P141]
* * *

[P142]
“We’ve arrived.”

[P143]
At Butler Kim’s words, sitting in the passenger seat, I came to my senses with a start and looked around. Through the window, I could see the entrance to an apartment complex.

[P144]
*When did we get here?*

[P145]
“Th-thank you.”

[P146]
“Don’t mention it.”

[P147]
A smile appeared on his handsomely lined face. He looked like a middle-aged actor who had once ruled an era.

[P148]
*No, this man really did rule an era, too.*

[P149]
Until now, I had thought of him as nothing more than a Senior Hunter from a distant generation. But that meant I hadn’t understood Butler Kim at all.

[P150]
*He worked an A-rank mage like a dog—and Im Chunsoo, no less.*

[P151]
He had made a former war hero do a hundred sets of PT Exercise No. 8, then later kicked him in the shin with his dress shoe. Even now, the way he had calmly berated Im Chunsoo in that gentle voice sent chills down my spine.

[P152]
*Trainee, who uses mana during PT exercises?*

[P153]
*Whack!*

[P154]
*Trainee Number One Im Chunsoo. S-sorry, sir.*

[P155]
*Does it hurt? Now that you’ve gotten older, has your voice gotten quieter, too?*

[P156]
*No, sirrrrr!*

[P157]
*Attention. At ease. Attention. At ease.*

[P158]
*Snap-snap-snap-snap!*

[P159]
*On your backs. On your fronts. On your backs. On your backs.*

[P160]
*Gasp.*

[P161]
*Trainee, didn’t you hear this Instructor say on your backs? Get your head straight.*

[P162]
*I’ll correct it, sirrrr!*

[P163]
*And why are you bullying an innocent junior? Hasn’t this Instructor told you time and again that Seniors and juniors should help each other?*

[P164]
*S-sorry, sir.*

[P165]
*Repeat after me. Cherish your junior on the way down. Cherish your junior on the way up. One. Two.*

[P166]
*Cherish my junior!*

[P167]
*Trainee, I remember you’re Class 25. Am I right?*

[P168]
*Trainee Number One Im Chunsoo. Yes, sir.*

[P169]
*This Instructor is Class 3. If what happened today gets out or happens again, Classes 4 through 24 will assemble without exception.*

[P170]
*…*

[P171]
*Why aren’t you answering? Prepare for squat jumps.*

[P172]
*P-prepare, sir…*

[P173]
He worked him over, and over, and over again.

[P174]
It was the kind of sight you couldn’t see even if you paid for it. If the Sangdong Guild members had witnessed it, the Guild might have had to close its doors that very day.

[P175]
*Who the hell is Butler Kim, really?*

[P176]
Being Class 3 at the Hunter Training Center meant he could line up every Guild Master in the country on a parade ground and beat every last one of them with a bat.

[P177]
And he had been an Instructor, no less.

[P178]
It wouldn’t be an exaggeration to say that nearly every mage from the early days of the Great Cataclysm had passed through his hands.

[P179]
*He’s at least A-rank as a mage, too.*

[P180]
I could tell just by watching Im Chunsoo take his punishment without daring to make a peep. Butler Kim surpassed him in both seniority and skill.

[P181]
There was probably also an elemental advantage between ice and fire. You could say Butler Kim was the one who taught Im Chunsoo and raised him to his current position.

[P182]
*But…*

[P183]
Why was someone that accomplished working as a butler?

[P184]
I stole a sidelong glance at Butler Kim, only for our eyes to meet.

[P185]
“You seem to have a lot you want to ask.”

[P186]
“To be honest, I do.”

[P187]
My curiosity was killing me.

[P188]
Seeing my thoughts written plainly across my face, Butler Kim curled up the corners of his mouth.

[P189]
“It’s a long story.”

[P190]
“That’s fine. I’m on vacation, so I have plenty of time.”

[P191]
“Ah, then this is a good opportunity to hear your story as well, Mr. Jin. I already have more than one or two questions myself.”

[P192]
“Now that I think about it, it’s already dinnertime. Tomorrow is the last day of my vacation, so I have to sign a real-estate contract, too. Hahaha.”

[P193]
“……”
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
# Chapter 101

[P2]
*What the hell is this?*

[P3]
I was dumbfounded. Butler Kim’s appearance was unexpected, but that was nothing compared to the words he had directed at Im Chunsoo.

[P4]
*Chunsoo? You?*

[P5]
*Were the two of them acquainted?*

[P6]
Come to think of it, Butler Kim and Im Chunsoo had a lot in common. They were around the same age, and both had been Hunters for a long time.

[P7]
*Come to think of it, Butler Kim was active as a Hunter during the Great Cataclysm, too.*

[P8]
I had never heard it directly from him, but I had suspected as much. Looking back and forth between the two men, I carefully asked,

[P9]
“Are you two close?”

[P10]
Im Chunsoo’s pupils trembled.

[P11]
* * *

[P12]
When Im Chunsoo first received the report on the Peace Guild, he had doubted his own eyes.

[P13]
The face in the photograph was one that remained in his hazy memories—a face he had been certain he would never see again.

[P14]
*Who did you say this man was?*

[P15]
*Peace Guild Master Kim Hwajong. He’s fifty-five years old and a B-rank Hunter.*

[P16]
*Kim Hwajong? A B-rank Hunter?*

[P17]
*Yes. Is there some problem?*

[P18]
*No, no. He resembles someone I used to know, so I mistook him for that person.*

[P19]
That figures. Im Chunsoo let out a sigh of relief.

[P20]
The face did resemble him a little, but that was all. More importantly, hadn’t that man died over thirty years ago?

[P21]
No matter how bizarre the world had become, the dead could not come back to life.

[P22]
*Even if that bastard had come back to life, he wouldn’t be rotting away in a place like this. I simply mistook him for an old B-rank Hunter.*

[P23]
That day, Im Chunsoo drank a glass of soju for the first time in a long while and tried to shake off his uneasy feelings. It was an attempt to cast off the terrible memories that had clung to his ankles even after he turned fifty.

[P24]
*Damn. I’m this old, and I’m still like this.*

[P25]
Later, when he heard that Kim Hwajong’s information was protected by airtight security, he had even felt a chill run down his spine.

[P26]
*Could it be? No. There’s no way.*

[P27]
But then… why did ominous premonitions never turn out to be wrong?

[P28]
“Rise up. Fire Wall.”

[P29]
A quiet voice chanting a spell rang out, and a wall of fire surged upward.

[P30]
*Fwoosh! Fwoosh!*

[P31]
Blue flames burning at an extreme temperature vaporized the ice spikes, which were harder than steel, without leaving a trace.

[P32]
And then—

[P33]
“I’m glad I’m not too late. You too, Chunsoo.”

[P34]
The moment he heard the voice he could never forget, not even in his dreams, Im Chunsoo remembered.

[P35]
The terror of being controlled by that man.

[P36]
The humiliation of rolling around on the ground to survive.

[P37]
*Fuck… I’m screwed.*

[P38]
As he stood frozen like a stone, Jin Taekyung asked him,

[P39]
“Are you two close?”

[P40]
What? Close?

[P41]
Im Chunsoo swallowed the stream of curses rising from the depths of his lungs and turned around.

[P42]
A man he had believed had died long ago was standing there.

[P43]
“I-Instructor.”

[P44]
Butler Kim smiled gently. It was the smile of a demon still deeply engraved in Im Chunsoo’s mind, even after all these years.

[P45]
“Twenty-eighth Regiment, First Battalion, Second Company. Im Chunsoo. Yes, I knew the moment I saw you.”

[P46]
It was the resonance of the soul.

[P47]
Im Chunsoo’s hunched back straightened. His feet snapped together at a forty-five-degree angle, and his gaze turned fifteen degrees upward toward the front.

[P48]
After a series of movements as fast as lightning, a thunderous shout burst from his throat.

[P49]
“Trainee Number One! Im! Chun! Soo!”

[P50]
The mountain shook as he bellowed out his military identification for the first time in thirty years.

[P51]
* * *

[P52]
What Team Leader 1 found after climbing up the mountain was grass splattered with blood in several places and the Security Team bound tightly with magical ropes.

[P53]
*What a sight.*

[P54]
Clicking his tongue inwardly, he drew his sword and cut through the ropes.

[P55]
Everyone had lost some blood, but none of them appeared to have suffered serious injuries. Jin Taekyung seemed to have shown them at least the bare minimum of consideration.

[P56]
*At this level, he’s either a top-tier B-rank… or an A-rank Hunter.*

[P57]
That was how strong Jin Taekyung appeared to Team Leader 1.

[P58]
For one person, the walk back down the mountain was a hellish experience.

[P59]
“Why did you do that? We might have been able to overlook the surveillance, but what happened today could amount to attempted murder. Did you start this after thinking about what would happen afterward?”

[P60]
“I’m… sorry.”

[P61]
At Team Leader 1’s words, the Security Team Leader hung his head.

[P62]
They had gone so far as to use force, only to be thoroughly trounced by Jin Taekyung. Even if he had ten mouths, he would have had nothing to say.

[P63]
“The Guild Master is deeply disappointed.”

[P64]
“Th-then?”

[P65]
“A written report and a pay cut are a given. Prepare yourself for anything beyond that, too.”

[P66]
“Are you talking about resignation?”

[P67]
“That depends on the Guild Master.”

[P68]
“Team Leader, perhaps…”

[P69]
“Let me tell you up front: don’t ask me for any favors. I don’t have any interest in taking the side of someone who smeared the name of the company I work for. And I have no intention of going against the Guild Master’s wishes.”

[P70]
“…”

[P71]
“Whew.”

[P72]
It was then that Team Leader 1 let out an irritated sigh.

[P73]
A booming shout echoed from far away.

[P74]
—Trainee Number One! Im! Chun! Soo!

[P75]
“……”

[P76]
“……”

[P77]
What was that? Were they hearing things?

[P78]
Team Leader 1 and even the Security Team members, who had all looked ready to die, jumped in surprise. The first to recover his composure was the Security Team Leader.

[P79]
“Team Leader 1, I’m sorry to bring this up in this kind of atmosphere, but I think I just heard the Guild Master’s voice.”

[P80]
Team Leader 1, who had been cleaning out his ears, opened his eyes wide.

[P81]
“Did you hear it too?”

[P82]
“We heard it, too.”

[P83]
“But we couldn’t really tell whether it was the Guild Master’s voice… We think we heard a name, though.”

[P84]
“That was a person’s name? I thought it was just someone screaming.”

[P85]
“Really? I thought it sounded like someone giving their name and rank.”

[P86]
Team Leader 1’s face hardened as he listened to the Security Team whispering among themselves.

[P87]
“Who just said that? What was that about giving a name and rank?”

[P88]
To him, Im Chunsoo was a respected senior and superior.

[P89]
Im Chunsoo was an unrivaled Hunter who had been active since the Great Cataclysm and a war hero—and they were saying he had suddenly given his name and rank?

[P90]
Team Leader 1 had never imagined such a thing. He couldn’t even imagine it.

[P91]
“Do you still have the leisure to spout this kind of nonsense? Do you think this is something people in their right minds would say?”

[P92]
“S-sorry.”

[P93]
“We must have heard it wrong.”

[P94]
“Everyone, get a hold of yourselves. Understood?”

[P95]
After issuing his warning, Team Leader 1 started walking again.

[P96]
That was when it happened.

[P97]
—No, sirrrrr!

[P98]
“……”

[P99]
—I’ll correct it, sirrrr!

[P100]
“……”

[P101]
Those were the shouts of a private second class filled with the very essence of his soul.

[P102]
It took a while before Team Leader 1’s tightly sealed mouth finally opened.

[P103]
“From now on, we’re running at full speed. Move.”

[P104]
“M-Move!”

[P105]
Everyone gathered there was at least a C-rank Hunter. They were superhuman beings who had already far surpassed the limits of ordinary people.

[P106]
They raced forward like runaway locomotives and reached the entrance to the hiking trail in less than five minutes.

[P107]
“You’re slow as hell. Took you long enough?”

[P108]
“Guild Master!”

[P109]
“Keep your voice down. You’ll burst my eardrums.”

[P110]
Seeing Im Chunsoo looking the same as always, Team Leader 1 let out a sigh of relief.

[P111]
“I was worried something might have happened…”

[P112]
“Something happened? Was there anything strange?”

[P113]
“N-no, sir. But where did that Jin Taekyung bastard go?”

[P114]
“I gave him a talking-to and sent him on his way. After speaking with him, I found out he was a better fellow than I expected. Why?”

[P115]
“I was wondering if he had caused some kind of disturbance.”

[P116]
“Ah, are you talking about the man shouting earlier?”

[P117]
“Yes, that’s right. But his voice sounded just like…”

[P118]
He couldn’t bring himself to finish the sentence.

[P119]
Just like the Guild Master’s.

[P120]
Im Chunsoo glared at him.

[P121]
“Just like what?”

[P122]
“Oh, it was nothing.”

[P123]
“What a bland bunch. Some greenhorns were playing army down there, so I chased them away. Do colleges still have hazing culture these days?”

[P124]
“Ah, I see.”

[P125]
“What was it? I made them do some PT exercises for a while, and they looked ready to die.”

[P126]
Team Leader 1 felt the suspicions he had been harboring vanish completely.

[P127]
*I must have been out of my mind. How dare I even think such a thing?*

[P128]
While he was deeply repenting to himself, Im Chunsoo was tearing into the Security Team.

[P129]
“Security Team Leader.”

[P130]
“Y-yes, sir!”

[P131]
“Oh, you can answer properly. After causing this mess, are you still a Team Leader just because you’re technically still a Team Leader?”

[P132]
“I’m sorry, Guild Master!”

[P133]
“Are the others keeping their mouths shut because they did such a good job? Do I need to make my sword dance today?”

[P134]
“We’re sorry, Guild Master!”

[P135]
Team Leader 1 watched the scene with a pleased smile.

[P136]
Every so often, there were people who spread the rumor that Im Chunsoo had a godawful personality. But after watching him up close, Team Leader 1 knew better. He was a charismatic superior and an outstanding senior in life.

[P137]
*Guild Master. I’ll follow you forever.*

[P138]
As Team Leader 1 gazed at Im Chunsoo’s back with boundless respect, he suddenly tilted his head.

[P139]
*…But why is there dirt on the Guild Master’s back?*

[P140]
He must have scolded those kids rather intensely.

[P141]
* * *

[P142]
“We’ve arrived.”

[P143]
At Butler Kim’s words, I came to my senses with a start and looked around. Through the window, I could see the entrance to an apartment complex.

[P144]
*When did we get here?*

[P145]
“Th-thank you.”

[P146]
“Don’t mention it.”

[P147]
A smile appeared on his handsomely lined face. He looked like a middle-aged actor who had once ruled an entire era.

[P148]
*No, this man really did rule an era, too.*

[P149]
Until now, I had thought of him as nothing more than a senior Hunter from a distant generation. But that meant I hadn’t understood Butler Kim at all.

[P150]
*He made an A-rank mage—and Im Chunsoo, no less—run around like a dog.*

[P151]
He had made a former war hero do a hundred sets of PT Exercise No. 8, then later kicked him in the shin with his dress shoe. Even now, the way he had calmly berated Im Chunsoo in that gentle voice sent chills down my spine.

[P152]
*Trainee, who uses mana during PT exercises?*

[P153]
*Whack!*

[P154]
*Trainee Number One Im Chunsoo. S-sorry, sir.*

[P155]
*Does it hurt? Now that you’ve gotten older, has your voice gotten quieter, too?*

[P156]
*No, sirrrrr!*

[P157]
*Attention. At ease. Attention. At ease.*

[P158]
*Snap-snap-snap-snap!*

[P159]
*On your backs. On your fronts. On your backs. On your backs.*

[P160]
*Gasp.*

[P161]
*Trainee, didn’t you hear me say on your backs? Get your head straight.*

[P162]
*I’ll correct it, sirrrr!*

[P163]
*And why are you bullying an innocent junior? Haven’t I repeatedly emphasized that seniors and juniors should help each other?*

[P164]
*S-sorry, sir.*

[P165]
*Repeat after me. Sitting down, cherish your junior; standing up, cherish him. One. Two.*

[P166]
*Cherish my junior!*

[P167]
*Trainee, I remember you’re Class 25. Am I right?*

[P168]
*Trainee Number One Im Chunsoo. Yes, sir.*

[P169]
*I’m Class 3. If what happened today gets out or happens again, Classes 4 through 24 will assemble without exception.*

[P170]
*…*

[P171]
*Why aren’t you answering? Prepare for squat jumps.*

[P172]
*P-prepare, sir…*

[P173]
He kept working him over, then working him over some more.

[P174]
It was the kind of sight you couldn’t see even if you paid for it. If the Sangdong Guild members had witnessed it, the Guild might have had to close its doors that very day.

[P175]
*What on earth is Butler Kim’s real identity?*

[P176]
If someone was Class 3 at the Hunter Training Center, they could line up every Guild Master in the country on a parade ground and beat every last one of them with a bat.

[P177]
And he had been an instructor, no less.

[P178]
It would not be an exaggeration to say that every mage from the early days of the Great Cataclysm had passed through his hands.

[P179]
*His ability as a mage is at least A-rank, too.*

[P180]
I could tell just by watching Im Chunsoo take his punishment without daring to make a peep. Butler Kim surpassed him in both seniority and skill.

[P181]
There was probably also an elemental advantage between ice and fire. You could say Butler Kim was the one who taught Im Chunsoo and raised him to his current position.

[P182]
*But…*

[P183]
Why was someone that accomplished working as a butler?

[P184]
I was sneaking a sidelong glance at Butler Kim when our eyes met.

[P185]
“You seem to have a lot you want to ask.”

[P186]
“To be honest, I do.”

[P187]
I was too curious to stand it any longer.

[P188]
Seeing my thoughts written plainly across my face, Butler Kim curled up the corners of his mouth.

[P189]
“It’s a long story.”

[P190]
“That’s fine. I’m on vacation, so I have plenty of time.”

[P191]
“Ah, then this is a good opportunity to hear your story as well, Mr. Jin. I already have more than one or two questions myself.”

[P192]
“Now that I think about it, it’s already dinnertime. Tomorrow is the last day of my vacation, so I have to sign a real-estate contract, too. Hahaha.”

[P193]
“……”
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 진태경    | **Jin Taekyung**   |
| 김화종    | **Kim Hwajong**   |
| 임춘수    | **Im Chunsoo**    |
| 살기     | **killing intent**                               |                                                       |
| 창기     | **Spear Energy**                                 | Explicit system skill for Taekyung                    |
| 선배     | **Senior**                                   |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 교관 | **Instructor** | Kim Hwajong's former Hunter Training Center role and address. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 101,
  "passed": true,
  "metrics": {
    "source_characters": 5677,
    "translation_characters": 12868,
    "length_ratio": 2.267,
    "source_paragraphs": 184,
    "translation_paragraphs": 193
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "살기",
        "preferred": "killing intent"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "창기",
        "preferred": "Spear Energy"
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
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "상동",
        "romanization": "sangdong"
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
