# Fidelity Gate — Chapter 96

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
  1|＃96화
  2|
  3|
  4|
  5|김준수는 상동 길드 보안팀 소속의 C급 헌터다.
  6|
  7|원소 마법에는 재능이 쥐뿔도 없었지만 다행히 희귀하다는 정신계 마법사로 각성한 덕에 나름 잘나가는 인생을 살고 있었다.
  8|
  9|‘집에 못 들어가는 것만 빼면.’
 10|
 11|100평이 넘는 집을 갖고 있으면 뭐 하나. 상동 길드 유일의 패밀리어 마법사인 그는 일거리가 끊이질 않았다.
 12|
 13|레이드 팀은 게이트 돌고 나면 퇴근이라도 하지, 보안팀은 그딴 거 없이 매번 달라지는 아지트에서 밤을 새야 한다.
 14|
 15|“준수야, 밤샜냐?”
 16|
 17|“네.”
 18|
 19|김준수의 퀭한 얼굴을 본 보안팀의 동료가 혀를 찼다. 귀중한 패밀리어 마법사를 경호하기 위해 남아 있던 한 사람이다.
 20|
 21|“고생 많다. 저 새끼는 어떻게 집 밖으로 한 발자국을 안 나오냐?”
 22|
 23|“그러니까요. 며칠째 감시 중인데 지금까지 딱 두 번 나왔어요, 두 번. 고양시 쪽 부동산 한 번이랑 일산 스토어.”
 24|
 25|“이래서 표적 대상은 흡연자인 게 좋은데. 걔들은 담배 피우러 나오기라도 하잖아.”
 26|
 27|새로 구한 고양이를 패밀리어 삼아 밤새 아파트 동 입구에서 기다렸지만 표적은 꿈쩍도 하지 않았다.
 28|
 29|유일한 사건이라면 기다림에 지쳐 야옹거리며 울다가 경비 아저씨한테 쫓겨날 뻔했던 것뿐이다.
 30|
 31|“평화 길드? 보니까 규모도 작던데 레이드도 안 뛰나.”
 32|
 33|“쟤들 지금 휴가래.”
 34|
 35|“휴가요?”
 36|
 37|“어. 2조에 있는 내 동기가 평화 길드 다른 애들 감시 중인데 다 쉬고 있다던데?”
 38|
 39|“아…… 그쪽 상황은 어떻대요?”
 40|
 41|“어제부로 철수. 여자 하나랑 아저씨 하난데 금방 끝났다더라. 팀장 반응 봐서는 그쪽에서 뭐 하나 건진 거 같긴 한데 잘은 모르겠고.”
 42|
 43|“후우. 이쪽도 그냥 적당히 하고 철수하지.”
 44|
 45|깊은 한숨을 내쉬는 김준수를 동료가 안쓰러운 표정으로 바라봤다.
 46|
 47|“길드에 딱 한 명 있는 패밀리어 마법사를 특별히 붙인 이유가 있지 않겠어?”
 48|
 49|“그래 봤자 C급 헌터인데, 이렇게까지 공들이는 건 좀 아니지 않아요?”
 50|
 51|“어쩌겠냐. 까라면 까야 하는걸. 팀장이 어제처럼 쪼아 대도 그러려니 해.”
 52|
 53|“적당히 쪼아 대야죠. 애초에 홍우진인가 하는 그 사람이랑 얘기해서 잘 협력했으면 진작 끝났을 문젠데.”
 54|
 55|“길드장님께 보여 주고 싶은 거지. 우리 보안팀이 홍우진보다 훨씬 낫다. 내 리더십이 이렇게 뛰어나다. 안 그래도 슬슬 하반기 인사이동 시즌인데 팀장도 똥줄 탈 만하잖아.”
 56|
 57|“……환장하겠네요.”
 58|
 59|“환장하지.”
 60|
 61|김준수는 머리라도 쥐어뜯고 싶은 마음이었지만 꾹 참았다. 그랬다가는 이제 겨우 봄철 새순처럼 돋아난 머리카락이 뽑혀 나갈지 모른다.
 62|
 63|‘아, 의사가 스트레스받으면 탈모 악화된다고 했는데.’
 64|
 65|그 쉬운 라이트 마법도 못 쓰는 민간인 의사지만 머리만 풍성하게 만들어 준다면 예수님으로 모실 수 있다.
 66|
 67|‘그러고 보니 오늘은 머리가 별로 안 빠진 것 같기도 하고.’
 68|
 69|김준수가 조심스럽게 정수리를 더듬으려던 그때였다.
 70|
 71|- 표적 확인. 표적 확인. 이동 중!
 72|
 73|무전기 너머로 들려오는 낮지만 긴박한 동료의 목소리.
 74|
 75|방 안의 두 사람은 물론이고 옆방에서 코를 골고 있던 보안팀장까지 벌떡 일어났다.
 76|
 77|추르릅. 입가의 침을 훔친 그가 외친다.
 78|
 79|“야! 김준수!”
 80|
 81|젠장. 아직 아침도 못 먹었는데.
 82|
 83|패밀리어 마법 쓰면 머리 또 빠지는데!
 84|
 85|‘씨바, 계약 끝나면 바로 길드 때려치운다.’
 86|
 87|눈물을 삼킨 김준수가 마나를 끌어 올렸다. 머리가 뜨거워지며 의식이 빨려 들어간다.
 88|
 89|‘충실한 종이여, 내 부름에 답하라. 링크!’
 90|
 91|화악!
 92|
 93|그리고 다음 순간, 차 밑에 엎드려 있던 새끼 고양이가 번쩍 눈을 떴다.
 94|
 95|미야옹.
 96|
 97|
 98|
 99|* * *
100|
101|
102|
103|나는 걸음을 멈췄다. 울음소리와 함께 갑자기 불쑥 튀어나온 검은 털 뭉치 때문이다.
104|
105|
106|
107|[Lv.2 고양이 - 패밀리어]
108|
109|
110|
111|“…….”
112|
113|또 고양이네. 이 자식들은 창의력이 이렇게 없나?
114|
115|아, 하나 달라지긴 했다. 이놈은 털 색이 새까맣다.
116|
117|미앙. 미야앙.
118|
119|새끼치고는 제법 당찬 걸음으로 다가온 고양이가 내 슬리퍼에 온몸을 비비적거렸다. 시전자가 누군지는 몰라도 클럽에서 좀 놀아 본 솜씨다.
120|
121|‘거참. 이런 식으로 관심받는 건 별론데.’
122|
123|하지만 새로운 패밀리어의 등장 덕분에 새로운 사실을 짐작할 수 있었다.
124|
125|‘이놈들, 한패가 아닌가?’
126|
127|하루 간격으로 고양이처럼 눈에 띄는 패밀리어를 두 마리나? 결코 좋은 접근 방식이 아니다. 오히려 황급히 따라 한다는 느낌이 강했다.
128|
129|냥!
130|
131|관심을 가져 달라는 듯이 울어 대는 고양이의 모습에 나는 피식 웃었다.
132|
133|“짜식, 귀엽네.”
134|
135|이놈을 데려가야 하나, 말아야 하나…….
136|
137|머리가 바쁘게 돌아가던 그때였다.
138|
139|“고양이가 애교가 많네. 아저씨가 기르는 거예요?”
140|
141|슬리퍼를 질질 끌며 다가온 한 남자. 40대 초반 정도로 보이는 얼굴은 지극히 평범했고 목 늘어난 티셔츠와 라면 국물이 묻은 축구 반바지는 친근하다.
142|
143|“아뇨. 길고양이인 것 같은데 갑자기 애교를 부리네요.”
144|
145|“이야, 이거 완전히 그거잖아. 개냥이.”
146|
147|“그러게요. 어제도 그렇고, 이 동네 고양이들은 애교가 많나 봐요.”
148|
149|“어제요?”
150|
151|“네, 어제도 한 마리 주웠거든요. 개냥이로.”
152|
153|“거 신기하네.”
154|
155|남자가 반쯤 타들어 간 담배를 한 모금 빨았다.
156|
157|“이렇게 보면 짐승들도 다 인연이 있는 것 같어. 좋은 주인이 될 것 같으니까 고양이가 애교도 부리고 하지.”
158|
159|“에이, 좋은 주인은 무슨. 그냥 원래 이런 성격인 것 같은데요?”
160|
161|“그런가? 야, 야, 이리 와 봐.”
162|
163|아저씨의 손짓에도 고양이는 꿈쩍도 하지 않는다.
164|
165|아니, 오히려 내 다리 사이로 파고들었다.
166|
167|“허허. 이놈 봐라. 어린 게 벌써부터 사람을 가릴 줄 아네.”
168|
169|내가 말없이 웃고만 있자 아저씨가 묻는다.
170|
171|“그래서, 키우시려고?”
172|
173|“글쎄요. 지금 급한 볼일이 있어서. 끝내고 왔을 때도 있으면 며칠 데리고 있어 보죠, 뭐.”
174|
175|“그때까지 이놈이 여기 있을까 모르겠네. 그치, 나비야?”
176|
177|에옹.
178|
179|“얼마 안 걸려요. 요 앞에 부동산 가는 거라.”
180|
181|“그래요? 참, 그쪽 젊은 양반은 처음 보는 분이시네. 나 여기 오래 살아서 어지간한 사람은 다 아는데. 부동산 가신다는 거 보니 새로 이사 오시는 분인가?”
182|
183|“저는 따로 살아서요. 가족들 보러 어쩌다 한 번씩만 옵니다. 부동산은 잠깐 뭐, 일이 있어서요.”
184|
185|“아아…….”
186|
187|후우. 마지막 연기가 바람에 흩어진다. 담배꽁초를 바닥으로 튕긴 아저씨가 입을 열었다.
188|
189|“이거 참, 내가 바쁜 사람 붙잡고 있었네. 마음 상한 건 아니죠?”
190|
191|“전혀요.”
192|
193|“그럼 다행이고. 다음에 만나면 알은체나 합시다. 이웃사촌끼리.”
194|
195|내가 대답했다.
196|
197|“네, 이웃사촌끼리.”
198|
199|“그럼 먼저 갑니다. 날씨도 좋은데 동네나 한 바퀴 돌아야지.”
200|
201|사람 좋은 웃음을 지은 아저씨가 걸음을 옮긴다. 휘적거리는 걸음으로 멀어지는 그의 뒷모습을 잠시 바라보며 생각했다.
202|
203|‘연기 잘하네.’
204|
205|야옹.
206|
207|그래, 너도 있었지.
208|
209|집을 나서자마자 연기자를 두 명이나 만났다. 길고양이와 이웃사촌이라는 탈을 쓴 연기자를.
210|
211|“금방 올 테니까 여기서 얌전히 기다리고 있어라, 응?”
212|
213|고양이가 무슨 소리냐는 듯 고개를 갸우뚱한다.
214|
215|하지만 나는 알고 있다. 저 녀석이 내 말을 알아들었고, 몇 시간이 흘러도 이 자리에 있을 거라는 사실을.
216|
217|그리고 하나 더.
218|
219|
220|
221|[Lv.42 김권동]
222|
223|
224|
225|우리 집 옆 동에는 헌터가 살지 않는다는 사실을.
226|
227|‘역시 한패가 아니야.’
228|
229|두 연기자의 등장은 짐작을 확신으로 바꾸기에 충분했다.
230|
231|집 앞 부동산을 향하는 내 발걸음은 한층 더 가벼워져 있었다.
232|
233|
234|
235|* * *
236|
237|
238|
239|늦은 아침, 슬리퍼를 질질 끌며 콧노래를 부르는 후줄근한 차림의 중년인. 어디에서나 흔하게 찾아볼 수 있는 모습인 그는 코너를 돌자마자 담배 한 개비를 빼 물었다.
240|
241|“어디 보자, 라이터가…….”
242|
243|손은 느릿느릿 주머니를 뒤지지만 눈은 바쁘게 움직인다.
244|
245|주위에 아무도 없는 것을 확인한 그가 라이터 대신 꺼낸 것은 초소형 무전기였다.
246|
247|“연기 괜찮았어? 나 헌터 말고 배우나 할 걸 그랬나 봐. 어째 전투보다 연기를 더 잘해.”
248|
249|- 나 팀장이다.
250|
251|툭. 입에 물고 있던 담배가 떨어졌다. 덕분에 자유로워진 입이 벙긋거린다.
252|
253|시바, 좆 됐네.
254|
255|황급히 정신을 수습한 보안팀 소속 C급 헌터, 김권동이 대답했다.
256|
257|“아, 예. 팀장님.”
258|
259|- 이야, 김권동이 연기 잘하데? 길드 관두고 할리우드 가도 되겠더라.
260|
261|“죄, 죄송합니다.”
262|
263|- 쫄기는, 칭찬이야. 그건 그렇고 표적은 어때? 냄새 못 맡았겠지?
264|
265|“제 생각으로는 그렇습니다.”
266|
267|패밀리어 마법을 사용 중인 김준수를 통해 대화를 이미 들었을 텐데도 재확인하는 이유는 간단하다.
268|
269|고양이의 시선으로는 표적의 모든 것을 명확하게 담을 수 없기 때문이다.
270|
271|- 확실해? 100%?
272|
273|“90%입니다.”
274|
275|- 자식이, 90%가 확실한 거냐? 이럴 때는 자신감 있게 질러야지.
276|
277|“섣부른 판단은 금물이니까요.”
278|
279|김권동은 속으로 팀장을 욕했다.
280|
281|‘자신 있게 지르면 뭐 해. 나중에 일 잘못되면 나한테 제일 먼저 지랄할 거면서.’
282|
283|이런 식으로 빠져나갈 구멍은 만들어 둬야 한다. 김권동의 90%는 팀장의 10%가 더해져야 비로소 완성된다.
284|
285|- 그런 모습 아주 보기 좋아. 다음 행동은 알지?
286|
287|팀장의 기분 좋은 목소리는 이제야 100%가 됐다는 신호다.
288|
289|김권동은 저 멀리서 걸어오는 주민을 피해 슬그머니 발길을 틀었다.
290|
291|“예. 자연스럽게 주위 맴돌면서 관찰하겠습니다.”
292|
293|- 그래, 특이 사항 생기면 바로바로 보고하고.
294|
295|“예.”
296|
297|- 그럼 수고.
298|
299|1분 남짓 이루어진 둘의 대화는 아무도 듣지 못했다.
300|
301|이번에는 진짜 라이터를 꺼내 담배에 불을 붙인 김권동이 연기를 깊이 들이마셨다.
302|
303|“시발, 몬스터한테 죽는 것보다 폐암 걸려 죽는 게 더 빠르겠네.”
304|
305|
306|
307|* * *
308|
309|
310|
311|보안팀장이 바빠졌다. 외부 감시 인원은 총 셋. 남은 두 명에게 지시를 하달하고 만전을 기해야 한다.
312|
313|“1번.”
314|
315|- 1번 등장했습니다.
316|
317|“전체 채널로 듣고 있었지? 표적이 가는 부동산은 어떻게 됐어?”
318|
319|- 인근 상가에 두 개 있고, 두 곳 모두 도청 마법 장비 깔았습니다.
320|
321|“잘했어. 표적 위치는?”
322|
323|- 아직 안 보이는…… 아, 등장했습니다. 약 300m 밖에서 접근 중.
324|
325|“자리 떠. 어차피 장비 깔았으니까 괜히 접촉할 필요 없어.”
326|
327|- 예. 특이 사항 있으면 바로 보고하겠습니다.
328|
329|“오케이. 2번은?”
330|
331|- 현 위치에서 대기 중입니다.
332|
333|무전기 너머로 들려오는 굵은 목소리.
334|
335|근처 상가에 은신해 있던 또 다른 팀원의 대답에 보안팀장이 고개를 끄덕였다.
336|
337|“이 자식 다른 길로 샐 수도 있으니까 잘 감시해.”
338|
339|- 네.
340|
341|은신, 추적 계열의 C급 헌터 넷과 패밀리어 마법사.
342|
343|전투력은 떨어지지만 이 분야에서는 하나같이 풍부한 경험이 있는 베테랑들이다.
344|
345|‘C급 헌터 하나한테 붙기에는 과분한 정도지.’
346|
347|처음에는 약간의 경계심이 있었다. 표적에 관하여 길드장이 특별히 언질한 부분이 있었기 때문이다.
348|
349|‘B급 게이트를 혼자 클리어했다고 했지, 아마.’
350|
351|하지만 놈에 관한 정보를 모을수록, 지켜보면 지켜볼수록 전혀 아니라는 생각이 들었다. 의심에 종지부를 찍은 건 정보의 출처가 임창수라는 사실이다.
352|
353|‘망나니 새끼가 맞아 죽기 싫어서 이빨 깐 거지.’
354|
355|어디서나 볼 수 있는 평범한 C급 헌터.
356|
357|그의 눈에 비친 진태경은 딱 그 정도였다.
358|
359|삑.
360|
361|- 표적, 부동산으로 들어갑니다.
362|
363|감시하고 있던 팀원의 무전.
364|
365|상동 길드 보안팀은 촉각을 곤두세웠다.
```

## Assembled English

```markdown
[P1]
# Chapter 96

[P2]
Kim Junsu was a C-rank Hunter in Sangdong Guild’s Security Team.

[P3]
He didn’t have an ounce of talent for elemental magic, but fortunately, he had awakened as a rare mental mage and was doing pretty well for himself.

[P4]
*Except I can never go home.*

[P5]
What good was owning a house of more than 330 square meters? As Sangdong Guild’s only Familiar mage, he never ran out of work.

[P6]
Raid teams at least got to go home after running a Gate. The Security Team had no such luxury. They had to stay up all night in a different hideout each time.

[P7]
“Junsu, did you pull an all-nighter?”

[P8]
“Yes.”

[P9]
A Security Team colleague clicked his tongue at Kim Junsu’s hollow-eyed face. He was the one person who had stayed behind to protect their valuable Familiar mage.

[P10]
“You’ve got it rough. How does that bastard not set one foot outside?”

[P11]
“Tell me about it. We’ve been watching him for days, and he’s only gone out twice. Twice. Once to a real-estate office in Goyang, and once to the Ilsan Store.”

[P12]
“This is why smokers make better targets. At least they come outside for a cigarette.”

[P13]
They had acquired a new cat to use as a Familiar and waited all night at the entrance to the apartment building, but the target hadn’t budged.

[P14]
The only incident had come when the cat, tired of waiting, started yowling and nearly got chased away by a security guard.

[P15]
“Peace Guild? It looked pretty small. Do they even go on raids?”

[P16]
“They’re on vacation right now.”

[P17]
“Vacation?”

[P18]
“Yeah. A buddy of mine in Team 2 is watching the other Peace Guild members, and he said they’re all taking time off.”

[P19]
“Ah… How are things going over there?”

[P20]
“They pulled out yesterday. There was one woman and one middle-aged man, but it ended quickly. Judging by the Team Leader’s reaction, it seems like they turned up something over there, but I don’t know the details.”

[P21]
“Phew. We should just do enough to get by and pull out, too.”

[P22]
His colleague gave Kim Junsu a pitying look as he heaved a deep sigh.

[P23]
“There has to be a reason they specially assigned the Guild’s only Familiar mage, right?”

[P24]
“He’s still only a C-rank Hunter. Don’t you think this is going a little overboard?”

[P25]
“What can we do? When they say jump, we jump. If the Team Leader keeps riding you like he did yesterday, just put up with it.”

[P26]
“He could stand to ease up. This would’ve been over ages ago if he’d talked things through with that Hong Woojin guy and cooperated properly.”

[P27]
“He wants to show off for the Guild Master. ‘Our Security Team is far better than Hong Woojin. Look at my outstanding leadership.’ Besides, it’s almost time for the second-half personnel reshuffle. No wonder the Team Leader’s sweating bullets.”

[P28]
“…This is driving me insane.”

[P29]
“Sure is.”

[P30]
Kim Junsu wanted to tear his hair out, but he held himself back. If he did, the hair that had only just begun sprouting like fresh spring shoots might come right out.

[P31]
*Ah, the doctor said stress makes hair loss worse.*

[P32]
The doctor was a civilian who couldn’t even use the simple Light magic, but if he could give Kim Junsu a full head of hair, Junsu would worship him as Jesus.

[P33]
*Come to think of it, maybe I haven’t lost much hair today.*

[P34]
Kim Junsu was cautiously reaching up to feel the crown of his head when—

[P35]
—Target confirmed. Target confirmed. Moving!

[P36]
A low but urgent voice came through the radio.

[P37]
The two men in the room—and even the Security Team Leader, who had been snoring in the next room—bolted upright.

[P38]
Slurp.

[P39]
The Team Leader wiped the drool from his mouth and shouted, “Hey! Kim Junsu!”

[P40]
*Damn it. I haven’t even had breakfast yet.*

[P41]
*Using Familiar magic makes my hair fall out again!*

[P42]
*Fuck this. The moment my contract ends, I’m quitting the Guild.*

[P43]
Swallowing back his tears, Kim Junsu drew up his mana. His head grew hot as his consciousness was sucked inward.

[P44]
*Faithful servant, answer my call. Link!*

[P45]
Whoosh!

[P46]
The next moment, a kitten lying beneath a car snapped its eyes open.

[P47]
“Myaow.”

[P48]
* * *

[P49]
I stopped walking.

[P50]
A black ball of fur had suddenly popped out with a cry.

[P51]
> **System**
>
> Lv. 2 Cat—Familiar

[P52]
“…”

[P53]
Another cat. Did these bastards have no creativity at all?

[P54]
Well, one thing was different. This one’s fur was pitch-black.

[P55]
“Miaow. Miaowww.”

[P56]
The kitten approached with a surprisingly bold stride for something so young, then rubbed its whole body against my slipper. Whoever was controlling it clearly knew how to work a club.

[P57]
*Man. I’m not into getting attention this way.*

[P58]
But the appearance of this new Familiar allowed me to make a new guess.

[P59]
*These guys aren’t working together, are they?*

[P60]
Two conspicuous Familiars, both in the form of cats, appearing a day apart? It was hardly a good approach. If anything, it felt like someone had hurriedly copied the first attempt.

[P61]
“Meow!”

[P62]
The cat cried as if demanding my attention, and I let out a quiet laugh.

[P63]
“You little thing. You’re cute.”

[P64]
Should I take it with me or not…?

[P65]
My mind was racing when—

[P66]
“That cat’s pretty affectionate. Is it yours, sir?”

[P67]
A man approached, dragging his slippers. He looked to be in his early forties, with an utterly ordinary face. His stretched-out T-shirt and soccer shorts stained with ramen broth gave him an approachable air.

[P68]
“No. I think it’s a stray, but it suddenly started acting affectionate.”

[P69]
“Wow, this is totally one of those. A dog-cat.”[^1]

[P70]
“Exactly. Just like yesterday. I guess the cats in this neighborhood are pretty affectionate.”

[P71]
“Yesterday?”

[P72]
“Yeah. I picked one up yesterday too. Another dog-cat.”

[P73]
“Well, that’s something.”

[P74]
The man took a drag from his half-smoked cigarette.

[P75]
“Times like this make you think even animals are brought together with people for a reason. It must think you’d make a good owner. That’s why it’s cozying up to you.”

[P76]
“Come on, what do you mean, a good owner? I think it just has this kind of personality.”

[P77]
“Is that so? Hey, hey, come here.”

[P78]
The cat didn’t budge at the man’s beckoning.

[P79]
No, it burrowed between my legs instead.

[P80]
“Well, look at this one. Young as it is, it already knows how to pick its people.”

[P81]
I only smiled without saying anything, so the man asked, “So, are you going to keep it?”

[P82]
“I’m not sure. I have something urgent to take care of. If it’s still here when I get back, maybe I’ll look after it for a few days.”

[P83]
“Who knows if it’ll still be here by then. Right, Nabi?”

[P84]
“Mrow.”

[P85]
“I won’t be long. I’m just going to the real-estate office right over there.”

[P86]
“Really? Oh, come to think of it, I’ve never seen you before, young man. I’ve lived here a long time, so I know just about everyone. Since you’re going to a real-estate office, are you moving into the neighborhood?”

[P87]
“I live somewhere else. I only come by once in a while to see my family. I just have something to take care of at the real-estate office.”

[P88]
“Ah…”

[P89]
Phew.

[P90]
His last breath of smoke scattered in the wind. The man flicked his cigarette butt onto the ground and said, “Well, look at me, holding up a busy man. You’re not offended, are you?”

[P91]
“Not at all.”

[P92]
“Then that’s good. If we meet again, let’s say hello. We’re neighbors, after all.”

[P93]
I answered, “Yes. We’re neighbors.”

[P94]
“Then I’ll be off. The weather’s nice, so I should take a lap around the neighborhood.”

[P95]
The man gave me a good-natured smile and started walking. I watched his retreating back for a moment as he moved away with a loose, swinging gait.

[P96]
*He’s a good actor.*

[P97]
“Meow.”

[P98]
Right. You’re here, too.

[P99]
The moment I left the house, I met two actors. Actors wearing the guises of a stray cat and a neighbor.

[P100]
“I’ll be back soon, so wait here quietly, okay?”

[P101]
The cat tilted its head as if it had no idea what I was talking about.

[P102]
But I knew. It had understood me, and it would still be sitting here even if several hours passed.

[P103]
And there was one more thing.

[P104]
> **System**
>
> Lv. 42 Kim Gwondong

[P105]
There weren’t any Hunters living in the building next to ours.

[P106]
*Just as I thought. They aren’t working together.*

[P107]
The appearance of the two actors was enough to turn my guess into certainty.

[P108]
My steps grew even lighter as I headed toward the real-estate office in front of the house.

[P109]
* * *

[P110]
Late that morning, a middle-aged man in shabby clothes dragged his slippers along while humming to himself. He looked like someone you could see anywhere.

[P111]
The moment he rounded the corner, he pulled out a cigarette and stuck it between his lips.

[P112]
“Let’s see. Where’s my lighter…”

[P113]
His hand rummaged slowly through his pocket, but his eyes darted around.

[P114]
Once he had confirmed that no one was nearby, he pulled out something other than a lighter: a miniature radio.

[P115]
“How was my acting? Maybe I should’ve become an actor instead of a Hunter. Seems like I’m better at acting than fighting.”

[P116]
—It’s me, the Team Leader.

[P117]
Plop.

[P118]
The cigarette fell from his mouth. His now-free lips moved soundlessly.

[P119]
*Fuck. I’m screwed.*

[P120]
Kim Gwondong, a C-rank Hunter in the Security Team, hurriedly collected himself and answered.

[P121]
“Ah, yes, Team Leader.”

[P122]
—Kim Gwondong’s pretty good at acting, huh? You could quit the Guild and go to Hollywood.

[P123]
“I-I’m sorry.”

[P124]
—Don’t get scared. That was a compliment. Anyway, how’s the target? He didn’t catch on, did he?

[P125]
“I don’t think so.”

[P126]
The Team Leader had already heard the conversation through Kim Junsu, but there was a simple reason he was asking again.

[P127]
A cat’s eyes could not capture everything about the target clearly.

[P128]
—Are you sure? One hundred percent?

[P129]
“Ninety percent.”

[P130]
—You little shit, is ninety percent certain? At times like this, you’re supposed to say it confidently and go for it.

[P131]
“It’s dangerous to jump to conclusions.”

[P132]
Kim Gwondong cursed the Team Leader inwardly.

[P133]
*What good would that do? If something goes wrong later, you’ll be the first one to rip me a new asshole.*

[P134]
He had to leave himself an escape route. Kim Gwondong’s ninety percent would only be complete once the Team Leader supplied the remaining ten.

[P135]
—That’s exactly the attitude I like to see. You know what to do next, right?

[P136]
The pleasure in the Team Leader’s voice signaled that they had finally reached one hundred percent.

[P137]
Kim Gwondong subtly changed direction to avoid a resident approaching in the distance.

[P138]
“Yes. I’ll circle the area naturally and keep watch.”

[P139]
—Right. Report immediately if anything unusual happens.

[P140]
“Yes.”

[P141]
—Keep up the good work, then.

[P142]
No one overheard the conversation, which lasted just over a minute.

[P143]
This time, Kim Gwondong took out a real lighter and lit his cigarette. He inhaled deeply.

[P144]
“Fuck. Lung cancer’s going to kill me before a monster does.”

[P145]
* * *

[P146]
The Security Team Leader got busy. There were three external surveillance personnel in total. He had to give instructions to the other two and make sure every precaution was taken.

[P147]
“Number One.”

[P148]
—Number One here.

[P149]
“You were listening on the all-team channel, right? What’s the situation with the real-estate office the target is heading to?”

[P150]
—There are two in the nearby shopping district. We’ve installed magical eavesdropping Equipment in both.

[P151]
“Good. Where’s the target?”

[P152]
—We haven’t seen him yet… Ah, there he is. He’s approaching from about 300 meters away.

[P153]
“Leave your position. We already installed the Equipment, so there’s no need to make contact for no reason.”

[P154]
—Yes. I’ll report immediately if anything unusual happens.

[P155]
“Okay. Number Two?”

[P156]
—Standing by at my current position.

[P157]
A deep voice came over the radio.

[P158]
The Security Team Leader nodded at the reply from another team member concealed in a nearby shop.

[P159]
“That bastard might veer off and take another route, so keep a close eye on him.”

[P160]
—Yes.

[P161]
Four C-rank Hunters specializing in stealth and tracking, plus a Familiar mage.

[P162]
They lacked combat power, but every one of them was a veteran with extensive experience in this field.

[P163]
*It’s overkill for one C-rank Hunter.*

[P164]
At first, he had been somewhat wary. The Guild Master had given them a special warning about the target.

[P165]
*They said he cleared a B-rank Gate alone, I think.*

[P166]
But the more information he gathered about the man, the more he watched him, the more he felt that was not the case at all. The fact that the information had come from Im Changsoo finally put an end to his doubts.

[P167]
*That good-for-nothing bastard made it all up because he didn’t want to get beaten to death.*

[P168]
An ordinary C-rank Hunter you could find anywhere.

[P169]
In his eyes, that was all Jin Taekyung was.

[P170]
Beep.

[P171]
—Target entering the real-estate office.

[P172]
A report came over the radio from the team member keeping watch.

[P173]
Sangdong Guild’s Security Team went on full alert.

[P174]
[^1]: A Korean term for a cat that acts like a dog—friendly and affectionate.
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
# Chapter 96

[P2]
Kim Junsu was a C-rank Hunter belonging to Sangdong Guild’s Security Team.

[P3]
He had not an ounce of talent for elemental magic, but fortunately, he had awakened as a rare type of mage—a mental mage—and was living a fairly successful life.

[P4]
*Except for the fact that I can’t go home.*

[P5]
What good was owning a house larger than 330 square meters? As the only Familiar mage in Sangdong Guild, he never ran out of work.

[P6]
Raid teams at least got to go home after running a Gate, but the Security Team had no such luxury. They had to spend every night in a different hideout.

[P7]
“Junsu, did you pull an all-nighter?”

[P8]
“Yes.”

[P9]
A colleague on the Security Team clicked his tongue when he saw Kim Junsu’s hollowed-out face. He was the one person who had stayed behind to protect their valuable Familiar mage.

[P10]
“You’re working hard. How does that bastard manage not to step outside even once?”

[P11]
“I know. We’ve been watching him for days, and he’s only gone out twice. Twice. Once to a real-estate office in Goyang and once to the Ilsan Store.”

[P12]
“This is why it’s better when the target smokes. At least smokers come outside to have a cigarette.”

[P13]
They had obtained a new cat to use as a Familiar and waited all night at the entrance of the apartment building, but the target had not budged.

[P14]
The only incident was when the cat, exhausted from waiting, started meowing and was nearly chased away by a security guard.

[P15]
“Peace Guild? It looked pretty small. Do they even go on raids?”

[P16]
“They’re on vacation right now.”

[P17]
“Vacation?”

[P18]
“Yeah. A guy from Team 2 is watching the other members of Peace Guild, and apparently they’re all taking time off.”

[P19]
“Ah… How’s that situation going?”

[P20]
“They pulled out yesterday. There was one woman and one middle-aged man, but it ended quickly. Judging by the Team Leader’s reaction, it seems like they turned up something over there, but I don’t know the details.”

[P21]
“Phew. We should just do enough to get by and pull out, too.”

[P22]
His colleague looked at Kim Junsu with pity as he let out a deep sigh.

[P23]
“There has to be a reason they specially assigned the Guild’s only Familiar mage, right?”

[P24]
“He’s still only a C-rank Hunter. Don’t you think this is going a little overboard?”

[P25]
“What can we do? When we’re told to do something, we have to do it. Even if the Team Leader hounds us like he did yesterday, we just have to put up with it.”

[P26]
“He should hound us in moderation. This would’ve been over ages ago if he had just talked to that Hong Woojin guy and cooperated properly.”

[P27]
“He wants to show the Guild Master. ‘Our Security Team is much better than Hong Woojin. My leadership is this outstanding.’ Besides, it’s almost time for the second-half personnel reshuffle. No wonder the Team Leader is sweating bullets.”

[P28]
“…This is driving me insane.”

[P29]
“It is.”

[P30]
Kim Junsu wanted to tear his hair out, but he held himself back. If he did, the hair that had only just begun sprouting like fresh spring shoots might come right out.

[P31]
*Ah, the doctor said stress makes hair loss worse.*

[P32]
The doctor was a civilian who couldn’t even use the simple Light magic, but if he could give Kim Junsu a full head of hair, Junsu would worship him as Jesus.

[P33]
*Come to think of it, maybe I haven’t lost much hair today.*

[P34]
That was when Kim Junsu cautiously reached up to feel the crown of his head.

[P35]
—Target confirmed. Target confirmed. Moving!

[P36]
A low but urgent voice came through the radio.

[P37]
The two men in the room—and even the Security Team Leader, who had been snoring in the next room—bolted upright.

[P38]
Slurp. After wiping the drool from his mouth, the Team Leader shouted.

[P39]
“Hey! Kim Junsu!”

[P40]
*Damn it. I haven’t even eaten breakfast yet.*

[P41]
*Using Familiar magic makes my hair fall out again!*

[P42]
*Fuck this. I’m quitting the Guild the moment my contract ends.*

[P43]
Swallowing back his tears, Kim Junsu drew up his mana. His head grew hot, and his consciousness was pulled inward.

[P44]
*Faithful servant, answer my call. Link!*

[P45]
Whoosh!

[P46]
The next moment, a kitten lying beneath a car opened its eyes wide.

[P47]
“Myaowww.”

[P48]
* * *

[P49]
I stopped walking.

[P50]
A black ball of fur had suddenly popped out with a cry.

[P51]
> **System**
>
> **Lv. 2 Cat—Familiar**

[P52]
“…”

[P53]
Another cat. Did these bastards have no creativity at all?

[P54]
Well, one thing was different. This one’s fur was pitch-black.

[P55]
“Miaow. Miaowww.”

[P56]
The kitten approached with surprisingly confident steps for such a young creature, then rubbed its entire body against my slipper. Whoever had cast the spell clearly knew its way around a club.

[P57]
*Man. I don’t like getting attention this way.*

[P58]
But the appearance of this new Familiar allowed me to make a new guess.

[P59]
*Could they be working together?*

[P60]
Two conspicuous Familiars, both in the form of cats, appearing a day apart? It was hardly a good approach. If anything, it felt like someone had hurriedly copied the first attempt.

[P61]
“Meow!”

[P62]
The cat cried as if demanding my attention, and I let out a quiet laugh.

[P63]
“You little thing. You’re cute.”

[P64]
Should I take it with me or not…?

[P65]
My mind was racing when—

[P66]
“That cat’s pretty affectionate. Is it yours, sir?”

[P67]
A man approached, dragging his slippers. He looked to be in his early forties, with an utterly ordinary face. His stretched-out T-shirt and soccer shorts stained with ramen broth gave him a friendly, familiar air.

[P68]
“No. I think it’s a stray, but it suddenly started acting affectionate.”

[P69]
“Wow, this is totally one of those. A dog-cat.”[^1]

[P70]
“Exactly. Just like yesterday. I guess the cats in this neighborhood are pretty affectionate.”

[P71]
“Yesterday?”

[P72]
“Yeah, I picked up another one yesterday. It was a dog-cat, too.”

[P73]
“That’s strange.”

[P74]
The man took a drag from a half-burned cigarette.

[P75]
“When you look at things like this, even animals seem to have connections with people. The cat’s acting affectionate because you look like you’d make a good owner.”

[P76]
“Come on, what do you mean, a good owner? I think it just has this kind of personality.”

[P77]
“Is that so? Hey, hey, come here.”

[P78]
The cat did not move at the man’s beckoning.

[P79]
No, it burrowed between my legs instead.

[P80]
“Well, look at this one. Young as it is, it already knows how to pick its people.”

[P81]
I only smiled without saying anything, so the man asked,

[P82]
“So, are you planning to raise it?”

[P83]
“I’m not sure. I have somewhere urgent to be right now. If it’s still here when I get back, I’ll keep it for a few days.”

[P84]
“Who knows if it’ll still be here by then. Right, Nabi?”

[P85]
“Mrow.”

[P86]
“It won’t take long. I’m just going to the real-estate office right over there.”

[P87]
“Really? Oh, come to think of it, I’ve never seen you before, young man. I’ve lived here a long time, so I know just about everyone. Since you’re going to a real-estate office, are you moving into the neighborhood?”

[P88]
“I live somewhere else, so I only come by to see my family once in a while. I just have something to take care of at the real-estate office.”

[P89]
“Ah…”

[P90]
Phew. His final breath of smoke scattered in the wind. The man flicked his cigarette butt onto the ground and spoke.

[P91]
“Well, look at me, holding up a busy man. You’re not offended, are you?”

[P92]
“Not at all.”

[P93]
“Then that’s good. If we meet again, let’s say hello. We’re neighbors, after all.”

[P94]
I answered,

[P95]
“Yes. We’re neighbors.”

[P96]
“Then I’ll be off. The weather’s nice, so I should take a lap around the neighborhood.”

[P97]
The man gave me a good-natured smile and started walking. I watched his retreating back for a moment as he moved away with a loose, swinging gait.

[P98]
*He’s good at acting.*

[P99]
“Meow.”

[P100]
Right. You’re here, too.

[P101]
The moment I left the house, I met two actors. Actors wearing the guises of a stray cat and a neighbor.

[P102]
“I’ll be back soon, so wait here quietly, okay?”

[P103]
The cat tilted its head as if it had no idea what I was talking about.

[P104]
But I knew. I knew that it understood me—and that it would still be sitting here even after several hours had passed.

[P105]
And there was one more thing.

[P106]
> **System**
>
> **Lv. 42 Kim Gwondong**

[P107]
There wasn’t a Hunter living in the building next to ours.

[P108]
*So they aren’t working together.*

[P109]
The appearance of the two actors was enough to turn my suspicion into certainty.

[P110]
My steps grew lighter as I headed toward the real-estate office in front of the house.

[P111]
* * *

[P112]
Late in the morning, a middle-aged man in shabby clothes dragged his slippers along while humming. He was such an ordinary sight that he could be found anywhere. The moment he turned the corner, he pulled out a cigarette and placed it between his lips.

[P113]
“Let’s see. Where’s my lighter…”

[P114]
His hand moved slowly as it rummaged through his pocket, but his eyes were moving busily.

[P115]
After confirming that no one was nearby, he pulled out something else instead of a lighter: a miniature radio.

[P116]
“Was the acting okay? Maybe I should’ve become an actor instead of a Hunter. I’m better at acting than fighting.”

[P117]
—It’s me, the Team Leader.

[P118]
Plop.

[P119]
The cigarette fell from his mouth. His now-free lips moved soundlessly.

[P120]
*Shit. I’m screwed.*

[P121]
The C-rank Hunter Kim Gwondong, a member of the Security Team, hurriedly pulled himself together and answered.

[P122]
“Ah, yes, Team Leader.”

[P123]
—Kim Gwondong’s pretty good at acting, huh? You could quit the Guild and go to Hollywood.

[P124]
“I-I’m sorry.”

[P125]
—Don’t get scared. It’s a compliment. Anyway, how’s the target? He didn’t smell anything, right?

[P126]
“I don’t think so.”

[P127]
The reason the Team Leader asked again, despite having already heard the conversation through Kim Junsu, was simple.

[P128]
A cat’s eyes could not capture everything about the target clearly.

[P129]
—Are you sure? One hundred percent?

[P130]
“Ninety percent.”

[P131]
—You little shit, is ninety percent certain? At times like this, you’re supposed to say it confidently and go for it.

[P132]
“Jumping to conclusions is dangerous.”

[P133]
Kim Gwondong cursed the Team Leader inwardly.

[P134]
*What good does it do me to say it confidently? If something goes wrong later, you’ll be the first one to chew me out.*

[P135]
He had to leave himself an escape route like this. Kim Gwondong’s ninety percent would only be complete once the Team Leader added his ten percent.

[P136]
—That attitude of yours is exactly what I like to see. You know what to do next, right?

[P137]
The Team Leader’s pleasant voice was a sign that he had finally reached one hundred percent.

[P138]
Kim Gwondong subtly changed direction to avoid a resident approaching from far away.

[P139]
“Yes. I’ll naturally circle around the area and keep watch.”

[P140]
—Right. Report immediately if anything unusual happens.

[P141]
“Yes.”

[P142]
—Then keep up the good work.

[P143]
The conversation between the two men lasted a little over a minute, and no one heard it.

[P144]
This time, Kim Gwondong took out a real lighter and lit his cigarette. He inhaled deeply.

[P145]
“Fuck. Looks like lung cancer’s going to kill me faster than a monster.”

[P146]
* * *

[P147]
The Security Team Leader got busy. There were three external surveillance personnel in total. He had to give instructions to the other two and make sure everything was in place.

[P148]
“Number One.”

[P149]
—Number One here.

[P150]
“You were listening on the all-team channel, right? What about the real-estate office the target is heading to?”

[P151]
—There are two in the nearby shopping district, and we’ve installed eavesdropping-magic Equipment in both.

[P152]
“Good. Where’s the target?”

[P153]
—We haven’t seen him yet… Ah, there he is. He’s approaching from about 300 meters away.

[P154]
“Leave your position. We already installed the Equipment, so there’s no need to make contact for no reason.”

[P155]
—Yes. I’ll report immediately if anything unusual happens.

[P156]
“Okay. Number Two?”

[P157]
—Waiting at my current position.

[P158]
A deep voice came through the radio.

[P159]
The Security Team Leader nodded at the reply from another team member hiding in a nearby shop.

[P160]
“That bastard might take another route, so keep a close eye on him.”

[P161]
—Yes.

[P162]
Four C-rank Hunters specializing in stealth and tracking, along with a Familiar mage.

[P163]
Their combat power was low, but every one of them was a veteran with extensive experience in this field.

[P164]
*It’s overkill for one C-rank Hunter.*

[P165]
At first, he had been somewhat wary. The Guild Master had given them a special warning about the target.

[P166]
*They said he cleared a B-rank Gate alone, I think.*

[P167]
But the more information he gathered about the man, the more he watched him, the more he felt that was not the case at all. The fact that the information had come from Im Changsoo finally put an end to his doubts.

[P168]
*That good-for-nothing bastard made it all up because he didn’t want to get beaten to death.*

[P169]
An ordinary C-rank Hunter whom one could find anywhere.

[P170]
That was all Jin Taekyung was in his eyes.

[P171]
Beep.

[P172]
—Target entering the real-estate office.

[P173]
A report came over the radio from the team member keeping watch.

[P174]
Sangdong Guild’s Security Team went on full alert.

[P175]
[^1]: A Korean term for a cat that acts like a dog—friendly and affectionate.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 진태경    | **Jin Taekyung**   |
| 철수     | **Cheol Soo**      |
| 임창수    | **Im Changsoo**   |
| 홍우진    | **Hong Woojin**   |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 평화 | **Peace Guild** | Guild name. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 96,
  "passed": true,
  "metrics": {
    "source_characters": 5585,
    "translation_characters": 12549,
    "length_ratio": 2.247,
    "source_paragraphs": 172,
    "translation_paragraphs": 174
  },
  "errors": [],
  "warnings": [
    {
      "code": "numbers",
      "message": "Arabic numerals from the source are absent",
      "details": {
        "values": [
          "10",
          "100",
          "90"
        ]
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "철수",
        "preferred": "Cheol Soo"
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
        "korean": "고양",
        "romanization": "goyang"
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
