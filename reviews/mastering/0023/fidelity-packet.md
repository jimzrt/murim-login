# Fidelity Gate — Chapter 23

Audit the complete assembled English chapter against the Korean source.
Report only genuine source-fidelity defects: wrong action, subject, object,
causality, quantity, mechanism, terminology, ambiguity, joke logic, register,
or physical detail. Check repeated UI labels and counters against how they
behave across the whole scene. Interpret idioms by their function, not by
translating their component words. Do not report optional stylistic rewrites.

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
  1|＃23화
  2|
  3|
  4|
  5|태원진가.
  6|
  7|이름에서 알 수 있듯이 그 본거지는 태원이다. 그러나 현실에서의 대기업이 그렇듯, 태원진가의 영향력은 태원 한 곳에 국한되지 않았다.
  8|
  9|가문이 세워진 지 200년. 산서성 곳곳에 산재한 현읍에 지부를 설치해 세력권을 넓힌 지 오래였다.
 10|
 11|
 12|
 13|닷새 안에 정양 인근을 정찰하고 복귀할 것.
 14|
 15|
 16|
 17|정찰조에게 내려진 첫 임무다. 명령 내용을 들은 조원들의 첫 반응은 두 가지로 나뉘었다.
 18|
 19|“별거 아니군요.”
 20|
 21|혁무진처럼 실망하는 자들이 있는가 하면, 한엽처럼 안도의 한숨을 내쉬는 자도 있었다.
 22|
 23|물론 둘 다 내 마음에 드는 반응은 아니었다.
 24|
 25|혁무진 쪽은 쓸데없는 공명심에 사로잡혀 있고, 한엽 쪽은 싸우는 것을 겁내고 있으니까.
 26|
 27|‘그래, 차라리 안전한 임무가 낫지.’
 28|
 29|이런 놈들 데리고 적들이랑 맞닥뜨려 봐라. 상상만 해도 끔찍하다. 차라리 믿을 만한 놈들이랑 일선에서 싸우는 게 덜 위험할 것이다.
 30|
 31|‘보직 이동이라도 신청해야 되나.’
 32|
 33|내심 한숨을 쉬며 주먹을 치켜올렸다. 앞서 숙지시킨 수신호 중 하나다. 뜻은 정지.
 34|
 35|푸르륵.
 36|
 37|적당한 속도로 달리고 있던 열한 마리의 말이 투레질 소리와 함께 멈췄다. 내 오른편에서 달리고 있던 혁무진이 퉁명스럽게 말했다.
 38|
 39|“왜 멈추는 거요?”
 40|
 41|“휴식.”
 42|
 43|“또?”
 44|
 45|“한 시진 이동. 일각 휴식. 내가 미리 말하지 않았나?”
 46|
 47|“더 달릴 수 있소!”
 48|
 49|“그럼 너 혼자 달리든가.”
 50|
 51|나는 슬쩍 뒤를 턱짓했다. 다른 조원들이 거친 숨을 몰아쉬고 있었다. 말을 타고 이동하는 것은 속도가 빠른 대신, 상당한 스태미나를 소모한다.
 52|
 53|레벨이 월등히 높은 혁무진은 그럭저럭 버틴다지만, 다른 조원들은 피로가 누적되고 있었다.
 54|
 55|“쉬라면 쉬어. 명령이다.”
 56|
 57|혁무진의 구겨진 얼굴을 무시하고 조원들을 향해 말했다.
 58|
 59|“일각 동안 휴식.”
 60|
 61|일각. 15분의 휴식 시간이 주어졌지만 정찰조원들의 표정은 썩 밝지 않았다. 내가 곧장 커다란 가죽 배낭을 꺼냈기 때문이다.
 62|
 63|배낭에 손을 집어넣고 생각했다.
 64|
 65|‘인벤토리 오픈.’
 66|
 67|철그럭 소리와 함께 방패 세 개가 배낭 안으로 소환됐다.
 68|
 69|표면에 철을 입힌 나무 방패는 태원진가를 떠나오기 전 무기고에서 얻어 온 것이었는데, 가볍고 단단해서 쓸 만했다.
 70|
 71|“칠 호. 팔 호. 구 호.”
 72|
 73|지명된 정찰조원 셋이 죽을상을 쓰며 방패를 받아 갔다.
 74|
 75|그 셋이 내게 강제로 선택된, 탱커(Tanker)다.
 76|
 77|‘딜러 일곱. 탱커 셋. 그리고 나.’
 78|
 79|게이트에 들어갔다가는 몰살을 당할 조합이었지만 우선은 이 정도로 만족해야 한다.
 80|
 81|“각자 위치로.”
 82|
 83|다음은 포메이션이다.
 84|
 85|“기본 대형.”
 86|
 87|방패를 든 셋이 가장 앞에 서고, 일 호 혁무진부터 육 호까지 여섯 명의 검사가 제2열. 최후방에는 나와 한엽이 있다.
 88|
 89|전방 위주의 경계다.
 90|
 91|“펼쳐. 헤쳐 모여. 산개.”
 92|
 93|불만이 가득한 얼굴들이었지만 이제는 제법 능숙하게 해낸다. 이정도면 이제 막 헌터 훈련소를 졸업한 F급 헌터보다 훨씬 낫다.
 94|
 95|‘사람보다 여기 NPC가 낫네.’
 96|
 97|공력의 유무에서 나오는 차이일 것이다.
 98|
 99|마나 자체를 다루지 못하는 F급 헌터와 달리 무림의 NPC들은 미미하나마 공력을 사용할 줄 아니까.
100|
101|단지 레벨이 낮고, 경험이 없을 뿐이지.
102|
103|나는 포메이션의 마지막 단계로 접어들었다.
104|
105|“전력 후퇴.”
106|
107|순간 정찰조원들이 멈칫했다.
108|
109|“예?”
110|
111|“전력 후퇴는 뭡니까?”
112|
113|“말 그대로지. 전력을 다해서 후퇴하라고.”
114|
115|“그럼 어떤 대형을……?”
116|
117|“그때쯤이면 대형이 무의미하지. 그냥 전력을 다해서 튀어라. 뒤도 돌아보지 말고 최대한 흩어져서.”
118|
119|“큭큭. 그걸 말이라고 하는 거요?”
120|
121|비웃음의 주인은, 당연하게도 혁무진이었다.
122|
123|“이제 도저히 못 참겠군. 삼공자, 전쟁이 소꿉장난이오? 헛소리를 그럴듯하게 하려면 최소한 병법서 한 권 정도는 읽고 왔어야지.”
124|
125|“병법서?”
126|
127|“그래. 병법서! 질서정연하게 후퇴하는 것은 병법의 기본중의 기본인데 무슨 망발을 지껄이는 거요?”
128|
129|혁무진이 대놓고 반발하자 정찰조원들 사이에서도 소극적인 목소리들이 새어 나왔다.
130|
131|“맞는 말이긴 해.”
132|
133|“우리가 관아의 군병도 아닌데 대형을 연습시키고, 억지로 방패까지 들게 하고…….”
134|
135|“전력 후퇴? 그런 건 들어 본 적도 없어.”
136|
137|봐라, 다들 나랑 같은 생각이다. 혁무진의 득의양양한 얼굴이 말하는 듯했다.
138|
139|그때 한엽이 더듬거리는 목소리로 끼어들었다.
140|
141|“저, 저는 그렇게 생각 안 하는데요.”
142|
143|“뭐?”
144|
145|“삼공자, 아니 조장님께서 다 생각이 있으셔서 그런 게 아닐까……요?”
146|
147|“생각?”
148|
149|혁무진이 눈을 부라렸다.
150|
151|“생각은 무슨 생각! 어릴 때부터 수련은 뒷전이고 계집 끼고 술만 퍼마시던 게 삼공자다. 그런 주제에 사고란 사고는 다 치고 다녔지. 그뿐인가, 이 전쟁의 원인을 제공한 것도…….”
152|
153|“그만하지?”
154|
155|말을 가로막자 혁무진이 움찔한다. 스스로도 말실수를 했다는 걸 깨달은 모양이었다.
156|
157|하지만 종종 그런 사람들이 있다. 물러서야 할 때, 오히려 한발 나아가는 그런 사람들이.
158|
159|“원인을 제공한 것도 삼공자 아닌가!”
160|
161|혁무진은 자신의 말을 멈추기에는 자존심이 너무나 강한 놈이었다.
162|
163|결국 뱉어 낸 그 말에, 싸늘한 침묵이 내려앉았다.
164|
165|꿀꺽. 누군가의 목울대가 크게 일렁였다. 아홉 쌍의 눈빛이 나와 혁무진을 바라보고 있었다.
166|
167|“하, 할 말이라도 있소?”
168|
169|할 말? 당연히 있지.
170|
171|“전원 일 다경 더 휴식.”
172|
173|동시에 곧게 편 손바닥으로 혁무진의 뺨을 후려쳤다.
174|
175|쫙!
176|
177|“한 대.”
178|
179|혁무진의 턱이 돌아간다. 공력이 전혀 실리지 않은 단순한 따귀다. 갑작스러운 상황에 멍해진 그 얼굴로 두 번째 손바닥을 날렸다.
180|
181|“이, 이게 무슨!”
182|
183|그래도 영 맹탕은 아닌지, 팔을 들어 막는다. 녀석이 간과한 부분이 있다면 그건 바로 힘의 차이다.
184|
185|쫙!
186|
187|“두 대.”
188|
189|상체 그대로 땅에 처박힌 혁무진이 벌떡 일어났다. 한쪽 뺨에는 내 손바닥 자국이 문신처럼 박혀 있었다.
190|
191|당황이 분노로 바뀌기까지는 그리 오랜 시간이 걸리지 않았다.
192|
193|“이 개새끼가!”
194|
195|제대로 열받았군. 눈이 뒤집혀서 달려드는 녀석의 다리를 걸어 넘어트렸다. 동시에 왼손에 힘을 실어 후려쳤다.
196|
197|쫙.
198|
199|“세 대.”
200|
201|“커헉.”
202|
203|다리에 힘이 풀리는지 비틀거린다. 이 정도 힘으로 연달아 세 번을 맞았으니 골이 흔들릴 법도 하다.
204|
205|“공력은 뒀다가 국 끓여 먹을래?”
206|
207|이 말은 효과가 있었다. 휘청거리던 하체에 힘이 들어가고 몸에서는 힘이 흘러넘친다. 독기가 줄줄 새는 눈빛이 나를 노려봤다.
208|
209|“후회하게 될 거야.”
210|
211|“아닐걸.”
212|
213|얼굴을 향해 날아오는 주먹을 붙잡았다. 속도, 힘, 타이밍.
214|
215|전부 눈에 보인다. 이소군에 비하면 한참이나 떨어진다.
216|
217|“네 대.”
218|
219|혁무진의 얼굴이 뒤로 젖혀진다. 찐득한 핏물이 슬로우 모션처럼 허공에 흩뿌려졌다. 풀린 동공, 축 늘어진 다리.
220|
221|하지만 용케도 쓰러지지 않았다.
222|
223|그건 내가 녀석의 주먹을 놔줘야만 가능한 일이니까.
224|
225|“다섯 대.”
226|
227|쫙!
228|
229|거기까지가 한계였다. 혁무진은 더 이상 버티지 못하고 혼절했다. 기이한 자세로 널브러진 혁무진의 몸뚱어리 위로 무언가가 투둑 떨어진다.
230|
231|‘눈?’
232|
233|고개를 들어 하늘을 바라봤다. 겨울 하늘이 희고 작은 쓰레기들을 쏟아 내는 중이었다.
234|
235|“휴식 끝. 출발한다.”
236|
237|한마디를 툭 던지고 돌아서는 내 등 뒤로, 정찰조원들이 참았던 숨을 토해 냈다.
238|
239|
240|
241|* * *
242|
243|
244|
245|두 시간 만에 깨어난 혁무진이 가장 먼저 한 일은 내게 달려드는 것이었다.
246|
247|“이런 씨발!”
248|
249|쫙. 털썩.
250|
251|“치워.”
252|
253|“예, 옛!”
254|
255|찰진 따귀 소리와 함께 또 다시 기절한 녀석은, 다른 정찰조원들의 손에 의해 오두막 한 구석에 처박혔다.
256|
257|‘오두막이라. 운 좋네.’
258|
259|인근 지리에 빠삭한 조원의 말에 따르면 적어도 오늘 해가 떨어지기 전까지는 정양에 도착했어야 했다.
260|
261|하지만 갑자기 쏟아지는 폭설에는 어쩔 도리가 없었고, 겨우 찾아낸 곳이 바로 이 오두막이었다.
262|
263|아는 사람만 아는 사냥꾼 쉼터라던가?
264|
265|‘턱 없이 작긴 한데, 이 정도면 땡큐지.’
266|
267|임무가 늦어질 수도 있겠지만, 눈밭에서 밤새 걷다가 기진맥진한 상태에서 적과 마주치는 것보다는 백배 낫다.
268|
269|그런 생각을 할 때였다.
270|
271|“저, 조장님.”
272|
273|한엽이다. 등 뒤로 조원들이 힐끔거리며 내 눈치를 살폈다.
274|
275|“이제 어떡할까요?”
276|
277|“응? 자야지.”
278|
279|“저, 그게 아니라…….”
280|
281|우물쭈물하는 정찰조원들을 보자 문득 떠오르는 게 있었다.
282|
283|너희 설마…….
284|
285|“수련하고 싶냐?”
286|
287|끄덕끄덕. 맹렬하게 상하를 오가는 고갯짓과 열의에 가득 찬 저 눈빛을 봐라.
288|
289|‘백문이 불여일퍽이라더니.’
290|
291|백번 말하는 것보다 한 번 패는 게 낫구나.
292|
293|
294|
295|* * *
296|
297|
298|
299|정오 무렵이었다. 검날이 햇빛을 받아 번쩍였고, 그것이 무사가 볼 수 있었던 유일한 것이었다.
300|
301|“커헉.”
302|
303|털썩. 무릎이 꺾이고 얼어붙은 땅바닥에 얼굴이 처박힌다.
304|
305|어깨부터 가슴까지, 쩍 벌어진 상처 사이로 피가 쏟아졌다. 회생 불능의 상처. 무사는 죽음을 직감했다.
306|
307|“다른 이들은…… 제발 살려.”
308|
309|힘을 다한 목소리가 뚝 끊겼다. 부릅뜬 무사의 눈동자를 보며 한 중년인이 혀를 찼다.
310|
311|“어이구, 이 미련한 친구야.”
312|
313|그렇게 다짜고짜 덤비면 어떡하나. 이어지는 말은 망자에게 닿지 못했다. 주위를 둘러싸고 있던 오십여 명의 낭인들이 낄낄거렸다.
314|
315|“하필 대형한테 걸리다니, 운도 더럽게 없는 놈일세그려.”
316|
317|“누가 정파 새끼 아니랄까 봐 마지막까지 협객 놀음은. 어쩔까요, 대형?”
318|
319|번들거리는 시선들이 남아 있는 생존자들을 향했다. 여자와 아이들로 이루어진 예닐곱 명의 무리였다.
320|
321|“대협. 아이들은 살려 주십시오.”
322|
323|가장 연장자로 보이는 여인의 말에 중년인, 일문일살(一問一殺) 조필은 부드럽게 웃었다.
324|
325|“미안하지만 어쩌지. 나는 대협이 아니라오.”
326|
327|“하지만 사람이지요. 어찌 사리분별도 하지 못하는 아이들까지 죽이려 하십니까?”
328|
329|“허, 아녀자의 몸으로 기개가 제법이오. 가만, 삭주 지부장의 일가가 살아남았다고 하던데. 혹시?”
330|
331|“제 부군 되십니다.”
332|
333|“아, 역시 그렇구려. 그런 못난 놈에게 이런 현숙한 부인이 있을 줄이야.”
334|
335|조필은 빙긋 웃었고, 여인은 얼굴을 굳혔다.
336|
337|“살려 줄 생각이 없군.”
338|
339|“안심하시오. 나는 간살하는 취미는 없거든.”
340|
341|“아이들은…….”
342|
343|“이 험난한 세상. 어린것들이 어미 없이 어찌 살아남겠소?”
344|
345|“금수만도 못한 놈.”
346|
347|“유언, 잘 들었소.”
348|
349|그 말이 신호탄이었다.
350|
351|검광이 번뜩이고 비명이 울려 퍼졌다.
352|
353|잠시 후 피를 흠뻑 뒤집어쓴 낭인들이 시체들을 산속 수풀로 던져 넣었다.
354|
355|“산짐승 놈들만 포식하겠군요.”
356|
357|뱁새눈이 중얼거렸다. 그는 조필의 오른팔 격인 인물로, 흑산도(黑山刀)라는 별호로 알려진 일급 낭인이었다.
358|
359|“우리도 포식해야지. 이번 일만 잘 마무리 짓는다면 천금이 별건가?”
360|
361|조필은 기분 좋게 웃었다. 이번 일로 받게 될 사례도 어마어마했지만, 그는 지금 이 상황 자체를 즐기고 있었다.
362|
363|“태원진가 놈들을 사냥하는 날이 오다니. 상상도 못 했지.”
364|
365|더러워진 가죽신이 고꾸라진 무사의 시신을 밟았다.
366|
367|무사는 태원진가에 속한 십여 개 지부 중 하나인 삭주(朔州) 지부 소속이었다.
368|
369|“방금 처리한 게 마지막인가?”
370|
371|“아닙니다, 대형.”
372|
373|“쥐새끼처럼 잘도 빠져나가는군. 머릿수는?”
374|
375|“도합 셋. 무사 하나에 아이 둘입니다. 불과 몇 시진 전에 정양을 통과, 혼주로 향하고 있다고 합니다.”
376|
377|“골치 아프군. 반나절은 걸릴 텐데.”
378|
379|“대형께서 나서실 필요도 없이 제가 다녀오겠습니다.”
380|
381|“그래 주겠나?”
382|
383|조필의 입가에 흐뭇한 미소가 떠올랐다.
384|
385|“좋아, 절반을 데려가게. 기한은 반나절, 어떤가?”
386|
387|대답은 이미 정해져 있었다. 흑산도는 깊이 고개를 숙였다.
```

## Assembled English

```markdown
[P1]
# Chapter 23

[P2]
The Jin Family of Taiyuan.

[P3]
As its name suggested, the family was based in Taiyuan. But like a conglomerate in the real world, its influence wasn’t limited to a single city.

[P4]
The family had been established two hundred years ago and had long since expanded its sphere of influence by setting up branches in county towns throughout Shanxi.

[P5]
*Scout the area near Jeongyang and return within five days.*

[P6]
That was the reconnaissance squad’s first mission. When the squad members heard their orders, their reactions fell into two camps.

[P7]
“Doesn’t sound like much.”

[P8]
Some, like Hyuk Mujin, were disappointed. Others, like Han Yeop, sighed with relief.

[P9]
Of course, neither reaction pleased me.

[P10]
Hyuk Mujin was caught up in a pointless hunger for glory, while Han Yeop was afraid of fighting.

[P11]
*Still, a safe mission is better.*

[P12]
Try running into the enemy with a bunch of guys like these. It was horrifying just to imagine. I’d be safer fighting on the front lines with people I could trust.

[P13]
*Should I apply for a transfer?*

[P14]
Suppressing a sigh, I raised my fist. It was one of the hand signals I had taught them earlier. It meant stop.

[P15]
Snort.

[P16]
The eleven horses, which had been moving at a moderate pace, halted with a chorus of snorts. Hyuk Mujin, riding to my right, spoke irritably.

[P17]
“Why are we stopping?”

[P18]
“Rest.”

[P19]
“Again?”

[P20]
“Two hours of travel, fifteen minutes of rest. Didn’t I tell you that beforehand?”

[P21]
“I can keep going!”

[P22]
“Then go by yourself.”

[P23]
I jerked my chin toward the rear. The other squad members were breathing heavily. Riding a horse was faster than traveling on foot, but it consumed a considerable amount of stamina.

[P24]
Hyuk Mujin’s much higher Level let him hold up fairly well, but fatigue was building in the others.

[P25]
“When I tell you to rest, rest. That’s an order.”

[P26]
Ignoring Hyuk Mujin’s scowl, I addressed the squad.

[P27]
“Fifteen minutes of rest.”

[P28]
They had fifteen minutes to rest, but the reconnaissance squad members didn’t look particularly happy. That was because I immediately pulled out a large leather backpack.

[P29]
I reached inside and thought,

[P30]
*Open Inventory.*

[P31]
With a clatter, three shields were summoned into the backpack.

[P32]
They were wooden shields plated with iron, taken from the armory before we left the Jin Family of Taiyuan. Light, sturdy, and perfectly usable.

[P33]
“Number Seven. Number Eight. Number Nine.”

[P34]
The three designated reconnaissance squad members accepted the shields with faces that looked ready to die.

[P35]
They were the tanks I had forcibly appointed.

[P36]
*Seven damage dealers. Three tanks. And me.*

[P37]
It was the kind of party that would be wiped out the moment it entered a Gate, but for now, this would have to do.

[P38]
“Everyone to your positions.”

[P39]
Next came formation.

[P40]
“Basic formation.”

[P41]
The three shield bearers took the front. Six swordsmen, from Number One Hyuk Mujin through Number Six, formed the second row. Han Yeop and I brought up the rear.

[P42]
A formation focused on watching the front.

[P43]
“Spread out. Scatter and assemble. Disperse.”

[P44]
Their faces were still full of complaints, but they carried out the commands with a fair amount of skill now. At this point, they were much better than F-rank Hunters fresh out of a Hunter training center.

[P45]
*The NPCs here are better than real people.*

[P46]
The difference probably came down to whether they could use internal energy.

[P47]
Unlike F-rank Hunters, who couldn’t manipulate mana at all, Murim’s NPCs could use internal energy, however faintly.

[P48]
They were merely low-Level and inexperienced.

[P49]
I moved on to the final stage of formation training.

[P50]
“All-out retreat.”

[P51]
The reconnaissance squad members hesitated.

[P52]
“What?”

[P53]
“What does ‘all-out retreat’ mean?”

[P54]
“Exactly what it sounds like. Retreat with everything you’ve got.”

[P55]
“Then what formation should we—?”

[P56]
“By that point, formation won’t matter. Just run as fast as you can. Don’t look back, and scatter as widely as possible.”

[P57]
“Heh. You call that an order?”

[P58]
The mocking voice belonged, naturally, to Hyuk Mujin.

[P59]
“I can’t stand this any longer. Third Young Master, is war some children’s game? If you want to make nonsense sound convincing, you should at least have read one military strategy manual before coming here.”

[P60]
“A military strategy manual?”

[P61]
“Yes, a military strategy manual! Retreating in good order is one of the most basic principles of warfare. What kind of nonsense are you spouting?”

[P62]
Hyuk Mujin’s open defiance drew hesitant murmurs from the other reconnaissance squad members.

[P63]
“He’s not wrong.”

[P64]
“We aren’t government soldiers. Why are we drilling formations and being forced to carry shields…?”

[P65]
“I’ve never even heard of an all-out retreat.”

[P66]
See? Everyone thinks the same way I do. Hyuk Mujin’s smug face seemed to say exactly that.

[P67]
Then Han Yeop cut in, his voice wavering.

[P68]
“I-I don’t think that way.”

[P69]
“What?”

[P70]
“The Third Young Master—I mean, the Squad Leader—must have a reason for doing this… right?”

[P71]
“A reason?”

[P72]
Hyuk Mujin glared at him.

[P73]
“What reason could there be? The Third Young Master spent his youth neglecting his training and doing nothing but guzzling booze with women. He caused every kind of trouble despite being like that. And that’s not all. He was also the one who caused this war—”

[P74]
“Enough.”

[P75]
Hyuk Mujin flinched when I cut him off. He seemed to realize he had made a mistake.

[P76]
But some people were like that. When they needed to back down, they took another step forward instead.

[P77]
“Wasn’t the Third Young Master the one who caused this war?”

[P78]
Hyuk Mujin’s pride was too great to let him stop there.

[P79]
The words finally left his mouth, and a chilly silence descended.

[P80]
Gulp.

[P81]
Someone’s throat bobbed loudly. Nine pairs of eyes turned toward Hyuk Mujin and me.

[P82]
“D-do you have something to say?”

[P83]
Something to say? Of course I did.

[P84]
“Everyone gets another fifteen minutes of rest.”

[P85]
At the same time, I slapped Hyuk Mujin across the cheek with my flat palm.

[P86]
Smack!

[P87]
“One.”

[P88]
His jaw twisted to the side. It was an ordinary slap, without even a trace of internal energy. His face was still dazed by the sudden turn of events when I struck him a second time.

[P89]
“What the—!”

[P90]
He wasn’t completely helpless, at least. He raised an arm to block.

[P91]
What he had failed to account for was the difference in our strength.

[P92]
Smack!

[P93]
“Two.”

[P94]
Hyuk Mujin’s upper body slammed into the ground. He sprang back up, my palm print stamped across one cheek like a tattoo.

[P95]
It didn’t take long for his bewilderment to turn into rage.

[P96]
“You fucking bastard!”

[P97]
Now he was properly pissed. He charged at me, eyes bulging, and I hooked his leg out from under him. At the same time, I put some strength into my left hand and struck him again.

[P98]
Smack.

[P99]
“Three.”

[P100]
“Urgh.”

[P101]
His legs seemed to give out, and he staggered. Three consecutive blows with that much force were bound to leave his skull rattling.

[P102]
“What, are you saving your internal energy to boil soup later?”

[P103]
That got through to him. Strength filled his wavering legs, and power surged through his body. His glare dripped venom.

[P104]
“You’ll regret this.”

[P105]
“I doubt it.”

[P106]
I caught the fist flying toward my face.

[P107]
Speed, strength, timing.

[P108]
I could see it all. Compared to Lee Seogeun, he was far behind.

[P109]
“Four.”

[P110]
Hyuk Mujin’s head snapped back. Sticky blood sprayed through the air in slow motion. His pupils were unfocused, and his legs hung limp.

[P111]
Yet somehow, he didn’t fall.

[P112]
He couldn’t—not unless I let go of his fist.

[P113]
“Five.”

[P114]
Smack!

[P115]
That was his limit. Hyuk Mujin could no longer endure and passed out. Something fell with a soft thud onto his body, sprawled out in a bizarre position.

[P116]
*Snow?*

[P117]
I raised my head toward the sky. The winter sky was raining down small white scraps of garbage.

[P118]
“Rest is over. We’re leaving.”

[P119]
I tossed out the words and turned away. Behind me, the reconnaissance squad members finally released the breaths they had been holding.

[P120]
* * *

[P121]
When Hyuk Mujin woke two hours later, the first thing he did was charge at me.

[P122]
“You fucking—!”

[P123]
Smack. Thud.

[P124]
“Move him.”

[P125]
“Y-yes, sir!”

[P126]
Another satisfying slap knocked him out cold. The other reconnaissance squad members dragged him into a corner of the cabin.

[P127]
*A cabin. We got lucky.*

[P128]
According to one squad member who knew the surrounding area well, we should have reached Jeongyang before sunset at the latest.

[P129]
But there was nothing we could do about the sudden heavy snowfall, and this cabin was the only place we had managed to find.

[P130]
Apparently, it was a hunters’ shelter known only to people familiar with the area.

[P131]
*It’s ridiculously small, but I’ll take it.*

[P132]
The mission might be delayed, but this was a hundred times better than walking through the snow all night and then running into the enemy while utterly exhausted.

[P133]
That was when—

[P134]
“Squad Leader?”

[P135]
It was Han Yeop. Behind him, the other squad members stole glances at me, trying to gauge my mood.

[P136]
“What should we do now?”

[P137]
“Hm? Sleep.”

[P138]
“N-no, that’s not what I meant…”

[P139]
As I looked at the fidgeting reconnaissance squad members, a thought struck me.

[P140]
*Don’t tell me…*

[P141]
“Do you want to train?”

[P142]
Nod, nod.

[P143]
Look at those heads bobbing furiously. Look at those eyes burning with enthusiasm.

[P144]
*Forget seeing once. One beating beats hearing something a hundred times.*

[P145]
One beating really was better than a hundred explanations.

[P146]
* * *

[P147]
It was around noon.

[P148]
Sunlight flashed along a sword blade. That was the only thing the martial artist managed to see.

[P149]
“Urgh.”

[P150]
Thud.

[P151]
His knees buckled, and his face slammed into the frozen ground.

[P152]
Blood poured from the gaping wound that ran from his shoulder to his chest. There was no recovering from an injury like that. The martial artist knew he was going to die.

[P153]
“The others… Please, spare them.”

[P154]
His exhausted voice cut off abruptly. Looking at the martial artist’s wide-open eyes, a middle-aged man clicked his tongue.

[P155]
“Good grief, you poor fool.”

[P156]
What were you thinking, charging in like that?

[P157]
The rest of his words never reached the dead man. The fifty-odd wandering martial artists surrounding them snickered.

[P158]
“Of all people, he had to run into the boss. What rotten luck.”

[P159]
“Only an orthodox-faction bastard would keep playing the hero right to the bitter end. What should we do, Boss?”

[P160]
Their gleaming eyes turned toward the remaining survivors—a group of six or seven women and children.

[P161]
“Great Hero, please spare the children.”

[P162]
At the plea from the oldest-looking woman, the middle-aged man—One Question, One Kill Jopil—smiled gently.

[P163]
“I’m sorry, but what can I do? I’m no Great Hero.”

[P164]
“But you’re still human. How can you kill children who can’t even tell right from wrong?”

[P165]
“Hah. You have quite a bit of spirit for a woman. Wait. I heard the Sakju Branch Leader’s family survived. Could you be…?”

[P166]
“He is my husband.”

[P167]
“Ah, I thought so. Who would have imagined such a pathetic man could have such a virtuous wife?”

[P168]
Jopil smiled, and the woman’s expression hardened.

[P169]
“You have no intention of sparing us.”

[P170]
“Don’t worry. I’m not in the habit of raping women before I kill them.”

[P171]
“The children…”

[P172]
“This is a harsh world. How could little ones survive without their mother?”

[P173]
“You’re worse than a beast.”

[P174]
“I heard your last words.”

[P175]
That was the signal.

[P176]
Swordlight flashed, and screams rang out.

[P177]
A short while later, the blood-soaked wandering martial artists tossed the corpses into the mountain thickets.

[P178]
“Looks like the wild animals will be the only ones feasting.”

[P179]
The man with tiny, birdlike eyes muttered. He was Jopil’s right-hand man, a first-rate wandering martial artist known as Black Mountain Blade.

[P180]
“We should feast, too. If we finish this job properly, what’s a mere thousand pieces of gold?”

[P181]
Jopil laughed with pleasure. The payment for this job would be enormous, but the situation itself was what he enjoyed.

[P182]
“I never imagined the day would come when we’d hunt the Jin Family of Taiyuan.”

[P183]
He planted a filthy leather shoe on the fallen martial artist’s corpse.

[P184]
The martial artist had belonged to the Sakju Branch, one of the ten or so branches of the Jin Family of Taiyuan.

[P185]
“Was that the last of them?”

[P186]
“No, Boss.”

[P187]
“They’re slipping away like rats. How many?”

[P188]
“Three in total. One martial artist and two children. They passed through Jeongyang only a few hours ago and are heading for Honju.”

[P189]
“That’s troublesome. It’ll take half a day.”

[P190]
“There’s no need for you to go yourself, Boss. I’ll take care of it.”

[P191]
“Would you?”

[P192]
A pleased smile spread across Jopil’s lips.

[P193]
“Good. Take half the men. You have half a day. How does that sound?”

[P194]
The answer was already decided.

[P195]
Black Mountain Blade bowed deeply.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 23

[P2]
Jin Family of Taiyuan.

[P3]
As its name suggests, its headquarters were in Taiyuan. But like a conglomerate in the real world, the Jin Family of Taiyuan’s influence was not limited to a single city.

[P4]
The family had been established for two hundred years. It had long since expanded its sphere of influence by establishing branches in county towns scattered throughout Shanxi.

[P5]
*Scout the area near Jeongyang and return within five days.*

[P6]
That was the first mission assigned to the reconnaissance squad. When they heard the order, the squad members’ reactions fell into two categories.

[P7]
“Doesn’t sound like much.”

[P8]
Some, like Hyuk Mujin, were disappointed. Others, like Han Yeop, let out sighs of relief.

[P9]
Of course, neither reaction pleased me.

[P10]
Hyuk Mujin was caught up in a pointless hunger for glory, while Han Yeop was afraid of fighting.

[P11]
*Still, I’d rather have a safe mission.*

[P12]
Try running into the enemy with a bunch of guys like these. It was horrifying just to imagine. I’d be safer fighting on the front lines with people I could trust.

[P13]
*Should I apply for a transfer?*

[P14]
Suppressing a sigh, I raised my fist. It was one of the hand signals I had taught them earlier. It meant stop.

[P15]
Snort.

[P16]
The eleven horses moving at a moderate pace stopped with a chorus of snorts. Hyuk Mujin, riding to my right, spoke irritably.

[P17]
“Why are we stopping?”

[P18]
“Rest.”

[P19]
“Again?”

[P20]
“Two hours of travel, fifteen minutes of rest. Didn’t I tell you that beforehand?”

[P21]
“I can keep going!”

[P22]
“Then go by yourself.”

[P23]
I jerked my chin toward the rear. The other squad members were breathing heavily. Riding a horse was faster than traveling on foot, but it consumed a considerable amount of stamina.

[P24]
Hyuk Mujin’s much higher Level let him endure fairly well, but fatigue was accumulating in the others.

[P25]
“Rest if I tell you to. That’s an order.”

[P26]
Ignoring Hyuk Mujin’s crumpled face, I addressed the squad.

[P27]
“Fifteen minutes of rest.”

[P28]
They had fifteen minutes to rest, but the reconnaissance squad members didn’t look particularly happy. That was because I immediately pulled out a large leather backpack.

[P29]
I reached into the backpack and thought,

[P30]
*Open Inventory.*

[P31]
With a clatter, three shields were summoned into the backpack.

[P32]
The wooden shields had been coated with iron on the surface. I had taken them from the armory before leaving the Jin Family of Taiyuan. They were light, sturdy, and perfectly usable.

[P33]
“Number Seven. Number Eight. Number Nine.”

[P34]
The three designated reconnaissance squad members accepted the shields with faces that looked ready to die.

[P35]
Those three had been forcibly selected by me as tanks.

[P36]
*Seven damage dealers. Three tanks. And me.*

[P37]
It was a party that would be wiped out the moment it entered a Gate, but for now, I had to be satisfied with this.

[P38]
“Everyone to your positions.”

[P39]
Next came formation.

[P40]
“Basic formation.”

[P41]
The three shield bearers stood at the front. Six swordsmen, from Number One Hyuk Mujin through Number Six, formed the second row. Han Yeop and I took the rear.

[P42]
A formation focused on watching the front.

[P43]
“Spread out. Scatter and assemble. Disperse.”

[P44]
Their faces were still full of complaints, but they now carried out the commands fairly skillfully. At this point, they were much better than F-rank Hunters who had just graduated from a Hunter training center.

[P45]
*These NPCs are better than people.*

[P46]
The difference probably came down to whether they could use internal energy.

[P47]
Unlike F-rank Hunters, who couldn’t manipulate mana at all, Murim’s NPCs could use internal energy, however faintly.

[P48]
They were merely low-Level and inexperienced.

[P49]
I moved on to the final stage of formation training.

[P50]
“All-out retreat.”

[P51]
The reconnaissance squad members froze.

[P52]
“What?”

[P53]
“What does ‘all-out retreat’ mean?”

[P54]
“It means exactly what it says. Retreat with all your strength.”

[P55]
“Then what formation should we—?”

[P56]
“By then, formation will be meaningless. Just run with all your strength. Don’t even look back. Scatter as much as possible.”

[P57]
“Heh. You call that an order?”

[P58]
The owner of the mocking voice was, naturally, Hyuk Mujin.

[P59]
“I can’t stand this any longer. Third Young Master, is war some children’s game? If you want to make nonsense sound convincing, you should at least have read one military strategy manual before coming here.”

[P60]
“A military strategy manual?”

[P61]
“Yes, a military strategy manual! Retreating in good order is one of the most basic principles of warfare. What kind of nonsense are you spouting?”

[P62]
Hyuk Mujin’s open defiance drew hesitant voices from the other reconnaissance squad members.

[P63]
“He’s not wrong.”

[P64]
“We aren’t government soldiers, so why are we practicing formations and being forced to carry shields…?”

[P65]
“I’ve never heard of an all-out retreat.”

[P66]
See? Everyone thinks the same way I do. Hyuk Mujin’s smug face seemed to say exactly that.

[P67]
Then Han Yeop joined in, his voice wavering.

[P68]
“I-I don’t think that way.”

[P69]
“What?”

[P70]
“The Third Young Master—I mean Squad Leader—must have a reason for doing this… right?”

[P71]
“A reason?”

[P72]
Hyuk Mujin glared at him.

[P73]
“What reason could there be? The Third Young Master spent his youth drinking with women instead of training. He caused every kind of trouble despite being like that. And that’s not all. He was also the one who caused this war—”

[P74]
“Enough.”

[P75]
Hyuk Mujin flinched when I cut him off. He seemed to realize that he had made a mistake.

[P76]
But some people were like that. When they needed to back down, they took another step forward instead.

[P77]
“Wasn’t the Third Young Master the one who caused this war?”

[P78]
Hyuk Mujin’s pride was too great for him to stop himself.

[P79]
The words finally left his mouth, and a chilly silence descended.

[P80]
Gulp.

[P81]
Someone’s throat bobbed loudly. Nine pairs of eyes turned toward Hyuk Mujin and me.

[P82]
“D-do you have something to say?”

[P83]
Something to say? Of course I did.

[P84]
“Everyone gets another fifteen minutes of rest.”

[P85]
At the same time, I slapped Hyuk Mujin across the cheek with my flat palm.

[P86]
Smack!

[P87]
“One.”

[P88]
His jaw twisted to the side. It was an ordinary slap, without even a trace of internal energy. His face was still dazed by the sudden turn of events when I struck him a second time.

[P89]
“What the—!”

[P90]
He wasn’t completely helpless, at least. He raised his arm to block.

[P91]
What he had failed to account for was the difference in strength.

[P92]
Smack!

[P93]
“Two.”

[P94]
Hyuk Mujin’s upper body slammed into the ground. He sprang back up, a palm print stamped onto one cheek like a tattoo.

[P95]
It didn’t take long for his bewilderment to turn into rage.

[P96]
“You fucking bastard!”

[P97]
He was properly furious now. As he charged at me with his eyes bulging, I hooked his leg and tripped him. At the same time, I put force into my left hand and struck him.

[P98]
Smack.

[P99]
“Three.”

[P100]
“Urgh.”

[P101]
His legs seemed to give out, and he staggered. After taking three consecutive blows with this much force, it was only natural that his head would be rattled.

[P102]
“What, were you saving your internal energy to boil soup?”

[P103]
That got through to him. Strength filled his wavering legs, and power surged through his body. His eyes glared at me, venom dripping from them.

[P104]
“You’ll regret this.”

[P105]
“No, I won’t.”

[P106]
I caught the fist flying toward my face.

[P107]
Speed, strength, timing.

[P108]
I could see all of them. Compared to Lee Seogeun, he was far behind.

[P109]
“Four.”

[P110]
Hyuk Mujin’s head snapped back. Sticky blood sprayed through the air in slow motion. His pupils were unfocused, and his legs hung limp.

[P111]
Yet somehow, he didn’t fall. He couldn’t—not unless I let go of his fist.

[P112]
“Five.”

[P113]
Smack!

[P114]
That was his limit. Hyuk Mujin could no longer endure and passed out. Something fell with a soft thud onto his body, sprawled out in a bizarre position.

[P115]
*An eye?*

[P116]
I raised my head toward the sky. The winter sky was raining down small white scraps of garbage.

[P117]
“Rest is over. We’re leaving.”

[P118]
I tossed out the words and turned away. Behind me, the reconnaissance squad members finally exhaled the breath they had been holding.

[P119]
* * *

[P120]
When Hyuk Mujin woke up two hours later, the first thing he did was charge at me.

[P121]
“You fucking—!”

[P122]
Smack. Thud.

[P123]
“Move him.”

[P124]
“Y-yes, sir!”

[P125]
After another ringing slap, he passed out again. The other reconnaissance squad members dragged him into a corner of the cabin.

[P126]
*A cabin. We got lucky.*

[P127]
According to one squad member who knew the surrounding area well, we should have reached Jeongyang before sunset at the latest.

[P128]
But there had been nothing we could do about the sudden blizzard, and this cabin was the only place we had managed to find.

[P129]
Apparently, it was a hunter’s shelter known only to those familiar with the area.

[P130]
*It’s ridiculously small, but I’ll take it.*

[P131]
The mission might be delayed, but this was a hundred times better than walking through the snow all night, collapsing from exhaustion, and then running into the enemy.

[P132]
That was when—

[P133]
“Squad Leader?”

[P134]
It was Han Yeop. The squad members behind him glanced at me, gauging my reaction.

[P135]
“What should we do now?”

[P136]
“Hm? Sleep.”

[P137]
“N-no, that’s not what I meant…”

[P138]
As I looked at the fidgeting reconnaissance squad members, a thought struck me.

[P139]
*Don’t tell me…*

[P140]
“Do you want to train?”

[P141]
Nod, nod.

[P142]
Look at the vigorous nodding and those eyes full of passion.

[P143]
*Seeing is believing, my ass. One beating beats a hundred explanations.*

[P144]
One beating really was better than explaining a hundred times.

[P145]
* * *

[P146]
It was around noon. Sunlight flashed along a sword blade. That was all the martial artist saw.

[P147]
“Urgh.”

[P148]
Thud.

[P149]
His knees buckled, and his face slammed into the frozen ground.

[P150]
Blood poured from the gaping wound that stretched from his shoulder to his chest. It was a fatal injury. The martial artist knew he was going to die.

[P151]
“The others… Please, let them live.”

[P152]
His exhausted voice cut off abruptly. Looking at the martial artist’s wide-open eyes, a middle-aged man clicked his tongue.

[P153]
“Good grief, you poor fool.”

[P154]
What were you thinking, charging in like that?

[P155]
The words that followed never reached the dead man. The fifty-odd wandering martial artists surrounding them snickered.

[P156]
“Of all people, he had to run into the boss. What rotten luck.”

[P157]
“Only an orthodox-faction bastard would keep playing the hero right to the end. What should we do, Boss?”

[P158]
Their gleaming eyes turned toward the survivors. There were six or seven women and children huddled together.

[P159]
“Great Hero, please spare the children.”

[P160]
At the plea from the oldest-looking woman, the middle-aged man—Jopil, One Question, One Kill—smiled gently.

[P161]
“I’m sorry, but what can I do? I’m no Great Hero.”

[P162]
“But you’re still a person. How can you kill children who can’t even tell right from wrong?”

[P163]
“Hah. For a woman, you have quite a bit of spirit. Wait. I heard that the family of the Sakju Branch Leader survived. Could it be…?”

[P164]
“He is my husband.”

[P165]
“Ah, so he is. I never imagined such a virtuous wife would belong to such a pathetic man.”

[P166]
Jopil smiled broadly, and the woman’s expression hardened.

[P167]
“You have no intention of sparing us.”

[P168]
“Rest easy. I don’t have a taste for tormenting people.”

[P169]
“The children…”

[P170]
“This is a harsh world. How are little ones supposed to survive without their mother?”

[P171]
“You’re worse than a beast.”

[P172]
“I heard your last words.”

[P173]
That was the signal.

[P174]
Swordlight flashed, and screams rang out.

[P175]
A short while later, the blood-soaked wandering martial artists tossed the corpses into the thickets in the mountains.

[P176]
“Only the wild animals will feast tonight.”

[P177]
The man with the tiny birdlike eyes muttered. He was Jopil’s right-hand man, a first-rate wandering martial artist known by the nickname Black Mountain Blade.

[P178]
“We should feast, too. If we finish this job properly, what’s a mere thousand pieces of gold?”

[P179]
Jopil laughed with pleasure. The payment for this job would be enormous, but the situation itself was what he enjoyed.

[P180]
“I never imagined the day would come when we’d hunt the Jin Family of Taiyuan.”

[P181]
His dirty leather shoe stepped on the fallen martial artist’s corpse.

[P182]
The martial artist had belonged to the Sakju Branch, one of the ten or so branches of the Jin Family of Taiyuan.

[P183]
“Was that the last one?”

[P184]
“No, Boss.”

[P185]
“They’re slipping away like rats. How many?”

[P186]
“Three in total. One martial artist and two children. They passed through Jeongyang only a few hours ago and are headed for Honju.”

[P187]
“That’s troublesome. It’ll take half a day.”

[P188]
“You don’t need to go yourself. I’ll take care of it.”

[P189]
“Would you?”

[P190]
A pleased smile spread across Jopil’s lips.

[P191]
“Good. Take half of them with you. You have half a day. How does that sound?”

[P192]
Black Mountain Blade already knew the answer and bowed deeply.
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 23,
  "passed": true,
  "metrics": {
    "source_characters": 5705,
    "translation_characters": 12502,
    "length_ratio": 2.191,
    "source_paragraphs": 187,
    "translation_paragraphs": 195
  },
  "errors": [],
  "warnings": [
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
        "korean": "상태",
        "preferred": "Status"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "청해",
        "preferred": "Qinghai"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "대협",
        "preferred": "Great Hero or Sir depending tone"
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
