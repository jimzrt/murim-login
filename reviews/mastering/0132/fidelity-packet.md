# Fidelity Gate — Chapter 132

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
  1|＃132화
  2|
  3|
  4|
  5|“실례가 안 된다면 빙당호로 하나만 먹어도 되겠습니까?”
  6|
  7|예상을 뛰어넘는 멘트에 순간 뇌정지가 왔다.
  8|
  9|‘이게 뭔 소리야.’
 10|
 11|도를 아십니까도 아니고, 빙당호로 하나만 먹어도 되겠냐니.
 12|
 13|처음 만난 절정 고수가 세상에서 가장 정중한 말투로 빙당호로를 구걸하는 상황은 내 계획에 없었는데.
 14|
 15|꼬르륵.
 16|
 17|이제는 배꼽시계로 측은지심까지 자극한다. 나는 엉겁결에 아직 들고 있던 빙당호로를 내밀었다.
 18|
 19|“여, 여기요.”
 20|
 21|“감사합니다, 은인.”
 22|
 23|빙당호로 가성비 보소, 만난 지 10초 만에 절정 고수의 은인이 됐다.
 24|
 25|애들이나 먹을 법한 사탕 과자를 맹렬하게 물고 빠는 청년, 청풍의 모습을 나와 혁무진이 멍하니 지켜봤다.
 26|
 27|“조장님, 아는 사람이에요?”
 28|
 29|“아니.”
 30|
 31|빙당호로 하나를 게 눈 감추듯 먹어 치운 청풍은 아직 모자란지 굶주린 맹수의 눈빛으로 혁무진을 바라봤다.
 32|
 33|정확히는 녀석의 양손에 들린 빙당호로 두 개를.
 34|
 35|“……무진아.”
 36|
 37|“네?”
 38|
 39|“드려라.”
 40|
 41|혁무진이 재빨리 손을 뒤로 감췄다.
 42|
 43|“싫습니다.”
 44|
 45|“싫어?”
 46|
 47|“예, 저 이거 오 년 만에 처음으로 먹는 겁니다. 아직 입도 안 댔어요.”
 48|
 49|“그렇구나. 우리 무진이가 예상 수명보다 오십 년 정도 일찍 죽고 싶구나.”
 50|
 51|“…….”
 52|
 53|한숨을 푹 내쉰 녀석이 빙당호로를 내밀자 청풍의 눈이 번쩍 빛났다.
 54|
 55|“감사합니다, 은인!”
 56|
 57|다음 순간, 휙 하는 바람 소리와 함께 빙당호로가 청풍의 손으로 옮겨 갔다.
 58|
 59|“으헉.”
 60|
 61|실로 엄청난 속도다. 헛숨을 들이킨 혁무진이 내게 떨리는 목소리로 속삭였다.
 62|
 63|“보, 보통 거지가 아닌데요?”
 64|
 65|눈앞의 꾀죄죄한 청년이 절정 고수라는 사실을 알면 무슨 표정을 지을까?
 66|
 67|나는 정신없이 빙당호로를 흡입 중인 청풍을 유심히 살폈다.
 68|
 69|‘절정 고수라기에는 너무 젊어 보이는데.’
 70|
 71|나도 지금까지 주워들은 풍문이 있다. 명문 대파에서 온갖 영재 교육과 지원을 쏟아부어도 가물에 콩 나듯 탄생하는 것이 절정 고수라는 사실도 이제는 안다.
 72|
 73|천하에서도 변방 촌구석 취급받는 산서성 출신인 진무경이 유명해진 이유도 그 때문이다.
 74|
 75|남들보다 10년, 20년을 앞서 절정의 경지에 올랐으니까.
 76|
 77|‘그런데…….’
 78|
 79|기껏해야 내 또래로 보이는 녀석이 기감으로도 레벨을 파악하지 못하는 절정 고수라니.
 80|
 81|산서성에 저렇게 젊은 절정 고수가 있다는 말은 들어 본 적이 없다.
 82|
 83|‘이런 놈이 어디서 튀어나온 거지?’
 84|
 85|때마침 청풍이 고개를 들었다. 허겁지겁 먹은 터라 입가에는 끈적끈적한 설탕이 한가득 묻어 있었다.
 86|
 87|“휴우, 잘 먹었습니다.”
 88|
 89|“배가 좀…… 많이 고프셨나 보네.”
 90|
 91|“네. 하루 종일 굶었거든요.”
 92|
 93|“저런, 어쩌다가?”
 94|
 95|“여비를 잃어버리는 바람에 그만. 그래도 재미있는 경험을 했네요.”
 96|
 97|“…….”
 98|
 99|돈 없어서 온종일 쫄쫄 굶은 게 재밌는 경험이 될 수 있나?
100|
101|처음 만난 그 순간부터 느낀 거지만 확실히 사고방식이 특이한 놈이다.
102|
103|청풍이 해맑게 웃으며 꾸벅 포권을 취했다.
104|
105|“아, 제 소개가 늦었네요. 은인들께 청풍이 인사 올립니다.”
106|
107|“진태경이라고 합니다.”
108|
109|“전 이분의 오른팔이자 심장, 혁무진입니다.”
110|
111|혁무진의 헛소리를 깔끔하게 무시하고 청풍을 주시했다.
112|
113|내가 이래 봬도 나름 산서성에서는 유명 인사다.
114|
115|몇 달 전까지만 해도 나쁜 쪽으로, 지금은 정반대의 이유로 산서성에서 내 이름을 모르는 사람이 없다.
116|
117|‘알아보려나?’
118|
119|은근히 기대감을 품은 그때, 청풍의 얼굴이 딱딱하게 굳었다.
120|
121|“저, 혹시…….”
122|
123|“네, 맞습니다. 제가 바로 그.”
124|
125|“실례가 안 된다면 좀 더 신세 져도 될까요?”
126|
127|“예?”
128|
129|“제가 좀 오래 굶어서.”
130|
131|때맞춰 청풍의 배에서 천둥 같은 소리가 흘러나왔다.
132|
133|꼬르륵.
134|
135|“……그럼 같이 식사라도.”
136|
137|“감사합니다, 은인!”
138|
139|이게 은인인지 호구인지 모르겠다.
140|
141|
142|
143|* * *
144|
145|
146|
147|홍화객잔의 내부는 이른 저녁 식사를 하러 온 사람들로 바글거렸다.
148|
149|발 빠르게 달려온 점소이가 몇 안 되는 빈자리로 우리를 안내해 주었다.
150|
151|“음식은 뭘로 드릴깝쇼?”
152|
153|나는 나무로 제작된 무림식 메뉴판을 청풍에게 건네줬다.
154|
155|“드시고 싶은 거 시키세요.”
156|
157|“아앗, 아닙니다. 제가 은혜도 모르는 금수(禽獸)도 아니고 어찌…….”
158|
159|“괜찮으니까 드시고 싶은 거 시키세요.”
160|
161|“그럼 여기 있는 거 전부 주세요.”
162|
163|“…….”
164|
165|이런 금수 같은 놈을 봤나.
166|
167|대형 호구의 등장에 주방만 바빠졌다. 얼마 지나지 않아 주문한 음식들이 쉬지 않고 줄줄이 쏟아져 나왔다.
168|
169|“산니백육(䔉泥白肉) 나왔습니다. 이 음식은 삶은 돼지고기를 얇게 포를 떠서…….”
170|
171|“오.”
172|
173|“어향육사(魚香肉絲) 나왔습니다. 돼지고기를 죽순, 목이버섯 등과 함께…….”
174|
175|“오오.”
176|
177|“경장육사(京醬肉絲)입니다.”
178|
179|“오오오!”
180|
181|“규화계(叫花鷄).”
182|
183|“오오오오!”
184|
185|처음에는 열심히 설명해 주던 점소이의 말이 점점 짧아지는 것과 달리, 청풍의 리액션은 갈수록 풍부해졌다.
186|
187|끊임없이 탁자를 채워 가는 요리. 슬슬 음식을 놓을 자리가 없어질 때쯤 점소이가 현자 타임이 온 듯한 얼굴로 새로 나온 접시를 슥 내밀었다.
188|
189|“매구.”
190|
191|“매구?”
192|
193|옆 동네 섬나라 사는 메구미는 알아도 매구는 처음 들어 본다. 내 시선에 점소이가 귀찮다는 듯이 대답했다.
194|
195|“매채구육(梅采拘肉)이요.”
196|
197|“…….”
198|
199|이제는 하다 하다 줄임말까지 쓰는구나.
200|
201|내가 어이없어하는 사이 청풍은 빠르게 음식 접시를 비워 나가고 있었다.
202|
203|“우걱, 우걱.”
204|
205|“천천히 드세요. 천천히.”
206|
207|“아히헤호. 하후이흡히하.”
208|
209|“……대답하지 말고 그냥 드세요.”
210|
211|“캉사합히하!”
212|
213|혁무진이 입맛이 뚝 떨어진 얼굴로 속삭였다.
214|
215|“진짜 거지 아닙니까?”
216|
217|“아까 빙당호로 낚아채는 거 못 봤어? 절대 아니야.”
218|
219|“쿰척, 쿰척!”
220|
221|“……아마도 아닐 거야.”
222|
223|“혹시 압니까, 개방(丐幫)의 고수일지도.”
224|
225|“개방이라.”
226|
227|무협 소설에서 질리도록 많이 봤다. 실제로 현 무림에도 구파일방(九派一幇) 중 하나로 버젓이 존재한다.
228|
229|아직 만나 보지는 못했지만, 당장 저기 객잔 입구에서 어슬렁거리는 거지 중 하나가 개방도일 수도 있다.
230|
231|“제가 매듭 있나 살짝 확인해 볼까요?”
232|
233|개방의 고수들은 허리의 매듭으로 신분을 구별한다던가?
234|
235|나는 고개를 저었다.
236|
237|‘아니, 일단 개방 소속은 아니야.’
238|
239|그렇다면 내 이름을 들었을 때 어떻게든 반응이 왔을 거다. 같은 정파 소속이니 일부러 모른 척할 이유도 없고.
240|
241|‘그럼 어느 문파 출신이지?’
242|
243|이렇게 젊은 절정 고수가 하늘에서 뚝 떨어졌을 리는 없다.
244|
245|최소한 이름난 문파 출신일 텐데……. 갈수록 이 수수께끼의 청년에 대한 호기심이 샘솟는다.
246|
247|“꺼윽, 잘 먹었습니다.”
248|
249|마침내 식사를 끝마친 청풍이 올챙이배를 두드리다가 나와 혁무진을 보고 멈칫했다.
250|
251|“다 처음 먹어 보는 음식이라 은인들 앞에서 추태를 보였습니다. 제가 너무 과하진 않았는지…….”
252|
253|이미 충분히 과했어, 인마.
254|
255|그래도 최소한의 자각이라도 있어서 다행이다.
256|
257|“괜찮습니다. 저도 가끔 그러는데요 뭘.”
258|
259|“저랑 통하는 구석이 있으시네요. 하하.”
260|
261|나는 청풍을 따라 웃으며 입을 열었다. 이제 슬슬 호구 조사를 시작할 타이밍이다.
262|
263|“그런데 다 처음 먹어 보는 음식이라니, 평소에 기름진 음식을 잘 안 드시는 모양이네요.”
264|
265|청풍이 침울하게 고개를 내저었다.
266|
267|“안 먹는 게 아니라 못 먹었어요. 이렇게 맛있는 음식들이 있는 걸 알았다면 좀 더 일찍 하산했을 텐데.”
268|
269|“아아, 산에 사셨구나. 많이 힘드셨겠네.”
270|
271|“산 생활이요? 재밌어요. 경치도 좋고, 여기저기 먹을 것도 많고요. 저희 할아버지도 산에서 평생 혼자 사셨는걸요.”
272|
273|“할아버님이요?”
274|
275|“예. 그런데 저어…….”
276|
277|“말씀하세요.”
278|
279|“술 좀 시켜도 될까요? 제가 아직 술을 못 먹어 봐서.”
280|
281|“……얼마든지 시키세요.”
282|
283|이 자식은 못 먹어 본 것도 많네.
284|
285|그래도 한 줄기 양심은 남아 있는지 가장 값싼 화주 한 병을 시킨다.
286|
287|잠시 후, 화주를 거침없이 들이킨 청풍이 약간 붉어진 얼굴로 중얼거렸다.
288|
289|“으아, 이게 취한다는 거구나. 그런데 우리가 무슨 얘기를 하고 있었죠?”
290|
291|“할아버님께서 산에서 평생 혼자 사셨다는 것까지.”
292|
293|“아, 맞다. 아무튼, 저도 어릴 때부터 할아버지랑 같이 살았어요. 그게 다섯 살 때부터니까, 벌써 십오 년이나 됐네요.”
294|
295|“그래요? 진짜 오래됐네.”
296|
297|나는 놀란 티를 내지 않으려고 애썼다.
298|
299|불과 약관에 절정 고수라니. 최소한 진무경에 버금가거나 그 이상 가는 천재란 소리다. 이야기를 나눌수록 그의 정체가 점점 궁금해졌다.
300|
301|“거기가 어디예요? 그렇게 살기 좋은 곳이면 나중에 한번 놀러 가 볼까 하는데.”
302|
303|뭔가 말하려던 청풍이 순간 멈칫했다.
304|
305|“어어, 그건 말씀 못 드릴 것 같은데.”
306|
307|“에이, 그 정도도 말 못 해 줘요?”
308|
309|“왜냐하면, 할아버지가 엄청나게 싫어하셔서…… 안 그래도 그것 때문에 일 년에 한두 번씩은 거처를 옮기시거든요.”
310|
311|“거처를 옮겨요?”
312|
313|“네. 자꾸 이상한 사람들이 찾아와서요.”
314|
315|이상한 사람들이라니. 진상 등산객인가?
316|
317|하긴, 산에 사는 사람한테는 불편할 만도 하겠다.
318|
319|그가 추억에 잠긴 눈으로 말을 이었다.
320|
321|“제가 열 살 때였는데, 어느 날 수십 명이 우르르 찾아와서 행패를 부리는 거예요. 할아버지께서 산에 불 질러 버리기 전에 꺼지라고 소리치시던 기억이 나요.”
322|
323|“아, 그래서 계속 거처를 옮기시는……?”
324|
325|“네, 다행히 산이 넓어서 십 년째 잘 피해 다니고 계세요.”
326|
327|“…….”
328|
329|십 년씩이나? 그 할아버지도 대단한 양반이다.
330|
331|그때 청풍의 이야기를 흥미진진하게 듣고 있던 혁무진이 물었다.
332|
333|“그럼 공자께서는 왜 하산하신 겁니까?”
334|
335|아쉬운 듯이 술병 주둥이를 쪽쪽 빨던 청풍이 대답했다.
336|
337|“십봉룡(十鳳龍) 때문에요.”
338|
339|“십봉룡? 그건 또 뭐야?”
340|
341|내 물음에 혁무진이 별 이상한 놈 다 본다는 눈빛으로 대답했다.
342|
343|“조장님이 십봉룡을 왜 몰라요?”
344|
345|“모를 수도 있지, 인마.”
346|
347|“엥? 작년에 기루에서 술 푸지게 먹고 십봉룡이 될 거라고 떠들었다가 개망신당했으면서.”
348|
349|“그건 내가 아니라…… 됐다. 그래서 십봉룡이 뭔데?”
350|
351|“진심으로 몰라서 물어보시는 겁니까?”
352|
353|“모르면 안 되냐?”
354|
355|“당연히 안 되죠. 당장 이공자님이 십봉룡인데.”
356|
357|어, 진짜?
358|
359|눈을 깜빡거리는 내게 혁무진이 열변을 토했다.
360|
361|“정파 무림 최고의 후기지수들! 차기 무림을 이끌어갈 용과 봉황들! 십봉룡을 모른다는 게 말이나 됩니까?”
362|
363|“야, 야. 목소리나 줄여. 사람들 쳐다보잖아.”
364|
365|그냥 하는 말이 아니라 혁무진의 쩌렁쩌렁한 외침 때문에 주위 손님들이 우리를 힐끗거리는 중이다.
366|
367|“쳐다보면 뭐 어때요. 이건 조장님이 해도 너무하잖아요! 사람 놀립니까, 예?”
368|
369|“사람 놀리는 건 모르겠고, 때리는 건 잘해.”
370|
371|“제가 너무 흥분한 것 같네요. 죄송합니다.”
372|
373|순식간에 이성을 되찾은 혁무진을 뒤로하고 청풍을 향해 사람 좋은 미소를 지어 보였다.
374|
375|“말씀 계속하시죠.”
376|
377|“별건 아니에요. 순간적으로 치기 어린 생각이 들었던 거죠.”
378|
379|청풍이 살짝 풀린 눈으로 나를 응시했다. 굳이 공력으로 취기를 몰아내지 않을 생각인지 여전히 살짝 알딸딸한 모습이다.
380|
381|“나와 저들 중에 누가 더 강할까? 저는 그 의문에 대한 답을 확인하고 싶었어요.”
382|
383|결국은 무인의 호승심(好勝心) 때문이라는 거다.
384|
385|새로운 세상으로 나아가고픈 마음, 강자를 꺾어 자신의 무공을 입증하고픈 마음이 그의 발걸음을 산 아래로 이끌었음을 짐작할 수 있었다.
386|
387|‘저런 생각을 해도 될 만큼의 실력도 있는 것 같고.’
388|
389|진무경은 약관에 절정의 경지에 올라 중원을 떠들썩하게 만들었다고 했다. 그랬던 그는 지금 십봉룡, 정파 최고의 후기지수 중 한 사람으로 꼽힌다.
390|
391|눈앞의 청풍은 최소 진무경에 비견할 만한 무재(武才)의 소유자다.
392|
393|‘그럴 만한 자격이 있어.’
394|
395|내심 고개를 끄덕이던 그 순간이었다.
396|
397|“푸하하하!”
398|
399|“큭, 크큭. 아, 웃음 참느라 혼났네.”
400|
401|소리의 근원지를 향해 고개를 들었다.
402|
403|2층. 비단옷을 걸친 다섯 명의 남녀가 얼굴 가득 비웃음을 띤 채 우리를 내려다보고 있었다.
```

## Assembled English

```markdown
[P1]
# Chapter 132

[P2]
“If it wouldn’t be too much trouble, may I have just one candied hawthorn skewer?[^1]”

[P3]
The unexpected comment caused my brain to freeze for a moment.

[P4]
*What the hell is he talking about?*

[P5]
It wasn’t one of those *Do you know the Way?* pitches. He was asking if he could have just one candied hawthorn skewer.

[P6]
I hadn’t planned for a Peak master I’d just met to beg for candied hawthorn in the most polite tone in the world.

[P7]
*Grrrrrrowl.*

[P8]
Now he was even tugging at my pity with his stomach clock. Without thinking, I held out the candied hawthorn skewer I was still holding.

[P9]
“H-here.”

[P10]
“Thank you, Benefactor.”

[P11]
Talk about value for money. Ten seconds after meeting him, I had become a Peak master’s Benefactor.

[P12]
Hyuk Mujin and I stared blankly at Cheongpung as he ferociously bit and sucked on a sugary snack meant for children.

[P13]
“Captain, do you know him?”

[P14]
“No.”

[P15]
Cheongpung devoured the candied hawthorn skewer as though it had vanished in the blink of an eye. Apparently, it hadn’t been enough, because he turned the eyes of a starving beast on Hyuk Mujin.

[P16]
More precisely, on the two candied hawthorn skewers in Mujin’s hands.

[P17]
“…Mujin.”

[P18]
“Yes?”

[P19]
“Give them to him.”

[P20]
Hyuk Mujin quickly hid his hands behind his back.

[P21]
“No.”

[P22]
“No?”

[P23]
“Yes. This is the first time I’ve eaten these in five years. I haven’t even taken a bite yet.”

[P24]
“I see. Our Mujin wants to die about fifty years ahead of schedule.”

[P25]
“…”

[P26]
With a deep sigh, he held out the skewers. Cheongpung’s eyes flashed.

[P27]
“Thank you, Benefactor!”

[P28]
The next moment, there was a sharp *whoosh*, and the skewers were in Cheongpung’s hands.

[P29]
“Gah!”

[P30]
That was incredible speed. Hyuk Mujin sucked in a startled breath and whispered to me in a trembling voice.

[P31]
“H-he’s no ordinary beggar, is he?”

[P32]
What kind of face would Mujin make if he learned that the filthy young man in front of us was a Peak master?

[P33]
I studied Cheongpung as he inhaled the candied hawthorn with single-minded focus.

[P34]
*He looks far too young to be a Peak master.*

[P35]
I had heard a few rumors by now. I also knew that even famous, powerful sects with every kind of genius training and support only produced a Peak master once in a blue moon.

[P36]
That was why Jin Mukyung, who came from Shanxi Province—a remote backwater even by the standards of the Central Plains—had become so famous.

[P37]
He had reached the Peak realm ten or twenty years ahead of everyone else.

[P38]
*But…*

[P39]
The young man in front of me looked barely my age, yet he was a Peak master whose Level I couldn’t even determine through Qi Sense.

[P40]
I had never heard of a Peak master this young in Shanxi Province.

[P41]
*Where the hell did this guy come from?*

[P42]
As if on cue, Cheongpung raised his head. He had eaten so hurriedly that sticky sugar covered the corners of his mouth.

[P43]
“Whew. That was delicious.”

[P44]
“You must’ve been a little… very hungry.”

[P45]
“Yes. I haven’t eaten all day.”

[P46]
“Oh dear. How did that happen?”

[P47]
“I lost my travel money. Still, it was an interesting experience.”

[P48]
“…”

[P49]
Could starving all day because you had no money really count as an interesting experience?

[P50]
I had sensed it from the moment we met, but this guy definitely had a peculiar way of thinking.

[P51]
Cheongpung smiled brightly and gave us a respectful fist-and-palm salute.

[P52]
“Ah, I’m late introducing myself. Cheongpung offers his greetings to his Benefactors.”

[P53]
“My name is Jin Taekyung.”

[P54]
“And I’m this man’s right arm and heart, Hyuk Mujin.”

[P55]
I completely ignored Hyuk Mujin’s nonsense and kept my eyes on Cheongpung.

[P56]
I might not look it, but I was fairly famous in Shanxi Province.

[P57]
Until a few months ago, I had been famous for all the wrong reasons. Now, for the exact opposite reason, there wasn’t a soul in Shanxi Province who didn’t know my name.

[P58]
*I wonder if he’ll recognize me.*

[P59]
Just as I was secretly getting my hopes up, Cheongpung’s face went stiff.

[P60]
“Excuse me, are you perhaps…”

[P61]
“Yes, that’s right. I’m the very—”

[P62]
“Would it be all right if I imposed on you a little longer?”

[P63]
“What?”

[P64]
“I’ve been hungry for quite a long time.”

[P65]
Right on cue, a thunderous sound came from Cheongpung’s stomach.

[P66]
*Grrrrrrowl.*

[P67]
“…Then why don’t we have a meal together?”

[P68]
“Thank you, Benefactor!”

[P69]
I couldn’t tell whether I was his Benefactor or just a sucker.

[P70]
* * *

[P71]
Honghwa Inn was packed with people who had come for an early dinner.

[P72]
A quick-footed waiter led us to one of the few remaining empty tables.

[P73]
“What’ll it be?”

[P74]
I handed Cheongpung the wooden Murim-style menu.

[P75]
“Order whatever you want.”

[P76]
“Oh, no, I couldn’t. I’m not some ungrateful beast who doesn’t know how to repay a kindness. How could I…”

[P77]
“It’s fine. Order whatever you want.”

[P78]
“Then I’ll have everything on here.”

[P79]
“…”

[P80]
What an ungrateful beast.

[P81]
The appearance of a colossal sucker kept the kitchen busy. Before long, the dishes we had ordered began pouring out without pause.

[P82]
“Garlic Pork is here. This dish is made by slicing boiled pork thin and…”

[P83]
“Oh.”

[P84]
“Fish-Fragrant Shredded Pork is here. It’s pork served with bamboo shoots, wood ear mushrooms, and…”

[P85]
“Ohhh.”

[P86]
“Beijing Sauce Shredded Pork.”

[P87]
“Ohhhh!”

[P88]
“Beggar’s Chicken.”

[P89]
“Ohhhhh!”

[P90]
Unlike the waiter, whose explanations had grown shorter and shorter, Cheongpung’s reactions were becoming more and more elaborate.

[P91]
Dish after dish continued filling the table. Just as there was barely any room left, the waiter slid out another plate with the expression of a man who had reached enlightenment.

[P92]
“Maegu.”

[P93]
“Maegu?”

[P94]
I’d heard of Megumi from the island country next door, but Maegu was a new one to me. Catching my look, the waiter answered as if explaining it was a chore.

[P95]
“Maechae Guyuk.”[^2]

[P96]
“…”

[P97]
Now he was even abbreviating dish names.

[P98]
While I stared at him in disbelief, Cheongpung rapidly emptied the plates.

[P99]
“Nom, nom.”

[P100]
“Slow down. Eat slowly.”

[P101]
“Mmph, mmph. Ah hih he ho. Ha hu i heup hi ha.”

[P102]
“Don’t answer. Just keep eating.”

[P103]
“Khanks hah!”

[P104]
Hyuk Mujin whispered with a thoroughly disgusted expression.

[P105]
“Isn’t he really a beggar?”

[P106]
“Didn’t you see him snatch the candied hawthorn earlier? No way.”

[P107]
*Chomp, chomp.*

[P108]
“…Probably not.”

[P109]
“What if he’s a master of the Beggars’ Sect?”

[P110]
“The Beggars’ Sect, huh?”

[P111]
I had seen it countless times in martial arts novels. It also existed openly in the actual Murim as one of the Nine Sects and One Gang.

[P112]
I had yet to meet one of its members, but any of the beggars loitering near the inn’s entrance could be a Beggars’ Sect disciple.

[P113]
“Should I take a quick look and see if he has any knots?”

[P114]
The masters of the Beggars’ Sect supposedly distinguished their status by the knots around their waists.

[P115]
I shook my head.

[P116]
*No. He isn’t with the Beggars’ Sect.*

[P117]
If he were, he would have reacted somehow when he heard my name. We belonged to the same orthodox faction, so he had no reason to pretend he didn’t recognize me.

[P118]
*Then what sect is he from?*

[P119]
There was no way a Peak master this young had simply dropped out of the sky.

[P120]
He had to be from a famous sect at the very least… The more I thought about it, the more curious I became about this mysterious young man.

[P121]
“Burp. That was delicious.”

[P122]
Cheongpung finally finished eating. After patting his tadpole-like belly, he looked at Hyuk Mujin and me, then stopped short.

[P123]
“It was my first time trying any of these dishes, so I made a spectacle of myself in front of my Benefactors. I hope I didn’t overdo it…”

[P124]
*You already overdid it, you idiot.*

[P125]
Still, it was good that he had at least a little self-awareness.

[P126]
“It’s fine. I do that sometimes, too.”

[P127]
“We have something in common. Ha-ha.”

[P128]
I laughed along with Cheongpung and opened my mouth. It was about time I started a background check on this sucker.

[P129]
“You said it was your first time trying all of this. I suppose you don’t usually eat rich food.”

[P130]
Cheongpung shook his head gloomily.

[P131]
“It’s not that I don’t. I couldn’t. If I’d known food this delicious existed, I would have come down from the mountain sooner.”

[P132]
“Oh, so you lived in the mountains. That must’ve been difficult.”

[P133]
“Life in the mountains? It was fun. The scenery was beautiful, and there was plenty to eat all over the place. My grandfather has lived alone in the mountains his entire life, too.”

[P134]
“Your grandfather?”

[P135]
“Yes. But, um…”

[P136]
“Go ahead.”

[P137]
“May I order some alcohol? I’ve never tried it before.”

[P138]
“…Order as much as you like.”

[P139]
This kid had a lot of things he’d never tried.

[P140]
At least he still had a sliver of conscience left. He ordered the cheapest bottle of fire liquor.

[P141]
A short while later, Cheongpung downed the fire liquor without hesitation and muttered, his face slightly flushed.

[P142]
“Ahh, so this is what it means to get drunk. But what were we talking about?”

[P143]
“Your grandfather living alone in the mountains his entire life.”

[P144]
“Oh, right. Anyway, I’ve lived with my grandfather since I was little. I was five when we started living together, so it’s already been fifteen years.”

[P145]
“Really? That’s a long time.”

[P146]
I did my best not to show my surprise.

[P147]
*A Peak master at barely twenty.*

[P148]
That meant he was a genius at least comparable to Jin Mukyung, if not greater. The more I talked with him, the more curious I became about his identity.

[P149]
“Where is it? If it’s such a nice place to live, maybe I could visit sometime.”

[P150]
Cheongpung hesitated just as he was about to say something.

[P151]
“Um, I don’t think I can tell you that.”

[P152]
“Come on. You can’t even tell me that much?”

[P153]
“Because my grandfather hates it so much… He already moves to a different place once or twice a year because of that.”

[P154]
“He moves?”

[P155]
“Yes. Strange people keep coming to see him.”

[P156]
*Strange people? Obnoxious hikers?*

[P157]
Well, I suppose it would be annoying for someone living in the mountains.

[P158]
He continued with a nostalgic look in his eyes.

[P159]
“When I was ten, dozens of people suddenly came rushing over and started causing trouble. I remember my grandfather shouting at them to get lost before he set the mountain on fire.”

[P160]
“Oh, so that’s why he keeps moving?”

[P161]
“Yes. Fortunately, the mountains are huge, so he’s managed to avoid them for ten years.”

[P162]
“…”

[P163]
Ten years? His grandfather was quite a man.

[P164]
Hyuk Mujin, who had been listening to Cheongpung’s story with great interest, asked, “Then why did you come down from the mountain, Young Master?”

[P165]
Cheongpung, who had been sucking on the mouth of the liquor bottle regretfully, answered,

[P166]
“Because of the Ten Dragons and Phoenixes.”

[P167]
“The Ten Dragons and Phoenixes? What’s that supposed to be?”

[P168]
At my question, Hyuk Mujin looked at me as though I were the strangest person he had ever seen.

[P169]
“Why don’t you know about the Ten Dragons and Phoenixes, Captain?”

[P170]
“I’m allowed not to know, damn it.”

[P171]
“Huh? Last year, you got plastered at a pleasure house and made a complete fool of yourself bragging that you were going to become one of them.”

[P172]
“That wasn’t me… Never mind. What are the Ten Dragons and Phoenixes?”

[P173]
“Are you seriously asking because you don’t know?”

[P174]
“Can’t I just not know?”

[P175]
“Of course you can’t. The Second Young Master is one of them, after all.”

[P176]
Wait, really?

[P177]
As I blinked at him, Hyuk Mujin launched into an impassioned explanation.

[P178]
“They’re the greatest young prodigies of the orthodox Murim! The dragons and phoenixes who will lead the Murim of the future! How can you not know about the Ten Dragons and Phoenixes?”

[P179]
“Hey, hey. Keep your voice down. People are staring.”

[P180]
I wasn’t exaggerating. Hyuk Mujin’s booming voice had drawn glances from the other customers.

[P181]
“Who cares if they stare? This is too much even for you, Captain! Are you making fun of me?”

[P182]
“I don’t know about making fun of people, but I’m good at hitting them.”

[P183]
“I think I got too worked up. I’m sorry.”

[P184]
Hyuk Mujin regained his composure in an instant. I turned away from him and gave Cheongpung a friendly smile.

[P185]
“Please continue.”

[P186]
“It’s nothing important. I just had a childish thought for a moment.”

[P187]
Cheongpung gazed at me through slightly unfocused eyes. Apparently, he had no intention of using his internal energy to dispel the drunkenness, because he still looked a little tipsy.

[P188]
“Who would be stronger, me or them? I wanted to find the answer to that question.”

[P189]
In the end, it came down to a martial artist’s competitive pride.

[P190]
The desire to venture into a new world. The desire to defeat the strong and prove his martial arts. I could tell those feelings had led him down the mountain.

[P191]
*He seems to have the skill to justify thinking that way, too.*

[P192]
Jin Mukyung had supposedly reached the Peak realm at barely twenty, causing an uproar throughout the Central Plains. Now he was counted among the Ten Dragons and Phoenixes, the greatest young prodigies of the orthodox faction.

[P193]
The Cheongpung in front of me possessed martial talent at least comparable to Jin Mukyung’s.

[P194]
*He has every right to think so.*

[P195]
I was nodding inwardly when—

[P196]
“Puhahaha!”

[P197]
“Pfft, hahahaha. Ah, holding back my laughter was torture.”

[P198]
I raised my head toward the source of the sound.

[P199]
On the second floor, five men and women dressed in silk were looking down at us, their faces full of mockery.

[P200]
[^1]: Candied hawthorn skewers are a traditional Chinese snack made by coating skewered fruit in hardened sugar.

[P201]
[^2]: *Maechae Guyuk* is pork belly with preserved mustard greens. The waiter shortens its Korean name to *Maegu*, which sounds like the beginning of the Japanese name Megumi.
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
# Chapter 132

[P2]
“If it wouldn’t be too much trouble, may I have just one candied hawthorn skewer?[^1]”

[P3]
[^1]: Candied hawthorn skewers are a traditional Chinese snack made by coating skewered fruit in hardened sugar.

[P4]
The unexpected comment caused my brain to freeze for a moment.

[P5]
*What the hell is he talking about?*

[P6]
It wasn’t one of those *Do you know the Way?* pitches. He was asking if he could have just one candied hawthorn skewer.

[P7]
I hadn’t planned for a Peak master I’d just met to beg for candied hawthorn in the most polite tone in the world.

[P8]
*Grrrrrrowl.*

[P9]
Now he was even tugging at my pity with his stomach clock. Without thinking, I held out the candied hawthorn skewer I was still holding.

[P10]
“H-here.”

[P11]
“Thank you, Benefactor.”

[P12]
Talk about value for money. Ten seconds after meeting him, I had become a Peak master’s Benefactor.

[P13]
Hyuk Mujin and I stared blankly at Cheongpung as he ferociously bit and sucked on the candy-coated snack children usually ate.

[P14]
“Captain, do you know him?”

[P15]
“No.”

[P16]
Cheongpung devoured the candied hawthorn skewer as though it had vanished in the blink of an eye. Apparently, it hadn’t been enough, because he turned toward Hyuk Mujin with the eyes of a starving beast.

[P17]
More precisely, he stared at the two candied hawthorn skewers in Mujin’s hands.

[P18]
“…Mujin.”

[P19]
“Yes?”

[P20]
“Give them to him.”

[P21]
Hyuk Mujin quickly hid his hands behind his back.

[P22]
“No.”

[P23]
“You don’t want to?”

[P24]
“Yes. This is the first time I’ve eaten these in five years. I haven’t even taken a bite yet.”

[P25]
“I see. Our Mujin wants to die fifty years ahead of schedule.”

[P26]
“…”

[P27]
With a deep sigh, he held out the candied hawthorn skewers. Cheongpung’s eyes flashed.

[P28]
“Thank you, Benefactor!”

[P29]
The next moment, accompanied by a sharp *whoosh*, the candied hawthorn skewers had transferred into Cheongpung’s hands.

[P30]
“Gah!”

[P31]
That was an incredible speed. Hyuk Mujin sucked in a startled breath and whispered to me in a trembling voice.

[P32]
“He’s not an ordinary beggar, is he?”

[P33]
What kind of expression would Mujin make if he learned that the filthy young man in front of us was a Peak master?

[P34]
I studied Cheongpung as he inhaled the candied hawthorn with single-minded focus.

[P35]
*He looks far too young to be a Peak master.*

[P36]
I had heard a few rumors by now. I also knew that even famous, powerful sects with every kind of genius training and support only produced a Peak master once in a blue moon.

[P37]
That was why Jin Mukyung, who had come from Shanxi Province—a remote backwater even by the standards of the Central Plains—had become so famous.

[P38]
*He reached the Peak realm ten or twenty years ahead of everyone else.*

[P39]
*But…*

[P40]
The young man in front of me looked barely my age, yet he was a Peak master whose Level I couldn’t even determine through Qi Sense.

[P41]
I had never heard of a Peak master this young living in Shanxi Province.

[P42]
*Where the hell did this guy come from?*

[P43]
As if on cue, Cheongpung raised his head. Since he had eaten so hurriedly, his mouth was covered in sticky sugar.

[P44]
“Whew. That was delicious.”

[P45]
“You must’ve been a little… very hungry.”

[P46]
“Yes. I haven’t eaten all day.”

[P47]
“Oh dear. How did that happen?”

[P48]
“I lost my travel expenses. Still, it was an interesting experience.”

[P49]
“…”

[P50]
Could being forced to starve all day because you had no money really count as an interesting experience?

[P51]
I had felt it from the moment we met, but this guy definitely had a peculiar way of thinking.

[P52]
Cheongpung smiled brightly and gave us a respectful fist-and-palm salute.

[P53]
“Ah, I’m late introducing myself. Cheongpung offers his greetings to his Benefactors.”

[P54]
“My name is Jin Taekyung.”

[P55]
“I’m this man’s right arm and heart, Hyuk Mujin.”

[P56]
I completely ignored Hyuk Mujin’s nonsense and kept my eyes on Cheongpung.

[P57]
I might not look it, but I was fairly famous in Shanxi Province.

[P58]
Until a few months ago, I had been famous for all the wrong reasons. Now, for the exact opposite reasons, there wasn’t a single person in Shanxi Province who didn’t know my name.

[P59]
*I wonder if he’ll recognize me.*

[P60]
Just as I was secretly getting my hopes up, Cheongpung’s face went stiff.

[P61]
“Excuse me, are you perhaps…”

[P62]
“Yes, that’s right. I’m the very—”

[P63]
“Would it be all right if I imposed on you a little longer?”

[P64]
“What?”

[P65]
“I’ve been hungry for quite a long time.”

[P66]
Right on cue, a thunderous sound came from Cheongpung’s stomach.

[P67]
*Grrrrrrowl.*

[P68]
“…Then why don’t we have a meal together?”

[P69]
“Thank you, Benefactor!”

[P70]
I couldn’t tell whether I was his Benefactor or just a sucker.

[P71]
* * *

[P72]
The inside of Honghwa Inn was packed with people who had come for an early dinner.

[P73]
A quick-footed waiter led us to one of the few remaining empty tables.

[P74]
“What’ll it be?”

[P75]
I handed the wooden menu board to Cheongpung.

[P76]
“Order whatever you want.”

[P77]
“Oh, no, I couldn’t. I’m not some ungrateful beast who doesn’t know how to repay a kindness. How could I…”

[P78]
“It’s fine. Order whatever you want.”

[P79]
“Then I’ll have everything on here.”

[P80]
“…”

[P81]
What an ungrateful beast.

[P82]
The appearance of a colossal sucker kept the kitchen busy. Before long, the dishes we had ordered began pouring out without pause.

[P83]
“Garlic Pork is here. This dish is made by slicing boiled pork thin and…”

[P84]
“Oh.”

[P85]
“Fish-Fragrant Shredded Pork is here. It’s pork served with bamboo shoots, wood ear mushrooms, and…”

[P86]
“Ohhh.”

[P87]
“Beijing Sauce Shredded Pork.”

[P88]
“Ohhhh!”

[P89]
“Beggar’s Chicken.”

[P90]
“Ohhhhh!”

[P91]
Unlike the waiter, whose explanations had grown shorter and shorter, Cheongpung’s reactions were becoming more and more elaborate.

[P92]
Dish after dish continued filling the table. Just as there was barely any room left, the waiter pushed out another plate with the expression of a man who had reached enlightenment.

[P93]
“Maegu.”

[P94]
“Maegu?”

[P95]
I’d heard of Megumi from the island country next door, but Maegu was a new one to me. Catching my look, the waiter answered as if explaining it was a chore.

[P96]
“Maechae Guyuk.”[^2]

[P97]
“…”

[P98]
Now he was even abbreviating dish names.

[P99]
While I stared at him in disbelief, Cheongpung rapidly emptied the plates.

[P100]
[^2]: *Maechae Guyuk* is pork belly with preserved mustard greens. The waiter shortens its Korean name to *Maegu*, which sounds like the beginning of the Japanese name Megumi.

[P101]
“Nom, nom.”

[P102]
“Slow down. Eat slowly.”

[P103]
“Mmph, mmph. Ah hih he ho. Ha hu i heup hi ha.”

[P104]
“Don’t answer. Just keep eating.”

[P105]
“Khanks hah!”

[P106]
Hyuk Mujin whispered with a thoroughly disgusted expression.

[P107]
“Isn’t he really a beggar?”

[P108]
“Didn’t you see him snatch the candied hawthorn earlier? He definitely isn’t.”

[P109]
*Chomp, chomp.*

[P110]
“…Probably.”

[P111]
“What if he’s a master of the Beggars’ Sect?”

[P112]
“The Beggars’ Sect, huh?”

[P113]
I had seen it countless times in martial arts novels. It also existed openly in the actual Murim as one of the Nine Sects and One Gang.

[P114]
I had never met one of its members, but any of the beggars loitering near the inn’s entrance could be a Beggars’ Sect disciple.

[P115]
“Should I take a quick look to see whether he has any knots?”

[P116]
The masters of the Beggars’ Sect supposedly distinguished their status by the knots around their waists.

[P117]
I shook my head.

[P118]
*No. He isn’t with the Beggars’ Sect.*

[P119]
If he were, he would have reacted somehow when he heard my name. We belonged to the same orthodox faction, so he had no reason to pretend he didn’t recognize me.

[P120]
*Then what sect is he from?*

[P121]
There was no way a Peak master this young had simply dropped out of the sky.

[P122]
He had to come from a famous sect at the very least… The more I thought about it, the more curious I became about this mysterious young man.

[P123]
“Burp. That was delicious.”

[P124]
Cheongpung finally finished eating. After patting his tadpole-like belly, he looked at Hyuk Mujin and me, then stopped short.

[P125]
“It was my first time trying any of these dishes, so I made a spectacle of myself in front of my Benefactors. I hope I didn’t overdo it…”

[P126]
*You were more than excessive, you idiot.*

[P127]
Still, it was good that he had at least a little self-awareness.

[P128]
“It’s fine. I do that sometimes, too.”

[P129]
“We have something in common. Ha-ha.”

[P130]
I laughed along with Cheongpung and opened my mouth. It was time to start questioning him.

[P131]
“You said everything was your first time eating it. You don’t usually eat rich food, do you?”

[P132]
Cheongpung shook his head gloomily.

[P133]
“It’s not that I don’t eat it. I couldn’t eat it. If I’d known food this delicious existed, I would have come down from the mountain sooner.”

[P134]
“Oh, so you lived in the mountains. That must have been difficult.”

[P135]
“Life in the mountains? It was fun. The scenery was beautiful, and there was plenty to eat here and there. My grandfather has lived alone in the mountains his entire life, too.”

[P136]
“Your grandfather?”

[P137]
“Yes. But, um…”

[P138]
“Go ahead.”

[P139]
“May I order some alcohol? I’ve never had any before.”

[P140]
“…Order as much as you like.”

[P141]
This kid had a lot of things he had never tried.

[P142]
At least he still had a sliver of conscience left. He ordered the cheapest bottle of fire liquor.

[P143]
A short while later, Cheongpung downed the fire liquor without hesitation and muttered with a slightly flushed face,

[P144]
“Ahh, so this is what it means to get drunk. But what were we talking about?”

[P145]
“That your grandfather had lived alone in the mountains his entire life.”

[P146]
“Oh, right. Anyway, I lived with my grandfather from a young age. That started when I was five, so it’s already been fifteen years.”

[P147]
“Really? That’s a long time.”

[P148]
I did my best not to show my surprise.

[P149]
*A Peak master at barely twenty.*

[P150]
That meant he was a genius at least comparable to Jin Mukyung, if not greater. The more I talked with him, the more curious I became about his identity.

[P151]
“Where was it? If it’s such a nice place to live, maybe I could visit sometime.”

[P152]
Cheongpung hesitated just as he was about to say something.

[P153]
“Um, I don’t think I can tell you that.”

[P154]
“Come on. You can’t even tell me that much?”

[P155]
“Because my grandfather hates it when people visit. He moves to a different place once or twice a year because of that.”

[P156]
“He moves?”

[P157]
“Yes. Strange people keep coming to see him.”

[P158]
*Strange people? Obnoxious hikers?*

[P159]
Well, I suppose it would be annoying for someone living in the mountains.

[P160]
He continued speaking with a nostalgic look in his eyes.

[P161]
“When I was ten, dozens of people suddenly came rushing over and started causing trouble. I remember my grandfather shouting at them to get lost before he set the mountain on fire.”

[P162]
“Oh, so that’s why he keeps moving?”

[P163]
“Yes. Fortunately, the mountains are huge, so he’s been avoiding them successfully for ten years.”

[P164]
“…”

[P165]
Ten years? His grandfather was quite a man.

[P166]
Hyuk Mujin, who had been listening to Cheongpung’s story with great interest, asked,

[P167]
“Then why did Young Master come down from the mountain?”

[P168]
Cheongpung, who had been sucking on the mouth of the liquor bottle regretfully, answered,

[P169]
“Because of the Ten Dragons and Phoenixes.”

[P170]
“The Ten Dragons and Phoenixes? What’s that supposed to be?”

[P171]
At my question, Hyuk Mujin looked at me as though I were the strangest person he had ever seen.

[P172]
“Why don’t you know about the Ten Dragons and Phoenixes, Captain?”

[P173]
“I’m allowed not to know, damn it.”

[P174]
“Huh? You made a complete fool of yourself last year after getting plastered at a pleasure house and bragging that you were going to become one of them.”

[P175]
“That wasn’t me… Never mind. What are the Ten Dragons and Phoenixes?”

[P176]
“Are you seriously asking because you don’t know?”

[P177]
“Can’t I just not know?”

[P178]
“Of course you can’t. The Second Young Master is one of them, after all.”

[P179]
Wait, really?

[P180]
As I blinked at him, Hyuk Mujin launched into an impassioned explanation.

[P181]
“They’re the greatest young prodigies of the orthodox Murim! The dragons and phoenixes who will lead the Murim of the future! How can you not know about the Ten Dragons and Phoenixes?”

[P182]
“Hey, hey. Keep your voice down. People are staring.”

[P183]
He wasn’t exaggerating. Hyuk Mujin’s booming voice had drawn glances from the other customers.

[P184]
“Who cares if they stare? This is too much even for you, Captain! Are you making fun of me?”

[P185]
“I don’t know about making fun of people, but I’m good at hitting them.”

[P186]
“I think I got too worked up. I’m sorry.”

[P187]
Hyuk Mujin regained his composure in an instant. I turned away from him and gave Cheongpung a friendly smile.

[P188]
“Please continue.”

[P189]
“It’s nothing important. I just had a childish thought for a moment.”

[P190]
Cheongpung looked at me through slightly unfocused eyes. Apparently, he had no intention of using his internal energy to dispel the drunkenness, because he was still a little tipsy.

[P191]
“Who would be stronger, me or them? I wanted to find the answer to that question.”

[P192]
In the end, it was because of a martial artist’s competitive pride.

[P193]
The desire to step into a new world. The desire to defeat a strong opponent and prove his martial arts. I could tell that those feelings had led him down the mountain.

[P194]
*He seems to have the skill to justify thinking that way, too.*

[P195]
Jin Mukyung had supposedly reached the Peak realm when he was barely twenty and caused an uproar throughout the Central Plains. Now, he was counted as one of the Ten Dragons and Phoenixes, one of the greatest young prodigies of the orthodox faction.

[P196]
The Cheongpung in front of me possessed martial talent at least comparable to Jin Mukyung’s.

[P197]
*He has every right to think so.*

[P198]
I was nodding inwardly when—

[P199]
“Puhahaha!”

[P200]
“Pfft, hahahaha. Ah, holding back my laughter was torture.”

[P201]
I raised my head toward the source of the sound.

[P202]
On the second floor, five men and women in silk clothes were looking down at us with faces full of mockery.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 은인     | **Benefactor**                               |
| 레벨               | **Level**                      |
| 산서     | **Shanxi**             |
| 공자      | **Young Master**                                                |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 메구미 | **Megumi** | Japanese name used in Taekyung's joke about the abbreviated dish name. |
| 산니백육 | **Garlic Pork** | Boiled pork sliced thin and served with garlic sauce. |
| 어향육사 | **Fish-Fragrant Shredded Pork** | Shredded pork dish. |
| 경장육사 | **Beijing Sauce Shredded Pork** | Shredded pork dish. |
| 규화계 | **Beggar's Chicken** | Named inn dish. |
| 매구 | **Maegu** | Waiter's shortened name for Maechae Guyuk. |
| 매채구육 | **Maechae Guyuk** | Pork belly with preserved mustard greens; the abbreviation is explained in a footnote. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 132,
  "passed": true,
  "metrics": {
    "source_characters": 5893,
    "translation_characters": 13272,
    "length_ratio": 2.252,
    "source_paragraphs": 199,
    "translation_paragraphs": 201
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
        "korean": "후기지수",
        "preferred": "young prodigy / rising martial artist"
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
        "korean": "규화계",
        "preferred": "Beggar's Chicken"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "개방",
        "preferred": "Beggars' Sect"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "푸하하하",
        "romanization": "puhahaha"
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
