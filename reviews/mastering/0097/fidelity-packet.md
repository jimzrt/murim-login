# Fidelity Gate — Chapter 97

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
  1|＃97화
  2|
  3|
  4|
  5|“어머, 어서 오세용.”
  6|
  7|40대로 보이는 아주머니가 콧소리와 함께 나를 맞이했다.
  8|
  9|집에서 가까운 부동산이라 그런가? 가끔 집에 올 때 얼핏 스쳐 갔던 얼굴 같기도 하다.
 10|
 11|“젊은 분이 오셨네. 뭐 마실래요? 커피? 율무차? 콜라?”
 12|
 13|“커피로 주세요.”
 14|
 15|“블랙, 프림, 아니면…….”
 16|
 17|“블랙이요.”
 18|
 19|“총각이 커피 마실 줄 아네.”
 20|
 21|쉴 새 없이 다다다 쏘아 대는 말을 한 귀로 흘리며 자리에 앉았다. 수다스러운 부동산 아줌마보다 더 신경 써야 할 곳이 있었기 때문이다.
 22|
 23|‘이건…….’
 24|
 25|부동산 내부에 흐르고 있는 익숙한 기운.
 26|
 27|바로 마나(Mana)다.
 28|
 29|‘도청 마법인가?’
 30|
 31|사장이 설치해 놓은 보안 마법일 확률은 거의 없다. 집도 아니고 부동산에 비싼 마법 제품을 둘 리는 없으니까.
 32|
 33|나를 감시하는 놈들이 미리 손을 쓴 게 분명했다.
 34|
 35|‘뭐, 충분히 예상했던 일이지.’
 36|
 37|패밀리어까지 쓰는 놈들이니 도청 마법 정도야 애교다.
 38|
 39|문제는 도대체 놈들이 몇 명이며 어디 있냐는 건데…….
 40|
 41|“자아, 커피 나왔습니다.”
 42|
 43|나는 예의 바른 웃음을 지으며 커피잔을 받았다.
 44|
 45|“아, 감사합니다.”
 46|
 47|감사하다는 말은 진심이다.
 48|
 49|지금부터 놈들의 근거지를 알려 줄 사람이니까.
 50|
 51|
 52|
 53|* * *
 54|
 55|
 56|
 57|- 그래서, 우리 잘생긴 사장님은 어떻게 오셨을까?
 58|
 59|- 집 좀 알아보려고요.
 60|
 61|도청 마법이 전달해 주는 음성은 또렷했다. 잠시 패밀리어 마법을 해제한 김준수와 또 다른 팀원, 보안팀장은 약속이나 한 듯이 서로를 바라봤다.
 62|
 63|“저놈 얼마 전에도 부동산 가지 않았냐?”
 64|
 65|“네, 고양시 쪽으로 갔었죠. 그때는 저희가 투입되기 전이라 1팀장님이 홍우진한테 정보 받아서 넘겨주셨고.”
 66|
 67|“준수 말이 맞습니다. 나중에 저희가 부동산 찾아가서 캐 보니까 계약금까지 걸고 왔더라고요.”
 68|
 69|“쟤 계좌에 지금 얼마 들어 있지?”
 70|
 71|진태경의 계좌 현황은 이미 훤히 알고 있는 보안팀이다.
 72|
 73|보안팀장의 말에 팀원이 재빨리 태블릿을 꺼내 보고서를 띄웠다.
 74|
 75|“약 37억 정도 됩니다. 이 중에 30억 원은 새로운 집 매입 비용으로 나갈 거고요.”
 76|
 77|“그거, 구입하는 거 확실해?”
 78|
 79|“조만간 집주인이랑 날 잡아서 계약한다는 말까지 들었으니까 구입할 생각인 건 확실합니다. 조사해 보니 표적이 어릴 때 살던 동네라서 좀 각별한 의미가 있는 것 같더군요.”
 80|
 81|“그렇단 말이지…….”
 82|
 83|보안팀장은 눈살을 찌푸렸다.
 84|
 85|곧 새로운 집에 전 재산의 대부분을 쏟아부을 놈이다. 그런데 이제 와서 이 동네에 무슨 집을 또 알아본단 말인가?
 86|
 87|‘심지어 길드도 부천에 있고.’
 88|
 89|무슨 생각인지는 몰라도 어쩐지 찝찝한 기분이다.
 90|
 91|“야, 소리 좀만 더 키워 봐.”
 92|
 93|“옙.”
 94|
 95|세 사람의 귀에 이어지는 대화가 흘러 들어온다.
 96|
 97|- 원하는 조건이 어떻게 되시는데?
 98|
 99|- 월세 아니면 전세요.
100|
101|- 몇 개 있긴 한데…… 알다시피 이 동네가 안전 구역에 걸쳐져 있어서 좀 비싸.
102|
103|- 괜찮아요. 저 헌터거든요.
104|
105|- 어머, 헌터였어? 어쩐지 몸 좋더라니. 등급이 어떻게 돼? 아, 이런 거 물어보면 좀 주책인가?
106|
107|- 뭐 그럭저럭? 별로 안 높아요. C급.
108|
109|- 어머, 어머. 돈 잘 벌겠네. 팔뚝 한 번 만져 봐도 돼? 오호호!
110|
111|- 하하, 매물 좋은 거 보여 주시면 생각해 볼게요. 아니, 아예 싹 다 보여 주세요. 전세고 매매고 마음에 드는 거 있으면 사 버려야지.
112|
113|듣고 있던 세 사람은 기가 찼다.
114|
115|“이 새끼 아주 신났네. 신났어.”
116|
117|“오죽하겠습니까. F급으로 살다가 재각성 후 목돈 턱턱 들어오니까 가오가 확 살겠죠.”
118|
119|“음, 그렇지. 한창 그럴 때지.”
120|
121|다들 경험해 봐서 안다. 새로운 세계에 발을 디딘 저 기분.
122|
123|비싸서 쳐다보지도 못하던 명품이 우습게 느껴지고 사람들의 보는 눈이 달라진다.
124|
125|“저 자식이 딱 그 상태네, 지금.”
126|
127|“마음에 드는 게 있으면 사긴 개뿔이. 계약한 집 잔금 치르면 네 잔고로는 전세가 고작이다, 이놈아.”
128|
129|“그래도 부럽네요. 쟤는 뭐 먹고 머리털이 저렇게 풍성하지?”
130|
131|진태경의 치기 어린 언행들을 지켜보고 있자니 한심하면서도 피식 실소가 새어 나온다.
132|
133|어느새 세 사람의 마음이 느슨하게 풀어졌다. 귀는 열려 있지만 라디오 방송을 듣는 기분이다.
134|
135|- 여기 어때요? 전세로 하면 5억 정도? 안전 구역인 거 감안하면 시세보다 훨씬 저렴하게 내놓은 거야.
136|
137|- 괜찮네요. 다른 곳은 없어요?
138|
139|- 왜 없겠어, 당연히 있지. 방금 보여 준 곳 바로 옆옆 동에 매물 있는데…… 아, 여긴 얼마 전에 나갔었네. 월세였는데 조건이 워낙 좋아서.
140|
141|- 아, 그래요?
142|
143|- 응. 총각이 며칠만 더 일찍 왔어도 건지는 건데. 관리가 잘 안 되어 있는 대신에 월세가 쌌거든. 뭐 그거야 돈 있으면 리모델링으로 해결할 수 있는 문제니까.
144|
145|- 그거 아쉽네요.
146|
147|- 나도 아쉬워. 웬 무섭게 생긴 아저씨가 와서 무슨 명령조로 얘기하더라니까? 지가 나한테 집을 맡겨 놨나…… 나도 기왕이면 젊고 잘생긴 총각한테 넘기는 게 기분 좋잖아. 그치?
148|
149|- 어휴, 완전 꼰대였나 보네요.
150|
151|- 조폭인가 싶어서 찍소리 못 했지. 몸에서도 홀아비 냄새가 진동을 해서 아주 죽는 줄 알았어. 호호호.
152|
153|빠드득.
154|
155|옆에서 들려오는 이 가는 소리. 김준수와 팀원은 터져 나오려는 웃음을 꾹 억눌렀다.
156|
157|‘팀장이네.’
158|
159|‘팀장이야.’
160|
161|조폭 같은 인상에 홀아비 냄새. 여기까지만 들어도 보안팀장이란 사실을 알 수 있다.
162|
163|인상이 어찌나 험악한지, 그가 처음 상동 길드에 입사했을 당시 면접관이 무서워서 더 볼 것도 없이 뽑았다는 소문도 있을 정도다.
164|
165|“저 아줌마가 미쳤나…….”
166|
167|이를 바득바득 갈던 팀장이 고개를 홱 돌렸다. 웃음을 참느라 얼굴이 벌겋게 달아오른 두 사람이 황급히 고개를 숙였다.
168|
169|“참느라 힘들어 보인다?”
170|
171|“아, 아닙니다.”
172|
173|“그런 사실 없습니다.”
174|
175|애써 부정해 보지만 이미 빈정이 상할 대로 상한 팀장은 자리에서 일어났다. 40대 중반의 솔로인 그에게 있어 홀아비라는 말은 결코 건드려서는 안 되는 부분이었다.
176|
177|“홀아비 냄새 씻으러 사우나 다녀올 테니까 오는 즉시 볼 수 있도록 녹취록 작성해 놔.”
178|
179|“예?”
180|
181|김준수와 다른 팀원은 어이가 없었다.
182|
183|부동산에서 허세 부리는 C급 헌터와 푼수 아줌마. 두 사람의 별것 없는 대화에 무슨 녹취록까지 작성한단 말인가.
184|
185|“팀장님. 이거 다 자동으로 저장되고 있는…….”
186|
187|“각자 소견서도 A4 용지 한 장 꽉 채워서 준비해. 중요한 표적이니까 팀원들 의견도 수렴해 봐야지.”
188|
189|“…….”
190|
191|“…….”
192|
193|도대체 언제부터 팀원들 의견을 물어봤다고? 그리고 그 중요한 표적을 두고 팀장이란 양반이 사우나를 간다는 게 말이 되나.
194|
195|속 좁은 상관의 화풀이에 두 사람의 표정이 일그러졌다.
196|
197|“내 말 못 들었어? 복명복창한다, 실시!”
198|
199|“……네.”
200|
201|“……실시.”
202|
203|“자식들이 빠져 가지고 말이야. 팀장 알기를 아주 개똥으로 알아요.”
204|
205|부하들을 노려본 보안팀장이 씩씩거리며 방을 빠져나갔다.
206|
207|쾅! 아파트 현관문 닫히는 소리에 남아 있던 두 사람이 동시에 참았던 말을 토해 낸다.
208|
209|“아니, 시바.”
210|
211|“이건 해도 해도 너무한 거 아니에요?”
212|
213|“지 인상 더럽고 결혼 못 한 걸 왜 우리한테 화풀이하냐고.”
214|
215|“인상만 더럽습니까? 아줌마 얘기 들어 보니까 명령조로 얘기했다잖아요. 인성까지 글러 먹은 거지.”
216|
217|“나 참, 진짜 더러워서 못 해 먹겠네.”
218|
219|“아, 진짜 스트레스받으면 안 되는데. 머리 더 빠지는데.”
220|
221|물기 어린 목소리로 중얼거린 김준수가 정수리를 더듬었다. 모르긴 몰라도 잠깐 사이에 열 가닥은 빠진 것 같다.
222|
223|“녹취록이랑 소견서, 어떡해요?”
224|
225|“어떡하긴, 팀장 지랄하는 거 보기 싫으면 써야지. 병원 가서 진단 소견서 떼어 올래?”
226|
227|“…….”
228|
229|“대충 써, 대충. 패밀리어 마법 쓰느라 못 썼다고 옆에서 커버 쳐 줄 테니까.”
230|
231|한숨을 푹 내쉰 두 사람은 본격적으로 팀장을 욕하기 시작했다. 그 와중에도 송신기 너머에서는 대화가 이어졌다.
232|
233|- 괜찮네요. 남향이라 햇빛도 잘 들어오고. 그 옆 동은 어때요? 설마 여기도 나간 건 아니죠?
234|
235|- 응? 아냐. 요즘 경기가 안 좋아서 최근에 나간 곳은…… 그런데 총각.
236|
237|- 예?
238|
239|- 팔뚝 진짜 단단하다. 세상에, 이 근육이랑 핏줄 도드라진 것 좀 봐.
240|
241|- …….
242|
243|
244|
245|* * *
246|
247|
248|
249|“총각, 또 와. 두 번 와!”
250|
251|아줌마의 아쉬움 섞인 배웅을 뒤로하고 부동산을 나섰다. 방금 그녀의 손길이 스친 팔뚝에는 닭살이 오소소 돋아 있다.
252|
253|‘아줌마나 아저씨나, 철없이 나이 먹으면 젊은 애한테 치근덕거리는 건 비슷하다니까.’
254|
255|끈적끈적한 눈빛에 도망치듯 자리를 떴지만 이미 부동산을 찾은 목적은 달성한 후라 별 미련은 없었다.
256|
257|‘최근에 거래된 매물 확인.’
258|
259|오늘은 임창수와의 레이드로부터 정확히 5일째 되는 날이다.
260|
261|그 말인즉슨, 감시자들이 붙은 것은 아무리 빨라도 5일 안이라는 뜻이 된다.
262|
263|‘나름 연기랍시고 티 나지 않게 돌려서 묻긴 했는데…….’
264|
265|도청 마법의 존재를 아는 나로서는 다분히 의도적인 언행이었다. 허세와 사치로 똘똘 뭉친, 별거 없는 C급 헌터로 비치길 바랐으니까.
266|
267|‘속아 넘어갔을지는 미지수지만.’
268|
269|부동산 아줌마와의 대화는 중요한 단서였다. 나는 미리 외워 두었던 주소를 마음속으로 중얼거렸다.
270|
271|‘5동 901호. 4동 302호. 3동 202호.’
272|
273|이 세 곳이 최근 5일간 거래된 매물이다.
274|
275|기준은 우리 집. 패밀리어 마법이 닿는 범위인 최대 500m로 잡았다. 감시자들은 분명 이 안에 있다.
276|
277|‘문제는 어떻게 찾아내냐는 거지.’
278|
279|내 목적은 놈들을 쫓아내는 게 아니라, 잡아서 족친 후에 배후를 알아내는 거다. 섣부르게 헛다리 짚었다가는 도주할 가능성이 있다.
280|
281|‘자동차에 숨어 있을 가능성도 있으니까 주차장도 한번 살펴보고.’
282|
283|근방의 집을 뒤지기 시작하면 낌새를 눈치채겠지만 주차장은 자연스럽게 수색할 수 있다.
284|
285|산책하는 척 [기감]으로 훑어보면 게임 끝이지, 뭐.
286|
287|
288|
289|[Lv.42 김권동]
290|
291|
292|
293|“어, 또 만났네?”
294|
295|그래, 이 아저씨처럼.
296|
297|나는 알은체를 해 오는 김권동에게 인사를 건넸다.
298|
299|“그러게요. 또 뵙네요.”
300|
301|“부동산 가신다면서? 벌써 볼일 끝난 거야?”
302|
303|“그냥 문의만 했어요. 그런데 막상 가서 알아보니까 집값이 만만치가 않더라고요. 바로 도망쳐 나왔죠.”
304|
305|“이 동네가 다 그렇지, 뭐. 그래도 젊은 친구가 능력이 있네. 난 그 나이에 집에서 밥만 축냈는데.”
306|
307|“능력이요? 하하.”
308|
309|진짜 능력이 뭔지 알면 까무러칠걸.
310|
311|내 속마음도 모른 채 따라 웃던 김권동이 입을 열었다.
312|
313|“그럼 난 이만 갑니다. 저쪽 공원까지 돌고 와야 해서.”
314|
315|“산책을 좋아하시나 봐요?”
316|
317|“응? 그거야 좋아서 하는 게 아니라 필요해서 하는 거지. 그쪽도 내 나이 되면 힘들걸?”
318|
319|보란 듯이 얇은 팔다리를 흔들어 보인다. 겉모습만 보면 마르고 배만 나온 중년 아저씨가 따로 없다.
320|
321|‘민간인처럼 보이기는 하네.’
322|
323|다른 사람이면 깜빡 속아 넘어갔을 모습이다.
324|
325|하지만 42레벨이나 되는 민간인이 있을 리가 있나.
326|
327|‘아마도 C급 헌터. 체형으로 봐서는 은신, 추격 계열.’
328|
329|상대가 헌터라는 것만 알면 유추해 낼 수 있는 정보는 많다.
330|
331|나는 김권동에게 인사했다.
332|
333|“그럼 다음에 또 뵙죠.”
334|
335|“그거야 볼 수도 있고, 못 볼 수도 있고. 하하.”
336|
337|글쎄, 나는 꼭 보고 싶은데.
338|
339|물론 그때는 지금처럼 하하 호호 웃으면서 헤어지진 않을 거다. 지금 당장이라도 때려눕히고 싶지만, 아직은 때가 아니었다.
340|
341|꾸벅.
342|
343|살짝 고개 숙여 인사하고 자리를 뜨려는데 등 뒤에서 그의 목소리가 들렸다.
344|
345|“아, 맞다. 그 고양이 진짜 똑똑한 놈 같던데? 오는 길에 보니까 아직도 거기 있더라고.”
346|
347|패밀리어를 잊지 말고 주워 가라는 친절한 안내 방송까지 해 준다.
348|
349|그리고 그의 말처럼 고양이는 아까와 같은 곳에서 날 기다리고 있었다.
350|
351|야옹.
352|
353|그래. 형 왔다, 인마.
```

## Assembled English

```markdown
[P1]
# Chapter 97

[P2]
“Oh my, welcome!”

[P3]
An ajumma who looked to be in her forties greeted me in a nasal singsong.

[P4]
Maybe it was because the real-estate office was so close to home, but she looked vaguely familiar, like someone I’d passed once or twice on my way home.

[P5]
“A young man! What would you like to drink? Coffee? Yulmu tea?[^1] Cola?”

[P6]
“Coffee, please.”

[P7]
“Black, creamer, or…”

[P8]
“Black.”

[P9]
“Well, look at you. A young bachelor who knows how to drink his coffee.”

[P10]
I let her rapid-fire chatter go in one ear and out the other as I took a seat. There was something else I needed to pay more attention to than the talkative real-estate ajumma.

[P11]
*This is…*

[P12]
The familiar energy flowing through the real-estate office.

[P13]
Mana.

[P14]
*Eavesdropping magic?*

[P15]
There was almost no chance it was security magic installed by the owner. Who would put an expensive magic product in a real-estate office instead of their home?

[P16]
The people watching me had clearly made preparations in advance.

[P17]
*Well, I expected as much.*

[P18]
They were using Familiars, after all. Eavesdropping magic was nothing by comparison.

[P19]
The question was how many of them there were and where they were hiding…

[P20]
“Here you go. One coffee.”

[P21]
I accepted the cup with a polite smile.

[P22]
“Ah, thank you.”

[P23]
I meant it sincerely.

[P24]
After all, she was about to tell me where their base was.

[P25]
* * *

[P26]
—So, what brings our handsome boss here?

[P27]
—I’m looking for a place.

[P28]
The eavesdropping magic transmitted their voices with perfect clarity. Kim Junsu, who had briefly deactivated his Familiar magic, exchanged looks with another team member and the Security Team Leader.

[P29]
“Didn’t that bastard go to a real-estate office recently, too?”

[P30]
“Yes. He went to one in Goyang. That was before we were assigned to him, so the Team 1 Leader got the information from Hong Woojin and passed it on to us.”

[P31]
“Junsu’s right. We went to the real-estate office afterward and dug around a little. Apparently, he even put down a deposit.”

[P32]
“How much does he have in his account right now?”

[P33]
The Security Team already knew Jin Taekyung’s account balance inside and out.

[P34]
At the Security Team Leader’s question, a team member quickly pulled out a tablet and brought up the report.

[P35]
“About 3.7 billion won. Three billion of that will go toward buying the new house.”

[P36]
“Are you sure he’s going to buy it?”

[P37]
“We even heard that he’s planning to set a date with the owner and sign the contract soon, so he definitely intends to purchase it. We looked into it, and apparently it’s the neighborhood where the target lived as a child. It seems to have some special meaning to him.”

[P38]
“I see…”

[P39]
The Security Team Leader frowned.

[P40]
The man was about to pour most of his fortune into a new house. So why was he looking into another house in this neighborhood now?

[P41]
*His Guild is in Bucheon, too.*

[P42]
Whatever he was thinking, the whole thing left him feeling uneasy.

[P43]
“Hey, turn up the volume a little.”

[P44]
“Yes, sir.”

[P45]
The conversation continued to flow into the three men’s ears.

[P46]
—What kind of conditions are you looking for?

[P47]
—Either monthly rent or a jeonse lease.

[P48]
—I do have a few, but… as you know, this neighborhood straddles a safety zone, so it’s a little expensive.

[P49]
—That’s fine. I’m a Hunter.

[P50]
—Oh my, you’re a Hunter? No wonder you’re so fit. What rank are you? Ah, am I being nosy asking something like that?

[P51]
—Nothing special. It’s not very high. C-rank.

[P52]
—Oh my, oh my. You must make good money. Can I feel your arm? Oh-ho-ho!

[P53]
—Ha-ha. Show me some good listings and I’ll think about it. Actually, show me everything you’ve got. Jeonse, places for sale, all of it. If I find something I like, I’ll just buy it.

[P54]
The three men listening were dumbfounded.

[P55]
“That bastard’s having the time of his life.”

[P56]
“Can you blame him? He lived as an F-rank Hunter, then after his reawakening, big chunks of money started rolling in. Of course his ego’s through the roof.”

[P57]
“Hmm, true. That’s the age for it.”

[P58]
They all knew from experience. The feeling of stepping into a new world.

[P59]
Luxury goods that had once been too expensive even to look at suddenly seemed laughable, and people began looking at you differently.

[P60]
“That bastard’s right in the middle of it.”

[P61]
“‘If I find something I like, I’ll buy it,’ my ass. Once you pay the balance on the house you already contracted for, your account will barely cover a jeonse deposit, you idiot.”

[P62]
“Still, I’m jealous. What does he eat to have hair that thick?”

[P63]
Watching Jin Taekyung’s childish, cocky behavior was pathetic, but a quiet laugh escaped them anyway.

[P64]
Before they knew it, the three men had relaxed. Their ears were still open, but they felt as if they were listening to a radio broadcast.

[P65]
—How about this place? Around five hundred million won for a jeonse lease? Considering it’s in a safety zone, it’s listed well below market price.

[P66]
—Not bad. Are there any others?

[P67]
—Of course there are. There’s another listing two buildings over from the one I just showed you… Oh, this one was taken recently. It was monthly rent, but the terms were exceptionally good.

[P68]
—Oh, really?

[P69]
—Yeah. If you’d come a few days earlier, young man, you could’ve snagged it. The place wasn’t well maintained, but the rent was cheap. Of course, if you have money, remodeling can solve that problem.

[P70]
—That’s a shame.

[P71]
—I’m disappointed too. Some scary-looking man came by and spoke to me in this commanding tone. Did he think he’d left a house in my care or something? I’d much rather hand it over to a young, handsome bachelor, you know. Right?

[P72]
—Ugh, sounds like a total boomer.

[P73]
—I thought he might be a gangster, so I couldn’t so much as squeak. The smell of an old bachelor was practically pouring off him. I thought I was going to die. Ho-ho-ho.

[P74]
Grrrind.

[P75]
Teeth ground beside them. Kim Junsu and the other team member fought back the laughter threatening to burst out.

[P76]
*It’s the Team Leader.*

[P77]
*Definitely the Team Leader.*

[P78]
A gangster-like impression and the smell of an old bachelor. Just hearing that much was enough to identify the Security Team Leader.

[P79]
His expression was so frightening that there was even a rumor that when he first joined Sangdong Guild, the interviewer had been too scared to look any further and hired him on the spot.

[P80]
“Has that ajumma lost her mind…?”

[P81]
The Team Leader ground his teeth and whipped around. The other two men, red-faced from holding back their laughter, hurriedly lowered their heads.

[P82]
“You two look like you’re having a hard time holding it in.”

[P83]
“Oh, no, sir.”

[P84]
“Nothing of the sort, sir.”

[P85]
They tried desperately to deny it, but the Team Leader was already thoroughly offended. He rose from his seat.

[P86]
For a single man in his mid-forties, the words *old bachelor* touched on a subject that absolutely should not be touched.

[P87]
“I’m going to the sauna to wash off this old-bachelor smell, so have the transcript ready for me to read as soon as I get back.”

[P88]
“What?”

[P89]
Kim Junsu and the other team member were dumbfounded.

[P90]
A C-rank Hunter showing off at a real-estate office and a scatterbrained ajumma. Why would anyone write up a transcript of their completely unremarkable conversation?

[P91]
“Team Leader, it’s all being saved automatically…”

[P92]
“Prepare a full-page A4 statement of your individual opinions, too. He’s an important target, so we should gather the team’s input.”

[P93]
“…”

[P94]
“…”

[P95]
Since when had he ever asked for their opinions? And how could it make sense for the Team Leader to go to a sauna while they were dealing with such an important target?

[P96]
Their expressions twisted at the narrow-minded superior’s petty retaliation.

[P97]
“Didn’t you hear me? Repeat the order back. Execute!”

[P98]
“…Yes.”

[P99]
“…Execute.”

[P100]
“You bastards have gotten way too lax. You treat your Team Leader like dog shit.”

[P101]
The Security Team Leader glared at his subordinates, snorted angrily, and stormed out of the room.

[P102]
Bang!

[P103]
The apartment’s front door slammed shut. The two men left behind immediately spat out everything they had been holding in.

[P104]
“Man, fuck this.”

[P105]
“Isn’t this taking things way too far?”

[P106]
“Why is he taking it out on us because he has an ugly face and can’t get married?”

[P107]
“Is his face the only problem? That ajumma said he spoke in a commanding tone. His personality’s rotten, too.”

[P108]
“I’m so damn sick of this. I can’t keep doing this.”

[P109]
“Ah, I really can’t afford to get stressed out. It’ll make even more of my hair fall out.”

[P110]
Kim Junsu muttered in a voice thick with tears and felt the top of his head. He couldn’t be sure, but it seemed like at least ten hairs had fallen out in the last few moments.

[P111]
“What do we do about the transcript and the statements?”

[P112]
“What do you think? If you don’t want to watch the Team Leader throw a fit, you have to write them. Want to go to the hospital and get a medical statement?”

[P113]
“…”

[P114]
“Just slap something together. I’ll cover for you and say you couldn’t write yours because you were using Familiar magic.”

[P115]
After heaving deep sighs, the two men began cursing the Team Leader in earnest.

[P116]
All the while, the conversation continued through the transmitter.

[P117]
—It’s nice. It faces south, so it gets plenty of sunlight. What about the building next to it? Don’t tell me that one’s gone, too?

[P118]
—Huh? No, it’s still available. Business has been slow lately, so the places that went recently were… Wait, young man.

[P119]
—Yes?

[P120]
—Your arm is really firm. Goodness, just look at those muscles and veins.

[P121]
—…

[P122]
* * *

[P123]
“Young man, come again! Come twice!”

[P124]
I left the real-estate office with the ajumma’s regretful farewell behind me.

[P125]
Goose bumps had risen all over the arm her hand had just brushed.

[P126]
*Whether it’s an ajumma or an ajusshi, people who grow old without growing up are all alike when it comes to hitting on younger people.*

[P127]
I left as if fleeing her sticky gaze, but I had already accomplished what I’d gone there to do, so I had no regrets about leaving.

[P128]
*Confirm the listings that were recently sold or leased.*

[P129]
Today was exactly five days after the raid with Im Changsoo.

[P130]
In other words, the surveillance team couldn’t have been assigned to me more than five days ago.

[P131]
*I tried to act and ask about it indirectly without making it obvious, but…*

[P132]
Knowing that eavesdropping magic was in place, every word and action had been deliberate. I wanted to come across as an unremarkable C-rank Hunter packed full of arrogance and extravagance.

[P133]
*Whether they fell for it or not was another matter.*

[P134]
My conversation with the real-estate ajumma had given me an important clue. I silently muttered the addresses I had memorized in advance.

[P135]
*Building 5, Unit 901. Building 4, Unit 302. Building 3, Unit 202.*

[P136]
These were the three listings that had changed hands in the past five days.

[P137]
I had used our house as the center point and set the range at a maximum of five hundred meters—the distance Familiar magic could reach.

[P138]
The watchers were definitely somewhere within that range.

[P139]
*The problem is how to find them.*

[P140]
My goal wasn’t to drive them away. I wanted to catch them, beat the hell out of them, and find out who was behind them.

[P141]
If I went after the wrong place too soon, they might catch on and run.

[P142]
*They could be hiding in a car, so I should check the parking lot too.*

[P143]
Searching the nearby homes would tip them off, but I could search the parking lot without looking suspicious.

[P144]
All I had to do was pretend to take a walk while sweeping the area with Qi Sense.

[P145]
Game over.

[P146]
> **System**
>
> **Lv. 42 Kim Gwondong**

[P147]
“Oh, we meet again.”

[P148]
Just like this guy.

[P149]
I greeted Kim Gwondong when he called out to me.

[P150]
“Indeed. We meet again.”

[P151]
“You said you were going to the real-estate office. Finished already?”

[P152]
“I just asked a few questions. But when I actually went there and looked into it, the house prices weren’t exactly cheap. I ran right back out.”

[P153]
“That’s this neighborhood for you. Still, you’re doing well for yourself, young man. At your age, all I did was sit at home and eat my parents’ food.”

[P154]
“Doing well? Ha-ha.”

[P155]
If he knew what real ability looked like, he’d faint.

[P156]
Kim Gwondong laughed along, unaware of my thoughts, then spoke.

[P157]
“Well, I should get going. I need to walk to the park over there and back.”

[P158]
“You must like taking walks.”

[P159]
“Huh? It’s not that I do it because I like it. I do it because I need to. You’ll have a hard time too once you reach my age.”

[P160]
He conspicuously waved his thin arms and legs.

[P161]
To all appearances, he was just a scrawny, potbellied middle-aged man.

[P162]
*He certainly looks like a civilian.*

[P163]
Anyone else would have fallen for it completely.

[P164]
But there was no such thing as a Level 42 civilian.

[P165]
*Probably a C-rank Hunter. Judging by his build, he likely specializes in stealth and pursuit.*

[P166]
Once you knew someone was a Hunter, there was plenty you could infer.

[P167]
I said goodbye to Kim Gwondong.

[P168]
“Then I’ll see you next time.”

[P169]
“Maybe you will, maybe you won’t. Ha-ha.”

[P170]
Well, I definitely wanted to see him.

[P171]
Of course, when that happened, I wouldn’t be parting from him with a smile and a laugh like I was now. I wanted to knock him flat right then and there, but it wasn’t time yet.

[P172]
I gave him a slight bow and turned to leave when his voice came from behind me.

[P173]
“Oh, right. That cat seemed awfully smart. I saw it on my way over, and it was still there.”

[P174]
He had even given me a friendly reminder not to forget to pick up my Familiar.

[P175]
And just as he said, the cat was waiting for me in the same spot as before.

[P176]
“Meow.”

[P177]
Right. Hyung’s here, you punk.

[P178]
[^1]: Yulmu tea is a sweet Korean grain beverage made from roasted Job’s tears.
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
# Chapter 97

[P2]
“Oh my, welcome!”

[P3]
An ajumma who looked to be in her forties greeted me with a nasal sing-song.

[P4]
Maybe it was because this real-estate office was close to home. Her face looked vaguely familiar, as though I had passed her by on my way home once or twice.

[P5]
“Young man, what would you like to drink? Coffee? Yulmu tea?[^1] Cola?”

[P6]
“Coffee, please.”

[P7]
“Black, creamer, or…”

[P8]
“Black.”

[P9]
“Well, look at you. A young bachelor who knows how to drink coffee.”

[P10]
I let her rapid-fire chatter go in one ear and out the other as I took a seat. There was another place I needed to pay more attention to than the talkative real-estate ajumma.

[P11]
*This is…*

[P12]
The familiar energy flowing through the real-estate office.

[P13]
It was mana.

[P14]
*Wiretapping magic?*

[P15]
There was almost no chance it was security magic installed by the owner. Who would put an expensive magic product in a real-estate office instead of their home?

[P16]
The people watching me had clearly made preparations in advance.

[P17]
*Well, it was something I expected.*

[P18]
They were using Familiars, after all. Wiretapping magic was the least of it.

[P19]
The question was how many of them there were and where they were hiding…

[P20]
“Here you go. One coffee.”

[P21]
I accepted the cup with a polite smile.

[P22]
“Ah, thank you.”

[P23]
I meant that sincerely.

[P24]
She was about to tell me where their base was.

[P25]
* * *

[P26]
—So, what brings our handsome boss here?

[P27]
—I’m looking for a house.

[P28]
The voice transmitted by the eavesdropping magic was perfectly clear. Kim Junsu, who had briefly deactivated his Familiar magic, exchanged a look with another team member and the Security Team Leader.

[P29]
“Didn’t that bastard go to a real-estate office recently, too?”

[P30]
“Yes. He went to Goyang. At the time, we hadn’t been assigned to him yet, so the Team 1 Leader got the information from Hong Woojin and passed it along.”

[P31]
“Junsu’s right. We went to the real-estate office afterward and dug around a little. Apparently, he even put down a deposit.”

[P32]
“How much money does he have in his account right now?”

[P33]
The Security Team already knew Jin Taekyung’s account balance inside and out.

[P34]
At the Security Team Leader’s question, a team member quickly pulled out a tablet and brought up the report.

[P35]
“About 3.7 billion won. Three billion of that will go toward buying the new house.”

[P36]
“Are you sure he’s going to buy it?”

[P37]
“We even heard that he’s planning to set a date with the owner and sign the contract soon, so he definitely intends to purchase it. We looked into it, and apparently it’s the neighborhood where the target lived as a child. It seems to have some special meaning to him.”

[P38]
“I see…”

[P39]
The Security Team Leader frowned.

[P40]
The man was about to pour most of his fortune into a new house. So why was he looking into another house in this neighborhood now?

[P41]
*Even though his Guild is in Bucheon.*

[P42]
Whatever he was thinking, the whole thing left an unpleasant feeling in the Security Team Leader’s gut.

[P43]
“Hey, turn up the volume a little.”

[P44]
“Yes, sir.”

[P45]
The conversation continued to flow into the three men’s ears.

[P46]
—What kind of conditions are you looking for?

[P47]
—Either monthly rent or a jeonse lease.

[P48]
—I do have a few, but… as you know, this neighborhood straddles a safety zone, so it’s a little expensive.

[P49]
—That’s fine. I’m a Hunter.

[P50]
—Oh my, you’re a Hunter? I knew you looked fit. What rank are you? Ah, is it rude of me to ask something like that?

[P51]
—Somewhere around there. It’s not very high. C-rank.

[P52]
—Oh my, oh my. You must make good money. Can I feel that arm? Oh-ho-ho!

[P53]
—Ha-ha. Show me some good listings and I’ll think about it. No, show me everything. Jeonse, purchases, whatever. If I find something I like, I’ll just buy it.

[P54]
The three men listening were dumbfounded.

[P55]
“That bastard’s really enjoying himself.”

[P56]
“Can you blame him? He lived as an F-rank Hunter, then after his reawakening, big chunks of money started rolling in. Of course his ego would swell.”

[P57]
“Hmm, true. That’s the age for it.”

[P58]
They all knew from experience. The feeling of stepping into a new world.

[P59]
Luxury goods they had once been unable to look at because they were too expensive suddenly seemed laughable, and other people started looking at them differently.

[P60]
“That bastard’s exactly like that right now.”

[P61]
“‘If I find something I like, I’ll buy it,’ my ass. Once you pay the balance on the house you already contracted for, your account will barely cover a jeonse deposit, you idiot.”

[P62]
“Still, I’m jealous. What does he eat to have such thick hair?”

[P63]
Watching Jin Taekyung’s childish, cocky behavior was pathetic, but a quiet laugh escaped them anyway.

[P64]
Before they knew it, the three men had relaxed. Their ears were still open, but they felt as if they were listening to a radio broadcast.

[P65]
—How about this place? Around five hundred million won for a jeonse lease? Considering that it’s in a safety zone, it’s much cheaper than market price.

[P66]
—Not bad. Are there any others?

[P67]
—Of course there are. There’s another listing in the building two over from the one I just showed you… Oh, this one already went off the market. It was monthly rent, but the terms were exceptionally good.

[P68]
—Oh, really?

[P69]
—Yeah. If you’d come a few days earlier, young man, you could’ve snagged it. The place wasn’t well maintained, but the rent was cheap. Of course, if you have money, remodeling can solve that problem.

[P70]
—That’s a shame.

[P71]
—Tell me about it. Some scary-looking man came by and spoke to me in this commanding tone. Did he think I’d been entrusted with his house or something? I’d much rather hand it over to a young, handsome bachelor, you know. Right?

[P72]
—Ugh, I guess he was a total old-fashioned jerk.

[P73]
—I thought he might be a gangster, so I couldn’t so much as squeak. The smell of an old bachelor was practically pouring off him. I thought I was going to die. Ho-ho-ho.

[P74]
Grrrind.

[P75]
The sound of teeth grinding came from beside them. Kim Junsu and the other team member suppressed the laughter threatening to burst out.

[P76]
*It’s the Team Leader.*

[P77]
*It really is the Team Leader.*

[P78]
A gangster-like impression and the smell of an old bachelor. Just hearing that much was enough to identify the Security Team Leader.

[P79]
His expression was so frightening that there was even a rumor that when he first joined Sangdong Guild, the interviewer had been too scared to look any further and hired him on the spot.

[P80]
“Has that ajumma lost her mind…?”

[P81]
The Team Leader ground his teeth and whipped his head around. The two men, whose faces had flushed red from holding back their laughter, hurriedly lowered their heads.

[P82]
“You two look like you’re having a hard time holding it in.”

[P83]
“Oh, no, sir.”

[P84]
“There’s no such thing.”

[P85]
They tried desperately to deny it, but the Team Leader was already thoroughly offended. He stood up.

[P86]
For a single man in his mid-forties, the words *old bachelor* touched on a subject that absolutely should not be touched.

[P87]
“I’m going to the sauna to wash off this old-bachelor smell, so have the transcript ready for me to read as soon as I get back.”

[P88]
“What?”

[P89]
Kim Junsu and the other team member were dumbfounded.

[P90]
A C-rank Hunter showing off at a real-estate office and a scatterbrained ajumma. Why would anyone write up a transcript of their completely unremarkable conversation?

[P91]
“Team Leader, it’s all being saved automatically…”

[P92]
“Prepare a full-page A4 statement of your individual opinions, too. He’s an important target, so we should gather the team’s input.”

[P93]
“…”

[P94]
“…”

[P95]
Since when had he ever asked for their opinions? And how could it make sense for the Team Leader to go to a sauna while they were dealing with such an important target?

[P96]
Their expressions twisted at the narrow-minded superior’s petty retaliation.

[P97]
“Didn’t you hear me? Repeat the order back. Execute!”

[P98]
“…Yes.”

[P99]
“…Execute.”

[P100]
“You bastards have gotten way too lax. You treat your Team Leader like dog shit.”

[P101]
The Security Team Leader glared at his subordinates, snorted angrily, and left the room.

[P102]
Bang!

[P103]
The apartment’s front door slammed shut. The two men left behind immediately let out everything they had been holding in.

[P104]
“Man, fuck this.”

[P105]
“Isn’t this taking things way too far?”

[P106]
“Why is he taking out the fact that he has an ugly face and can’t get married on us?”

[P107]
“Is his face the only problem? That ajumma said he spoke in a commanding tone. His personality’s rotten, too.”

[P108]
“This is so damn unpleasant. I can’t keep doing this.”

[P109]
“Ah, I really can’t afford to get stressed out. It’ll make even more of my hair fall out.”

[P110]
Kim Junsu muttered in a voice thick with tears and felt the top of his head.

[P111]
He couldn’t be sure, but it seemed like at least ten hairs had fallen out in the last few moments.

[P112]
“Then what do we do about the transcript and the statements?”

[P113]
“What do you think? If you don’t want to watch the Team Leader throw a fit, you have to write them. Want to go to the hospital and get a medical statement?”

[P114]
“…”

[P115]
“Just write something rough. I’ll cover for you and say you couldn’t write because you were using Familiar magic.”

[P116]
After letting out a deep sigh, the two men began cursing the Team Leader in earnest.

[P117]
Even then, the conversation continued through the transmitter.

[P118]
—It’s nice. Since it faces south, it gets plenty of sunlight. What about the building next to it? Don’t tell me that one’s gone, too?

[P119]
—Huh? No, it’s still available. Business has been slow lately, so the places that went recently were… Wait, young man.

[P120]
—Yes?

[P121]
—That arm of yours is really solid. Goodness, look at those muscles and veins.

[P122]
—…

[P123]
* * *

[P124]
“Young man, come again. Come twice!”

[P125]
I left the real-estate office with the ajumma’s regretful farewell behind me.

[P126]
Goose bumps had risen all over the arm her hand had just brushed.

[P127]
*Whether it’s an ajumma or an ajusshi, people who grow old without growing up are all alike when it comes to hitting on younger people.*

[P128]
I had escaped as if fleeing from her sticky gaze, but I had already accomplished my purpose in visiting the real-estate office, so I had no reason to linger.

[P129]
*Confirm the listings that were recently sold or leased.*

[P130]
Today was exactly five days after the raid with Im Changsoo.

[P131]
That meant the surveillance team had been assigned to me no more than five days ago.

[P132]
*I tried to act and ask about it indirectly without making it obvious, but…*

[P133]
Knowing that eavesdropping magic was in place, I had deliberately behaved that way. I wanted to come across as an unremarkable C-rank Hunter packed full of arrogance and extravagance.

[P134]
*Whether they fell for it or not was another matter.*

[P135]
My conversation with the real-estate ajumma had given me an important clue. I repeated the addresses I had memorized in advance in my head.

[P136]
*Building 5, Unit 901. Building 4, Unit 302. Building 3, Unit 202.*

[P137]
These were the listings that had changed hands in the past five days.

[P138]
I had used our house as the center point and set the range at a maximum of five hundred meters—the distance Familiar magic could reach.

[P139]
The watchers were definitely somewhere within that range.

[P140]
*The problem is how to find them.*

[P141]
My goal wasn’t to drive them away. I wanted to catch them, beat the hell out of them, and find out who was behind them.

[P142]
If I jumped at the wrong lead, they might realize what was happening and run.

[P143]
*They could be hiding in a car, too, so I should check the parking lot.*

[P144]
If I started searching the nearby houses, they would notice something was wrong. But I could search the parking lot naturally.

[P145]
All I had to do was scan the area with Qi Sense while pretending to take a walk.

[P146]
Game over.

[P147]
> **System**
>
> **Lv. 42 Kim Gwondong**

[P148]
“Oh, we meet again.”

[P149]
Just like this man.

[P150]
I returned Kim Gwondong’s familiar greeting.

[P151]
“Indeed. We meet again.”

[P152]
“You said you were going to the real-estate office. Are you done already?”

[P153]
“I just asked a few questions. But when I actually went there and looked into it, the house prices weren’t exactly cheap. I ran right back out.”

[P154]
“That’s how this neighborhood is. Still, you’re doing well for yourself, young man. At your age, I was just sitting at home eating my parents’ food.”

[P155]
“Doing well? Ha-ha.”

[P156]
If he knew what real ability looked like, he’d faint.

[P157]
Kim Gwondong laughed along, unaware of my thoughts, then spoke.

[P158]
“Well, I should be going. I need to walk as far as the park over there.”

[P159]
“You must like taking walks.”

[P160]
“Huh? It’s not that I do it because I like it. I do it because I need to. You’ll have a hard time too once you reach my age.”

[P161]
He deliberately waved his thin arms and legs.

[P162]
From the outside, he looked exactly like an ordinary middle-aged man who was skinny everywhere except for his protruding belly.

[P163]
*He certainly looks like a civilian.*

[P164]
Anyone else would have been fooled.

[P165]
But there was no way a civilian could be Level 42.

[P166]
*Probably a C-rank Hunter. Judging by his build, he’s probably specialized in stealth and pursuit.*

[P167]
Once you knew someone was a Hunter, there was a lot you could infer.

[P168]
I said goodbye to Kim Gwondong.

[P169]
“Then I’ll see you next time.”

[P170]
“That depends. We might run into each other, or we might not. Ha-ha.”

[P171]
Well, I definitely wanted to see him.

[P172]
Of course, when that happened, I wouldn’t be parting from him with a smile and a laugh like I was now. I wanted to knock him flat right then and there, but it wasn’t time yet.

[P173]
I gave him a slight bow and turned to leave.

[P174]
“Oh, right. That cat seemed awfully smart. I saw it on my way over, and it was still there.”

[P175]
He had even given me a friendly reminder not to forget to pick up my Familiar.

[P176]
And just as he said, the cat was waiting for me in the same spot as before.

[P177]
“Meow.”

[P178]
Right. Hyung’s here, you punk.

[P179]
[^1]: Yulmu tea is a sweet Korean grain beverage made from roasted Job’s tears.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 진태경    | **Jin Taekyung**   |
| 임창수    | **Im Changsoo**   |
| 홍우진    | **Hong Woojin**   |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 꼰대 | **boomer** | Modern slang for a hidebound older person; used by Cheongpung. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 97,
  "passed": true,
  "metrics": {
    "source_characters": 5791,
    "translation_characters": 13439,
    "length_ratio": 2.321,
    "source_paragraphs": 170,
    "translation_paragraphs": 178
  },
  "errors": [],
  "warnings": [
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
        "korean": "등급",
        "preferred": "Grade"
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
        "korean": "세가",
        "preferred": "great family"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "호호호",
        "romanization": "hohoho"
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
