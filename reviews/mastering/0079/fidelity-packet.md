# Fidelity Gate — Chapter 79

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
  1|＃79화
  2|
  3|
  4|
  5|나는 은은한 두통과 함께 눈을 떴다. 주위를 둘러보니 낯선 공간이다. 널찍하고 깨끗한 호텔 방.
  6|
  7|그제야 간밤의 기억이 새록새록 떠올랐다.
  8|
  9|‘아, 맞다. 2차로 호텔 가서 샴페인 파티 했지.’
 10|
 11|세상에, 호텔에서 샴페인 파티라니.
 12|
 13|이렇게 말하니까 무슨 재벌 3세가 된 기분이다. 아니, 최 팀장 정도면 진짜 재벌 3세일 수도 있겠다.
 14|
 15|“크허어어업. 크헙!”
 16|
 17|“…….”
 18|
 19|저 아저씨는 진짜 산적이고.
 20|
 21|무슨 코골이가 소리 지르는 것 같냐. 진호 형도 한 코골이 하는데 저 양반 앞에서는 음소거 수준이다.
 22|
 23|내가 호텔 지배인이면 진작 내쫓았을…….
 24|
 25|똑똑.
 26|
 27|“누구세요?”
 28|
 29|순간 강제 퇴실을 통보하러 온 호텔 직원인가 싶었지만 아니었다. 문 너머로 맑고 시원시원한 목소리가 들려왔다.
 30|
 31|“저예요. 송송이.”
 32|
 33|잠깐만. 누구?
 34|
 35|“자, 잠시만요!”
 36|
 37|나는 빛의 속도로 뛰어가 문을 열었다. 그전에 룸에 비치된 향수를 뿌리고 옷매무새를 점검하는 것도 잊지 않았다.
 38|
 39|달칵.
 40|
 41|나를 물끄러미 쳐다보는 송이 씨의 호수 같은 눈동자에 가슴이 쿵쾅거린다. 간신히 떨리는 목소리를 끄집어냈다.
 42|
 43|“아, 안녕히 주무셨어요?”
 44|
 45|“아니요. 코 고는 소리 때문에 잠을 설쳐서.”
 46|
 47|“아.”
 48|
 49|시작부터 좋지 않다. 나는 지금도 맹렬하게 코골이 중인 임꺽정을 원망하며 화제를 돌렸다.
 50|
 51|“그런데 어쩐 일로 오셨어요?”
 52|
 53|“아침 먹을 시간이잖아요.”
 54|
 55|“……식사 말입니까?”
 56|
 57|송이 씨가 뭐 잘못됐냐는 눈빛으로 말했다.
 58|
 59|“네. 왜요?”
 60|
 61|왜긴. 좋아서 그러지.
 62|
 63|살다 살다 여자랑 단둘이 아침을 먹는 날이 올 줄이야. 심지어 그 여자가 내 이상형이기까지 하다. 왠지 안구가 촉촉해져 오는 것만 같다.
 64|
 65|‘드디어 내 사막 같은 인생에 오아시스가 찾아왔구나.’
 66|
 67|그녀와 함께라면 아침으로 전투식량을 먹어도 상관없다. 나는 결연하게 대답했다.
 68|
 69|“지금 당장 준비하겠습니다.”
 70|
 71|“그럼 꺽정 아저씨부터 깨워 줄래요?”
 72|
 73|“……꺽정 형님은 왜요?”
 74|
 75|“톡 안 보셨어요?”
 76|
 77|송이 씨가 자신의 스마트폰을 내밀었다.
 78|
 79|화면에는 지난밤 만들었던 길드 단체 채팅방이 띄워져 있었다.
 80|
 81|
 82|
 83|〈 평화 길드
 84|
 85|
 86|
 87|최 팀장님
 88|
 89|다들 일어나셨습니까?
 90|
 91|김 집사님
 92|
 93|전 일어났습니다.
 94|
 95|송송이
 96|
 97|저도 일어났어요.
 98|
 99|최 팀장님
100|
101|다른 두 분은요?
102|
103|송송이
104|
105|코 고는 중.
106|
107|최 팀장님
108|
109|……깨워서 1층 레스토랑으로 와 주세요.
110|
111|
112|
113|“…….”
114|
115|젠장. 좋다 말았네. 내 인생이 이렇지 뭐.
116|
117|시무룩해진 나를 두고 송이 씨가 돌아섰다.
118|
119|“그럼 전 먼저 내려갈게요.”
120|
121|나는 사뿐거리는 발걸음으로 떠나는 그녀의 뒷모습을 하염없이 바라보았다.
122|
123|“뒷모습도 예쁘네.”
124|
125|“크헙, 크허어어업!”
126|
127|“…….”
128|
129|저 아저씨 진짜 산적 출신 아니야?
130|
131|
132|
133|* * *
134|
135|
136|
137|임꺽정을 겨우 깨워서 1층으로 내려갔다.
138|
139|창가 자리에 앉아 있던 최 팀장이 손을 흔들어 알은척했다.
140|
141|“미리 시켰습니다. 식기 전에 드세요.”
142|
143|호텔 조식이라고 해서 양도 더럽게 적은 파스타 같은 게 나오진 않을까 생각했는데, 테이블에 올라온 것은 뜨끈한 해장국이었다.
144|
145|“크, 역시 최 팀장!”
146|
147|“팀장님이 뭘 좀 아시네요.”
148|
149|아직 숙취가 남아 있었는데 해장국 한 그릇이면 운기조식도 필요 없겠다.
150|
151|나와 임꺽정의 반응에 최 팀장이 고개를 저었다.
152|
153|“송이 씨가 시킨 겁니다. 전 파스타 먹고 싶었는데.”
154|
155|“송이 씨가요?”
156|
157|“네.”
158|
159|표정이 어두운 걸 보니 어지간히 먹고 싶었나 보다.
160|
161|그나저나 송이 씨가 해장국이라니. 외모만 보면 애지중지 자란 부잣집 아가씨 같은데 어제 보여 준 모습도 그렇고, 의외로 털털한 구석이 있다.
162|
163|후루룩.
164|
165|“크으, 좋다. 다들 뭐 해요? 국물 뜨끈할 때 먹어야죠.”
166|
167|야무지게 해장국을 먹는 송이 씨를 보고 있자니 가슴 한구석이 뜨끈해진다. 먹는 것도 참 복스럽다.
168|
169|‘보기만 해도 배가 부르다는 게 이런 거였구나.’
170|
171|그렇게 밥이 코로 들어가는지, 입으로 들어가는지도 헷갈리는 상태에서 식사가 마무리됐다. 나를 뺀 다른 사람들이 포만감에 늘어져 있을 때 최 팀장이 말했다.
172|
173|“식사도 했으니 이제 자리를 옮길까요?”
174|
175|뭐야, 이제 집 가서 쉬는 분위기 아니었어?
176|
177|“무슨 자리요?”
178|
179|내 말에 임꺽정이 빵빵한 배를 두드리며 끼어들었다.
180|
181|“어디긴, 어제에 이어서 또 달려야지. 오늘은 막걸리 어때? 내가 잘하는 집 알아.”
182|
183|“아, 저도 막걸리 참 좋아하는데.”
184|
185|우리의 대화를 가만히 듣고 있던 김 집사가 빙긋 웃으며 말을 이었다.
186|
187|“아쉽지만 거긴 다음 회식 때 가는 게 좋겠습니다. 오늘은 더 중요한 일이 있으니까요.”
188|
189|길드장은 김 집사지만 결정을 내리는 사람은 따로 있다.
190|
191|사람들의 시선 속에서 최 팀장이 입을 열었다.
192|
193|“먹고 마시고 쉬었으니 이제 일해야죠.”
194|
195|평화 길드의 첫 레이드다.
196|
197|
198|
199|* * *
200|
201|
202|
203|대격변을 맞이한 인류는 경악했다.
204|
205|어느 날 예고 없이 생성된 게이트, 그리고 그곳에서 쏟아지는 정체불명의 생물체들.
206|
207|- 저, 저게 뭐야?
208|
209|- 괴물, 괴물이다!
210|
211|차라리 팔다리가 가늘고 머리가 큰 외계인이 쳐들어왔다면 덜 놀랐을 거다. 그러나 놈들은 우주선을 타고 오지도, 총을 쏘지도 않았다.
212|
213|- 취이이익!
214|
215|- 카룩! 크루루룩!
216|
217|끔찍한 악취와 살기로 번들거리는 눈. 인간을 종잇장처럼 찢어 죽이는 괴물들이 도시를 휩쓸고 불태웠다.
218|
219|소설에서, 영화에서, 혹은 신화 속에서나 나올 법한 괴물들.
220|
221|미노타우로스(Minotaurus)도 그중 하나였다……고 역사 시간에 배웠다.
222|
223|“미노타우로스 아시죠?”
224|
225|최 팀장의 물음에 임꺽정이 자랑스럽게 대답했다.
226|
227|“그럼. 나 초등학생 때 그리스 로마 신화 만화로 봤지. 되게 멋있었는데, 근육 빵빵하고.”
228|
229|“……태경 씨는요?”
230|
231|“구경도 못 해 봤는데요.”
232|
233|미노타우로스는 B급 몬스터 중에서도 제법 상위에 속하는 놈이다. 만년 F급이었던 나와는 오백 광년쯤 거리가 있었지.
234|
235|“괜찮습니다. 이참에 구경해 보면 되죠.”
236|
237|“…….”
238|
239|게이트가 무슨 동물원이야? 가서 구경만 하게?
240|
241|자기 일 아니라고 시원하게 대꾸한 최 팀장이 태블릿을 건넸다.
242|
243|“자요.”
244|
245|“이게 뭡니까?”
246|
247|“C급 마정석으로 작동하는 차세대 태블릿입니다. 유려한 디자인과 뛰어난 성능으로 소수의 VIP에게만 한정 판매 되는…….”
248|
249|“결론만.”
250|
251|“레이드 영상 넣어 놨습니다. 보세요.”
252|
253|진작 그렇게 말할 것이지. 나와 임꺽정은 머리를 맞대고 태블릿에 저장된 영상을 감상했다.
254|
255|- 자, 차분하게 해. 차분하게. 특히 탱커들! 실드 바짝 들어라. 이거 뚫리면 여기 있는 사람들 다 뒈진다. 물론 그전에 너흰 나한테 뒈지고.
256|
257|- 옙!
258|
259|열댓 명의 헌터들이 레이드 팀장의 지시에 따라 일사불란하게 대형을 갖춘다. 다들 긴장한 기색이 역력하다.
260|
261|‘탱커 넷에 근거리, 원거리 딜러들. 마법사도 있고 힐러까지.’
262|
263|팀웍도 괜찮고, 팀 구성도 괜찮다.
264|
265|그리고…….
266|
267|‘저게 미노타우로스군.’
268|
269|몬스터 백과사전에서나 보던 B급 몬스터가 모습을 드러냈다.
270|
271|- 음모오오.
272|
273|소의 머리에 인간의 몸. 반인반수(半人半獸)의 미노타우로스 일곱 마리가 침입자들을 향해 다가간다.
274|
275|아니, 돌격했다.
276|
277|- 모오오오오!
278|
279|놈들이 울부짖는 소리가 동굴을 울렸다. 떨림 때문에 투두둑 떨어지는 돌가루 아래, 전투가 시작됐다.
280|
281|- 원거리! 쏴!
282|
283|레이드 팀장이 목이 터져라 외쳤다. 동시에 마나를 머금은 이십여 발의 화살이 선두에 선 미노타우로스의 머리에 꽂혔다.
284|
285|퓨퓨퓩!
286|
287|광범위한 공격 대신 한 놈에게 일점사를 가한 것은 좋은 선택이었다. 특히 머리를 정확히 노리고 쏜 것이 주효했다.
288|
289|제아무리 B급 몬스터라 한들 눈동자까지 강화할 수는 없으니까.
290|
291|- 모오오!
292|
293|제 얼굴을 할퀴며 괴로워하던 놈의 최후를 장식한 것은 뒤따르던 동료들이었다.
294|
295|퍼걱!
296|
297|거무튀튀한 쇠몽둥이가 소 대가리를 터트렸다. 그리고.
298|
299|쿵쿵쿵!
300|
301|‘허.’
302|
303|죽은 놈의 시체를 방패로 삼고 그대로 내달린다. 화살이며 마법이 날아들었지만 시체만 걸레짝으로 만들 뿐, 뒤에 숨은 미노타우로스들은 멀쩡했다.
304|
305|‘이놈들…….’
306|
307|제법 머리를 쓸 줄 안다. 최소한 고블린만큼 지능이 뛰어나고, 고블린보다는 수십 배 강한 놈들이다.
308|
309|그래서 더 위험하다.
310|
311|- 버텨!
312|
313|- 으하압!
314|
315|팀장의 외침에 탱커들의 핏줄이 불뚝 섰다. 희뿌연 마나가 어린 방패로 거력이 담긴 쇠몽둥이를 막아 낸다.
316|
317|퍼버벅!
318|
319|그 사이로 자그마한 그림자 하나가 허공에서 뚝 떨어졌다. ‘은신’ 계열의 헌터인 그는 또 다른 미노타우로스의 눈알에 검게 칠한 단검을 쑤셔 박고 사라졌다.
320|
321|- 모오오…….
322|
323|B급 몬스터는 무적이 아니다. 다른 근접 딜러들과 궁수, 마법사의 원조까지 더해지니 눈 깜짝할 사이에 두 마리가 더 쓰러졌다.
324|
325|하지만 위기는 빠르게 찾아왔다.
326|
327|‘뚫린다!’
328|
329|생각이 들기가 무섭게 위태위태하던 탱커 라인이 허물어졌다.
330|
331|콰과광!
332|
333|- 크아아악!
334|
335|- 힐러, 힐러!
336|
337|비명과 괴성이 난무한다. 피어나는 먼지 너머로 대형을 헤집으며 쇠몽둥이를 휘두르는 소 대가리들이 보였다.
338|
339|- 음모오오!
340|
341|- 탱커, 딜러! 원거리 마나 아끼지 말고 쏟아부어! 원거리는 거리 벌려!
342|
343|퍼버버벅!
344|
345|- 음모오오오오!
346|
347|- 힐러어어어!
348|
349|영상은 10분 남짓 이어지다가 끊겼다. 전투가 완전히 끝난 건 아니고, 카메라가 쇠몽둥이에 박살 났기 때문이다.
350|
351|- 음모오오오오!
352|
353|치지지직.
354|
355|미노타우로스의 포효와 함께 화면이 흑백으로 물든다. 임꺽정이 침을 꿀꺽 삼켰다.
356|
357|“……이거 장난 아닌데.”
358|
359|당연하지, 이 양반아.
360|
361|나는 태블릿을 최 팀장에게 넘겨주며 물었다.
362|
363|“어느 길드예요?”
364|
365|“지난주에 있었던 부천터미널 길드의 레이드 영상입니다.”
366|
367|“…….”
368|
369|거, 누가 지었는지 작명 센스 한번 끝내주네. 평화 길드에 들어온 입장으로서 할 말은 아니지만 부천터미널 길드보다는 낫다.
370|
371|“결과는요?”
372|
373|“미노타우로스는 전멸. 헌터는 두 명이 죽었습니다.”
374|
375|레이드 중 사망하는 일은 그리 드문 일이 아니다. 헌터는 죽음에 가까워졌다 도망치기를 반복하는 직업이니까.
376|
377|그런데도 마음이 무거워지는 것은 어쩔 수 없다. 살아남은 자들이 평생 짊어져야 하는 무게다.
378|
379|지금의 나처럼.
380|
381|“그렇군요.”
382|
383|내가 할 수 있는 말은 이 정도가 고작이었다. 스마트폰을 꺼내어 검색해 보니 관련된 인터넷 기사가 몇 개 떴다.
384|
385|
386|
387|[부천 모 길드. 무리한 레이드가 불러온 희생]
388|
389|지난 16일 C급 헌터 이 모 씨, 박 모 씨가 B급 게이트 ‘미노타우로스의 미로’에서 사망했다. 헌터 협회 당국은…….
390|
391|
392|
393|사망자들이 C급 헌터였구나. 하긴 저 정도 중소 길드에서 B급 헌터들로 열댓 명을 꽉꽉 채워 보낼 만한 인재 풀이 될 리가 없지.
394|
395|‘그럼…….’
396|
397|나는 빠르게 길드원들을 훑었다. 그보다 한발 먼저 끌어 올린 [기감]이 그들의 레벨창을 띄운 후였다.
398|
399|띠링. 띠링. 띠링.
400|
401|
402|
403|[Lv.75 최민우]
404|
405|[Lv.80 김화종]
406|
407|[Lv.64 송송이]
408|
409|
410|
411|그리고 다음 순간, 임꺽정과 눈이 딱 마주쳤다.
412|
413|“왜 그래?”
414|
415|“별것 아니에요.”
416|
417|애써 아무렇지 않게 대답하고 고개를 돌렸지만 속마음은 그게 아니었다.
418|
419|
420|
421|[Lv.24 임혁준]
422|
423|
424|
425|이 레이드, 위험하다.
```

## Assembled English

```markdown
[P1]
# Chapter 79

[P2]
I woke with a dull headache and looked around. I was in an unfamiliar place—a spacious, clean hotel room.

[P3]
Only then did the memories of last night gradually come back to me.

[P4]
*Right. We came to a hotel for the second round and had a champagne party.*

[P5]
Good God. A champagne party at a hotel.

[P6]
Put that way, I felt like I’d become the third-generation heir to some chaebol family. Then again, Team Leader Choi might actually be one.

[P7]
“Khrrr-heeeurk. Khrrp!”

[P8]
“……”

[P9]
That man really was a bandit.

[P10]
What kind of snoring sounded like someone shouting? Jinho hyung was a champion snorer himself, but next to this guy, he might as well have been on mute.

[P11]
*If I were the hotel manager, I would’ve kicked him out long ago—*

[P12]
Knock, knock.

[P13]
“Who is it?”

[P14]
For a moment, I thought a hotel employee had come to inform us that we were being thrown out. But no. A clear, bright voice came from the other side of the door.

[P15]
“It’s me. Song Song.”

[P16]
*Wait. Who?*

[P17]
“J-just a moment!”

[P18]
I dashed to the door at the speed of light. Before opening it, I made sure to spray on some of the perfume provided in the room and straighten my clothes.

[P19]
Click.

[P20]
Miss Song-i’s clear, lake-like eyes gazed steadily at me, setting my heart pounding. I barely managed to squeeze out a greeting in a trembling voice.

[P21]
“G-good morning. Did you sleep well?”

[P22]
“No. The snoring kept waking me up.”

[P23]
“Oh.”

[P24]
Not a good start. I blamed Im Kkeokjeong, who was still snoring ferociously, and quickly changed the subject.

[P25]
“But what brings you here?”

[P26]
“It’s time for breakfast.”

[P27]
“……Breakfast?”

[P28]
Miss Song looked at me as if she couldn’t see what the problem was.

[P29]
“Yes. Why?”

[P30]
*Why? Because I’m happy.*

[P31]
Who would’ve thought I’d live to see the day I had breakfast alone with a woman? And not just any woman—one who was exactly my type. I could almost feel my eyes welling up.

[P32]
*At last, an oasis has appeared in my desert of a life.*

[P33]
I wouldn’t have minded eating combat rations for breakfast as long as I was eating them with her. I answered with determination.

[P34]
“I’ll get ready right now.”

[P35]
“Then could you wake Uncle Kkeokjeong first?”

[P36]
“……Why Kkeokjeong Hyung-nim?”

[P37]
“Didn’t you check the chat?”

[P38]
Miss Song held out her smartphone.

[P39]
The Guild group chat we had created last night was open on the screen.

[P40]
> **Peace Guild**
>
> **Team Leader Choi**  
> Is everyone awake?
>
> **Butler Kim**  
> I’m up.
>
> **Song Song**  
> I’m up too.
>
> **Team Leader Choi**  
> What about the other two?
>
> **Song Song**  
> They’re snoring.
>
> **Team Leader Choi**  
> ……Wake them up and come to the restaurant on the first floor.

[P41]
“……”

[P42]
Damn it. And just when I was getting excited. Story of my life.

[P43]
Leaving me there dejected, Miss Song turned away.

[P44]
“Then I’ll go down first.”

[P45]
I stared longingly at her retreating back as she walked away on light, graceful steps.

[P46]
“Even her back is pretty.”

[P47]
“Khrrp, khrrr-heeeurk!”

[P48]
“……”

[P49]
*Is this guy really not a former bandit?*

[P50]
* * *

[P51]
After barely managing to wake Im Kkeokjeong, I headed down to the first floor with him.

[P52]
Team Leader Choi was sitting by the window. He waved when he saw us.

[P53]
“I ordered ahead. Eat before it gets cold.”

[P54]
Since it was a hotel breakfast, I had expected something like an absurdly tiny serving of pasta. Instead, a steaming bowl of haejangguk sat on the table.[^1]

[P55]
“Ah, now that’s Team Leader Choi!”

[P56]
“You really know your stuff, Team Leader.”

[P57]
I still had some of last night’s hangover left, but one bowl of haejangguk seemed like it would make circulating my qi unnecessary.

[P58]
Team Leader Choi shook his head at our reactions.

[P59]
“Miss Song ordered it. I wanted pasta.”

[P60]
“Miss Song did?”

[P61]
“Yes.”

[P62]
Judging by his dark expression, he must have really wanted that pasta.

[P63]
Still, I never would’ve expected Miss Song to order hangover soup. Judging by her appearance, she looked like a pampered young lady from a wealthy family. But after what she had shown us yesterday, and now this, she had a surprisingly down-to-earth side.

[P64]
Slurp.

[P65]
“Ah, that hits the spot. What are you all doing? You should eat while the broth’s still hot.”

[P66]
Watching Miss Song dig into her haejangguk warmed a corner of my heart. Even the way she ate was delightful.

[P67]
*So this is what it means when simply looking at someone fills you up.*

[P68]
In a state where I could no longer tell whether the food was going into my nose or my mouth, the meal finally came to an end. While everyone except me sagged back in their seats, bloated with food, Team Leader Choi spoke.

[P69]
“Now that we’ve eaten, shall we move somewhere else?”

[P70]
What? Wasn’t this supposed to be the part where we went home and rested?

[P71]
“Move where?”

[P72]
Im Kkeokjeong cut in, patting his bulging belly.

[P73]
“Where else? We’ve got to keep the party going from yesterday. How about makgeolli today?[^2] I know a good place.”

[P74]
“Oh, I really like makgeolli too.”

[P75]
Butler Kim, who had been quietly listening to us, smiled and continued.

[P76]
“Unfortunately, I think we’d better save that for our next Guild dinner. We have something more important to take care of today.”

[P77]
Butler Kim might have been the Guild Master, but someone else made the decisions.

[P78]
With everyone’s eyes on him, Team Leader Choi opened his mouth.

[P79]
“We’ve eaten, drunk, and rested. Now it’s time to work.”

[P80]
It was the Peace Guild’s first raid.

[P81]
* * *

[P82]
The Great Cataclysm left humanity reeling in shock.

[P83]
Gates appeared without warning one day, and unknown creatures came pouring out of them.

[P84]
“W-what is that?”

[P85]
“A monster! It’s a monster!”

[P86]
People might have been less shocked if aliens with thin limbs and oversized heads had invaded instead. But these creatures hadn’t arrived in spaceships, nor did they fire guns.

[P87]
“Skreeee!”

[P88]
“Karuk! Krrruuuk!”

[P89]
With their terrible stench and eyes gleaming with killing intent, the monsters tore humans apart like sheets of paper as they swept through cities and set them ablaze.

[P90]
They were monsters that seemed as if they belonged in novels, movies, or myths.

[P91]
The Minotaur was one of them……or so I had learned in history class.

[P92]
“You know what a Minotaur is, right?”

[P93]
Im Kkeokjeong answered proudly.

[P94]
“Of course. I saw them in a Greek and Roman mythology comic when I was in elementary school. They were pretty cool—huge muscles and everything.”

[P95]
“……What about you, Taekyung?”

[P96]
“I’ve never even seen one.”

[P97]
A Minotaur was among the stronger monsters in the B-rank category. It had been roughly five hundred light-years away from me, an eternal F-rank Hunter.

[P98]
“That’s all right. This is your chance to see one.”

[P99]
“……”

[P100]
*Is a Gate a zoo? Are we going there just to sightsee?*

[P101]
Team Leader Choi answered breezily, as if this had nothing to do with him, and handed me a tablet.

[P102]
“Here.”

[P103]
“What is this?”

[P104]
“It’s a next-generation tablet powered by a C-rank Magic Gem. With its elegant design and outstanding performance, it’s sold exclusively to a select number of VIPs……”

[P105]
“Just give me the conclusion.”

[P106]
“I loaded some raid footage onto it. Watch.”

[P107]
He could’ve just said that from the start. Im Kkeokjeong and I put our heads together and watched the video stored on the tablet.

[P108]
“All right, stay calm. Stay calm. Especially the tanks! Keep those shields up. If they break through, everyone here is dead. Of course, I’ll kill you myself before that happens.”

[P109]
“Yes, sir!”

[P110]
Around fifteen Hunters formed an orderly formation at the raid leader’s command. Every one of them was visibly tense.

[P111]
*Four tanks, melee and ranged damage dealers. They’ve even got a mage and a healer.*

[P112]
Their teamwork seemed decent, and so did the team composition.

[P113]
And then……

[P114]
*So that’s a Minotaur.*

[P115]
A B-rank monster I had only ever seen in monster encyclopedias appeared on the screen.

[P116]
“Moooooo!”

[P117]
A cow’s head on a human body. Seven half-human, half-beast Minotaurs advanced toward the intruders.

[P118]
No—they charged.

[P119]
“Mooooooo!”

[P120]
Their bellowing echoed through the cave. Rock dust shook loose and fell in little showers as the battle began.

[P121]
“Ranged! Fire!”

[P122]
The raid leader screamed himself hoarse. At the same moment, around twenty mana-infused arrows struck the lead Minotaur in the head.

[P123]
Fwish-fwish-fwish!

[P124]
Focusing fire on one target instead of using a wide-area attack had been a good choice. Aiming precisely for its head had been especially effective.

[P125]
No matter how strong a B-rank monster was, it couldn’t reinforce its eyeballs.

[P126]
The Minotaur clawed at its own face in agony. The finishing blow came from the companions following behind it.

[P127]
Crunch!

[P128]
A dark iron club smashed the cow’s head apart.

[P129]
And then—

[P130]
Thud, thud, thud!

[P131]
*Huh.*

[P132]
They used the dead Minotaur’s corpse as a shield and charged straight ahead. Arrows and magic rained down, but they only shredded the corpse. The Minotaurs hiding behind it were unharmed.

[P133]
*These bastards……*

[P134]
They knew how to use their heads. They were at least as intelligent as goblins and dozens of times stronger.

[P135]
That made them all the more dangerous.

[P136]
“Hold!”

[P137]
“Urrrgh!”

[P138]
At the team leader’s shout, the tanks’ veins bulged. Their shields, covered in hazy mana, blocked the iron clubs carrying tremendous force.

[P139]
Wham! Wham! Wham!

[P140]
A small shadow suddenly dropped out of the air between them. A stealth-type Hunter drove a black-painted dagger into another Minotaur’s eye, then vanished.

[P141]
“Moooo……”

[P142]
B-rank monsters weren’t invincible. With support from the other melee damage dealers, archers, and mage, two more Minotaurs fell in the blink of an eye.

[P143]
But the crisis came quickly.

[P144]
*They’re breaking through!*

[P145]
No sooner had the thought occurred to me than the wavering tank line collapsed.

[P146]
Kra-koom!

[P147]
“Graaagh!”

[P148]
“Healer! Healer!”

[P149]
Screams and roars filled the cave. Through the billowing dust, I could see the cow-headed monsters tearing through the formation and swinging their iron clubs.

[P150]
“Moooooo!”

[P151]
“Tanks, damage dealers! Ranged, don’t hold back your mana—pour it all in! Ranged, open up some distance!”

[P152]
Wham-wham-wham!

[P153]
“Mooooooo!”

[P154]
“Healeeeer!”

[P155]
The video continued for about ten minutes before cutting off. The battle hadn’t ended yet. The camera had simply been smashed by an iron club.

[P156]
“Mooooooo!”

[P157]
Bzzzt.

[P158]
As the Minotaur’s roar rang out, the screen filled with static and faded to black and white. Im Kkeokjeong swallowed hard.

[P159]
“……This is no joke.”

[P160]
*Of course it isn’t, old man.*

[P161]
I handed the tablet back to Team Leader Choi and asked,

[P162]
“What Guild was that?”

[P163]
“It was footage of the Bucheon Terminal Guild’s raid last week.”

[P164]
“……”

[P165]
*Whoever named that Guild had one hell of a sense for names.*

[P166]
Not that I had much room to talk as a member of the Peace Guild, but at least our name was better than Bucheon Terminal Guild.

[P167]
“What was the result?”

[P168]
“The Minotaurs were wiped out. Two Hunters died.”

[P169]
People dying during raids wasn’t particularly rare. Being a Hunter meant repeatedly drawing close to death, then running away from it.

[P170]
Even so, I couldn’t help feeling heavy-hearted. It was a burden the survivors would have to carry for the rest of their lives.

[P171]
Just as I did now.

[P172]
“I see.”

[P173]
That was all I could manage. I pulled out my smartphone and searched for the incident. Several related articles appeared.

[P174]
> **A Bucheon Guild: The Sacrifice Brought on by a Reckless Raid**
>
> On the sixteenth, C-rank Hunters identified as Mr. Lee and Mr. Park died in the B-rank Gate *The Minotaur’s Labyrinth*. The Hunter Association authorities……

[P175]
So the Hunters who died had been C-rank. That made sense. A small-to-medium Guild like that couldn’t possibly have enough talent to fill all fifteen or so spots on a raid team with B-rank Hunters.

[P176]
*Then……*

[P177]
I quickly looked over the Guild members. The Qi Sense I had activated a moment earlier had already brought up their Level windows.

[P178]
Ding. Ding. Ding.

[P179]
> **System**
>
> **Level 75 — Choi Minwoo**
>
> **Level 80 — Kim Hwajong**
>
> **Level 64 — Song Song**

[P180]
The next moment, my eyes met Im Kkeokjeong’s.

[P181]
“What’s wrong?”

[P182]
“It’s nothing.”

[P183]
I answered as casually as I could and turned away, but my thoughts were anything but casual.

[P184]
> **System**
>
> **Level 24 — Im Hyeokjun**

[P185]
*This raid is dangerous.*

[P186]
[^1]: Haejangguk, literally “hangover soup,” is a Korean soup traditionally eaten after drinking to help ease a hangover.

[P187]
[^2]: Makgeolli is a traditional Korean rice wine with a milky appearance and a mildly sweet, tangy flavor.
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
# Chapter 79

[P2]
I woke with a dull headache and looked around. I was in an unfamiliar place—a spacious, clean hotel room.

[P3]
Only then did the memories of last night gradually come back to me.

[P4]
*Right. We went to a hotel for the second round and had a champagne party.*

[P5]
Good God, a champagne party at a hotel.

[P6]
Put that way, it made me feel like I had become the third-generation heir to some chaebol family. Though, come to think of it, Team Leader Choi might actually be one.

[P7]
“Khrrr-heeeurk. Khrrp!”

[P8]
“……”

[P9]
That man really was a bandit.

[P10]
What kind of snore sounded like someone shouting? Hyung Jinho snored pretty loudly too, but next to this guy, it was practically on mute.

[P11]
*If I were the hotel manager, I would’ve kicked him out long ago—*

[P12]
Knock, knock.

[P13]
“Who is it?”

[P14]
For a moment, I thought it was a hotel employee coming to inform us of our forced eviction. But it wasn’t. A clear, refreshing voice came from the other side of the door.

[P15]
“It’s me. Song Song.”

[P16]
*Wait. Who?*

[P17]
“J-just a moment!”

[P18]
I dashed to the door at the speed of light. Before opening it, I didn’t forget to spray on some of the perfume provided in the room and check my clothes.

[P19]
Click.

[P20]
My heart pounded when I looked into Miss Song’s limpid, lake-like eyes. I somehow managed to squeeze out a trembling voice.

[P21]
“G-good morning. Did you sleep well?”

[P22]
“No. I kept waking up because of the snoring.”

[P23]
“Oh.”

[P24]
Not a good start. I blamed Im Kkeokjeong, who was still snoring ferociously, and quickly changed the subject.

[P25]
“But what brings you here?”

[P26]
“It’s time for breakfast.”

[P27]
“……Breakfast?”

[P28]
Miss Song looked at me as if something were wrong.

[P29]
“Yes. Why?”

[P30]
*Why? Because I’m happy.*

[P31]
Who would’ve thought I’d live to see the day I had breakfast alone with a woman? And not just any woman—she was exactly my type. I felt as if my eyes were growing moist.

[P32]
*At last, an oasis has appeared in my desert of a life.*

[P33]
I wouldn’t have minded eating combat rations for breakfast if I could eat them with her. I answered with determination.

[P34]
“I’ll get ready right now.”

[P35]
“Then could you wake Uncle Kkeokjeong first?”

[P36]
“……Why Kkeokjeong Hyung-nim?”

[P37]
“Didn’t you check the chat?”

[P38]
Miss Song held out her smartphone.

[P39]
The group chat we had created for the Guild last night was open on the screen.

[P40]
> **Peace Guild**
>
> **Team Leader Choi**  
> Is everyone awake?
>
> **Butler Kim**  
> I’m up.
>
> **Song Song**  
> I’m up too.
>
> **Team Leader Choi**  
> What about the other two?
>
> **Song Song**  
> They’re snoring.
>
> **Team Leader Choi**  
> ……Wake them up and come to the restaurant on the first floor.

[P41]
“……”

[P42]
Damn it. And just when I was getting excited. That was my life for you.

[P43]
Miss Song turned away, leaving me looking dejected.

[P44]
“Then I’ll go down first.”

[P45]
I stared longingly at her retreating back as she walked away on light, graceful steps.

[P46]
“Even her back is pretty.”

[P47]
“Khrrp, khrrr-heeeurk!”

[P48]
“……”

[P49]
*Is this guy really not a former bandit?*

[P50]
* * *

[P51]
I barely managed to wake Im Kkeokjeong before heading down to the first floor.

[P52]
Team Leader Choi, who was sitting by the window, waved when he saw us.

[P53]
“I ordered ahead. Eat before it gets cold.”

[P54]
Since it was a hotel breakfast, I had expected something like an absurdly tiny serving of pasta. But what arrived on the table was a steaming bowl of haejangguk.[^1]

[P55]
“Ah, now that’s Team Leader Choi!”

[P56]
“You really know what you’re doing, Team Leader.”

[P57]
I still had some of last night’s hangover left, but one bowl of haejangguk seemed like it would make circulating my qi unnecessary.

[P58]
Team Leader Choi shook his head at our reactions.

[P59]
“Miss Song ordered it. I wanted pasta.”

[P60]
“Miss Song did?”

[P61]
“Yes.”

[P62]
His dark expression suggested that he had really wanted it.

[P63]
Still, I never would’ve expected Miss Song to order hangover soup. Judging by her appearance, she looked like a pampered young lady from a wealthy family. But after what she had shown us yesterday, and now this, she had a surprisingly down-to-earth side.

[P64]
Slurp.

[P65]
“Ah, this is good. What are you all doing? You should eat while the broth’s still hot.”

[P66]
Watching Miss Song eat her haejangguk with such gusto warmed a corner of my heart. She had such a healthy appetite.

[P67]
*So this is what it means when simply looking at someone fills you up.*

[P68]
In a state where I could no longer tell whether the food was going into my nose or my mouth, the meal finally came to an end. While everyone except me sagged back in their seats, bloated with food, Team Leader Choi spoke.

[P69]
“Now that we’ve eaten, shall we move somewhere else?”

[P70]
What? Wasn’t this supposed to be the part where we went home and rested?

[P71]
“Move where?”

[P72]
Im Kkeokjeong cut in while patting his stuffed belly.

[P73]
“Where else? We’ve got to keep the party going from yesterday. How about makgeolli today?[^2] I know a good place.”

[P74]
“Oh, I really like makgeolli too.”

[P75]
[^2]: Makgeolli is a traditional Korean rice wine with a milky appearance and a mildly sweet, tangy flavor.

[P76]
Butler Kim, who had been quietly listening to us, smiled and continued.

[P77]
“Unfortunately, it would be better to go there for our next Guild dinner. We have something more important to take care of today.”

[P78]
The Guild Master was Butler Kim, but he wasn’t the one who made the decisions.

[P79]
With everyone’s eyes on him, Team Leader Choi opened his mouth.

[P80]
“We’ve eaten, drunk, and rested. Now it’s time to work.”

[P81]
It was the Peace Guild’s first raid.

[P82]
* * *

[P83]
Humanity was thrown into shock by the Great Cataclysm.

[P84]
Gates began appearing without warning one day, and unidentified creatures poured out of them.

[P85]
“W-what is that?”

[P86]
“A monster! It’s a monster!”

[P87]
If aliens with thin limbs and oversized heads had invaded, people might have been less surprised. But these creatures hadn’t come in spaceships, and they didn’t shoot guns.

[P88]
“Skreeee!”

[P89]
“Karuk! Krrruuuk!”

[P90]
With their terrible stench and eyes gleaming with killing intent, the monsters tore humans apart like sheets of paper as they swept through cities and set them ablaze.

[P91]
They were monsters that seemed as if they belonged in novels, movies, or myths.

[P92]
The Minotaur was one of them……or so I had learned in history class.

[P93]
“You know what a Minotaur is, right?”

[P94]
Im Kkeokjeong answered proudly.

[P95]
“Of course. I saw them in a Greek and Roman mythology comic when I was in elementary school. They were pretty cool—huge muscles and everything.”

[P96]
“……What about you, Taekyung?”

[P97]
“I’ve never even seen one.”

[P98]
A Minotaur was among the stronger monsters in the B-rank category. It had been roughly five hundred light-years away from me, an eternal F-rank Hunter.

[P99]
“That’s all right. You can see one now.”

[P100]
“……”

[P101]
*Is a Gate a zoo? Are we going there just to sightsee?*

[P102]
Team Leader Choi handed me a tablet, answering as breezily as if this had nothing to do with him.

[P103]
“Here.”

[P104]
“What is this?”

[P105]
“It’s a next-generation tablet powered by a C-rank Magic Gem. With its elegant design and outstanding performance, it’s sold exclusively to a select number of VIPs……”

[P106]
“Just give me the conclusion.”

[P107]
“I put some raid footage on it. Watch.”

[P108]
He could’ve just said that from the start. Im Kkeokjeong and I put our heads together and watched the video stored on the tablet.

[P109]
“All right, stay calm. Stay calm. Especially the tanks! Keep those shields up. If they break through, everyone here is dead. Of course, I’ll kill you before that happens.”

[P110]
“Yes, sir!”

[P111]
Around fifteen Hunters formed an orderly formation at the raid leader’s command. Every one of them was visibly tense.

[P112]
*Tanks, melee and ranged damage dealers. There’s a mage and even a healer.*

[P113]
Their teamwork seemed decent, and so did the team composition.

[P114]
And then……

[P115]
*So that’s a Minotaur.*

[P116]
A B-rank monster, something I had only ever seen in monster encyclopedias, appeared on the screen.

[P117]
“Moooooo!”

[P118]
A cow’s head on a human body. Seven half-human, half-beast Minotaurs advanced toward the intruders.

[P119]
No—they charged.

[P120]
“Mooooooo!”

[P121]
Their bellowing echoed through the cave. Rock dust shook loose and fell in little showers as the battle began.

[P122]
“Ranged! Fire!”

[P123]
The raid leader screamed himself hoarse. At the same time, around twenty arrows infused with mana struck the head of the lead Minotaur.

[P124]
Fwish-fwish-fwish!

[P125]
Focusing fire on one target instead of using a wide-area attack had been a good choice. Aiming precisely for its head had been especially effective.

[P126]
No matter how strong a B-rank monster was, it couldn’t reinforce its eyeballs.

[P127]
The Minotaur clawed at its own face in agony. The finishing blow came from the companions following behind it.

[P128]
Crunch!

[P129]
A dark iron club smashed the cow’s head apart.

[P130]
And then—

[P131]
Thud, thud, thud!

[P132]
*Huh.*

[P133]
They used the dead Minotaur’s corpse as a shield and charged straight ahead. Arrows and magic rained down, but they only shredded the corpse. The Minotaurs hiding behind it were unharmed.

[P134]
*These bastards……*

[P135]
They knew how to use their heads. They were at least as intelligent as goblins, while being dozens of times stronger.

[P136]
Which made them even more dangerous.

[P137]
“Hold!”

[P138]
“Urrrgh!”

[P139]
At the team leader’s shout, the veins stood out on the tanks’ arms and necks. Their shields, covered in hazy mana, blocked the iron clubs carrying tremendous force.

[P140]
Wham! Wham! Wham!

[P141]
A small shadow suddenly dropped from the air between them. A Hunter from the stealth category drove a blackened dagger into another Minotaur’s eye before disappearing.

[P142]
“Moooo……”

[P143]
B-rank monsters weren’t invincible. With the support of the other melee damage dealers, archers, and mage, two more Minotaurs fell in the blink of an eye.

[P144]
But the crisis came quickly.

[P145]
*They’re breaking through!*

[P146]
No sooner had the thought occurred to me than the wavering tank line collapsed.

[P147]
Kra-koom!

[P148]
“Graaagh!”

[P149]
“Healer! Healer!”

[P150]
Screams and roars filled the cave. Through the clouds of dust, I could see the cow-headed monsters tearing through the formation and swinging their iron clubs.

[P151]
“Moooooo!”

[P152]
“Tanks, damage dealers! Ranged, don’t hold back your mana—pour it all in! Ranged, open up some distance!”

[P153]
Wham-wham-wham!

[P154]
“Mooooooo!”

[P155]
“Healeeeer!”

[P156]
The video continued for about ten minutes before cutting off. The battle hadn’t ended yet. The camera had simply been smashed by an iron club.

[P157]
“Mooooooo!”

[P158]
Bzzzt.

[P159]
As the Minotaur’s roar rang out, the screen filled with static and faded to black and white. Im Kkeokjeong swallowed hard.

[P160]
“……This is no joke.”

[P161]
*Of course it isn’t, old man.*

[P162]
I handed the tablet back to Team Leader Choi and asked,

[P163]
“What Guild was that?”

[P164]
“It was footage of the Bucheon Terminal Guild’s raid last week.”

[P165]
“……”

[P166]
*Whoever named that Guild had some incredible naming sense.*

[P167]
Not that I had any room to talk, considering I belonged to the Peace Guild, but at least our name was better than Bucheon Terminal Guild.

[P168]
“What was the result?”

[P169]
“The Minotaurs were wiped out. Two Hunters died.”

[P170]
People dying during raids wasn’t particularly rare. Being a Hunter meant repeatedly drawing close to death, then running away from it.

[P171]
Even so, I couldn’t help feeling heavy-hearted. It was a burden the survivors would have to carry for the rest of their lives.

[P172]
Just as I did now.

[P173]
“I see.”

[P174]
That was all I could say. I pulled out my smartphone and searched for it. Several related articles appeared.

[P175]
> **A Bucheon Guild: The Sacrifice Brought on by a Reckless Raid**
>
> On the sixteenth, C-rank Hunters identified as Mr. Lee and Mr. Park died in the B-rank Gate *The Minotaur’s Labyrinth*. The Hunter Association authorities……

[P176]
So the people who died had been C-rank Hunters. That made sense. A small-to-medium Guild like that couldn’t possibly have a talent pool large enough to fill a raid team of fifteen B-rank Hunters.

[P177]
*Then……*

[P178]
I quickly looked over the Guild members. The Qi Sense I had activated a moment earlier had already brought up their Level windows.

[P179]
Ding. Ding. Ding.

[P180]
> **System**
>
> **Level 75 — Choi Minwoo**
>
> **Level 80 — Kim Hwajong**
>
> **Level 64 — Song Song**

[P181]
The next moment, my eyes met Im Kkeokjeong’s.

[P182]
“What’s wrong?”

[P183]
“It’s nothing.”

[P184]
I answered as casually as I could and turned away, but my thoughts were anything but casual.

[P185]
> **System**
>
> **Level 24 — Im Hyeokjun**

[P186]
*This raid is dangerous.*

[P187]
[^1]: Haejangguk, literally “hangover soup,” is a Korean soup traditionally eaten after drinking to help ease a hangover.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 김화종    | **Kim Hwajong**   |
| 최민우    | **Choi Minwoo**   |
| 송송이    | **Song Song**     |
| 살기     | **killing intent**                               |                                                       |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 지능               | **Intelligence**               |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 탱커      | **tank**              |
| 힐러      | **healer**            |
| 마법사     | **mage**              |
| 마정석     | **Magic Gem**         |
| 대격변     | **Great Cataclysm**   |
| 임꺽정 | **Im Kkeokjeong** |
| 평화 | **Peace Guild** | Guild name. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 임혁준 | **Im Hyeokjun** | Im Kkeokjeong's personal name, shown in the System Level window. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 아가씨 | **Young Lady** | Former address used for Lee Seowol before she demands the title Sect Leader. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 79,
  "passed": true,
  "metrics": {
    "source_characters": 5426,
    "translation_characters": 12215,
    "length_ratio": 2.251,
    "source_paragraphs": 199,
    "translation_paragraphs": 187
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
        "korean": "지능",
        "preferred": "Intelligence"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "세가",
        "preferred": "great family"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "꺽정",
        "romanization": "kkeokjeong"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "해장국",
        "romanization": "haejangguk"
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
