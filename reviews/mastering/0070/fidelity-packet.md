# Fidelity Gate — Chapter 70

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
  1|＃70화
  2|
  3|
  4|
  5|밖은 어스름한 새벽이었다. 겨울철 공기는 얼음장처럼 차가웠고 걸을 때마다 연무장 바닥에 낀 서리가 바스러졌다.
  6|
  7|미리 몸을 풀고 있던 진무경이 나를 보며 씩 웃었다.
  8|
  9|“그래, 마음의 준비는 끝났고?”
 10|
 11|당연히 아니지. 하지만 쓰린 속을 감추고 고개를 끄덕였다.
 12|
 13|누가 그랬다. 피할 수 없다면 즐기라고. 강해지는 과정 중 하나라고 생각하니 마음이 한결 편안…….
 14|
 15|스르릉.
 16|
 17|“그럼 그 대단한 실력 좀 보자.”
 18|
 19|이 새끼 한국인인가. 성격이 왜 이렇게 급해?
 20|
 21|피할 시간도 없다. 순식간에 코앞까지 짓쳐 든 진무경을 향해 황급히 창대를 휘둘렀다.
 22|
 23|캉! 카가가각!
 24|
 25|서로 맞댄 무기 너머로 진무경의 입김이 흘러나온다.
 26|
 27|“자세는 제법이구나.”
 28|
 29|그럴 수밖에. 목숨이 왔다 갔다 하는 게이트에서 7년을 창 하나로 버틴 나다. 권각술과는 쌓인 깜냥부터 다르다.
 30|
 31|나는 녀석의 눈을 노려보며 대답했다.
 32|
 33|“이번에는 쉽지 않을 겁니다.”
 34|
 35|한 글자씩. 또박또박.
 36|
 37|“너…….”
 38|
 39|범상치 않은 내 기세를 느낀 걸까? 진무경의 눈동자가 파르르 떨렸다.
 40|
 41|“눈깔 똑바로 안 떠?”
 42|
 43|“아.”
 44|
 45|
 46|
 47|* * *
 48|
 49|
 50|
 51|스르륵. 쿵!
 52|
 53|진태경이 쓰러졌다. 그리 놀라운 일은 아니다. 벌써 다섯 번째 기절이니까. 정말 놀랄 만한 일은 따로 있다.
 54|
 55|‘날 상대로 이백 합을 버틸 줄이야.’
 56|
 57|두 시진 동안 이어진 다섯 번의 비무.
 58|
 59|사람이라면 응당 지치기 마련이다. 하지만 진태경은 달랐다. 오뚝이처럼 일어났고 점점 강해졌다. 결국 마지막에는 진무경도 진심으로 상대해야 했다.
 60|
 61|‘이 녀석, 정체가 뭐야?’
 62|
 63|적수공권일 때는 여든 먹은 노인네처럼 엉거주춤하던 동생. 그러나 창을 잡자 모든 것이 달라졌다.
 64|
 65|맞기 싫어 살살 비위를 맞추던 겁쟁이는 어디 가고 노련한 창수(槍手)가 그곳에 있었다.
 66|
 67|‘낭인 같았다. 수도 없이 죽음의 위기를 넘긴.’
 68|
 69|투박해 보일 정도로 간결한 움직임, 스스로의 직감에 의존하는 변칙적인 공격과 회피. 낭인의 싸움에는 정해진 것이 없다. 진무경의 눈에 비친 진태경이 바로 그랬다.
 70|
 71|그렇기에 더욱 큰 의문이 남는 거고.
 72|
 73|‘도대체 어떻게?’
 74|
 75|걸음마와 동시에 검을 잡는 명문가의 자제들도 일류 언저리만 기웃거리는 놈들이 부지기수다. 한데 저놈은 삼 년 만에 절정의 벽 앞에 섰다.
 76|
 77|그것도 기녀들의 분 냄새가 아닌, 노련한 낭인의 냄새를 풀풀 풍기면서. 생각할수록 기가 찼다.
 78|
 79|‘이게 가능한 일인가?’
 80|
 81|가능하긴 하다. 초절정 고수의 벌모세수, 영약을 이용한 체질 개선. 그다음 피똥 쌀 만큼 창을 휘두르며 실전 경험을 쌓으면 된다. 삼 년간 하루도 빠짐없이!
 82|
 83|“……말도 안 되는 소리지.”
 84|
 85|허탈한 목소리로 중얼거린 진무경이 머리를 벅벅 긁었다.
 86|
 87|그렇다면 이제 남은 답은 하나밖에 없다.
 88|
 89|‘천재.’
 90|
 91|이 단어 하나면 모든 의문이 명쾌하게 해결된다.
 92|
 93|왜? 천재니까. 말 그대로 하늘이 내린 놈. 재능을 타고난 놈이니까. 모든 면에서 천재는 앞서간다. 출발점부터가 다르다.
 94|
 95|“드르렁. 푸우.”
 96|
 97|“…….”
 98|
 99|그런데 하필 이런 놈이 천재라고?
100|
101|그럴 리가 없다. 그래서는 안 되는 거다! 문득 분노가 치밀어 오른 진무경은 동생의 엉덩이를 걷어찼다.
102|
103|“푸루루루룹.”
104|
105|데굴데굴 굴러간 진태경이 몸을 부르르 떨었다.
106|
107|“워, 월화 누나. 거긴 안 돼요.”
108|
109|“……!”
110|
111|“갑자기 이러시면. 앗. 아아!”
112|
113|뚜둑.
114|
115|실오라기 같던 마지막 인내심이 끊어졌다.
116|
117|
118|
119|* * *
120|
121|
122|
123|삐빅!
124|
125|
126|
127|- 수면 모드가 강제 종료 됩니다!
128|
129|
130|
131|이거 강제 종료도 되는 거였구나.
132|
133|새로운 기능을 알았다는 기쁨도 잠시였다. 수면 모드가 왜 강제 종료 됐겠는가. 누가 깨우니까 종료된 거지.
134|
135|“신성한, 연무장에서, 뭐? 거긴 안 돼요? 안 돼요?”
136|
137|뻑! 뻑! 뻑!
138|
139|새우처럼 웅크린 나는 죽어 가는 목소리로 말했다.
140|
141|“살려 주세요…….”
142|
143|“안 돼요!”
144|
145|퍼버버벅!
146|
147|정확히 몇 대를 맞았는지 모르겠다. 중간에 두 번 정도 의식이 끊겼기 때문이다.
148|
149|마지막 힘을 쥐어짜 연무장에 다잉 메시지를 남기다가 쓰러진 것이 마지막 기억이었고, 눈을 떠 보니 이미 밤이었다.
150|
151|‘뭐 했다고 벌써 밤이냐.’
152|
153|시간 여행자가 된 기분이다. 진무경을 만난 후로는 아주 그냥 하루가 휙휙 지나간다. 나는 전신을 엄습하는 통증을 느끼며 중얼거렸다.
154|
155|“진무경, 세긴 세다.”
156|
157|진무경을 제외한다면 지금까지 내가 상대한 절정 고수는 두 명이다. 대장로, 그리고 조필.
158|
159|‘그중에서 대장로는 제외.’
160|
161|대장로의 경우는 천운이 따랐다고 봐야 한다. 그는 태원진가 무인들의 희생과 이천백의 기습이 아니었다면 죽었다 깨어나도 이길 수 없는 고수였다.
162|
163|‘그럼 조필과 진무경을 비교한다면?’
164|
165|고민은 그리 길지 않았다.
166|
167|두 명 모두 겪어 봤기에 선택은 쉬웠다.
168|
169|‘진무경이 더 강해.’
170|
171|조필은 분명 괴물 같은 놈이다. 화염신장에서 뿜어져 나오는 무지막지한 열기를 떠올리면 지금도 소름이 돋는다.
172|
173|하지만 뭐랄까, 절정 고수답게 강하고 화염신장이라는 치명적인 무공을 사용했지만 그게 전부였다.
174|
175|‘정확히는 무공의 활용 차이라고 해야겠지.’
176|
177|진무경은 조필과 다르다. 그는 비무 중에도 최소 십여 개의 무공을 사용하며 내 공격을 철저히 차단했다.
178|
179|무림인에게 무공이란 또 다른 무기다. 진무경은 적재적소에 알맞은 무기를 꺼내 쓸 줄 아는 녀석이다.
180|
181|‘그에 비하면 나는?’
182|
183|처음부터 있었던 진가심법은 제외. 무림에서 익힌 무공이라고는 진가창법과 진가보법 두 개가 전부다.
184|
185|물론 둘 다 의심할 여지가 없는 일류 무공이지만…… 바꿔 말하면 딱 일류 수준에서나 쓸 만한 무공이라는 말도 된다.
186|
187|무공의 한계. 내가 느낀 것을 진위경이 모를 리 없다.
188|
189|‘그게 나를 진무경한테 붙여 준 이유고. 윽.’
190|
191|고통에 절로 눈살이 찌푸려진다. 상반신을 조금 일으켰을 뿐인데, 전신의 뼈마디가 욱신거리고 살갗이 아려 왔다.
192|
193|수면 모드를 통한 휴식에도 한계가 있었던 모양이다.
194|
195|‘하긴, 그렇게 얻어맞았으니.’
196|
197|진무경의 인정을 받아 퀘스트를 완료하려면 오늘 같은, 아니 오늘보다 더한 날들을 보내야 한다.
198|
199|어쩌면 흠씬 두들겨 맞기만 하고 퀘스트까지 실패할지 모른다.
200|
201|‘산 넘어 산이군.’
202|
203|그래서 기쁘다.
204|
205|F급 헌터였던 내게는 산을 오를 수 있는 자격조차 주어지지 않았으니까. 하지만 모든 것이 달라졌다.
206|
207|넘어야 할 산이 있고, 그 산에 오를 자격이 주어졌다. 그것도 누구보다 빠르게!
208|
209|‘이럴 때가 아니지.’
210|
211|나는 통증도 잊은 채 자리에서 일어났다. 덧없이 흘려보내는 1분 1초가 아쉬웠다.
212|
213|
214|
215|* * *
216|
217|
218|
219|진무경은 지하 연무장에 있었다. 최대한 발소리를 죽이며 지하로 통하는 계단을 내려가자 그의 모습이 보였다.
220|
221|“합!”
222|
223|짧은 기합성과 함께 검이 움직였다.
224|
225|쉭! 쉬쉬쉭!
226|
227|검신을 따라 바람이 갈라진다. 빛살 같은 속도로 허공을 찌르고 베어 내는 진무경의 움직임은 거침없었다.
228|
229|그렇게 일각 정도가 흘렀을까? 검을 내린 진무경이 긴 날숨을 토해 냈다.
230|
231|“후우.”
232|
233|소매로 땀을 훔친 그가 나를 향해 고개를 돌렸다.
234|
235|이미 아까 전부터 내 존재를 눈치채고 있었던 모양이다.
236|
237|“말해 봐.”
238|
239|뜬금없는 한마디.
240|
241|당황한 나는 엉겁결에 반문했다.
242|
243|“뭐, 뭘요?
244|
245|“내가 방금 펼친 무공에 대해서.”
246|
247|“어, 그게 일단 굉장히 빠…….”
248|
249|“참고로 빠르다, 강하다. 이딴 헛소리 지껄이면 죽는다.”
250|
251|귀신이네. 나는 살기 위해 머리를 쥐어짰다.
252|
253|진무경의 무공이 어땠더라? 곰곰이 생각해 보니 희미하게 떠오르는 느낌이 있었다.
254|
255|“거칠다?”
256|
257|진무경의 눈썹이 꿈틀거렸다. 정답인가?
258|
259|“너 지금 나한테 말 놓은 거냐?”
260|
261|“……거칠었던 것 같아요.”
262|
263|“그따위 말은 삼척동자도 할 수 있어. 더 자세히.”
264|
265|머릿속의 이미지가 점점 또렷해진다. 허상의 적을 향해 쏟아지던 검날과 움직임이 떠올랐다. 빠르고, 거침없는 동작들. 그리고 사방을 짓누르던 기세.
266|
267|그건 마치…….
268|
269|“폭포?”
270|
271|“…….”
272|
273|“엥?”
274|
275|뭐야, 정답이야?
276|
277|한동안 말이 없던 진무경이 돌연 검집을 휘둘렀다.
278|
279|딱!
280|
281|“악! 왜 때려요!”
282|
283|“그냥.”
284|
285|그가 묘한 눈빛으로 나를 응시했다.
286|
287|“어쩌다 너 같은 놈이 나왔을까?”
288|
289|저게 욕일까, 칭찬일까.
290|
291|속뜻이 뭔지는 모르겠지만 질문에 대한 답은 억울해서라도 들어야겠다. 나는 욱신거리는 이마를 문지르며 물었다.
292|
293|“그래서, 정답입니까?”
294|
295|“천무학관에는 수천 권의 무공 비급이 존재한다. 정파 무림의 후학 양성을 생각한 선배 고인들의 안배지.”
296|
297|“그런데요?”
298|
299|“방금 네가 본 낙류검(落流劍)도 그중 하나다. 서고 깊숙이 파묻혀 있었던 것을 내가 찾아냈지.”
300|
301|낙류. 풀이하자면 떨어지는 물의 흐름. 즉, 폭포다.
302|
303|그냥 생각나는 대로 말한 건데 설마 정답일 줄이야.
304|
305|“오, 오오.”
306|
307|설마 나, 진짜 천재인 건가? 무공 입문 두 달 만에 이 정도면 앞으로 얼마나 강해질지 내가 생각해도 나 스스로가 무서워진다.
308|
309|“설마 겨우 이 정도로 난 천재니, 뭐니 하는 낯부끄러운 생각을 하는 건 아니겠지?”
310|
311|“…….”
312|
313|진짜 귀신이네. 그래도 조금은 재능이 있는 것 같은데.
314|
315|나는 미련을 버리지 못하고 조심스럽게 물었다.
316|
317|“원래 다들 이 정도는 하는 건가요?”
318|
319|내 질문에 진무경이 순간 움찔했다.
320|
321|“그, 그럼. 눈 달린 놈이면 이 정도는 맞춰야지.”
322|
323|“에이.”
324|
325|“에이? 눈깔 하나 뽑아 줘?”
326|
327|“……그건 좀.”
328|
329|이 자식은 오늘따라 유난히 정색하네. 무슨 기분 나쁜 일이라도 있나. 한발 물러났는데도 진무경은 화를 삭이지 못하고 씨근덕거렸다.
330|
331|“기본이야, 기본. 누구나 다 하는 거라고.”
332|
333|“알았다니까요. 왜 자꾸 화를 내고 그러세요? 무섭게.”
334|
335|“너 지금 반항하냐? 질풍노도의 시기라서 질풍십이권으로 맞고 싶어?”
336|
337|질풍십이권이 뭔지는 모르겠지만 맞으면 아플 것 같다.
338|
339|맹렬히 고개를 흔들었지만 진무경의 화는 좀처럼 가라앉지 않았다.
340|
341|“네가 무공을 알아? 어?”
342|
343|“모, 모릅니다.”
344|
345|“너 무공 익힌 지 얼마나 됐어.”
346|
347|반사적으로 대답이 튀어 나갔다.
348|
349|“두 달, 두 달이요.”
350|
351|“그래, 두 달밖에 안 된 놈이…… 뭐? 두 달?”
352|
353|진무경이 핏줄 선 눈동자로 나를 노려본다.
354|
355|“삼 년이 아니라 두 달?”
356|
357|다급한 상황. 7년의 사회생활을 통해 얻은 눈치가 빛을 발하는 순간이다. 나는 재빨리 입을 열었다. 특히 일정 부분을 강조하는 것도 잊지 않고.
358|
359|“삼 년 하고도! 두 달이요.”
360|
361|풍 맞은 것처럼 부들거리던 진무경의 주먹이 안정을 되찾았다. 왠지는 몰라도 목소리까지 살짝 온화해진 느낌이다.
362|
363|“자식이, 깜짝 놀랐네.”
364|
365|내가 더 놀랐다. 이 새끼야…….
366|
367|‘분노 조절 장애인가.’
368|
369|진위경에게 물어보면 금방 들통나겠지만, 적어도 지금 당장 질풍십이권을 체험하는 불상사는 일어나지 않을 것이다.
370|
371|어쨌건 그사이에 진무경의 분노는 수그러들었다.
372|
373|“딱 한 번 말한다. 잘 들어.”
374|
375|“가슴에 새기겠습니다.”
376|
377|내가 넙죽 고개를 숙이자 그가 고압적인 자세로 선언했다.
378|
379|“난 가르치고, 넌 복종한다.”
380|
381|“…….”
382|
383|애견 훈련소야 뭐야.
384|
385|“반론은 없다. 왜? 내가 너보다 강하니까.”
386|
387|맞는 말이라 반박할 생각도 들지 않는다.
388|
389|돈, 권력, 무력. 형태는 달라도 세상은 강자를 중심으로 돌아가는 법이니까. 나는 그 중심에 서고 싶다.
390|
391|“어찌하겠느냐?”
392|
393|아주 오래전부터, 내 대답은 정해져 있었다.
```

## Assembled English

```markdown
[P1]
# Chapter 70

[P2]
Outside, dawn was dim. The winter air was cold as ice, and frost crumbled underfoot with every step across the training ground.

[P3]
Jin Mukyung, who had already been warming up, grinned at me.

[P4]
“Well? Are you mentally prepared?”

[P5]
Of course not. But I hid my churning stomach and nodded.

[P6]
Someone once said that if you couldn’t avoid something, you should enjoy it. Thinking of this as just another step toward becoming stronger made me feel a little more at ease…

[P7]
Shing.

[P8]
“Then let’s see that impressive skill of yours.”

[P9]
*Is this bastard Korean? Why is he so impatient?*

[P10]
I had no time to avoid him. Jin Mukyung rushed toward me in an instant, and I hurriedly swung my spear shaft at him.

[P11]
Clang! Kaga-gang!

[P12]
Jin Mukyung’s breath drifted between us over our locked weapons.

[P13]
“Your stance isn’t bad.”

[P14]
It had to be. I had survived seven years in a Gate where my life had been on the line, using nothing but a spear. The experience I’d built up with the spear was on a completely different level from my fists and kicks.

[P15]
I glared into his eyes and answered.

[P16]
“This time, it won’t be easy.”

[P17]
One word at a time. Clearly and distinctly.

[P18]
“You…”

[P19]
Had he sensed my unusual aura? Jin Mukyung’s eyes trembled.

[P20]
“Can’t you keep your damn eyes open?”

[P21]
“Oh.”

[P22]
* * *

[P23]
Swoosh. Thud!

[P24]
Jin Taekyung collapsed.

[P25]
It was hardly surprising. This was already his fifth knockout.

[P26]
The real surprise lay elsewhere.

[P27]
*I can’t believe he lasted two hundred exchanges against me.*

[P28]
Five spars over two shichen—roughly four hours.

[P29]
Anyone would have been exhausted. But Jin Taekyung was different. He kept springing back up like a roly-poly toy, growing stronger each time. By the final spar, even Jin Mukyung had been forced to take him seriously.

[P30]
*What the hell is this guy?*

[P31]
Unarmed, his movements had been as clumsy as those of an eighty-year-old man. But the moment he picked up a spear, everything changed.

[P32]
The coward who had fawned over Jin Mukyung to avoid getting hit had vanished. In his place stood a seasoned spearman.

[P33]
*He was like a wandering martial artist. Someone who had survived countless brushes with death.*

[P34]
His movements were so simple they seemed crude, while his irregular attacks and evasions relied entirely on instinct. A wandering martial artist’s fighting style followed no fixed pattern.

[P35]
That was exactly what Jin Taekyung looked like to Jin Mukyung.

[P36]
Which only made the question more baffling.

[P37]
*How?*

[P38]
Even among the heirs of prestigious families who picked up a sword as soon as they learned to walk, countless people only hovered around the threshold of First Rate. Yet this man had stood before the wall of the Peak realm in just three years.

[P39]
And he did it while giving off not the scent of a courtesan’s powder, but the strong scent of a seasoned wandering martial artist. The more Jin Mukyung thought about it, the more absurd it seemed.

[P40]
*Was something like this even possible?*

[P41]
Technically, yes.

[P42]
Having a Supreme Peak master cleanse his tendons and marrow. Improving his constitution with elixirs. Then swinging a spear until he shit blood while building real combat experience.

[P43]
Every single day for three years!

[P44]
“…That’s ridiculous.”

[P45]
Jin Mukyung muttered hollowly and scratched his head.

[P46]
Then only one answer remained.

[P47]
*A genius.*

[P48]
That one word resolved every question with perfect clarity.

[P49]
Why?

[P50]
Because he was a genius. Someone blessed by heaven, just as the word implied. Someone born with talent.

[P51]
Geniuses were ahead in every way. They started from a completely different place.

[P52]
“Zzz… Hoo…”

[P53]
“…”

[P54]
But of all people, this guy was a genius?

[P55]
That was impossible. It couldn’t be allowed!

[P56]
Anger suddenly surged within Jin Mukyung, and he kicked his younger brother in the rear.

[P57]
“Prrrblblbl.”

[P58]
Jin Taekyung rolled away several times before shuddering all over.

[P59]
“W-Wolhwa noona. Not there.”

[P60]
“…!”

[P61]
“If you suddenly do this… Ah. Aah!”

[P62]
Crack.

[P63]
The last thread of Jin Mukyung’s patience snapped.

[P64]
* * *

[P65]
Beep!

[P66]
> **System**
>
> - Sleep Mode has been forcibly terminated!

[P67]
*So it can be forcibly terminated?*

[P68]
My joy at discovering a new function lasted only a moment. Why had Sleep Mode been forcibly terminated?

[P69]
Because someone had woken me up, obviously.

[P70]
“On the sacred training ground, you say what? ‘Not there’? ‘Not there’?”

[P71]
Whack! Whack! Whack!

[P72]
Curled up like a shrimp, I pleaded in a dying voice.

[P73]
“Please, spare me…”

[P74]
“No!”

[P75]
Thwack-thwack-thwack!

[P76]
I had no idea how many times he hit me. I lost consciousness twice in the middle of it.

[P77]
My last memory was of collapsing while using the last of my strength to leave a dying message on the training ground. When I opened my eyes, it was already night.

[P78]
*What did I even do for it to be night already?*

[P79]
I felt like a time traveler. Ever since I had met Jin Mukyung, entire days had been flying by.

[P80]
Pain swept through my body as I muttered, “Jin Mukyung really is strong.”

[P81]
Excluding Jin Mukyung, I had faced two Peak masters so far.

[P82]
The Head Elder and Jopil.

[P83]
*The Head Elder doesn’t count.*

[P84]
In his case, I had to admit that luck had been on my side. If not for the sacrifices of the Jin Family of Taiyuan’s martial artists and Lee Cheonbaek’s surprise attack, he was a master I could never have defeated in a million years.

[P85]
*Then how does Jopil compare to Jin Mukyung?*

[P86]
I did not have to think for long.

[P87]
I had fought both of them, so the choice was easy.

[P88]
*Jin Mukyung is stronger.*

[P89]
Jopil was unquestionably a monster. Even now, I got goose bumps whenever I remembered the savage heat pouring from his Flame Divine Palm.

[P90]
But how should I put it? He was strong like a Peak master, and he used the deadly Flame Divine Palm, but that was all.

[P91]
*More precisely, it was a difference in how they used their martial arts.*

[P92]
Jin Mukyung was different from Jopil. Even during our spar, he had used more than ten different martial arts to completely shut down my attacks.

[P93]
To a martial artist, martial arts were another weapon. Jin Mukyung knew how to draw out the right weapon at exactly the right moment.

[P94]
*Compared to him, what did I have?*

[P95]
Setting aside the Jin Family’s Cultivation Technique, which I had possessed from the beginning, the only martial arts I had learned in Murim were the Jin Family’s Spear Technique and the Jin Family’s Manoeuvre Technique.

[P96]
Of course, both were unquestionably First Rate martial arts.

[P97]
But put another way, they were only useful at the First Rate level.

[P98]
The limitations of my martial arts. There was no way Jin Wikyung had failed to notice what I had felt.

[P99]
*That must be why he put me with Jin Mukyung. Ugh.*

[P100]
The pain made my brow furrow on its own. I had barely raised my upper body, yet every joint throbbed and my skin stung.

[P101]
Apparently, even the rest provided by Sleep Mode had its limits.

[P102]
*Well, I did get beaten half to death.*

[P103]
To complete the Quest by earning Jin Mukyung’s recognition, I would have to endure days like today—or even worse ones.

[P104]
Maybe I would simply get beaten senseless and fail the Quest anyway.

[P105]
*It really is one mountain after another.*

[P106]
And that made me happy.

[P107]
As an F-rank Hunter, I had not even been given the right to climb a mountain. But everything had changed.

[P108]
There was a mountain I had to climb, and I had been given the right to climb it.

[P109]
Faster than anyone else!

[P110]
*This isn’t the time for this.*

[P111]
Forgetting the pain, I rose. I could not bear to waste another minute or second.

[P112]
* * *

[P113]
Jin Mukyung was in the underground training ground.

[P114]
I descended the stairs as quietly as possible and spotted him below.

[P115]
“Hah!”

[P116]
With a short shout, his sword moved.

[P117]
Whoosh! Shh-shh-shhk!

[P118]
The wind split along the blade.

[P119]
Jin Mukyung moved without hesitation, thrusting and slashing through empty space at the speed of a ray of light.

[P120]
About fifteen minutes passed before he lowered his sword and released a long breath.

[P121]
“Hoo.”

[P122]
He wiped away his sweat with his sleeve, then turned toward me.

[P123]
It seemed he had noticed my presence some time ago.

[P124]
“Tell me.”

[P125]
The words came out of nowhere.

[P126]
Caught off guard, I asked, “Tell you what?”

[P127]
“About the martial art I just performed.”

[P128]
“Uh, well, first of all, it was really fast…”

[P129]
“For the record, if you spout pointless bullshit like ‘It was fast’ or ‘It was strong,’ I’ll kill you.”

[P130]
*He’s a mind reader.*

[P131]
I racked my brain for an answer that would keep me alive.

[P132]
What had Jin Mukyung’s martial art been like?

[P133]
As I thought about it carefully, a vague impression began to surface.

[P134]
“Rough?”

[P135]
Jin Mukyung’s eyebrow twitched.

[P136]
*Was that the right answer?*

[P137]
“Did you just speak informally to me?”

[P138]
“…It seemed rough.”

[P139]
“Even a little kid could say that. Be more specific.”

[P140]
The image in my head gradually became clearer.

[P141]
I remembered the blade pouring down upon an imaginary enemy and the movements that accompanied it. Fast and unrestrained. And the aura pressing down from every direction.

[P142]
It was like…

[P143]
“A waterfall?”

[P144]
“…”

[P145]
“Huh?”

[P146]
*What? Was that the right answer?*

[P147]
After a long silence, Jin Mukyung abruptly swung his scabbard.

[P148]
Smack!

[P149]
“Ow! Why did you hit me?”

[P150]
“Just because.”

[P151]
He stared at me with a strange look in his eyes.

[P152]
“How did someone like you ever come out?”

[P153]
Was that an insult or a compliment?

[P154]
I had no idea what he truly meant, but I had to hear the answer to his question if only because I felt wronged. Rubbing my throbbing forehead, I asked:

[P155]
“So, was that the correct answer?”

[P156]
“There are thousands of martial arts manuals in Heaven’s Gate Temple. They were arrangements left behind by the departed Seniors who hoped to cultivate the younger generation of the orthodox Murim.”

[P157]
“And?”

[P158]
“The Falling Flow Sword you just saw is one of them. I found it buried deep in the archives.”

[P159]
Falling flow. In other words, falling water.

[P160]
A waterfall.

[P161]
I had simply blurted out the first thing that came to mind, but it had actually been the right answer.

[P162]
“Oh, ooh.”

[P163]
*Am I really a genius?*

[P164]
If I could recognize martial arts like this after only two months of learning them, I was afraid of how strong I might become in the future. Even I found myself frightening.

[P165]
“Surely you’re not having the embarrassing thought that you’re a genius or something after managing only that much?”

[P166]
“…”

[P167]
*He really is a mind reader.*

[P168]
Still, I seemed to have at least a little talent.

[P169]
Unable to let go of the thought, I cautiously asked, “Can everyone normally do this much?”

[P170]
Jin Mukyung flinched.

[P171]
“O-Of course. Anyone with eyes should be able to guess this much.”

[P172]
“Come on.”

[P173]
“‘Come on’? Want me to pluck out one of your eyes?”

[P174]
“…That might be a bit much.”

[P175]
*Why is this bastard being especially stone-faced today? Did something unpleasant happen?*

[P176]
Even after I backed down, Jin Mukyung could not contain his anger. He kept huffing angrily.

[P177]
“It’s basic. Basic. Everyone can do it.”

[P178]
“I said I get it. Why do you keep getting angry? You’re scaring me.”

[P179]
“Are you rebelling against me? Is it because you’re going through the storm-and-stress stage of adolescence? Do you want to get beaten with the Twelve Gale Fists?”

[P180]
I did not know what the Twelve Gale Fists were, but getting hit by them sounded painful.

[P181]
I shook my head fiercely, but Jin Mukyung’s anger showed no sign of fading.

[P182]
“Do you know martial arts? Huh?”

[P183]
“N-No, sir.”

[P184]
“How long have you been learning martial arts?”

[P185]
The answer slipped out reflexively.

[P186]
“Two months. Two months.”

[P187]
“Right, a bastard who’s only been at it for two months… What? Two months?”

[P188]
Jin Mukyung glared at me with bloodshot eyes.

[P189]
“Not three years, but two months?”

[P190]
This was an emergency.

[P191]
The social instincts I had gained through seven years of working life shone at that moment. I hurriedly opened my mouth, making sure to emphasize one particular part.

[P192]
“Three years! Plus two months!”

[P193]
Jin Mukyung’s fist had been trembling as though he had suffered a stroke, but it steadied again. For some reason, even his voice seemed slightly gentler.

[P194]
“You little bastard. You startled me.”

[P195]
*You startled me even more, you son of a bitch.*

[P196]
*Does he have anger-management issues?*

[P197]
If he asked Jin Wikyung, my lie would be exposed immediately. But at least I would avoid the misfortune of experiencing the Twelve Gale Fists right now.

[P198]
In any case, Jin Mukyung’s anger subsided in the meantime.

[P199]
“I’ll say this only once. Listen carefully.”

[P200]
“I’ll engrave it on my heart.”

[P201]
I bowed deeply, and he declared in a domineering tone, “I teach. You obey.”

[P202]
“…”

[P203]
*Is this a dog-training school or what?*

[P204]
“There will be no objections. Why? Because I’m stronger than you.”

[P205]
It was true, so I had no desire to argue.

[P206]
Money, power, and force. Their forms might differ, but the world always revolved around the strong.

[P207]
I wanted to stand at its center.

[P208]
“What will you do?”

[P209]
My answer had been decided a long time ago.
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
# Chapter 70

[P2]
Outside, dawn was dim. The winter air was cold as ice, and frost crumbled underfoot with every step across the training ground.

[P3]
Jin Mukyung, who had already been warming up, grinned at me.

[P4]
“Well, have you finished preparing yourself mentally?”

[P5]
Of course not. But I hid my churning stomach and nodded.

[P6]
Someone once said that if you couldn’t avoid something, you should enjoy it. When I thought of this as just another part of becoming stronger, I felt a little more at ease…

[P7]
Shing.

[P8]
“Then let’s see that impressive skill of yours.”

[P9]
*Is this bastard Korean? Why is he so impatient?*

[P10]
I had no time to avoid him. Jin Mukyung rushed toward me in an instant, and I hurriedly swung my spear shaft at him.

[P11]
Clang! Kaga-gang!

[P12]
Jin Mukyung’s breath drifted between us through the weapons we had crossed.

[P13]
“Your stance isn’t bad.”

[P14]
It had to be. I had survived seven years in a Gate where my life had been on the line, using nothing but a spear. The experience I’d built up with the spear was on a completely different level from my fists and kicks.

[P15]
I glared into his eyes and answered.

[P16]
“This time, it won’t be easy.”

[P17]
One word at a time. Clearly and distinctly.

[P18]
“You…”

[P19]
Perhaps he sensed that something about my momentum was different. Jin Mukyung’s pupils trembled.

[P20]
“Can’t you keep your damn eyes open?”

[P21]
“Oh.”

[P22]
* * *

[P23]
Swoosh. Thud!

[P24]
Jin Taekyung collapsed. It was not particularly surprising. This was already his fifth knockout.

[P25]
The truly surprising thing was something else.

[P26]
*I can’t believe he lasted two hundred exchanges against me.*

[P27]
Five spars over two hours.

[P28]
Anyone would naturally become exhausted. But Jin Taekyung was different. He kept getting back up like a roly-poly toy, growing stronger each time. By the end, even Jin Mukyung had been forced to face him seriously.

[P29]
*What the hell is this guy?*

[P30]
When he fought unarmed, his movements had been awkward enough to resemble those of an eighty-year-old man. But the moment he picked up a spear, everything changed.

[P31]
The coward who had fawned over Jin Mukyung to avoid getting hit had vanished. In his place stood a seasoned spearman.

[P32]
*He was like a wandering martial artist. Someone who had survived countless brushes with death.*

[P33]
His movements were simple to the point of seeming crude. His attacks and evasions were irregular, relying on his own instincts. There was nothing fixed about the way a wandering martial artist fought.

[P34]
That was exactly what Jin Taekyung looked like to Jin Mukyung.

[P35]
And that was why the question only grew larger.

[P36]
*How?*

[P37]
Even among the heirs of prestigious families who picked up a sword as soon as they learned to walk, countless people only hovered around the threshold of First Rate. Yet this man had stood before the wall of the Peak realm in just three years.

[P38]
And he did it while giving off not the scent of a courtesan’s powder, but the strong scent of a seasoned wandering martial artist. The more Jin Mukyung thought about it, the more absurd it seemed.

[P39]
*Was something like this even possible?*

[P40]
It was possible.

[P41]
Having a Supreme Peak master cleanse his tendons and marrow. Improving his constitution with elixirs. Then swinging a spear until he shit blood while building real combat experience.

[P42]
For three years without missing a single day!

[P43]
“…That’s ridiculous.”

[P44]
Jin Mukyung muttered hollowly and scratched his head.

[P45]
If that was the case, only one answer remained.

[P46]
*A genius.*

[P47]
That one word resolved every question with perfect clarity.

[P48]
Why?

[P49]
Because he was a genius. Someone blessed by heaven, just as the word implied. Someone born with talent.

[P50]
Geniuses were ahead in every way. They started from a completely different place.

[P51]
“Zzz… Hoo…”

[P52]
“…”

[P53]
But of all people, this guy was a genius?

[P54]
That was impossible. It couldn’t be true!

[P55]
A sudden surge of anger rose within Jin Mukyung, and he kicked his younger brother in the rear.

[P56]
“Prrrblblbl.”

[P57]
Jin Taekyung rolled away several times before shuddering all over.

[P58]
“W-Wolhwa noona. Not there.”

[P59]
“…”

[P60]
“If you suddenly do this… Ah. Aah!”

[P61]
Crack.

[P62]
The last thread of Jin Mukyung’s patience snapped.

[P63]
* * *

[P64]
Beep!

[P65]
> **System**
>
> - Sleep Mode has been forcibly terminated!

[P66]
*So it can be forcibly terminated?*

[P67]
My joy at discovering a new function lasted only a moment. Why had Sleep Mode been forcibly terminated?

[P68]
Because someone had woken me up, obviously.

[P69]
“In the sacred training hall, you say what? ‘Not there’? ‘Not there’?”

[P70]
Whack! Whack! Whack!

[P71]
I curled up like a shrimp and spoke in a dying voice.

[P72]
“Please, spare me…”

[P73]
“No!”

[P74]
Thwack-thwack-thwack!

[P75]
I had no idea how many times I was hit. My consciousness had cut out twice in the middle of it.

[P76]
My last memory was of squeezing out my remaining strength to leave a dying message on the training hall floor before collapsing.

[P77]
When I opened my eyes, it was already night.

[P78]
*What did I do for it to be night already?*

[P79]
I felt like a time traveler. Ever since I had met Jin Mukyung, entire days had been flying by.

[P80]
I muttered as pain swept through my entire body.

[P81]
“Jin Mukyung is really strong.”

[P82]
Excluding Jin Mukyung, I had faced two Peak masters so far.

[P83]
The Head Elder and Jopil.

[P84]
*The Head Elder doesn’t count.*

[P85]
In his case, I had to admit that heaven itself had helped me. If not for the sacrifices of the Jin Family of Taiyuan’s martial artists and Lee Cheonbaek’s surprise attack, he was a master I could never have defeated, even if I had died and come back to life.

[P86]
*Then what if I compare Jopil and Jin Mukyung?*

[P87]
I did not have to think for long.

[P88]
I had experienced fighting both of them, so the choice was easy.

[P89]
*Jin Mukyung is stronger.*

[P90]
Jopil was unquestionably a monster. Even now, I got goose bumps whenever I remembered the savage heat pouring from his Flame Divine Palm.

[P91]
But how should I put it? He was strong like a Peak master, and he used the deadly Flame Divine Palm, but that was all.

[P92]
*More precisely, it was a difference in how they used their martial arts.*

[P93]
Jin Mukyung was different from Jopil. Even during our spar, he had used at least ten different martial arts to completely shut down my attacks.

[P94]
To a martial artist, martial arts were another weapon. Jin Mukyung knew how to draw out the right weapon at exactly the right moment.

[P95]
*Compared to him, what did I have?*

[P96]
I could exclude the Jin Family’s Cultivation Technique, which I had possessed from the beginning. As for martial arts I had learned in Murim, I had only the Jin Family’s Spear Technique and the Jin Family’s Manoeuvre Technique.

[P97]
Of course, both were unquestionably First Rate martial arts.

[P98]
But put another way, they were only useful up to the First Rate level.

[P99]
The limits of martial arts. Jin Wikyung could not possibly have failed to notice what I had felt.

[P100]
*That was why he had sent me to Jin Mukyung. Ugh.*

[P101]
My brow furrowed automatically from the pain. I had only raised my upper body a little, but every joint in my body throbbed, and my skin ached.

[P102]
It seemed even Sleep Mode had its limits when it came to rest.

[P103]
*Well, I did get beaten half to death.*

[P104]
To complete the Quest by earning Jin Mukyung’s recognition, I would have to endure days like today—or even worse ones.

[P105]
Maybe I would simply get beaten senseless and fail the Quest anyway.

[P106]
*It really is one mountain after another.*

[P107]
And that made me happy.

[P108]
As an F-rank Hunter, I had not even been given the right to climb a mountain. But everything had changed.

[P109]
There was a mountain I had to climb, and I had been given the right to climb it.

[P110]
And I could do it faster than anyone else!

[P111]
*This isn’t the time for this.*

[P112]
I rose from my place, forgetting the pain. Every minute and second I wasted felt unbearable.

[P113]
* * *

[P114]
Jin Mukyung was in the underground training hall.

[P115]
I descended the stairs leading underground, keeping my footsteps as quiet as possible, and saw him.

[P116]
“Hah!”

[P117]
With a short shout, his sword moved.

[P118]
Whoosh! Shh-shh-shhk!

[P119]
The wind split along the blade.

[P120]
Jin Mukyung’s movements were as unrestrained as he thrust and slashed through the empty air at the speed of a ray of light.

[P121]
About fifteen minutes passed.

[P122]
Jin Mukyung lowered his sword and let out a long breath.

[P123]
“Hoo.”

[P124]
He wiped the sweat from his brow with his sleeve, then turned his head toward me.

[P125]
It seemed he had noticed my presence some time ago.

[P126]
“Tell me.”

[P127]
The words came out of nowhere.

[P128]
Confused, I reflexively asked:

[P129]
“Tell you what?”

[P130]
“About the martial art I just performed.”

[P131]
“Uh, well, first of all, it was really fast…”

[P132]
“For the record, if you say some pointless bullshit like ‘It was fast’ or ‘It was strong,’ I’ll kill you.”

[P133]
*What a ghost.*

[P134]
I racked my brain for an answer that would keep me alive.

[P135]
What had Jin Mukyung’s martial art been like?

[P136]
As I thought about it carefully, a vague impression began to surface.

[P137]
“Rough?”

[P138]
Jin Mukyung’s eyebrow twitched.

[P139]
*Was that the right answer?*

[P140]
“Did you just speak informally to me?”

[P141]
“…It seemed rough.”

[P142]
“Even a little kid could say that. Be more specific.”

[P143]
The image in my head gradually became clearer.

[P144]
I remembered the sword blades pouring toward an imaginary enemy and the movements that accompanied them. Fast, unrestrained motions. And an aura that seemed to press down from every direction.

[P145]
It was like…

[P146]
“A waterfall?”

[P147]
“…”

[P148]
“Huh?”

[P149]
*What? Was that the right answer?*

[P150]
After remaining silent for a while, Jin Mukyung suddenly swung his scabbard.

[P151]
Smack!

[P152]
“Ow! Why did you hit me?”

[P153]
“Just because.”

[P154]
He stared at me with a strange look in his eyes.

[P155]
“How did someone like you ever come out?”

[P156]
Was that an insult or a compliment?

[P157]
I had no idea what he truly meant, but I had to hear the answer to his question if only to soothe my wounded pride. Rubbing my throbbing forehead, I asked:

[P158]
“So, was that the correct answer?”

[P159]
“There are thousands of martial arts manuals in Heaven’s Gate Temple. They were arrangements left behind by the departed Seniors who hoped to cultivate the younger generation of the orthodox Murim.”

[P160]
“And?”

[P161]
“The Falling Flow Sword you just saw is one of them. I found it buried deep in the archives.”

[P162]
Falling flow. In other words, water falling down.

[P163]
A waterfall.

[P164]
I had only said the first thing that came to mind, but it had actually been the right answer.

[P165]
“Oh, ooh.”

[P166]
*Am I really a genius?*

[P167]
If I could recognize martial arts like this after only two months of learning them, I was afraid of how strong I might become in the future. Even I found myself frightening.

[P168]
“Surely you’re not having the embarrassing thought that you’re a genius or something after managing only that much?”

[P169]
“…”

[P170]
*He really is a ghost.*

[P171]
Still, I seemed to have at least a little talent.

[P172]
Unable to let go of the thought, I cautiously asked:

[P173]
“Can everyone normally do this much?”

[P174]
Jin Mukyung flinched.

[P175]
“O-Of course. Anyone with eyes should be able to guess this much.”

[P176]
“Come on.”

[P177]
“‘Come on’? Do you want me to pluck out one of your eyes?”

[P178]
“…That might be a bit much.”

[P179]
*Why is this bastard being especially stone-faced today? Did something unpleasant happen?*

[P180]
Even after I backed down, Jin Mukyung could not contain his anger. He snorted irritably.

[P181]
“It’s basic. Basic. Everyone can do it.”

[P182]
“I get it. Why do you keep getting angry? You’re scaring me.”

[P183]
“Are you rebelling against me? Is it because you’re going through the storm-and-stress stage of adolescence? Do you want to get beaten with the Twelve Gale Fists?”

[P184]
I did not know what the Twelve Gale Fists were, but getting hit by them sounded painful.

[P185]
I shook my head fiercely, but Jin Mukyung’s anger showed no sign of fading.

[P186]
“Do you know martial arts? Huh?”

[P187]
“N-No, sir.”

[P188]
“How long have you been learning martial arts?”

[P189]
The answer slipped out reflexively.

[P190]
“Two months. Two months.”

[P191]
“Right, a bastard who’s only been at it for two months… What? Two months?”

[P192]
Jin Mukyung glared at me with bloodshot eyes.

[P193]
“Not three years, but two months?”

[P194]
This was an emergency.

[P195]
The social instincts I had gained through seven years of working life shone at that moment. I hurriedly opened my mouth, making sure to emphasize one particular part.

[P196]
“Three years! Plus two months!”

[P197]
Jin Mukyung’s fist had been trembling as though he had suffered a stroke, but it steadied again. For some reason, even his voice seemed slightly gentler.

[P198]
“You little bastard. You startled me.”

[P199]
*You startled me even more, you son of a bitch.*

[P200]
*Does he have anger-management issues?*

[P201]
If Jin Mukyung asked Jin Wikyung, my lie would be exposed immediately. But at least I would not have the misfortune of experiencing the Twelve Gale Fists right now.

[P202]
In any case, Jin Mukyung’s anger subsided in the meantime.

[P203]
“I’ll say this only once. Listen carefully.”

[P204]
“I’ll engrave it on my heart.”

[P205]
I bowed deeply, and he declared in a domineering tone:

[P206]
“I teach, and you obey.”

[P207]
“…”

[P208]
*Is this a dog-training school or what?*

[P209]
“There will be no objections. Why? Because I’m stronger than you.”

[P210]
It was true, so I had no desire to argue.

[P211]
Money, power, and force. Their forms might differ, but the world always revolved around the strong.

[P212]
I wanted to stand at its center.

[P213]
“What will you do?”

[P214]
My answer had been decided a long time ago.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 이천백    | **Lee Cheonbaek**  |
| 조필     | **Jopil**          |
| 월화     | **Wolhwa**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 천무학관   | **Heaven's Gate Temple**         |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 영약     | **elixir**                                       |                                                       |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 낭인     | **wandering martial artist**                     |                                                       |
| 정파     | **orthodox faction**                             |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 선배     | **Senior**                                   |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 진가보법   | **Jin Family's Manoeuvre Technique**   |
| 진가창법   | **Jin Family's Spear Technique**       |
| 퀘스트              | **Quest**                      |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 태원     | **Taiyuan**            |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 70,
  "passed": true,
  "metrics": {
    "source_characters": 5516,
    "translation_characters": 12690,
    "length_ratio": 2.301,
    "source_paragraphs": 188,
    "translation_paragraphs": 209
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "천무학관",
        "preferred": "Heaven's Gate Temple"
      }
    },
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
        "korean": "정파",
        "preferred": "orthodox faction"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진가심법",
        "preferred": "Jin Family's Cultivation Technique"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진가보법",
        "preferred": "Jin Family's Manoeuvre Technique"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진가창법",
        "preferred": "Jin Family's Spear Technique"
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
        "korean": "갑자",
        "preferred": "jiazi"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "검신",
        "preferred": "Sword God"
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
