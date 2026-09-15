# Fidelity Gate — Chapter 78

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
  1|＃78화
  2|
  3|
  4|
  5|헌터들은 하나같이 술고래다.
  6|
  7|최하급인 F급 헌터라고 해도 일반인을 훌쩍 뛰어넘는 신체 능력과 신진대사의 소유자들이니까.
  8|
  9|술을 안 먹는 헌터는 있어도 못 먹는 헌터는 없다는 말이 괜히 있는 게 아니다.
 10|
 11|“히끅. 한 잔 더.”
 12|
 13|그런데 여기 한 명 있었네.
 14|
 15|어느새 반쯤 눈이 풀린 송이 씨가 맹렬하게 빈 잔을 흔들었다.
 16|
 17|“한 잔 더어!”
 18|
 19|취한 모습도 예뻐……가 아니고. 이 정도면 살짝 위험한 거 아닌가? 나는 걱정스러운 눈빛으로 송이 씨를 바라봤다.
 20|
 21|‘너무 급하게 마신 것 같은데.’
 22|
 23|본격적으로 술자리가 시작되자마자 소주 한 병을 나발로 불더니 쭉 저 상태다. 가끔은 혀 꼬인 발음으로 눈치도 더럽게 없다느니, 재수 옴 붙었다느니 하는 뜻 모를 소리를 중얼거리기도 했다.
 24|
 25|‘안 좋은 일이라도 있는 건가?’
 26|
 27|임꺽정이 그녀의 술잔을 채워 주는 틈을 타 최 팀장에게 소곤거렸다.
 28|
 29|“팀장님. 송이 씨 무슨 일 있었어요?”
 30|
 31|최 팀장이 떨떠름한 얼굴로 대답했다.
 32|
 33|“……있긴 있죠.”
 34|
 35|“역시.”
 36|
 37|“그것도 아주 최근에.”
 38|
 39|“앗. 아아.”
 40|
 41|송이 씨의 불행은 곧 나의 불행. 지켜보고만 있자니 억장이 무너진다.
 42|
 43|“후우. 잘 해결됐으면 좋겠네요.”
 44|
 45|“…….”
 46|
 47|“…….”
 48|
 49|최 팀장은 물론이고 옆에 앉아 있던 김 집사까지 괴상한 표정으로 나를 바라본다.
 50|
 51|이거 왠지 기분이 이상해지는데.
 52|
 53|“왜요?”
 54|
 55|“아닙니다.”
 56|
 57|“젊을 때는 그럴 수도 있죠.”
 58|
 59|어째 미적지근한 대답이지만 지금 그게 중요한 게 아니다.
 60|
 61|까드득.
 62|
 63|“마셔요! 오늘 마시고 죽어!”
 64|
 65|세 병째 소주를 깐 송이 씨가 미쳐 날뛰고 있었으니까.
 66|
 67|“으하하! 난 이래서 송이 씨가 참 좋더라!”
 68|
 69|물 만난 고기. 아니, 술 만난 산적처럼 옆에서 거드는 임꺽정은 덤이다.
 70|
 71|“말려야 되는 거 아니에요?”
 72|
 73|“아, 송이 씨요?”
 74|
 75|“네.”
 76|
 77|최 팀장이 어깨를 으쓱했다.
 78|
 79|“괜찮습니다. 하루 이틀 본 것도 아니고. 송이 씨 술버릇이 원래 저래요.”
 80|
 81|“아무리 그래도…… 아니 잠깐만.”
 82|
 83|나는 최 팀장을 지그시 노려봤다.
 84|
 85|아까부터 수상하다 싶었는데, 이제야 덜미를 잡았다.
 86|
 87|“팀장님이 송이 씨 술버릇을 어떻게 압니까?”
 88|
 89|“같이 술을 마셨으니까 알죠.”
 90|
 91|“…….”
 92|
 93|이 자식이 누굴 놀리나. 내가 그걸 몰라서 물어본 것 같니?
 94|
 95|“그 얘기가 아니잖아요.”
 96|
 97|“그럼 어떤 얘깁니까?”
 98|
 99|“그러니까…….”
100|
101|막상 이렇게 나오니까 할 말이 없다. 생각해 보면 내가 뭐라고 두 사람 관계를 따진단 말인가?
102|
103|순간 말문이 막힌 그때, 최 팀장이 불쑥 입을 열었다.
104|
105|“아레스. 들어 보셨죠?”
106|
107|“당연하죠.”
108|
109|전신(戰神) 아레스.
110|
111|고대 그리스 로마 신화에 등장하는 신의 이름이다. 지금에 이르러서는 다른 의미로 유명해졌지만.
112|
113|“아레스 길드 모르는 사람이 어디 있어요?”
114|
115|대한민국 헌터의 자존심이자 자부심.
116|
117|국내에는 수백 개의 길드가 존재하지만 정점은 오직 하나, 아레스 길드였다. 대격변 초기부터 지금까지 그들이 이룩한 위업은 셀 수 없이 많다.
118|
119|‘말 그대로 전설이지, 전설.’
120|
121|학습 만화, 교육 애니메이션, 영화와 소설 등등. 심지어는 교과서에도 나온다.
122|
123|아레스 길드가 국내에서 차지하는 위치는 살아 있는 세종대왕이요, 현역 이순신 장군에 버금간다. 아니, 그 이상일 것이다.
124|
125|‘세계적으로 워낙 유명하니까.’
126|
127|두 유노 킹 세종? 킹 갓 제너럴 순신 리? 하고 물어보면 대다수의 외국인들은 이 동양인 새끼가 뭐라는 거야, 하겠지만 아레스 길드는 다르다.
128|
129|- 두 유노 아레스?
130|
131|- 오, 예쓰!
132|
133|터프하기 짝이 없는 텍사스 할아버지도 쌍권총을 탁 치며 알아듣는다는 게 학계 정설이다.
134|
135|“그런데 아레스 길드는 왜요?”
136|
137|맥주 한 모금을 삼킨 최 팀장이 대답했다.
138|
139|“제가 거기 있었거든요.”
140|
141|“아. 그렇구나…… 예?”
142|
143|내가 지금 무슨 말을 들은 거지?
144|
145|말문이 막혀 한동안 눈만 껌뻑이다가 입을 열었다.
146|
147|“아레스 길드 소속이셨다고요?”
148|
149|“팀장이었습니다. 그래 봤자 한참 말단이지만.”
150|
151|아레스 길드의 문턱은 높다. 최고만 가려서 뽑고, 최고로 길러 낸다. 최 팀장은 스스로를 한참 말단이라고 했지만 이미 거기서 팀장을 달았다는 것부터가 대단한 거다.
152|
153|지금 내 눈에는 그냥 미친놈처럼 보이지만.
154|
155|“아니, 거길 왜 나왔어요?”
156|
157|돈, 명예, 지위.
158|
159|헌터라면, 남자라면 바라마지 않는 최고의 직장이다. 그걸 걷어차고 나오다니!
160|
161|“혹시 사내 왕따, 뭐 그런 거 당했어요?”
162|
163|곰곰이 생각하던 최 팀장이 대답했다.
164|
165|“그랬을 수도 있겠네요. 절 편하게 대해 주는 사람은 송이 씨밖에 없었으니까.”
166|
167|“……그럼 송이 씨도 아레스 길드?”
168|
169|“제 팀원이었습니다. 팀 회식 때 술버릇을 알게 됐죠.”
170|
171|침이 목울대를 타고 꿀꺽 넘어간다.
172|
173|‘이거 완전 엘리트들이잖아.’
174|
175|맥주를 홀짝이는 최 팀장과 병나발을 불고 있는 송이 씨를 번갈아 보던 내 시선이 한 사람에게 멈췄다.
176|
177|“혹시 김 집사님께서도……?”
178|
179|“저 말입니까?”
180|
181|김 집사가 인자하게 웃으며 손을 내저었다.
182|
183|“전 이미 오래전에 은퇴했습니다. 허허허.”
184|
185|“네?”
186|
187|그럼 전직 헌터란 소린데.
188|
189|문득 김 집사를 대할 때마다 느꼈던 이질감이 떠올랐다. 지금까지 단 한 번도 그를 [기감]으로 파악해 보지 않았다는 사실도.
190|
191|‘이 사람, 정체가 뭐지?’
192|
193|기감을 끌어 올리려던 그때.
194|
195|우리가 이야기를 나누건 말건 열심히 술과 고기를 흡입하던 임꺽정이 말했다.
196|
197|“어, 버너 불 꺼졌다. 송 양. 가스 새 거 없어?”
198|
199|“히끅. 그게 마지막이었는데요.”
200|
201|“에이, 흐름 끊기면 안 되는데. 그냥 먹을까?”
202|
203|한참 설익은 고기를 뒤집으며 투덜거리는 임꺽정을 향해, 김 집사가 부드럽게 웃어 보였다.
204|
205|“그럼 안 되죠.”
206|
207|그리고 다음 순간, 두 가지 일이 동시에 일어났다.
208|
209|딱!
210|
211|김 집사가 손가락을 튕겼고.
212|
213|화아아악!
214|
215|후끈한 열기가 뿜어져 나왔다. 정확히 불판 위로 솟구친 푸른 불꽃은 순식간에 판을 달구고 고기를 익힌 뒤 사라졌다.
216|
217|“이건…….”
218|
219|나와 임꺽정은 누가 먼저랄 것도 없이 외쳤다.
220|
221|“마법사!”
222|
223|“엄청 잘 구웠어!”
224|
225|“…….”
226|
227|“왜? 태경이 너도 빨리 먹어.”
228|
229|됐네, 이 양반아. 나는 고개를 절레절레 저었다.
230|
231|그보다 김 집사가 마법사였을 줄이야. 어쩐지 느낌이 이상하더라니.
232|
233|“깜빡 속았네요.”
234|
235|김 집사가 잘 익은 고기를 한 점 집어 올렸다.
236|
237|“속일 생각은 없었습니다. 저야 말씀드렸다시피 이미 은퇴한 퇴물이니까요.”
238|
239|퇴물은 무슨. 김 집사가 퇴물이면 지금 현역으로 활동하는 마법사 중에 절반은 대가리 박아야 한다.
240|
241|‘최소 B급 이상.’
242|
243|손가락 한 번 튕기는 것만으로도 불꽃을 불러내고 고기를 태우지도, 덜 익히지도 않고 알맞게 구울 만큼 컨트롤 역시 정교하다. 정황을 미루어 볼 때 은퇴 전에는 그 역시 아레스 길드 소속이었을 것이다.
244|
245|만약 대격변 때도 활동한 인물이라면.
246|
247|‘……이거 거물인데?’
248|
249|거기에 더해 까마득한 대선배다.
250|
251|나는 조심스럽게 물었다.
252|
253|“저어, 혹시 헌터 훈련소는 어디 나오셨는지.”
254|
255|“논산 나왔습니다. 태경 씨는요?”
256|
257|“헉. 저도 논산입니다. 28연대 1대대.”
258|
259|“그래요? 이거 우연이네요. 나도 28연대 1대대 나왔는데. 몇 중대 출신이에요?”
260|
261|“2중댑니다.”
262|
263|“우연이 아니라 인연인가 보네요. 하하.”
264|
265|두말할 필요가 없다. 자리에서 일어난 나는 허리를 꺾었다.
266|
267|“반갑습니다, 선배님.”
268|
269|대한민국은 학연, 지연, 혈연이라는 말이 있다. 헌터도 마찬가지다.
270|
271|각성 확률은 0.1퍼센트. 천 명당 하나꼴이고 이런 희박한 확률 때문에 사회에서 알던 지인이 각성하는 경우는 드물다. 별것 아닌 것처럼 보이는 헌터 훈련소가 인맥의 시작점인 셈이다.
272|
273|“뭘 또 이렇게까지. 앉으세요.”
274|
275|“말씀 편하게 하셔도 됩니다.”
276|
277|“저는 그런 거 안 따지니까…….”
278|
279|나와 김 집사가 선후배 간의 훈훈한 분위기를 연출하고 있던 그때, 가만히 지켜보던 최 팀장이 불쑥 끼어들었다.
280|
281|“김 집사님. 진태경 씨 말대로 하는 게 어떻겠습니까?”
282|
283|이런 버르장머리 없는 놈을 봤나. 감히 대선배님께 이래라저래라…….
284|
285|‘으음. 할 수 있지.’
286|
287|생각해 보면 최 팀장이 더 거물이다. 아레스 길드 출신 마법사를 집사로 쓰는 놈이니까.
288|
289|‘도대체 어떤 집안이길래.’
290|
291|할아버지가 대통령이고 아버지가 국무총리쯤 되나?
292|
293|궁금증만 더해 갈 때 최 팀장의 말이 이어졌다.
294|
295|“이쯤에서 호칭 정리를 해야겠죠. 명색이 우리 길드의 얼굴이신데 언제까지 집사님이나 아저씨라고 부를 수는 없는 것 아닙니까?”
296|
297|잠시 고민하던 김 집사가 대답했다.
298|
299|“도련님 말씀에 따르겠습니다.”
300|
301|고개를 끄덕인 최 팀장이 준엄한 눈빛으로 좌중을 쓸어 보았다.
302|
303|“그럼 앞으로 김 집사님에 대한 호칭은 길드장님으로 통일합니다. 이의 없으시죠?”
304|
305|임꺽정과 송이 씨가 대답했다.
306|
307|“크, 고기 맛 죽이네. 마법으로 구워서 그런가?”
308|
309|“술이 들어간다. 술! 술술, 술술!”
310|
311|“…….”
312|
313|회한 어린 눈빛으로 두 사람을 응시한 최 팀장이 내게 시선을 돌렸다. 나는 보란 듯이 한쪽 팔을 들고 있었다.
314|
315|“그건 무슨 뜻입니까?”
316|
317|“질문드릴 게 있어서요.”
318|
319|그나마 이놈은 좀 낫군. 최 팀장이 그런 얼굴로 말했다.
320|
321|“말씀하세요.”
322|
323|“최 팀장님이 길드장 아니었습니까?”
324|
325|“…….”
326|
327|배신당한 듯한 표정을 지은 최 팀장이 품에서 뭔가를 꺼내 건넸다. 받아 살펴보니 명함이다.
328|
329|“저 이거 있는데요.”
330|
331|“뭐라고 적혀 있습니까?”
332|
333|“평화 길드 1팀장 최민우요.”
334|
335|“네. 저 팀장입니다.”
336|
337|“아.”
338|
339|“김 집사님이 길드장. 제가 팀장. 나머지 세 분이 팀원입니다. 이제 이해되셨습니까?”
340|
341|김 집사가 바지 사장인지, 얼굴마담인지는 모르겠지만 일단 고개를 끄덕였다. 그렇게 안 하면 최 팀장이 울 것 같아서.
342|
343|“다른 분들도 알아들으셨습니까?”
344|
345|최 팀장의 질문에 임꺽정과 송이 씨가 대답했다.
346|
347|“이야, 술맛도 죽이네. 마법으로 구운 고기가 안주라 그런가?”
348|
349|“언제까지 어깨춤을 추게 할 거야. 탈골됐잖아. 탈골! 탈골!”
350|
351|“…….”
352|
353|야, 우냐?
```

## Assembled English

```markdown
[P1]
# Chapter 78

[P2]
Hunters are all hard drinkers.

[P3]
Even an F-rank Hunter—the lowest classification—has physical abilities and a metabolism far beyond those of an ordinary person.

[P4]
There’s a reason people say some Hunters don’t drink, but no Hunter can’t drink.

[P5]
“Hic. One more glass.”

[P6]
Well, there was one here.

[P7]
Miss Song-i’s eyes were already half-glazed as she shook her empty glass furiously.

[P8]
“One more glaaass!”

[P9]
*She’s pretty even when she’s drunk… No, that’s not the point. Isn’t this getting a little dangerous?*

[P10]
I looked at Miss Song-i with concern.

[P11]
*She must’ve drunk too fast.*

[P12]
The moment the drinking party had begun in earnest, she had chugged an entire bottle of soju straight from the bottle and had been like this ever since. Every now and then, she slurred incomprehensible things about someone having no damn tact and rotten luck clinging like a curse.

[P13]
*Is something bad going on?*

[P14]
While Im Kkeokjeong was filling her glass, I leaned toward Team Leader Choi and whispered.

[P15]
“Team Leader. Did something happen to Miss Song-i?”

[P16]
Team Leader Choi answered with an awkward expression.

[P17]
“……Something did happen.”

[P18]
“I knew it.”

[P19]
“Very recently, too.”

[P20]
“Oh. Ah.”

[P21]
Miss Song’s misfortune was my misfortune. Just sitting there and watching her was breaking my heart.

[P22]
“Whew. I hope things work out for her.”

[P23]
“……”

[P24]
“……”

[P25]
Team Leader Choi, and even Butler Kim, who was sitting beside him, stared at me with strange expressions.

[P26]
This was starting to feel weird.

[P27]
“What?”

[P28]
“Nothing.”

[P29]
“People can be like that when they’re young.”

[P30]
It was an oddly lukewarm answer, but that wasn’t important right now.

[P31]
Crack.

[P32]
“Drink! Today, we drink ourselves to death!”

[P33]
Miss Song had opened her third bottle of soju and was going wild.

[P34]
“Ha-ha-ha! This is why I like Miss Song so much!”

[P35]
Like a fish in water—no, like a bandit who’d found booze—Im Kkeokjeong egged her on from beside her.

[P36]
“Shouldn’t we stop her?”

[P37]
“Ah, Miss Song-i?”

[P38]
“Yes.”

[P39]
Team Leader Choi shrugged.

[P40]
“It’s fine. It’s not like I’ve only known her for a day or two. That’s just how Miss Song gets when she drinks.”

[P41]
“Even so… No, wait a second.”

[P42]
I fixed Team Leader Choi with a penetrating stare.

[P43]
He’d seemed suspicious for a while, and now I’d finally caught him.

[P44]
“How do you know what Miss Song is like when she drinks?”

[P45]
“Because I’ve drunk with her.”

[P46]
“……”

[P47]
Was this bastard making fun of me? Did he think I was asking because I couldn’t figure that out?

[P48]
“That’s not what I mean.”

[P49]
“Then what do you mean?”

[P50]
“I mean…”

[P51]
Now that he’d put it that way, I had nothing to say. When I thought about it, who was I to question the relationship between them?

[P52]
Just as I found myself at a loss for words, Team Leader Choi suddenly spoke.

[P53]
“You’ve heard of Ares, right?”

[P54]
“Of course.”

[P55]
Ares, the god of war.

[P56]
The name of a god from ancient Greek and Roman mythology. These days, though, it was famous for something else.

[P57]
“Who in Korea doesn’t know the Ares Guild?”

[P58]
The pride and joy of Korea’s Hunters.

[P59]
Hundreds of Guilds existed in Korea, but only one stood at the top: the Ares Guild. From the early days of the Great Cataclysm to the present, their achievements had been too numerous to count.

[P60]
*They’re legends. Plain and simple.*

[P61]
They appeared in educational comics, educational animations, movies, novels, and all kinds of other media. They had even made it into textbooks.

[P62]
The Ares Guild held a position in Korea comparable to a living King Sejong or an active General Yi Sun-sin. No, perhaps even higher.

[P63]
*They’re famous all over the world, after all.*

[P64]
If you asked most foreigners, *Do you know King Sejong? King-God-General Yi Sun-sin?* they’d probably think, *What the hell is this Asian bastard talking about?* But the Ares Guild was different.

[P65]
*Do you know Ares?*

[P66]
*Oh, yes!*

[P67]
Even a tough-as-nails Texas grandpa would slap his twin pistols and know what you meant. That was the accepted academic consensus.

[P68]
“Why are you asking about the Ares Guild?”

[P69]
Team Leader Choi swallowed a mouthful of beer before answering.

[P70]
“Because I used to be there.”

[P71]
“Oh. I see… Huh?”

[P72]
What had I just heard?

[P73]
I blinked for a while before finally speaking.

[P74]
“You used to belong to the Ares Guild?”

[P75]
“I was a Team Leader. Though I was pretty far down the ladder.”

[P76]
The Ares Guild had high standards. They selected only the best and trained them to become even better. Team Leader Choi had called himself low-ranking, but the fact that he’d made Team Leader there was already incredible.

[P77]
Though right now, he just looked like a lunatic to me.

[P78]
“Then why did you leave?”

[P79]
Money, honor, status.

[P80]
It was the best job any Hunter—or any man—could dream of. And he had kicked it all away and left!

[P81]
“Were you ostracized at work or something?”

[P82]
Team Leader Choi thought about it for a moment before answering.

[P83]
“That might have been the case. Miss Song was the only person who treated me normally.”

[P84]
“……Then was Miss Song in the Ares Guild too?”

[P85]
“She was on my team. I found out about her drinking habits during team dinners.”

[P86]
I swallowed hard.

[P87]
*These people are total elites.*

[P88]
My gaze moved back and forth between Team Leader Choi, who was sipping his beer, and Miss Song, who was drinking straight from the bottle, before stopping on one person.

[P89]
“Could it be that Butler Kim also…?”

[P90]
“Me?”

[P91]
Butler Kim smiled kindly and waved a hand.

[P92]
“I retired a long time ago. Ha-ha-ha.”

[P93]
“What?”

[P94]
So he was a former Hunter.

[P95]
Suddenly, I remembered the sense of incongruity I had always felt whenever I dealt with Butler Kim. I had also never once tried to assess him with my Qi Sense.

[P96]
*Who is this man, really?*

[P97]
Just as I was about to raise my Qi Sense, Im Kkeokjeong, who had been enthusiastically inhaling meat and liquor whether or not we were talking, spoke up.

[P98]
“Oh, the burner went out. Miss Song, do we have another gas canister?”

[P99]
“Hic. That was the last one.”

[P100]
“Aw, we can’t let the momentum die. Should we just eat it?”

[P101]
Im Kkeokjeong grumbled as he flipped a piece of meat that was still mostly raw. Butler Kim smiled gently at him.

[P102]
“That won’t do.”

[P103]
The next moment, two things happened at once.

[P104]
Snap!

[P105]
Butler Kim snapped his fingers.

[P106]
Fwoosh!

[P107]
A wave of scorching heat burst forth. Blue flames surged precisely up over the grill, heating the plate and cooking the meat in an instant before vanishing.

[P108]
“This is…”

[P109]
Im Kkeokjeong and I shouted at the same time.

[P110]
“A mage!”

[P111]
“It’s cooked incredibly well!”

[P112]
“……”

[P113]
“What? Taekyung, hurry up and eat.”

[P114]
*Forget it, old man.*

[P115]
I shook my head back and forth.

[P116]
More importantly, who would’ve guessed Butler Kim was a mage? No wonder something about him had always felt strange.

[P117]
“You really had me fooled.”

[P118]
Butler Kim picked up a well-cooked piece of meat.

[P119]
“I had no intention of fooling you. As I told you, I’m already a retired has-been.”

[P120]
*Has-been, my ass.*

[P121]
If Butler Kim was a has-been, half the mages still active today ought to bow their damn heads.

[P122]
*At least B-rank.*

[P123]
He could summon flames with a single snap of his fingers and control them precisely enough to cook the meat just right without burning or undercooking it. Judging from the circumstances, he had probably belonged to the Ares Guild as well before retiring.

[P124]
If he had been active during the Great Cataclysm, too…

[P125]
*……This guy’s a big shot.*

[P126]
On top of that, he was an incredibly senior one.

[P127]
I asked cautiously, “Um, which Hunter training center did you graduate from?”

[P128]
“Nonsan.[^1] What about you, Mr. Taekyung?”

[P129]
“Gasp. Me too. The 28th Regiment, 1st Battalion.”

[P130]
“Really? What a coincidence. I was in the 28th Regiment, 1st Battalion too. Which company were you in?”

[P131]
“Second Company.”

[P132]
“Then perhaps it isn’t a coincidence but fate. Ha-ha.”

[P133]
There was nothing more to discuss. I rose from my seat and bowed deeply at the waist.

[P134]
“Nice to meet you, Senior.”

[P135]
[^1]: Nonsan is home to Korea’s main Army recruit training center.

[P136]
There’s a saying in Korea about school ties, regional ties, and blood ties.[^2] Hunters were no different.

[P137]
The chance of awakening was 0.1 percent—one in a thousand. With odds that slim, it was rare for anyone you knew from ordinary life to awaken. The Hunter training center might not seem like much, but it was where a Hunter’s network began.

[P138]
“You don’t have to go this far. Please, sit down.”

[P139]
“You can speak casually with me.”

[P140]
“I don’t really stand on ceremony…”

[P141]
Just as Butler Kim and I were creating a warm atmosphere between Senior and junior, Team Leader Choi, who had been watching quietly, suddenly cut in.

[P142]
“Butler Kim. Why don’t you do as Mr. Jin Taekyung says?”

[P143]
*What an ill-mannered bastard. How dare he tell such a distinguished Senior what to do…*

[P144]
*Hmm. I guess he can.*

[P145]
Come to think of it, Team Leader Choi was the bigger shot. He employed a former Ares Guild mage as his butler.

[P146]
*What kind of family does he come from?*

[P147]
Was his grandfather the president and his father the prime minister?

[P148]
As my curiosity continued to grow, Team Leader Choi went on.

[P149]
“I think it’s time we sorted out everyone’s forms of address. You’re the face of our Guild, after all. We can’t keep calling you Butler Kim or Uncle forever, can we?”

[P150]
Butler Kim considered it for a moment before answering.

[P151]
“I’ll follow the Young Master’s wishes.”

[P152]
Team Leader Choi nodded and swept a stern gaze over everyone present.

[P153]
“Then from now on, we’ll all address Butler Kim as Guild Master. No objections, correct?”

[P154]
Im Kkeokjeong and Miss Song answered.

[P155]
“Man, this meat is incredible. Is it because it was grilled with magic?”

[P156]
“The booze is going in. Booze! Down it goes, down it goes!”

[P157]
“……”

[P158]
Team Leader Choi gazed at the two of them with regret before turning his eyes toward me. I had raised one arm conspicuously.

[P159]
“What does that mean?”

[P160]
“I have a question.”

[P161]
*At least this guy is a little better.*

[P162]
Team Leader Choi spoke with an expression that seemed to say as much.

[P163]
“Go ahead.”

[P164]
“Wasn’t Team Leader Choi the Guild Master?”

[P165]
“……”

[P166]
Looking as if he had been betrayed, Team Leader Choi pulled something from inside his coat and handed it to me. I took it and examined it.

[P167]
It was a business card.

[P168]
“I have this.”

[P169]
“What does it say?”

[P170]
“Choi Minwoo, Team Leader of Team 1, Peace Guild.”

[P171]
“Yes. I’m the Team Leader.”

[P172]
“Oh.”

[P173]
“Butler Kim is the Guild Master. I’m the Team Leader. The other three are team members. Do you understand now?”

[P174]
I didn’t know whether Butler Kim was a boss in name only or a public figurehead, but I nodded anyway.

[P175]
If I didn’t, Team Leader Choi looked like he might cry.

[P176]
“Did everyone else understand?”

[P177]
At Team Leader Choi’s question, Im Kkeokjeong and Miss Song answered.

[P178]
“Wow, even the liquor tastes amazing. Is it because we’ve got magically grilled meat to go with it?”

[P179]
“How long are you going to make me do the shoulder dance? It’s dislocated! Dislocated! Dislocated!”

[P180]
“……”

[P181]
*Hey, are you crying?*

[P182]
[^2]: School ties, regional ties, and blood ties are traditionally regarded in Korea as major sources of social connections and influence.
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
# Chapter 78

[P2]
Every Hunter is a heavy drinker.

[P3]
Even an F-rank Hunter, the lowest classification, possesses physical abilities and a metabolism far beyond those of an ordinary person.

[P4]
There is a reason people say that while some Hunters do not drink, there are none who cannot.

[P5]
“Hic. One more glass.”

[P6]
Well, there was one here.

[P7]
Miss Song’s eyes had already gone half-glazed as she furiously shook her empty glass.

[P8]
“One more glaaass!”

[P9]
*She’s pretty even when she’s drunk… No, that’s not the point. Isn’t this getting a little dangerous?*

[P10]
I looked at Miss Song with concern.

[P11]
*She must have drunk too quickly.*

[P12]
The moment the drinking party had begun in earnest, she had chugged an entire bottle of soju straight from the bottle and had been like this ever since. Every now and then, she slurred incomprehensible things about someone having no damn tact and rotten luck clinging like a curse.

[P13]
*Is something bad going on?*

[P14]
While Im Kkeokjeong was filling her glass, I leaned toward Team Leader Choi and whispered.

[P15]
“Team Leader. Did something happen to Miss Song?”

[P16]
Team Leader Choi answered with an awkward expression.

[P17]
“……Something did happen.”

[P18]
“I knew it.”

[P19]
“Something that happened very recently, too.”

[P20]
“Oh. Ah.”

[P21]
Miss Song’s misfortune was my misfortune. Just sitting there and watching her was breaking my heart.

[P22]
“Whew. I hope things work out for her.”

[P23]
“……”

[P24]
“……”

[P25]
Team Leader Choi, along with Butler Kim, who was sitting beside him, stared at me with strange expressions.

[P26]
This was starting to feel weird.

[P27]
“What?”

[P28]
“Nothing.”

[P29]
“People can be like that when they’re young.”

[P30]
It was a lukewarm answer, but that was not important right now.

[P31]
Crack.

[P32]
“Drink! Drink until you drop dead today!”

[P33]
Miss Song had opened her third bottle of soju and was going wild.

[P34]
“Ha-ha-ha! This is why I really like Miss Song!”

[P35]
Like a fish in water—no, like a bandit who’d found booze—Im Kkeokjeong egged her on from beside her.

[P36]
“Shouldn’t we stop her?”

[P37]
“Ah, Miss Song?”

[P38]
“Yes.”

[P39]
Team Leader Choi shrugged.

[P40]
“It’s fine. It’s not like I’ve only known her for a day or two. That’s just how Miss Song gets when she drinks.”

[P41]
“Even so… No, wait a second.”

[P42]
I stared intently at Team Leader Choi.

[P43]
I had thought he was suspicious for a while, but now I had finally caught him.

[P44]
“How do you know what Miss Song is like when she drinks?”

[P45]
“Because I’ve drunk with her.”

[P46]
“……”

[P47]
Was this bastard making fun of me? Did he think I was asking because I didn’t understand that?

[P48]
“That’s not what I mean.”

[P49]
“Then what do you mean?”

[P50]
“I mean…”

[P51]
Now that he had put it that way, I had nothing to say. When I thought about it, who was I to question the relationship between the two of them?

[P52]
Just as I was rendered speechless, Team Leader Choi suddenly opened his mouth.

[P53]
“You’ve heard of Ares, right?”

[P54]
“Of course.”

[P55]
Ares, the god of war.

[P56]
The name of a god who appeared in ancient Greek and Roman mythology. These days, though, it was famous for something else.

[P57]
“Who in Korea doesn’t know the Ares Guild?”

[P58]
The pride and joy of Korea’s Hunters.

[P59]
Hundreds of Guilds existed in Korea, but only one stood at the top: the Ares Guild. The achievements they had made from the early days of the Great Cataclysm to the present were too numerous to count.

[P60]
*They’re legends. Plain and simple.*

[P61]
They appeared in educational comics, educational animations, movies, novels, and all kinds of other media. They had even made it into textbooks.

[P62]
The Ares Guild held a position in Korea comparable to a living King Sejong or an active General Yi Sun-sin. No, perhaps even higher.

[P63]
*They’re famous all over the world, after all.*

[P64]
If you asked most foreigners, *Do you know King Sejong? King-God-General Yi Sun-sin?* they would probably respond, *What the hell is this Asian guy talking about?* But the Ares Guild was different.

[P65]
*Do you know Ares?*

[P66]
*Oh, yeah!*

[P67]
Even a tough-as-nails Texas grandpa would tap his twin pistols and understand. That was the accepted truth among scholars.

[P68]
“Why are you asking about the Ares Guild?”

[P69]
Team Leader Choi swallowed a mouthful of beer before answering.

[P70]
“Because I used to be there.”

[P71]
“Oh. I see… Huh?”

[P72]
What had I just heard?

[P73]
I blinked for a while before finally speaking.

[P74]
“You used to belong to the Ares Guild?”

[P75]
“I was a Team Leader. Though I was still pretty low-ranking.”

[P76]
The Ares Guild had high standards. They selected only the best and trained them to become even better. Team Leader Choi had called himself a low-ranking member, but the fact that he had become a Team Leader there was already incredible.

[P77]
Though at the moment, he just looked like a lunatic to me.

[P78]
“Then why did you leave?”

[P79]
Money, honor, and status.

[P80]
It was the best job any Hunter—or any man—could dream of. And he had kicked it all away and left!

[P81]
“Were you ostracized at work or something?”

[P82]
Team Leader Choi thought about it for a moment before answering.

[P83]
“That might have been the case. Miss Song was the only person who treated me normally.”

[P84]
“……Then was Miss Song in the Ares Guild too?”

[P85]
“She was on my team. I found out about her drinking habits during team dinners.”

[P86]
I swallowed hard.

[P87]
*These people are total elites.*

[P88]
My gaze moved back and forth between Team Leader Choi, who was sipping his beer, and Miss Song, who was drinking straight from the bottle, before stopping on one person.

[P89]
“Could it be that Butler Kim also…?”

[P90]
“Me?”

[P91]
Butler Kim smiled kindly and waved his hand.

[P92]
“I retired a long time ago. Ha-ha-ha.”

[P93]
“What?”

[P94]
So he was a former Hunter.

[P95]
Suddenly, I remembered the sense of incongruity I had always felt whenever I dealt with Butler Kim. I had also never once tried to assess him with my Qi Sense.

[P96]
*What is this man’s real identity?*

[P97]
Just as I was about to raise my Qi Sense, Im Kkeokjeong, who had been enthusiastically inhaling meat and liquor whether or not we were talking, spoke up.

[P98]
“Oh, the burner went out. Miss Song, do we have another gas canister?”

[P99]
“Hic. That was the last one.”

[P100]
“Aw, we can’t let the momentum die. Should we just eat it?”

[P101]
Im Kkeokjeong grumbled as he flipped a piece of meat that was still mostly raw. Butler Kim smiled gently at him.

[P102]
“That won’t do.”

[P103]
The next moment, two things happened at once.

[P104]
Snap!

[P105]
Butler Kim snapped his fingers.

[P106]
Fwoosh!

[P107]
A wave of scorching heat burst forth. Blue flames shot precisely up over the grill, heating the plate and cooking the meat in an instant before vanishing.

[P108]
“This is…”

[P109]
Im Kkeokjeong and I shouted at the same time.

[P110]
“A mage!”

[P111]
“It’s cooked incredibly well!”

[P112]
“……”

[P113]
“What? Taekyung, hurry up and eat.”

[P114]
*Forget it, old man.*

[P115]
I shook my head back and forth.

[P116]
More importantly, who would have thought Butler Kim was a mage? No wonder something about him had always felt strange.

[P117]
“You really fooled me.”

[P118]
Butler Kim picked up a well-cooked piece of meat.

[P119]
“I had no intention of fooling you. As I told you, I’m already a retired has-been.”

[P120]
*Has-been, my ass.*

[P121]
If Butler Kim was a has-been, half the mages still active today ought to bow their damn heads.

[P122]
*At least B-rank.*

[P123]
He could summon flames with a single snap of his fingers and control them precisely enough to cook the meat just right without burning or undercooking it. Judging from the circumstances, he had probably belonged to the Ares Guild as well before retiring.

[P124]
If he had been active during the Great Cataclysm, too…

[P125]
*……This guy’s a big shot.*

[P126]
And on top of that, he was an incredibly senior one.

[P127]
I asked cautiously.

[P128]
“Um, which Hunter training center did you graduate from?”

[P129]
“Nonsan.[^1] What about you, Mr. Taekyung?”

[P130]
“Gasp. Me too. The 28th Regiment, 1st Battalion.”

[P131]
“Really? What a coincidence. I was in the 28th Regiment, 1st Battalion too. Which company were you in?”

[P132]
“Second Company.”

[P133]
“Then it wasn’t a coincidence. I suppose it was fate. Ha-ha.”

[P134]
There was no need for further discussion. I stood up and bent deeply at the waist.

[P135]
“Nice to meet you, Senior.”

[P136]
[^1]: Nonsan is home to Korea’s main Army recruit training center.

[P137]
There is a saying in Korea about school ties, hometown ties, and blood ties.[^2] Hunters were no different.

[P138]
The probability of awakening was 0.1 percent—one in a thousand. Because the odds were so slim, it was rare for someone you knew from ordinary society to awaken. The Hunter training center, which might seem like nothing special, was where a Hunter’s network began.

[P139]
“You don’t have to go that far. Please, sit down.”

[P140]
“You can speak comfortably with me.”

[P141]
“I don’t really stand on ceremony…”

[P142]
Just as Butler Kim and I were creating a warm senior-junior atmosphere, Team Leader Choi suddenly cut in.

[P143]
“Butler Kim. Why don’t you do as Mr. Jin says?”

[P144]
*What an ill-mannered bastard. How dare he tell such a senior what to do…*

[P145]
*Hmm. He can do that.*

[P146]
Come to think of it, Team Leader Choi was the bigger shot. He employed a mage from the Ares Guild as his butler.

[P147]
*What kind of family does he come from?*

[P148]
Was his grandfather the president and his father the prime minister?

[P149]
As my curiosity continued to grow, Team Leader Choi went on.

[P150]
“I think it’s time we sorted out everyone’s forms of address. You’re the face of our Guild, after all. We can’t keep calling you Butler Kim or Uncle forever, can we?”

[P151]
Butler Kim considered it for a moment before answering.

[P152]
“I’ll follow the Young Master’s wishes.”

[P153]
Team Leader Choi nodded and swept his stern gaze over everyone present.

[P154]
“Then from now on, we’ll all address Butler Kim as Guild Master. No objections, correct?”

[P155]
Im Kkeokjeong and Miss Song answered.

[P156]
“Man, this meat is incredible. Is it because it was grilled with magic?”

[P157]
“The booze is going in. Booze! Down it goes, down it goes!”

[P158]
“……”

[P159]
Team Leader Choi gazed at the two of them with regret before turning his eyes toward me. I had raised one arm conspicuously.

[P160]
“What does that mean?”

[P161]
“I have a question.”

[P162]
*At least this guy is a little better.*

[P163]
Team Leader Choi spoke with an expression that seemed to say as much.

[P164]
“Go ahead.”

[P165]
“Wasn’t Team Leader Choi the Guild Master?”

[P166]
“……”

[P167]
Team Leader Choi wore an expression as if he had been betrayed, then pulled something from inside his coat and handed it to me. I took it and looked at it. It was a business card.

[P168]
“I have this.”

[P169]
“What does it say?”

[P170]
“Choi Minwoo, Team Leader of Team 1, Peace Guild.”

[P171]
“Yes. I’m the Team Leader.”

[P172]
“Oh.”

[P173]
“Butler Kim is the Guild Master. I’m the Team Leader. The other three are team members. Do you understand now?”

[P174]
I didn’t know whether Butler Kim was a boss in name only or merely a figurehead, but I nodded anyway. If I didn’t, Team Leader Choi looked like he might cry.

[P175]
“Did everyone else understand?”

[P176]
At Team Leader Choi’s question, Im Kkeokjeong and Miss Song answered.

[P177]
“Wow, even the liquor tastes amazing. Is it because we have magically grilled meat for an appetizer?”

[P178]
“How long are you going to make me do the shoulder dance? It’s dislocated! Dislocated! Dislocated!”

[P179]
“……”

[P180]
*Hey, are you crying?*

[P181]
[^2]: School ties, regional ties, and blood ties are traditionally regarded in Korea as major sources of social connections and influence.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 선배     | **Senior**                                   |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 대사      | **Master** for a senior Buddhist monk                           |
| 임꺽정 | **Im Kkeokjeong** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 대한민국 | **Korea** | Country reference. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 78,
  "passed": true,
  "metrics": {
    "source_characters": 4895,
    "translation_characters": 10896,
    "length_ratio": 2.226,
    "source_paragraphs": 176,
    "translation_paragraphs": 182
  },
  "errors": [],
  "warnings": [
    {
      "code": "numbers",
      "message": "Arabic numerals from the source are absent",
      "details": {
        "values": [
          "0"
        ]
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "대사",
        "preferred": "Master for a senior Buddhist monk"
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
        "korean": "세종",
        "romanization": "sejong"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "순신",
        "romanization": "sunsin"
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
