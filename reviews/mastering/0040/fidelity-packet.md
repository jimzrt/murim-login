# Fidelity Gate — Chapter 40

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
  1|＃40화
  2|
  3|
  4|
  5|나는 하늘을 날고 있다. 거대한 날개를 펴고 바람을 갈랐다.
  6|
  7|저 아래 보이는 높고 가파른 협곡. 호리병 형상을 띤 그곳에 인간들이 있었다. 그 수가 어림잡아 수백.
  8|
  9|중심에 선 남자가 목청껏 외쳤다.
 10|
 11|“태원진가를 위해 싸우지 마라!”
 12|
 13|그때 땅이 진동했다. 나무가 흔들리고 산새가 날아오른다.
 14|
 15|흘끗 뒤를 돌아보자 거대한 먼지구름이 협곡을 휩쓸며 다가오고 있었다.
 16|
 17|“너희를 위해 싸워라! 적들에게 짓밟힐 혈육과 사랑하는 이를 위해 싸워라!”
 18|
 19|검을 뽑아 든 그가 포효한다.
 20|
 21|“무인답게 맞서라! 나도 그러할 것이다!”
 22|
 23|수백 개의 병장기가 나란히 뽑혔다. 성큼성큼 걸어 나간 남자가 선두에 섰다. 협곡을 가로지르던 먼지구름이 흩어지고 무수한 인간들이 모습을 드러낸다.
 24|
 25|- 와아아!
 26|
 27|- 태원진가 놈들을 쓸어 버려라!
 28|
 29|문득 남자가 고개를 들었다. 나를 발견한 그가 씩 웃었다.
 30|
 31|“느낌이 좋군.”
 32|
 33|남자의 얼굴을 본 순간, 날개에 힘이 스르륵 빠졌다. 나는 의식 깊은 곳으로 추락했다.
 34|
 35|
 36|
 37|* * *
 38|
 39|
 40|
 41|“어푸, 어푸어푸!”
 42|
 43|필사적으로 날개를, 아니 팔을 퍼덕거리다가 깨달았다.
 44|
 45|‘꿈이었구나.’
 46|
 47|천만다행이다. 죽는 줄 알았네. 한숨 돌린 후에야 방 안의 상황이 눈에 들어왔다.
 48|
 49|
 50|
 51|- 뉴스 속보입니다. 합정역 3번 출구에서 새로운 게이트가 출몰했습니다. 마력 측정 결과 C급 게이트로 판명 났으며…….
 52|
 53|
 54|
 55|책상 위, 아나운서의 모습을 비추고 있는 소형 TV. 그리고.
 56|
 57|“방금 뭐냐?”
 58|
 59|진호 형이 있었다. 한 손에는 냄비 뚜껑. 다른 한 손에는 젓가락을 든 그가 어처구니가 없다는 표정으로 나를 바라본다.
 60|
 61|“행위 예술 같은 건가.”
 62|
 63|“닥쳐. 꿈꿨어.”
 64|
 65|“헤엄치는 꿈?”
 66|
 67|“떨어지는 꿈.”
 68|
 69|“좋겠네. 키 크겠다.”
 70|
 71|영혼 없는 말을 던지고 후루룩 면발을 빨아들이는 모습이 자연스럽다. 순간 여기가 내 방이 맞나, 헷갈릴 정도로.
 72|
 73|“여기 내 방 맞지?”
 74|
 75|“그럴걸.”
 76|
 77|“근데 형이 왜 여기 있어?”
 78|
 79|“하루 이틀이야?”
 80|
 81|그럴듯한데? 순간 설득당할 뻔했다.
 82|
 83|“TV나 좀 끄든가. 사람 자는데.”
 84|
 85|“어떤 몰상식한 새끼는 목젖도 때리더라. 사람 자는데.”
 86|
 87|“…….”
 88|
 89|하여간 저 인간, 말빨 하나는 끝내준다.
 90|
 91|“할 말 없으면 라면이나 먹어. 너 깰 것 같아서 다섯 개 끓였어.”
 92|
 93|선견지명 보소. 젓가락을 받아 든 나는 감회에 젖었다.
 94|
 95|이게 보통 라면인가. 한 달 만에 먹는 라면이다. 식욕을 당기는 냄새, 딱 알맞게 익은 면발과 따로 썰어 넣은 청양고추로 매콤하게 끓여진 국물.
 96|
 97|‘미쳤다, 미쳤어.’
 98|
 99|후루루룩.
100|
101|정신이 들었을 때는 모든 게 끝난 후였다. 냄비 바닥까지 싹싹 핥아 먹고 있는 나를 진호 형이 멍하니 바라봤다.
102|
103|“광고 찍는 줄 알았네. 태어나서 라면 처음 먹어 보냐?”
104|
105|“돌아와서 처음 먹는 라면이니까.”
106|
107|“또 그 소리냐?”
108|
109|“한 달 동안 중국 음식만 먹다가 라면 먹어 봐. 미슐랭이 따로 없다.”
110|
111|“그만해. 이제 재미없으니까.”
112|
113|질렸다는 표정. 하지만 이번에는 나도 믿는 구석이 있다.
114|
115|“이거나 보고 다시 얘기합시다.”
116|
117|“뭔데 이게.”
118|
119|“뭐긴. 제품 사용 설명서지.”
120|
121|“……이거 설마.”
122|
123|“어, 저 캡슐에 들어 있더라고. 읽어 봐.”
124|
125|“20년도 더 지난 고물을 버리면서 이런 걸 넣어 둔다고?”
126|
127|진호 형은 고개를 갸웃하더니 설명서를 읽기 시작했다. 그리고 몇 초 지나지 않아 고개를 들었다.
128|
129|“이거 인쇄가 잘못됐네. 제조일이 2020년 1월 1일이야.”
130|
131|나도 처음에는 그렇게 생각했다. 처음에는.
132|
133|“그거, 인쇄 오류 아닐지도 몰라.”
134|
135|“응?”
136|
137|“아니, 이건 아직 짐작이니까 넘어가자. 다른 부분은 어때? 거기 적혀 있는 모델명이나 제조사, 형은 들어 봤어?”
138|
139|전자 기기, 그중에서도 캡슐이라면 사족을 못 쓰는 그다.
140|
141|관련 사이트에서도 이름만 대면 아는 네임드 유저에 IT 전문 블로그도 운영했었다고 했다.
142|
143|하지만 즉각 튀어나온 대답은 기대를 와르르 무너트렸다.
144|
145|“아니.”
146|
147|하긴, 인터넷 검색으로도 나오지 않았으니 어떻게 보면 당연한 결과다. 하지만 약간의 실망감은 어쩔 수 없다.
148|
149|“전혀 몰라? 형 이쪽 계통은 완전 빠삭하잖아.”
150|
151|“그렇지. 근데 이건 모르겠다.”
152|
153|진호 형이 머리를 긁적였다.
154|
155|“불법 개조 캡슐? 아니면 커스텀인가? 솔직히 저런 디자인은 처음 보네.”
156|
157|들을수록 암담하다.
158|
159|“그래, 디자인은 뭐 그렇다 쳐. 근데, 내가 최초 모델부터 최신형까지 다 꿰고 있는 사람이거든? 국내에 한 번이라도 풀린 물건은 싹 다.”
160|
161|“그런데?”
162|
163|“여기 적힌 모델명. 제조사. 완전히 쌩 초면이야.”
164|
165|“해외 쪽 제조사일 수도 있지 않나?”
166|
167|“어이고. 이 화상아, 등신아, 머저리 같은 놈아.”
168|
169|진호 형이 속 터진다는 얼굴로 설명서를 내밀었다.
170|
171|“첫 줄 읽어 봐라.”
172|
173|“제품 사용 설명서?”
174|
175|“그래. 한글이라고, 한글!”
176|
177|“아.”
178|
179|“H 소프트가 국내 제조 업체건, 해외 제조 업체건 사용 설명서까지 한글로 만들 정도면 모를 수가 없지. 그 바닥에 캡슐 제조사가 수백, 수천 개도 아닌데.”
180|
181|완전 바보가 된 기분이다. 내가 캡슐 관해서 뭐 아는 게 있어야지. 그때 진호 형이 말했다.
182|
183|“잠깐 기다려 봐.”
184|
185|스마트폰을 꺼내 화면을 두드리는 걸 보니 검색 중인 모양이다. 하지만 결과는 뻔했다.
186|
187|“시발, 야동 사이트밖에 안 뜨네.”
188|
189|어, 거기 괜찮더라.
190|
191|“유령 회사도 아니고. 왜 아무것도 안 떠?”
192|
193|“일단 뒷장도 읽어 봐.”
194|
195|마지막 장까지 읽으면 정말 유령에 홀린 기분이 될걸. 진호 형은 심각한 얼굴로 설명서를 넘겼다.
196|
197|한 번. 그리고 다시 한번.
198|
199|“기가 막히지?”
200|
201|“그러네. 기가 막히네.”
202|
203|허탈한 음성이었다.
204|
205|“백지를 보라고 하니까 기가 막히네.”
206|
207|“어?”
208|
209|“어쩐지 뭔 설명서가 이렇게 허술하나 했다. 캡슐 부품 설명도 없고, 실행 방법도 없고, 그나마 있는 모델명, 제조사, 제조일도 개판이고.”
210|
211|“아니, 백지? 그게 무슨 소리야!”
212|
213|“얼씨구. 문과충 자식 천연덕스러운 거 보소.”
214|
215|황급히 설명서를 뺏어 읽었다. 잠들기 전 봤던 그 내용이 그대로 있다. 두 번째 페이지에는 주의 사항. 마지막 페이지에는 주요 기능.
216|
217|“이게 안 보여?”
218|
219|“그만해라. 무서워지려고 한다.”
220|
221|저 표정. 말투. 진심이다. 내게 보이는 이 글씨가, 진호 형에게는 보이지 않는다.
222|
223|아니, 어쩌면…….
224|
225|‘이 내용은 나한테만 보인다.’
226|
227|나는 한동안 그렇게 굳어 있었다.
228|
229|
230|
231|* * *
232|
233|
234|
235|푸쉭-
236|
237|후들거리는 다리로 캡슐을 빠져나왔다. 반질거리는 외관, 흡사 거대한 달걀처럼 보이는 이 물건은 지난달에 출시된 최신형 캡슐이다.
238|
239|“어, 금방 나오셨네. 제가 추천해 드린 게임 해 보셨어요?”
240|
241|카운터에 앉아 있던 캡슐방 사장의 물음에 나는 반쯤 혼이 나간 채로 대답했다.
242|
243|“네.”
244|
245|사장이 권유한 가상현실 게임은 동시 접속자만 천만 명에 달한다는 메가 히트작. 엄청난 그래픽과 뛰어난 자유도로 시장 점유율 70%가 넘는다고 했다.
246|
247|“그래픽 미쳤죠?”
248|
249|게임에 접속. 그래픽을 보고 생각했다. 내가 미쳤나?
250|
251|‘이게 가장 잘나가는 가상현실 게임이라고?’
252|
253|그래픽 좋은 건 알겠다. 하지만 딱 거기까지였다.
254|
255|NPC들의 외모와 움직임, 대화 패턴과 내 캐릭터로 느껴지는 오감(五感). 모두 부자연스럽다. ‘게임’이지만 결코 ‘현실’처럼 느껴지진 않는다.
256|
257|“혹시 무협 배경 게임도 있나요?”
258|
259|“아하, 무협 쪽 취향이시구나? 꽤 있긴 하죠. 찾으시는 게임 제목이 뭔데요?”
260|
261|“무림이요.”
262|
263|“무림 온라인?”
264|
265|“아뇨. 오픈 월드 식 게임이에요. 혼자 플레이하는.”
266|
267|“무협 게임 중에 그런 게 있어요?”
268|
269|그럼 그렇지. 더 들어 볼 것도 없다. 비틀비틀 문을 나서는 내게 사장이 인사했다.
270|
271|“또 오세요!”
272|
273|안 올 거다. 두 번 다시.
274|
275|
276|
277|* * *
278|
279|
280|
281|희망 고시원.
282|
283|낡고 녹슨 간판 아래에 앉아 스마트폰을 꺼냈다. 신호음이 가기 무섭게 상대방이 전화를 받았다.
284|
285|딸깍.
286|
287|- 어, 왜.
288|
289|하나뿐인 웬수, 아니 여동생인 하연이다. 특유의 싸가지 없는 목소리를 듣는 순간 목이 꽉 막혔다.
290|
291|- 여보세요?
292|
293|“……어.”
294|
295|- 왜 전화했어?
296|
297|“그냥. 목소리 듣고 싶어서.”
298|
299|순간, 죽음 같은 침묵이 흘렀다.
300|
301|- 끊는다.
302|
303|“아니, 잠깐만. 잠깐만!”
304|
305|- 3초 준다. 용건.
306|
307|망할 년…….
308|
309|그래, 이래야 진하연이지. 덕분에 잠시나마 촉촉해졌던 눈물샘이 피라미드 인근 모래처럼 건조해졌다.
310|
311|“엄마는 뭐 하셔?”
312|
313|- 잠깐 볼일 있다고 외출. 궁금하면 전화해 봐.
314|
315|일부러 하지 않았다. 이 녀석 목소리에도 울컥하는데 엄마 목소리를 들으면 어린아이처럼 엉엉 울 것 같아서.
316|
317|나는 재빨리 말을 돌렸다.
318|
319|“너는?”
320|
321|- 수능 120일 남은 고삼이 뭐 하겠어. 공부하지.
322|
323|평소보다 까칠한 말투. 수험생 스트레스가 상당한 모양이다.
324|
325|“공부는 잘되고?”
326|
327|- 이번에 7월 모의고사 망쳤어. 컨디션 조절 실패해서 쉬운 문제도 다 틀리고. 아, 생각할수록 짜증 나.
328|
329|“괜찮아. 실전에서만 잘하면 되지. 몇 개나 틀렸는데?”
330|
331|- 두 개.
332|
333|“그 정도면 1등급이잖아. 다른 과목은?”
334|
335|- 전 과목 두 개.
336|
337|“응?”
338|
339|- 한국사에서 하나. 수학에서 하나.
340|
341|“……전 과목 통틀어서 두 개? 진심이냐?”
342|
343|- 당연히 그거 말한 거지.
344|
345|똑똑한 년…….
346|
347|공부 잘하는 건 알고 있었는데 이 정도일 줄이야. 과거 내 학창 시절 성적을 생각해 보면 유전자 몰빵이라는 게 정말 존재하는 모양이다.
348|
349|“공부 좀 한다?”
350|
351|- 오빠 입장에서 보면 엄청 잘하는 거 아냐?
352|
353|“무, 무슨 헛소리를! 나도 공부 꽤 했거든? 네가 초등학생 때라 기억을 못 하는 거…….”
354|
355|- 지난주에 대청소하다가 오빠 성적표 나왔어. 7등급이 하도 많아서 무슨 잭팟 터진 슬롯머신인 줄.
356|
357|“용돈 필요하지? 요즘 화장품은 얼마나 하냐?”
358|
359|- 애잔하다. 진짜.
360|
361|잔인한 년…….
362|
363|통화는 10분이 넘도록 이어졌다. 나는 주로 듣는 쪽이었다. 공부, 학교, 관심 있는 남학생 이야기를 떠들어 대는 하연이의 목소리는 처음보다 한결 밝아져 있었다.
364|
365|문득 묘한 감상에 젖어 들었다.
366|
367|‘정말 돌아왔구나.’
368|
369|나는 꿈을 꿨던 걸까, 아니면 망상에 빠져 있던 걸까.
370|
371|현실에서는 고작 하루가 지났을 뿐인데 도저히 이해할 수 없는 불가사의한 일들이 일어났다.
372|
373|하지만 이제는 이해하지 않기로 했다.
374|
375|‘이제 현실로 돌아왔으니까.’
376|
377|그리고 현실에서 살아야 하니까.
378|
379|이곳에 가족이 있고 내가 있다. 그럼 그걸로 된 거다. 나는 아주 잠깐 이상한 꿈을 꾼 거다. 시간이 흐르면 자연스럽게 잊혀질, 그런 꿈.
380|
381|- 그래서 내가…….
382|
383|“응.”
384|
385|조잘거리는 여동생의 목소리를 들으며, 나는 자리에서 일어났다. 낡고 녹슨 간판 아래를 벗어나 내 방으로 돌아가야 할 시간이었다.
386|
387|
388|
389|* * *
390|
391|
392|
393|지잉. 지이잉.
394|
395|성진호는 부스스 눈을 떴다. 머리맡에 놓아둔 스마트폰이 울리고 있었다. 새벽 여섯 시. 오늘 하루를 시작하는 신호였다.
396|
397|“어이고, 죽겠다.”
398|
399|집을 나온 지 5년째. 아침마다 코끝을 파고드는 곰팡내가 퍽 익숙해졌다. 성진호는 반쯤 감긴 눈으로 담배와 라이터를 주머니에 쑤셔 넣고 방을 나섰다.
400|
401|‘잠 깨는 데는 담배가 최고지.’
402|
403|슬리퍼를 질질 끌며 옥상으로 올라간 그가 담배를 입에 물었을 때였다.
404|
405|쿵.
406|
407|“응?”
408|
409|무슨 소리지? 의문과 함께 난간으로 고개를 내밀자 바로 앞 분리수거장에 놓인 쇳덩어리가 눈에 띄었다.
410|
411|그리고 그걸 물끄러미 바라보는 덩치 좋은 청년도.
412|
413|“야! 진태경!”
414|
415|성진호의 외침에 진태경이 고개를 들었다.
416|
417|“왜?”
418|
419|“그거 버리게?”
420|
421|쇳덩어리의 정체는 전날 주워 온 고물 캡슐이었다. 저걸로 되지 않는 장난이나 치더니 도로 갖다 버리려는 모양이었다.
422|
423|‘그런 것치곤 너무 진지하긴 했는데…… 뭐, 헛소리지.’
424|
425|성진호가 피식 웃었다.
426|
427|“왜 버려. 무림 다시 안 가?”
428|
429|“그걸 믿었어?”
430|
431|진태경이 마주 웃었다. 하지만 오랫동안 그를 지켜봐 온 성진호가 보기에는 어쩐지 어색한 웃음이었다.
432|
433|‘뭐지?’
434|
435|묘한 느낌이다. 찝찝해하는 성진호에게 손을 흔들어 보인 진태경이 언덕을 내려가기 시작했다.
436|
437|“어디 가, 인마! 이따 같이 아침 안 먹어?”
438|
439|“일해야 돼!”
440|
441|진태경은 뒤도 돌아보지 않고 떠났다. 성진호는 반쯤 타들어 간 담배를 한 모금 빨았다.
442|
443|“새끼, 열심히 사네…….”
444|
445|이윽고 진태경의 모습이 시야에서 사라졌다. 화분에 담배를 비벼 끄고 떠나려던 성진호의 눈에 고물 캡슐이 눈에 띈 것도 그때였다.
446|
447|‘제조사가 H 소프트라고 했나?’
448|
449|허접한 장난이겠지만, 알아봐서 나쁠 건 없겠지.
```

## Assembled English

```markdown
[P1]
# Chapter 40

[P2]
I was flying through the sky, enormous wings spread wide as I cut through the wind.

[P3]
Far below, a high, steep gorge came into view. Shaped like a bottle gourd, it held people—hundreds of them, at a rough count.

[P4]
A man standing at the center shouted at the top of his lungs.

[P5]
“Don’t fight for the Jin Family of Taiyuan!”

[P6]
Then the ground shook. Trees trembled, and mountain birds took flight.

[P7]
I glanced over my shoulder. A huge cloud of dust was sweeping through the gorge toward us.

[P8]
“Fight for yourselves! Fight for the flesh and blood and loved ones who will be trampled by the enemy!”

[P9]
He drew his sword and roared.

[P10]
“Stand and face them like martial artists! I will do the same!”

[P11]
Hundreds of weapons were drawn in unison. The man strode forward and took the lead. The cloud of dust crossing the gorge scattered, revealing countless people.

[P12]
— Waaaaah!

[P13]
— Wipe out those Jin Family bastards!

[P14]
The man suddenly looked up. When he spotted me, he grinned.

[P15]
“I’ve got a good feeling about this.”

[P16]
The moment I saw his face, the strength drained from my wings. I plunged into the depths of consciousness.

[P17]
* * *

[P18]
“Pwah, pwah-pwah!”

[P19]
I flailed desperately with my wings—or rather, my arms—before it hit me.

[P20]
*It was a dream.*

[P21]
Thank god. I thought I was a goner. Only after catching my breath did the situation in the room come into focus.

[P22]
— This is a breaking news report. A new Gate has appeared at Exit 3 of Hapjeong Station. Mana measurements have confirmed it as a C-rank Gate, and…

[P23]
A small TV sat on the desk, showing an announcer. And then there was—

[P24]
“What the hell was that?”

[P25]
Jinho hyung. He held a pot lid in one hand and chopsticks in the other, staring at me like I was out of my mind.

[P26]
“Some kind of performance art?”

[P27]
“Shut up. I was dreaming.”

[P28]
“About swimming?”

[P29]
“About falling.”

[P30]
“Good for you. You’ll grow taller.”

[P31]
He tossed out the line with zero soul and slurped up his noodles, looking completely at home. For a moment I wondered if this was even my room.

[P32]
“This is my room, right?”

[P33]
“Probably.”

[P34]
“Then why are you here?”

[P35]
“Is this anything new?”

[P36]
That actually sounded plausible. I almost bought it.

[P37]
“Turn the TV off or something. People are sleeping.”

[P38]
“Some inconsiderate bastard even hits people in the uvula while they’re sleeping.”

[P39]
“…”

[P40]
Anyway, that bastard had one hell of a mouth on him.

[P41]
“If you’ve got nothing to say, eat some ramen. I boiled five packs because I thought you might wake up.”

[P42]
Talk about foresight. I took the chopsticks from him, a wave of feeling hitting me.

[P43]
Was this ordinary ramen? This was my first ramen in a month.

[P44]
The smell that pulled at my appetite. Noodles cooked just right. Broth boiled spicy with separately sliced Cheongyang peppers.

[P45]
*Insane. This is insane.*

[P46]
Slurp.

[P47]
By the time I came to my senses, it was all over. Jinho hyung stared blankly at me as I licked the pot clean.

[P48]
“I thought you were filming a commercial. Have you never eaten ramen in your life?”

[P49]
“It’s my first ramen since I came back.”

[P50]
“You’re still going on about that?”

[P51]
“Try eating nothing but Chinese food for a month, then have some ramen. Michelin’s got nothing on this.”

[P52]
“Stop. It’s not funny anymore.”

[P53]
He looked thoroughly fed up. But this time, I had something to back me up.

[P54]
“Look this over, then we’ll talk again.”

[P55]
“What is this?”

[P56]
“What do you think? A product user manual.”

[P57]
“…”

[P58]
“Don’t tell me…”

[P59]
“Yeah. It was inside that capsule. Read it.”

[P60]
“You’re saying someone put this inside a piece of junk more than twenty years old when they threw it away?”

[P61]
Jinho hyung tilted his head, then started reading. A few seconds later, he looked up.

[P62]
“This is a misprint. The date of manufacture is January 1, 2020.”

[P63]
I’d thought the same thing at first. At first.

[P64]
“That might not be a printing error.”

[P65]
“Huh?”

[P66]
“No, never mind. That’s still just a guess. What about the rest? Have you ever heard of the model or manufacturer listed there?”

[P67]
Jinho hyung was crazy about electronics, especially capsules.

[P68]
On the related sites, he was a named user people knew by name alone. He’d even run an IT blog.

[P69]
But his immediate answer sent my expectations crashing down.

[P70]
“No.”

[P71]
Well, that was only natural. Even an internet search hadn’t turned anything up. Still, I couldn’t help feeling a little disappointed.

[P72]
“You really don’t know? You know this field inside out.”

[P73]
“Yeah. But I don’t know this.”

[P74]
Jinho hyung scratched his head.

[P75]
“An illegally modded capsule? Or a custom job? Honestly, I’ve never seen a design like that.”

[P76]
The more he talked, the bleaker it got.

[P77]
“Fine, I’ll grant you the design. But I know every model from the earliest ones to the latest. Everything that’s ever been released in Korea.”

[P78]
“And?”

[P79]
“The model name written here. The manufacturer. Complete strangers.”

[P80]
“Couldn’t it be an overseas manufacturer?”

[P81]
“Oh, you hopeless idiot. You dumbass. You moron.”

[P82]
Jinho hyung thrust the manual at me, looking thoroughly exasperated.

[P83]
“Read the first line.”

[P84]
“Product User Manual?”

[P85]
“Exactly. It’s in Korean. Korean!”

[P86]
“Oh.”

[P87]
“Whether H Soft is a domestic manufacturer or an overseas one, if they went as far as making the user manual in Korean, there’s no way I wouldn’t know them. It’s not like there are hundreds or thousands of capsule manufacturers in this business.”

[P88]
I felt like a complete idiot. Not that I knew anything about capsules. That was when Jinho hyung spoke up.

[P89]
“Wait a second.”

[P90]
He pulled out his smartphone and started tapping the screen. Searching, from the looks of it. But the result was obvious.

[P91]
“Fuck. Nothing but a porn site.”

[P92]
*Yeah, that one was pretty good.*

[P93]
“It’s not even a ghost company. Why isn’t anything coming up?”

[P94]
“Read the rest of it, too.”

[P95]
By the time he reached the last page, he’d really feel like he’d been haunted. Jinho hyung turned the pages with a serious expression.

[P96]
Once.

[P97]
Then once more.

[P98]
“Isn’t it incredible?”

[P99]
“Yeah. Incredible.”

[P100]
His voice was hollow.

[P101]
“You told me to look at blank pages. That’s incredible.”

[P102]
“Huh?”

[P103]
“No wonder I thought this manual was so slapdash. No explanation of the capsule’s parts, no operating instructions, and even the model name, manufacturer, and date of manufacture are a mess.”

[P104]
“Blank pages? What are you talking about?”

[P105]
“Well, well. Look at this liberal-arts dumbass playing innocent.”

[P106]
I snatched the manual and read it in a hurry. The contents I’d seen before falling asleep were still there. Precautions on the second page. Key features on the last.

[P107]
“You can’t see this?”

[P108]
“Cut it out. This is starting to get scary.”

[P109]
That look. That tone. He meant it. The writing I could see was invisible to Jinho hyung.

[P110]
Or maybe…

[P111]
*Only I can see this.*

[P112]
I stayed frozen like that for a long while.

[P113]
* * *

[P114]
Pshhh—

[P115]
I climbed out of the capsule on shaky legs. Glossy exterior, shaped like a giant egg—this was the latest model, released only last month.

[P116]
“Oh, you’re out already. Did you try the game I recommended?”

[P117]
Still half out of my mind, I answered the capsule café owner sitting at the counter.

[P118]
“Yes.”

[P119]
The virtual-reality game he’d recommended was a megahit with ten million concurrent users. It had incredible graphics, outstanding freedom, and more than seventy percent of the market, he’d said.

[P120]
“The graphics are insane, right?”

[P121]
I logged in. I looked at the graphics and thought:

[P122]
*Am I the one who’s insane?*

[P123]
*This is the most popular virtual-reality game there is?*

[P124]
The graphics were good. I could give it that. But that was as far as it went.

[P125]
The NPCs’ appearances and movements, their dialogue patterns, the five senses I felt through my character—all of it was unnatural. It was a *game*, but it never felt like *reality*.

[P126]
“Do you have any games set in wuxia?”

[P127]
“Ah, so you’re into wuxia? There are quite a few. What’s the title you’re looking for?”

[P128]
“Murim.”

[P129]
“Murim Online?”

[P130]
“No. It’s an open-world game. Single-player.”

[P131]
“Is there a wuxia game like that?”

[P132]
Figures. There was nothing more to hear. I staggered out the door, and the owner called after me.

[P133]
“Come again!”

[P134]
I wouldn’t.

[P135]
Not ever again.

[P136]
* * *

[P137]
Hope Goshiwon.

[P138]
I sat beneath the old, rusted sign and pulled out my smartphone. The other end picked up almost before it could ring.

[P139]
Click.

[P140]
“Yeah. Why?”

[P141]
My one and only nemesis—no, my younger sister, Hayeon. The moment I heard that uniquely bratty voice of hers, my throat closed up.

[P142]
“Hello?”

[P143]
“…Yeah.”

[P144]
“Why’d you call?”

[P145]
“Just. I wanted to hear your voice.”

[P146]
A deathly silence followed.

[P147]
“I’m hanging up.”

[P148]
“No, wait. Wait!”

[P149]
“Three seconds. What’s your business.”

[P150]
*That damn girl…*

[P151]
Right. This was Jin Hayeon. Thanks to her, the tear ducts that had gotten a little moist dried out like sand around the pyramids.

[P152]
“What’s Mom doing?”

[P153]
“She went out. Said she had an errand. Call her if you’re curious.”

[P154]
I deliberately didn’t. Even this brat’s voice was enough to choke me up. If I heard Mom’s, I’d probably bawl like a little kid.

[P155]
I quickly changed the subject.

[P156]
“What about you?”

[P157]
“What’s a high-school senior with a hundred and twenty days left until the college entrance exam supposed to do? Study.”

[P158]
Her tone was sharper than usual. Exam stress must have been hitting her hard.

[P159]
“How’s studying going?”

[P160]
“I bombed the July mock exam. I failed to manage my condition and missed even the easy questions. God, the more I think about it, the more annoyed I get.”

[P161]
“It’s fine. Just do well on the real thing. How many did you miss?”

[P162]
“Two.”

[P163]
“That’s still Grade 1.[^1] What about the other subjects?”

[P164]
“Two across all subjects.”

[P165]
“Huh?”

[P166]
“One in Korean history and one in math.”

[P167]
“…Two in total, across every subject? Are you serious?”

[P168]
“Obviously that’s what I meant.”

[P169]
*Smart little brat…*

[P170]
I knew she was good at studying, but I hadn’t realized she was this good. Thinking back on my own school grades, it really seemed like there was such a thing as dumping all the genes into one kid.

[P171]
“You study pretty well, huh?”

[P172]
“From your perspective, isn’t that really good?”

[P173]
“W-what kind of nonsense is that? I studied pretty well too, you know? You just don’t remember because you were in elementary school…”

[P174]
“Last week during a deep clean, I found your report card. There were so many Grade 7s I thought it was a slot machine that had hit the jackpot.”

[P175]
“You need some allowance, right? How much does makeup cost these days?”

[P176]
“That’s pathetic. Seriously.”

[P177]
*Cruel girl…*

[P178]
The call lasted more than ten minutes. I mostly listened. Hayeon rattled on about studying, school, and a boy she was interested in, her voice much brighter than it had been at first.

[P179]
I found myself getting oddly sentimental.

[P180]
*I really did come back.*

[P181]
Had I been dreaming? Or lost in a delusion?

[P182]
Only a day had passed in reality, yet utterly incomprehensible, inexplicable things had happened.

[P183]
But I decided to stop trying to understand them.

[P184]
*I’m back in reality now.*

[P185]
And I had to live in reality.

[P186]
My family was here. I was here. That was enough. I had simply dreamed a strange dream for a little while. The kind of dream that would fade on its own with time.

[P187]
“So I…”

[P188]
“Yeah.”

[P189]
Listening to my little sister chatter, I stood up. It was time to step out from beneath the old, rusted sign and go back to my room.

[P190]
* * *

[P191]
Bzzzt. Bzzzt.

[P192]
Seong Jinho cracked his bleary eyes open. The smartphone beside his pillow was vibrating.

[P193]
Six in the morning. The signal that started the day.

[P194]
“Oh, I’m dying.”

[P195]
It had been five years since he left home. The moldy smell that crept into his nose every morning had gotten pretty familiar. Eyes half shut, Seong Jinho shoved his cigarettes and lighter into his pocket and left the room.

[P196]
*Nothing wakes you up like a cigarette.*

[P197]
He shuffled up to the rooftop in his slippers. He’d just put a cigarette between his lips when—

[P198]
Thud.

[P199]
“Huh?”

[P200]
What was that? Wondering, he leaned over the railing, and a hunk of metal sitting in the recycling area right in front of him caught his eye.

[P201]
So did the well-built young man gazing at it.

[P202]
“Hey! Jin Taekyung!”

[P203]
At Seong Jinho’s shout, Jin Taekyung looked up.

[P204]
“What?”

[P205]
“You throwing that away?”

[P206]
The hunk of metal was the junk capsule Taekyung had picked up the day before. After using it for some ridiculous prank, he seemed to be taking it back out to throw away.

[P207]
*He’d been awfully serious for a prank like that… Ah, whatever. It was nonsense.*

[P208]
Seong Jinho gave a short laugh.

[P209]
“Why throw it away? Not going back to Murim?”

[P210]
“You believed that?”

[P211]
Jin Taekyung smiled back. But to Seong Jinho, who had watched him for a long time, the smile looked somehow awkward.

[P212]
*What’s with him?*

[P213]
Something felt off. As Seong Jinho stood there uneasily, Jin Taekyung waved and started down the hill.

[P214]
“Where are you going, you punk? Aren’t we eating breakfast together later?”

[P215]
“I have to work!”

[P216]
Jin Taekyung left without looking back. Seong Jinho took a drag from his half-burned cigarette.

[P217]
“That bastard’s really working hard…”

[P218]
Soon, Jin Taekyung disappeared from sight. Seong Jinho stubbed out his cigarette in a flowerpot and was about to leave when the junk capsule caught his eye.

[P219]
*He said the manufacturer was H Soft, right?*

[P220]
It was probably just some half-assed prank, but there was no harm in looking into it.

[P221]
[^1]: Korean mock exams use a 1–9 scale; Grade 1 is the highest.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 40

[P2]
I was flying through the sky. Enormous wings spread, I cut through the wind.

[P3]
Far below, a high, steep gorge came into view. Shaped like a bottle gourd, it held people—hundreds of them, at a rough count.

[P4]
A man standing at the center shouted at the top of his lungs.

[P5]
“Don’t fight for the Jin Family of Taiyuan!”

[P6]
Then the ground shook. Trees trembled, and mountain birds took flight.

[P7]
I glanced over my shoulder. A huge cloud of dust was sweeping through the gorge toward us.

[P8]
“Fight for yourselves! Fight for the flesh and blood and loved ones who will be trampled by the enemy!”

[P9]
He drew his sword and roared.

[P10]
“Stand and face them like martial artists! I will do the same!”

[P11]
Hundreds of weapons were drawn in unison. The man strode forward and took the lead. The cloud of dust crossing the gorge scattered, revealing countless people.

[P12]
— Waaaaah!

[P13]
— Wipe out those Jin Family bastards!

[P14]
The man suddenly looked up. When he spotted me, he grinned.

[P15]
“I’ve got a good feeling about this.”

[P16]
The moment I saw his face, the strength drained from my wings. I plunged into the depths of consciousness.

[P17]
* * *

[P18]
“Pwah, pwah-pwah!”

[P19]
I flailed desperately with my wings—or rather, my arms—before it hit me.

[P20]
*It was a dream.*

[P21]
Thank god. I thought I was a goner. Only after catching my breath did the situation in the room come into focus.

[P22]
— This is a breaking news report. A new Gate has appeared at Exit 3 of Hapjeong Station. Mana measurements have confirmed it as a C-rank Gate, and…

[P23]
A small TV sat on the desk, showing an announcer. And then there was—

[P24]
“What the hell was that?”

[P25]
Jinho hyung. He held a pot lid in one hand and chopsticks in the other, staring at me like I was out of my mind.

[P26]
“Some kind of performance art?”

[P27]
“Shut up. I was dreaming.”

[P28]
“About swimming?”

[P29]
“About falling.”

[P30]
“Good for you. You’ll grow taller.”

[P31]
He tossed out the line with zero soul and slurped up his noodles, looking completely at home. For a moment I wondered if this was even my room.

[P32]
“This is my room, right?”

[P33]
“Probably.”

[P34]
“Then why are you here?”

[P35]
“What, has it only been a day or two?”

[P36]
That actually sounded plausible. I almost bought it.

[P37]
“Turn the TV off or something. People are sleeping.”

[P38]
“Some inconsiderate bastard even hits people in the uvula while they’re sleeping.”

[P39]
“…”

[P40]
Anyway, that bastard had one hell of a mouth on him.

[P41]
“If you’ve got nothing to say, eat some ramen. I boiled five packs because I thought you might wake up.”

[P42]
Talk about foresight. I took the chopsticks from him, a wave of feeling hitting me.

[P43]
Was this ordinary ramen? This was ramen I was eating for the first time in a month.

[P44]
The smell that pulled at my appetite. Noodles cooked just right. Broth boiled spicy with separately sliced Cheongyang peppers.

[P45]
*Insane. This is insane.*

[P46]
Slurp.

[P47]
By the time I came to, it was all over. Jinho hyung stared blankly at me as I licked the pot clean.

[P48]
“I thought you were filming a commercial. Have you never eaten ramen in your life?”

[P49]
“It’s my first ramen since I came back.”

[P50]
“Are you still on that?”

[P51]
“Try eating nothing but Chinese food for a month, then have some ramen. Michelin’s got nothing on this.”

[P52]
“Stop. It’s not funny anymore.”

[P53]
He looked thoroughly fed up. But this time, I had something to back me up.

[P54]
“Look this over, then we’ll talk again.”

[P55]
“What is this?”

[P56]
“What do you think? A product user manual.”

[P57]
“…”

[P58]
“Don’t tell me…”

[P59]
“Yeah. It was inside that capsule. Read it.”

[P60]
“You stuck this in a piece of junk more than twenty years old before throwing it away?”

[P61]
Jinho hyung tilted his head, then started reading. A few seconds later, he looked up.

[P62]
“This is a misprint. The date of manufacture is January 1, 2020.”

[P63]
I’d thought the same thing at first. At first.

[P64]
“That might not be a printing error.”

[P65]
“Huh?”

[P66]
“No, never mind—that’s still just a guess. What about the rest? The model name and manufacturer listed there. Have you heard of them?”

[P67]
Jinho hyung was crazy about electronics, especially capsules.

[P68]
On the related sites, he was a named user people recognized on sight. He’d even run an IT blog.

[P69]
But the answer that came out immediately sent my expectations crashing down.

[P70]
“No.”

[P71]
Well, that was only natural. Even an internet search hadn’t turned anything up. Still, I couldn’t help feeling a little disappointed.

[P72]
“You really don’t know? You know this field inside out.”

[P73]
“Yeah. But I don’t know this.”

[P74]
Jinho hyung scratched his head.

[P75]
“An illegally modded capsule? Or a custom job? Honestly, I’ve never seen a design like that.”

[P76]
The more he talked, the bleaker it got.

[P77]
“Fine, I’ll grant you the design. But I know every model from the earliest ones to the latest. Everything that’s ever been released in Korea.”

[P78]
“And?”

[P79]
“The model name written here. The manufacturer. Complete strangers.”

[P80]
“Couldn’t it be an overseas manufacturer?”

[P81]
“Oh, you hopeless idiot. You dumbass. You moron.”

[P82]
Jinho hyung thrust the manual at me, looking thoroughly exasperated.

[P83]
“Read the first line.”

[P84]
“Product User Manual?”

[P85]
“Exactly. It’s in Korean. Korean!”

[P86]
“Oh.”

[P87]
“Whether H Soft is a domestic manufacturer or an overseas one, if they went as far as making the user manual in Korean, there’s no way I wouldn’t know them. It’s not like there are hundreds or thousands of capsule manufacturers in this business.”

[P88]
I felt like a complete idiot. Not that I knew anything about capsules. That was when Jinho hyung spoke up.

[P89]
“Wait a second.”

[P90]
He pulled out his smartphone and started tapping the screen. Searching, from the looks of it. But the result was obvious.

[P91]
“Fuck. All that comes up is porn sites.”

[P92]
*Yeah, that one was pretty good.*

[P93]
“It’s not even a ghost company. Why isn’t anything coming up?”

[P94]
“Read the rest of it, too.”

[P95]
By the time he reached the last page, he’d really feel like he’d been haunted. Jinho hyung turned the pages with a serious expression.

[P96]
Once.

[P97]
Then once more.

[P98]
“Isn’t it incredible?”

[P99]
“Yeah. Incredible.”

[P100]
His voice was hollow.

[P101]
“You told me to look at blank pages. That’s incredible.”

[P102]
“Huh?”

[P103]
“No wonder I thought this manual was so slapdash. No explanation of the capsule’s parts, no operating instructions, and even the model name, manufacturer, and date of manufacture are a mess.”

[P104]
“Blank pages? What are you talking about?”

[P105]
“Well, well. Look at this humanities-major bastard, acting all innocent.”

[P106]
I snatched the manual and read it in a hurry. The contents I’d seen before falling asleep were still there. Precautions on the second page. Key features on the last.

[P107]
“You can’t see this?”

[P108]
“Cut it out. This is starting to get scary.”

[P109]
That look. That tone. He meant it. The writing I could see was invisible to Jinho hyung.

[P110]
Or maybe…

[P111]
*Only I can see this.*

[P112]
I stayed frozen like that for a long while.

[P113]
* * *

[P114]
Pshhh—

[P115]
I climbed out of the capsule on shaky legs. Glossy exterior, shaped like a giant egg—this was the latest model, released only last month.

[P116]
“Oh, you’re out already. Did you try the game I recommended?”

[P117]
Still half out of my mind, I answered the capsule café owner at the counter.

[P118]
“Yes.”

[P119]
The virtual-reality game he’d recommended was a megahit with ten million concurrent users. Incredible graphics, outstanding freedom, over seventy percent of the market, he’d said.

[P120]
“The graphics are insane, right?”

[P121]
I logged in. I looked at the graphics and thought:

[P122]
*Am I the one who’s insane?*

[P123]
*This is the most popular virtual-reality game there is?*

[P124]
The graphics were good. I could give it that. But that was as far as it went.

[P125]
The NPCs’ faces and movements, their dialogue patterns, the five senses I felt through my character—all of it was unnatural. It was a *game*, but it never felt like *reality*.

[P126]
“Do you have any games set in wuxia?”

[P127]
“Ah, so you’re into wuxia? There are quite a few. What’s the title you’re looking for?”

[P128]
“Murim.”

[P129]
“Murim Online?”

[P130]
“No. It’s an open-world game. One you play alone.”

[P131]
“Are there games like that in the wuxia genre?”

[P132]
Figures. There was nothing more to hear. I staggered out the door, and the owner called after me.

[P133]
“Come again!”

[P134]
I wouldn’t.

[P135]
Not ever again.

[P136]
* * *

[P137]
Hope Goshiwon.

[P138]
I sat beneath the old, rusted sign and pulled out my smartphone. The other end picked up almost before it could ring.

[P139]
Click.

[P140]
“Yeah. Why?”

[P141]
My one and only nemesis—no, my younger sister, Hayeon. The moment I heard that uniquely bratty voice of hers, my throat closed up.

[P142]
“Hello?”

[P143]
“…Yeah.”

[P144]
“Why’d you call?”

[P145]
“Just. I wanted to hear your voice.”

[P146]
A deathly silence followed.

[P147]
“I’m hanging up.”

[P148]
“No, wait. Wait!”

[P149]
“Three seconds. What’s your business.”

[P150]
*That damn girl…*

[P151]
Right. This was Jin Hayeon. Thanks to her, the tear ducts that had gotten a little moist dried out like sand around the pyramids.

[P152]
“What’s Mom doing?”

[P153]
“She went out. Said she had an errand. Call her if you’re curious.”

[P154]
I didn’t. On purpose. Even this brat’s voice was enough to choke me up. If I heard Mom’s, I’d bawl like a little kid.

[P155]
I quickly changed the subject.

[P156]
“What about you?”

[P157]
“What’s a high-school senior with a hundred and twenty days left until the college entrance exam supposed to do? Study.”

[P158]
Her tone was sharper than usual. Exam stress must have been hitting her hard.

[P159]
“How’s studying going?”

[P160]
“I bombed the July mock exam. I didn’t manage my condition right and missed even the easy questions. God, the more I think about it, the more annoyed I get.”

[P161]
“It’s fine. Just do well on the real thing. How many did you miss?”

[P162]
“Two.”

[P163]
“That’s still Grade 1.[^1] What about the other subjects?”

[P164]
“Two across all subjects.”

[P165]
“Huh?”

[P166]
“One in Korean history and one in math.”

[P167]
“…Two in total, across every subject? Are you serious?”

[P168]
“Obviously that’s what I meant.”

[P169]
*Smart little brat…*

[P170]
I knew she was good at studying, but I hadn’t realized she was this good. Thinking back on my own school grades, it really seemed like there was such a thing as dumping all the genes into one kid.

[P171]
“You study pretty well, huh?”

[P172]
“From an older brother’s standpoint, isn’t it amazing?”

[P173]
“W-what kind of nonsense is that? I studied pretty well too, you know? You just don’t remember because you were in elementary school…”

[P174]
“Last week during a deep clean, I found your report card. There were so many Grade 7s I thought it was a slot machine that had hit the jackpot.”

[P175]
“You need some allowance, right? How much do cosmetics cost these days?”

[P176]
“That’s pathetic. Seriously.”

[P177]
*Cruel girl…*

[P178]
The call lasted more than ten minutes. I did most of the listening. Hayeon rattled on about studying, school, and a boy she was interested in, and her voice was much brighter than it had been at first.

[P179]
I found myself getting oddly sentimental.

[P180]
*I really did come back.*

[P181]
Had I been dreaming? Or lost in a delusion?

[P182]
Only a day had passed in reality, yet utterly incomprehensible, inexplicable things had happened.

[P183]
But I decided not to try to understand them anymore.

[P184]
*I’m back in reality now.*

[P185]
And I had to live in reality.

[P186]
My family was here. I was here. That was enough. I had simply dreamed a strange dream for a little while. The kind of dream that would fade on its own with time.

[P187]
“So I…”

[P188]
“Yeah.”

[P189]
Listening to my little sister chatter, I stood up. It was time to leave the old, rusted sign behind and go back to my room.

[P190]
* * *

[P191]
Bzzzt. Bzzzt.

[P192]
Seong Jinho cracked his bleary eyes open. The smartphone by his pillow was ringing.

[P193]
Six in the morning. The signal that started the day.

[P194]
“Oh, I’m dying.”

[P195]
It had been five years since he left home. The moldy smell that crept into his nose every morning had gotten pretty familiar. Eyes half shut, Seong Jinho shoved his cigarettes and lighter into his pocket and left the room.

[P196]
*Nothing wakes you up like a cigarette.*

[P197]
He shuffled up to the rooftop in his slippers. He’d just put a cigarette between his lips when—

[P198]
Thud.

[P199]
“Huh?”

[P200]
What was that? Wondering, he leaned over the railing, and a hunk of metal sitting in the recycling area right in front of him caught his eye.

[P201]
So did the well-built young man gazing at it.

[P202]
“Hey! Jin Taekyung!”

[P203]
At Seong Jinho’s shout, Jin Taekyung looked up.

[P204]
“What?”

[P205]
“You throwing that away?”

[P206]
The hunk of metal was the junk capsule Taekyung had picked up the day before. After pulling some failed prank with it, he seemed to be taking it back out to throw away.

[P207]
*He’d been awfully serious for a prank like that… Ah, whatever. It was nonsense.*

[P208]
Seong Jinho gave a short laugh.

[P209]
“Why throw it away? Not going back to Murim?”

[P210]
“You believed that?”

[P211]
Jin Taekyung smiled back. But to Seong Jinho, who had watched him for a long time, the smile looked somehow awkward.

[P212]
*What’s with him?*

[P213]
Something felt off. As Seong Jinho stood there uneasily, Jin Taekyung waved and started down the hill.

[P214]
“Where are you going, you punk? Aren’t we eating breakfast together later?”

[P215]
“I have to work!”

[P216]
Jin Taekyung left without looking back. Seong Jinho took a drag from his half-burned cigarette.

[P217]
“That bastard’s really working hard…”

[P218]
Soon, Jin Taekyung disappeared from sight. Seong Jinho stubbed out his cigarette in a flowerpot and was about to leave when the junk capsule caught his eye.

[P219]
*He said the manufacturer was H Soft, right?*

[P220]
It was probably just some half-assed prank, but there was no harm in looking into it.

[P221]
[^1]: Korean mock exams use a 1–9 scale; Grade 1 is the highest.
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 40,
  "passed": true,
  "metrics": {
    "source_characters": 6138,
    "translation_characters": 13155,
    "length_ratio": 2.143,
    "source_paragraphs": 214,
    "translation_paragraphs": 221
  },
  "errors": [],
  "warnings": [
    {
      "code": "numbers",
      "message": "Arabic numerals from the source are absent",
      "details": {
        "values": [
          "70"
        ]
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
