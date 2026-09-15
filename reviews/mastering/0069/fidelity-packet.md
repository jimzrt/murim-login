# Fidelity Gate — Chapter 69

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
  1|＃69화
  2|
  3|
  4|
  5|모두가 잠든 깊은 밤. 진위경은 비명과 함께 눈을 떴다.
  6|
  7|“크허업!”
  8|
  9|맹렬한 기세로 양팔을 허우적거리던 그는 얼마 지나지 않아 자신이 현실로 돌아왔음을 깨달았다.
 10|
 11|일렁이는 등잔불과 탁자를 가득 채운 서류. 익숙한 집무실의 풍경이다.
 12|
 13|“휴우.”
 14|
 15|안도의 한숨을 내쉰 진위경이 목덜미를 주물렀다. 악몽을 꾼 탓인지 목덜미는 식은땀으로 축축했다.
 16|
 17|‘죽는 줄 알았네.’
 18|
 19|땅이 갈라지고 하늘이 무너지는 꿈이었다. 천지를 진동하는 굉음을 피해 턱에 숨이 차도록 도망치다가 넘어진 것이 마지막 기억이다.
 20|
 21|‘너무 무리해서 그런가.’
 22|
 23|처리해야 할 일은 넘쳐나는데 인력은 턱없이 부족하다. 피 말리는 하루하루의 연속이다 보니 피로는 쌓여만 갔다.
 24|
 25|“끙. 빨리 사람을 뽑든가 해야지. 이러다가는 제 명에 못 살겠어.”
 26|
 27|천하는 넓고 인재는 많다. 그런데도 아직 변변한 책사 하나 없는 것은 태원진가의 역량이 부족했기 때문이다.
 28|
 29|두 팔 벌려 환영하는 중원의 거대 문파나 이름난 세가(世家)를 놔두고 뭣 하러 산서의 태원진가에 몸을 담겠는가?
 30|
 31|그들로서는 당연한 선택일지도 모른다.
 32|
 33|‘지금까지는, 말이지.’
 34|
 35|이제는 모든 게 바뀔 것이다. 다가오는 원단에 산서 무림을 일통하고 계속해서 영향력을 확장한다면…… 머지않아 태원진가의 깃발 아래로 천하의 인재들이 몰려드는 날이 올 것이다.
 36|
 37|‘……그전에 과로로 죽겠지만.’
 38|
 39|진위경이 살벌한 양의 서류 더미를 보며 깊은 한숨을 내쉬던 그때였다.
 40|
 41|쿠르릉.
 42|
 43|아주 미세한 소리. 절정 고수인 진위경이기에 알아차릴 수 있을 만큼 작은 소음이 울렸다.
 44|
 45|‘뭐지?’
 46|
 47|그는 감각을 곤두세웠다. 공력을 귀에 집중시키자 소리가 또렷해졌다.
 48|
 49|쿠르릉. 캉.
 50|
 51|작지만 분명히 들었다. 강철이 부딪치는 소리.
 52|
 53|누군가 싸우고 있는 것이다. 그것도 이 야심한 시각에.
 54|
 55|진위경의 얼굴이 굳은 이유는 그 사실 때문만은 아니었다.
 56|
 57|‘저 방향은…….’
 58|
 59|진무경의 처소가 있는 곳이다. 그리고 어제부로 한 사람이 더 들어가게 된 곳.
 60|
 61|‘설마 무경이가 막내를……. 에이, 아니겠지.’
 62|
 63|사이좋게 지내라고 그렇게 신신당부했는데 벌써 치고받고 싸우겠는가. 그는 사랑하는 아우들을 굳게 믿었다.
 64|
 65|캉. 캉!
 66|
 67|“…….”
 68|
 69|진위경이 슬그머니 자리에서 일어났다.
 70|
 71|
 72|
 73|* * *
 74|
 75|
 76|
 77|작정하고 경신법을 펼치자 진무경의 처소까지는 금방이었다.
 78|
 79|문제는 목적지가 가까워질수록 들려오는 소리가 심상치 않다는 것에 있었다.
 80|
 81|‘……연무장에서 혼자 수련하는 거겠지?’
 82|
 83|전각 안으로 들어가야 하나, 말아야 하나. 잠시 고민하던 진위경은 담벼락 위로 고개를 빼꼼 내밀었다.
 84|
 85|그리고 충격적인 광경을 목격했다.
 86|
 87|“내가, 말했지. 두 번째 규칙. 어?”
 88|
 89|쾅! 콰광!
 90|
 91|쉬지 않고 검집을 휘두르는 진무경. 그리고 그런 그를 피해 정신없이 도망치는 한 사람.
 92|
 93|“로, 로그아웃!”
 94|
 95|진태경의 필사적인 외침이 끝나기도 전에 검집이 날아들었다. 아슬아슬하게 비껴간 검집이 연무장의 청석(靑石)을 박살 냈다.
 96|
 97|콰앙!
 98|
 99|“내가, 이 새끼야, 주화입마, 임독양맥!”
100|
101|“로그아우우웃!”
102|
103|“…….”
104|
105|노구아욱은 뭐고 주화입마에 임독양맥은 왜 튀어나오는가.
106|
107|당최 알 수 없는 대화의 흐름이었지만 한 가지는 확실했다.
108|
109|‘저러다가 일 나겠군.’
110|
111|이대로라면 정말 의원이든 장의사든 둘 중 하나는 불러야 할지도 모르는 판이다.
112|
113|‘막내는 내가 지킨다!’
114|
115|진위경이 결의에 찬 얼굴로 난입하려던 그때.
116|
117|“옆구리는 왜 또 비어? 맞고 싶어서 안달 났냐?”
118|
119|뻑!
120|
121|“커흑!”
122|
123|옆구리에 일격을 얻어맞은 진태경이 비틀거렸다. 진무경이 때를 놓치지 않고 따라붙으며 검집을 휘둘렀다.
124|
125|퍼버벅!
126|
127|“악, 악, 악!”
128|
129|“맞았다고 움츠러들지 마라. 특히 하체!”
130|
131|퍽!
132|
133|“이익!”
134|
135|“어쭈.”
136|
137|이를 악물고 달려드는 아우의 모습에 진무경이 가소롭다는 듯이 웃었다.
138|
139|“넌 기본도 안 된 놈이야. 본능대로 손 뻗고 발 나가는 습관부터 고쳐. 무공은 사람이 익히는 거지 짐승이 익히는 게 아니니까.”
140|
141|“닥쳐!”
142|
143|“기억력도 안 좋은 놈이군. 푹 자라. 일어나면 규칙을 다시 한번 설명해 주마.”
144|
145|쉭! 털썩.
146|
147|정통으로 턱을 얻어맞은 진태경의 신형이 허물어졌다. 대자로 뻗은 그를 말없이 내려다보던 진무경이 천천히 입을 열었다.
148|
149|“나오십시오.”
150|
151|누구에게 한 말인지는 명백하다. 머쓱한 얼굴의 진위경이 담벼락 뒤에서 모습을 드러냈다.
152|
153|“알고 있었느냐?”
154|
155|“모르는 게 이상하죠. 이 녀석 맞을 때마다 형님 침 삼키는 소리가 천둥처럼 들리던데요.”
156|
157|진위경이 걱정스러운 눈빛으로 쓰러진 진태경의 상태를 살폈다.
158|
159|“그렇게 심한 상처는 아니구나. 다행이다.”
160|
161|“설마 죽기야 하겠습니까?”
162|
163|“무경아!”
164|
165|“걱정 마십시오. 근골 하나는 기가 막히게 튼튼한 녀석이니까요.”
166|
167|“그래?”
168|
169|“그렇게 두들겨 맞으면서도 두 시진이나 버티더군요. 이 정도 체력과 독기면 금방…… 왜 웃으십니까?”
170|
171|묘한 미소를 머금은 채로 동생의 얼굴을 들여다보던 진위경이 흔쾌히 대답했다.
172|
173|“신기해서. 네가 막내 칭찬하는 건 처음 아니냐?”
174|
175|그 말에 진무경이 멈칫했다.
176|
177|‘칭찬? 내가 저 녀석을?’
178|
179|있을 수 없는 일이다. 장점이라고는 눈곱만큼도 없는 동생 아닌가. 가문이 어떻게 돌아가든 말든 술독에 빠져 계집질이나 일삼던 놈을 자신이 칭찬했다니.
180|
181|진무경은 애써 고개를 저었다.
182|
183|“……그런 적 없습니다.”
184|
185|“그렇구나.”
186|
187|“정말입니다.”
188|
189|“알았다. 누가 뭐라던?”
190|
191|“아니, 지금도 웃고 계시잖습니까!”
192|
193|“그런 적 없다.”
194|
195|“형님!”
196|
197|진위경은 터져 나오려는 웃음을 참으려 애썼다. 눈에 넣어도 아프지 않을 막내가 다친 건 마음 아픈 일이지만…… 언젠가는 겪어야 할 일이었다.
198|
199|‘언제까지 품 안에 둘 수는 없어.’
200|
201|산서잠룡. 태원진가가 배출한 또 한 명의 천재.
202|
203|그는 훌쩍 커 버린 아우를 보며 기쁨과 불안감을 동시에 느꼈다. 아니, 그건 어쩌면 두려움이었다.
204|
205|‘이게 가능한 일인가?’
206|
207|빨라도 너무 빠르다. 진무경이라는 천재를 가장 가까이서 지켜본 그의 눈에도 진태경의 성장 속도는 불가해(不可解)의 영역이다.
208|
209|‘나로서는 도저히 가늠이 안 돼.’
210|
211|어린 시절, 진위경은 촉망받는 기재였지만 결코 천재는 아니었다. 자신 같은 범인(凡人)이 어찌 천재를 이해하고, 가르칠 수 있단 말인가?
212|
213|그렇게 고민이 깊어 가던 찰나에 진무경이 돌아온 것이다.
214|
215|진위경은 이때구나, 하고 두 사람을 붙여 놨다.
216|
217|‘워낙 사이가 좋지 않아 걱정이 많았었는데…….’
218|
219|오늘 와 보니 괜한 걱정을 했다. 방법이 거칠긴 하지만 그건 분명 일방적인 구타가 아니라 단련이었다. 성장은 빠르지만 아직 미숙한 진태경을 더욱 단단하고 날카롭게 만들어 줄 단련.
220|
221|비록 몸은 고달프겠지만 말이다.
222|
223|‘다 널 위해서다.’
224|
225|쓰러진 막내를 하염없이 다정한 시선으로 바라보던 진위경이 입을 열었다.
226|
227|“이만 가마.”
228|
229|하지만 그걸 그냥 보고만 있을 진무경이 아니었다.
230|
231|“혼자 가긴 어딜 갑니까? 저 녀석도 데려가십시오. 같이 못 살겠습니다.”
232|
233|“열흘이다. 고작 그 정도도 못 참겠느냐?”
234|
235|“오늘은 형님을 봐서 이 정도로 끝낸 겁니다. 정 그러면 내일은 장의사 부르시든가요.”
236|
237|“진심이냐?”
238|
239|“예. 그러니 당장 데려가는 게 저 녀석한테도 좋을 겁니다.”
240|
241|“네 뜻이 정 그렇다면…….”
242|
243|고개를 끄덕인 진위경이 말을 이었다.
244|
245|“그렇게 하거라.”
246|
247|“예, 예?”
248|
249|“원하는 대로 하라고.”
250|
251|한마디를 툭 던진 진위경이 뒤돌아 걷기 시작했다.
252|
253|진무경이 어떤 표정을 짓고 있을지 상상하니 피식 실소가 새어 나왔다.
254|
255|‘네게도 좋은 경험이 될 게다.’
256|
257|이 불편한 동거는 비단 막내만을 위한 것이 아니다.
258|
259|천재는 언제나 외로운 법. 두 천재가 서로에게 큰 자극이 될 것임을, 그는 믿어 의심치 않았다.
260|
261|“일어나, 이 새끼야!”
262|
263|빡!
264|
265|“…….”
266|
267|진위경은 돌아가는 길 내내 뒤돌아보고 싶은 충동을 억눌러야 했다.
268|
269|
270|
271|* * *
272|
273|
274|
275|“일어났냐?”
276|
277|“…….”
278|
279|“일어난 거 다 안다. 대답해라.”
280|
281|“…….”
282|
283|“마지막 기회 준다. 셋 셀 동안 안 일어나면 연무장이 네 무덤이 될 줄 알아라.”
284|
285|“…….”
286|
287|“하나, 둘.”
288|
289|개새끼. 숫자 한번 더럽게 빨리 센다.
290|
291|나는 슬그머니 일어나 기지개를 켰다.
292|
293|“어우, 잘 잤다.”
294|
295|슬쩍 고개를 돌리니 고리눈을 뜬 진무경이 보였다.
296|
297|저 얼굴을 보니까 어제의 기억이 새록새록 되살아난다. 피도 눈물도 없는 놈. 쳐 죽일 놈.
298|
299|나는 천연덕스러운 목소리로 말을 걸었다.
300|
301|“어? 형님. 언제 오셨어요?”
302|
303|“……방금.”
304|
305|아쉬운 얼굴로 입맛을 다시는 진무경을 보니 존댓말을 쓴 게 신의 한 수라는 생각이 들었다. 뭐 하나 트집 잡히기라도 하면 복날 개 잡듯이 두들겨 팰 놈이니까.
306|
307|‘시바…… 약한 게 죄다. 죄.’
308|
309|나도 오기가 있는 놈이다. 하지만 맨주먹으로 하는 싸움에서는 죽었다 깨어나도 진무경을 당할 수 없었다.
310|
311|저놈이 체계적인 권법, 각법을 익힐 때 나는 UFC 경기를 봤다. 애초에 오기로 어떻게 해볼 수 있는 상대가 아니다.
312|
313|그래서 마지막으로 선택한 게 로그아웃이었다.
314|
315|물론 보기 좋게 실패했지만.
316|
317|‘전투 시에는 로그아웃이 불가능하다니. 그딴 게 어디 있어.’
318|
319|미리 말이나 해 주든가. 그것도 모르고 덤볐다가 인생에서 로그아웃 당할 뻔했다. 나는 힐끔 진무경을 곁눈질했다.
320|
321|“야.”
322|
323|“예?”
324|
325|“너 왜 눈을 그렇게 떠?”
326|
327|“제가요?”
328|
329|싸늘한 목소리에 최대한 눈을 초롱초롱하게 떴다. 이제는 눈도 착하게 떠야 한 대라도 덜 맞는다.
330|
331|“너…… 후. 조심해라.”
332|
333|“네, 형님.”
334|
335|갑자기 공손해진 내 태도에 진무경은 기분 나쁘다는 듯한 표정을 지었다. 하지만 예의 바르다고 때릴 수도 없는 노릇이겠지.
336|
337|“어제 일 말인데…….”
338|
339|잽싸게 고개를 숙였다.
340|
341|“제 잘못입니다. 수련 중이신데 큰 소리를 내다니. 맞아도 싸죠.”
342|
343|“아니, 야.”
344|
345|“어떡해, 어제 저 때리시느라 손 아프셨겠다. 제가 호 불어 드릴까요?”
346|
347|“이거 완전히 미친놈이네.”
348|
349|진무경은 나를 때릴까 말까 고민하는 눈치였지만 결국 포기하고 주먹을 내려놨다.
350|
351|“됐다. 따라 나와.”
352|
353|“……어디로요?”
354|
355|“연무장.”
356|
357|앞에 했던 말 정정. 연무장에서 때릴 모양이다. 그래, 또 내 방을 초토화시킬 순 없을 테니까.
358|
359|바짝 굳은 내 표정을 본 진무경이 혀를 찼다.
360|
361|“그런 거 아니니까 따라와. 오늘부터 수련이다.”
362|
363|“수련이요?”
364|
365|“그래. 네 녀석의 끔찍한 무공을 처음부터 뜯어고쳐 주마.”
366|
367|볼 때마다 두들겨 패던 인간이 갑자기 수련을 도와준다고? 그것도 자기 시간까지 쪼개 가면서?
368|
369|‘차라리 마왕 아스모데우스가 회개했다는 말을 믿지.’
370|
371|의심 가득한 눈초리를 스스로도 느꼈는지 진무경이 깊은 한숨을 내쉬었다.
372|
373|“어제 형님께서 다녀가셨다.”
374|
375|“아.”
376|
377|성격은 지랄맞아도 위아래가 확실한 놈이다. 진위경이 직접 부탁했다면 지금 상황이 이해된다.
378|
379|“비어 있는 건물이 몇 채인데 너를 왜 내게 보냈겠느냐? 젠장. 아예 처음부터 거절했어야 했는데.”
380|
381|……어지간히 가르쳐 주기 싫은 모양이군.
382|
383|하지만 나로서는 그의 도움이 꼭 필요하다. 하다못해 괜찮은 권각술 하나라도 전수받는다면 분명히 써먹을 데가 있을 테니까.
384|
385|“부탁드립니다.”
386|
387|진무경이 고개를 저었다.
388|
389|“생각하고 말해. 내 기준에 맞추려면 벅찰 테니까. 힘들다고 포기할 바에야 지금 깨끗하게 접어라.”
390|
391|힘들 때마다 포기했다면, 여기까지 오지도 못했다.
392|
393|“강해지고 싶습니다.”
394|
395|목소리에 담긴 진심을 읽은 걸까? 한동안 물끄러미 나를 응시하던 그가 결국 입을 열었다.
396|
397|“연무장으로 나와라.”
398|
399|띠링.
400|
401|
402|
403|- 퀘스트가 생성되었습니다.
404|
405|
406|
407|퀘스트
408|
409|
410|
411|[시련? 수련?]
412|
413|정해진 기간 동안 진무경의 지도를 받으며 수련하십시오. 당신이 얼마나 강해지건, 진무경이 만족하지 않는다면 퀘스트는 실패합니다!
414|
415|
416|
417|등급 : 절정
418|
419|제한 : 진태경
420|
421|임무 : 진무경의 인정 (미완료)
422|
423|보상 : ???
424|
425|실패 : ???
426|
427|남은 시간 : 9일 23시간 51분 10초
428|
429|
430|
431|
432|
433|‘진무경의 인정이라.’
434|
435|추상적인 임무지만 충분히 자신 있다. 시스템의 사기성과 내 노력이 합쳐진다면 진무경의 눈이 튀어나올 만큼 빠르게 성장할 수 있을 테니까.
436|
437|‘할 수 있어.’
438|
439|내가 결의를 다지던 그 순간이었다.
440|
441|“참. 너 창 쓰지?”
442|
443|“아, 네.”
444|
445|“그것도 챙겨서 나와.”
446|
447|진무경은 검사다. 그러니 당연히 권법 위주로 가르쳐 줄 거라 생각했는데. 어리둥절한 일이라 일단 조심스럽게 물어봤다.
448|
449|“갑자기 창은 왜……?”
450|
451|“수련도 실전처럼. 그런 말 못 들어 봤어?”
452|
453|진무경이 환하게 웃으며 덧붙였다.
454|
455|“형님한테도 허락 맡아 뒀다. 장의사 불러도 상관없대.”
456|
457|경쾌한 발걸음으로 사라지는 그의 뒷모습을 멍하니 쳐다보던 나는 간신히 입을 열었다.
458|
459|“……로그아웃.”
460|
461|삑.
462|
463|
464|
465|- 해당 퀘스트 중에는 로그아웃이 제한됩니다.
466|
467|
468|
469|이런 시발.
```

## Assembled English

```markdown
[P1]
# Chapter 69

[P2]
In the dead of night, while everyone else slept, Jin Wikyung awoke with a scream.

[P3]
“Graaah!”

[P4]
He flailed both arms wildly, then soon realized that he had returned to reality.

[P5]
The flickering lamplight and the documents covering his desk. The familiar sight of his study.

[P6]
“Phew.”

[P7]
After letting out a sigh of relief, Jin Wikyung rubbed the back of his neck. It was damp with cold sweat, probably because of the nightmare.

[P8]
*I thought I was going to die.*

[P9]
He had dreamed that the earth split apart and the sky came crashing down. He had fled from a deafening roar that shook heaven and earth, running until he could barely breathe. The last thing he remembered was falling.

[P10]
*Maybe I’ve been pushing myself too hard.*

[P11]
There was more work than he could handle, but nowhere near enough people to do it. Each nerve-racking day bled into the next, and the fatigue kept piling up.

[P12]
“Ugh. I need to hire more people soon. At this rate, I’ll die before my time.”

[P13]
The world was vast, and there were plenty of talented people in it. And yet the Jin Family of Taiyuan still did not have a single decent strategist. That was because the family’s capabilities were lacking.

[P14]
Why would anyone talented choose the Jin Family of Taiyuan in Shanxi over the great sects or renowned great families of the Central Plains, all of which would welcome them with open arms?

[P15]
From their perspective, it was an obvious choice.

[P16]
*Until now, that is.*

[P17]
Everything was about to change. If the Jin Family united Shanxi Murim on New Year’s Day and continued expanding its influence…

[P18]
Before long, talented people from across the land would come flocking beneath the Jin Family of Taiyuan’s banner.

[P19]
*Although I’ll probably die of overwork before then.*

[P20]
Jin Wikyung let out a deep sigh as he stared at the murderous mountain of paperwork.

[P21]
That was when it happened.

[P22]
Rumble.

[P23]
The sound was extremely faint—so faint that only a Peak master like Jin Wikyung could have noticed it.

[P24]
*What was that?*

[P25]
He sharpened his senses. When he focused his internal energy on his ears, the sound became clearer.

[P26]
Rumble. Clang.

[P27]
Small, but unmistakable.

[P28]
The sound of steel striking steel.

[P29]
Someone was fighting. At this hour of the night, no less.

[P30]
That was not the only reason Jin Wikyung’s face hardened.

[P31]
*That direction is…*

[P32]
Jin Mukyung’s residence lay in that direction. And as of yesterday, one more person lived there.

[P33]
*Surely Mukyung isn’t beating up the youngest… No, of course not.*

[P34]
He had repeatedly urged them to get along. Surely they would not start trading blows already.

[P35]
He had faith in his beloved younger brothers.

[P36]
Clang. Clang!

[P37]
“…”

[P38]
Jin Wikyung quietly rose from his seat.

[P39]
* * *

[P40]
Once he fully unleashed his movement technique, Jin Wikyung reached Jin Mukyung’s residence in no time.

[P41]
The problem was that the closer he got, the more ominous the sounds became.

[P42]
*…He’s probably training alone in the training ground, right?*

[P43]
Jin Wikyung hesitated, unsure whether to enter the pavilion. After a moment, he cautiously poked his head over the wall.

[P44]
And witnessed a shocking sight.

[P45]
“I told you. Rule number two. Huh?”

[P46]
Boom! Crash!

[P47]
Jin Mukyung swung his scabbard without pause. One person fled desperately, trying to escape him.

[P48]
“Lo-Logout!”

[P49]
Before Jin Taekyung could even finish his desperate cry, the scabbard flew toward him. It missed him by a hair and shattered the bluestone floor of the training ground.

[P50]
Bang!

[P51]
“I told you, you bastard—qi deviation! Conception and Governor Vessels!”

[P52]
“Logouuuut!”

[P53]
“…”

[P54]
What was “Loguawk,” and why were qi deviation and the Conception and Governor Vessels suddenly coming up?

[P55]
The flow of the conversation made absolutely no sense, but one thing was certain.

[P56]
*Something bad is going to happen if this keeps up.*

[P57]
At this rate, they might really have to call either a physician or an undertaker.

[P58]
*I’ll protect the youngest!*

[P59]
Jin Wikyung was about to charge in, his face set with determination, when—

[P60]
“Why is your side open again? Are you that desperate to get hit?”

[P61]
Whack!

[P62]
“Guh!”

[P63]
Jin Taekyung staggered after taking a blow to the ribs. Jin Mukyung did not miss the opening. He closed in and swung his scabbard again.

[P64]
Thwack-thwack-thwack!

[P65]
“Argh! Argh! Argh!”

[P66]
“Don’t shrink back just because you got hit. Especially your lower body!”

[P67]
Thwack!

[P68]
“Grrr!”

[P69]
“Oh, look at you.”

[P70]
Jin Mukyung smiled disdainfully at the sight of his younger brother charging at him with his teeth clenched.

[P71]
“You don’t even have the fundamentals down. First, fix that habit of throwing out your hands and feet on instinct. People learn martial arts, not beasts.”

[P72]
“Shut up!”

[P73]
“You have a terrible memory, too. Sleep well. When you wake up, I’ll explain the rules again.”

[P74]
Whoosh! Thud.

[P75]
Jin Taekyung took a direct hit to the chin, and his body crumpled. Jin Mukyung silently looked down at him lying spread-eagled on the floor, then slowly spoke.

[P76]
“Please come out.”

[P77]
There was no question who he was speaking to. Jin Wikyung emerged from behind the wall with an awkward expression.

[P78]
“You knew I was here?”

[P79]
“It would be strange if I didn’t. Every time that kid got hit, I could hear you swallowing from here like thunder.”

[P80]
Jin Wikyung examined the fallen Jin Taekyung with worried eyes.

[P81]
“His injuries aren’t too severe. That’s a relief.”

[P82]
“It’s not like he’s going to die.”

[P83]
“Mukyung!”

[P84]
“Don’t worry. His bones and sinews are unbelievably sturdy.”

[P85]
“Really?”

[P86]
“He lasted four hours while taking a beating like that. With that kind of stamina and grit, he’ll soon… Why are you laughing?”

[P87]
Jin Wikyung gazed at his younger brother’s face with a strange smile and answered cheerfully.

[P88]
“It’s fascinating. Isn’t this the first time you’ve ever praised the youngest?”

[P89]
Jin Mukyung stiffened.

[P90]
*Praise? I praised that bastard?*

[P91]
Impossible. His younger brother did not have a single redeeming quality. He had spent his days drowning in alcohol and chasing women, without a care for what happened to the family. And Jin Mukyung had praised him?

[P92]
He forced himself to shake his head.

[P93]
“…I did no such thing.”

[P94]
“I see.”

[P95]
“I really haven’t.”

[P96]
“All right. Who said otherwise?”

[P97]
“No, you’re still laughing!”

[P98]
“I have never done that.”

[P99]
“Hyung!”

[P100]
Jin Wikyung struggled to suppress the laughter bubbling up inside him. It pained him to see his beloved youngest brother hurt, but this was something Taekyung would have to experience sooner or later.

[P101]
*I can’t keep him under my wing forever.*

[P102]
The Sleeping Dragon of Shanxi.

[P103]
Another genius produced by the Jin Family of Taiyuan.

[P104]
As he looked at his younger brother, who had grown so much in such a short time, Jin Wikyung felt both joy and unease.

[P105]
No. Perhaps it was fear.

[P106]
*Is this even possible?*

[P107]
It was far too fast. Even to someone who had watched the genius Jin Mukyung from closer than anyone else, Jin Taekyung’s rate of growth was beyond comprehension.

[P108]
*I can’t even begin to gauge it.*

[P109]
As a child, Jin Wikyung had been a promising talent, but he had never been a genius. How could an ordinary man like him understand a genius, let alone teach one?

[P110]
Just as his worries were deepening, Jin Mukyung had returned.

[P111]
Jin Wikyung had known at once that this was the moment, and put the two of them together.

[P112]
*I was so worried because they got along so poorly…*

[P113]
But now that he had seen them together, he knew those worries had been unnecessary. Jin Mukyung’s methods were rough, but this was clearly training, not a one-sided beating.

[P114]
Training that would make the fast-growing but still inexperienced Jin Taekyung tougher and sharper.

[P115]
His body would suffer, though.

[P116]
*It’s all for your sake.*

[P117]
Jin Wikyung gazed down at the fallen youngest with boundless tenderness and spoke.

[P118]
“I’ll be going now.”

[P119]
But Jin Mukyung was not about to let him leave like that.

[P120]
“Where do you think you’re going alone? Take that kid with you. I can’t live with him.”

[P121]
“It’s ten days. Can’t you endure even that much?”

[P122]
“I stopped at this much today out of respect for you. If you insist, call an undertaker tomorrow.”

[P123]
“Are you serious?”

[P124]
“Yes. So taking him with you right now would be better for him, too.”

[P125]
“If that is truly what you want…”

[P126]
Jin Wikyung nodded and continued.

[P127]
“Then do so.”

[P128]
“Yes, yes?”

[P129]
“Do as you wish.”

[P130]
After tossing out that one sentence, Jin Wikyung turned and began walking away.

[P131]
Imagining what expression Jin Mukyung must be wearing, he let out a quiet laugh.

[P132]
*This will be a good experience for you, too.*

[P133]
This uncomfortable arrangement was not solely for the youngest’s sake.

[P134]
Geniuses were always lonely. Jin Wikyung had no doubt that the two geniuses would greatly spur each other on.

[P135]
“Get up, you bastard!”

[P136]
Whack!

[P137]
“…”

[P138]
Jin Wikyung had to suppress the urge to look back the entire way home.

[P139]
* * *

[P140]
“You awake?”

[P141]
“…”

[P142]
“I know you’re awake. Answer me.”

[P143]
“…”

[P144]
“I’ll give you one last chance. If you’re not up by the time I count to three, this training ground will be your grave.”

[P145]
“…”

[P146]
“One, two.”

[P147]
*Bastard. He counts ridiculously fast.*

[P148]
I quietly got up and stretched.

[P149]
“Whew, I slept well.”

[P150]
When I casually turned my head, I found Jin Mukyung glaring at me.

[P151]
The sight of his face brought yesterday’s memories flooding back.

[P152]
A man without blood or tears. A bastard who deserved to be beaten to death.

[P153]
I addressed him in an innocent voice.

[P154]
“Oh? Hyung-nim. When did you get here?”

[P155]
“…Just now.”

[P156]
Seeing Jin Mukyung smack his lips with disappointment, I decided that switching to formal speech had been a stroke of genius. If he found even one thing to nitpick, he was the type to beat me like a dog.

[P157]
*Fuck… Being weak is a sin. A sin.*

[P158]
I had my pride, too. But in an unarmed fight, I could not beat Jin Mukyung even if I died and came back to life.

[P159]
While that bastard had been learning systematic fist and kicking techniques, I had been watching UFC matches. He was not someone I could overcome through sheer stubbornness.

[P160]
That was why I had chosen Logout as my last resort.

[P161]
Of course, it had failed spectacularly.

[P162]
*You can’t Logout during combat? What kind of bullshit rule is that?*

[P163]
They could have told me beforehand. I had charged in without knowing and nearly gotten logged out of life.

[P164]
I cast a sidelong glance at Jin Mukyung.

[P165]
“Hey.”

[P166]
“Yes?”

[P167]
“Why are you looking at me like that?”

[P168]
“Me?”

[P169]
At his icy tone, I made my eyes as bright and innocent as possible.

[P170]
Now I even had to watch how I looked at him if I wanted one less beating.

[P171]
“You… Hah. Watch yourself.”

[P172]
“Yes, Hyung-nim.”

[P173]
Jin Mukyung looked displeased by my sudden politeness. But he could hardly hit me just for having good manners.

[P174]
“About yesterday…”

[P175]
I quickly bowed my head.

[P176]
“It was my fault. I made so much noise while you were training. I deserved to get hit.”

[P177]
“No, hey.”

[P178]
“Oh, no. Your hand must hurt from hitting me yesterday. Would you like me to blow on it?”

[P179]
“You’re completely insane.”

[P180]
Jin Mukyung looked as though he was debating whether to hit me, but eventually gave up and lowered his fist.

[P181]
“Enough. Follow me.”

[P182]
“…Where?”

[P183]
“The training ground.”

[P184]
I took back what I had just thought. He planned to beat me in the training ground.

[P185]
He could not exactly turn my room into a wasteland again.

[P186]
Jin Mukyung clicked his tongue when he saw my expression stiffen.

[P187]
“It’s not that. Follow me. Training starts today.”

[P188]
“Training?”

[P189]
“Yes. I’m going to tear apart those horrible martial arts of yours and rebuild them from the ground up.”

[P190]
The man who had beaten me senseless every time he saw me was suddenly offering to help me train? And he was even carving out time from his own schedule?

[P191]
*I’d sooner believe the Demon King Asmodeus had repented.*

[P192]
Perhaps he noticed the suspicion in my eyes, because Jin Mukyung let out a deep sigh.

[P193]
“Hyung came by yesterday.”

[P194]
“Ah.”

[P195]
His personality might have been foul, but he had a clear sense of rank and propriety. If Jin Wikyung had personally asked him, the current situation made sense.

[P196]
“There are several empty buildings. Why do you think he sent you to me? Damn it. I should have refused from the beginning.”

[P197]
…I suppose he really did not want to teach me.

[P198]
But I desperately needed his help. If nothing else, there had to be some use for learning even one decent fist-and-kicking technique from him.

[P199]
“Please teach me.”

[P200]
Jin Mukyung shook his head.

[P201]
“Think before you speak. Meeting my standards will be difficult. If you’re going to give up as soon as things become hard, quit now.”

[P202]
If I had given up every time things became difficult, I would never have made it this far.

[P203]
“I want to become stronger.”

[P204]
Perhaps he sensed the sincerity in my voice. After staring at me for a long time, he finally opened his mouth.

[P205]
“Come out to the training ground.”

[P206]
Ding.

[P207]
> **System**
>
> A Quest has been created.
>
> **Quest**
>
> **Trial? Training?**
>
> Train under Jin Mukyung’s guidance for the designated period. No matter how strong you become, the Quest will fail if Jin Mukyung is not satisfied!
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Jin Mukyung’s recognition (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???
>
> **Time Remaining:** 9 days 23 hours 51 minutes 10 seconds

[P208]
*Jin Mukyung’s recognition.*

[P209]
It was an abstract mission, but I was confident enough. If I combined the System’s cheat-like advantages with my own effort, I could grow so quickly that Jin Mukyung’s eyes would pop out.

[P210]
*I can do this.*

[P211]
That was when I was steeling my resolve.

[P212]
“Oh, right. You use a spear, don’t you?”

[P213]
“Ah, yes.”

[P214]
“Bring that with you, too.”

[P215]
Jin Mukyung was a swordsman, so I had naturally assumed he would focus on teaching me fist techniques. Confused, I cautiously asked,

[P216]
“Why the spear all of a sudden…?”

[P217]
“Train as if it were real combat. Haven’t you heard that saying?”

[P218]
Jin Mukyung smiled brightly and added:

[P219]
“I even got Hyung’s permission. He said he doesn’t mind if we have to call an undertaker.”

[P220]
I stared blankly at his back as he walked away with light, cheerful steps. At last, I managed to open my mouth.

[P221]
“…Logout.”

[P222]
Beep.

[P223]
> **System**
>
> Logout is restricted during this Quest.

[P224]
*What the fuck.*
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
# Chapter 69

[P2]
In the dead of night, while everyone else slept, Jin Wikyung awoke with a scream.

[P3]
“Graaah!”

[P4]
He flailed both arms with startling force, then soon realized that he had returned to reality.

[P5]
The flickering lamplight and the documents covering his desk. The familiar sight of his study.

[P6]
“Phew.”

[P7]
After letting out a sigh of relief, Jin Wikyung rubbed the back of his neck. It was damp with cold sweat, probably because of the nightmare.

[P8]
*I thought I was going to die.*

[P9]
It had been a dream in which the earth split apart and the sky collapsed. He had run from a deafening roar that shook heaven and earth until he was gasping for breath, and his last memory was of falling.

[P10]
*Maybe I’ve been pushing myself too hard.*

[P11]
There was more work than he could handle, but nowhere near enough people to do it. Each day was a nerve-racking struggle, and the fatigue kept piling up.

[P12]
“Ugh. I need to hire more people soon. At this rate, I’ll die before my time.”

[P13]
The world was vast, and there were plenty of talented people in it. And yet the Jin Family of Taiyuan still did not have a single decent strategist. That was because the family’s capabilities were lacking.

[P14]
Why would any talented person choose to join the Jin Family of Taiyuan in Shanxi when they could go to one of the great sects or renowned clans of the Central Plains, where people would welcome them with open arms?

[P15]
From their perspective, it was an obvious choice.

[P16]
*Until now, that is.*

[P17]
Everything was about to change. If the Jin Family united Shanxi Murim on New Year’s Day and continued expanding its influence…

[P18]
Before long, talented people from across the land would come flocking beneath the Jin Family of Taiyuan’s banner.

[P19]
*Although I’ll probably die of overwork before then.*

[P20]
Jin Wikyung let out a deep sigh as he stared at the terrifying mountain of paperwork.

[P21]
That was when it happened.

[P22]
Rumble.

[P23]
It was an extremely faint sound, so quiet that only a Peak master like Jin Wikyung could have noticed it.

[P24]
*What was that?*

[P25]
He sharpened his senses. When he focused his internal energy on his ears, the sound became clearer.

[P26]
Rumble. Clang.

[P27]
Small, but unmistakable.

[P28]
The sound of steel striking steel.

[P29]
Someone was fighting. At this hour of the night, no less.

[P30]
That was not the only reason Jin Wikyung’s face hardened.

[P31]
*That direction is…*

[P32]
It was where Jin Mukyung’s residence was located. And, as of yesterday, there was one more person living there.

[P33]
*Surely Mukyung isn’t beating up the youngest… No, of course not.*

[P34]
He had repeatedly urged them to get along. Surely they would not already be beating each other senseless.

[P35]
He trusted his beloved younger brothers.

[P36]
Clang. Clang!

[P37]
“…”

[P38]
Jin Wikyung quietly rose from his seat.

[P39]
* * *

[P40]
Once he fully unleashed his movement technique, Jin Wikyung reached Jin Mukyung’s residence in no time.

[P41]
The problem was that the closer he got, the more ominous the sounds became.

[P42]
*…He’s probably training alone in the training hall, right?*

[P43]
Jin Wikyung hesitated over whether he should enter the pavilion. In the end, he cautiously poked his head over the wall.

[P44]
And witnessed a shocking sight.

[P45]
“I told you. Rule number two. Huh?”

[P46]
Boom! Crash!

[P47]
Jin Mukyung swung his scabbard without pause. One person fled desperately, trying to escape him.

[P48]
“Lo, Logout!”

[P49]
Before Jin Taekyung could even finish his desperate cry, the scabbard flew toward him. It narrowly missed him and smashed into the bluestone floor of the training hall.

[P50]
Bang!

[P51]
“I told you, you bastard—qi deviation! Ren and Du meridians!”

[P52]
“Logouuuut!”

[P53]
“…”

[P54]
What was “Loguawk,” and why were qi deviation and the Ren and Du meridians suddenly coming up?

[P55]
The flow of the conversation made absolutely no sense, but one thing was certain.

[P56]
*Something bad is going to happen if this keeps up.*

[P57]
At this rate, they might really need to call either a physician or an undertaker.

[P58]
*I’ll protect the youngest!*

[P59]
Jin Wikyung was just about to charge in with determination on his face when—

[P60]
“Why is your side open again? Are you that desperate to get hit?”

[P61]
Whack!

[P62]
“Guh!”

[P63]
Jin Taekyung staggered after taking a blow to the ribs. Jin Mukyung did not miss the opportunity and followed up with another swing of his scabbard.

[P64]
Thwack-thwack-thwack!

[P65]
“Argh! Argh! Argh!”

[P66]
“Don’t shrink back just because you got hit. Especially with your lower body!”

[P67]
Thwack!

[P68]
“Grrr!”

[P69]
“Oh, look at you.”

[P70]
Jin Mukyung smiled disdainfully at the sight of his younger brother charging at him with his teeth clenched.

[P71]
“You’re an idiot who doesn’t even have the basics down. Fix that habit of throwing out your hands and feet on instinct first. Martial arts are learned by people, not beasts.”

[P72]
“Shut up!”

[P73]
“You have a terrible memory, too. Sleep well. When you wake up, I’ll explain the rules again.”

[P74]
Whoosh! Thud.

[P75]
Jin Taekyung took a direct hit to the chin, and his body crumpled. Jin Mukyung silently looked down at him lying spread-eagled on the floor, then slowly spoke.

[P76]
“Please come out.”

[P77]
There was no question who he was speaking to. Jin Wikyung emerged from behind the wall with an awkward expression.

[P78]
“You knew I was here?”

[P79]
“It would be strange if I didn’t. Every time that kid got hit, I could hear you swallowing from here like thunder.”

[P80]
Jin Wikyung examined Jin Taekyung’s fallen body with worried eyes.

[P81]
“The injuries aren’t too severe. That’s a relief.”

[P82]
“It’s not like he’s going to die.”

[P83]
“Mukyung!”

[P84]
“Don’t worry. His bones and sinews are unbelievably sturdy.”

[P85]
“Really?”

[P86]
“He lasted four hours while taking a beating like that. With that kind of stamina and grit, he’ll soon… Why are you laughing?”

[P87]
Jin Wikyung gazed at his younger brother’s face with a strange smile and answered cheerfully.

[P88]
“It’s fascinating. Isn’t this the first time you’ve ever praised the youngest?”

[P89]
Jin Mukyung stiffened.

[P90]
*Praise? I praised that bastard?*

[P91]
It was impossible. Wasn’t he a younger brother without a single redeeming quality? Jin Mukyung had praised the man who had spent his days drowning in alcohol and chasing women, heedless of what happened to the family?

[P92]
Jin Mukyung forced himself to shake his head.

[P93]
“…I have never done such a thing.”

[P94]
“I see.”

[P95]
“I really haven’t.”

[P96]
“All right. Who said otherwise?”

[P97]
“No, you’re still laughing!”

[P98]
“I have never done that.”

[P99]
“Hyung!”

[P100]
Jin Wikyung tried to suppress the laughter welling up inside him. It pained him to see his beloved youngest brother hurt, but this was something he would have to experience someday.

[P101]
*I can’t keep him under my wing forever.*

[P102]
Sleeping Dragon of Shanxi.

[P103]
Another genius produced by the Jin Family of Taiyuan.

[P104]
Jin Wikyung felt both joy and unease as he looked at his younger brother, who had grown so much in such a short time.

[P105]
No. Perhaps it was fear.

[P106]
*Is this even possible?*

[P107]
It was far too fast. Even to someone who had watched the genius Jin Mukyung from closer than anyone else, Jin Taekyung’s rate of growth was beyond comprehension.

[P108]
*I can’t even begin to gauge it.*

[P109]
As a child, Jin Wikyung had been a promising talent, but he had never been a genius. How could an ordinary man like him understand a genius, let alone teach one?

[P110]
His thoughts were growing deeper when Jin Mukyung returned.

[P111]
Jin Wikyung had known at once that this was the moment, and put the two of them together.

[P112]
*I was so worried because they got along so poorly…*

[P113]
Now that he had seen them together, those worries had been pointless. The method was rough, but this was clearly not one-sided beating. It was training.

[P114]
Training that would make the fast-growing but still inexperienced Jin Taekyung stronger and sharper.

[P115]
His body would suffer, though.

[P116]
*It’s all for your sake.*

[P117]
Jin Wikyung looked down at the fallen youngest with boundless tenderness and spoke.

[P118]
“I’ll be going now.”

[P119]
But Jin Mukyung was not about to let him leave like that.

[P120]
“Where are you going alone? Take that kid with you. I can’t live with him.”

[P121]
“It’s ten days. Can’t you endure that much?”

[P122]
“I stopped at this much today out of respect for you. If you insist, call an undertaker tomorrow.”

[P123]
“Are you serious?”

[P124]
“Yes. So taking him with you right now would be better for him, too.”

[P125]
“If that is truly what you want…”

[P126]
Jin Wikyung nodded and continued.

[P127]
“Then do so.”

[P128]
“Yes, yes?”

[P129]
“Do as you wish.”

[P130]
After tossing out that one sentence, Jin Wikyung turned and began walking away.

[P131]
Imagining what expression Jin Mukyung must be wearing, he let out a quiet laugh.

[P132]
*This will be good experience for you, too.*

[P133]
This uncomfortable arrangement was not only for the youngest.

[P134]
Geniuses were always lonely. Jin Wikyung had no doubt that the two geniuses would greatly spur each other on.

[P135]
“Get up, you bastard!”

[P136]
Whack!

[P137]
“…”

[P138]
Jin Wikyung had to suppress the urge to look back the entire way home.

[P139]
* * *

[P140]
“Are you awake?”

[P141]
“…”

[P142]
“I know you’re awake. Answer me.”

[P143]
“…”

[P144]
“I’ll give you one last chance. If you’re not up by the time I count to three, this training hall will be your grave.”

[P145]
“…”

[P146]
“One, two.”

[P147]
*Bastard. He counts ridiculously fast.*

[P148]
I quietly got up and stretched.

[P149]
“Whew, I slept well.”

[P150]
I casually turned my head and found Jin Mukyung glaring at me.

[P151]
The moment I saw that face, yesterday’s memories came flooding back.

[P152]
A man without blood or tears. A bastard who deserved to be beaten to death.

[P153]
I addressed him in a nonchalant voice.

[P154]
“Oh? Hyung-nim. When did you get here?”

[P155]
“…Just now.”

[P156]
Seeing Jin Mukyung smack his lips with disappointment, I decided that switching to formal speech had been a stroke of genius. If he found even one thing to nitpick, he was the type to beat me like a dog.

[P157]
*Fuck… Being weak is a sin. A sin.*

[P158]
I had my pride, too. But in an unarmed fight, I could not beat Jin Mukyung even if I died and came back to life.

[P159]
While that bastard had been learning systematic fist and kicking techniques, I had been watching UFC matches. He was not someone I could overcome through sheer stubbornness.

[P160]
That was why I had chosen Logout as a last resort.

[P161]
Of course, it had failed spectacularly.

[P162]
*You can’t Logout during combat? What kind of ridiculous rule is that?*

[P163]
They could have told me beforehand. I had charged in without knowing and nearly logged out of life.

[P164]
I cast a sidelong glance at Jin Mukyung.

[P165]
“Hey.”

[P166]
“Yes?”

[P167]
“Why are you looking at me like that?”

[P168]
“Me?”

[P169]
At his icy tone, I made my eyes look as bright and innocent as possible.

[P170]
Now I even had to watch how I looked at him if I wanted one less beating.

[P171]
“You… Hah. Be careful.”

[P172]
“Yes, Hyung-nim.”

[P173]
Jin Mukyung looked displeased by my sudden politeness. But he could hardly hit me just for having good manners.

[P174]
“About yesterday…”

[P175]
I quickly bowed my head.

[P176]
“It was my fault. I was making so much noise while you were training. I deserved to get hit.”

[P177]
“No, hey.”

[P178]
“Oh, no. Your hand must hurt from hitting me yesterday. Would you like me to blow on it?”

[P179]
“You’re completely insane.”

[P180]
Jin Mukyung looked as though he was debating whether to hit me, but eventually gave up and lowered his fist.

[P181]
“Enough. Follow me.”

[P182]
“…Where?”

[P183]
“The training hall.”

[P184]
Retract what I said earlier. He planned to beat me in the training hall.

[P185]
There was no way he could turn my room into a wasteland again, after all.

[P186]
Seeing my expression stiffen, Jin Mukyung clicked his tongue.

[P187]
“It’s not that. Follow me. Training starts today.”

[P188]
“Training?”

[P189]
“Yes. I’ll tear apart your horrible martial arts and rebuild them from the beginning.”

[P190]
The man who had beaten me senseless every time he saw me was suddenly offering to help me train? And he was even carving out time from his own schedule?

[P191]
*I’d sooner believe that the Demon King Asmodeus had repented.*

[P192]
Perhaps he noticed the suspicion in my eyes, because Jin Mukyung let out a deep sigh.

[P193]
“Hyung came by yesterday.”

[P194]
“Ah.”

[P195]
His personality might have been foul, but he had a clear sense of rank and propriety. If Jin Wikyung had personally asked him, the current situation made sense.

[P196]
“There are several empty buildings. Why do you think he sent you to me? Damn it. I should have refused from the beginning.”

[P197]
…I suppose he really did not want to teach me.

[P198]
But I desperately needed his help. If nothing else, there had to be some use for learning even one decent fist-and-kicking technique from him.

[P199]
“Please teach me.”

[P200]
Jin Mukyung shook his head.

[P201]
“Think before you speak. Meeting my standards will be difficult. If you’re going to give up as soon as things become hard, quit now.”

[P202]
If I had given up every time things became difficult, I would never have made it this far.

[P203]
“I want to become stronger.”

[P204]
Perhaps he sensed the sincerity in my voice. After staring at me for a long time, he finally opened his mouth.

[P205]
“Come out to the training hall.”

[P206]
Ding.

[P207]
> **System**
>
> **Quest**
>
> **Trial? Training?**
>
> Train under Jin Mukyung’s guidance for the designated period. No matter how strong you become, the Quest will fail if Jin Mukyung is not satisfied!
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Jin Mukyung’s recognition (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???
>
> **Time Remaining:** 9 days 23 hours 51 minutes 10 seconds

[P208]
*Jin Mukyung’s recognition.*

[P209]
It was an abstract mission, but I was confident enough. If I combined the System’s cheat-like advantages with my own effort, I could grow so quickly that Jin Mukyung’s eyes would pop out.

[P210]
*I can do this.*

[P211]
That was when I was steeling my resolve.

[P212]
“Oh, right. You use a spear, don’t you?”

[P213]
“Ah, yes.”

[P214]
“Bring that with you, too.”

[P215]
Jin Mukyung was a swordsman. Naturally, I had assumed he would primarily teach me fist techniques. Puzzled, I cautiously asked:

[P216]
“Why the spear all of a sudden…?”

[P217]
“Train as if it were real combat. Haven’t you heard that saying?”

[P218]
Jin Mukyung smiled brightly and added:

[P219]
“I even got Hyung’s permission. He said he doesn’t mind if we have to call an undertaker.”

[P220]
I stared blankly at his back as he walked away with light, cheerful steps. At last, I managed to open my mouth.

[P221]
“…Logout.”

[P222]
Beep.

[P223]
> **System**
>
> - Logout is restricted during this Quest.

[P224]
*Fuck.*
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 권법     | **fist technique**                               |                                                       |
| 신법     | **movement technique**                           |                                                       |
| 주화입마   | **qi deviation**                                 |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 로그아웃             | **Logout**                     |
| 체력               | **Stamina**                    |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 임독양맥 | **Conception and Governor Vessels** | The paired vessels Taekyung attempts to open. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 69,
  "passed": true,
  "metrics": {
    "source_characters": 6273,
    "translation_characters": 13987,
    "length_ratio": 2.23,
    "source_paragraphs": 222,
    "translation_paragraphs": 224
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "기세",
        "preferred": "aura / momentum"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "일격",
        "preferred": "One Strike"
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
        "korean": "진태",
        "preferred": "Jintae"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "화시",
        "preferred": "fire arrow"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "원단",
        "preferred": "New Year's Day"
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
        "korean": "시진",
        "preferred": "shichen"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "기해",
        "preferred": "qi sea"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "세가",
        "preferred": "great family"
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
