# Fidelity Gate — Chapter 146

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
  1|＃146화
  2|
  3|
  4|
  5|모든 만남에는 헤어짐이 있는 법.
  6|
  7|눈에 익은 육두마차가 가까이 다가오자 주표가 손바닥만 한 뭔가를 내게 내밀었다.
  8|
  9|“이게 뭡니까?”
 10|
 11|“오늘 만남에 대한 과인의 보답이다.”
 12|
 13|“어이쿠, 뭐 이런 걸 다…….”
 14|
 15|건네받아 자세히 살펴보니 일종의 황금 메달이다.
 16|
 17|표면에 구름과 용이 섬세하게 음각된 그것은 햇빛을 받아 번쩍 빛났다.
 18|
 19|띠링.
 20|
 21|
 22|
 23|- 퀘스트 대상이 오늘의 만남을 매우 흡족해합니다!
 24|
 25|- 퀘스트 보상으로 [상산왕의 증표]를 얻었습니다!
 26|
 27|
 28|
 29|“과인의 증표다. 혹시 따로 원하는 물건이나 소원이 있다면 증표를 들고 찾아오너라. 내 힘이 닿는 데까지 들어줄 터이니.”
 30|
 31|“오.”
 32|
 33|교환 쿠폰이네.
 34|
 35|중국집 쿠폰은 스무 장에 탕수육 대짜인데, 이건 무려 상산왕의 교환 쿠폰이니까 각종 영약이나 보물로 바꿀 수 있을지도 모르겠다.
 36|
 37|‘안 그래도 무기가 하나 필요하긴 한데.’
 38|
 39|열화신단을 흡수한 덕분에 공력은 충분한 상황.
 40|
 41|다만 쓸 만한 창이 없다는 게 아쉽던 차다. 다른 무기들은 처음부터 거의 일회용 젓가락처럼 쓰고 버리는 수준이었으니까.
 42|
 43|‘아예 지금 확 바꿔 버려?’
 44|
 45|순간 고민했지만 이내 고개를 저었다.
 46|
 47|이미 큰 위기는 넘겼다. 급할 것 없는 상황에 왕의 증표를 무기 하나와 교환하기에는 너무 아깝다.
 48|
 49|“감사합니다. 저 이거 되게 갖고 싶었던 건데.”
 50|
 51|허리를 꾸벅 숙이자 주표가 까치발을 들고 내 머리를 쓱쓱 쓰다듬었다.
 52|
 53|“그대가 좋아하니 나도 기쁘다.”
 54|
 55|“…….”
 56|
 57|이거 되게 기분 묘하네. 귀여우니까 봐준다.
 58|
 59|그사이 우리를 데려다줄 마차가 멈춰 섰다. 마차에 오르려는 내게 주표가 손을 흔든다.
 60|
 61|“조심히 가게! 다음에 또 와!”
 62|
 63|다음에는 네가 와야지, 인마.
 64|
 65|새해 첫날, 그러니까 원단(元旦)까지는 고작 보름 남짓 남았다. 아마 그때쯤 어린 왕을 다시 만날 수 있을 것이다.
 66|
 67|“그럼 이만.”
 68|
 69|“다녀오겠습니다, 전하.”
 70|
 71|마차가 워낙 크다 보니 입구도 넓다. 나와 홍진은 나란히 마차에 올랐다.
 72|
 73|“……응?”
 74|
 75|아니, 잠깐만. 너무 자연스러워서 넘어갈 뻔했네.
 76|
 77|나는 황당한 마음을 담아 홍진을 바라봤다.
 78|
 79|“뭡니까?”
 80|
 81|“응? 왜요?”
 82|
 83|“이거 태원진가 가는 마차인데요.”
 84|
 85|“알아요. 그래서 탄 거지.”
 86|
 87|“예?”
 88|
 89|“쇠뿔도 단김에 빼라고. 이참에 진 소가주님과 이야기를 한번 나눠 봐야 하지 않겠어요?”
 90|
 91|빙긋 웃은 홍진이 손가락을 튕기자 관리 한 명이 바람처럼 달려왔다.
 92|
 93|“도지휘동지. 분부하실 일이라도?”
 94|
 95|“선약도 없이 방문하는데 선물이라도 듬뿍 가져가야지. 미리 전령을 보내서 정중히 인사드리는 것도 잊지 말고.”
 96|
 97|“명을 받들겠습니다!”
 98|
 99|이풍도 휘하의 장수에게 지시를 내렸다.
100|
101|“귀빈이시다. 태원진가까지 모셔다드려라.”
102|
103|“충!”
104|
105|두 사람의 명령에 자그마치 백 명에 달하는 병력과 급하게 꾸려진 사절단이 일사불란하게 움직이기 시작한다.
106|
107|그 광경에 뒤따라 오르려던 청풍이 작게 박수를 쳤다.
108|
109|“우와.”
110|
111|그토록 염원하던 근위대 굿즈 세트를 손에 넣은 그는 당분간 태원진가에 머무르기로 했다.
112|
113|이풍이 나를 향해 고개를 까딱 숙였다.
114|
115|“사숙을 부탁드리겠소.”
116|
117|“별말씀을.”
118|
119|그런 말을 굳이 듣지 않아도 이쪽에서 먼저 친하게 지내고 싶은 상대다.
120|
121|청풍을 징검다리 삼아 화산파와의 관계를 돈독히 한다면 태원진가의 앞날도 화창할 게 분명하니까.
122|
123|‘재밌는 놈이기도 하고.’
124|
125|청풍이 해맑게 웃으며 손을 흔들었다.
126|
127|“이풍 사질, 난 걱정하지 말아요! 진 공자랑 같이 있으면 재미있는 일이 자꾸자꾸 생기거든요!”
128|
129|“……혹시 싶어서 말해 두는데, 사고만 치지 마십쇼.”
130|
131|“네!”
132|
133|대답은 잘한다.
134|
135|나는 남아 있는 사람들을 향해 고개를 돌렸다.
136|
137|“너희는 어떻게 하기로 했어?”
138|
139|산서오문의 후기지수들이 우물쭈물 대답했다.
140|
141|“원단이 다가올 때까지 홍화객잔에 묵을 계획입니다.”
142|
143|“본가에 다녀오기에는 워낙 시간이 빡빡하기도 하고…….”
144|
145|“사실 돌아갈 엄두도 안 납니다.”
146|
147|“지금 돌아가면 아버지께서 절 죽이실지도 몰라요.”
148|
149|우울하기 짝이 없는 대답이다.
150|
151|하긴, 지금쯤이면 전날 있었던 일에 대한 소문이 날개 달린 말처럼 퍼져 나가고 있을 테니 그럴 만도 하다.
152|
153|나는 녀석들을 보며 혀를 찼다.
154|
155|“원단까지는 얌전하게 있어라. 문주님들께는 나중에 말 잘해 놓을 테니까.”
156|
157|“저, 정말이십니까?”
158|
159|“그 대신 너희도 각자 잘하고. 무슨 얘긴지 알지?”
160|
161|“성운표국…… 예, 알겠습니다.”
162|
163|이미 대세는 거스를 수 없다. 이제는 이 녀석들도, 산서오문의 문주들도 그 사실을 알 것이다.
164|
165|앞으로는 그저 태원진가의 밑에서 최대한 몸집을 불리는 수밖에.
166|
167|“그래, 그럼 수고들 하고 원단에 보자.”
168|
169|“네?”
170|
171|“왜, 뭐.”
172|
173|“저, 저희도 가는 길인데요.”
174|
175|“어디. 홍화객잔?”
176|
177|“예.”
178|
179|나는 황당해하는 녀석들에게 한마디를 날렸다.
180|
181|“이거 태원진가 급행이야.”
182|
183|쾅!
184|
185|문이 닫히기 무섭게 마차가 움직이기 시작했다.
186|
187|
188|
189|* * *
190|
191|
192|
193|여섯 명이 앉아도 넓었던 내부다. 나와 청풍, 그리고 홍진 세 사람은 각자 몇 자리씩을 차지하고 푹신한 좌석에 몸을 기댔다.
194|
195|“여기서 살아도 될 것 같아요.”
196|
197|행복한 웃음을 띤 청풍이 말을 이었다.
198|
199|“할아버지와 살 때는 풀이나 돌 위에서 잤거든요. 이제는 그렇게 못 살 것 같아요.”
200|
201|문명을 접한 원시인이 따로 없네.
202|
203|그 말에 홍진이 호기심 어린 눈빛으로 물었다.
204|
205|“그럼 공자께서는 줄곧 화산에 살았던 건가요?”
206|
207|“네. 엄청 어릴 때부터요. 하지만 화산에서 태어난 건 아니래요. 예전에 할아버지께 여쭤본 적이 있는데, 화산에 온 건 제가 서너 살 때라고 들었어요.”
208|
209|그렇겠지. 검성이 아무리 엄청난 고수라지만 육아에는 한계가 있기 마련이다.
210|
211|초절정 고수가 된다고 남자 가슴에서 젖이 나오지는 않을 테니까.
212|
213|“…….”
214|
215|아냐, 초절정 고수라면 혹시 몰라.
216|
217|검기, 검강도 쓰는 괴물들인데 젖 정도야 나올 수 있지.
218|
219|나는 호호백발 할아버지가 갓난아기에게 젖을 물리는 장면을 상상해 보았다.
220|
221|“우웩.”
222|
223|“은인, 괜찮으세요?”
224|
225|“진 공자. 괜찮아요?”
226|
227|“괜찮습니다. 잠깐 속이 메슥거린 것뿐이에요.”
228|
229|“어머, 그러면 안 되지. 자, 내 무릎에 누워요.”
230|
231|“…….”
232|
233|확 그냥 무릎을 부숴 버릴까 보다.
234|
235|내가 눈으로 쌍욕을 퍼붓자 홍진이 입을 가리며 웃었다.
236|
237|“호호, 역시 진 공자는 놀리는 재미가 있다니까.”
238|
239|미인이 저런 말을 했다면 나도 따라서 헤헤 웃었을 텐데, 홍진은 명백한 남자다. 얼굴에 하얗게 분을 칠하고 입술에 뭘 발라도 그 사실은 달라지지 않는다.
240|
241|‘내관 출신이라고 했지.’
242|
243|내관이면 내시 아닌가?
244|
245|예전에 듣기로는 내시라고 해서 꼭 고자는 아니라던데. 하지만 홍진이 달린 놈인지 안 달린 놈인지 구분할 방법이 없다.
246|
247|“진 공자.”
248|
249|“예, 예?”
250|
251|“지금 어디 보고 있어요?”
252|
253|“아, 뭐가 묻은 것 같아서 그만.”
254|
255|젠장, 걸렸네.
256|
257|무림인은 아닌데 눈치가 절정 고수 급이다. 홍진의 하체에서 시선을 뗀 나는 황급히 화제를 돌렸다.
258|
259|“그런데 이풍 대협은 어쩌다가 군문에 들어가게 된 겁니까?”
260|
261|“이 첨사? 당연히 무과에 급제해서 들어온 거죠. 그 후로는 쭉 탄탄대로였고.”
262|
263|“역시 화산파 속가제자라 다르긴 하군요.”
264|
265|“영향이 없다고는 말 못 하겠지만 꼭 그런 것만은 아니에요. 고작 십 년 만에 정삼품 도지휘첨사가 된다는 건 정말 어려운 일이거든.”
266|
267|“정삼품이라면……?”
268|
269|“정삼품이 뭐예요? 먹는 건가?”
270|
271|높은 직책인 건 대충 알겠는데 딱 거기까지다.
272|
273|영 감을 못 잡는 나와 청풍에게 홍진이 차근차근 설명해 주었다.
274|
275|“고위직이죠. 각 성에 겨우 넷밖에 없는 데다가 이 첨사 같은 경우는 품계로 군부에서 세 손가락 안에 들어요.”
276|
277|홍진이 손가락을 하나씩 꼽았다.
278|
279|“총사령관인 도지휘사, 그 아래가 나. 그리고 세 번째가 이 첨사. 물론 모두의 위에 계신 분이 상산왕 전하시고.”
280|
281|“도지휘사요?”
282|
283|“곧 은퇴를 앞둔 분이죠. 대장군의 아들로 태어나 약간의 공을 세웠고 뇌물을 엄청나게 좋아하시는.”
284|
285|부패한 군인이군. 생계형 비리가 일상이 되어 버린.
286|
287|총사령관이라는 인간이 그 모양이니 근래 산서성 치안이 엉망이었던 것도 충분히 설명이 된다.
288|
289|“지금의 도지휘사는 무능해요. 항산검문이 무너지자마자 마적 떼가 활보하는 것만 봐도 알 수 있죠.”
290|
291|“그렇게 무능하면 차라리…….”
292|
293|잘라 버리지 그러십니까, 라는 말을 내뱉기 전에 꿀꺽 삼켰다. 내가 뭐라고 남의 직장 일에 관여를 하나. 그것도 고위 공무원들인데.
294|
295|이런 내 반응에 홍진이 친절한 설명을 덧붙였다.
296|
297|“도지휘사는 황상께서 직접 임명하세요. 해임도 마찬가지고.”
298|
299|“아.”
300|
301|“뭐, 그래도 그 이상의 욕심은 없으니 다행이죠. 나도 뇌물 좋아하니까 욕할 처지는 아니고.”
302|
303|뭐 이런 놈이 다 있어.
304|
305|각종 뇌물 수수 혐의에 결백을 주장하는 정치인들은 TV에서 많이 봤지만 홍진 같은 경우는 처음이다.
306|
307|“왜요, 내가 그렇게 청렴해 보였나?”
308|
309|“아뇨. 뇌물 좋아하실 것 같긴 했는데…….”
310|
311|“이렇게 대놓고 말할 줄 몰랐다?”
312|
313|“뭐, 그렇죠. 솔직히 지금 살짝 당황했습니다.”
314|
315|“진 공자. 그거 알아요?”
316|
317|홍진이 진지한 표정으로 말을 이었다.
318|
319|“나, 물건이 없어.”
320|
321|“예?”
322|
323|“고자라고.”
324|
325|“…….”
326|
327|이거 뭐 어떻게 대답해야 하냐. 짐작은 했지만 이런 폭탄 발언을 갑자기 던질 줄이야.
328|
329|창밖을 구경 중이던 청풍이 궁금한 듯한 얼굴로 대뜸 끼어들었다.
330|
331|“고자가 뭐예요?”
332|
333|“……제발, 제발 입 좀 다물어.”
334|
335|고추가 없다잖아, 고추가!
336|
337|일분일초가 느릿하다. 나는 식은땀을 흘리며 입을 열었다.
338|
339|“유감입니다.”
340|
341|“유감일 것까지야. 살다 보면 없는 사람도 있고, 있는 사람도 있지. 안 그래요?”
342|
343|“그……렇죠.”
344|
345|존경스러운 마인드에 괜히 나까지 숙연해진다.
346|
347|그 와중에 고자의 뜻을 모르는 원시인 놈은 눈치도 없이 자꾸 떠들어 댔다.
348|
349|“은인, 고자가 뭔지 알려 주시면 안 돼요?”
350|
351|죽어도 안 알려 줄 거다. 절대.
352|
353|알려 줘 봤자 ‘와, 저 고추 없는 사람 처음 봐요!’ 이딴 소리 지껄일 확률이 99.99%니까.
354|
355|하지만 홍진은 의연했다.
356|
357|“고자는 고추가 없어요.”
358|
359|“와, 저 고추 없는 사람 처음…….”
360|
361|“아, 닥치라고!”
362|
363|헉, 깜짝 놀란 청풍이 헛숨을 들이켰다.
364|
365|“으, 은인.”
366|
367|“진정해요. 진 공자. 산에서 살다 왔으면 그럴 수도 있죠. 그리고 뭐, 내가 하루 이틀 고자로 살고 있는 것도 아니고.”
368|
369|“그래도 말이 너무 심하잖아요.”
370|
371|“제가 잘못한 거예요? 정말 죄송합니다.”
372|
373|“괜찮아요. 어깨 펴. 아직 달려 있잖아.”
374|
375|고자 수십 년 짬밥이 어디 가는 게 아니구나.
376|
377|진정하라는 듯 손을 내저은 홍진은 대수롭지 않게 말을 이어 갔다.
378|
379|“내가 내린 결정에 대해서는 후회한 적 없어요. 일가 피붙이가 굶어 죽어 가는 마당에 뭐든 못 하겠어. 안 그래요?”
380|
381|“암요. 그렇죠.”
382|
383|“저도, 저도 그랬을 거예요!”
384|
385|지금은 홍진이 무슨 말을 하든 맞장구쳐 줘야 한다. 나와 청풍은 대역 죄인이 된 기분으로 고개만 끄덕였다.
386|
387|“난 청렴하진 않지만 신의를 저버릴 만큼 비겁한 놈은 아니에요. 그랬다면 지금까지 전하를 모시지도 않았겠지.”
388|
389|홍진이 흐릿한 시선으로 창밖을 응시했다.
390|
391|“오래전 선황(先皇)을 곁에서 모셨었죠. 제게 상산왕 전하를 보필하라는 명을 내리셨어요.”
392|
393|“선황께서요?”
394|
395|죽은 전대 황제가 그런 부탁을 했을 정도라면 그때 역시 내관 중에서도 상당한 고위직이었다는 뜻이다.
396|
397|고개를 끄덕인 홍진이 말을 이었다.
398|
399|“변방으로 귀양 아닌 귀양을 왔지만…… 지금은 이 정도로 만족해요. 충분히.”
400|
401|말과는 달리 눈동자에는 숨길 수 없는 빛이 스며들어 있다.
402|
403|야망? 희망? 그것이 품은 의미를 알아차리기도 전에 빛은 사라졌고, 마부의 조용한 음성이 귓가를 파고들었다.
404|
405|“태원진가가 보입니다.”
```

## Assembled English

```markdown
[P1]
# Chapter 146

[P2]
Every meeting must eventually end in parting.

[P3]
As the familiar six-horse carriage drew near, Zhu Bao held out something about the size of my palm.

[P4]
“What is this?”

[P5]
“My reward for today’s meeting.”

[P6]
“Oh, you really didn’t have to…”

[P7]
I accepted it and took a closer look. It was some kind of gold medallion.

[P8]
Clouds and a dragon had been delicately engraved into its surface, which flashed brilliantly in the sunlight.

[P9]
*Ding.*

[P10]
> **System**
>
> - The Quest target is extremely pleased with today’s meeting!
>
> - As a Quest Reward, obtained **Prince Shangshan’s Token**!

[P11]
“It is my token. If there is anything else you desire or a wish you would like granted, bring this token and come find me. I shall fulfill it to the best of my ability.”

[P12]
“Oh.”

[P13]
An exchange coupon.

[P14]
Twenty coupons from a Chinese restaurant would get you a large serving of sweet-and-sour pork. Since this was an exchange coupon from Prince Shangshan, I might be able to trade it for all kinds of elixirs or treasures.

[P15]
*I do need a weapon, too.*

[P16]
Thanks to absorbing the Blazing Flame Divine Pill, I had more than enough internal energy.

[P17]
It was just a shame that I didn’t have a decent spear. I’d been using and discarding other weapons like disposable chopsticks from the very beginning.

[P18]
*Should I just trade it in right now?*

[P19]
I considered it for a moment, then shook my head.

[P20]
The greatest danger had already passed. With no urgent need, trading the prince’s token for a single weapon would be a waste.

[P21]
“Thank you. I really wanted something like this.”

[P22]
When I bowed deeply from the waist, Zhu Bao rose onto his tiptoes and gently ruffled my hair.

[P23]
“I am happy that you like it.”

[P24]
“……”

[P25]
This felt really strange. I’d let it slide because he was cute.

[P26]
Meanwhile, the carriage that would take us home came to a stop. As I was about to climb aboard, Zhu Bao waved at me.

[P27]
“Take care! Come again!”

[P28]
*Next time, you should come to me, you little punk.*

[P29]
There were only a little over two weeks left until New Year’s Day. I would probably see the young prince again around then.

[P30]
“Then I shall take my leave.”

[P31]
“I’ll return, Your Highness.”

[P32]
The carriage was so large that even its entrance was wide. Hong Jin and I climbed aboard side by side.

[P33]
“……Hm?”

[P34]
Wait a minute. That had been so natural that I’d almost let it pass.

[P35]
I stared at Hong Jin in disbelief.

[P36]
“What is it?”

[P37]
“Hm? Why?”

[P38]
“This carriage is going to the Jin Family of Taiyuan.”

[P39]
“I know. That’s why I got on.”

[P40]
“What?”

[P41]
“You know what they say—strike while the iron is hot. Shouldn’t I take this opportunity to speak with the Lesser Family Head Jin?”

[P42]
Hong Jin smiled pleasantly and snapped his fingers. An official came running over like the wind.

[P43]
“Deputy Military Commissioner. Do you have an order for me?”

[P44]
“We’re visiting without an appointment, so we should at least bring plenty of gifts. Don’t forget to send a messenger ahead to offer our respects.”

[P45]
“I shall carry out your orders!”

[P46]
Li Feng also issued an order to one of his officers.

[P47]
“He is an honored guest. Escort him to the Jin Family of Taiyuan.”

[P48]
“Yes, sir!”

[P49]
At the two men’s commands, nearly a hundred soldiers and a hastily assembled delegation began moving in perfect order.

[P50]
Cheongpung, who had been about to climb aboard after us, gave a small round of applause at the sight.

[P51]
“Wow.”

[P52]
Having obtained the royal guard gear set he had longed for so desperately, he decided to stay at the Jin Family of Taiyuan for the time being.

[P53]
Li Feng dipped his head toward me.

[P54]
“I entrust Martial Uncle to you.”

[P55]
“Of course.”

[P56]
Even without hearing him say that, Cheongpung was someone I wanted to befriend first.

[P57]
If I used him as a bridge to strengthen the Jin Family of Taiyuan’s relationship with Huashan, our family’s future would surely be bright.

[P58]
*Besides, he’s an interesting guy.*

[P59]
Cheongpung waved with a sunny smile.

[P60]
“Martial Nephew Li Feng, don’t worry about me! Interesting things keep happening whenever I’m with Young Master Jin!”

[P61]
“Just in case, let me say this now. Don’t cause any trouble.”

[P62]
“Yes!”

[P63]
At least he was good at answering.

[P64]
I turned toward the people who remained behind.

[P65]
“What have you decided to do?”

[P66]
The young prodigies of the Five Gates of Shanxi answered hesitantly.

[P67]
“We plan to stay at Honghwa Inn until New Year’s Day.”

[P68]
“There isn’t enough time to visit our families and return…”

[P69]
“To be honest, we don’t even dare go back.”

[P70]
“If I return now, my father might kill me.”

[P71]
Their answers couldn’t have been gloomier.

[P72]
Then again, rumors about what had happened the day before were probably already racing across the land like a winged horse, so their fear was understandable.

[P73]
I clicked my tongue as I looked at them.

[P74]
“Behave yourselves until New Year’s Day. I’ll smooth things over with the Sect Leaders later.”

[P75]
“R-Really?”

[P76]
“But in return, each of you needs to do your part. You know what I mean, right?”

[P77]
“The Seongun Escort Bureau… Yes, sir. We understand.”

[P78]
The tide could no longer be turned. By now, both these young men and the Sect Leaders of the Five Gates of Shanxi would know that.

[P79]
From now on, all they could do was grow as large as possible under the Jin Family of Taiyuan.

[P80]
“All right, then. Do your best, and I’ll see you on New Year’s Day.”

[P81]
“What?”

[P82]
“Why? What is it?”

[P83]
“W-we’re going the same way.”

[P84]
“Where? To Honghwa Inn?”

[P85]
“Yes.”

[P86]
I tossed one final remark at the bewildered young men.

[P87]
“This is the express carriage to the Jin Family of Taiyuan.”

[P88]
*Bang!*

[P89]
The carriage began moving almost the instant the door slammed shut.

[P90]
* * *

[P91]
The inside had been spacious even with six people seated in it. Cheongpung, Hong Jin, and I each claimed several seats and leaned back against the soft cushions.

[P92]
“I think I could live here.”

[P93]
Cheongpung continued with a blissful smile.

[P94]
“When I lived with Grandfather, I slept on grass or rocks. I don’t think I could live like that anymore.”

[P95]
*He’s a primitive man discovering civilization.*

[P96]
Hong Jin gave him a curious look.

[P97]
“Then have you always lived on Huashan, Young Master?”

[P98]
“Yes. Ever since I was very young. But apparently I wasn’t born on Huashan. I asked Grandfather about it once, and he said I came to Huashan when I was three or four.”

[P99]
That figured. No matter how great a master the Sword Saint was, even he had his limits when it came to raising a child.

[P100]
Reaching the Supreme Peak realm wouldn’t make milk come out of a man’s chest, after all.

[P101]
“……”

[P102]
*Actually, a Supreme Peak master might be able to do it.*

[P103]
They were monsters who could use Sword Energy and Sword Force. Producing a little milk couldn’t be beyond them.

[P104]
I imagined a white-haired old man nursing a newborn baby.

[P105]
“Ugh.”

[P106]
“Benefactor, are you all right?”

[P107]
“Young Master Jin, are you all right?”

[P108]
“I’m fine. I just felt a little nauseous.”

[P109]
“Oh my, that won’t do. Here, lie down on my lap.”

[P110]
“……”

[P111]
*Maybe I should just smash his knee.*

[P112]
When I hurled silent curses at him with my eyes, Hong Jin covered his mouth and laughed.

[P113]
“Hoho. Young Master Jin really is so much fun to tease.”

[P114]
If a beautiful woman had said that, I would have laughed along with her. But Hong Jin was unmistakably a man. No amount of white powder on his face or lipstick on his lips could change that fact.

[P115]
*He said he used to be a palace attendant.*

[P116]
Didn’t that make him a eunuch?

[P117]
I’d once heard that not every palace attendant was necessarily a eunuch. But there was no way to tell whether Hong Jin was equipped or not.

[P118]
“Young Master Jin.”

[P119]
“Y-Yes?”

[P120]
“What are you looking at?”

[P121]
“Ah, I thought there was something stuck there.”

[P122]
*Damn it. He caught me.*

[P123]
He wasn’t a Murim martial artist, but his ability to read the situation was on the level of a Peak master. I quickly pulled my gaze away from Hong Jin’s lower body and changed the subject.

[P124]
“By the way, how did Great Hero Li Feng end up joining the military?”

[P125]
“Assistant Military Commissioner Li? He passed the military examination, of course. After that, it was smooth sailing all the way.”

[P126]
“As expected of a Huashan lay disciple.”

[P127]
“I can’t say that had no influence, but that wasn’t the only reason. Becoming a Third-Rank Assistant Military Commissioner in only ten years is extremely difficult.”

[P128]
“Third-Rank means…?”

[P129]
“What’s Third-Rank? Is it something you eat?”

[P130]
I vaguely understood that it was a high position, but that was about it.

[P131]
Seeing that Cheongpung and I had no idea what he was talking about, Hong Jin explained patiently.

[P132]
“It’s a high office. There are only four such positions in each province, and Assistant Military Commissioner Li is among the top three in the military hierarchy.”

[P133]
Hong Jin counted them off on his fingers.

[P134]
“First is the Military Commissioner, the commander in chief. Then me, directly beneath him. And third is Assistant Military Commissioner Li. Of course, His Highness Prince Shangshan stands above us all.”

[P135]
“The Military Commissioner?”

[P136]
“He’ll be retiring soon. He was born the son of a Grand General, accomplished a little, and has a tremendous fondness for bribes.”

[P137]
*A corrupt military official. The kind whose petty corruption had become a way of life.*

[P138]
With the commander in chief being that kind of man, it was easy to understand why security in Shanxi Province had been such a mess lately.

[P139]
“The current Military Commissioner is incompetent. You only need to look at the mounted bandits roaming freely the moment the Mount Heng Sword Sect collapsed.”

[P140]
“If he’s that incompetent, why not just…”

[P141]
I swallowed the rest of the sentence before it left my mouth.

[P142]
*Who was I to meddle in someone else’s workplace? Especially when they were all high-ranking government officials.*

[P143]
Seeing my reaction, Hong Jin kindly added an explanation.

[P144]
“The Military Commissioner is appointed directly by the Emperor. The same goes for dismissing him.”

[P145]
“Oh.”

[P146]
“Well, at least he has no ambitions beyond that. I like bribes too, so I’m hardly in a position to criticize him.”

[P147]
*What kind of person was this?*

[P148]
I’d seen plenty of politicians on television proclaiming their innocence against accusations of accepting bribes, but Hong Jin was the first person I’d met who openly admitted to liking them.

[P149]
“Why? Did I look that upright?”

[P150]
“No. You did look like someone who would enjoy bribes, but…”

[P151]
“But you didn’t expect me to say it so openly?”

[P152]
“Well, yes. Honestly, I’m a little flustered.”

[P153]
“Young Master Jin. Do you know what?”

[P154]
Hong Jin continued with a serious expression.

[P155]
“I don’t have a thing.”

[P156]
“What?”

[P157]
“I’m a eunuch.”

[P158]
“……”

[P159]
*What the hell was I supposed to say to that?*

[P160]
I’d suspected as much, but I hadn’t expected him to drop a bomb like that out of nowhere.

[P161]
Cheongpung, who had been looking out the window, abruptly joined in with a curious expression.

[P162]
“What’s a eunuch?”

[P163]
“……Please, please shut your mouth.”

[P164]
*He’s saying he doesn’t have his thing—his thing!*

[P165]
Every second dragged by. Sweating coldly, I forced myself to speak.

[P166]
“I’m sorry to hear that.”

[P167]
“There’s no need to be sorry. Some people live without one, and some live with one. Right?”

[P168]
“Th—that’s right.”

[P169]
His admirable attitude made me solemn for no reason.

[P170]
Meanwhile, the mountain-dwelling primitive who didn’t know what a eunuch was kept chattering without the slightest hint of tact.

[P171]
“Benefactor, could you please tell me what a eunuch is?”

[P172]
*Even if I die, I’m not telling him. Never.*

[P173]
Even if I explained it, there was a 99.99 percent chance he would say something like, *Wow, I’ve never met anyone without a dick before!*

[P174]
But Hong Jin remained composed.

[P175]
“A eunuch doesn’t have a dick.”

[P176]
“Wow, I’ve never met anyone without—”

[P177]
“Oh, shut up already!”

[P178]
Cheongpung sucked in a startled breath.

[P179]
“B-Benefactor.”

[P180]
“Calm down, Young Master Jin. If he grew up in the mountains, it’s understandable. And besides, it’s not as if I’ve only been living as a eunuch for a day or two.”

[P181]
“Still, that was too harsh.”

[P182]
“Was I in the wrong? I’m truly sorry.”

[P183]
“It’s fine. Chin up. Yours is still attached.”

[P184]
*Decades of experience as a eunuch hadn’t gone anywhere.*

[P185]
Hong Jin waved a hand as if to calm us down, then continued as though nothing important had happened.

[P186]
“I’ve never regretted my decision. When your own family is starving to death, what wouldn’t you do? Am I wrong?”

[P187]
“Of course not.”

[P188]
“I—I would have done the same!”

[P189]
Whatever Hong Jin said now, we had to agree with him. Cheongpung and I could only nod, feeling like condemned criminals.

[P190]
“I’m not an upright man, but I’m not cowardly enough to betray a trust. If I were, I wouldn’t have continued serving His Highness all this time.”

[P191]
Hong Jin gazed out the window with hazy eyes.

[P192]
“Long ago, I served at the late Emperor’s side. He ordered me to assist His Highness Prince Shangshan.”

[P193]
“The late Emperor?”

[P194]
If the previous Emperor had entrusted Hong Jin with such a request, Hong Jin must have held a considerably high position among the palace attendants even back then.

[P195]
Hong Jin nodded and continued.

[P196]
“I came to the frontier in what was practically exile, but… I’m satisfied with things as they are now. Truly, this is enough.”

[P197]
Despite his words, an unmistakable light shone in his eyes.

[P198]
Ambition? Hope?

[P199]
Before I could understand what that light meant, it disappeared, and the coachman’s quiet voice reached my ears.

[P200]
“The Jin Family of Taiyuan is in sight.”
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
# Chapter 146

[P2]
Every meeting must eventually end in a parting.

[P3]
As the familiar six-horse carriage drew near, Zhu Bao held out something about the size of my palm.

[P4]
“What is this?”

[P5]
“My reward for today’s meeting.”

[P6]
“Oh, you really didn’t have to…”

[P7]
When I accepted it and examined it closely, I saw that it was a kind of golden medallion.

[P8]
Clouds and a dragon had been delicately engraved into its surface, which flashed brilliantly in the sunlight.

[P9]
*Ding.*

[P10]
> **System**
>
> - The Quest target is extremely pleased with today’s meeting!
>
> - As a Quest Reward, obtained **Prince Shangshan’s Token**!

[P11]
“It is my token. If there is anything else you desire or a wish you would like granted, bring this token and come find me. I shall fulfill it to the best of my ability.”

[P12]
“Oh.”

[P13]
A coupon for an exchange.

[P14]
At a Chinese restaurant, twenty coupons would get you a large serving of sweet-and-sour pork. Since this was a coupon from Prince Shangshan, I might be able to exchange it for all kinds of elixirs or treasures.

[P15]
*I do need a weapon, too.*

[P16]
Thanks to absorbing the Blazing Flame Divine Pill, I had more than enough internal energy.

[P17]
It was just a shame that I didn’t have a decent spear to use. As for the other weapons, I had used and discarded them from the start like disposable chopsticks.

[P18]
*Should I just trade it in right now?*

[P19]
I considered it for a moment, then shook my head.

[P20]
The greatest dangers had already passed. Exchanging the prince’s token for a single weapon when there was no immediate need would be a waste.

[P21]
“Thank you. I really wanted something like this.”

[P22]
When I bowed deeply from the waist, Zhu Bao rose onto his tiptoes and gently ruffled my hair.

[P23]
“I am happy that you like it.”

[P24]
“……”

[P25]
This felt really strange. I’d let it slide because he was cute.

[P26]
In the meantime, the carriage that would take us home came to a stop. As I was about to climb aboard, Zhu Bao waved at me.

[P27]
“Take care! Come again!”

[P28]
*Next time, you should come to me, you little punk.*

[P29]
There were only a little over two weeks left until New Year’s Day. I would probably be able to see the young prince again around then.

[P30]
“Then, I shall take my leave.”

[P31]
“I’ll return, Your Highness.”

[P32]
The carriage was so large that its entrance was wide as well. Hong Jin and I climbed aboard side by side.

[P33]
“……Hm?”

[P34]
Wait a minute. That had been so natural that I’d almost let it pass.

[P35]
I stared at Hong Jin in disbelief.

[P36]
“What is it?”

[P37]
“Hm? Why?”

[P38]
“This carriage is going to the Jin Family of Taiyuan.”

[P39]
“I know. That’s why I got on.”

[P40]
“What?”

[P41]
“You know what they say—strike while the iron is hot. Shouldn’t I take this opportunity to have a conversation with the Lesser Family Head Jin?”

[P42]
Hong Jin smiled pleasantly and snapped his fingers. An official came running over like the wind.

[P43]
“Deputy Military Commissioner. Do you have an order for me?”

[P44]
“We’re visiting without an appointment, so we should bring plenty of gifts. Don’t forget to send a messenger ahead to offer them our respects.”

[P45]
“I shall carry out your orders!”

[P46]
Li Feng also issued an order to one of the officers under his command.

[P47]
“He is an honored guest. Escort him to the Jin Family of Taiyuan.”

[P48]
“Yes, sir!”

[P49]
At the two men’s commands, nearly a hundred soldiers and a hastily assembled delegation began moving in perfect order.

[P50]
Cheongpung, who had been about to climb aboard after us, gave a small round of applause at the sight.

[P51]
“Wow.”

[P52]
Having obtained the royal guard gear set he had longed for so desperately, he decided to stay at the Jin Family of Taiyuan for the time being.

[P53]
Li Feng dipped his head toward me.

[P54]
“I entrust Martial Uncle to you.”

[P55]
“Of course.”

[P56]
Even without hearing him say that, Cheongpung was someone I wanted to become friends with first.

[P57]
If I used him as a bridge to strengthen the Jin Family of Taiyuan’s relationship with Huashan, our family’s future would surely be bright.

[P58]
*He’s an interesting guy, too.*

[P59]
Cheongpung waved with a sunny smile.

[P60]
“Martial Nephew Li Feng, don’t worry about me! Interesting things keep happening whenever I’m with Young Master Jin!”

[P61]
“Just in case, I’ll say this now. Don’t cause any trouble.”

[P62]
“Yes!”

[P63]
At least he was good at answering.

[P64]
I turned toward the people who remained behind.

[P65]
“What have you decided to do?”

[P66]
The young prodigies of the Five Gates of Shanxi answered hesitantly.

[P67]
“We plan to stay at Honghwa Inn until New Year’s Day.”

[P68]
“It would be difficult to visit our families. There isn’t much time…”

[P69]
“To be honest, we don’t even dare go back.”

[P70]
“If I return now, my father might kill me.”

[P71]
Their answers were as gloomy as could be.

[P72]
Then again, rumors about what had happened the day before had probably already spread like wildfire, so their fear was understandable.

[P73]
I clicked my tongue as I looked at them.

[P74]
“Behave yourselves until New Year’s Day. I’ll smooth things over with the Sect Leaders later.”

[P75]
“Are you really going to do that?”

[P76]
“But in return, each of you needs to do your part. You know what I mean, right?”

[P77]
“The Seongun Escort Bureau… Yes, sir. We understand.”

[P78]
The tide could no longer be turned. By now, both these young men and the Sect Leaders of the Five Gates of Shanxi would know that.

[P79]
All that remained was to grow as large as possible under the Jin Family of Taiyuan.

[P80]
“All right, then. Do your best, and I’ll see you at New Year’s.”

[P81]
“What?”

[P82]
“Why? What is it?”

[P83]
“W-we’re going the same way.”

[P84]
“Where? To Honghwa Inn?”

[P85]
“Yes.”

[P86]
I tossed one final remark at the bewildered young men.

[P87]
“This is an express carriage to the Jin Family of Taiyuan.”

[P88]
*Bang!*

[P89]
The carriage began moving almost as soon as the door slammed shut.

[P90]
* * *

[P91]
The inside had been spacious even with six people seated in it. Cheongpung, Hong Jin, and I each claimed several seats and leaned back against the soft cushions.

[P92]
“I think I could live here.”

[P93]
Cheongpung continued with a blissful smile.

[P94]
“When I lived with Grandfather, I slept on grass or rocks. I don’t think I could live like that anymore.”

[P95]
*He’s a primitive man discovering civilization.*

[P96]
At his words, Hong Jin asked with curious eyes,

[P97]
“Then have you always lived on Huashan, Young Master?”

[P98]
“Yes. Ever since I was very young. But apparently I wasn’t born on Huashan. I asked Grandfather about it once, and he said I came to Huashan when I was three or four years old.”

[P99]
That figured. No matter how great a master the Sword Saint was, even he had limits when it came to raising a child.

[P100]
Reaching the Supreme Peak realm wouldn’t make milk come out of a man’s chest, after all.

[P101]
“……”

[P102]
*Actually, a Supreme Peak master might be able to do it.*

[P103]
They were monsters who could use Sword Energy and Sword Force. Producing a little milk couldn’t be beyond them.

[P104]
I imagined a white-haired old man nursing a newborn baby.

[P105]
“Ugh.”

[P106]
“Benefactor, are you all right?”

[P107]
“Young Master Jin, are you all right?”

[P108]
“I’m fine. I just felt a little nauseated.”

[P109]
“Oh my, that won’t do. Here, lie down on my lap.”

[P110]
“……”

[P111]
*Maybe I should just smash his knee.*

[P112]
When I hurled a silent double curse at him with my eyes, Hong Jin covered his mouth and laughed.

[P113]
“Hoho. As expected, Young Master Jin is so much fun to tease.”

[P114]
If a beautiful woman had said that, I would have laughed along with her. But Hong Jin was unmistakably a man. No amount of white powder on his face or lipstick on his lips could change that fact.

[P115]
*He said he used to be a palace attendant.*

[P116]
Didn’t that make him a eunuch?

[P117]
I had heard once that not every eunuch was necessarily castrated. But there was no way to tell whether Hong Jin was equipped or not.

[P118]
“Young Master Jin.”

[P119]
“Yes, yes?”

[P120]
“What are you looking at right now?”

[P121]
“Ah, I thought there was something stuck there.”

[P122]
*Damn it. He caught me.*

[P123]
He wasn’t a Murim martial artist, but his ability to read the situation was on the level of a Supreme Peak master. I quickly pulled my gaze away from Hong Jin’s lower body and changed the subject.

[P124]
“By the way, how did Great Hero Li Feng end up joining the military?”

[P125]
“Assistant Military Commissioner Li? He passed the military examination, of course. After that, it was smooth sailing all the way.”

[P126]
“As expected of a Huashan lay disciple.”

[P127]
“I can’t say that had no influence, but it wasn’t only because of that. Becoming a Third-Rank Assistant Military Commissioner in only ten years is extremely difficult.”

[P128]
“Third-Rank means…?”

[P129]
“What is Third-Rank? Is it something you eat?”

[P130]
I vaguely understood that it was a high position, but that was about it.

[P131]
Seeing that Cheongpung and I had no idea what he was talking about, Hong Jin explained patiently.

[P132]
“It’s a high office. There are only four such positions in each province, and in terms of rank, Assistant Military Commissioner Li is one of the top three in the military.”

[P133]
Hong Jin counted them off on his fingers.

[P134]
“The Military Commissioner, who is the commander in chief. Then me, directly beneath him. And third is Assistant Military Commissioner Li. Of course, His Highness Prince Shangshan stands above all of us.”

[P135]
“The Military Commissioner?”

[P136]
“He’s about to retire. He was born the son of a Grand General, accomplished a little, and has a tremendous fondness for bribes.”

[P137]
*A corrupt military official. The kind whose petty corruption had become a way of life.*

[P138]
With the commander in chief being that kind of person, it was easy to understand why security in Shanxi Province had been such a mess lately.

[P139]
“The current Military Commissioner is incompetent. You only need to look at the mounted bandits roaming freely the moment the Mount Heng Sword Sect collapsed.”

[P140]
“If he’s that incompetent, then why not just…”

[P141]
I swallowed the rest of the sentence before it left my mouth.

[P142]
*Why should I meddle in someone else’s workplace? Especially when they’re all high-ranking government officials.*

[P143]
Seeing my reaction, Hong Jin kindly added an explanation.

[P144]
“The Military Commissioner is appointed directly by the Emperor. His dismissal works the same way.”

[P145]
“Oh.”

[P146]
“Well, at least he has no ambitions beyond that. I like bribes too, so I’m hardly in a position to criticize him.”

[P147]
*What kind of person was this?*

[P148]
I had seen plenty of politicians on television who claimed to be innocent of all charges of accepting bribes, but Hong Jin was the first person I had met who admitted to liking them so openly.

[P149]
“Why? Did I look that upright?”

[P150]
“No. You did look like someone who would enjoy bribes, but…”

[P151]
“But you didn’t expect me to say it so openly?”

[P152]
“Something like that. To be honest, I’m a little flustered.”

[P153]
“Young Master Jin. Do you know what?”

[P154]
Hong Jin continued with a serious expression.

[P155]
“I don’t have a thing.”

[P156]
“What?”

[P157]
“I’ve been castrated.”

[P158]
“……”

[P159]
*What the hell was I supposed to say to that?*

[P160]
I had suspected as much, but I hadn’t expected him to suddenly drop a bomb like that.

[P161]
Cheongpung, who had been looking out the window, abruptly joined in with a curious expression.

[P162]
“What does ‘castrated’ mean?”

[P163]
“……Please, please shut your mouth.”

[P164]
*He said he doesn’t have his thing—his thing!*

[P165]
Every second dragged by. Sweating coldly, I forced myself to speak.

[P166]
“I’m sorry to hear that.”

[P167]
“There’s no need to be sorry. Some people live without it, and some people live with it. Right?”

[P168]
“Th—that’s right.”

[P169]
His admirable attitude made me solemn for no reason.

[P170]
Meanwhile, the mountain-dwelling primitive who didn’t know what a eunuch was kept chattering without the slightest sense of danger.

[P171]
“Benefactor, could you please tell me what a eunuch is?”

[P172]
*Even if I die, I’m not telling him. Never.*

[P173]
Even if I explained it, there was a 99.99 percent chance he would say something like, *Wow, I’ve never met anyone without one before!*

[P174]
But Hong Jin remained composed.

[P175]
“It means a man doesn’t have his thing.”

[P176]
“Wow, I’ve never met anyone who didn’t have—”

[P177]
“Oh, shut up already!”

[P178]
Cheongpung sucked in a startled breath.

[P179]
“B-Benefactor.”

[P180]
“Calm down, Young Master Jin. If he grew up in the mountains, it’s understandable. And besides, it’s not as if I’ve only been living as a eunuch for a day or two.”

[P181]
“Still, that was too harsh.”

[P182]
“Was I in the wrong? My sincerest apologies.”

[P183]
“It’s fine. Chin up. It’s still attached.”

[P184]
*Decades of experience as a eunuch hadn’t gone anywhere.*

[P185]
Hong Jin waved his hand as if telling us to calm down, then continued as though nothing important had happened.

[P186]
“I have never regretted the decision I made. When your own family is starving to death, what wouldn’t you do? Am I wrong?”

[P187]
“Of course not.”

[P188]
“I—I would have done the same!”

[P189]
Whatever Hong Jin said now, we had to agree with him. Cheongpung and I could only nod, feeling like condemned criminals.

[P190]
“I’m not an upright man, but I’m not cowardly enough to betray my loyalty. If I were, I wouldn’t have continued serving His Highness all this time.”

[P191]
Hong Jin gazed out the window with hazy eyes.

[P192]
“I served the late Emperor at his side long ago. He ordered me to assist His Highness Prince Shangshan.”

[P193]
“The late Emperor?”

[P194]
If the previous Emperor had entrusted Hong Jin with such a request, it meant he must have held a considerably high position among the palace eunuchs even back then.

[P195]
Hong Jin nodded and continued.

[P196]
“I came to the frontier in something like exile, but… I’m satisfied with things as they are now. More than satisfied.”

[P197]
Despite his words, an unmistakable light shone in his eyes.

[P198]
Ambition? Hope?

[P199]
Before I could understand what that light meant, it disappeared, and the coachman’s quiet voice reached my ears.

[P200]
“We can see the Jin Family of Taiyuan.”
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 화산파    | **Huashan**                      |
| 산서오문   | **Five Gates of Shanxi**         |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 영약     | **elixir**                                       |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 표국     | **Escort Bureau**                            |
| 제자     | **Disciple**                                 |
| 사숙     | **Martial Uncle**                            |
| 사질     | **Martial Nephew**                           |
| 은인     | **Benefactor**                               |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 화산     | **Huashan**            |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 정삼품 | **Third-Rank** | Official rank of the unnamed Assistant Military Commissioner. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 도지휘사 | **Military Commissioner** | Provincial military commander's office |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 근위대 | **royal guard** | Guard unit protecting Prince Shangshan. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 내관 | **palace attendant** | Hong Jin's former palace role; context identifies him as a eunuch. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 146,
  "passed": true,
  "metrics": {
    "source_characters": 5780,
    "translation_characters": 13193,
    "length_ratio": 2.283,
    "source_paragraphs": 198,
    "translation_paragraphs": 200
  },
  "errors": [],
  "warnings": [
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
        "korean": "대협",
        "preferred": "Great Hero or Sir depending tone"
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
        "korean": "소원",
        "preferred": "Sowon"
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
