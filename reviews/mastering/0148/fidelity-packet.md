# Fidelity Gate — Chapter 148

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
  1|＃148화
  2|
  3|
  4|
  5|십만 냥이라는 거금이 따뜻하게 덥혀 놓은 분위기 속, 진위경과 홍진이 인사를 주고받았다.
  6|
  7|“태원진가의 진위경이라 합니다. 말로만 듣던 도지휘동지를 뵙게 되어 기쁘기 한량없습니다.”
  8|
  9|“대태원진가의 소가주께서 이리 환대해 주시니 몸 둘 바를 모르겠네요. 앞으로는 편하게 홍 동지라고 불러 주세요.”
 10|
 11|“그래도 벼슬하시는 분께 그럴 수야 있습니까.”
 12|
 13|“아이, 너무 딱딱하시다. 편하게 부르시라니까.”
 14|
 15|“하하, 그럼 그럴까요, 홍 동지?”
 16|
 17|갑자기 분위기 공산주의 뭔데.
 18|
 19|여기가 평양인지 무림인지 고민하고 있을 때, 통성명을 끝마친 진위경의 시선이 이쪽을 향했다.
 20|
 21|“음. 태경이 왔느냐?”
 22|
 23|“예.”
 24|
 25|평소와는 다른 묵직한 목소리에 눈치껏 공손히 대답했다.
 26|
 27|아무래도 외부인이 보는 앞에서 평소처럼 굴었다가는 진위경 개인의 위신은 물론이고 가문 전체가 망신임을 알고 있는 것 같다.
 28|
 29|“그래, 전하께 인사는 잘 드렸고?”
 30|
 31|인사 정도가 아니라 단독 팬 사인회도 하고 왔지.
 32|
 33|홍진이 웃으며 내 어깨를 톡톡 두드렸다.
 34|
 35|“전하께서 아주 기뻐하셨어요. 평소에 여기 진 공자를 너무 보고 싶어 하셨거든요.”
 36|
 37|“아, 그렇습니까?”
 38|
 39|“네. 얼마나 좋아하시던지 도무지 놔줄 생각을 안 하시더라니까요.”
 40|
 41|“으허허, 우리 막내…… 아니. 제 아우가 마음에 쏙 드신 모양이군요.”
 42|
 43|“그럴 만도 하죠. 얼굴 잘생겼지, 키 크고 몸 좋지. 무공도 강한 데다 성격도 아주 서글서글하니 싫어할 사람이 어디 있겠어요?”
 44|
 45|“으흠, 제 입으로 이런 말 하긴 뭐 하지만, 사실 태경이가 대단한 인재이긴 합니다. 본가가 아니라 오대세가 같은 곳에서 태어났으면 천하제일인이 되었어도 이상하지 않아요.”
 46|
 47|무게 잡는 것도 잊고 신이 나서 떠들어 대는 진위경의 모습에 홍진이 얼굴을 굳혔다.
 48|
 49|“천하제일이요? 진 소가주님. 농담이 너무 심하시다.”
 50|
 51|“네? 그게 무슨.”
 52|
 53|“진 공자가 천하제일인이 될 재목이라니요. 아무리 제가 무림과 연이 없다고 해도 그렇지, 너무 우습게 보시는 거 아녜요?”
 54|
 55|“……커흠.”
 56|
 57|순간 싸해진 분위기 속에 진위경이 불편한 헛기침을 내뱉었다. 그때 홍진이 재깍 말을 이었다.
 58|
 59|“진 공자 정도라면 고금제일인도 될 수 있죠.”
 60|
 61|“……!”
 62|
 63|“미리 축하드려요, 소가주님. 태원진가에서 고금제일인이 나오다니, 산서성의 홍복이네요.”
 64|
 65|진위경이 감격에 찬 얼굴로 외쳤다.
 66|
 67|“홍 동지!”
 68|
 69|“진 소가주님!”
 70|
 71|“…….”
 72|
 73|황궁에서 20년을 살았다더니, 과연 혓바닥 놀리는 솜씨가 보통이 아니다.
 74|
 75|나는 영혼의 단짝을 만나기라도 한 것처럼 기뻐하는 진위경을 보며 혀를 내둘렀다.
 76|
 77|“안 되겠습니다. 여기서 이럴 게 아니라 제가 자리를 마련해 뒀으니 술이라도 한잔…….”
 78|
 79|“어쩌죠? 제가 술은 잘 못 먹어서.”
 80|
 81|“아, 이리 안타까울 수가.”
 82|
 83|“없어서 못 먹어요.”
 84|
 85|“홍 동지!”
 86|
 87|“진 소가주님!”
 88|
 89|“…….”
 90|
 91|“…….”
 92|
 93|쿵짝 잘 맞는 거 봐라.
 94|
 95|두 사람이 껄껄 웃으며 어깨동무를 하고 사라지자 위팽이 황당하다는 얼굴로 나를 바라봤다.
 96|
 97|“저자가 정말 도지휘동지가 맞습니까?”
 98|
 99|“안타깝지만 사실이에요.”
100|
101|“내관 출신이라고는 들었지만 저렇게 경박스러울 줄은.”
102|
103|글쎄, 그럼 거기에 맞장구까지 다 쳐 준 무인 출신인 진위경은 뭐가 되나.
104|
105|아까부터 썩은 표정이던 진무경이 입을 열었다.
106|
107|“원래 저런 작자입니다. 지난번에는 은근슬쩍 제 어깨를 쓰다듬더군요. 팔을 부러트리려다가 간신히 참았습니다.”
108|
109|손에 들고 있던 천을 쫙쫙 찢어 땅바닥에 내팽개친 그가 한결 후련해진 표정으로 말했다.
110|
111|“그럼 전 중요한 볼일이 있어서 이만.”
112|
113|“볼일은 무슨. 또 수련이겠지 뭐.”
114|
115|“무인에게 있어 수련보다 중요한 일이 있나?”
116|
117|“……없지.”
118|
119|할 말 없게 만드는군.
120|
121|말문이 막혀 입맛만 다시던 그때, 또랑또랑하고 맑은 목소리가 울려 퍼졌다.
122|
123|“우와, 저희 할아버지가 항상 하시는 말씀이랑 똑같아요.”
124|
125|순간 위팽과 진무경의 시선이 청풍을 송곳처럼 찔렀다.
126|
127|양민들이 볼 때야 조금 독특한 분위기의 청년, 딱 그 정도지만 고수들에겐 다르다.
128|
129|두 사람의 눈썹이 위로 솟구치자 청풍이 당황한 얼굴로 나를 돌아봤다.
130|
131|“어, 은인. 제가 무슨 잘못이라도 했나요?”
132|
133|“잘못은 무슨. 그냥 신기해서 그런 거예요. 그렇죠, 두 분?”
134|
135|두 사람은 청풍에게 시선을 고정시킨 채 고개만 끄덕였다.
136|
137|새파랗게 젊은 절정 고수. 그들로서는 난데없이 튀어나온 청풍의 정체가 궁금할 법도 했다.
138|
139|“이참에 서로 통성명이라도 하시죠. 이쪽은 청풍.”
140|
141|내 말이 끝나기가 무섭게 청풍이 고개를 꾸벅 숙였다.
142|
143|“안녕하세요, 청풍입니다! 산서에 온 지는 며칠밖에 안 됐고요. 그전에는 하남에 있었고 또…….”
144|
145|이거 어디서 굴러먹다 온 놈이야? 두 사람의 얼굴엔 딱 저렇게 쓰여 있다.
146|
147|예상했던 바다. 나는 청풍의 정체를 간단명료하게 설명했다.
148|
149|“검성의 제잡니다.”
150|
151|“……!”
152|
153|“……!”
154|
155|검성 매종학의 이름은 무림인들에게 있어 확실히 치트키나 다름없다.
156|
157|두 사람이 경악에 찬 얼굴로 입을 딱 벌리고 말을 잇지 못하자 청풍이 조심스럽게 물었다.
158|
159|“저어, 그런데 두 분 중 누가 진천검이시죠?”
160|
161|아직 충격에서 빠져나오지 못한 진무경이 더듬더듬 대답했다.
162|
163|“내, 내가 진천검이오. 한데 정말 검성 매종학 대협의……?”
164|
165|“네. 저희 할아버지세요.”
166|
167|“헉!”
168|
169|화염신장의 비급을 봤을 때보다 몇 배는 놀란 표정이다.
170|
171|이미 수십 년 전 은거한 것으로 알려진 초절정 고수의 제자, 그것도 손자라고 하는 젊은이가 툭 튀어나왔으니 그럴 만도 했다.
172|
173|“이럴 수가…….”
174|
175|“검성의 후인이라니.”
176|
177|놀라움을 금치 못하는 두 사람을 번갈아 보던 청풍이 해맑게 웃었다.
178|
179|“저도 하산하기 전까지는 몰랐네요.”
180|
181|“소, 소협. 혹시 매 대협께서도 하산을……?”
182|
183|물어보는 목소리에는 기대와 흥분이 한껏 담겨 있었다.
184|
185|두 사람 모두 일평생 검을 수련해 온 검객. 매종학은 검성이라는 별호를 얻을 정도로 검도(劍道)의 경지를 이룩한 사람이니 그들에게 있어 신이나 다름없는 존재였다.
186|
187|그러나 청풍은 대답은 두 사람의 기대를 산산조각 냈다.
188|
189|“아뇨, 저만 몰래 도망쳐 나왔어요. 만나고 싶은 분들이 있어서.”
190|
191|“아아.”
192|
193|“그럴 수가…….”
194|
195|“근데 그건 그렇고…….”
196|
197|안타까워하는 두 사람을 바라보던 청풍이 재차 입을 열었다.
198|
199|그의 반짝거리는 눈빛은 아까 전부터 진무경에게 고정되어 있었다.
200|
201|“정말 진천검 진무경 소협이신가요? 십봉룡(十鳳龍)의 그분?”
202|
203|“맞소, 내가 진무경이오.”
204|
205|“와, 드디어 찾았다!”
206|
207|“……음?”
208|
209|“제가 그쪽을 엄청 찾아 헤맸거든요. 하남의 천무학관에서부터 여기까지.”
210|
211|뭐야, 저 녀석이 찾고 있던 사람이 진무경이었어?
212|
213|위팽은 물론이고 당사자인 진무경도 어리둥절한 표정으로 물었다.
214|
215|“날 말이오?”
216|
217|“네. 마침 가깝기도 하고, 첫 번째 시작으로 나쁘지 않겠다 싶어서요.”
218|
219|“첫 번째라니. 그게 무슨 말이오?”
220|
221|“비무행(比武行).”
222|
223|청풍이 잔잔하게 웃었다. 그건 지금까지 보아 왔던 해맑고 순수한 웃음과는 전혀 다른 종류의 것이었다.
224|
225|“하산하면서 결심했지요. 십봉룡을 모두 꺾기 전에는 돌아가지 않겠다고.”
226|
227|“……!”
228|
229|“할아버지께서 그러셨어요. 무인에게는 대화가 필요 없다. 오직 무(武)로 겨룰 뿐이다.”
230|
231|스으으.
232|
233|그 순간, 나는 뜨거운 열기를 느꼈다. 어느새 솟구친 자줏빛 광염(光焰)이 청풍의 전신에서 피어오르고 있었다.
234|
235|이미 한 번 본 적 있는 광경이다.
236|
237|‘자하신공.’
238|
239|극양의 기운이 냉기를 불살랐다. 땅이 녹고 흙이 그을렸다. 청풍이 웃음이 사라진 얼굴로 입을 열었다.
240|
241|“자리를 옮길까요?”
242|
243|“그럴 필요 있나?”
244|
245|진무경의 말이 이어졌다.
246|
247|“검을 뽑아.”
248|
249|
250|
251|* * *
252|
253|
254|
255|진무경은 길게 숨을 내뱉었다. 빠르게 뛰던 심장이 천천히 속도를 늦춘다. 전투에서 중요한 것은 호흡이다. 이제야 비로소 검을 뽑을 준비를 갖췄다.
256|
257|그는 검파에 손을 올리며 한 사람의 이름을 떠올렸다.
258|
259|‘검성 매종학.’
260|
261|검을 처음 쥔 날부터 단 하루도 그 이름을 잊은 적이 없었다.
262|
263|검의 궁극에 다다랐다는, 혹은 그 너머의 경지에 이르렀다는 전설적인 검객.
264|
265|모두가 검성을 추앙했지만 진무경은 달랐다.
266|
267|‘언젠가 그를 꺾고 말겠다.’
268|
269|누군가 들었다면 코웃음을 쳤을 일이다. 미친놈이라며 손가락질했을 것이다.
270|
271|진무경이 제아무리 천재라 한들 검성이라는 이름에는 닿을 수 없다. 매종학이 검성이라 불리기 시작한 이래, 그 누구도 그를 넘어서지 못했으니까.
272|
273|검성 매종학은 이미 수십 년 전 정파 무림의 새로운 역사를 썼고, 신화의 주인공이 되었다.
274|
275|‘상관없어. 이건 내 목표니까.’
276|
277|만용이 아니라 목표다.
278|
279|지금껏 검을 수련하며 매일같이 뼈와 가슴에 새겨 온 목표.
280|
281|그리고 이 순간, 검성 매종학의 모든 것을 물려받은 한 사람이 눈앞에 있다.
282|
283|“할아버지께서 그러셨죠. 너는 십봉룡에 비하면 아무것도 아니다. 자만하지 말아라.”
284|
285|청풍이 천천히 발을 내디뎠다. 허리춤에는 아무렇게나 매인 청강검 한 자루가 대롱거렸고, 발걸음은 산책이라도 나온 것처럼 가벼웠다.
286|
287|그러나…….
288|
289|‘빈틈이 없다.’
290|
291|허술하기 짝이 없는데 도무지 언제, 어떻게 상대를 공격해야 할지 모르겠다.
292|
293|진무경은 바짝 마른 입술을 핥았다.
294|
295|“난 그분을 만나 본 적도 없는데…… 과찬을 하셨군.”
296|
297|“아니에요. 솔직히 살짝 놀랐는걸요. 이건 진심이에요.”
298|
299|진무경 역시 지금 청풍이 하는 말들이 모두 진심이라는 사실을 안다. 그래서 더 기분이 묘했다.
300|
301|‘살짝, 이라고.’
302|
303|검을 수련한 지 어느덧 이십여 년이 지났다. 재능과 노력을 바탕으로 이 자리에 올랐다.
304|
305|세인들은 자신을 천재라고 불렀고, 진천검이라는 별호를 붙여 주었으며 십봉룡이라 칭했다.
306|
307|단 한 번도 그런 허명(虛名)에 취한 적이 없다고 생각했는데…….
308|
309|‘나도 아직 한참 멀었군.’
310|
311|어느새 자신을 우러러보는 사람들의 시선에 익숙해져 있었던 모양이다.
312|
313|얼마 전 풍양에게 당한 상처가 다시 욱신거리는 듯했다.
314|
315|“그거 아시오?”
316|
317|“뭘요?”
318|
319|“당신이 강하다는 것.”
320|
321|“사실 얼마 전까지 확신하지 못했어요. 하지만 이제는 알겠네요.”
322|
323|“나를 만나서?”
324|
325|“네. 진 소협을 만나서. 십봉룡이 어느 정도인지 알게 됐으니까요.”
326|
327|“그렇소?”
328|
329|진무경이 피식 웃었다.
330|
331|재미있는 놈이다. 이미 구파일방의 장로에 버금가는 무공, 혹은 그 이상이면서도 때 묻지 않은 순수함. 솔직함.
332|
333|무인이지만 무림에는 어울리지 않는 놈이다.
334|
335|‘내가 아는 누구랑은 정반대로군.’
336|
337|문득 한 사람이 떠오른다.
338|
339|무림 어디에 던져 놔도 어떻게든 살아남을 것 같은 놈, 동시에 가장 무인답지 않게 싸우는 놈이.
340|
341|“나이가 어떻게 되시오?”
342|
343|“올해로 약관입니다.”
344|
345|“마침 나이도 같군. 우연인가? 아니면 인연?”
346|
347|“네?”
348|
349|진무경은 대답 대신에 고개를 저었다.
350|
351|사실 이 비무의 결과는 이미 알고 있다. 청풍의 전신에서 넘실거리는 자하신공의 기운이 그만큼 압도적이었으니까.
352|
353|이 정도의 고수를 상대로 모든 기량을 펼치지 못하는 것이 아쉬울 뿐이다.
354|
355|‘이럴 때 저 녀석이라면 어떻게 했을까?’
356|
357|진무경은 자신의 사고뭉치 동생을 흘끗 바라봤다. 놈은 악동 같은 웃음과 함께 입을 벙긋거리고 있었다.
358|
359|넌. 좆. 됐. 다.
360|
361|이런 쳐 죽일 놈을 봤나. 허탈하게 웃은 진무경이 검파에 손을 올렸다. 단전에서 끓어오른 공력이 사지백해로 뻗어 나간다.
362|
363|청풍이 진무경의 검을 바라보며 입을 열었다.
364|
365|“할아버지께서 그런 말씀도 해 주셨어요. 비무에는 기수식 따위 필요 없다.”
366|
367|“동감이오.”
368|
369|다음 순간.
370|
371|거대한 굉음과 함께 자줏빛 광염과 은빛 검기가 격돌했다.
```

## Assembled English

```markdown
[P1]
# Chapter 148

[P2]
In the atmosphere warmed by the enormous sum of a hundred thousand nyang, Jin Wikyung and Hong Jin exchanged greetings.

[P3]
“I am Jin Wikyung of the Jin Family of Taiyuan. It is an immense pleasure to meet the Deputy Military Commissioner I’ve heard so much about.”

[P4]
“To receive such a warm welcome from the Lesser Family Head of the great Jin Family of Taiyuan—I hardly know what to do with myself. Please, call me Comrade Hong from now on.”

[P5]
“Even so, how could I address an official that casually?”

[P6]
“Come now, you’re being too stiff. I said to call me casually.”

[P7]
“Ha-ha. Then shall I, Comrade Hong?”

[P8]
What was with the sudden communist atmosphere?

[P9]
As I wondered whether I was in Pyongyang or the Murim, Jin Wikyung finished exchanging introductions and turned his gaze toward me.

[P10]
“Hmm. Taekyung, you’re here?”

[P11]
“Yes.”

[P12]
His voice was heavier than usual, so I answered politely and read the room.

[P13]
Apparently, he understood that acting as he normally did in front of outsiders would not only damage his personal dignity but also humiliate the entire family.

[P14]
“So, did you greet His Highness properly?”

[P15]
*Properly? I didn’t just greet him. I even held a private autograph session.*

[P16]
Hong Jin smiled and patted my shoulder.

[P17]
“His Highness was delighted. He’d always wanted to meet Young Master Jin here.”

[P18]
“Oh, is that so?”

[P19]
“Yes. He was so happy, he simply wouldn’t let him go.”

[P20]
“Uhehehe. It seems our youngest—no. It seems His Highness has taken quite a liking to my younger brother.”

[P21]
“I can see why. He’s handsome, tall, and well-built. He’s strong in martial arts and has such an easygoing personality. Who could dislike him?”

[P22]
“Ahem. It feels rather awkward to say this myself, but Taekyung truly is an extraordinary talent. If he had been born into one of the Five Great Families instead of our family, no one would be surprised if he became the greatest under heaven.”

[P23]
Jin Wikyung got so carried away that he forgot all about acting dignified. As he chattered excitedly, Hong Jin’s expression hardened.

[P24]
“The greatest under heaven? Lesser Family Head Jin, that joke goes too far.”

[P25]
“Pardon? What do you mean?”

[P26]
“You’re saying Young Master Jin has what it takes to become the greatest under heaven? Even if I have no connection to the Murim, surely you aren’t making light of me.”

[P27]
“……Ahem.”

[P28]
As the atmosphere instantly turned cold, Jin Wikyung gave an uncomfortable cough. Hong Jin immediately continued.

[P29]
“Someone like Young Master Jin could become the greatest of all time.”

[P30]
“……!”

[P31]
“Allow me to congratulate you in advance, Lesser Family Head. For the greatest of all time to come from the Jin Family of Taiyuan—what a blessing for Shanxi Province.”

[P32]
Jin Wikyung cried out, overcome with emotion.

[P33]
“Comrade Hong!”

[P34]
“Lesser Family Head Jin!”

[P35]
“……”

[P36]
They say Hong Jin lived in the imperial palace for twenty years. His skill with his tongue certainly wasn’t ordinary.

[P37]
I clicked my tongue as I watched Jin Wikyung rejoice as though he had found his soulmate.

[P38]
“This won’t do. There’s no point staying here. I’ve already arranged a place, so why don’t we have a drink?”

[P39]
“What should I do? I’m not very good with alcohol.”

[P40]
“Ah, what a shame.”

[P41]
“The only time I can’t drink is when there’s none to be had.”

[P42]
“Comrade Hong!”

[P43]
“Lesser Family Head Jin!”

[P44]
“……”

[P45]
“……”

[P46]
Look at how perfectly they clicked together.

[P47]
When the two men disappeared, laughing loudly with their arms around each other’s shoulders, Wipeng stared at me with an utterly dumbfounded expression.

[P48]
“Is that man really the Deputy Military Commissioner?”

[P49]
“Unfortunately, yes.”

[P50]
“I heard he was once a palace attendant, but I never imagined he would be so frivolous.”

[P51]
Well, then what did that make Jin Wikyung, a martial artist who had played along with every bit of it?

[P52]
Jin Mukyung, who had been wearing a sour expression for some time, finally spoke.

[P53]
“That’s just the kind of man he is. Last time, he subtly stroked my shoulder. I barely stopped myself from breaking his arm.”

[P54]
He tore the cloth in his hands to shreds and flung it to the ground. Looking much more relieved, he said,

[P55]
“Then I have important business, so I’ll be leaving.”

[P56]
“What business? Training again, I assume.”

[P57]
“Is anything more important to a martial artist than training?”

[P58]
“……No.”

[P59]
That left me with nothing to say.

[P60]
As I stood there at a loss, merely smacking my lips, a clear, ringing voice rang out.

[P61]
“Wow, that’s exactly what my grandfather always says.”

[P62]
Wipeng and Jin Mukyung’s gazes pierced Cheongpung like awls.

[P63]
To ordinary people, Cheongpung was merely a young man with a slightly unusual air about him. To masters, however, he was something else entirely.

[P64]
When both men’s eyebrows shot upward, Cheongpung turned to me with a flustered expression.

[P65]
“Uh, Benefactor. Did I do something wrong?”

[P66]
“Wrong? Of course not. They’re just intrigued. Right, gentlemen?”

[P67]
Neither man took his eyes off Cheongpung. They merely nodded.

[P68]
An extraordinarily young Peak master. It was only natural that they would be curious about the identity of this Cheongpung who had suddenly appeared out of nowhere.

[P69]
“While we’re at it, why don’t you introduce yourselves? This is Cheongpung.”

[P70]
Before I had even finished speaking, Cheongpung bowed deeply.

[P71]
“Hello, I’m Cheongpung! I’ve only been in Shanxi for a few days. Before that, I was in Henan, and before that…”

[P72]
*Where did this guy crawl out of?*

[P73]
The question was written all over their faces.

[P74]
Just as I expected. I explained Cheongpung’s identity simply and clearly.

[P75]
“He’s the Sword Saint’s disciple.”

[P76]
“……!”

[P77]
“……!”

[P78]
The name of Sword Saint Mae Jonghak was practically a cheat code among martial artists.

[P79]
Both men gaped at Cheongpung, too stunned to speak. Cheongpung cautiously asked,

[P80]
“Um, which of you is the Heaven Shaking Sword?”

[P81]
Still reeling from the shock, Jin Mukyung stammered out a reply.

[P82]
“I-I’m the Heaven Shaking Sword. But are you really the Sword Saint, Great Hero Mae Jonghak’s…?”

[P83]
“Yes. He’s my grandfather.”

[P84]
“Gasp!”

[P85]
He looked several times more shocked than when he had seen the Flame Divine Palm martial arts manual.

[P86]
A young man claiming to be the disciple—and grandson—of a Supreme Peak master who was known to have gone into seclusion decades ago had suddenly appeared before them. Their reaction was understandable.

[P87]
“This can’t be…”

[P88]
“The Sword Saint’s successor…”

[P89]
Cheongpung looked back and forth between the two astonished men, then smiled brightly.

[P90]
“I didn’t know either until I came down the mountain.”

[P91]
“Y-Young Hero. Did Great Hero Mae also descend the mountain…?”

[P92]
His voice was filled with expectation and excitement.

[P93]
Both men were swordsmen who had trained with the sword their entire lives. Mae Jonghak had attained such heights in the Way of the Sword that he had earned the title Sword Saint. To them, he was practically a god.

[P94]
But Cheongpung’s answer shattered their expectations.

[P95]
“No. I snuck out alone. There were people I wanted to meet.”

[P96]
“Ah…”

[P97]
“How unfortunate…”

[P98]
“But putting that aside…”

[P99]
Cheongpung looked at the two crestfallen men before speaking again.

[P100]
His gleaming eyes had been fixed on Jin Mukyung for some time now.

[P101]
“Are you really Young Hero Jin Mukyung, the Heaven Shaking Sword? The one from the Ten Dragons and Phoenixes?”

[P102]
“That’s right. I am Jin Mukyung.”

[P103]
“Wow, I finally found you!”

[P104]
“……Hmm?”

[P105]
“I’ve been searching everywhere for you. From Heaven’s Gate Temple in Henan all the way here.”

[P106]
*What? The person that guy had been looking for was Jin Mukyung?*

[P107]
Wipeng, as well as Jin Mukyung himself, asked with bewildered expressions,

[P108]
“You were looking for me?”

[P109]
“Yes. Since you were nearby, I thought you’d be a decent place to start.”

[P110]
“A first? What does that mean?”

[P111]
“A dueling tour.”

[P112]
Cheongpung smiled softly. It was completely different from the bright, innocent smile I had seen from him until now.

[P113]
“I decided it while coming down the mountain. I won’t return until I’ve defeated all the Ten Dragons and Phoenixes.”

[P114]
“……!”

[P115]
“My grandfather told me this: A martial artist has no need for conversation. We contend through martial arts alone.”

[P116]
Sssss.

[P117]
At that moment, I felt a wave of heat. Violet light-flames had risen around Cheongpung’s entire body, surging upward.

[P118]
I had already seen this once before.

[P119]
*The Zaha Divine Technique.*

[P120]
The Extreme Yang qi burned the cold away. The earth melted, and the soil scorched. Cheongpung opened his mouth with all traces of his smile gone.

[P121]
“Shall we move somewhere else?”

[P122]
“Is there any need?”

[P123]
Jin Mukyung continued.

[P124]
“Draw your sword.”

[P125]
* * *

[P126]
Jin Mukyung let out a long breath. His rapidly beating heart slowly began to settle. Breathing was important in battle. Only now was he finally ready to draw his sword.

[P127]
As he placed a hand on the hilt, he thought of one man’s name.

[P128]
*Sword Saint Mae Jonghak.*

[P129]
Not once had he forgotten that name since the day he first held a sword.

[P130]
A legendary swordsman said to have reached the ultimate realm of the sword—or perhaps a realm beyond it.

[P131]
Everyone revered the Sword Saint, but Jin Mukyung was different.

[P132]
*Someday, I will defeat him.*

[P133]
If anyone had heard him say that, they would have snorted. They would have pointed at him and called him crazy.

[P134]
No matter how much of a genius Jin Mukyung was, he could never reach the Sword Saint’s name. Ever since Mae Jonghak had begun to be called the Sword Saint, no one had surpassed him.

[P135]
Decades ago, Sword Saint Mae Jonghak had already written a new chapter in the history of the orthodox Murim and become the protagonist of a legend.

[P136]
*It doesn’t matter. This is my goal.*

[P137]
It was not reckless arrogance. It was a goal.

[P138]
A goal he had etched into his bones and heart every day as he trained with his sword.

[P139]
And at this very moment, someone who had inherited everything from Sword Saint Mae Jonghak stood before him.

[P140]
“My grandfather used to tell me, ‘Compared to the Ten Dragons and Phoenixes, you are nothing. Don’t become arrogant.’”

[P141]
Cheongpung slowly stepped forward. A single blue-steel sword dangled from his waist, tied on haphazardly, and his footsteps were as light as though he had come out for a stroll.

[P142]
But…

[P143]
*There are no openings.*

[P144]
He looked utterly careless, but Jin Mukyung had no idea when or how he could attack.

[P145]
Jin Mukyung licked his parched lips.

[P146]
“I’ve never even met him… He praised me too highly.”

[P147]
“No. Honestly, you surprised me a little. I mean that.”

[P148]
Jin Mukyung knew that Cheongpung meant every word. That only made him feel stranger.

[P149]
*Only a little?*

[P150]
It had been more than twenty years since he began training with the sword. Talent and effort had brought him this far.

[P151]
People called him a genius, gave him the martial title Heaven Shaking Sword, and counted him among the Ten Dragons and Phoenixes.

[P152]
He had believed he had never once become drunk on such empty fame, but…

[P153]
*I still have a long way to go.*

[P154]
At some point, he must have grown accustomed to the gazes of people who looked up to him.

[P155]
The wound Pung Yang had inflicted on him not long ago seemed to throb again.

[P156]
“Do you know something?”

[P157]
“What?”

[P158]
“That you’re strong.”

[P159]
“Until recently, I wasn’t certain. But now I know.”

[P160]
“Because you met me?”

[P161]
“Yes. Because I met you, Young Hero Jin. Now I know what the Ten Dragons and Phoenixes are capable of.”

[P162]
“Is that so?”

[P163]
Jin Mukyung let out a quiet laugh.

[P164]
What an interesting guy. He possessed martial arts that rivaled—or even surpassed—those of an Elder of the Nine Sects and One Gang, yet he remained untainted by the world. He was pure. Honest.

[P165]
He was a martial artist, but he didn’t fit in the Murim.

[P166]
*He’s the exact opposite of someone I know.*

[P167]
One person suddenly came to mind.

[P168]
A guy who seemed like he could somehow survive no matter where he was thrown in the Murim, and who fought in the least martial-artist-like way imaginable.

[P169]
“How old are you?”

[P170]
“I turned twenty this year.”

[P171]
“We’re even the same age. Coincidence? Or fate?”

[P172]
“What?”

[P173]
Instead of answering, Jin Mukyung shook his head.

[P174]
In truth, he already knew the outcome of this duel. The qi of the Zaha Divine Technique surging through Cheongpung’s entire body was that overwhelming.

[P175]
His only regret was that he couldn’t display the full extent of his skill against an opponent of this caliber.

[P176]
*What would that troublemaker do in a situation like this?*

[P177]
Jin Mukyung glanced at his troublesome younger brother. With a grin like a little devil’s, Taekyung was mouthing something.

[P178]
*You. Are. Fucked.*

[P179]
*What a goddamn bastard.*

[P180]
Laughing hollowly, Jin Mukyung placed a hand on his sword hilt. The internal energy boiling up from his dantian coursed through every part of his body.

[P181]
Cheongpung looked at Jin Mukyung’s sword and spoke.

[P182]
“My grandfather told me something else, too. A duel doesn’t need an opening stance or anything like that.”

[P183]
“I agree.”

[P184]
The next moment—

[P185]
With a tremendous boom, violet light-flames and silver Sword Energy collided.
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
# Chapter 148

[P2]
In the atmosphere warmed by the enormous sum of a hundred thousand nyang, Jin Wikyung and Hong Jin exchanged greetings.

[P3]
“I am Jin Wikyung of the Jin Family of Taiyuan. It is an immense pleasure to meet the Deputy Military Commissioner I’ve heard so much about.”

[P4]
“Being so warmly welcomed by the Lesser Family Head of the great Jin Family of Taiyuan leaves me at a loss. From now on, please just call me Comrade Hong.”

[P5]
“Even so, how could I address an official that casually?”

[P6]
“Come now, you’re being too stiff. I said to call me casually.”

[P7]
“Ha-ha. Then shall I, Comrade Hong?”

[P8]
What was with the sudden communist atmosphere?

[P9]
As I wondered whether I was in Pyongyang or the Murim, Jin Wikyung finished exchanging introductions and turned his gaze toward me.

[P10]
“Hmm. Taekyung, you’re here?”

[P11]
“Yes.”

[P12]
His voice was heavier than usual, so I answered politely and read the room.

[P13]
Apparently, he understood that acting as he normally did in front of outsiders would not only damage his personal dignity but also humiliate the entire family.

[P14]
“So, did you greet His Highness properly?”

[P15]
*Properly? I didn’t just greet him. I even held a private autograph session.*

[P16]
Hong Jin smiled and patted my shoulder.

[P17]
“His Highness was delighted. He’d always wanted to meet Young Master Jin here.”

[P18]
“Oh, is that so?”

[P19]
“Yes. He was so happy that he had no intention of letting him go.”

[P20]
“Uhehehe. It seems our youngest—no. It seems His Highness has taken quite a liking to my younger brother.”

[P21]
“I can see why. He’s handsome, tall, and well-built. He’s strong in martial arts, and he has such an easygoing personality. Who could dislike him?”

[P22]
“Ehem. It feels strange to say this myself, but Taekyung really is an extraordinary talent. If he had been born somewhere like the Five Great Families instead of our family, it wouldn’t be strange if he became the greatest under heaven.”

[P23]
Hong Jin’s expression hardened as Jin Wikyung got carried away, chattering excitedly and forgetting all about maintaining his dignity.

[P24]
“The greatest under heaven? Lesser Family Head Jin, that’s too much of a joke.”

[P25]
“Pardon? What do you mean?”

[P26]
“You’re saying Young Master Jin has what it takes to become the greatest under heaven? Even if I have no connection to the Murim, surely you aren’t making light of me.”

[P27]
“……Ahem.”

[P28]
As the atmosphere instantly turned cold, Jin Wikyung gave an uncomfortable cough. Hong Jin immediately continued.

[P29]
“Someone like Young Master Jin could become the greatest of all time.”

[P30]
“……!”

[P31]
“Allow me to congratulate you in advance, Lesser Family Head. For the greatest of all time to come from the Jin Family of Taiyuan—what a blessing for Shanxi Province.”

[P32]
Jin Wikyung cried out with a deeply moved expression.

[P33]
“Comrade Hong!”

[P34]
“Lesser Family Head Jin!”

[P35]
“……”

[P36]
They say Hong Jin lived in the imperial palace for twenty years. His skill with his tongue certainly wasn’t ordinary.

[P37]
I clicked my tongue as I watched Jin Wikyung rejoice as though he had found his soulmate.

[P38]
“This won’t do. There’s no point staying here. I’ve already arranged a place, so why don’t we have a drink?”

[P39]
“What should I do? I’m not very good with alcohol.”

[P40]
“Ah, what a shame.”

[P41]
“The only time I can’t drink is when there’s none to be had.”

[P42]
“Comrade Hong!”

[P43]
“Lesser Family Head Jin!”

[P44]
“……”

[P45]
“……”

[P46]
Look at how perfectly they clicked together.

[P47]
When the two men disappeared, laughing loudly with their arms around each other’s shoulders, Wipeng stared at me with an utterly dumbfounded expression.

[P48]
“Is that man really the Deputy Military Commissioner?”

[P49]
“Unfortunately, yes.”

[P50]
“I heard he was a former palace attendant, but I didn’t know he’d be so frivolous.”

[P51]
Well, then what did that make Jin Wikyung, a martial artist who had played along with every bit of it?

[P52]
Jin Mukyung, who had been wearing a sour expression for some time, finally spoke.

[P53]
“That’s just the kind of man he is. Last time, he subtly stroked my shoulder. I barely stopped myself from breaking his arm.”

[P54]
He ripped the cloth in his hands into strips and threw them onto the ground, then spoke with a much more relieved expression.

[P55]
“Then I have important business, so I’ll be leaving.”

[P56]
“What business? Training again, I assume.”

[P57]
“Is there anything more important to a martial artist than training?”

[P58]
“……No.”

[P59]
That left me with nothing to say.

[P60]
As I stood there at a loss, merely smacking my lips, a clear, ringing voice rang out.

[P61]
“Wow, that’s exactly what my grandfather always says.”

[P62]
Wipeng and Jin Mukyung’s gazes pierced Cheongpung like awls.

[P63]
To ordinary people, Cheongpung was merely a young man with a slightly unusual air about him. To masters, however, he was something else entirely.

[P64]
When both men’s eyebrows shot upward, Cheongpung turned to me with a flustered expression.

[P65]
“Uh, Benefactor. Did I do something wrong?”

[P66]
“What do you mean, wrong? They just found it interesting. Right, gentlemen?”

[P67]
Neither man took his eyes off Cheongpung. They merely nodded.

[P68]
An extraordinarily young Peak master. It was only natural that they would be curious about the identity of this Cheongpung who had suddenly appeared out of nowhere.

[P69]
“Since we’re here, why don’t you introduce yourselves? This is Cheongpung.”

[P70]
Before I had even finished speaking, Cheongpung gave a deep bow.

[P71]
“Hello, I’m Cheongpung! I’ve only been in Shanxi for a few days. Before that, I was in Henan, and before that…”

[P72]
*Where did this guy crawl out of?*

[P73]
The question was written plainly across both men’s faces.

[P74]
Just as I expected. I explained Cheongpung’s identity simply and clearly.

[P75]
“He’s the Sword Saint’s disciple.”

[P76]
“……!”

[P77]
“……!”

[P78]
The name of Sword Saint Mae Jonghak was practically an instant cheat code among martial artists.

[P79]
When the two men stared at Cheongpung in shock, mouths hanging open and unable to speak, he asked cautiously,

[P80]
“Um, which of you is the Heaven Shaking Sword?”

[P81]
Jin Mukyung, who still hadn’t recovered from the shock, stammered out a reply.

[P82]
“I-I’m the Heaven Shaking Sword. But are you really the Sword Saint Mae Jonghak’s…?”

[P83]
“Yes. He’s my grandfather.”

[P84]
“Gasp!”

[P85]
He looked several times more shocked than when he had seen the Flame Divine Palm martial arts manual.

[P86]
A young man claiming to be the disciple—and grandson—of a Supreme Peak master who was known to have gone into seclusion decades ago had suddenly appeared before them. Their reaction was understandable.

[P87]
“This can’t be…”

[P88]
“He’s the Sword Saint’s successor…”

[P89]
Cheongpung looked back and forth between the two astonished men, then smiled brightly.

[P90]
“I didn’t know either until I came down the mountain.”

[P91]
“Y-Young Hero. Did Great Hero Mae also descend the mountain…?”

[P92]
His voice was filled with expectation and excitement.

[P93]
Both men had trained in swordsmanship their entire lives. To them, Mae Jonghak was practically a god—a man who had reached such a level in the Way of the Sword that he had earned the martial title of Sword Saint.

[P94]
But Cheongpung’s answer shattered their expectations.

[P95]
“No. I just snuck out by myself. There were people I wanted to meet.”

[P96]
“Ah…”

[P97]
“How unfortunate…”

[P98]
“But putting that aside…”

[P99]
Cheongpung looked at the two crestfallen men before speaking again.

[P100]
His bright eyes had been fixed on Jin Mukyung for some time.

[P101]
“Are you really Young Hero Jin Mukyung, the one from the Ten Dragons and Phoenixes?”

[P102]
“That’s right. I’m Jin Mukyung.”

[P103]
“Wow, I finally found you!”

[P104]
“……Hmm?”

[P105]
“I searched everywhere for you. From Heaven’s Gate Temple in Henan all the way here.”

[P106]
*What? The person that guy had been looking for was Jin Mukyung?*

[P107]
Wipeng, as well as Jin Mukyung himself, asked with bewildered expressions,

[P108]
“You were looking for me?”

[P109]
“Yes. Since you were nearby, I thought you’d be a decent place to start.”

[P110]
“A first? What does that mean?”

[P111]
“A dueling tour.”

[P112]
Cheongpung smiled softly. It was completely different from the bright, innocent smile I had seen from him until now.

[P113]
“I decided it while coming down the mountain. I won’t return until I’ve defeated all the Ten Dragons and Phoenixes.”

[P114]
“……!”

[P115]
“My grandfather told me this: A martial artist has no need for conversation. We settle things through martial arts alone.”

[P116]
Sssss.

[P117]
At that moment, I felt a wave of heat. Violet light-flames had risen around Cheongpung’s entire body, surging upward.

[P118]
I had already seen this once before.

[P119]
*The Zaha Divine Technique.*

[P120]
The Extreme Yang qi burned the cold away. The earth melted, and the soil scorched. Cheongpung opened his mouth with all traces of his smile gone.

[P121]
“Shall we move somewhere else?”

[P122]
“Is there any need?”

[P123]
Jin Mukyung continued,

[P124]
“Draw your sword.”

[P125]
* * *

[P126]
Jin Mukyung let out a long breath. His rapidly beating heart slowly began to settle. Breathing was important in battle. Only now was he finally ready to draw his sword.

[P127]
As he placed a hand on the hilt, he thought of one man’s name.

[P128]
*Sword Saint Mae Jonghak.*

[P129]
Not once had he forgotten that name since the day he first held a sword.

[P130]
A legendary swordsman who was said to have reached the ultimate realm of the sword—or perhaps a realm beyond it.

[P131]
Everyone revered the Sword Saint, but Jin Mukyung was different.

[P132]
*Someday, I’ll defeat him.*

[P133]
If anyone had heard him say that, they would have snorted. They would have pointed at him and called him crazy.

[P134]
No matter how talented Jin Mukyung was, he could never touch the Sword Saint’s level. Ever since Mae Jonghak had begun to be called the Sword Saint, no one had surpassed him.

[P135]
Sword Saint Mae Jonghak had written a new chapter in the history of the orthodox Murim decades ago and become the protagonist of a legend.

[P136]
*It doesn’t matter. This is my goal.*

[P137]
It wasn’t reckless arrogance. It was a goal.

[P138]
A goal he had etched into his bones and heart every day as he trained with his sword.

[P139]
And at this very moment, someone who had inherited everything from Sword Saint Mae Jonghak stood before him.

[P140]
“My grandfather used to tell me this. ‘Compared to the Ten Dragons and Phoenixes, you are nothing. Don’t become arrogant.’”

[P141]
Cheongpung slowly stepped forward. A single blue-steel sword dangled from his waist, tied on haphazardly, and his footsteps were as light as though he had come out for a stroll.

[P142]
But…

[P143]
*There are no openings.*

[P144]
He looked utterly careless, yet Jin Mukyung couldn’t figure out when or how he was supposed to attack him.

[P145]
Jin Mukyung licked his parched lips.

[P146]
“I’ve never even met him… He praised me too highly.”

[P147]
“No, honestly, you surprised me a little. I mean that.”

[P148]
Jin Mukyung knew that everything Cheongpung was saying was sincere. That only made it feel stranger.

[P149]
*Just a little?*

[P150]
More than twenty years had passed since he began training with the sword. He had reached this point through talent and effort.

[P151]
People had called him a genius, given him the martial title Heaven Shaking Sword, and counted him among the Ten Dragons and Phoenixes.

[P152]
He had believed that he had never once been intoxicated by such hollow fame, but…

[P153]
*I still have a long way to go.*

[P154]
At some point, he must have grown accustomed to the gazes of people who looked up to him.

[P155]
The wound Pung Yang had inflicted on him not long ago seemed to throb again.

[P156]
“Do you know something?”

[P157]
“What?”

[P158]
“That you’re strong.”

[P159]
“Until recently, I wasn’t certain. But now I know.”

[P160]
“Because you met me?”

[P161]
“Yes. Because I met Young Hero Jin. Now I know what the Ten Dragons and Phoenixes are capable of.”

[P162]
“Is that so?”

[P163]
Jin Mukyung let out a quiet laugh.

[P164]
What an interesting guy. He possessed martial arts that rivaled—or even surpassed—those of an Elder of the Nine Sects and One Gang, yet he remained untainted by the world. He was pure. Honest.

[P165]
He was a martial artist, but he didn’t fit in the Murim.

[P166]
*He’s the exact opposite of someone I know.*

[P167]
One person suddenly came to mind.

[P168]
A guy who seemed like he could somehow survive no matter where he was thrown in the Murim, and who fought in the least martial-artist-like way imaginable.

[P169]
“How old are you?”

[P170]
“I’m twenty this year.”

[P171]
“We’re the same age. Is it coincidence? Or fate?”

[P172]
“What?”

[P173]
Jin Mukyung shook his head instead of answering.

[P174]
In truth, he already knew the outcome of this duel. The qi of the Zaha Divine Technique surging through Cheongpung’s entire body was that overwhelming.

[P175]
It was merely regrettable that he couldn’t display all his abilities against an opponent of this caliber.

[P176]
*How would that troublemaker handle a situation like this?*

[P177]
Jin Mukyung glanced at his troublesome younger brother. With a grin like a little devil’s, Taekyung was mouthing something.

[P178]
*You. Are. Fucked.*

[P179]
*What a goddamn bastard.*

[P180]
Laughing hollowly, Jin Mukyung placed a hand on his sword hilt. The internal energy boiling up from his dantian coursed through every part of his body.

[P181]
Cheongpung looked at Jin Mukyung’s sword and spoke.

[P182]
“My grandfather told me something else, too. A duel doesn’t need an opening stance or anything like that.”

[P183]
“I agree.”

[P184]
The next moment—

[P185]
With a tremendous boom, violet light-flames and silver Sword Energy collided.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 천무학관   | **Heaven's Gate Temple**         |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 정파     | **orthodox faction**                             |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장로     | **Elder**                                    |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 극양                        | **Extreme Yang**      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 내관 | **palace attendant** | Hong Jin's former palace role; context identifies him as a eunuch. |
| 대태원진가 | **great Jin Family of Taiyuan** | Formal exalted reference to the Jin Family of Taiyuan. |
| 평양 | **Pyongyang** | City invoked in Taekyung's communist-atmosphere joke. |
| 천하제일인 | **greatest under heaven** | Superlative martial distinction used in Hong Jin and Jin Wikyung's banter. |
| 고금제일인 | **greatest of all time** | Superlative martial distinction used in Hong Jin's exaggerated praise. |
| 비무행 | **dueling tour** | Cheongpung's planned journey to challenge the Ten Dragons and Phoenixes. |
| 청강검 | **blue-steel sword** | Cheongpung's sword. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 148,
  "passed": true,
  "metrics": {
    "source_characters": 5676,
    "translation_characters": 12813,
    "length_ratio": 2.257,
    "source_paragraphs": 183,
    "translation_paragraphs": 185
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
        "korean": "정파",
        "preferred": "orthodox faction"
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
        "korean": "인도",
        "preferred": "Human Butcher"
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
