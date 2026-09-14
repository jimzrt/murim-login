# Fidelity Gate — Chapter 41

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
  1|＃41화
  2|
  3|
  4|
  5|헌터 인력 사무소.
  6|
  7|말이 사무소지 빌딩이다. 역세권 노른자위 땅에 세운 이 6층 빌딩에는 하루에도 수백 명의 헌터들이 드나들었다.
  8|
  9|‘오랜만이네.’
 10|
 11|새벽인데도 불구하고 로비는 인산인해였다.
 12|
 13|긴 줄을 거쳐 창구에 도착하자 여직원이 사무적인 태도로 물었다.
 14|
 15|“인력 사무소는 처음이신가요?”
 16|
 17|“아뇨, 등록되어 있습니다.”
 18|
 19|“성함이?”
 20|
 21|“진태경입니다.”
 22|
 23|초짜 시절이었다. 헌터 훈련소를 우수한 성적으로 수료했지만 나 같은 F급 헌터를 필요로 하는 곳은 거의 없었고, 몇몇 중소 길드가 적선하듯 내민 계약서는 날강도 수준이었다.
 24|
 25|그래서 찾은 곳이 이곳이었다. 지역은 달랐지만.
 26|
 27|“일산 지점에 기록이 남아 있네요. 명단에 올렸으니 1층 강당에서 대기해 주세요.”
 28|
 29|“네.”
 30|
 31|이 6층 빌딩은 그 자체로 피라미드다. 1층은 E급과 F급을 수용하고, 2층은 최소 D급부터 발을 들일 수 있다.
 32|
 33|너무 대놓고 차별하는 것 아니냐며 분노하는 사람도 있지만, 차별하는 거 맞다.
 34|
 35|‘한두 번도 아니고.’
 36|
 37|이 바닥에서 7년을 버티면서 온갖 더러운 꼴을 다 겪었다. 찬밥 더운밥 가릴 시기는 오래전에 지났지.
 38|
 39|그런 생각과 함께 걸음을 뗀 순간이었다.
 40|
 41|“어, 이게 누구야!”
 42|
 43|걸걸한 목소리에 돌아보니 웬 털북숭이가 나를 보며 활짝 웃고 있었다.
 44|
 45|“태경이. 진태경 맞지?”
 46|
 47|“꺽정 아저씨?
 48|
 49|이 아저씨, 아직 살아 있었어?
 50|
 51|
 52|
 53|* * *
 54|
 55|
 56|
 57|성은 임. 이름은 까먹었다. 7년 전 딱 한 번, 자기소개할 때 들은 것 같은데 기억이 나지 않는다.
 58|
 59|다만 산적을 연상시키는 외모라 모두 그를 임꺽정이라고 불렀다.
 60|
 61|“그동안 어떻게 지냈냐?”
 62|
 63|“F급 헌터 사는 게 거기서 거기죠. 아저씨는요?”
 64|
 65|“아저씨는 무슨.”
 66|
 67|임꺽정이 넉넉한 웃음을 지어 보였다.
 68|
 69|“형님이라고 불러라. 나이 차이도 얼마나 안 나는데.”
 70|
 71|몇 살 차이였더라. 가물가물하다.
 72|
 73|“형님, 혹시 나이가?”
 74|
 75|“마흔다섯.”
 76|
 77|“…….”
 78|
 79|저 당당함 뭔데.
 80|
 81|하지만 그동안 갈고 닦은 처세술이 빛을 발했다. 나는 가까스로 억지 미소를 지을 수 있었다.
 82|
 83|“그러네요. 그냥 형님이라고 부를게요.”
 84|
 85|“그래, 동생. 으하하하!”
 86|
 87|강당 안에 호탕한 웃음이 울려 퍼졌다. 백 명에 가까운 사람들의 시선이 붙었다가 떨어진다.
 88|
 89|‘그냥 못 들은 척하고 갈걸.’
 90|
 91|어떻게 보면 얕은 인연이다. 반년 남짓 일산 사무소에서 매일같이 마주치고, 가끔 같이 일도 하고. 딱 그 정도 인연.
 92|
 93|‘사람은 좋은데…….’
 94|
 95|가끔 옆에 있으면 부끄러울 때가 있다. 지금처럼.
 96|
 97|“여기 율무차가 끝내줘. 강당 의자도 푹신하고.”
 98|
 99|율무차를 한입에 털어 넣은 임꺽정이 의자를 한껏 젖혔다.
100|
101|보아하니 한두 번 들락거린 솜씨가 아니다.
102|
103|“자주 오시나 봐요?”
104|
105|“매일은 아니고 가끔 들르는 정도지. 결혼하고 자식도 생기니까 몸을 사리게 되더라고. 흐흐.”
106|
107|못 본 사이에 가정을 꾸린 모양이다. 내가 축하 인사를 건네자 임꺽정이 머리를 긁적였다.
108|
109|“그게 뭐 대단한 일이라고.”
110|
111|겸양을 떨지만 대단한 건 대단한 거다. 헌터, 그것도 F급 헌터로 20년 넘게 활동하면서 가정까지 일구다니.
112|
113|어쩌면 눈앞의 임꺽정이 미래의 내 모습일지도 모른다는 생각이 들었다.
114|
115|‘물론 저 나이까지 살아 있어야 가능한 거지만.’
116|
117|헌터는 오래 할 직업이 못 된다. 그래서 연금 지급 대상인 10년을 채우자마자 은퇴하는 이들도 부지기수다.
118|
119|“그나저나 너도 이제 제법 티가 난다? 처음 봤을 때는 완전히 얼어서 말도 잘 못하더니.”
120|
121|“당연하죠. 나름 7년 찬데.”
122|
123|“그럼 그때 이후로 계속 사무소만 돈 거야? 그럭저럭 괜찮은 조건으로 중소 길드랑 계약하지 않았나? 소, 소…… 거기 이름이 뭐더라.”
124|
125|“소풍 길드요. 그저께 잘렸어요.”
126|
127|임꺽정이 애써 웃었다.
128|
129|“으하하! 잘했어. 길드 이름도 구리네. 소풍이 뭐냐 소풍이. 게이트에 소풍 가는 것도 아니고.”
130|
131|“아뇨, 그 소풍이 아니라 지역명인데요. 부천 소풍터미널 근처라 소풍 길드.”
132|
133|“아…….”
134|
135|그 후로 이어지는 임꺽정과의 대화는 제법 유익했다. 어쨌건 그는 인력 사무소의 단골이었고 괜찮은 정보와 자신만의 노하우를 가진 베테랑 헌터였으니까.
136|
137|“사무소 수수료 10%. 뭐 이거야 기본이고, 여기 꽤 타율이 좋아.”
138|
139|타율. 고용될 확률을 이르는 이 바닥 속어다. 당장 일당 치기가 목적인 나로서는 희소식이었다.
140|
141|“저희 같은 F급 헌터도요?”
142|
143|“어? 응. 그렇지.”
144|
145|뭐야, 저 어색한 표정은?
146|
147|하지만 뭔가를 더 물어보기도 전에 강당에 설치된 스피커에서 음성이 흘러나왔다.
148|
149|
150|
151|- E급 헌터 임혁준. 임혁준 님께서는 로비로 나와 주시기 바랍니다.
152|
153|
154|
155|오전 여섯 시 반.
156|
157|드디어 첫 타자가 나왔다. 그리고 E급 헌터들이 다 빠져나간 후에야 내 차례가 돌아올 것이다.
158|
159|“역시 E급 먼저 나가는…… 형님 어디 가세요?”
160|
161|“먼저 갈게.”
162|
163|방어구와 무기가 든 커다란 가방을 둘러맨 임꺽정, 아니 임혁준이 허허 웃었다.
164|
165|‘어쩐지 표정이 이상하더라니.’
166|
167|저 양반, 못 본 사이 정말 피나는 노력을 한 모양이다.
168|
169|고작 한 단계지만 F급의 잠재력으로 승급하는 건 정말 쉬운 일이 아니니까.
170|
171|“또 보자.”
172|
173|“네. 또 봬요.”
174|
175|그가 강당을 빠져나간 것이 시작이었다. 스피커는 작정한 듯 사람들의 이름을 쏟아 내기 시작했다.
176|
177|E급 누구누구, E급 누구, E급…… 염병, 여긴 나만 F급이냐?
178|
179|슬슬 초조해지려던 그 순간이었다.
180|
181|
182|
183|- F급 헌터 진태경. 진태경 님께서는 로비로 나와 주시기 바랍니다.
184|
185|
186|
187|떴다!
188|
189|
190|
191|* * *
192|
193|
194|
195|“진태경 씨?”
196|
197|로비에는 흰색 린넨 셔츠를 입은 남자가 기다리고 있었다. 그는 다짜고짜 덤덤한 얼굴로 계약서를 내밀었다.
198|
199|“평화 길드에서 나왔습니다. 읽고 사인하십시오.”
200|
201|이 자식 말투가 상당히 거슬리는데?
202|
203|나는 계약서와 남자의 얼굴을 번갈아 노려보았다.
204|
205|“정산 비율이 8:2로 되어 있는데요.”
206|
207|“레이드 후 기여도에 따라 공정한 금액 분배 후. 진태경 씨가 받게 될 금액의 2할을 저희가 가져갑니다.”
208|
209|“기본 수당은요?”
210|
211|“삼십.”
212|
213|“삼시입?”
214|
215|이 자식은 혀가 반 토막이 났나.
216|
217|“게이트 등급.”
218|
219|“E급.”
220|
221|“거절.”
222|
223|“포지션 다 찼습니다. 진태경 씨는 짐꾼 역할입니다.”
224|
225|나도 모르게 눈가가 파르르 떨렸다.
226|
227|이 자식이 방금 뭐라고 한 거야?
228|
229|“짐꾸운?”
230|
231|“문제가 있습니까?”
232|
233|“당연히.”
234|
235|셔츠남이 고압적인 시선으로 쏘아봤다.
236|
237|“뭡니까?”
238|
239|“펜이 없어요.”
240|
241|“…….”
242|
243|잠깐의 침묵이 흐른 후, 셔츠남이 건네주는 펜을 받아 사인을 휘갈겼다. 기본급 30만 원에 정산 비율도 후하다.
244|
245|E급 게이트라는 말에 흠칫했지만 짐꾼이니까 상관없지. 몬스터 가죽 좀 벗기고, 배낭 좀 메고 있다가 기분 좋게 헤어지는 거다.
246|
247|‘평화 길드. 이름부터 마음에 드네.’
248|
249|아까부터 사인하고 싶어서 손가락에 쥐 날 뻔했다.
250|
251|“잘 썼습니다.”
252|
253|“…….”
254|
255|“이제 어디로 가요? 봉고차 타고 가나?”
256|
257|“밖에 승합차 대 놨습니다.”
258|
259|“오, 저거죠? 좋아 보이네. 에어컨도 빵빵할 것 같고.”
260|
261|“…….”
262|
263|“제가 마지막이었나 봐요? 이미 몇 분 계시네…… 어? 꺽정 형님!”
264|
265|“어? 태경아!”
266|
267|버스 트렁크에 짐을 넣기 위해 대기 중이던 임꺽정이 활짝 웃었다.
268|
269|“너도 같이 가는구나. 잘됐다!”
270|
271|“그러게요. 제가 형님이랑 제법 인연이 있나 본데?”
272|
273|“으하하하!”
274|
275|“아하하하!”
276|
277|“……출발하시죠.”
278|
279|더위 때문인가, 셔츠남의 얼굴이 부쩍 늙어 보였다.
280|
281|
282|
283|* * *
284|
285|
286|
287|버스가 출발했다. 조수석에 앉은 셔츠남은 20분 안에 도착한다는 말을 남기고 눈을 감았다.
288|
289|임꺽정이 함께 고용된 이들에게 나를 소개했다.
290|
291|“자, 다들 인사해. 여긴 내 아는 동생.”
292|
293|이제 보니 다들 아는 사이였다. 나는 꾸벅 고개를 숙였다.
294|
295|“안녕하십니까. 진태경입니다.”
296|
297|“어어, 반가워요.”
298|
299|“젊은 친구가 훤칠하네. 잘 싸울 것 같어.”
300|
301|새로운 사람들은 총 세 명이었는데, 최소 30대 후반에서 40대 초반의 아저씨들이었다. 훈훈한 분위기 속에서 임꺽정이 설명했다.
302|
303|“이 친구들은 다 E급이야. 오래전부터 알았지. 10년도 넘었으니까.”
304|
305|“뭐, 그쯤 됐죠. 세월 참 빨라.”
306|
307|다들 최소 10년 차라는 말이다. 나도 어디 가서 풋내기 소리 들을 정도의 경력은 아닌데, 이 사람들은 완전히…….
308|
309|‘고인물 파티.’
310|
311|이런 사람들은 어딜 가든 제 몫은 한다. 급박한 상황에서는 오히려 어중간한 D급보다 훨씬 낫다.
312|
313|“그런데 젊은 친구는 등급이 어떻게 돼?”
314|
315|올 게 왔다. 등급 조사.
316|
317|나는 조심스럽게 대답했다.
318|
319|“F급입니다.”
320|
321|“아. 그래? 경력은?”
322|
323|“7년 찹니다.”
324|
325|“흠. 그래?”
326|
327|미적지근한 분위기. 첫 레이드부터 이런 식이면 곤란한데.
328|
329|나는 재빨리 입을 털었다.
330|
331|“전투 참여는 일절 안 하고 짐꾼으로 참여할 겁니다. 걱정 안 하셔도…….”
332|
333|세 사람이 멀뚱멀뚱 나를 바라본다.
334|
335|“뭘 부연 설명까지 해. 우리가 잡아먹나?”
336|
337|“됐어. 7년 굴렀으면 알 만큼 알겠지.”
338|
339|“꺽정 형님 추천이면 된 거지. 최 팀장도 괜찮다 싶으니까 오케이 했을 거고.”
340|
341|추천? 최 팀장?
342|
343|정확히는 몰라도 대충 돌아가는 그림은 알겠다.
344|
345|임꺽정이 나를 추천한 거다. 셔츠남, 최 팀장에게.
346|
347|“무, 무슨 소리를!”
348|
349|손사래 치는 임꺽정의 얼굴이 빨갛게 달아올라 있었다.
350|
351|그 모습에 아저씨 셋이 낄낄거렸다.
352|
353|“다 티 나, 아주. 저 형님 장가는 어떻게 갔대?”
354|
355|“원래 선행은 밝혀져야 좋은 거야. 뭘 그렇게 숨기고 살아.”
356|
357|“그럼. 그쪽도 그렇게 생각하지?”
358|
359|나는 냉큼 고개를 끄덕였다.
360|
361|“그럼요. 마음 써 주셔서 감사합니다.”
362|
363|“흠흠. 뭐 나야 그냥 한 번 찔러 본 거지. 결정은 최 팀장이 다 했어.”
364|
365|이거 참…….
366|
367|잠깐 들렀다 스쳐 지나간 수많은 인연 중 하나라고 생각했는데, 다시 만난 임꺽정은 생각보다 순박하고 정이 깊은 사람이었다.
368|
369|‘그래서 조건도 후했던 건가.’
370|
371|최 팀장, 최 팀장 하는 걸 보니 그들 사이의 친분도 내 계약조건에 한몫했을 거라는 생각이 든다.
372|
373|“열심히 하겠습니다.”
374|
375|“아니, 결정은 최 팀장이 했다니까!”
376|
377|임꺽정의 어색한 변명에 당사자가 대답했다.
378|
379|“그럼 제가 결정한 걸로 하죠.”
380|
381|어느새 눈을 뜬 셔츠남. 아니, 최 팀장이 우리에게 말했다.
382|
383|“이제 다 도착했으니까요.”
384|
385|고개를 돌리니 점점 가까워지는 4m 높이의 문(Gate)이 보였다. 그 중심에는 우리를 빨아들일 마력의 소용돌이가 휘몰아치고 있었다.
386|
387|‘E급 게이트.’
388|
389|복귀 후 첫 레이드다.
```

## Assembled English

```markdown
[P1]
# Chapter 41

[P2]
The Hunter Manpower Office.

[P3]
They called it an office, but it was a building. This six-story building sat on prime real estate right by the station, and hundreds of Hunters came through it every day.

[P4]
*It’s been a while.*

[P5]
Even at dawn, the lobby was packed.

[P6]
After making my way through the long line, I reached the counter. The woman there asked in a businesslike tone,

[P7]
“Is this your first time at the manpower office?”

[P8]
“No. I’m already registered.”

[P9]
“Your name?”

[P10]
“Jin Taekyung.”

[P11]
Back when I was a rookie, I’d graduated from the Hunter Training Center with excellent scores. But almost nowhere needed an F-rank Hunter like me, and the contracts a few small and midsize Guilds offered as if they were doing me a favor amounted to highway robbery.

[P12]
So I’d found this place. The region had been different, though.

[P13]
“There’s a record at the Ilsan branch. I’ve put you on the list, so please wait in the hall on the first floor.”

[P14]
“Yes.”

[P15]
This six-story building was a pyramid all by itself. The first floor took E- and F-ranks. You needed at least D-rank to set foot on the second.

[P16]
Some people got angry and asked if that wasn’t blatant discrimination.

[P17]
It was.

[P18]
*Not like this was the first or second time.*

[P19]
I’d lasted seven years in this business and endured every kind of shitty treatment there was. I’d long since passed the point of being picky.

[P20]
I had just started walking with that thought when—

[P21]
“Hey, look who it is!”

[P22]
I turned at the gravelly voice. Some hairy guy was grinning at me.

[P23]
“Taekyung. You’re Jin Taekyung, right?”

[P24]
“Uncle Kkeokjeong?”

[P25]
*This guy’s still alive?*

[P26]
* * *

[P27]
His surname was Im. I’d forgotten his given name. I was pretty sure I’d heard it once, when he introduced himself seven years ago, but I couldn’t remember it.

[P28]
He looked so much like a bandit that everyone called him Im Kkeokjeong.[^1]

[P29]
“How’ve you been all this time?”

[P30]
“Life as an F-rank Hunter is always the same. How about you?”

[P31]
“Don’t call me uncle.”

[P32]
Im Kkeokjeong gave me an easy smile.

[P33]
“Call me hyung. We’re not even that far apart in age.”

[P34]
How many years apart were we again? It was hazy.

[P35]
“Hyung, how old are you?”

[P36]
“Forty-five.”

[P37]
“…”

[P38]
*What’s with that confidence?*

[P39]
But the people skills I’d honed over the years paid off. I somehow managed to force a smile.

[P40]
“Right. I’ll just call you hyung.”

[P41]
“That’s it, little brother. Hahahaha!”

[P42]
His hearty laugh rang through the hall. Nearly a hundred people looked over, then looked away.

[P43]
*I should’ve just pretended I didn’t hear him and kept walking.*

[P44]
In a way, it was a shallow connection. We’d run into each other every day for about half a year at the Ilsan office, and sometimes worked together. That was about it.

[P45]
*He’s a good guy, but…*

[P46]
Sometimes having him next to me was embarrassing.

[P47]
Like now.

[P48]
“The yulmu tea here is incredible. And the chairs in the hall are nice and soft.”

[P49]
Im Kkeokjeong knocked back his yulmu tea[^2] in one gulp and tipped his chair as far as it would go.

[P50]
From the way he did it, this clearly wasn’t his first or second visit.

[P51]
“You come here often?”

[P52]
“Not every day. I drop by now and then. Once I got married and had kids, I started being more careful. Heh heh.”

[P53]
It seemed he’d started a family while we were out of touch. When I congratulated him, Im Kkeokjeong scratched his head.

[P54]
“What’s so great about that.”

[P55]
He was being modest, but a big deal was a big deal. He’d worked as a Hunter—an F-rank Hunter—for more than twenty years and still managed to build a family.

[P56]
I wondered if the Im Kkeokjeong in front of me might be my future self.

[P57]
*Assuming I lived to that age first.*

[P58]
Being a Hunter wasn’t a career you could keep up for long. Plenty of people retired the moment they completed the ten years needed to qualify for a pension.

[P59]
“Anyway, you’re starting to look the part. When I first saw you, you were completely frozen. You could barely even talk.”

[P60]
“Of course. I’ve got seven years in.”

[P61]
“So you’ve just been bouncing around manpower offices ever since? Didn’t you sign with a small or midsize Guild on fairly decent terms? So, So… what was the name again?”

[P62]
“Sopung Guild. They fired me the day before yesterday.”

[P63]
Im Kkeokjeong forced a laugh.

[P64]
“Hahaha! Good for you. The Guild’s name was lousy, too. What the hell is Sopung? It’s not like you’re going on a picnic to a Gate.”

[P65]
“No, not that sopung. It’s a place name. They’re near Bucheon Sopung Terminal, so Sopung Guild.”

[P66]
“Oh…”

[P67]
The conversation that followed was pretty useful. Im Kkeokjeong was a regular at the manpower office, after all, and a veteran Hunter with decent information and his own hard-earned know-how.

[P68]
“The office takes a ten percent commission. That’s standard. But the batting average here is pretty good.”

[P69]
*Batting average* was slang in this business for the odds of getting hired. For someone whose immediate goal was a day’s pay, that was good news.

[P70]
“Even for F-rank Hunters like us?”

[P71]
“Huh? Yeah. That’s right.”

[P72]
*What’s with that awkward look?*

[P73]
Before I could ask anything else, a voice came through the speakers in the hall.

[P74]
—E-rank Hunter Im Hyeokjun. Im Hyeokjun, please come to the lobby.

[P75]
Six thirty in the morning.

[P76]
At last, the first batter was up. And my turn would only come after all the E-rank Hunters had left.

[P77]
“E-ranks first, as expected… Hyung, where are you going?”

[P78]
“I’ll go on ahead.”

[P79]
Im Kkeokjeong—or rather, Im Hyeokjun—slung a large bag of armor and weapons over his shoulder and gave a sheepish laugh.

[P80]
*No wonder his expression looked off.*

[P81]
The man had clearly worked himself to the bone while we were out of touch.

[P82]
It was only one step up, but rising even that far with an F-rank’s potential was no easy feat.

[P83]
“See you around.”

[P84]
“Yes. See you.”

[P85]
Him walking out of the hall was the start. The speakers began pouring out names like they meant it.

[P86]
E-rank this person, E-rank that person, E-rank…

[P87]
*Goddamn it, am I the only F-rank here?*

[P88]
Just as I was starting to get anxious—

[P89]
—F-rank Hunter Jin Taekyung. Jin Taekyung, please come to the lobby.

[P90]
*There it is!*

[P91]
* * *

[P92]
“Mr. Jin Taekyung?”

[P93]
A man in a white linen shirt was waiting in the lobby. Without preamble, he held out a contract with a blank face.

[P94]
“I’m from the Peace Guild. Read it and sign.”

[P95]
*This guy’s way of talking is seriously irritating.*

[P96]
I glared from the contract to the man’s face and back.

[P97]
“The settlement split is eight to two.”

[P98]
“After the raid, the proceeds are distributed fairly according to contribution. We take twenty percent of the amount you receive.”

[P99]
“And the base pay?”

[P100]
“Thirty.”

[P101]
“Thir…ty?”

[P102]
*Did this guy’s tongue get cut in half?*

[P103]
“Gate rank.”

[P104]
“E-rank.”

[P105]
“Rejected.”

[P106]
“The positions are full. You’ll be a porter.”

[P107]
The corner of my eye twitched.

[P108]
*What the hell did this guy just say?*

[P109]
“Por-ter?”

[P110]
“Is there a problem?”

[P111]
“Obviously.”

[P112]
The shirt guy glared down his nose at me.

[P113]
“What is it?”

[P114]
“I don’t have a pen.”

[P115]
“…”

[P116]
After a brief silence, I took the pen he handed me and scrawled my signature. The base pay was 300,000 won, and the settlement split was generous too.

[P117]
I’d flinched at the mention of an E-rank Gate, but I was only going as a porter, so it didn’t matter. I’d skin a few monsters, carry a pack for a while, and then we’d part ways in a good mood.

[P118]
*Peace Guild. I like the name already.*

[P119]
I’d been itching to sign so badly my fingers had almost cramped.

[P120]
“All signed.”

[P121]
“…”

[P122]
“So where are we going now? We taking a van?”

[P123]
“There’s a van waiting outside.”

[P124]
“Oh, that one? Looks nice. Bet the AC’s blasting too.”

[P125]
“…”

[P126]
“Guess I was last? There are already a few people here… Huh? Kkeokjeong hyung!”

[P127]
“Huh? Taekyung!”

[P128]
Im Kkeokjeong was waiting to load his bags into the bus’s trunk. He grinned wide.

[P129]
“You’re coming too. Great!”

[P130]
“Right? I guess I really do have a connection with you, hyung.”

[P131]
“Hahahaha!”

[P132]
“Ahahaha!”

[P133]
“…Let’s get going.”

[P134]
Maybe it was the heat, but the shirt guy’s face looked years older.

[P135]
* * *

[P136]
The bus pulled out. From the passenger seat, the shirt guy said we’d arrive within twenty minutes, then closed his eyes.

[P137]
Im Kkeokjeong introduced me to the others who’d been hired with us.

[P138]
“All right, everyone, say hello. This is a younger brother I know.”

[P139]
Now that I looked, they all knew each other. I dipped my head.

[P140]
“Hello. I’m Jin Taekyung.”

[P141]
“Oh, nice to meet you.”

[P142]
“Tall young fellow. Looks like he can fight.”

[P143]
There were three new people in all, men in their late thirties or early forties. In that warm atmosphere, Im Kkeokjeong explained.

[P144]
“These guys are all E-rank. I’ve known them a long time. Over ten years now.”

[P145]
“Yeah, about that long. Time sure flies.”

[P146]
Meaning they all had at least ten years in. I had enough experience that nobody was going to call me a rookie wherever I went, but these guys were on another level entirely.

[P147]
*Old-timer party.*

[P148]
People like them pulled their weight wherever they went. In a pinch, they were much better than a middling D-rank.

[P149]
“So what’s the young guy’s rank?”

[P150]
Here it came. The rank check.

[P151]
I answered carefully.

[P152]
“F-rank.”

[P153]
“Ah. That so? How many years?”

[P154]
“Seven.”

[P155]
“Hmm. That so?”

[P156]
The mood went lukewarm. If my first raid started like this, that would be a problem.

[P157]
I ran my mouth before it could settle.

[P158]
“I won’t be taking part in combat at all. I’m joining as a porter, so you don’t have to worry…”

[P159]
The three men stared at me blankly.

[P160]
“Why the extra explanation? We gonna eat you?”

[P161]
“Drop it. If he’s been knocking around for seven years, he knows enough.”

[P162]
“If Kkeokjeong hyung recommended him, that’s enough. Team Leader Choi must’ve thought he was all right too, or he wouldn’t have said yes.”

[P163]
*Recommended? Team Leader Choi?*

[P164]
I didn’t know the exact details, but I could more or less see how this had gone.

[P165]
Im Kkeokjeong had recommended me. To the shirt guy—Team Leader Choi.

[P166]
“W-what are you talking about?”

[P167]
Im Kkeokjeong waved his hands, his face bright red.

[P168]
The three men snickered.

[P169]
“It’s written all over him. How did that hyung ever get married?”

[P170]
“Good deeds are supposed to come to light. Why go through life hiding them?”

[P171]
“Right. You think so too, don’t you?”

[P172]
I nodded at once.

[P173]
“Of course. Thank you for looking out for me.”

[P174]
“Ahem. I just put in a word. Team Leader Choi made the decision.”

[P175]
Well, then…

[P176]
I’d thought of Im Kkeokjeong as one of the many people I’d crossed paths with for a moment and moved on from. Meeting him again, he was more guileless and warmhearted than I’d expected.

[P177]
*So that’s why the terms were so generous.*

[P178]
The way they kept saying Team Leader Choi, Team Leader Choi, I figured their friendship had played a part in my contract too.

[P179]
“I’ll work hard.”

[P180]
“I told you, Team Leader Choi made the decision!”

[P181]
The man in question answered Im Kkeokjeong’s awkward excuse.

[P182]
“Then let’s say I made the decision.”

[P183]
The shirt guy had opened his eyes at some point. No—Team Leader Choi. He spoke to us.

[P184]
“We’re almost there.”

[P185]
I turned my head. A four-meter-high Gate was drawing closer. At its center, a vortex of mana churned, ready to suck us in.

[P186]
*An E-rank Gate.*

[P187]
My first raid since coming back.

[P188]
[^1]: A famous Joseon-era bandit and folk hero; the nickname comes from his looks.
[^2]: Yulmu tea is a sweet Korean grain drink, commonly served hot or cold.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 41

[P2]
The Hunter Manpower Office.

[P3]
They called it an office, but it was a building. This six-story building sat on prime real estate right by the station, and hundreds of Hunters came through it every day.

[P4]
*It’s been a while.*

[P5]
Even at dawn, the lobby was packed.

[P6]
After working through the long line, I reached the counter. The woman there asked in a businesslike tone,

[P7]
“Is this your first time at the manpower office?”

[P8]
“No. I’m already registered.”

[P9]
“Your name?”

[P10]
“Jin Taekyung.”

[P11]
Back when I was a rookie, I’d graduated from the Hunter Training Center with excellent scores. But almost nowhere needed an F-rank Hunter like me, and the contracts a few small and midsize Guilds offered like they were doing me a favor were highway robbery.

[P12]
So I’d found this place. The region had been different, though.

[P13]
“There’s a record at the Ilsan branch. I’ve put you on the list, so please wait in the hall on the first floor.”

[P14]
“Yes.”

[P15]
This six-story building was a pyramid all by itself. The first floor took E- and F-ranks. You needed at least D-rank to set foot on the second.

[P16]
Some people got angry, asking if this wasn’t just open discrimination.

[P17]
It was.

[P18]
*Not like this was the first or second time.*

[P19]
I’d lasted seven years in this business and taken every kind of dirty treatment there was. I’d long since passed the point of being picky.

[P20]
I started walking with that thought when—

[P21]
“Hey, look who it is!”

[P22]
I turned at the gravelly voice. Some hairy guy was grinning at me.

[P23]
“Taekyung. You’re Jin Taekyung, right?”

[P24]
“Uncle Kkeokjeong?”

[P25]
*This guy’s still alive?*

[P26]
* * *

[P27]
His surname was Im. I’d forgotten his given name. I was pretty sure I’d heard it once, when he introduced himself seven years ago, but I couldn’t remember it.

[P28]
He just looked so much like a bandit that everyone called him Im Kkeokjeong[^1].

[P29]
“How’ve you been all this time?”

[P30]
“Life as an F-rank Hunter is always the same. How about you?”

[P31]
“Don’t call me uncle.”

[P32]
Im Kkeokjeong gave me an easy smile.

[P33]
“Call me hyung. We’re not even that far apart in age.”

[P34]
How many years apart were we again? It was hazy.

[P35]
“Hyung, how old are you?”

[P36]
“Forty-five.”

[P37]
“…”

[P38]
*What’s with that confidence?*

[P39]
But the people skills I’d honed over the years paid off. I somehow managed to force a smile.

[P40]
“Right. I’ll just call you hyung.”

[P41]
“That’s it, little brother. Hahahaha!”

[P42]
His hearty laugh rolled through the hall. Nearly a hundred people looked over, then looked away.

[P43]
*I should’ve just pretended I didn’t hear him and kept walking.*

[P44]
In a way, it was a shallow connection. We’d run into each other every day for about half a year at the Ilsan office, and sometimes worked together. That was about it.

[P45]
*He’s a good guy, but…*

[P46]
Sometimes having him next to me was embarrassing.

[P47]
Like now.

[P48]
“The yulmu tea here is incredible. And the chairs in the hall are nice and soft.”

[P49]
Im Kkeokjeong knocked back a mouthful of yulmu tea[^2] and tipped his chair as far as it would go.

[P50]
From the way he did it, this clearly wasn’t his first or second visit.

[P51]
“You come here often?”

[P52]
“Not every day. I drop by now and then. Once I got married and had kids, I started watching myself. Heh heh.”

[P53]
It seemed he’d started a family while we were out of touch. When I congratulated him, Im Kkeokjeong scratched his head.

[P54]
“What’s so great about that.”

[P55]
He was being modest, but a big deal was a big deal. He’d worked as a Hunter—an F-rank Hunter—for more than twenty years and still managed to build a family.

[P56]
I wondered if the Im Kkeokjeong in front of me might be my future self.

[P57]
*Assuming I lived to that age first.*

[P58]
Being a Hunter wasn’t a career you could keep up for long. Plenty of people retired the moment they finished the ten years that qualified them for a pension.

[P59]
“Anyway, you’re starting to look the part. When I first saw you, you were completely frozen. Could barely even talk.”

[P60]
“Of course. I’ve got seven years in.”

[P61]
“So you’ve just been bouncing around offices ever since? Didn’t you sign with a small or midsize Guild on fairly decent terms? So, So… what was the name again?”

[P62]
“Sopung Guild. They fired me the day before yesterday.”

[P63]
Im Kkeokjeong forced a laugh.

[P64]
“Hahaha! Good for you. The Guild’s name was lousy, too. What the hell is Sopung? It’s not like you’re going on a picnic to a Gate.”

[P65]
“No, not that sopung. It’s a place name. They’re near Bucheon Sopung Terminal, so Sopung Guild.”

[P66]
“Oh…”

[P67]
The conversation that followed was pretty useful. Im Kkeokjeong was a regular at the manpower office, after all, and a veteran Hunter with decent information and his own hard-earned know-how.

[P68]
“The office takes a ten percent commission. That’s standard. But the batting average here is pretty good.”

[P69]
*Batting average* was slang in this business for the odds of getting hired. For someone whose immediate goal was a day’s pay, that was good news.

[P70]
“Even for F-rank Hunters like us?”

[P71]
“Huh? Yeah. That’s right.”

[P72]
*What’s with that awkward look?*

[P73]
Before I could ask anything else, a voice came through the speakers in the hall.

[P74]
—E-rank Hunter Im Hyeokjun. Im Hyeokjun, please come to the lobby.

[P75]
Six thirty in the morning.

[P76]
At last, the first batter was up. And it would only be my turn after all the E-rank Hunters had left.

[P77]
“E-ranks first, as expected… Hyung, where are you going?”

[P78]
“I’ll go ahead.”

[P79]
Im Kkeokjeong—or rather, Im Hyeokjun—slung a large bag of armor and weapons over his shoulder and gave a sheepish laugh.

[P80]
*No wonder his expression looked off.*

[P81]
The man had clearly worked himself to the bone while I wasn’t looking.

[P82]
It was only one step, but ranking up on an F-rank’s potential was no easy feat.

[P83]
“See you again.”

[P84]
“Yes. See you.”

[P85]
Him walking out of the hall was the start. The speakers began pouring out names like they meant it.

[P86]
E-rank this person, E-rank that person, E-rank…

[P87]
*Goddamn it, am I the only F-rank here?*

[P88]
Just as I was starting to get anxious—

[P89]
—F-rank Hunter Jin Taekyung. Jin Taekyung, please come to the lobby.

[P90]
*There it is!*

[P91]
* * *

[P92]
“Mr. Jin Taekyung?”

[P93]
A man in a white linen shirt was waiting in the lobby. Without preamble, he held out a contract with a blank face.

[P94]
“I’m from the Peace Guild. Read it and sign.”

[P95]
*This guy’s way of talking is seriously irritating.*

[P96]
I glared from the contract to the man’s face and back.

[P97]
“The settlement split is eight to two.”

[P98]
“After the raid, we divide the proceeds fairly by contribution. Then we take twenty percent of the amount you receive.”

[P99]
“And the base pay?”

[P100]
“Thirty.”

[P101]
“Thir…ty?”

[P102]
*Did this guy’s tongue get cut in half?*

[P103]
“Gate rank.”

[P104]
“E-rank.”

[P105]
“Rejected.”

[P106]
“The positions are full. You’ll be a porter.”

[P107]
The corner of my eye twitched.

[P108]
*What the hell did this guy just say?*

[P109]
“Por-ter?”

[P110]
“Is there a problem?”

[P111]
“Obviously.”

[P112]
The shirt guy glared at me, looking down his nose.

[P113]
“What is it?”

[P114]
“I don’t have a pen.”

[P115]
“…”

[P116]
After a brief silence, I took the pen he handed me and scrawled my signature. The base pay was 300,000 won, and the settlement split was generous too.

[P117]
I’d flinched at E-rank Gate, but I was only going as a porter, so it didn’t matter. Skin a few monsters, haul a pack for a while, and part ways in a good mood.

[P118]
*Peace Guild. I like the name already.*

[P119]
I’d been itching to sign so badly my fingers had almost cramped.

[P120]
“All signed.”

[P121]
“…”

[P122]
“So where are we going now? We taking a van?”

[P123]
“There’s a van waiting outside.”

[P124]
“Oh, that one? Looks nice. Bet the AC’s blasting too.”

[P125]
“…”

[P126]
“Guess I was last? There are already a few people here… Huh? Kkeokjeong hyung!”

[P127]
“Huh? Taekyung!”

[P128]
Im Kkeokjeong was waiting to load his bags into the bus’s trunk. He grinned wide.

[P129]
“You’re coming too. Great!”

[P130]
“Right? I must really have a connection with you, hyung.”

[P131]
“Hahahaha!”

[P132]
“Ahahaha!”

[P133]
“…Let’s get going.”

[P134]
Maybe it was the heat, but the shirt guy’s face looked years older.

[P135]
* * *

[P136]
The bus pulled out. From the passenger seat, the shirt guy said we’d arrive within twenty minutes, then closed his eyes.

[P137]
Im Kkeokjeong introduced me to the others who’d been hired with us.

[P138]
“All right, everyone, say hello. This is a younger brother I know.”

[P139]
Now that I looked, they all knew each other. I dipped my head.

[P140]
“Hello. I’m Jin Taekyung.”

[P141]
“Oh, nice to meet you.”

[P142]
“Tall young fellow. Looks like he can fight.”

[P143]
There were three new people in all, men in their late thirties or early forties. In that warm atmosphere, Im Kkeokjeong explained.

[P144]
“These guys are all E-rank. I’ve known them a long time. Over ten years now.”

[P145]
“Yeah, about that long. Time sure flies.”

[P146]
Meaning they all had at least ten years in. I had enough experience that nobody was going to call me a rookie wherever I went, but these guys were on another level entirely.

[P147]
*Old-timer party.*

[P148]
People like them pulled their weight wherever they went. In a pinch, they were much better than a middling D-rank.

[P149]
“So what’s the young guy’s rank?”

[P150]
Here it came. The rank check.

[P151]
I answered carefully.

[P152]
“F-rank.”

[P153]
“Ah. That so? How many years?”

[P154]
“Seven.”

[P155]
“Hmm. That so?”

[P156]
The mood went lukewarm. If my first raid started like this, that would be a problem.

[P157]
I ran my mouth before it could settle.

[P158]
“I won’t be in combat at all. I’m joining as a porter, so you don’t have to worry…”

[P159]
The three men stared at me blankly.

[P160]
“Why the extra explanation? We gonna eat you?”

[P161]
“Drop it. If he’s been knocking around for seven years, he knows enough.”

[P162]
“If Kkeokjeong hyung recommended him, that’s enough. Team Leader Choi must’ve thought he was all right too, or he wouldn’t have said yes.”

[P163]
*Recommended? Team Leader Choi?*

[P164]
I didn’t know the exact details, but I could more or less see how this had gone.

[P165]
Im Kkeokjeong had recommended me. To the shirt guy—Team Leader Choi.

[P166]
“W-what are you talking about?”

[P167]
Im Kkeokjeong waved his hands, his face bright red.

[P168]
The three men snickered.

[P169]
“It’s written all over him. How did that hyung ever get married?”

[P170]
“Good deeds are supposed to come to light. Why live hiding them?”

[P171]
“Right. You think so too, don’t you?”

[P172]
I nodded at once.

[P173]
“Of course. Thank you for looking out for me.”

[P174]
“Ahem. I just put in a word. Team Leader Choi made the decision.”

[P175]
Well, then…

[P176]
I’d thought of Im Kkeokjeong as one of the many people I’d crossed paths with for a moment and moved on from. Meeting him again, he was more simple and warmhearted than I’d expected.

[P177]
*So that’s why the terms were so generous.*

[P178]
The way they kept saying Team Leader Choi, Team Leader Choi, I figured their friendship had played a part in my contract too.

[P179]
“I’ll work hard.”

[P180]
“I told you, Team Leader Choi made the decision!”

[P181]
The man in question answered Im Kkeokjeong’s awkward excuse.

[P182]
“Then let’s say I made the decision.”

[P183]
The shirt guy had opened his eyes at some point. No—Team Leader Choi. He spoke to us.

[P184]
“We’ve arrived.”

[P185]
I looked over. A four-meter-high Gate was drawing closer. At its center, a vortex of mana churned, ready to suck us in.

[P186]
*An E-rank Gate.*

[P187]
My first raid since coming back.

[P188]
[^1]: Famous Joseon-era folk-hero bandit; the nickname comes from his looks.
[^2]: Yulmu tea is a sweet Korean grain drink, commonly served hot or cold.
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 41,
  "passed": true,
  "metrics": {
    "source_characters": 5143,
    "translation_characters": 11147,
    "length_ratio": 2.167,
    "source_paragraphs": 184,
    "translation_paragraphs": 188
  },
  "errors": [],
  "warnings": [
    {
      "code": "numbers",
      "message": "Arabic numerals from the source are absent",
      "details": {
        "values": [
          "10",
          "8"
        ]
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
        "korean": "꺽정",
        "romanization": "kkeokjeong"
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
        "korean": "부천",
        "romanization": "bucheon"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "아하하하",
        "romanization": "ahahaha"
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
