# Fidelity Gate — Chapter 92

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
  1|＃92화
  2|
  3|
  4|
  5|[표적 보고서]
  6|
  7|이름 : 진태경
  8|
  9|나이 : 27
 10|
 11|거주지 : 주소지 xxx-xxx 희망 고시원. 가족과 별거 중.
 12|
 13|가족관계 : 1남 1녀 중 장남. 11년 전 아버지 사고사. 어머니와 여동생에 관한 정보는 따로 첨부.
 14|
 15|
 16|
 17|조사를 지시한 지 사흘 만에 받아 보는 보고서다. 다섯 장에 걸쳐 빽빽하게 적힌 정보들을 읽은 임춘수가 입을 열었다.
 18|
 19|“야, 1팀장아.”
 20|
 21|“예, 길드장님.”
 22|
 23|맞은편에 앉아 있던 1팀장이 대답했다. 길드장인 임춘수를 제외하면 상동 길드 유일한 A급 헌터이자 임춘수의 충직한 오른팔이다.
 24|
 25|“이 보고서, 읽어 봤냐?”
 26|
 27|“아직 안 읽어 봤습니다.”
 28|
 29|“왜?”
 30|
 31|“길드장님 지시니까요. 추후 들어오는 정보는 중간에서 거르지 말고 그대로 보고하라고 하셨습니다.”
 32|
 33|“그럼 이참에 읽어 봐.”
 34|
 35|임춘수가 내미는 보고서를 공손히 받아 든 1팀장의 눈동자가 바삐 움직였다. 10분 정도 후, 고개를 든 그가 중얼거렸다.
 36|
 37|“이건 좀.”
 38|
 39|“그 보고서, 어떻게 생각하냐?”
 40|
 41|“전 길드장님 판단에 따를 뿐입니다.”
 42|
 43|“아냐, 허심탄회하게 말해 봐.”
 44|
 45|잠깐 망설이던 1팀장이 대답했다.
 46|
 47|“정보가 잘못된 것 같습니다.”
 48|
 49|“정확히 어떤 부분이?”
 50|
 51|“보고서 대상인 진태경은 불과 보름 전까지 F급 헌터였습니다. 그러나 C급 헌터로 재각성에 성공했죠. 여기까지는 드문 일이긴 해도 불가능하진 않습니다.”
 52|
 53|“계속.”
 54|
 55|“하지만 임창수 팀장, 아니 임창수 헌터와 해당 레이드에 참여했던 인원들의 증언에 의하면 진태경은 B급 몬스터인 미노타우로스 무리를 단신으로 해치웠습니다.”
 56|
 57|“최소 다섯 마리. 최대 열 마리였지, 아마?”
 58|
 59|“네. 심지어 보스 몬스터는 일격에 쓰러트렸다고 했죠.”
 60|
 61|“그래. C급 헌터 나부랭이가 미노타우로스 대전사를 한 방에. 이게 말이 되냐?”
 62|
 63|“말이 안 된다고 생각합니다.”
 64|
 65|“그럼 뭘까?”
 66|
 67|결코 몰라서 물어보는 것이 아니다. 1팀장이 자신과 같은 생각을 하고 있는지 다시 한번 확인하는 과정일 뿐이다.
 68|
 69|“의심이 가는 부분이 셋 있습니다.”
 70|
 71|“읊어 봐.”
 72|
 73|“첫째, 보고서가 잘못됐을 경우입니다.”
 74|
 75|“이 보고서, 누가 작성한 거지? 홍, 홍 뭐였는데. 홍길동은 확실히 아니고.”
 76|
 77|“홍우진입니다. 아직 젊고 경력은 얼마 되지 않았습니다만, 실력은 정평이 나 있습니다.”
 78|
 79|“그래, 홍우진인지 홍길동인지 하는 그 새끼한테 다시 한번 확인해. 으름장도 좀 놓고. 아무튼 그래서 두 번째는?”
 80|
 81|“둘째, 임창수 헌터와 다른 인원들이 입을 맞춰 거짓말을 한 경우입니다.”
 82|
 83|“창수 그 녀석이 정신이 똑바로 안 박혀 있어서 그렇지, 살면서 나한테 거짓말 쳐 본 적이 없다. 계속.”
 84|
 85|“마지막은 진태경이 아직 확인되지 않은 A급 헌터이거나 혹은…….”
 86|
 87|침착하던 1팀장의 얼굴 위에 곤란한 빛이 스쳤다. 잠시 후, 그가 머뭇머뭇 입을 열었다.
 88|
 89|“3차 각성자가 아닐까요?”
 90|
 91|“3차?”
 92|
 93|“……네.”
 94|
 95|“1팀장아. 네가 말해 놓고도 황당하지? 3차 각성자가 말이 되냐, 응?”
 96|
 97|1팀장은 고개를 숙이는 것으로 대답을 대신했다.
 98|
 99|그 모습에 혀를 찬 임춘수가 보고서를 집어 들었다. 그의 손끝에서부터 극한의 냉기가 흘러나온다.
100|
101|파스스슥. 차창!
102|
103|“보고서 다시 작성해. 이번 주까지 끝마치고 월요일 출근할 때 책상 앞에 갖다 놔. 산뜻하게.”
104|
105|“알겠습니다.”
106|
107|“그리고 거, 누구야. 평화 길드인가 사랑 길드인가 거기 다른 놈들 관련 정보는 어떻게 됐어?”
108|
109|“……저, 그에 관해서 지금 막 보고드리려고 했습니다만.”
110|
111|“뭐야, 하나도 파악 안 됐어?”
112|
113|“세 명 제외하고는 전부 파악 완료된 상태입니다.”
114|
115|임춘수가 눈살을 찌푸렸다.
116|
117|“세 명? 그중 하나는 진태경일 테고. 나머지 둘은?”
118|
119|“평화 길드의 길드장과 팀장입니다.”
120|
121|아들놈에게 들어 본 적이 있다. 팀장이라는 젊은 놈은 싸가지가 없고, 길드장이라는 장년인은 레이드 내내 허허 웃기만 하는 속없는 인간이라고.
122|
123|“그놈들이 왜?”
124|
125|“락(Lock)이 걸려 있었습니다.”
126|
127|“뭐?”
128|
129|“말씀드린 그대롭니다. 개인 정보는 물론이고 계좌 관련해서까지 모두 보안 상태라 감찰팀에서도 당혹스러워하고 있습니다.”
130|
131|“돈 아꼈냐?”
132|
133|길드를 운영하려면 기관의 도움이 필요하다. 각 기관에 근무하는 타락한 공무원들은 뇌물을 받고 정보를 넘겨주는 걸 주저하지 않는다.
134|
135|“안 그래도 듬뿍 안겨 줬는데…….”
136|
137|“그랬는데?”
138|
139|“그쪽에서도 좀 꺼리는 기색이 역력합니다. 그쪽 말로는 상부 기관에서 보안을 걸어 놔서 건드리기가 어렵다더군요.”
140|
141|임춘수는 황당했다.
142|
143|만들어진 지 한 달도 안 된 길드. 길드원을 다 합쳐 봐야 레이드 팀 하나도 안 나오는 소규모 길드다. 아니, 그 정도면 길드가 아니라 친목회라고 해도 이상하지 않다.
144|
145|그런데 그깟 놈들이 뭐라고 락이 걸려 있단 말인가?
146|
147|“허, 이 자식들 봐라.”
148|
149|“어떻게 할까요?”
150|
151|“일단 그 부분은 더 깊게 파지 말고 내버려 둬. 이번에 돈 찔러 준 놈들 입단속도 확실히 하고.”
152|
153|대격변 시절, 불같은 성격으로 유명했던 임찬수는 길드를 운영하면서 중요한 한 가지를 배웠다.
154|
155|목표를 이루기 위해서는, 그리고 목표 이상의 성과를 얻기 위해서는 침착하고 신중해야 한다는 것이다.
156|
157|“그럼 그 셋 빼고는 전부 파악 끝났지?”
158|
159|“네, 완벽합니다.”
160|
161|철두철미한 성격으로 신임을 얻은 1팀장의 말이다. 임춘수는 고개를 끄덕였다.
162|
163|“보안 걸려 있다는 두 놈은 방금 내가 말한 대로 조치하고. 우선 진태경 그놈만 집중적으로 파. 길드 감사팀 몇 명 동원해서 따로 감시 인원 늘리고.”
164|
165|“따로……말입니까?”
166|
167|“그래, 보고서 상태 보니까 영 아니야. 생각해 보면 우리 길드 감사팀도 뭐, 딱히 밀릴 거 없잖아?”
168|
169|“그렇긴 합니다만.”
170|
171|1팀장이 순간 멈칫했다. 의뢰를 하러 갔을 때 홍우진이 신신당부했던 말이 생각나서였다.
172|
173|
174|
175|‘이 의뢰, 받는 순간 이거 내 일 되는 겁니다. 알죠? 일주일 안에 이 새끼 그날 입은 팬티 색까지 알아낼 테니까 믿고 맡겨요. 괜히 그쪽에서 일 벌렸다가 감시 대상이 눈치 까면 내 일 망치는 거니까.’
176|
177|
178|
179|경력은 짧아도 일 잘한다고 알음알음 입소문이 나 있는 홍우진이다. 말투는 건방졌지만 프로다운 모습에 신뢰가 갔고, 직접 약속까지 했다.
180|
181|‘말씀드려야 할 것 같은데.’
182|
183|하지만 1팀장이 꺼내려던 반대 의견은 임춘수의 한마디에 목구멍 안으로 쏙 돌아갔다.
184|
185|“왜? 더 할 말 있어?”
186|
187|“아, 아닙니다. 그대로 전달하겠습니다.”
188|
189|“그래, 가 봐.”
190|
191|요즘 임춘수의 기분이 좋지 않다. 최대한 비위를 맞춰 주면서 좋은 방향으로 이끌어 가는 것이 그의 일이다.
192|
193|‘괜찮겠지? 괜찮을 거야.’
194|
195|1팀장은 길드장실을 나오면서도 찝찝한 기분을 감추지 못했다.
196|
197|
198|
199|* * *
200|
201|
202|
203|집, 휴가.
204|
205|이 두 단어는 생각만으로도 행복감을 준다. 실제로도 그랬고. 그런데…….
206|
207|왜앵. 왜애애애앵.
208|
209|“아오, 미치겠네.”
210|
211|나는 전광석화 같은 속도로 파리를 후려쳤다. 평범한 손바닥도 아닌 공력이 실린 손바닥이다. 일격에 즉사한 파리를 쓰레기통에 버리고 소파로 돌아왔다.
212|
213|“뭔 놈의 파리 새끼들이 이렇게 많아?”
214|
215|물을 마시려고 잠깐 거실로 나온 하연이가 한숨을 푹 내쉬었다.
216|
217|“여름이니까 그렇지, 오빠 바보야?”
218|
219|“그 정도가 아니라니까, 지금.”
220|
221|“뭐 많아 봤자 얼마나 많다고. 방금도 한 마리밖에 없었잖아.”
222|
223|“한 마리씩 계속 들어오니까 문제지. 잡는 족족 어디서 자꾸 들어오네.”
224|
225|“몇 마리나 잡았는데?”
226|
227|“하늘에 맹세코 오전부터 지금까지 100마리는 잡았다.”
228|
229|“과장하는 것 봐. 이래서 남자들이란…….”
230|
231|“진짜라고!”
232|
233|“알았어, 알았어.”
234|
235|와, 미치겠네. 나는 머리를 쥐어뜯으며 새로운 파리를 때려잡았다. 백 마리? 결코 과장이 아니다. 이놈의 동네는 어떻게 되었길래 한 집에 파리가 이렇게 들끓을 수 있지?
236|
237|‘창문에 꿀이라도 발라 놨나.’
238|
239|처음에는 그냥 거슬리는 정도였다. 앞서 하연이가 말했던 것처럼 여름이니까 당연한 현상이라고 생각했다.
240|
241|하지만 갈수록 뭔가 이상하다는 걸 깨달았다.
242|
243|‘한 30마리쯤 잡은 후였지.’
244|
245|이 염병할 것들이 쉬지 않고 들어온다! 한 놈을 잡으면 또 한 놈이, 그놈을 잡으면 다른 놈이 들어와서 자리를 잡았다.
246|
247|집 안의 모든 창문을 닫고 기감으로 수색 작업까지 거쳤음에도 파리 군단의 악몽은 이어졌다.
248|
249|왜애애앵.
250|
251|“저거 봐, 그새를 못 참고 또 한 마리 들어오잖아. 이놈들 도대체 어디서 들어오는 거야?”
252|
253|미처 발견 못 한 미세한 틈 같은 게 있나 꼼꼼하게 살펴봤지만 나로서는 도저히 알 수 없었다. 말 그대로 개미 새끼 한 마리 통과할 만한 공간에서 들어오는 듯싶었다.
254|
255|“때려잡지 말고 가만히 둬. 그럼 조용해지니까.”
256|
257|“그게 무슨 창의적인 헛소리냐. 가만히 둔다고 쟤들이 가만히 있어? 왱왱 하는 소리에 잠도 못 잘 게 뻔한데.”
258|
259|“내 방 파리는 가만히 있던데?”
260|
261|“뭐?”
262|
263|“내 방에도 한 세 마리 정도 있다고. 처음에는 신경 쓰여서 잡을까 했는데, 가만히 두니까 안 날아다니고 가만히 책상에 앉아 있어.”
264|
265|“그거야 잠깐이고. 너 안 보는 사이에 엄청 날아다닐걸.”
266|
267|“그냥 좀 게으른 파리들인 것 같던데. 한 번도 안 움직였어.”
268|
269|“말이 되는 소리를 해라.”
270|
271|“진짜라니까. 10만 원 내기 콜?”
272|
273|“10만 원은 있냐? 수험생 주제에.”
274|
275|“당연히 있지. 지난번에 오빠한테 받은 거.”
276|
277|“나한테 받은 용돈으로 나랑 내기를 하겠다고?”
278|
279|“쫄리면 뒈지시든지.”
280|
281|“……콜.”
282|
283|시바, 돈이 이렇게 돌고 도는구나. 우리는 하연이의 방으로 곧장 직행했다. 얌전히 앉아 있는 파리 한 마리를 가리키며 녀석이 의기양양하게 웃는다.
284|
285|“봤지? 내 말이 맞지? 빨리 10만 원 내놔.”
286|
287|“내놓긴 뭘 내놔. 실험을 해 봐야지.”
288|
289|나는 파리 위로 손바닥을 내리쳤다. 딱 일반인 수준의, 파리가 충분히 피할 수 있는 속도였다. 그런데…….
290|
291|움찔. 후다닥.
292|
293|그 순간에 화들짝 놀라더니 다리를 바쁘게 놀려 도망치는 파리.
294|
295|그 모습을 본 나는 황당함을 금치 못했다. 하연이도 저게 뭔가 하는 얼굴이다.
296|
297|“동생아.”
298|
299|“으, 응.”
300|
301|“요즘 파리들은 다 저러냐?”
302|
303|“그, 그럴 수도 있지 않을까? 아무튼 10만 원 줘.”
304|
305|“줘야지. 주긴 주는데…… 저 파리 좀 이상하지 않아?”
306|
307|“파리가 파리지. 그냥 좀 이상한 애 같은데.”
308|
309|“저런 파리가 어디 있어. 내가 살면서 고블린에 미노타우로스는 봤어도 이렇게까지 안 날아다니는 파리는 처음 본다.”
310|
311|말이 끝난 그 순간이었다.
312|
313|왜애애앵-
314|
315|“…….”
316|
317|“…….”
318|
319|수상해. 너무 수상해. 타이밍도 공교롭지만 마치 평범해 보이려고 애쓰는 듯한 날갯짓은 더 이상하다. 날아다니는 것도 뭔가 어설프게 비틀거리고.
320|
321|‘그런 건 둘째치고 기분 나빠. 이 느낌 묘하게 익숙한데.’
322|
323|어디서 비슷한 기분을 느꼈더라?
324|
325|아, 그랬지. 이틀 전 집 보러 갔다가 돌아오던 그 골목길.
326|
327|어쩐지 누군가 나를 감시하는 것 같은 기시감.
328|
329|‘내가 진짜 예민한 건가.’
330|
331|파리를 노려보던 내가 [기감]을 끌어 올렸다. 이제 반경 70미터에 이르는 기감의 발동 범위가 집 전체 구석구석으로 뻗어 나갔다.
332|
333|그리고 아무도 예상치 못한 일이 일어났다.
334|
335|띠링. 띠링. 띠링.
336|
337|
338|
339|[Lv.1 집파리 – 패밀리어]
340|
341|[Lv.1 검정파리 – 패밀리어]
342|
343|[Lv.1 금파리 - 패밀리어]
344|
345|
346|
347|“……?”
348|
349|뭔데, 이거.
```

## Assembled English

```markdown
[P1]
# Chapter 92

[P2]
> **Target Report**
>
> **Name:** Jin Taekyung
>
> **Age:** 27
>
> **Residence:** Address xxx-xxx, Hope Goshiwon[^1]. Living separately from his family.
>
> **Family:** Eldest son in a family of one son and one daughter. Father died in an accident eleven years ago. Information on his mother and younger sister attached separately.

[P3]
Im Chunsoo received the report three days after ordering the investigation. After reading through five densely packed pages, he spoke.

[P4]
“Hey, Team 1 Leader.”

[P5]
“Yes, Guild Master.”

[P6]
The Team 1 Leader sitting across from him answered. Aside from Guild Master Im Chunsoo himself, he was Sangdong Guild’s only A-rank Hunter and Chunsoo’s loyal right-hand man.

[P7]
“Have you read this report?”

[P8]
“Not yet.”

[P9]
“Why not?”

[P10]
“Because of your instructions, Guild Master. You told me to pass along any new information exactly as it came in, without filtering it first.”

[P11]
“Then read it now.”

[P12]
The Team 1 Leader respectfully accepted the report Im Chunsoo held out. His eyes raced across the pages. About ten minutes later, he looked up and muttered,

[P13]
“This is a little…”

[P14]
“What do you think of the report?”

[P15]
“I’ll defer to your judgment, Guild Master.”

[P16]
“No. Speak frankly.”

[P17]
After a brief hesitation, the Team 1 Leader answered.

[P18]
“I think the information is incorrect.”

[P19]
“Which part, exactly?”

[P20]
“The subject of the report, Jin Taekyung, was an F-rank Hunter until just two weeks ago. However, he successfully reawakened as a C-rank Hunter. That much is rare, but not impossible.”

[P21]
“Go on.”

[P22]
“But according to the testimony of Team Leader Im Changsoo—no, Hunter Im Changsoo—and the others who participated in the raid, Jin Taekyung single-handedly defeated a group of B-rank Minotaurs.”

[P23]
“At least five. As many as ten, if I remember correctly?”

[P24]
“Yes. They even said he brought down the boss monster with a single strike.”

[P25]
“Right. Some measly C-rank Hunter took down a Minotaur Warrior in one blow. Does that make any sense?”

[P26]
“I don’t think it does.”

[P27]
“Then what is it?”

[P28]
He was not asking because he genuinely did not know. He only wanted to confirm once again whether the Team 1 Leader was thinking the same thing he was.

[P29]
“There are three suspicious possibilities.”

[P30]
“Let’s hear them.”

[P31]
“First, the report may be wrong.”

[P32]
“Who wrote this report? Hong… What was it? Definitely not Hong Gil-dong.”

[P33]
“Hong Woojin. He’s still young and relatively inexperienced, but his skills are well regarded.”

[P34]
“Right, that Hong Woojin—or Hong Gil-dong, or whatever the hell his name is. Check with that bastard again. Put some pressure on him, too. Anyway, what’s the second?”

[P35]
“Second, Hunter Im Changsoo and the others may have coordinated their stories and lied.”

[P36]
“Changsoo may be an idiot with his head screwed on wrong, but he’s never lied to me in his life. Continue.”

[P37]
“The last possibility is that Jin Taekyung is an A-rank Hunter who has not yet been confirmed, or perhaps…”

[P38]
A troubled look crossed the otherwise composed Team 1 Leader’s face. After a moment, he spoke hesitantly.

[P39]
“Could he be a third-awakening Hunter?”

[P40]
“Third awakening?”

[P41]
“…Yes.”

[P42]
“Team 1 Leader. It sounds absurd even to you, doesn’t it? A third-awakening Hunter? Does that make any sense?”

[P43]
The Team 1 Leader lowered his head in lieu of an answer.

[P44]
Im Chunsoo clicked his tongue at the sight and picked up the report. Extreme cold began to flow from his fingertips.

[P45]
Crackle. Crash!

[P46]
“Rewrite the report. Finish it by the end of this week and put it on my desk when you come in on Monday. Make it nice and clean.”

[P47]
“Yes, sir.”

[P48]
“And what about the others from that Peace Guild—or was it Love Guild?”

[P49]
“…I was just about to report on that.”

[P50]
“What? You haven’t found out anything?”

[P51]
“We’ve finished identifying everyone except for three people.”

[P52]
Im Chunsoo frowned.

[P53]
“Three? One must be Jin Taekyung. Who are the other two?”

[P54]
“The Guild Master and Team Leader of Peace Guild.”

[P55]
He had heard about them from his son. The young Team Leader was an insolent brat, while the middle-aged Guild Master was a clueless man who had done nothing but chuckle throughout the entire raid.

[P56]
“Why those two?”

[P57]
“There was a Lock on them.”

[P58]
“What?”

[P59]
“Exactly as I said. Not only their personal information, but even their account details are all under security restrictions. The Audit Team is at a loss as well.”

[P60]
“Did you skimp on the money?”

[P61]
Running a Guild required help from government agencies. The corrupt officials who worked for them had no qualms about accepting bribes in exchange for information.

[P62]
“I already gave them plenty…”

[P63]
“And yet?”

[P64]
“They seem very reluctant on their end as well. They said an upper agency had placed the security lock, making it difficult for them to touch.”

[P65]
Im Chunsoo was dumbfounded.

[P66]
The Guild had existed for less than a month. Its entire membership was too small to fill a single raid team. At that size, it would hardly be strange to call it a social club instead of a Guild.

[P67]
And yet, who the hell were those bastards to have a Lock placed on them?

[P68]
“Huh. Look at these bastards.”

[P69]
“What should we do?”

[P70]
“Don’t dig any deeper into that for now. Leave it alone. And make damn sure the people we paid this time keep their mouths shut.”

[P71]
During the Great Cataclysm, Im Chunsoo had been famous for his fiery temper. But running a Guild had taught him one important lesson.

[P72]
To achieve a goal—and to gain results beyond that goal—one had to remain calm and cautious.

[P73]
“So aside from those three, you’ve identified everyone?”

[P74]
“Yes. Completely.”

[P75]
The Team 1 Leader’s meticulous nature had earned Im Chunsoo’s trust. Chunsoo nodded.

[P76]
“Deal with those two locked targets as I said. For now, focus only on Jin Taekyung. Mobilize a few people from the Guild Audit Team and increase the surveillance separately.”

[P77]
“Separately…?”

[P78]
“Yeah. This report is no good. And when you think about it, our Guild Audit Team is no slouch either, is it?”

[P79]
“That’s true, but…”

[P80]
The Team 1 Leader faltered. He remembered what Hong Woojin had repeatedly stressed when he commissioned the investigation.

[P81]
> “The moment I accept this assignment, it becomes my job. Got it? Within a week, I’ll find out what color underwear the bastard wore that day, so leave it to me. If you start something on your end and the surveillance target catches on, you’ll ruin my job.”

[P82]
Hong Woojin had little experience, but word had spread that he was good at his job. His arrogant tone aside, his professionalism had inspired confidence, and the Team 1 Leader had personally given him his word.

[P83]
*I should probably tell him.*

[P84]
But the objection he was about to raise slipped straight back down his throat at Im Chunsoo’s next words.

[P85]
“Why? Something else you want to say?”

[P86]
“Oh, no, sir. I’ll relay it exactly as you said.”

[P87]
“Good. You can go.”

[P88]
Im Chunsoo had been in a bad mood lately. It was the Team 1 Leader’s job to keep him appeased as much as possible and guide him in a favorable direction.

[P89]
*It’ll be fine, right? It’ll be fine.*

[P90]
Even after leaving the Guild Master’s office, the Team 1 Leader could not shake his unease.

[P91]
* * *

[P92]
Home. Vacation.

[P93]
Just thinking about those two words made me happy. The reality was every bit as wonderful.

[P94]
Except…

[P95]
Bzzzz. Bzzzzzz.

[P96]
“Ah, this is driving me crazy.”

[P97]
I swatted a fly with lightning speed. Not with an ordinary palm, either, but one charged with internal energy. I tossed the fly, dead in one strike, into the trash and returned to the sofa.

[P98]
“Why the hell are there so many fucking flies?”

[P99]
Hayeon, who had briefly come out into the living room to get a drink of water, let out a deep sigh.

[P100]
“It’s summer, you idiot, Oppa.”

[P101]
“I’m telling you, this is more than that.”

[P102]
“How many could there possibly be? There was only one just now.”

[P103]
“That’s the problem. They keep coming in one at a time. Every time I kill one, another shows up from somewhere.”

[P104]
“How many have you killed?”

[P105]
“I swear to heaven, I’ve killed at least a hundred since this morning.”

[P106]
“Look at you exaggerating. This is why men are…”

[P107]
“I’m serious!”

[P108]
“Okay, okay.”

[P109]
Wow. This was driving me insane. I tore at my hair and swatted another fly. A hundred? That was no exaggeration. What the hell was wrong with this neighborhood that one house could be overrun with so many flies?

[P110]
*Did someone smear honey on the windows?*

[P111]
At first, they had merely been annoying. Like Hayeon said, I assumed they were only around because it was summer.

[P112]
But the more time passed, the more I realized that something was strange.

[P113]
*It was after I’d killed about thirty of them.*

[P114]
These damn things kept coming in without a break! I would kill one, then another would come in. I would kill that one, and a different fly would take its place.

[P115]
Even after I closed every window and searched the whole house with Qi Sense, the nightmare of the fly army continued.

[P116]
Bzzzzzz.

[P117]
“See? Another one came in before we could even turn around. Where the hell are these things coming from?”

[P118]
I carefully searched for some tiny gap I had failed to notice, but I could not figure it out. They seemed to be coming through spaces barely large enough for a single ant to pass through.

[P119]
“Stop swatting them and leave them alone. Then they’ll quiet down.”

[P120]
“What kind of creative bullshit is that? You think they’ll sit still just because you leave them alone? We obviously won’t be able to sleep with them buzzing all night.”

[P121]
“The flies in my room stay still.”

[P122]
“What?”

[P123]
“There are about three in my room, too. They bothered me at first, so I thought about killing them, but when I left them alone, they stopped flying around and just sat on my desk.”

[P124]
“That’s only temporary. They probably fly around like crazy when you’re not looking.”

[P125]
“I think they’re just lazy flies. They haven’t moved even once.”

[P126]
“Say something that makes sense.”

[P127]
“I’m serious. Want to bet a hundred thousand won?”

[P128]
“You even have a hundred thousand won? You’re supposed to be studying for exams.”

[P129]
“Of course I do. It’s the money you gave me last time.”

[P130]
“You’re going to bet against me with the allowance I gave you?”

[P131]
“If you’re scared, you can just die.”

[P132]
“…Deal.”

[P133]
Shit. So this was how money went around in circles.

[P134]
We went straight to Hayeon’s room. She pointed at a fly sitting quietly on her desk and grinned triumphantly.

[P135]
“See? I was right, wasn’t I? Hurry up and hand over the hundred thousand won.”

[P136]
“Hand over what? We need to run an experiment first.”

[P137]
I brought my palm down over the fly. I struck at an ordinary person’s speed, slow enough for the fly to dodge easily. But then…

[P138]
Flinch. Scramble.

[P139]
The fly jumped in alarm and scurried away as fast as its legs could carry it.

[P140]
I was dumbfounded. Hayeon looked just as baffled.

[P141]
“Sis.”

[P142]
“Y-Yeah?”

[P143]
“Are all flies these days like that?”

[P144]
“M-Maybe they do? Anyway, give me the hundred thousand won.”

[P145]
“I’ll give it to you. I will. But isn’t that fly strange?”

[P146]
“A fly is a fly. That one’s just a little strange.”

[P147]
“What kind of fly acts like that? I’ve seen goblins and Minotaurs in my life, but I’ve never seen a fly that flies around so little.”

[P148]
The instant I finished speaking—

[P149]
Bzzzzzz—

[P150]
“……”

[P151]
“……”

[P152]
Suspicious. Way too suspicious.

[P153]
The timing was questionable enough, but the way its wings moved—as if it were trying hard to look ordinary—was even stranger. Even its flight was awkward and unsteady.

[P154]
*Never mind that. It gives me the creeps. This feeling is weirdly familiar.*

[P155]
Where had I felt something like this before?

[P156]
Oh, right. That alley I had walked through two days ago, on my way home from viewing the house.

[P157]
That strange sense of déjà vu, as though someone were watching me.

[P158]
*Am I really just being oversensitive?*

[P159]
I glared at the fly and raised my Qi Sense. Its activation range now extended to a radius of seventy meters, spreading into every corner of the house.

[P160]
And then something no one could have expected happened.

[P161]
Ding. Ding. Ding.

[P162]
> **System**
>
> Lv. 1 Housefly—Familiar
>
> Lv. 1 Black Blow Fly—Familiar
>
> Lv. 1 Green Bottle Fly—Familiar

[P163]
“…?”

[P164]
*What the hell is this?*

[P165]
[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement.
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
# Chapter 92

[P2]
> **Target Report**
>
> **Name:** Jin Taekyung
>
> **Age:** 27
>
> **Residence:** Address xxx-xxx, Hope Goshiwon[^1]. Living separately from his family.
>
> **Family:** Eldest son in a family of one son and one daughter. Father died in an accident eleven years ago. Information on his mother and younger sister attached separately.

[P3]
This was the report Im Chunsoo received three days after ordering the investigation. After reading through the densely packed information filling five pages, he opened his mouth.

[P4]
“Hey, Team 1 Leader.”

[P5]
“Yes, Guild Master.”

[P6]
The Team 1 Leader seated across from him answered. Apart from Guild Master Im Chunsoo, he was the only A-rank Hunter in Sangdong Guild, as well as Im Chunsoo’s loyal right hand.

[P7]
“Did you read this report?”

[P8]
“Not yet.”

[P9]
“Why not?”

[P10]
“Because it was your order, Guild Master. You told us to report any information that came in without filtering it along the way.”

[P11]
“Then read it now.”

[P12]
The Team 1 Leader politely accepted the report Im Chunsoo held out to him. His eyes moved rapidly across the pages. About ten minutes later, he raised his head and muttered,

[P13]
“This is a little…”

[P14]
“What do you think of the report?”

[P15]
“I can only follow your judgment, Guild Master.”

[P16]
“No. Speak frankly.”

[P17]
After a brief hesitation, the Team 1 Leader answered.

[P18]
“I think the information is incorrect.”

[P19]
“Which part, exactly?”

[P20]
“The subject of the report, Jin Taekyung, was an F-rank Hunter until only half a month ago. However, he succeeded in reawakening as a C-rank Hunter. That much is rare, but not impossible.”

[P21]
“Go on.”

[P22]
“But according to the testimony of Team Leader Im Changsoo—no, Hunter Im Changsoo—and the others who participated in that raid, Jin Taekyung single-handedly defeated a group of B-rank monsters, the Minotaurs.”

[P23]
“Minimum five. Maximum ten, if I remember correctly?”

[P24]
“Yes. They even said he brought down the boss monster with a single strike.”

[P25]
“Right. A mere C-rank Hunter taking down a Minotaur Warrior with one blow. Does that make any sense?”

[P26]
“I don’t think it does.”

[P27]
“Then what is it?”

[P28]
He was not asking because he genuinely did not know. He only wanted to confirm once again whether the Team 1 Leader was thinking the same thing he was.

[P29]
“There are three things that concern me.”

[P30]
“List them.”

[P31]
“First, the report may be wrong.”

[P32]
“Who wrote this report? Hong… What was it? Definitely not Hong Gil-dong.”

[P33]
“Hong Woojin. He’s still young and doesn’t have much experience, but his ability is well known.”

[P34]
“Right, that Hong Woojin—or Hong Gil-dong, or whatever the hell his name is. Check with that bastard again. Put some pressure on him, too. Anyway, what’s the second?”

[P35]
“Second, Hunter Im Changsoo and the others may have coordinated their stories and lied.”

[P36]
“Changsoo’s an idiot who can’t think straight, but he’s never lied to me in his life. Continue.”

[P37]
“The last possibility is that Jin Taekyung is an A-rank Hunter whose strength has not yet been confirmed, or perhaps…”

[P38]
A troubled look crossed the otherwise calm Team 1 Leader’s face. After a moment, he hesitantly opened his mouth.

[P39]
“Could he be a third-awakening Hunter?”

[P40]
“Third awakening?”

[P41]
“…Yes.”

[P42]
“Team 1 Leader. Doesn’t it sound absurd even to you? A third-awakening Hunter? Does that make any sense?”

[P43]
The Team 1 Leader answered by lowering his head.

[P44]
Im Chunsoo clicked his tongue at the sight and picked up the report. Extreme cold began to flow from his fingertips.

[P45]
Crackle. Crash!

[P46]
“Rewrite the report. Finish it by the end of this week and put it on my desk when you come in on Monday. Make it nice and clean.”

[P47]
“Yes, sir.”

[P48]
“And what about the information on the other people from that Peace Guild—or was it Love Guild?”

[P49]
“……I was just about to report on that.”

[P50]
“What? You haven’t found out anything?”

[P51]
“We’ve finished identifying everyone except for three people.”

[P52]
Im Chunsoo frowned.

[P53]
“Three? One of them must be Jin Taekyung. Who are the other two?”

[P54]
“The Guild Master and Team Leader of Peace Guild.”

[P55]
He had heard about them from his son. The young Team Leader was an insolent brat, while the middle-aged Guild Master was a clueless man who had done nothing but chuckle throughout the entire raid.

[P56]
“Why those two?”

[P57]
“There was a Lock on them.”

[P58]
“What?”

[P59]
“Exactly as I said. Not only their personal information, but even their account details are all under security restrictions. The Audit Team is at a loss as well.”

[P60]
“Did you skimp on the money?”

[P61]
“Not at all. I already gave them plenty…”

[P62]
“And yet?”

[P63]
“They seem very reluctant on their end as well. They said an upper agency had placed the security lock, making it difficult for them to touch.”

[P64]
Im Chunsoo was dumbfounded.

[P65]
A Guild that had not even existed for a month. A small Guild whose entire membership could not even make up one raid team. No, at that point, calling it a Guild was strange. It would not have been odd to call it a social club instead.

[P66]
And yet, who the hell were those bastards to have a Lock placed on them?

[P67]
“Huh. Look at these bastards.”

[P68]
“What should we do?”

[P69]
“Don’t dig any deeper into that part for now. Leave it alone. And make absolutely sure the people we paid this time keep their mouths shut.”

[P70]
During the Great Cataclysm, Im Chunsoo had been famous for his fiery temper. But after running a Guild, he had learned one important thing.

[P71]
To achieve a goal—and to gain results beyond that goal—one had to remain calm and cautious.

[P72]
“So everything else is completely investigated?”

[P73]
“Yes. Completely.”

[P74]
That was the answer of the Team 1 Leader, who had earned Im Chunsoo’s trust through his meticulous nature. Im Chunsoo nodded.

[P75]
“Deal with those two locked targets as I said. For now, focus only on Jin Taekyung. Mobilize a few people from the Guild Audit Team and increase the surveillance separately.”

[P76]
“Separately…?”

[P77]
“Yes. Looking at the state of this report, it’s no good. When you think about it, our Guild Audit Team isn’t exactly outclassed, is it?”

[P78]
“That’s true, but…”

[P79]
The Team 1 Leader suddenly hesitated. He remembered what Hong Woojin had repeatedly stressed when he went to commission Woojin for the job.

[P80]
> “The moment I accept this assignment, it becomes my job. Got it? Within a week, I’ll find out the color of this bastard’s underwear on the day in question, so leave it to me. If you cause trouble on your end and the surveillance target catches on, you’ll ruin my job.”

[P81]
Hong Woojin had little experience, but word had spread that he was good at his work. Despite Woojin’s arrogant way of speaking, his professionalism had inspired trust, and the Team 1 Leader had personally given him his word.

[P82]
*I should probably tell him.*

[P83]
But the objection the Team 1 Leader was about to raise went straight back down his throat at Im Chunsoo’s next words.

[P84]
“Why? Is there something else you want to say?”

[P85]
“Oh, no, sir. I’ll relay it exactly as you said.”

[P86]
“Good. You can go.”

[P87]
Im Chunsoo had been in a bad mood lately. It was the Team 1 Leader’s job to keep him appeased as much as possible and guide him in a favorable direction.

[P88]
*It’ll be fine, right? It will be.*

[P89]
Even after leaving the Guild Master’s office, the Team 1 Leader could not shake his uneasy feeling.

[P90]
* * *

[P91]
Home. Vacation.

[P92]
Just thinking about those two words made me happy. And in reality, it was just as wonderful. But…

[P93]
Bzzzz. Bzzzzzz.

[P94]
“Ah, this is driving me crazy.”

[P95]
I swatted at a fly with lightning-fast speed. It was not an ordinary palm strike, either—my palm was charged with internal energy. After killing the fly instantly, I tossed it into the trash and returned to the sofa.

[P96]
“Why the hell are there so many flies?”

[P97]
Hayeon, who had briefly come out into the living room to get a drink of water, let out a deep sigh.

[P98]
“It’s summer, you idiot, Oppa.”

[P99]
“It’s not just that.”

[P100]
“What’s the big deal? How many could there be? There was only one just now.”

[P101]
“That’s the problem. They keep coming in one at a time. Every time I catch one, another one keeps coming in from somewhere.”

[P102]
“How many have you caught?”

[P103]
“I swear to heaven, I’ve caught at least a hundred since this morning.”

[P104]
“Look at you exaggerating. This is why men are…”

[P105]
“I’m serious!”

[P106]
“Okay, okay.”

[P107]
Damn, this was driving me crazy. I tore at my hair and swatted down another fly. A hundred? I was not exaggerating at all. What had happened to this neighborhood that so many flies could swarm into one house?

[P108]
*Did someone smear honey on the windows?*

[P109]
At first, they had only been annoying. Just like Hayeon had said, I thought it was a normal phenomenon because it was summer.

[P110]
But the more time passed, the more I realized that something was strange.

[P111]
*It was after I’d killed about thirty of them.*

[P112]
These damn things kept coming in without a break! I would kill one, then another would come in. I would kill that one, and a different fly would take its place.

[P113]
Even after closing every window in the house and searching with my Qi Sense, the nightmare of the fly army continued.

[P114]
Bzzzzzz.

[P115]
“See? Another one came in before we could even turn around. Where the hell are these things coming from?”

[P116]
I carefully searched for some tiny gap I had failed to notice, but I could not figure it out. They seemed to be coming through spaces barely large enough for a single ant to pass through.

[P117]
“Don’t swat them. Just leave them alone. Then they’ll quiet down.”

[P118]
“What kind of creative bullshit is that? You think they’ll stay still just because you leave them alone? We won’t be able to sleep with all that buzzing.”

[P119]
“The flies in my room stay still.”

[P120]
“What?”

[P121]
“There are about three in my room, too. They bothered me at first, so I thought about killing them, but when I left them alone, they stopped flying around and just sat on my desk.”

[P122]
“That’s only temporary. They must fly around like crazy when you’re not looking.”

[P123]
“I think they’re just lazy flies. They haven’t moved even once.”

[P124]
“Say something that makes sense.”

[P125]
“I’m serious. Want to bet a hundred thousand won?”

[P126]
“You even have a hundred thousand won? You’re an examinee.”

[P127]
“Of course I do. It’s from the money you gave me last time.”

[P128]
“You’re going to bet against me with the allowance I gave you?”

[P129]
“If you’re scared, you can just die.”

[P130]
“……Deal.”

[P131]
Shit. So this was how money went around in circles.

[P132]
We went straight to Hayeon’s room. She pointed at a fly sitting quietly in place and grinned triumphantly.

[P133]
“See? I was right, wasn’t I? Hand over the hundred thousand won.”

[P134]
“Hand over what? We need to run an experiment first.”

[P135]
I brought my palm down over the fly. I struck at an ordinary person’s speed, slow enough for the fly to dodge easily. But then…

[P136]
Flinch. Scramble.

[P137]
The fly startled violently and scurried away, moving its legs as fast as it could.

[P138]
I could not hide my bewilderment. Hayeon wore a similar expression.

[P139]
“Sis.”

[P140]
“Y-Yeah?”

[P141]
“Are all flies these days like that?”

[P142]
“Th-They could be, couldn’t they? Anyway, give me the hundred thousand won.”

[P143]
“I’ll give it to you. I will. But isn’t that fly strange?”

[P144]
“A fly is a fly. It’s just a weird one.”

[P145]
“What kind of fly acts like that? I’ve seen goblins and Minotaurs in my life, but I’ve never seen a fly that flies around so little.”

[P146]
The instant I finished speaking—

[P147]
Bzzzzzz—

[P148]
“……”

[P149]
“……”

[P150]
Suspicious. Extremely suspicious.

[P151]
The timing was questionable enough, but the way its wings moved—as if it were trying hard to look ordinary—was even stranger. Even its flight was awkward and unsteady.

[P152]
*Forget that. It gives me the creeps. This feeling is weirdly familiar.*

[P153]
Where had I felt something similar?

[P154]
Oh, right. That alley I had walked through on the way home two days ago, after looking at a house.

[P155]
That déjà vu of someone secretly watching me.

[P156]
*Am I really just being oversensitive?*

[P157]
I glared at the fly and raised my Qi Sense. Its activation range now extended to a radius of seventy meters, spreading into every corner of the house.

[P158]
And then something no one could have expected happened.

[P159]
Ding. Ding. Ding.

[P160]
> **System**
>
> Lv. 1 Housefly—Familiar
>
> Lv. 1 Black Blow Fly—Familiar
>
> Lv. 1 Green Bottle Fly—Familiar

[P161]
“……?”

[P162]
*What the hell is this?*

[P163]
[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 진태경    | **Jin Taekyung**   |
| 임춘수    | **Im Chunsoo**    |
| 임창수    | **Im Changsoo**   |
| 홍우진    | **Hong Woojin**   |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 정파     | **orthodox faction**                             |                                                       |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 평화 | **Peace Guild** | Guild name. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 집파리 | **Housefly** | System label for a Level 1 fly familiar. |
| 검정파리 | **Black Blow Fly** | System label for a Level 1 fly familiar. |
| 금파리 | **Green Bottle Fly** | System label for a Level 1 fly familiar. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 92,
  "passed": true,
  "metrics": {
    "source_characters": 5542,
    "translation_characters": 12003,
    "length_ratio": 2.166,
    "source_paragraphs": 167,
    "translation_paragraphs": 165
  },
  "errors": [],
  "warnings": [
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
        "korean": "재각성",
        "preferred": "reawakening"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "여름이",
        "preferred": "Yeoreum"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "상동",
        "romanization": "sangdong"
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
