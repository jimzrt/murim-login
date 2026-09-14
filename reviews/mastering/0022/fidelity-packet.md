# Fidelity Gate — Chapter 22

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
  1|＃22화
  2|
  3|
  4|
  5|방에 들어서자 곰팡이 냄새가 코를 찔렀다. 과거 군대 내무반을 연상시키는 그곳에 정찰조원들이 대기 중이었다.
  6|
  7|‘열 명.’
  8|
  9|나는 기감을 일으킴과 동시에 그들의 면면을 훑었다.
 10|
 11|시선이 스쳐 갈 때마다 낯선 얼굴들 위로 레벨창이 불쑥불쑥 솟아오른다.
 12|
 13|‘14레벨. 15레벨. 14레벨…….’
 14|
 15|대부분이 비슷한 수준이었다. 그렇게 아홉 번째 인물로 넘어간 순간이었다.
 16|
 17|
 18|
 19|[Lv.22 혁무진]
 20|
 21|
 22|
 23|숫자가 훌쩍 뛰었다. 심지어 낯익은 얼굴이다.
 24|
 25|‘혁무진?’
 26|
 27|며칠 전 처음으로 태원진가에 도착했을 때 내게 시비를 걸었던 그 혁무진이 맞다. 시선이 마주치자 녀석이 입꼬리를 말아 올렸다.
 28|
 29|“이렇게 또 뵙는군요. 삼. 공. 자.”
 30|
 31|나는 적의가 드러나는 웃음을 빤히 쳐다보다 말했다.
 32|
 33|“앞으로 조장님, 이라고 불러라.”
 34|
 35|“……그리하지요.”
 36|
 37|혁무진의 따가운 시선을 흘리고 열 번째 정찰조원을 바라봤다. 내가 처음 등장했을 때부터 환한 웃음을 짓고 있던 청년이 벌떡 일어났다.
 38|
 39|“공자, 아니 조장님! 잘 부탁드립니다.”
 40|
 41|
 42|
 43|[Lv.13 한엽]
 44|
 45|
 46|
 47|전시 상황이다 보니 보직이 변경된 모양이다. 앞서 만난 백호당 서기는 정찰조 자체가 여러 곳에서 차출된 무사들로 구성되었다고 했다.
 48|
 49|‘혁무진도 원래는 수문각 소속이니까.’
 50|
 51|그래서인지 몰라도 방 안의 분위기는 어수선했다.
 52|
 53|조원들은 낯선 이들끼리의 어색함과 전쟁에 대한 불안, 기대가 뒤섞인 표정들로 나를 바라보는 중이었다.
 54|
 55|처음으로 입을 뗐다.
 56|
 57|“백호당 정찰조장으로 임명된 진태경이다. 잘 부탁한다.”
 58|
 59|짝짝짝. 누군가의 외로운 박수 소리는 불과 몇 초 만에 사그라지고 한엽이 무안한 얼굴로 손을 내렸다.
 60|
 61|생각 이상으로 딱딱한 분위기다.
 62|
 63|‘하지만 이것도 나쁘지 않지.’
 64|
 65|지금은 전시 상황이다. 서로 웃으며 친목을 도모하는 것보다는 지금처럼 긴장감을 유지하는 게 낫다.
 66|
 67|물론 그것도 과하면 독이 되고, 적당한 선에서 풀어 주는 게 조장인 내가 할 일 중 하나다.
 68|
 69|‘그거야 뭐, 익숙하니까.’
 70|
 71|처음 게이트에 입장한 초짜 헌터들은 말 그대로 얼어붙는다. 실전은 연습과 다르니까. 헌터 훈련소에서 배운 지식, 훈련은 우주 저 멀리 날아가고 원초적인 죽음의 냄새에 압도되는 것이다.
 72|
 73|그래서 길드 내 베테랑들이 초짜의 멘탈 케어를 도왔는데, 나도 그중 하나였다.
 74|
 75|‘그래 봤자 F급 전담이었지만.’
 76|
 77|수준도 엇비슷하다. 내가 느낀 바로는 무림의 이류는 E급과 F급을 오가는 수준이니까.
 78|
 79|그러니까 나는 열 명의 F급 파티를 이끄는 파티장이 된 셈이다. 내가 파티장이라, 해 본 적은 없었지만, 뭘 해야 하는지는 질리도록 봐 왔다.
 80|
 81|“본인이 전투 경험이 있다. 거수.”
 82|
 83|대뜸 던진 말에 정찰조 전원이 손을 들었다. 다들 어리둥절한 얼굴이다.
 84|
 85|“5회 이상 전투를 겪었다. 거수.”
 86|
 87|절반의 손이 내려갔다. 그중에는 한엽도 포함되어 있었다.
 88|
 89|5회 이상 전투 경험자가 다섯 명이라. 이 정도면 나쁘지 않다. 아니, 기대 이상이다.
 90|
 91|하지만 가장 중요한 마지막 질문이 남았다.
 92|
 93|“살인 경험이 있다. 거수.”
 94|
 95|힘없이 내려가는 네 개의 손. 나는 아직까지도 손을 들고 있는 유일한 정찰조원을 바라봤다.
 96|
 97|
 98|
 99|[Lv.22 혁무진]
100|
101|
102|
103|“얼마나 죽였지?”
104|
105|녀석이 코웃음 쳤다.
106|
107|“다섯. 작년 산적 토벌 때였소. 그중 하나는 부채주였고. 제법 강한 놈이었…….”
108|
109|더 들을 것도 없이 말했다.
110|
111|“좋아. 지금부터 네가 부조장이다.”
112|
113|주절거리려던 혁무진의 입이 딱 다물어졌다.
114|
115|“부조장?”
116|
117|“어. 싫으면 지금 말해.”
118|
119|초보들만 모인 지금, 무엇보다 중요한 건 경험자다.
120|
121|망설임 없이 적에게 무기를 휘두를 수 있는 놈은 혁무진이 유일하다.
122|
123|‘흑묘백묘.’
124|
125|흰 고양이든 검은 고양이든, 싸가지 없는 고양이든 쥐만 잘 잡으면 장땡이지.
126|
127|복잡한 얼굴로 생각에 잠겨 있던 혁무진이 대답했다.
128|
129|“……흥. 명령이니까 어쩔 수 없군.”
130|
131|부조장 하고 싶다는 말을 어렵게도 한다.
132|
133|“그럼 혁무진이 부조장. 앞으로 부를 때는 일 호다.”
134|
135|“일 호? 그건 또 뭐요?”
136|
137|“번호 순서. 앞으로 정찰조는 이름 대신 번호로 통칭한다. 혁무진이 일 호. 그 다음에 저기 앉아 있는 너. 그래. 네가 이 호.”
138|
139|일 호부터 십 호까지. 한 사람씩 가리키며 지명을 끝냈다.
140|
141|혁무진이 눈살을 찌푸렸다.
142|
143|“왜 그렇게 하는 거요?”
144|
145|“이게 편하니까. 오늘 당장 전투가 벌어질지도 모르는데 하루 종일 이름만 외울래?”
146|
147|“그건.”
148|
149|“그럼 시키는 대로 해. 명령이다.”
150|
151|굳은 얼굴로 나를 노려보는 혁무진을, 나는 피하지 않았다.
152|
153|오히려 그때처럼 건방지게 나와 주기를 기대하는 마음도 있었다. 당장 며칠 안에 전투가 벌어질 수도 있는데 지금 같은 식이라면 곤란하다.
154|
155|만약 덤빈다면 힘의 격차를 알려 줘야 한다. 확실하게.
156|
157|“……명령에 따르겠소.”
158|
159|“네가 뭐라고?”
160|
161|“일 호, 일 호요.”
162|
163|대답하는 혁무진의 목소리가 파르르 떨렸다. 생각보다 감이 좋은 놈이다. 산서잠룡에 관한 소문 때문인지도 모르고.
164|
165|중요한 사실은 혁무진이 나에게 순응했다는 사실이다.
166|
167|나는 내색하지 않고 말을 이었다.
168|
169|“지금부터 하는 말이 낯설고 이상하게 들릴 수 있다. 하지만 참아. 그게 칼 맞아 죽는 것보다 낫잖아. 안 그래?”
170|
171|혁무진만큼 대놓고 불만을 드러내진 않았지만, 다른 정찰조원들도 불안한 표정으로 나를 바라봤다.
172|
173|한 사람만 빼고.
174|
175|“저는 조장님 말씀을 따르겠습니다!”
176|
177|한엽이 소녀 팬처럼 외쳤다. 차이점이 있다면 손에 아이돌 응원봉 대신 창이 들려 있다는 건데…….
178|
179|‘아, 그렇지.’
180|
181|나는 정찰조원들을 향해 씩 웃어 보였다.
182|
183|“자, 본인이 검을 쓴다. 거수.”
184|
185|파티 사냥의 핵심. 포지션 나누기다.
186|
187|
188|
189|* * *
190|
191|
192|
193|현실의 레이드 방식은 이미 교범화된 지 오래다.
194|
195|탱커 셋. 딜러 넷. 마법사 둘과 힐러 하나. 10인 파티 기준으로 가장 이상적인 조합이다.
196|
197|‘마법사, 힐러는 당연히 없고.’
198|
199|탱커, 딜러만으로 최대한 균형을 맞춰야 하는데, 그런데…….
200|
201|“……방패 쓸 줄 아는 사람이 없다고?”
202|
203|충격적인 결과에 목소리가 떨렸다. 세상에, 딜러만 열 명이라니. 심지어 아홉이 검이고, 창은 한엽, 한 명밖에 없다.
204|
205|‘이 무슨 끔찍한 단일종인가.’
206|
207|차라리 혼종이 낫다. 그건 이것저것 섞여 있기라도 하니까.
208|
209|혁무진이 뭐 잘못됐냐는 표정으로 말했다.
210|
211|“사내라면 응당 검을 쥐어야지 않겠소.”
212|
213|그 말에 고개를 끄덕이는 다른 놈들을 보니 기도 안 찬다.
214|
215|‘아주 배가 불렀구먼. 배가 불렀어.’
216|
217|피 웅덩이에 머리 박아 봐라, 저런 말이 나오나.
218|
219|칼? 창? 그런 거 없다. 엉겁결에 잡은 돌멩이로 찍고, 흙 뿌리고 올라타서 이빨로 깨물고…….
220|
221|사선(死線)에서는 손에 잡히는 게 무기고 생명줄이다.
222|
223|기껏해야 산적들이나 상대해 왔던 이 녀석들은 아직 그걸 모른다.
224|
225|‘당장 내일부터라도 연습시켜야 하나?’
226|
227|저들을 위해서가 아니라, 내 생존을 위해서.
228|
229|요령만 가르쳐도 난전에서는 확실한 효과를 발휘할 것이다.
230|
231|‘7년 동안 개처럼 굴렀는데 초짜들 때문에 죽을 수는 없지.’
232|
233|그런 생각을 할 때였다. 댕. 댕. 댕. 커다란 종소리가 세 번 울렸다.
234|
235|개개인이 정확한 시간을 알 수 없는 이곳에서는 특정 시각마다 종을 치는데, 방금 울린 세 번의 종소리는 미시(未時:오후1~3시)가 되었다는 신호였다.
236|
237|그리고…….
238|
239|“준비해. 첫 출동이다.”
240|
241|정찰조의 첫 임무를 알리는 신호탄이기도 했다.
242|
243|
244|
245|* * *
246|
247|
248|
249|“잘하고 있을 겁니다.”
250|
251|위팽의 뜬금없는 말에 진위경이 고개를 들었다. 그는 방금까지 식어 가는 찻잔을 멍하니 바라보고 있던 중이었다.
252|
253|“무슨 소린가?”
254|
255|“삼공자 말입니다.”
256|
257|진태경이 속한 정찰조가 태원진가를 출발한 지 꼬박 하루가 흘렀다. 태원진가 인근 현읍을 정찰하는 것이 이번 임무였다.
258|
259|“어제 정오 무렵에 출발했으니 이틀 안에는 도착할 겁니다.”
260|
261|“아. 태경이.”
262|
263|진위경은 풀썩 웃었다. 어딘가 지쳐 보이는 웃음이었다.
264|
265|“난 또 뭐라고. 아닐세.”
266|
267|“아닙니까?”
268|
269|“언제까지 어린아이 취급 할 텐가? 이제 그 아이도 당당한 사내야. 알아서 잘하겠지.”
270|
271|“……제 귀가 의심되는군요.”
272|
273|“그동안 내가 많이 감싸기는 했지. 그때는 많이 어렸거든.”
274|
275|“저도 어느 정도는 동감입니다. 며칠 사이에 부쩍 달라졌어요.”
276|
277|“영웅은 역경을 딛고 성장하는 법이니까.”
278|
279|“…….”
280|
281|“아무튼 이제 막내에 대해서는 한시름 놨네. 이제 좀 더 본가에 집중할 수 있겠어.”
282|
283|“잠시 쉬시지요. 힘들어 보이십니다.”
284|
285|“위팽. 본가의 식솔들이 죽었네.”
286|
287|슬픔과 결의가 묻어 나오는 목소리에 위팽은 입을 다물었고, 진위경은 다시 업무를 보기 시작했다.
288|
289|하지만 침묵은 불과 한 시진 만에 깨졌다.
290|
291|“저건…….”
292|
293|점점 가까워지는 하늘 위의 검은 점. 거대한 날개를 펼치며 집무실 창가에 내려앉은 전서응은 하오문의 그것이었다.
294|
295|황급히 자리에서 일어난 진위경은 전서응의 발목에 고정된 통을 열었다. 서신을 펼친 순간 깨알처럼 적힌 글씨가 눈에 들어왔다.
296|
297|
298|
299|일문일살一問一殺 조필 외 별동대 이십 인. 정양定壤 출현.
300|
301|
302|
303|“정양……!”
304|
305|정양을 넘으면 혼주. 혼주를 넘으면 태원이다. 제아무리 별동대라고 하지만 며칠 만에 수백 리를 주파할 줄이야.
306|
307|그뿐만이 아니다.
308|
309|아직까지 본가로 복귀하지 않은 지부의 식솔들이 있다. 설마 놈들이 그들을 추적하고 있다면?
310|
311|‘한시가 급하다.’
312|
313|진위경이 결단을 내리기까지는 오래 걸리지 않았다.
314|
315|“지금 당장 무사 오십을 선별하여 정양으로 가게. 일문일살은 잔학무도한 절정 고수. 본가의 식솔들을…….”
316|
317|아이들이 생각났다. 작은 팔다리, 고통스럽게 일그러진 얼굴과 공허한 그 눈동자. 진위경은 이를 악물었다.
318|
319|“식솔들을 안전하게 데려와 주게.”
320|
321|“주군.”
322|
323|위팽의 표정이 딱딱하게 굳어 있었다. 진위경은 뭔가에 사로잡힌 듯, 멍하니 그의 얼굴을 바라보다가 입을 열었다.
324|
325|“태경이. 태경이가 어디로 갔다고 했지?”
326|
327|쥐어 짜낸 목소리가 흘러나왔다.
328|
329|“……정양입니다.”
```

## Assembled English

```markdown
[P1]
# Chapter 22

[P2]
The smell of mold stabbed at my nose as soon as I entered the room. The place reminded me of a military barracks, and the members of the reconnaissance squad were waiting inside.

[P3]
*Ten people.*

[P4]
I activated my qi sense and looked them over one by one.

[P5]
Every time my gaze passed over an unfamiliar face, a Level display popped up.

[P6]
*Level 14. Level 15. Level 14…*

[P7]
Most of them were around the same level. Then, as I moved on to the ninth person—

[P8]
> **Lv. 22 Hyuk Mujin**

[P9]
The number jumped sharply. The face was familiar, too.

[P10]
*Hyuk Mujin?*

[P11]
It was the same Hyuk Mujin who had picked a fight with me when I first arrived at the Jin Family of Taiyuan a few days ago. When our eyes met, he curled his lips into a smirk.

[P12]
“What a pleasure to see you again, Third. Young. Master.”

[P13]
I stared at his openly hostile smile.

[P14]
“From now on, call me Squad Leader.”

[P15]
“…As you wish.”

[P16]
Ignoring Hyuk Mujin’s piercing stare, I turned to the tenth member of the reconnaissance squad. The young man who had been beaming ever since I walked in shot to his feet.

[P17]
“Young Master—no, Squad Leader! I look forward to working with you.”

[P18]
> **Lv. 13 Han Yeop**

[P19]
It seemed some assignments had been changed because of the war. The White Tiger Hall clerk I had met earlier said that the reconnaissance squad itself was made up of martial artists drawn from several different places.

[P20]
*Hyuk Mujin originally belonged to the Gate Watch Office, too.*

[P21]
Maybe that was why the atmosphere in the room was so disorganized.

[P22]
The squad members watched me with expressions that mixed the awkwardness of strangers with anxiety and anticipation about the war.

[P23]
I spoke first.

[P24]
“I’m Jin Taekyung, appointed leader of White Tiger Hall’s reconnaissance squad. I look forward to working with you.”

[P25]
Clap, clap, clap.

[P26]
Someone’s lonely applause died out within a few seconds, and Han Yeop lowered his hand with an embarrassed expression.

[P27]
The atmosphere was stiffer than I had expected.

[P28]
*But that isn’t necessarily a bad thing.*

[P29]
We were at war. Better to keep them on edge than have everyone laughing and trying to make friends.

[P30]
Of course, too much tension could become poisonous. Easing it at the right moment was one of my duties as squad leader.

[P31]
*That much, I’m used to.*

[P32]
Newbie Hunters froze the moment they entered a Gate for the first time. Real combat was different from practice. Everything they had learned and trained for at the Hunter training center flew off into outer space, and they were overwhelmed by the primal scent of death.

[P33]
That was why Guild veterans helped the rookies keep their heads. I had been one of them.

[P34]
*Though I only handled F-ranks.*

[P35]
The levels were similar, too. From what I could tell, a Second Rate martial artist in Murim fell somewhere between an E-rank and an F-rank.

[P36]
In other words, I had become the leader of a ten-person F-rank party. I had never actually been a party leader before, but I had watched other people do the job until I was sick of it.

[P37]
“Raise your hand if you have combat experience.”

[P38]
At my abrupt question, every member of the reconnaissance squad raised a hand. They all looked bewildered.

[P39]
“Keep it raised if you’ve fought at least five times.”

[P40]
Half the hands went down. Han Yeop’s was among them.

[P41]
Five people with experience in at least five battles. That wasn’t bad. No, it was better than expected.

[P42]
But the most important question remained.

[P43]
“Keep it raised if you’ve killed someone.”

[P44]
Four hands dropped weakly. I looked at the only member of the reconnaissance squad who still had his hand raised.

[P45]
> **Lv. 22 Hyuk Mujin**

[P46]
“How many?”

[P47]
He snorted.

[P48]
“Five. During last year’s bandit suppression campaign. One of them was a deputy stronghold chief, and he was quite a strong bastard—”

[P49]
I cut him off.

[P50]
“Good. You’re the deputy squad leader from now on.”

[P51]
Hyuk Mujin’s mouth snapped shut just as he was about to ramble on.

[P52]
“Deputy squad leader?”

[P53]
“Yeah. Speak up now if you don’t like it.”

[P54]
With nothing but rookies gathered here, experience mattered more than anything.

[P55]
Hyuk Mujin was the only one who could swing a weapon at the enemy without hesitation.

[P56]
*Black cat, white cat.*

[P57]
White cat, black cat, or even a rude cat—it didn’t matter as long as it caught mice.

[P58]
Hyuk Mujin thought for a while with a complicated expression before answering.

[P59]
“…Hmph. Since it’s an order, I suppose it can’t be helped.”

[P60]
He sure had a difficult way of saying he wanted to be deputy squad leader.

[P61]
“Then Hyuk Mujin is the deputy squad leader. From now on, we’ll call you Number One.”

[P62]
“Number One? What’s that supposed to mean?”

[P63]
“Number order. From now on, everyone in the reconnaissance squad goes by a number instead of a name. Hyuk Mujin is Number One. Next, you sitting over there. Yes, you’re Number Two.”

[P64]
I pointed them out one by one until I had assigned Numbers One through Ten.

[P65]
Hyuk Mujin frowned.

[P66]
“Why are you doing this?”

[P67]
“It’s more convenient. We might be fighting today. Do you want to spend all day memorizing names?”

[P68]
“That’s—”

[P69]
“Then do as you’re told. It’s an order.”

[P70]
Hyuk Mujin glared at me, his face rigid, but I didn’t look away.

[P71]
Part of me even hoped he would get cocky like he had that day. A battle could break out within the next few days. If things continued as they were, that would be a problem.

[P72]
If he challenged me, I would have to show him the difference in our strength.

[P73]
Clearly.

[P74]
“…I will follow your orders.”

[P75]
“What did you say?”

[P76]
“Number One. Number One, sir.”

[P77]
Hyuk Mujin’s voice trembled. He was more perceptive than I had expected. Maybe it was because of the rumors about the Sleeping Dragon of Shanxi.

[P78]
The important thing was that Hyuk Mujin had submitted to me.

[P79]
Without letting anything show on my face, I continued.

[P80]
“What I’m about to say may sound strange and unfamiliar. But bear with it. It’s better than getting stabbed to death, isn’t it? Don’t you agree?”

[P81]
The other reconnaissance squad members didn’t show their displeasure as openly as Hyuk Mujin, but they also looked at me anxiously.

[P82]
Everyone except one.

[P83]
“I’ll follow whatever the Squad Leader says!”

[P84]
Han Yeop shouted like a fangirl. The only difference was that he was holding a spear instead of an idol light stick.

[P85]
*Oh, right.*

[P86]
I grinned at the reconnaissance squad.

[P87]
“Now, raise your hand if you use a sword.”

[P88]
The core of party hunting was dividing up positions.

[P89]
* * *

[P90]
Raid strategies in the real world had been standardized into manuals long ago.

[P91]
Three tanks. Four damage dealers. Two mages and one healer. For a ten-person party, that was the ideal combination.

[P92]
*Of course, there are no mages or healers.*

[P93]
I had to balance the party as best I could using only tanks and damage dealers, but—

[P94]
“…You’re telling me no one knows how to use a shield?”

[P95]
My voice trembled at the shocking result. Good lord, all ten of them were damage dealers. Nine used swords, and Han Yeop was the only one with a spear.

[P96]
*What kind of horrifying single-species party is this?*

[P97]
A hybrid would be better. At least that would mean something had been mixed in.

[P98]
Hyuk Mujin spoke with an expression that suggested he couldn’t understand what was wrong.

[P99]
“A man ought to wield a sword.”

[P100]
Seeing the others nod along left me speechless.

[P101]
*You’ve had it way too easy. Way too easy.*

[P102]
Try slamming your head into a pool of blood and see if you still talk like that.

[P103]
Sword? Spear? There was no such distinction. You bashed people with whatever rock you happened to grab, threw dirt, climbed on top of them, and bit them with your teeth.

[P104]
On the line between life and death, anything in your hand was a weapon and a lifeline.

[P105]
These people had only ever fought bandits at best. They still didn’t understand that.

[P106]
*Do I need to start training them tomorrow?*

[P107]
Not for their sake. For my survival.

[P108]
Even teaching them a few tricks would make a real difference in a melee.

[P109]
*I worked like a dog for seven years. I can’t die because of a bunch of rookies.*

[P110]
That was when it happened.

[P111]
Ding. Ding. Ding.

[P112]
A great bell tolled three times.

[P113]
Here, where no one could tell the exact time, bells were rung at set intervals. The three tolls that had just sounded marked Mi-si, roughly one to three in the afternoon.[^1]

[P114]
And—

[P115]
“Get ready. This is our first deployment.”

[P116]
They also signaled the reconnaissance squad’s first mission.

[P117]
* * *

[P118]
“He should be doing fine.”

[P119]
Jin Wikyung looked up at Wipeng’s abrupt comment. Until a moment ago, he had been staring blankly at a teacup as it slowly cooled.

[P120]
“What are you talking about?”

[P121]
“The Third Young Master.”

[P122]
A full day had passed since the reconnaissance squad led by Jin Taekyung departed from the Jin Family of Taiyuan. Their mission was to scout the county towns near the Jin Family.

[P123]
“They left around noon yesterday, so they should arrive within two days.”

[P124]
“Ah. Taekyung.”

[P125]
Jin Wikyung let out a weak laugh. He looked exhausted.

[P126]
“I thought you meant something else. That’s not it.”

[P127]
“It’s not?”

[P128]
“How long are you going to treat him like a child? He’s a grown man now. I’m sure he’ll manage on his own.”

[P129]
“…I’m beginning to doubt my ears.”

[P130]
“I did coddle him quite a bit. He was very young back then.”

[P131]
“I agree, to some extent. He’s changed considerably over the past few days.”

[P132]
“Heroes grow by overcoming adversity.”

[P133]
“…”

[P134]
“Anyway, I can stop worrying about the youngest now. I’ll be able to focus more on the main family.”

[P135]
“You should rest for a while. You look tired.”

[P136]
“Wipeng. Members of our family have died.”

[P137]
Wipeng fell silent at the sorrow and determination in his voice, and Jin Wikyung returned to his work.

[P138]
But the silence broke after a mere two hours.

[P139]
“What is that…?”

[P140]
A black dot in the sky was gradually drawing closer. The messenger hawk spread its enormous wings and landed by the office window.

[P141]
It belonged to the Lower District Sect.

[P142]
Jin Wikyung hurriedly stood and opened the tube fastened to the hawk’s leg. The moment he unfolded the letter, tiny writing caught his eye.

[P143]
> One Question, One Kill Jopil and twenty members of a special detachment have appeared in Jeongyang.

[P144]
“Jeongyang…!”

[P145]
Beyond Jeongyang lay Honju. Beyond Honju lay Taiyuan. Even for a special detachment, he had never expected them to cover hundreds of li in only a few days.

[P146]
That wasn’t all.

[P147]
There were still family members from the branches who had not returned to the main family. What if the enemy was tracking them?

[P148]
*Every moment counts.*

[P149]
It didn’t take Jin Wikyung long to decide.

[P150]
“Select fifty martial artists immediately and send them to Jeongyang. One Question, One Kill Jopil is a brutal Peak master. Bring our family members—”

[P151]
He thought of the children.

[P152]
Their small limbs. Their faces twisted in pain. Their vacant eyes.

[P153]
Jin Wikyung clenched his teeth.

[P154]
“Bring our family members home safely.”

[P155]
“My lord.”

[P156]
Wipeng’s expression had hardened. Jin Wikyung stared blankly at him as though something had taken hold of him, then opened his mouth.

[P157]
“Taekyung. Where did you say Taekyung went?”

[P158]
His voice came out strained.

[P159]
“…Jeongyang.”

[P160]
[^1]: Mi-si is one of the traditional two-hour divisions of the day, corresponding roughly to 1–3 p.m.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 22

[P2]
The smell of mold stabbed at my nose as soon as I entered the room. The place reminded me of a military barracks, and the members of the reconnaissance squad were waiting inside.

[P3]
*Ten people.*

[P4]
I sharpened my senses and looked over each of them.

[P5]
Every time my gaze passed over an unfamiliar face, a Level display popped up.

[P6]
*Level 14. Level 15. Level 14…*

[P7]
Most of them were around the same level. Then, as I moved on to the ninth person—

[P8]
> **Lv. 22 Hyuk Mujin**

[P9]
The number jumped sharply. The face was familiar, too.

[P10]
*Hyuk Mujin?*

[P11]
It was the same Hyuk Mujin who had picked a fight with me when I first arrived at the Jin Family of Taiyuan a few days ago. When our eyes met, he smirked.

[P12]
“What a pleasure to see you again, Third. Young. Master.”

[P13]
I stared at his openly hostile smile and said,

[P14]
“From now on, call me Squad Leader.”

[P15]
“……As you wish.”

[P16]
I ignored Hyuk Mujin’s piercing stare and looked at the tenth member of the reconnaissance squad. The young man who had been smiling brightly since I first appeared shot to his feet.

[P17]
“Young Master—no, Squad Leader! I look forward to working with you.”

[P18]
> **Lv. 13 Han Yeop**

[P19]
It seemed some assignments had been changed because of the war. The White Tiger Hall clerk I had met earlier said that the reconnaissance squad itself was made up of martial artists drawn from several different places.

[P20]
*Hyuk Mujin originally belonged to the Gate Watch Office, too.*

[P21]
Maybe that was why the atmosphere in the room was so disorganized.

[P22]
The squad members looked at me with expressions that mixed the awkwardness of strangers meeting for the first time with anxiety and anticipation about the war.

[P23]
I spoke first.

[P24]
“I’m Jin Taekyung, appointed leader of White Tiger Hall’s reconnaissance squad. I look forward to working with you.”

[P25]
Clap, clap, clap.

[P26]
Someone’s lonely applause died out within a few seconds, and Han Yeop lowered his hand with an embarrassed expression.

[P27]
The atmosphere was stiffer than I had expected.

[P28]
*But that isn’t necessarily a bad thing.*

[P29]
We were in wartime. Maintaining the current tension was better than laughing together and trying to socialize.

[P30]
Of course, too much tension could become poisonous. Easing it at the right moment was one of my duties as squad leader.

[P31]
*That much, I’m used to.*

[P32]
Newbie Hunters froze the moment they entered a Gate for the first time. Real combat was different from practice. Everything they had learned and trained for at the Hunter training center flew off into outer space, and they were overwhelmed by the primal scent of death.

[P33]
That was why veterans in the Guild handled mental care for the rookies. I had been one of them.

[P34]
*Though I was assigned exclusively to F-ranks.*

[P35]
The levels were similar, too. From what I could tell, a second-rate martial artist from Murim was somewhere between an E-rank and an F-rank.

[P36]
In other words, I had become the leader of a ten-person F-rank party. I had never actually been a party leader, but I had watched what they were supposed to do until I was sick of it.

[P37]
“Raise your hand if you have combat experience.”

[P38]
At my abrupt question, every member of the reconnaissance squad raised a hand. They all looked bewildered.

[P39]
“Raise your hand if you’ve been in combat at least five times.”

[P40]
Half the hands went down. Han Yeop was among them.

[P41]
Five people with experience in at least five battles. That wasn’t bad. No, it was better than expected.

[P42]
But the most important question remained.

[P43]
“Raise your hand if you’ve killed someone.”

[P44]
Four hands dropped weakly. I looked at the only member of the reconnaissance squad who still had his hand raised.

[P45]
> **Lv. 22 Hyuk Mujin**

[P46]
“How many?”

[P47]
He snorted.

[P48]
“Five. It was during last year’s bandit suppression campaign. One of them was a bandit chieftain. He was quite a strong bastard—”

[P49]
I cut him off before he could continue.

[P50]
“Good. You’re the deputy squad leader from now on.”

[P51]
Hyuk Mujin’s mouth, which had been preparing to ramble on, snapped shut.

[P52]
“Deputy squad leader?”

[P53]
“Yeah. Speak up now if you don’t like it.”

[P54]
With nothing but rookies gathered here, experience mattered more than anything.

[P55]
Hyuk Mujin was the only one who could swing a weapon at the enemy without hesitation.

[P56]
*Black cat, white cat.*

[P57]
White cat, black cat, or even a rude cat—it didn’t matter as long as it caught mice.

[P58]
Hyuk Mujin thought for a while with a complicated expression before answering.

[P59]
“……Hmph. Since it’s an order, I suppose it can’t be helped.”

[P60]
He sure had a difficult way of saying he wanted to be deputy squad leader.

[P61]
“Then Hyuk Mujin is deputy squad leader. From now on, we’ll call you Number One.”

[P62]
“Number One? What’s that supposed to mean?”

[P63]
“Number order. From now on, the reconnaissance squad will be referred to by number instead of name. Hyuk Mujin is Number One. Next, you sitting over there. Yes, you’re Number Two.”

[P64]
I finished assigning numbers one by one, from Number One to Number Ten.

[P65]
Hyuk Mujin frowned.

[P66]
“Why are you doing this?”

[P67]
“It’s more convenient. We might be fighting today. Do you want to spend all day memorizing names?”

[P68]
“That’s—”

[P69]
“Then do as you’re told. It’s an order.”

[P70]
I didn’t look away from Hyuk Mujin as he glared at me with a hard expression.

[P71]
Part of me even hoped he would act insolent like he had that day. A battle could break out within the next few days. If things continued as they were, that would be a problem.

[P72]
If he challenged me, I would have to show him the difference in our strength.

[P73]
Clearly.

[P74]
“……I will follow your orders.”

[P75]
“What did you say?”

[P76]
“Number One. I said Number One.”

[P77]
Hyuk Mujin’s voice trembled as he answered. He was more perceptive than I had expected. Maybe it was because of the rumors about the Sleeping Dragon of Shanxi.

[P78]
The important thing was that Hyuk Mujin had submitted to me.

[P79]
Without showing anything on my face, I continued.

[P80]
“What I’m about to say may sound strange and unfamiliar. But bear with it. It’s better than getting stabbed to death, isn’t it? Don’t you agree?”

[P81]
The other reconnaissance squad members didn’t show their displeasure as openly as Hyuk Mujin, but they also looked at me anxiously.

[P82]
Everyone except one.

[P83]
“I’ll follow whatever the Squad Leader says!”

[P84]
Han Yeop shouted like a teenage girl idol fan. The only difference was that he was holding a spear instead of an idol light stick.

[P85]
*Oh, right.*

[P86]
I grinned at the reconnaissance squad.

[P87]
“Now, raise your hand if you use a sword.”

[P88]
The core of party hunting was dividing up positions.

[P89]
* * *

[P90]
Raid strategies in the real world had been standardized into manuals long ago.

[P91]
Three tanks. Four damage dealers. Two mages and one healer. For a ten-person party, that was the ideal combination.

[P92]
*Of course, there are no mages or healers.*

[P93]
I had to balance things as much as possible with tanks and damage dealers alone, but—

[P94]
“……You’re telling me no one knows how to use a shield?”

[P95]
My voice trembled at the shocking result. Good lord, there were ten damage dealers. Nine used swords, and the only person with a spear was Han Yeop.

[P96]
*What kind of horrifying single-species party is this?*

[P97]
A hybrid would be better. At least that would mean something had been mixed in.

[P98]
Hyuk Mujin spoke with an expression that suggested he couldn’t understand what was wrong.

[P99]
“A man ought to wield a sword.”

[P100]
I was speechless when I saw the others nodding along with him.

[P101]
*You’re too well-fed. Way too well-fed.*

[P102]
Try slamming your head into a pool of blood and see if you still talk like that.

[P103]
Sword? Spear? There was no such distinction. You bashed people with whatever rock you happened to grab, threw dirt, climbed on top of them, and bit them with your teeth.

[P104]
On the line between life and death, anything in your hand was a weapon and a lifeline.

[P105]
These people, who had only ever fought bandits at best, still didn’t understand that.

[P106]
*Do I need to start training them tomorrow?*

[P107]
Not for their sake. For my survival.

[P108]
Even teaching them a few tricks would make a real difference in a melee.

[P109]
*I worked like a dog for seven years. I can’t die because of a bunch of rookies.*

[P110]
That was when it happened.

[P111]
Ding. Ding. Ding.

[P112]
A large bell rang three times.

[P113]
Since no one could tell the exact time, bells were rung at set intervals. The three tolls that had just sounded marked Mi-si, roughly one to three in the afternoon.[^1]

[P114]
And—

[P115]
“Get ready. This is our first deployment.”

[P116]
The bells also served as the signal announcing the reconnaissance squad’s first mission.

[P117]
* * *

[P118]
“He should be doing fine.”

[P119]
Jin Wikyung looked up at Wipeng’s abrupt comment. Until a moment ago, he had been staring blankly at a teacup as it slowly cooled.

[P120]
“What are you talking about?”

[P121]
“The Third Young Master.”

[P122]
A full day had passed since the reconnaissance squad led by Jin Taekyung departed from the Jin Family of Taiyuan. Their mission was to scout the county towns near the Jin Family.

[P123]
“They left around noon yesterday, so they should arrive within two days.”

[P124]
“Ah. Taekyung.”

[P125]
Jin Wikyung let out a weak laugh. He looked exhausted.

[P126]
“I thought you meant something else. That’s not it.”

[P127]
“It’s not?”

[P128]
“How long are you going to treat him like a child? He’s a grown man now. I’m sure he’ll manage on his own.”

[P129]
“……I’m beginning to doubt my ears.”

[P130]
“I did coddle him quite a bit. He was very young back then.”

[P131]
“I agree, to some extent. He’s changed considerably over the past few days.”

[P132]
“Heroes grow by overcoming adversity.”

[P133]
“……”

[P134]
“Anyway, I can stop worrying about the youngest now. I’ll be able to focus more on the main family.”

[P135]
“You should rest for a while. You look tired.”

[P136]
“Wipeng. Members of our family have died.”

[P137]
At the sorrow and determination in his voice, Wipeng fell silent, and Jin Wikyung returned to his work.

[P138]
But the silence broke after a mere two hours.

[P139]
“What is that…?”

[P140]
A black dot in the sky was gradually drawing closer. Spreading its enormous wings, the messenger hawk landed by the window of the office. It belonged to the Lower District Sect.

[P141]
Jin Wikyung hurriedly stood and opened the tube fastened to the hawk’s leg. The moment he unfolded the letter, tiny writing caught his eye.

[P142]
> Jopil, One Question, One Kill, and twenty members of a special detachment have appeared in Jeongyang.

[P143]
“Jeongyang…!”

[P144]
Beyond Jeongyang was Honju. Beyond Honju was Taiyuan. Even if they were a special detachment, he had never expected them to cover hundreds of li in only a few days.

[P145]
That wasn’t all.

[P146]
There were still family members from the branches who had not returned to the main family. What if the enemy was tracking them?

[P147]
*Every moment counts.*

[P148]
It didn’t take Jin Wikyung long to make a decision.

[P149]
“Select fifty martial artists immediately and send them to Jeongyang. One Question, One Kill Jopil is a brutal Peak master. Bring our family members—”

[P150]
He thought of the children.

[P151]
Their small limbs. Their faces twisted in pain. Their vacant eyes.

[P152]
Jin Wikyung clenched his teeth.

[P153]
“Bring our family members home safely.”

[P154]
“My lord.”

[P155]
Wipeng’s expression had hardened. Jin Wikyung stared blankly at him, as though a thought had seized him, before speaking.

[P156]
“Taekyung. Where did you say Taekyung went?”

[P157]
His voice came out strained.

[P158]
“……Jeongyang.”

[P159]
[^1]: Mi-si is one of the traditional two-hour divisions of the day, corresponding roughly to 1–3 p.m.
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 22,
  "passed": true,
  "metrics": {
    "source_characters": 4884,
    "translation_characters": 11045,
    "length_ratio": 2.261,
    "source_paragraphs": 152,
    "translation_paragraphs": 160
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "귀가",
        "preferred": "your family"
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
