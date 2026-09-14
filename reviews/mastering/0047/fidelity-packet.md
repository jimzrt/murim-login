# Fidelity Gate — Chapter 47

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
  1|＃47화
  2|
  3|
  4|
  5|헌터 협회.
  6|
  7|삼십여 년 전, 대격변의 종전과 동시에 등장한 이름이다.
  8|
  9|피로 얼룩진 대격변에서 살아남은 1세대 헌터들이 깃발을 세웠고, 헌터 협회는 세월의 흐름에 따라 엄청난 위상을 지닌 단체로 발돋움했다.
 10|
 11|꿀꺽.
 12|
 13|나는 침을 삼키며 우뚝 선 협회 건물을 바라봤다. 이 빽빽한 빌딩 숲에서도 눈에 띄는 크기와 높이. 특별한 것 없는 평일에도 수많은 사람이 그곳을 드나들고 있었다.
 14|
 15|‘이게 몇 년 만이지?’
 16|
 17|모든 각성자는 협회의 감독하에 등급 측정을 실시한다.
 18|
 19|나도 마찬가지였다. 설레는 마음으로 이곳을 찾았던 스무 살의 진태경을 생각하니 피식 웃음이 나오……긴 개뿔.
 20|
 21|‘막상 오니까 엄청 긴장되네.’
 22|
 23|경직된 걸음으로 로비로 들어섰다. 운동장만 한 로비는 인파로 득실거렸다. 곳곳에 설치된 전광판을 따라 걸음을 옮기니 원하는 곳을 찾을 수 있었다.
 24|
 25|
 26|
 27|[측정 대기실]
 28|
 29|
 30|
 31|창구 직원의 안내에 따라 서류를 작성하고 들어갔다. 대기실에는 수십 명의 인원이 측정을 기다리고 있었다.
 32|
 33|쿵. 문 닫히는 소리에 시선들이 화살처럼 날아와 꽂힌다.
 34|
 35|‘숨 막힌다, 숨 막혀.’
 36|
 37|이곳은 공기부터 다르다. 팽팽한 긴장감이 대기실 전체를 짓누르고 있었다.
 38|
 39|‘측정 한 번에 헌터 인생이 결정 나는 거니까.’
 40|
 41|나도 마찬가지였다. 너무 긴장한 탓에 감독관 앞에서 방귀를 뀐 적도 있으니 말 다 했지, 뭐.
 42|
 43|이런저런 생각을 하며 순서를 기다리고 있을 때였다.
 44|
 45|“진태경?”
 46|
 47|등 뒤로 들려오는 익숙한 목소리. 천천히 고개를 돌리자 그곳에 그가 있었다.
 48|
 49|“설마 했는데, 맞네.”
 50|
 51|주먹코에 배불뚝이의 중년인. 잊으려야 잊을 수 없는 얼굴이었다.
 52|
 53|‘……김 팀장?’
 54|
 55|김상식. 내가 수년간 몸담았던 소풍 길드의 창립 멤버이자 팀장인 그는 한 단어로 설명할 수 있다.
 56|
 57|전(前) 직장 상사.
 58|
 59|“이야, 이런 데서 볼 줄은 몰랐네. 반가워.”
 60|
 61|김 팀장이 너털웃음과 함께 손을 불쑥 내민다. 나는 잠깐 망설이다가 그의 손을 맞잡았다.
 62|
 63|“그러게요. 오랜만이네요.”
 64|
 65|“오랜만은 무슨. 며칠이나 됐다고.”
 66|
 67|“그 며칠이, 저는 꽤 길게 느껴지더라고요.”
 68|
 69|무림을 떠올리며 한 말이었지만 김 팀장에게는 다른 의미로 들릴 것이다. 그도 그럴 것이, 불과 며칠 전 내게 해고 통보를 한 장본인이니까.
 70|
 71|“여름이라 그래. 나도 요즘 하루가 길어.”
 72|
 73|“그래요?”
 74|
 75|능구렁이처럼 넘어가는 그를 보자 실소가 흘러나왔다.
 76|
 77|언제 봐도 재미있는 양반이다. 여러 가지 의미로.
 78|
 79|“그런데 여긴 어쩐 일이야?”
 80|
 81|“볼일이 좀 있어서요. 팀장님은요?”
 82|
 83|“스카우트차 왔지. 이번에 괜찮은 놈이 있다는 얘길 들어서.”
 84|
 85|해고 사유는 구조 조정으로 인한 인원 감축인데 스카우트라.
 86|
 87|“그렇군요.”
 88|
 89|내가 할 말은 그것밖에 없었다. 다들 아는 뻔한 스토리. 그것도 완결 난 이야기에 더 이상 미련은 없다.
 90|
 91|“그러는 너는 왜 왔어? 설마 재측정이라도 해 보려고?”
 92|
 93|“네.”
 94|
 95|김 팀장이 웃는 얼굴로 말했다.
 96|
 97|“거, 시도는 좋지만 너무 돈 낭비 아냐? 재측정 비용이 한두 푼도 아니고. F급 헌터 처지에 부담될 텐데.”
 98|
 99|“그래도 해 보는 거죠. 혹시나 하는 마음에.”
100|
101|“젊을 때 모아 놔야지. 안 되는 거 계속 붙잡고 있으면 뭐가 달라지나.”
102|
103|“글쎄요. 이번엔 좀 다를 것 같아서요.”
104|
105|“그게 그렇게 쉬운 일이 아닌…….”
106|
107|“팀장님.”
108|
109|“어, 왜?”
110|
111|나는 부드럽게 웃었다.
112|
113|“적당히 하시죠.”
114|
115|순간 김 팀장의 웃음에 실금이 갔다.
116|
117|“뭐?”
118|
119|“적당히 하시라고요. 이제 길드도 나갔으니 저한테 신경 끄시고.”
120|
121|“무슨 뜻이야?”
122|
123|무슨 뜻이긴.
124|
125|“아시잖아요. 제가 무슨 말을 하는 건지.”
126|
127|“…….”
128|
129|“어쩔 수 없었다. 너라도 살아서 다행이다. 다 잊고 새 시작 하자. 위로하는 척하면서 뒤에서 열심히 쪼아 대셨던데요.”
130|
131|“너…….”
132|
133|“길드장님한테 저 자르자고 처음 얘기 꺼낸 것도 팀장님 아닙니까. 제가 모를 줄 아셨어요?”
134|
135|김 팀장은 한마디로 어중간한 소인배다.
136|
137|인간성도, 능력도 부족한 인간.
138|
139|게이트에서도 제 목숨 챙기기에 급급해 길드 내의 평가는 바닥을 기었다.
140|
141|“저 자르고 그 자리에 누구 넣었습니까? 얼마 받고 꽂아 주기로 했어요?”
142|
143|“야, 진태경이.”
144|
145|김 팀장이 내 어깨를 짓누르며 으르렁거렸다. 저래 봬도 소풍 길드에서 셋밖에 없다는 D급 헌터다. 이 정도 힘이면 F급 헌터 따위는 한 손으로도 갖고 놀 수 있다.
146|
147|하지만…….
148|
149|“손 떼.”
150|
151|나는 눈 하나 깜짝하지 않았다. 동기화된 것은 시스템뿐만이 아니다. 무공과 능력치. 그리고 강철 같은 근골까지 포함이다.
152|
153|“셋 센다. 손 떼.”
154|
155|“이 새끼가 보자 보자 하니까…….”
156|
157|나는 망설이지 않고 입을 열었다.
158|
159|“하나, 둘.”
160|
161|셋. 동시에 김 팀장의 손목을 움켜쥔 그 순간이었다.
162|
163|덜컹.
164|
165|“다음 분들 들어오세요. 21번부터 30번!”
166|
167|서류철을 든 협회 감독관의 등장에 우리는 누가 먼저랄 것도 없이 떨어졌다. 협회에 찍혀 봤자 서로에게 좋을 게 없다.
168|
169|“운 좋은 줄 알아라.”
170|
171|“누구. 내가? 아니면 당신?”
172|
173|벌겋게 달아오른 김 팀장의 얼굴이 퍽 우습다. 기감으로 파악한 그의 레벨창까지도.
174|
175|
176|
177|[Lv.24 김상식]
178|
179|
180|
181|“만나서 기분 더러웠고, 다신 보지 맙시다.”
182|
183|미련 없이 자리를 털고 일어났다. 내가 받은 대기 번호는 30번. 감독관을 향해 걸어가는 발걸음은 더 이상 경직되어 있지 않았다.
184|
185|
186|
187|* * *
188|
189|
190|
191|“21번. 앞으로 나와 주세요.”
192|
193|긴장된 얼굴의 각성자가 측정기 앞에 섰다. A급 마정석을 재료로 만든 등급 측정기는 그의 전신을 스캔, 체내의 마나를 수치로 환산한다.
194|
195|지이잉-
196|
197|수치를 확인한 감독관이 입을 열었다.
198|
199|“체내 마나 분포량, F급.”
200|
201|각성자의 얼굴이 흙빛으로 변했다. 하지만 절망하기에는 이르다. 두 번째 기회가 있으니까.
202|
203|“마나를 움직여 보세요. 최대한 집중해서 측정기로 쏘아 보낸다는 느낌으로.”
204|
205|마나 컨트롤을 보는 거다. 아직 끝나지 않았다는 사실을 깨달은 각성자가 이를 악물고 힘을 끌어 올렸다.
206|
207|젖 먹던 힘까지 빡!
208|
209|뿌우웅.
210|
211|“…….”
212|
213|“…….”
214|
215|감독관이 토할 것 같은 얼굴로 말했다.
216|
217|“제어 능력, F급.”
218|
219|“한 번만! 다시 한번만 해 볼게요!”
220|
221|“안 됩니다. 다음.”
222|
223|순서가 휙휙 넘어간다.
224|
225|죄다 E급, F급에 심지어는 비각성자인 놈까지 나왔다.
226|
227|“이거 사기야, 사기! 저 측정기 중국산이지! 어? 이 새끼들아!”
228|
229|“처리하세요.”
230|
231|감독관의 말에 대기하고 있던 경비 헌터들이 사기꾼을 질질 끌고 나갔다. 아마 저놈은 기적적으로 각성한다고 해도 협회 블랙리스트에 등록될 거다.
232|
233|“다음, 30번.”
234|
235|올 게 왔구나.
236|
237|나는 크게 숨을 들이켜고 앞으로 나섰다. 감독관이 손에 든 서류철을 흘끗 보더니 말했다.
238|
239|“재측정이시네요?”
240|
241|“네.”
242|
243|“진태경 씨, 7년 전 F급 취득하셨고…… 재측정은 따로 비용 청구되는 건 아시죠?”
244|
245|대충 들어 보니 괜히 헛돈 쓰지 말고 기회 줄 때 집에나 가란 소리다. F급 헌터를 보는 흔한 시선들.
246|
247|‘누굴 거지로 아나.’
248|
249|익숙한 것과 기분이 더러운 건 별개다. 내가 노려보자 감독관이 피식 웃었다.
250|
251|“혹시 싶어 말씀드리는 건데 비용은 2백만 원입니다.”
252|
253|“……가격 올랐어요?”
254|
255|“몇 년 됐죠.”
256|
257|시벌, 그걸 몰랐네.
258|
259|지금 내 통장 잔고가 얼마더라…….
260|
261|“그럼 측정 시작하겠습니다.”
262|
263|나는 떨리는 마음으로 눈을 감았다. 그리고 다음 순간.
264|
265|지이잉.
266|
267|측정기에서 흘러나온 마력의 파동이 전신을 훑고 지나갔다.
268|
269|15년의 공력이 그에 감응해 부르르 떨었다.
270|
271|‘몇 급일까?’
272|
273|C급? 아니, D급만 되어도 좋다. 하지만 십여 초를 기다려도 감독관의 입은 열리지 않았다.
274|
275|“어어, 이게 왜 이러지?”
276|
277|“왜요?”
278|
279|당황한 얼굴로 측정기와 나를 번갈아 보던 그가 헛기침했다.
280|
281|“오류가 좀 생긴 것 같은데…… 일단 다음 순서로 넘어가겠습니다.”
282|
283|뭐가 어떻게 돌아가는 건지는 모르겠지만 어쩐지 불길하게 느껴지진 않는다.
284|
285|‘느낌이 좋아.’
286|
287|나는 두근거리는 심장 박동을 느끼며 공력을 끌어 올렸다.
288|
289|스아아.
290|
291|진가심법의 부름에 따라 솟구친 15년의 공력이 측정기를 향해 쏘아졌다.
292|
293|
294|
295|* * *
296|
297|
298|
299|로비 입구.
300|
301|“잘했다.”
302|
303|김상식은 청년의 어깨를 두드렸다. 오늘부로 D급 각성자로 공인받은 전도유망한 젊은이다.
304|
305|그는 곧 소풍 길드에 가입, 김상식의 팀에 배정될 것이다. 곧 다가올 그 날을 떠올린 김상식은 뿌듯하게 웃었다.
306|
307|“부자(父子)가 한 팀을 이루겠구나. 역시 내 아들이야.”
308|
309|“뭘요, 아직 정식 헌터가 된 것도 아닌데. 훈련소도 들어가야 하고.”
310|
311|“걱정하지 마라. 이 아버지가 미리 손써 뒀으니까.”
312|
313|“어, 진짜요? 길드에 자리 없다고 하지 않았나?”
314|
315|“다 방법이 있지.”
316|
317|그 과정에서 눈엣가시 같던 최하급 헌터를 잘랐다는 사실은 말하지 않았다.
318|
319|“어쨌든 이번 주는 푹 쉬고, 다음 주부터 같이 출근…….”
320|
321|문득 김상식의 표정이 일그러졌다.
322|
323|“왜 그래요?”
324|
325|“……아니다. 먼저 차에 가 있어.”
326|
327|아들이 떠난 후 홀로 남은 그는 셔츠 소매를 걷어 올렸다.
328|
329|어느새 검푸른색으로 부어오른 손목을 확인하자 이가 갈린다.
330|
331|“진태경, 이 개새끼가.”
332|
333|그 자식은 처음부터 마음에 안 들었다. F급 헌터인 주제에 부팀장인 것도, 지금은 죽고 없는 전 팀장과 형제처럼 지내던 모습도 그랬다.
334|
335|‘저 새끼도 그때 같이 뒈졌어야 했는데.’
336|
337|2년 전 벌어진 불의의 사고는 김상식에게 있어 천운이었다.
338|
339|각종 성추문으로 일선에서 물러나 있던 그는 팀장으로 금의환향했고, 며칠 전 진태경까지 내보낼 수 있었으니까.
340|
341|‘그런데 이놈, 정말 재각성인가?’
342|
343|김상식은 욱신거리는 손목을 내려다봤다.
344|
345|그야말로 찰나의 순간이었지만 그때 느낀 힘은 어마어마했다. E급, 어쩌면 D급으로 재각성 했을지도 모를 일이다.
346|
347|“아니지, 재각성이 무슨 애들 장난도 아니고.”
348|
349|요즘 운동을 안 해서 약해진 건가. 김상식이 복잡한 심정으로 중얼거리던 순간이었다.
350|
351|“측정실에서 속보 왔습니다.”
352|
353|“괜찮은 놈 있대?”
354|
355|“월척 하나 떴답니다. C급.”
356|
357|“C급? 나쁘진 않은데 월척 소리 들을 정도는 아니잖아?”
358|
359|“그런데 마나 컨트롤이 A급이랍니다.”
360|
361|“뭐? A급! 빨대 꽂아, 빨리!”
362|
363|“예. 상동 길드 최민숩니다. 다름이 아니고…….”
364|
365|로비 입구를 하이에나처럼 어슬렁거리던 스카우터들 사이로 술렁임이 번졌다.
366|
367|대부분이 중소 길드에서 파견된 이들이었지만 대형 길드에서 나온 몇몇은 이미 발 빠르게 움직이고 있다.
368|
369|‘C급만 해도 상당한데, 마나 컨트롤까지 타고났어?’
370|
371|이건 대박이다.
372|
373|김상식은 정신이 번쩍 들었다. 진태경에 관한 생각은 저 멀리 내팽개치고 핸드폰을 꺼내 들었다.
374|
375|- 어, 김 팀장. 갔던 일은 잘됐고?
376|
377|수화기 너머 굵은 목소리의 주인은 소풍 길드장이었다.
378|
379|김상식이 다급하게 말했다.
380|
381|“길드장님. 지금 여기 난리 났습니다. C급 떴어요. 거기에 마나 컨트롤은 상위 헌터 수준이랍니다.”
382|
383|- 뭐? 그런 놈이 어디서 튀어나와?
384|
385|“그러니까요. 대형 길드 놈들, 매번 중간에 가로채더니 이번에는 한발 늦은 모양입니다.”
386|
387|- 좋아, 그렇단 말이지…….
388|
389|후욱. 훅.
390|
391|흥분했는지 거친 숨소리가 흘러나왔다. 김상식을 부르는 호칭도 바뀌었다.
392|
393|- 상식아. 너 이거 꼭 붙잡아라. 무조건 원하는 조건에 맞춘다고 해.
394|
395|“금액 어디까지 됩니까?”
396|
397|- 신경 쓰지 말고 다른 놈들 부르는 금액에 듬뿍 얹어 줘. 대형 길드 놈들이야 수지 좀 안 맞는다 싶으면 떨어질 거야. 그것들은 아쉬울 것도 없잖아?
398|
399|“예, 예.”
400|
401|- 나 지금 간다. 꼭 붙잡고 있어. 이거 성공시키면…… 알지?
402|
403|전화를 끊은 김상식은 주먹을 불끈 움켜쥐었다.
404|
405|‘됐다!’
406|
407|이 바닥에서 닳고 닳은 그다. 이제 막 각성한 신출내기 각성자 정도쯤이야 붙잡아 두는 건 일도 아니다.
408|
409|돈이면 귀신도 부리는 세상 아닌가.
410|
411|‘다른 놈들보다 무조건 두 배. 두 배 부른다.’
412|
413|그때 웅성거림이 더 커졌다. 측정실이 있는 3층에서 멈춘 엘리베이터가 로비를 향해 내려오고 있었다.
414|
415|“온다!”
416|
417|“아 거, 밀치지 좀 맙시다.”
418|
419|스카우터 이십여 명이 개미 떼처럼 입구에 달라붙었다. 우악스럽게 선두 자리를 차지한 김상식이 명함을 건넬 만반의 준비를 마쳤다.
420|
421|띵.
422|
423|그리고 마침내 열리는 엘리베이터 문.
424|
425|김상식은 넙죽 고개를 숙이며 준비해 둔 말을 꺼냈다.
426|
427|“안녕하십니까. 소풍 길드의 김상식 팀장입니다. 저희는 전통 있는 부천의 명문 길드로서…….”
428|
429|“소풍 길드가 명문이라는 소리는 또 처음 들어 보네.”
430|
431|“……네?”
432|
433|익숙한 목소리. 김상식의 고개가 슬그머니 들렸다.
434|
435|그리고 두 사람의 시선이 부딪쳤다. 단춧구멍 같던 김상식의 눈이 부릅떠진 것도 동시였다.
436|
437|“너, 너…….”
438|
439|진태경이 씩 웃었다.
440|
441|“또 만났네요. 김상식 씨.”
```

## Assembled English

```markdown
[P1]
# Chapter 47

[P2]
The Hunter Association.

[P3]
The name had appeared some thirty years ago, at the same time the Great Cataclysm ended.

[P4]
The first-generation Hunters who survived that blood-soaked catastrophe raised their flag, and over the years the Hunter Association grew into an organization of tremendous stature.

[P5]
Gulp.

[P6]
I swallowed as I stared up at the Association building standing tall before me. Even in this dense forest of skyscrapers, its size and height stood out. Even on an ordinary weekday, countless people streamed in and out.

[P7]
*How many years has it been?*

[P8]
Every Awakened had their rank assessed under the Association’s supervision.

[P9]
I was no exception. The thought of twenty-year-old Jin Taekyung walking in here all excited almost made me snort—

[P10]
Like hell it did.

[P11]
*Now that I’m actually here, I’m incredibly nervous.*

[P12]
I walked into the lobby on stiff legs. The place was the size of a sports field and packed with people. Following the electronic signs posted throughout, I found the place I was looking for.

[P13]
**Measurement Waiting Room**

[P14]
On the clerk’s instructions, I filled out the paperwork and went inside. Dozens of people were waiting to be measured.

[P15]
Thud.

[P16]
The door shut, and everyone’s eyes shot into me like arrows.

[P17]
*Suffocating. This is suffocating.*

[P18]
Even the air was different here. A taut tension pressed down on the entire waiting room.

[P19]
*One measurement decides your whole Hunter life.*

[P20]
I’d been the same way. I’d once gotten so nervous that I farted in front of an examiner. That pretty much said it all.

[P21]
I was waiting my turn, thinking about this and that, when—

[P22]
“Jin Taekyung?”

[P23]
A familiar voice came from behind me. I slowly turned my head.

[P24]
There he was.

[P25]
“I didn’t think it would be, but it is.”

[P26]
A middle-aged man with a bulbous nose and a potbelly. A face I couldn’t forget no matter how hard I tried.

[P27]
*…Team Leader Kim?*

[P28]
Kim Sangshik. A founding member and team leader of Sopung Guild, where I’d spent years. He could be summed up in two words.

[P29]
Former boss.

[P30]
“Wow, I never expected to run into you somewhere like this. Good to see you.”

[P31]
Team Leader Kim thrust out his hand with a hearty laugh. I hesitated for a moment, then shook it.

[P32]
“Likewise. It’s been a while.”

[P33]
“What do you mean, a while? It’s only been a few days.”

[P34]
“Those few days felt pretty long to me.”

[P35]
I’d said it thinking of Murim, but Team Leader Kim would take it another way. After all, he was the one who’d handed me my dismissal only a few days ago.

[P36]
“It’s because it’s summer. My days have felt long lately too.”

[P37]
“Really?”

[P38]
Watching him slide past it like a sly old fox, I let out a hollow laugh.

[P39]
He was a funny guy, no matter when you saw him.

[P40]
In more ways than one.

[P41]
“So what brings you here?”

[P42]
“I had some business. What about you, Team Leader?”

[P43]
“Came to scout. Heard there was a decent one this time.”

[P44]
They’d fired me for staff cuts in a restructuring. And he was here to scout.

[P45]
“I see.”

[P46]
That was all I had to say. It was the same tired story everyone knew, and the story was already over. I had no lingering attachment to it.

[P47]
“What about you? Why are you here? Don’t tell me you’re trying to get reassessed.”

[P48]
“Yes.”

[P49]
Team Leader Kim smiled.

[P50]
“Well, it’s good to try, but isn’t that a waste of money? A reassessment isn’t cheap. Must be a burden for an F-rank Hunter.”

[P51]
“I still figured I’d give it a shot. Just in case.”

[P52]
“You should save up while you’re young. What’s going to change if you keep clinging to something that isn’t going to work?”

[P53]
“Who knows? I think this time might be different.”

[P54]
“It’s not that easy—”

[P55]
“Team Leader.”

[P56]
“Huh? What?”

[P57]
I smiled gently.

[P58]
“That’s enough.”

[P59]
A crack ran through Team Leader Kim’s smile.

[P60]
“What?”

[P61]
“I said that’s enough. I’m out of the Guild now, so stay out of my business.”

[P62]
“What’s that supposed to mean?”

[P63]
What did he think it meant?

[P64]
“You know what I mean.”

[P65]
“…”

[P66]
“It couldn’t be helped. You’re lucky you survived. Forget it all and make a fresh start. You pecked away at me behind my back while pretending to console me.”

[P67]
“You…”

[P68]
“Weren’t you the one who first told the Guild Master to fire me? Did you think I wouldn’t know?”

[P69]
Kim Sangshik was a half-baked, petty little man.

[P70]
Short on humanity, short on ability.

[P71]
Even in Gates, he was too busy saving his own skin. His reputation in the Guild was rock-bottom.

[P72]
“Who did you put in my place after you fired me? How much did you take to slot someone in?”

[P73]
“Hey, Jin Taekyung.”

[P74]
Team Leader Kim clamped a hand down on my shoulder and growled. He might not have looked it, but he was one of only three D-rank Hunters in Sopung Guild. With that kind of strength, he could toy with an F-rank Hunter like me using one hand.

[P75]
But—

[P76]
“Take your hand off.”

[P77]
I didn’t even blink. The System wasn’t the only thing that had synchronized. My martial arts, my stats, even my steel-like Sinews and Bones had come with it.

[P78]
“I’ll count to three. Take your hand off.”

[P79]
“You little bastard. I’ve been putting up with you, but—”

[P80]
I didn’t hesitate.

[P81]
“One. Two.”

[P82]
Three.

[P83]
The instant I grabbed Kim Sangshik’s wrist—

[P84]
Clack.

[P85]
“Would the next group please come in? Numbers twenty-one through thirty!”

[P86]
An Association examiner walked in with a file, and we both let go before the other could. Getting marked by the Association wouldn’t do either of us any good.

[P87]
“Consider yourself lucky.”

[P88]
“Who. Me? Or you?”

[P89]
Kim Sangshik’s flushed face looked downright ridiculous.

[P90]
So did the Level Window I’d picked up through Qi Sense.

[P91]
> **System**
>
> Lv. 24 Kim Sangshik

[P92]
“It was disgusting seeing you. Let’s never meet again.”

[P93]
I got up without a shred of regret. My waiting number was thirty.

[P94]
The steps I took toward the examiner weren’t stiff anymore.

[P95]
* * *

[P96]
“Number twenty-one. Please come forward.”

[P97]
An Awakened with a tense face stood in front of the measuring device. Made from an A-rank Magic Gem, it scanned his whole body and converted the mana inside him into numbers.

[P98]
Bzzzzzt—

[P99]
The examiner checked the reading and spoke.

[P100]
“Mana distribution in the body: F-rank.”

[P101]
The Awakened’s face turned ashen. But it was too soon to despair. He still had a second chance.

[P102]
“Try moving your mana. Concentrate as hard as you can, and imagine firing it into the measuring device.”

[P103]
They were checking his mana control. Realizing it wasn’t over yet, the Awakened gritted his teeth and drew up his strength.

[P104]
Every last ounce of it—ngh!

[P105]
Bwoooom.

[P106]
“…”

[P107]
“…”

[P108]
Looking ready to vomit, the examiner spoke.

[P109]
“Control ability: F-rank.”

[P110]
“Just once! Let me try one more time!”

[P111]
“No. Next.”

[P112]
The line moved fast.

[P113]
Everyone was E-rank or F-rank. One guy wasn’t even Awakened.

[P114]
“This is a scam! A scam! That measuring device is made in China, isn’t it? Huh? You bastards!”

[P115]
“Handle him.”

[P116]
At the examiner’s word, the security Hunters waiting nearby dragged the fraud out. Even if that guy miraculously Awakened, he’d probably end up on the Association’s blacklist.

[P117]
“Next. Number thirty.”

[P118]
Here it came.

[P119]
I took a deep breath and stepped forward. The examiner glanced at the file in his hand.

[P120]
“This is a reassessment?”

[P121]
“Yes.”

[P122]
“Mr. Jin Taekyung, you received F-rank seven years ago… and you know there’s a separate fee for reassessments, right?”

[P123]
From the way he said it, he might as well have been telling me not to waste my money and to go home while I still could. The usual look people gave an F-rank Hunter.

[P124]
*Do they think I’m a beggar?*

[P125]
I was used to it, but that didn’t make it any less filthy. When I glared at him, the examiner gave a short puff of a laugh.

[P126]
“I’m only mentioning it in case you weren’t aware, but the fee is two million won.”

[P127]
“…The price went up?”

[P128]
“It’s been a few years.”

[P129]
*Fuck. I didn’t know that.*

[P130]
How much was in my account right now…?

[P131]
“Then we’ll begin the assessment.”

[P132]
With my heart trembling, I closed my eyes.

[P133]
And the next moment—

[P134]
Bzzzzzt.

[P135]
A wave of mana flowed from the measuring device and swept over my entire body.

[P136]
Fifteen years of internal energy answered it and shuddered.

[P137]
*What rank will it be?*

[P138]
C-rank? No, I’d be happy with D-rank.

[P139]
But ten seconds or so passed, and the examiner still didn’t open his mouth.

[P140]
“Uh… why is it doing this?”

[P141]
“Why?”

[P142]
He looked back and forth between the device and me, visibly flustered, then cleared his throat.

[P143]
“There seems to be some kind of error… We’ll move on to the next step for now.”

[P144]
I had no idea what was going on, but strangely, it didn’t feel ominous.

[P145]
*I’ve got a good feeling about this.*

[P146]
My heart pounding, I drew up my internal energy.

[P147]
Ssshhh.

[P148]
At the call of the Jin Family’s Cultivation Technique, fifteen years of internal energy surged up and shot toward the measuring device.

[P149]
* * *

[P150]
At the lobby entrance.

[P151]
“Well done.”

[P152]
Kim Sangshik patted a young man on the shoulder. As of today, the promising young man had officially been recognized as a D-rank Awakened.

[P153]
He would soon join Sopung Guild and be assigned to Kim Sangshik’s team. Thinking of that coming day, Kim Sangshik smiled proudly.

[P154]
“Father and son on the same team. That’s my boy.”

[P155]
“Come on, I’m not even an official Hunter yet. I still have to enter the training center.”

[P156]
“Don’t worry. Your father already made arrangements.”

[P157]
“Wait, really? Didn’t you say there weren’t any openings in the Guild?”

[P158]
“There’s always a way.”

[P159]
He didn’t mention that, in the process, he’d cut the lowest-rank Hunter who’d been a thorn in his side.

[P160]
“Anyway, get plenty of rest this week. Starting next week, we’ll go to work together—”

[P161]
Kim Sangshik’s expression suddenly twisted.

[P162]
“What’s wrong?”

[P163]
“…Nothing. Go wait in the car.”

[P164]
After his son left, he was alone. He rolled up his shirtsleeve.

[P165]
His wrist had already swollen to a dark blue-black. The sight made him grind his teeth.

[P166]
“Jin Taekyung, that fucking bastard.”

[P167]
He’d disliked that bastard from the start. An F-rank Hunter as deputy team leader, and the way he’d been like brothers with the former team leader, who was dead now.

[P168]
*That bastard should’ve fucking died with him back then.*

[P169]
The unfortunate accident two years ago had been a stroke of tremendous luck for Kim Sangshik.

[P170]
After various sex scandals had forced him away from the front lines, he’d made a triumphant return as team leader. A few days ago, he’d even managed to force Jin Taekyung out.

[P171]
*But did that bastard really reawaken?*

[P172]
Kim Sangshik stared down at his throbbing wrist.

[P173]
It had lasted only an instant, but the strength he’d felt had been tremendous. Taekyung might have reawakened as an E-rank, or possibly even a D-rank.

[P174]
“No. Reawakening isn’t child’s play.”

[P175]
Maybe he’d grown weaker because he hadn’t exercised lately.

[P176]
Kim Sangshik was muttering, mixed up inside, when—

[P177]
“We have breaking news from the measurement room.”

[P178]
“Someone good?”

[P179]
“They say a big fish surfaced. C-rank.”

[P180]
“C-rank? Not bad, but that’s not enough to call a big fish, is it?”

[P181]
“But they say his mana control is A-rank.”

[P182]
“What? A-rank! Get a straw in him, now!”

[P183]
“Yes. This is Choi Min-su from Sangdong Guild. The thing is—”

[P184]
A stir spread through the scouts prowling the lobby entrance like hyenas.

[P185]
Most had been dispatched by small and midsized Guilds, but the handful from major Guilds were already moving quickly.

[P186]
*C-rank alone is impressive, and he’s gifted with mana control on top of it?*

[P187]
This was a jackpot.

[P188]
Kim Sangshik’s mind snapped into focus. He shoved every thought of Jin Taekyung far away and pulled out his phone.

[P189]
—Hey, Team Leader Kim. Did that business go well?

[P190]
The deep voice on the other end belonged to Sopung Guild’s Guild Master.

[P191]
Kim Sangshik answered urgently.

[P192]
“Guild Master, all hell has broken loose here. A C-rank just appeared, and they say his mana control is at the level of a high-ranking Hunter.”

[P193]
—What? Where did a guy like that come from?

[P194]
“Exactly. The major Guilds always snatch them up midway, but it looks like they were a step late this time.”

[P195]
—Good. So that’s how it is…

[P196]
Huff. Huff.

[P197]
Rough breaths came through the phone, as if the Guild Master was excited. Even the way he addressed Kim Sangshik changed.

[P198]
—Sangshik. Hold on to this guy no matter what. Tell him we’ll meet any conditions he asks for.

[P199]
“How high can we go on the money?”

[P200]
—Don’t worry about it. Pile plenty on top of whatever the others offer. The major Guilds will drop out if they decide it isn’t profitable enough. It’s not like they’re desperate.

[P201]
“Yes, yes.”

[P202]
—I’m on my way. Keep hold of him until I get there. If you pull this off… you know what that means, right?

[P203]
Kim Sangshik hung up and clenched his fist.

[P204]
*We’ve got this!*

[P205]
He’d been worn smooth by years in this business. Holding on to a newly Awakened rookie was nothing.

[P206]
This was a world where money could put even ghosts to work.

[P207]
*Twice what everyone else offers. I’ll quote double, no matter what.*

[P208]
The commotion grew louder. The elevator that had stopped on the third floor, where the measurement room was, was coming down toward the lobby.

[P209]
“He’s coming!”

[P210]
“Hey, stop shoving.”

[P211]
About twenty scouts clung to the entrance like a swarm of ants. Kim Sangshik had muscled his way into the lead and was ready to hand over his business card.

[P212]
Ding.

[P213]
At last, the elevator doors opened.

[P214]
Kim Sangshik bowed low and launched into the words he’d prepared.

[P215]
“Hello. I’m Team Leader Kim Sangshik of Sopung Guild. We’re a prestigious Guild with a long tradition here in Bucheon—”

[P216]
“This is the first time I’ve heard anyone call Sopung a prestigious Guild.”

[P217]
“…What?”

[P218]
The familiar voice made Kim Sangshik lift his head, gingerly.

[P219]
Their eyes met.

[P220]
At the same moment, Kim Sangshik’s buttonhole-sized eyes flew wide open.

[P221]
“You, you…”

[P222]
Jin Taekyung grinned.

[P223]
“We meet again, Mr. Kim Sangshik.”
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 47

[P2]
Hunter Association.

[P3]
The name had appeared some thirty years ago, at the same time the Great Cataclysm ended.

[P4]
The first-generation Hunters who survived that blood-soaked catastrophe raised their flag, and over the years the Hunter Association grew into an organization of tremendous stature.

[P5]
Gulp.

[P6]
I swallowed as I stared up at the Association building standing tall before me. Even in this dense forest of skyscrapers, its size and height stood out. Even on an ordinary weekday, people streamed in and out.

[P7]
*How many years has it been?*

[P8]
Every Awakened underwent rank measurement under the Association’s supervision.

[P9]
I was no different. The thought of twenty-year-old Jin Taekyung walking in here all excited almost made me snort—like hell it did.

[P10]
*Now that I’m actually here, I’m incredibly nervous.*

[P11]
I went into the lobby on stiff legs. The place was the size of a sports field and packed with people. I followed the electronic signs posted throughout until I found what I wanted.

[P12]
**Measurement Waiting Room**

[P13]
On the clerk’s instructions, I filled out the paperwork and went inside. Dozens of people were waiting to be measured.

[P14]
Thud.

[P15]
The door shut, and everyone’s eyes shot into me like arrows.

[P16]
*Suffocating. This is suffocating.*

[P17]
Even the air was different here. A taut tension pressed down on the entire waiting room.

[P18]
*One measurement decides your whole Hunter life.*

[P19]
I was no different. I’d been so nervous I’d even farted in front of an examiner once. That pretty much said it all.

[P20]
I was waiting my turn, thinking about this and that, when—

[P21]
“Jin Taekyung?”

[P22]
A familiar voice from behind me. I turned my head slowly.

[P23]
There he was.

[P24]
“I didn’t think it would be, but it is.”

[P25]
A middle-aged man with a bulbous nose and a potbelly. A face I couldn’t forget no matter how hard I tried.

[P26]
*…Team Leader Kim?*

[P27]
Kim Sangshik. A founding member and team leader of Sopung Guild, where I’d spent years. He could be summed up in one word.

[P28]
Former boss.

[P29]
“Wow, I never expected to run into you somewhere like this. Good to see you.”

[P30]
Team Leader Kim thrust out his hand with a hearty laugh. I hesitated a moment, then took it.

[P31]
“Likewise. It’s been a while.”

[P32]
“What do you mean, a while? It’s only been a few days.”

[P33]
“Those few days felt pretty long to me.”

[P34]
I’d said it thinking of Murim, but Team Leader Kim would hear something else. After all, he was the one who’d handed me my dismissal only a few days ago.

[P35]
“It’s because it’s summer. My days have felt long lately too.”

[P36]
“Really?”

[P37]
Watching him slide past it like a sly old fox, I let out a hollow laugh.

[P38]
He was a funny guy, no matter when you saw him.

[P39]
In more ways than one.

[P40]
“So what brings you here?”

[P41]
“I had some business. What about you, Team Leader?”

[P42]
“Came to scout. Heard there was a decent one this time.”

[P43]
They’d fired me for staff cuts in a restructuring. And he was here to scout.

[P44]
“I see.”

[P45]
That was all I had to say. Everyone knew that tired story, and it was already over. I had no lingering attachment left.

[P46]
“What about you? Why are you here? Don’t tell me you’re trying to get reassessed.”

[P47]
“Yes.”

[P48]
Team Leader Kim spoke with a smile.

[P49]
“Nice try, but isn’t that a waste of money? A reassessment isn’t cheap. Must be a burden for an F-rank Hunter.”

[P50]
“Still, I figured I’d try. Just in case.”

[P51]
“You should save up while you’re young. What’s going to change if you keep clinging to something that isn’t going to work?”

[P52]
“Who knows? I think this time might be different.”

[P53]
“It’s not that easy—”

[P54]
“Team Leader.”

[P55]
“Huh? What?”

[P56]
I smiled, gentle.

[P57]
“That’s enough.”

[P58]
A crack ran through Team Leader Kim’s smile.

[P59]
“What?”

[P60]
“I said that’s enough. I’ve left the Guild now, so stay out of my business.”

[P61]
“What’s that supposed to mean?”

[P62]
What did it mean?

[P63]
“You know what I mean.”

[P64]
“…”

[P65]
“It couldn’t be helped. You’re lucky you survived. Forget it all and make a fresh start. You pecked away at me behind my back while pretending to console me.”

[P66]
“You…”

[P67]
“Weren’t you the one who first told the Guild Master to cut me? Did you think I wouldn’t know?”

[P68]
Kim Sangshik was a half-baked, petty little man.

[P69]
Short on humanity, short on ability.

[P70]
Even in Gates, he was too busy saving his own skin. His reputation in the Guild was rock-bottom.

[P71]
“Who did you put in my place after you fired me? How much did you take to slot someone in?”

[P72]
“Hey. Jin Taekyung.”

[P73]
Team Leader Kim clamped down on my shoulder and growled. He didn’t look it, but he was one of only three D-rank Hunters in Sopung Guild. With that kind of strength, he could have toyed with an F-rank Hunter like me with one hand.

[P74]
But—

[P75]
“Take your hand off.”

[P76]
I didn’t even blink. It wasn’t only the System that had synchronized. My martial arts, my stats, and even my steel-like Sinews and Bones had come with it.

[P77]
“I’ll count to three. Take your hand off.”

[P78]
“You little bastard. I’ve been putting up with you, but—”

[P79]
I didn’t hesitate.

[P80]
“One. Two.”

[P81]
Three.

[P82]
The instant I grabbed Kim Sangshik’s wrist—

[P83]
Clack.

[P84]
“Would the next group please come in. Numbers twenty-one through thirty!”

[P85]
An Association examiner walked in with a file, and we both let go before the other could. Getting marked by the Association wouldn’t do either of us any good.

[P86]
“Consider yourself lucky.”

[P87]
“Who. Me? Or you?”

[P88]
Kim Sangshik’s flushed face looked downright ridiculous. Even the Level Window I’d picked up through Qi Sense.

[P89]
> **System**
> Lv. 24 Kim Sangshik

[P90]
“Meeting you was disgusting. Let’s never see each other again.”

[P91]
I got up without a shred of regret. My waiting number was thirty. The steps I took toward the examiner weren’t stiff anymore.

[P92]
* * *

[P93]
“Number twenty-one. Please come forward.”

[P94]
An Awakened with a tense face stood in front of the measuring device. Made from an A-rank Magic Gem, it scanned his whole body and converted the mana inside him into numbers.

[P95]
Bzzzzzt—

[P96]
The examiner checked the reading and spoke.

[P97]
“Mana distribution in the body: F-rank.”

[P98]
The Awakened’s face turned ashen. But it was too soon to despair. He had a second chance.

[P99]
“Try moving your mana. Concentrate as hard as you can, and imagine firing it into the measuring device.”

[P100]
They were checking his mana control. Realizing it wasn’t over yet, the Awakened gritted his teeth and drew up his strength.

[P101]
Every last ounce of it—ngh!

[P102]
Bwoooom.

[P103]
“…”

[P104]
“…”

[P105]
The examiner spoke with a face that looked ready to vomit.

[P106]
“Control ability: F-rank.”

[P107]
“Just once! Let me try one more time!”

[P108]
“No. Next.”

[P109]
The line moved fast.

[P110]
All E-rank or F-rank. One guy wasn’t even Awakened.

[P111]
“This is a scam! A scam! That measuring device is made in China, isn’t it? Huh? You bastards!”

[P112]
“Handle him.”

[P113]
At the examiner’s word, the security Hunters waiting nearby dragged the fraud out. Even if that guy miraculously Awakened, he’d probably end up on the Association’s blacklist.

[P114]
“Next. Number thirty.”

[P115]
Here it came.

[P116]
I took a deep breath and stepped forward. The examiner glanced at the file in his hand.

[P117]
“This is a reassessment?”

[P118]
“Yes.”

[P119]
“Mr. Jin Taekyung, you received F-rank seven years ago… and you know there’s a separate fee for reassessments, right?”

[P120]
From the way he said it, he might as well have been telling me not to waste my money and to go home while I still could. The usual look people gave an F-rank Hunter.

[P121]
*Do they think I’m a beggar?*

[P122]
Familiar was one thing. Still filthy was another. When I glared at him, the examiner gave a short puff of a laugh.

[P123]
“I’m only mentioning it in case you weren’t aware, but the fee is two million won.”

[P124]
“…The price went up?”

[P125]
“It’s been a few years.”

[P126]
*Fuck. I didn’t know that.*

[P127]
How much was in my account right now…?

[P128]
“Then we’ll begin the assessment.”

[P129]
Nervous, I closed my eyes.

[P130]
And the next moment—

[P131]
Bzzzzzt.

[P132]
A wave of mana rolled out of the measuring device and swept through my whole body.

[P133]
Fifteen years of internal energy answered it and shuddered.

[P134]
*What rank will it be?*

[P135]
C-rank? No, I’d be happy with D-rank. But ten seconds or so passed, and the examiner still didn’t open his mouth.

[P136]
“Uh… why is it doing this?”

[P137]
“Why?”

[P138]
He looked from the device to me, flustered, then cleared his throat.

[P139]
“There seems to be some kind of error… We’ll move on to the next step for now.”

[P140]
I had no idea what was going on, but strangely, it didn’t feel ominous.

[P141]
*This feels good.*

[P142]
Feeling my heart pound, I drew up my internal energy.

[P143]
Ssshhh.

[P144]
At the call of the Jin Family’s Cultivation Technique, fifteen years of internal energy surged up and shot toward the measuring device.

[P145]
* * *

[P146]
The lobby entrance.

[P147]
“Well done.”

[P148]
Kim Sangshik patted a young man on the shoulder. As of today, he was a promising young D-rank Awakened, officially recognized.

[P149]
He would soon join Sopung Guild and be assigned to Kim Sangshik’s team. Thinking of that coming day, Kim Sangshik smiled, proud.

[P150]
“Father and son on the same team. That’s my boy.”

[P151]
“What are you talking about? I’m not even an official Hunter yet. I still have to go through the training center.”

[P152]
“Don’t worry. Your father already took care of it.”

[P153]
“Wait, really? Didn’t you say the Guild didn’t have a spot?”

[P154]
“There’s always a way.”

[P155]
He didn’t mention that, in the process, he’d cut the lowest-rank Hunter who’d been a thorn in his eye.

[P156]
“Anyway, rest up this week, and starting next week we’ll commute together—”

[P157]
Kim Sangshik’s face suddenly twisted.

[P158]
“What’s wrong?”

[P159]
“…Nothing. Go wait in the car.”

[P160]
After his son left, he was alone. He rolled up his shirtsleeve.

[P161]
His wrist had already swollen a dark blue-green. The sight made him grind his teeth.

[P162]
“Jin Taekyung, you fucking bastard.”

[P163]
He’d disliked that bastard from the start. An F-rank Hunter as deputy team leader, and the way he’d been like brothers with the old team leader, who was dead now.

[P164]
*That bastard should’ve fucking died with him back then.*

[P165]
The unfortunate accident two years ago had been a stroke of luck for Kim Sangshik.

[P166]
After being sidelined by various sex scandals, he’d made a triumphant return as team leader. A few days ago, he’d even gotten Jin Taekyung thrown out.

[P167]
*But was this bastard really a reawakening?*

[P168]
Kim Sangshik stared down at his throbbing wrist.

[P169]
It had only lasted an instant, but the strength he’d felt then had been tremendous. Taekyung might have reawakened as E-rank—or even D-rank.

[P170]
“No. Reawakening isn’t child’s play.”

[P171]
Maybe he’d gotten weaker from not exercising lately. Kim Sangshik was muttering, mixed up inside, when—

[P172]
“We have breaking news from the measurement room.”

[P173]
“Someone good?”

[P174]
“They say a big fish surfaced. C-rank.”

[P175]
“C-rank? Not bad, but that’s not enough to call a big fish, is it?”

[P176]
“But they say his mana control is A-rank.”

[P177]
“What? A-rank! Get a straw in him, now!”

[P178]
“Yes. This is Choi Min-su from Sangdong Guild. The thing is—”

[P179]
A stir spread through the scouts prowling the lobby entrance like hyenas.

[P180]
Most of them had been sent by small and midsized Guilds, but a few from the major ones were already moving fast.

[P181]
*C-rank alone is impressive, and he’s gifted with mana control on top of it?*

[P182]
This was a jackpot.

[P183]
Kim Sangshik’s mind snapped clear. He shoved every thought of Jin Taekyung far away and pulled out his phone.

[P184]
—Hey, Team Leader Kim. Did that business go well?

[P185]
The deep voice on the other end belonged to Sopung Guild’s Guild Master.

[P186]
Kim Sangshik spoke in a rush.

[P187]
“Guild Master, it’s chaos here. A C-rank just showed up. And they say his mana control is at the level of a high-ranking Hunter.”

[P188]
—What? Where did a guy like that come from?

[P189]
“Exactly. The major Guilds always snatch them up midway, but it looks like they were a step late this time.”

[P190]
—Good. So that’s how it is…

[P191]
Huff. Huff.

[P192]
Rough breaths came through the phone, as if he was excited. Even the way he addressed Kim Sangshik changed.

[P193]
—Sangshik. You hold on to this guy no matter what. Tell him we’ll meet whatever conditions he wants.

[P194]
“How high can we go on the money?”

[P195]
—Don’t worry about it. Pile plenty on top of whatever the others offer. The major Guilds will drop out if they decide it isn’t profitable enough. It’s not like they need him.

[P196]
“Yes, yes.”

[P197]
—I’m on my way. Keep hold of him until I get there. If we pull this off… you know what that means, right?

[P198]
After hanging up, Kim Sangshik clenched his fist.

[P199]
*We’ve got this!*

[P200]
He’d been worn smooth by years in this business. Holding on to a newly Awakened rookie was nothing.

[P201]
This was a world where money could put even ghosts to work.

[P202]
*Twice what everyone else offers. I’ll quote double, no matter what.*

[P203]
The commotion grew louder. The elevator that had stopped on the third floor, where the measurement room was, was coming down toward the lobby.

[P204]
“He’s coming!”

[P205]
“Hey, stop shoving.”

[P206]
About twenty scouts clung to the entrance like a swarm of ants. Kim Sangshik had muscled his way into the lead and was ready to hand over his card.

[P207]
Ding.

[P208]
At last, the elevator doors opened.

[P209]
Kim Sangshik bowed low and launched into the words he’d prepared.

[P210]
“Hello. I’m Team Leader Kim Sangshik of Sopung Guild. We’re a prestigious Guild with a long tradition here in Bucheon—”

[P211]
“This is the first time I’ve heard anyone call Sopung a prestigious Guild.”

[P212]
“…What?”

[P213]
The familiar voice made Kim Sangshik lift his head, gingerly.

[P214]
Their eyes met.

[P215]
At the same time, Kim Sangshik’s buttonhole-sized eyes went wide.

[P216]
“You, you…”

[P217]
Jin Taekyung grinned.

[P218]
“We meet again, Mr. Kim Sangshik.”
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 47,
  "passed": true,
  "metrics": {
    "source_characters": 6247,
    "translation_characters": 13554,
    "length_ratio": 2.17,
    "source_paragraphs": 212,
    "translation_paragraphs": 223
  },
  "errors": [],
  "warnings": [
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
        "korean": "등급",
        "preferred": "Grade"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "소풍",
        "romanization": "sopung"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "상동",
        "romanization": "sangdong"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "부천",
        "romanization": "bucheon"
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
