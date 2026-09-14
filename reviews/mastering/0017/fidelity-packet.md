# Fidelity Gate — Chapter 17

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
  1|＃17화
  2|
  3|
  4|
  5|운기조식.
  6|
  7|숨을 고르게 하여 기운을 다스리는 방법이다. 외부의 기를 내부로 받아들여 순환, 축적하는 행위.
  8|
  9|지금 나는 진가심법이 적용된 운기조식을 하고 있었다.
 10|
 11|‘이건 매번 신기하단 말이야.’
 12|
 13|몰랐다. 내 몸에 이렇게 많은 혈이 존재하는지.
 14|
 15|일전에 주워듣기로 인체의 혈도는 360여 개에 달한다고 했는데, 직접 심법을 운용하며 느낀 바로는 그 이상이다.
 16|
 17|게임 속 가상 캐릭터라 그런가?
 18|
 19|‘뭐 어때.’
 20|
 21|단전에서 끌어 올린 10년의 공력이 신체를 순환한다. 공력이 자동차라면 혈도는 고속도로다. 나는 운전대에 앉아 그저 액셀을 밟으면 된다.
 22|
 23|직선과 곡선이 반복되는 신체의 혈도를 달린 공력은 다시 단전으로 돌아간다.
 24|
 25|‘그리고 여기서부터가 진짜 문제지.’
 26|
 27|나는 길게 심호흡했다. 그리고 느꼈다.
 28|
 29|내 의지에도 꿈쩍하지 않는, 거대한 바위처럼 단전을 차지하고 있는 또 다른 공력을.
 30|
 31|‘넌 도대체 뭐냐.’
 32|
 33|처음 운기조식을 했을 때부터 의문이었다. 터줏대감처럼 자리 잡고 있는 정체불명의 기운.
 34|
 35|어디서, 어떻게 생겼고 왜 사용할 수 없는지는 모르겠지만 한 가지는 확실하다. 이 정체불명의 기운은, 내가 가진 10년의 공력보다도 더 큰 힘을 품고 있다.
 36|
 37|‘지금까지는 건드릴 엄두가 안 났었지.’
 38|
 39|정확히 말하면 건드릴 생각도 없었다. 며칠 전까지는 적당히 목숨 부지하면서 내심 구조를 기다리는 입장이었으니까.
 40|
 41|하지만 이제는 다르다.
 42|
 43|‘공력이 필요해.’
 44|
 45|상황이 바뀌었다. 자력으로 탈출하려면 로그아웃 퀘스트 조건을 충족시켜야 하고, 충족 조건은 [일류]의 경지에 오르는 것.
 46|
 47|그리고 일류가 되기 위해서는 이소군 정도의 공력이 필요하다는 것도 알았다.
 48|
 49|‘내 것으로 만든다.’
 50|
 51|나는 신중하게 공력을 움직이기 시작했다.
 52|
 53|불안 반, 기대 반의 마음으로 정체불명의 기운을 향해 공력을 흘려보낸 순간, 깨달았다.
 54|
 55|‘턱도 없네.’
 56|
 57|공력은 엄연히 말해서 형체가 없는 기(氣), 그 자체다. 그런데 단순히 접촉하는 것만으로도 강한 거부와 반발이 느껴진다.
 58|
 59|아니, 오히려 끌어당기기까지 한다. 이러다간 오히려 잡아먹힐 기세다.
 60|
 61|‘야, 야, 야. 잠깐만!’
 62|
 63|나는 황급히 공력을 회수했다. 끝까지 물고 늘어지는 정체불명의 기운을 뿌리쳤다. 동시에 시스템 알림이 울렸다.
 64|
 65|띠링.
 66|
 67|
 68|
 69|- [진가심법]을 수련했습니다. 공력이 소량 상승합니다.
 70|
 71|- 반복 수련의 결과로 근맥과 근골이 1씩 상승합니다.
 72|
 73|
 74|
 75|“아니, 뭐 저딴 게 다 있어?”
 76|
 77|식겁한 마음을 진정시키며 상태창을 열었다.
 78|
 79|
 80|
 81|상태창
 82|
 83|
 84|
 85|[Lv.17 진태경]
 86|
 87|직업 : 이류 무인
 88|
 89|명성 : 70
 90|
 91|칭호 : 4개 (칭호 효과 적용 중)
 92|
 93|- 명가의 자제 (모든 능력치 +5, 명성 +50)
 94|
 95|- 가문의 수치 (모든 능력치 –5, 명성 –50)
 96|
 97|- 초보 수련자 (수련 속도 +10%)
 98|
 99|- 승부사 (일대일 승부 시 전투 관련 능력치 10% 향상)
100|
101|근력 : 65체력 : 65
102|
103|민첩 : 75 지력 : 10
104|
105|매력 : 10 공력 : 10년
106|
107|잔여 포인트 : 0
108|
109|
110|
111|
112|
113|이제는 제법 높은 수치를 기록하고 있는 상태창이다.
114|
115|비무 퀘스트를 통해 한꺼번에 3레벨이 올랐고, 30포인트를 근력, 체력, 민첩에 균등 분배한 결과였다.
116|
117|하지만 상태창을 보는 내 마음은 쓰라렸다.
118|
119|‘에휴, 공력만 제자리걸음이네.’
120|
121|이 빌어먹을 시스템은 말만 공력이 상승했다고 하지, 정작 상태창에 표시되는 공력은 그대로다.
122|
123|‘영단, 영약. 뭐 이런 거라도 하나 먹어야 되나?’
124|
125|나는 진위경을 떠올렸다. 눈 딱 감고 형, 나 영단 하나만 주라, 하면 단칼에 거절하진 않을 것 같은데.
126|
127|다음에 만나면 물어봐야겠다. 내 단전에 존재하는 정체불명의 기운에 관해서도.
128|
129|쿠구궁.
130|
131|그때 수련동의 입구가 열리더니 두 사람이 들어왔다.
132|
133|“저어, 진 공자님?”
134|
135|한엽이다. 그 뒤에는 처음 보는 무사가 서 있었다. 생긴 것만큼이나 무뚝뚝한 말투로 무사가 말했다.
136|
137|“가로회의에 참석하시라는 소가주님의 명입니다.”
138|
139|“소가주님이요?”
140|
141|마침 잘됐네. 물어볼 거 있었는데.
142|
143|
144|
145|* * *
146|
147|
148|
149|“틀림없소. 몇 군데 부러지고 약간의 내상이 있었지만 그 정도로는 절대…….”
150|
151|“확실해? 약왕당주의 이름을 걸고?”
152|
153|“아, 맞다고. 내가 직접 진찰했다고!”
154|
155|“맞으면 됐지. 왜 반말이야. 어? 같은 당주라고 대접해 주니까 내가 우스워 보여!”
156|
157|“백호당주 당신이 먼저 반말했잖아!”
158|
159|나는 멍하니 회의실 천장을 바라봤다. 사방에서 난무하는 고함과 욕설에 귀가 따끔거린다.
160|
161|‘뭐여, 이게.’
162|
163|내가 생각한 가로회의는 이런 게 아니었는데. 조용하고 질서정연한 분위기에서 서로의 의견을 주고받고 합의점을 찾는, 뭐 그런 거였는데…….
164|
165|“당주라고 다 같은 당주인 줄 알아! 어디 의원 나부랭이가.”
166|
167|“어린 노무 새끼가 말하는 본새 보소. 대침으로 회음혈을 쑤셔 버릴라.”
168|
169|M자 탈모가 진행 중인 4, 50대 아저씨 두 명이 서로의 멱살을 잡고 흔드는 모습을 보니 골이 다 아파 온다.
170|
171|문제는 이런 상황이 곳곳에서 벌어지고 있다는 사실이다.
172|
173|그 때문인지는 몰라도 대부분의 사람들은 내가 문을 열고 들어와 자리에 앉은 것도 모르는 눈치였다.
174|
175|- 왔느냐?
176|
177|귀가 아니라 머리를 통해 들리는 듯한 목소리. 전음이다.
178|
179|고개를 돌리자 상석의 진위경과 시선이 마주쳤다. 그는 피곤한 웃음을 지어 보였다.
180|
181|- 난장판이지?
182|
183|그러게. 이 난장판에 날 왜 불러 이 양반아.
184|
185|내가 비난의 시선을 보내자 진위경이 찔리는 듯한 표정으로 전음을 날렸다.
186|
187|- 나도 어쩔 수 없었다. 장로원에서 네 출석을 요구했거든. 어찌 되었건…… 태경이 네가 이 일에 연관된 것은 사실이니까.
188|
189|장로원? 내가 이 일에 연관되어 있다고?
190|
191|‘내가 무슨 일에 연관…… 아. 항산검문?’
192|
193|나는 사람들의 고성방가 속에서 빠르게 퍼즐을 조합했다.
194|
195|우선 최근에 나와 연관된 일이라면 항산검문밖에 없고, 그 일로 장로원인가 뭔가 하는 곳에서 나를 불러오게 했다. 이건데.
196|
197|‘그러고 보니 못 보던 할아버지들이 있네.’
198|
199|숫자는 네 명. 하나같이 검버섯이 가득한 얼굴에 머리가 하얗게 셌다.
200|
201|그들은 탈모인들의 멱살잡이를 차가운 눈으로 바라보고 있었다. 누가 봐도 양로원, 아니 장로원이다.
202|
203|- 그리고…… 대장로께서 와 계신다.
204|
205|무심코 진위경 쪽으로 고개를 돌린 나는 흠칫했다.
206|
207|‘뭐야. 저 노인네.’
208|
209|언제부터 저기 있었지? 이제야 알아차렸지만 오늘의 상석은 두 자리였다. 진위경의 오른편에 앉아 나를 응시하고 있는 노인의 시선에 얼굴이 따끔거렸다.
210|
211|‘저 노인이 대장로?’
212|
213|백발, 백염, 백미. 오래된 그림에서 튀어나온 신선 같은 모습이다. 꼿꼿한 허리와 딱 벌어진 어깨, 팽팽한 피부는 나이가 무색해 보였다.
214|
215|‘그런데 왜 저렇게 빤히 쳐다봐?’
216|
217|눈에 힘을 빡 주고 대장로를 노려……보려다가 슬그머니 시선을 돌렸다. 붙으면 질 것 같아서가 아니라, 노인 공경이다. 노인 공경. 정말이다.
218|
219|‘……쭈그리고 있자.’
220|
221|그사이에도 진위경의 전음은 꾸준히 들려왔다.
222|
223|- 기억을 잃어서 모르겠지만 대장로께서는 네 작은할아버님이자 가문의 최고 어르신이다. 언행에 각별히 신경 쓰거라.
224|
225|아버지라는 양반 얼굴도 못 봤는데 작은할아버지란다.
226|
227|어쩌면 이 자리에 사돈에 팔촌, 오촌 당숙까지 있을지도 모르겠다. 나는 진위경에게 살짝 고개를 끄덕여 보였다.
228|
229|- 그리고…… 지금부터 벌어지는 일에 결코 당황해서는 안 된다. 차분하게 진실만을 고해라. 알겠느냐?
230|
231|정확히 무슨 상황인지는 모르겠지만 진위경이 내 편이라는 사실은 확실했다. 이번에도 작게 고개를 끄덕이자 진위경이 희미한 미소를 지으며 일어났다.
232|
233|“모두 정숙하십시오.”
234|
235|공력이 담긴 목소리가 회의장을 휩쓸었다.
236|
237|“이 자리는 태원진가의 가로회의이며, 우리는 중대한 사안을 위해 모였습니다. 때마침 증인이 도착했으니 심문을 시작하고자 합니다.”
238|
239|어느새 조용해진 회의장의 중심. 사람들의 이목이 집중된 가운데 진위경이 입을 열었다.
240|
241|“소가주이자 현 가주 대행의 권한으로 심문을 시작한다. 삼공자 진태경은 앞으로 나서라.”
242|
243|나는 사람들의 시선을 느끼며 걸어 나왔다. 여기까진 충분히 예상했다. 괜히 나를 부르진 않았을 테니까.
244|
245|하지만…….
246|
247|“묻겠다. 네가 항산검문의 이소군을 독살했느냐?”
248|
249|이건 예상 못 했다.
250|
251|
252|
253|* * *
254|
255|
256|
257|“아닙니다.”
258|
259|간신히 입을 뗐다. 갑작스러운 말에 머릿속이 뒤죽박죽이다.
260|
261|이소군이 죽었다고? 그것도 독에 중독돼서?
262|
263|“진실을 고하라. 만일 거짓으로 밝혀진다면…….”
264|
265|“이소군의 독살은 저와 아무런 연관이 없습니다.”
266|
267|칼 같은 내 대답에 진위경은 안도 섞인 한숨을 내쉬었다.
268|
269|- 지금처럼만 하면 된다.
270|
271|심문은 빠르게 진행되었다. 그들은 묻고, 나는 답한다.
272|
273|진위경을 시작으로 차례차례 질문이 쏟아졌다.
274|
275|이소군과의 독살에 연관되어 있느냐는 질문이 절반이었고, 나는 계속해서 부정했다.
276|
277|‘사실이니까.’
278|
279|혹시나 해서 몰래 시스템창을 띄워 확인해 봤지만 확실했다. 내가 가진 무공, 능력들은 독과는 아무 관련이 없다. 그런 아이템도 없고.
280|
281|그래서 망설임 없이 대답할 수 있었다.
282|
283|“아닙니다.”
284|
285|문제는 어느 순간부터 회의장 분위기가 묘하게 흘러가고 있다는 사실이었다.
286|
287|“혹시 입증할 수 있는 증거가 있소?”
288|
289|“증거요?”
290|
291|백호당주라고 했나? 이름도 모르는 그는 썩 달갑지 않은 눈초리로 나를 응시했다.
292|
293|“그렇소. 증거. 삼공자의 무죄를 입증할 만한 증거 말이오.”
294|
295|이 새끼가 지금 뭐라는 거야.
296|
297|“그걸 왜 내가 입증해야 하는데요?”
298|
299|“뭐?”
300|
301|“뭐는 반말이고.”
302|
303|“이보시오. 삼공자!”
304|
305|“날 의심하는 건 좋은데, 증거는 그쪽에서 찾아야 하는 거 아닌가? 예? 안 그래요?”
306|
307|이 새끼들이 보자 보자 하니까 누굴 보자기로 보나. 나는 씨근덕거리며 자리에 앉는 백호당주를 노려보다가 문득 이상한 점을 발견했다.
308|
309|‘허. 이것 봐라.’
310|
311|흘끗 장로원 노인네들에게 시선을 보내는 백호당주의 모습.
312|
313|공교로운 사실은 나를 추궁하고 압박하는 질문을 하는 이들 모두가 비슷한 모습을 보이고 있다는 것이다.
314|
315|그 숫자가 참석 인원의 절반 가까이 되니 모른 척하기가 미안할 지경이었다.
316|
317|‘파벌이라 이거지.’
318|
319|진위경과 장로원.
320|
321|한 집안의 웃어른과 그 손자뻘 되는 소가주의 힘 싸움이 이 순간에도 벌어지고 있었다니.
322|
323|‘집안 꼴 잘 돌아간다.’
324|
325|이제 남은 이들은 몇 되지 않았다. 문제는 그들의 면면이었다. 검버섯 핀 얼굴. 노회한 눈빛. 바로 장로원의 노인네들이었다.
326|
327|그중 가장 늙고 뚱뚱한 노인이 입을 열었다.
328|
329|“실속 없는 문답은 집어치우지. 이 늙은이가 말하고 싶은 건 단 하나일세. 이 문제는 어디서부터 비롯되었는가?”
330|
331|장로원에 동조하는 중진들이 기다렸다는 듯이 대답했다.
332|
333|“삼공자입니다.”
334|
335|“문란한 언행으로 본가의 명성에 먹칠을 하고 다닌 것은 누구인가?”
336|
337|“그 또한 삼공자입니다.”
338|
339|같은 대답이 여기저기서 튀어나왔다.
340|
341|“하면, 항산검문의 장중보옥을 건드려 작금의 사태에 이르게 한 것은 누구인가?”
342|
343|“…….”
344|
345|그냥 죽여라, 이 새끼들아.
```

## Assembled English

```markdown
[P1]
# Chapter 17

[P2]
Circulating qi.

[P3]
It was a method of regulating one’s energy by steadying one’s breathing—drawing qi from outside the body, circulating it within, and accumulating it.

[P4]
Right now, I was circulating qi using the Jin Family’s Cultivation Technique.

[P5]
*This still feels incredible every time.*

[P6]
I had never realized there were so many acupoints in my body.

[P7]
I had once heard that the human body contained more than three hundred and sixty acupoints, but based on what I could feel while using the cultivation technique, there were even more than that.

[P8]
*Is it because I’m a virtual game character?*

[P9]
*Whatever.*

[P10]
The ten years of internal energy I drew up from my dantian circulated through my body. If internal energy was a car, then the meridians were a highway. All I had to do was sit behind the wheel and press the accelerator.

[P11]
The internal energy raced along the straight and curving meridians throughout my body before returning to my dantian.

[P12]
*And this is where the real problem starts.*

[P13]
I took a long, deep breath. Then I felt it.

[P14]
Another internal energy occupied my dantian like an enormous boulder that refused to budge, no matter how hard I willed it to.

[P15]
*What the hell are you?*

[P16]
It had been a mystery ever since I first circulated my qi—an unidentified energy entrenched there as if it owned the place.

[P17]
I didn’t know where it had come from, how it had formed, or why I couldn’t use it, but one thing was certain. This unidentified energy contained even more power than my ten years of internal energy.

[P18]
*Until now, I hadn’t even dared touch it.*

[P19]
To be more precise, I hadn’t intended to. Until a few days ago, I had been waiting for rescue while doing just enough to stay alive.

[P20]
But things were different now.

[P21]
*I need more internal energy.*

[P22]
The situation had changed. If I wanted to escape on my own, I had to fulfill the Logout Quest’s condition: reaching the First Rate realm.

[P23]
I also knew that I needed internal energy on the level of Lee Seogeun’s to become First Rate.

[P24]
*I’ll make it mine.*

[P25]
I cautiously began moving my internal energy.

[P26]
The moment I sent it toward the unidentified energy, half anxious and half hopeful, I realized something.

[P27]
*Not even close.*

[P28]
Internal energy was, strictly speaking, qi itself—something without physical form. Yet the instant the two energies touched, I felt a powerful rejection and resistance.

[P29]
No. It was even pulling my internal energy toward it. At this rate, my energy would be devoured instead.

[P30]
*Hey, hey, hey! Wait a second!*

[P31]
I hurriedly pulled my internal energy back and shook off the unidentified energy as it clung on to the bitter end. At the same time, a System notification rang out.

[P32]
Ding.

[P33]
> **System**
>
> - You have trained the **Jin Family’s Cultivation Technique**. Internal energy has risen slightly.
>
> - As a result of repeated training, **Sinews** and **Bones** have each increased by 1.

[P34]
“What the hell was that?”

[P35]
I calmed my pounding heart and opened my Status Window.

[P36]
> **Status Window**
>
> **Lv. 17 Jin Taekyung**
>
> **Class:** Second Rate martial artist  
> **Fame:** 70  
> **Titles:** 4 (Title effects active)
>
> - **Scion of a Prestigious Family** — All stats +5, Fame +50
> - **Family’s Shame** — All stats –5, Fame –50
> - **Novice Trainee** — Training speed +10%
> - **Gambler** — Combat-related stats +10% in one-on-one matches
>
> **Strength:** 65  **Stamina:** 65  
> **Agility:** 75  **Intelligence:** 10  
> **Charm:** 10  **Internal Energy:** 10 years
>
> **Remaining Points:** 0

[P37]
The numbers in my Status Window were fairly impressive by now.

[P38]
I had gained three levels all at once through the Duel Quest, then distributed the thirty points equally among Strength, Stamina, and Agility.

[P39]
But looking at the Status Window still left a bitter taste in my mouth.

[P40]
*My internal energy is the only thing that hasn’t changed.*

[P41]
This damn System kept saying that my internal energy had risen, but the amount displayed in the Status Window remained exactly the same.

[P42]
*Do I need to take a spirit pill or an elixir or something?*

[P43]
I thought of Jin Wikyung. If I screwed up my courage and said, *Big brother, just give me one spirit pill,* I didn’t think he would refuse me outright.

[P44]
I’d ask him the next time I saw him. I would also ask about the unidentified energy inside my dantian.

[P45]
Krrrummble.

[P46]
At that moment, the entrance to the training hall opened, and two people stepped inside.

[P47]
“Um, Young Master Jin?”

[P48]
It was Han Yeop. Behind him stood a martial artist I had never seen before. The man spoke in a blunt tone that matched his appearance.

[P49]
“The Lesser Family Head commands you to attend the family council.”

[P50]
“The Lesser Family Head?”

[P51]
Perfect timing. There was something I wanted to ask him.

[P52]
* * *

[P53]
“It is beyond doubt. A few bones were broken, and there was some minor internal damage, but injuries like that could never…”

[P54]
“Are you sure? Will you swear on your name as the Medicine King Hall Leader?”

[P55]
“I said it’s true! I examined him myself!”

[P56]
“Then that settles it. Why are you talking down to me? Huh? I treat you with respect because you’re another Hall Leader, and now you think I’m a joke?”

[P57]
“You were the one who started talking down to me, White Tiger Hall Leader!”

[P58]
I stared blankly at the ceiling of the meeting room. The shouts and curses flying from every direction made my ears ring.

[P59]
*What the hell is this?*

[P60]
This wasn’t what I had imagined a family council would be like. I had pictured a quiet, orderly atmosphere where everyone exchanged opinions and searched for common ground…

[P61]
“You think all Hall Leaders are equal? You’re nothing but a mere physician!”

[P62]
“Listen to this young bastard. I ought to ram a great big needle into your perineal acupoint.”

[P63]
Two men in their forties or fifties, both with receding M-shaped hairlines, were grabbing each other by the collars and shaking one another. Just watching them made my head hurt.

[P64]
The problem was that scenes like this were unfolding all over the room.

[P65]
Maybe that was why most of the people there didn’t seem to notice me open the door and take my seat.

[P66]
—You’re here?

[P67]
The voice seemed to enter through my head rather than my ears.

[P68]
Sound Transmission.

[P69]
I turned and met Jin Wikyung’s gaze from the seat of honor. He gave me a weary smile.

[P70]
—It’s a madhouse, isn’t it?

[P71]
*Exactly. So why did you call me into this madhouse?*

[P72]
I shot him a reproachful look. Looking sheepish, Jin Wikyung sent another Sound Transmission.

[P73]
—I had no choice. The Elder Council demanded your attendance. In any case… you are involved in this matter.

[P74]
*The Elder Council? I’m involved in this matter?*

[P75]
*What matter am I involved in…? Oh. The Mount Heng Sword Sect?*

[P76]
I quickly pieced things together amid the shouting and cursing.

[P77]
The only recent incident involving me was the one with the Mount Heng Sword Sect. And because of that incident, the Elder Council or whatever had summoned me.

[P78]
That had to be it.

[P79]
*Come to think of it, there are some old men here I’ve never seen before.*

[P80]
There were four of them. Every one had a face covered in age spots and hair that had gone completely white.

[P81]
They watched the men with the M-shaped hairlines grab each other by the collars with cold eyes. Anyone could see it was a nursing home—or rather, the Elder Council.

[P82]
—And… the Head Elder is here.

[P83]
I turned toward Jin Wikyung without thinking, then flinched.

[P84]
*What the hell? That old man… How long had he been sitting there?*

[P85]
I had only just noticed that there were two seats of honor today. An old man was sitting to Jin Wikyung’s right, staring at me. His gaze made my face prickle.

[P86]
*Is that old man the Head Elder?*

[P87]
White hair, a white beard, and white eyebrows. He looked like an immortal who had stepped out of an old painting. His straight back, broad shoulders, and taut skin seemed to defy his age.

[P88]
*But why is he staring at me so intently?*

[P89]
I put some force into my gaze and tried to glare back at the Head Elder…

[P90]
Then I quietly looked away.

[P91]
Not because I thought I would lose if we fought. It was respect for my elders. Respect for my elders. Really.

[P92]
*I’ll just keep my head down.*

[P93]
Jin Wikyung’s Sound Transmission continued in the meantime.

[P94]
—You may not know this because you lost your memory, but the Head Elder is your great-uncle and the most senior elder in the family. Be especially careful with your words and actions.

[P95]
I hadn’t even seen my father’s face, and now I had a great-uncle.

[P96]
*Maybe there were in-laws, eighth-degree relatives, and even one of my father’s cousins somewhere in this room.*

[P97]
I gave Jin Wikyung a small nod.

[P98]
—And… you must not be flustered by what happens from this point onward. Calmly tell them only the truth. Do you understand?

[P99]
I didn’t know exactly what was going on, but one thing was certain: Jin Wikyung was on my side.

[P100]
I nodded again, and Jin Wikyung rose with a faint smile.

[P101]
“Silence, everyone.”

[P102]
His voice, infused with internal energy, swept across the meeting hall.

[P103]
“This is a family council of the Jin Family of Taiyuan, and we have gathered to discuss a grave matter. Since the witness has arrived, I intend to begin the interrogation.”

[P104]
The meeting hall had fallen silent before I knew it. With everyone’s attention fixed on him, Jin Wikyung spoke.

[P105]
“By the authority of the Lesser Family Head and current acting Family Head, I begin this interrogation. Third Young Master Jin Taekyung, step forward.”

[P106]
I felt everyone’s eyes on me as I walked forward. I had expected this much. They hadn’t summoned me for no reason.

[P107]
But…

[P108]
“I ask you this. Did you poison Lee Seogeun of the Mount Heng Sword Sect?”

[P109]
That was something I hadn’t expected.

[P110]
* * *

[P111]
“No.”

[P112]
I barely managed to get the word out. My thoughts were a mess from the sudden question.

[P113]
*Lee Seogeun was dead? Poisoned, at that?*

[P114]
“Tell us the truth. If your words are proven false…”

[P115]
“I had nothing to do with poisoning Lee Seogeun.”

[P116]
My answer was as sharp as a blade. Jin Wikyung let out a sigh tinged with relief.

[P117]
—Keep doing exactly this.

[P118]
The interrogation proceeded quickly. They asked questions, and I answered.

[P119]
Starting with Jin Wikyung, they fired one question after another at me.

[P120]
About half of the questions concerned whether I had been involved in poisoning Lee Seogeun, and I continued to deny it.

[P121]
*Because it was true.*

[P122]
Just in case, I secretly opened my System Window and checked. I was certain. None of my martial arts or abilities had anything to do with poison. I didn’t have any such Items, either.

[P123]
That was why I could answer without hesitation.

[P124]
“No.”

[P125]
The problem was that, at some point, the atmosphere in the meeting hall began to take a strange turn.

[P126]
“Do you have any evidence to prove it?”

[P127]
“Evidence?”

[P128]
White Tiger Hall Leader, was it? The man whose name I didn’t even know stared at me with obvious displeasure.

[P129]
“That is correct. Evidence. I mean evidence that would prove the Third Young Master’s innocence.”

[P130]
*What the hell is this bastard talking about?*

[P131]
“Why do I have to prove it?”

[P132]
“What?”

[P133]
“Don’t ‘what’ me.”

[P134]
“Listen here, Third Young Master!”

[P135]
“You’re free to suspect me, but shouldn’t you be the ones looking for evidence? Am I wrong?”

[P136]
I’d let this go on long enough. Did these bastards think I was some damn wrapping cloth?[^1]

[P137]
Fuming, I glared at the White Tiger Hall Leader as he sat down, then noticed something strange.

[P138]
*Well, well. Look at this.*

[P139]
The White Tiger Hall Leader kept stealing glances at the old men of the Elder Council.

[P140]
The strange thing was that everyone who had been pressing and interrogating me was doing something similar.

[P141]
Nearly half the people in attendance were acting this way. It was getting difficult to pretend I hadn’t noticed.

[P142]
*So this is a factional struggle.*

[P143]
Jin Wikyung and the Elder Council.

[P144]
Even now, a power struggle was taking place between the senior members of the family and the Lesser Family Head who was young enough to be their grandson.

[P145]
*What a family.*

[P146]
Only a few people remained to question me. The problem was who those people were.

[P147]
Faces covered in age spots. Canny, experienced eyes.

[P148]
The old men of the Elder Council.

[P149]
The oldest and fattest of them opened his mouth.

[P150]
“Enough of this empty questioning. There is only one thing this old man wishes to ask. Where did this matter begin?”

[P151]
The senior members allied with the Elder Council answered as if they had been waiting for the question.

[P152]
“The Third Young Master.”

[P153]
“Who was it that dragged our family’s reputation through the mud with disorderly words and conduct?”

[P154]
“The Third Young Master.”

[P155]
The same answer came from several places around the room.

[P156]
“Then who was it that laid hands on the Mount Heng Sword Sect’s treasured jewel and brought about the present crisis?”

[P157]
“…”

[P158]
*Just kill me already, you bastards.*

[P159]
[^1]: In Korean, the line puns on *boja* (“let’s see / wait and see”) and *bojagi*, a wrapping cloth.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 17

[P2]
Circulating qi.

[P3]
It was a method of regulating one’s energy by evening one’s breathing: drawing qi from outside the body, circulating it within, and accumulating it.

[P4]
Right now, I was circulating qi using the Jin Family’s Cultivation Technique.

[P5]
*This still feels incredible every time.*

[P6]
I had never realized there were so many acupoints in my body.

[P7]
I had once heard that the human body contained more than three hundred and sixty acupoints, but based on what I could feel while circulating qi through the cultivation technique, there were even more than that.

[P8]
*Is it because I’m a virtual game character?*

[P9]
*Whatever.*

[P10]
The ten years of internal energy I drew up from my dantian circulated through my body. If internal energy was a car, then the meridians were a highway. All I had to do was sit behind the wheel and press the accelerator.

[P11]
The internal energy raced along the straight and curving meridians throughout my body before returning to my dantian.

[P12]
*And this is where the real problem starts.*

[P13]
I took a long, deep breath. Then I felt it.

[P14]
A second internal energy occupied my dantian like an enormous boulder that would not budge, no matter how hard I willed it to.

[P15]
*What the hell are you?*

[P16]
It had been a mystery ever since I first circulated qi. An unidentified energy that had taken root like it owned the place.

[P17]
I didn’t know where it had come from, how it had been formed, or why I couldn’t use it, but one thing was certain. This unidentified energy contained more power than the ten years of internal energy I possessed.

[P18]
*Until now, I hadn’t even dared touch it.*

[P19]
To be more precise, I hadn’t intended to. Until a few days ago, I had been waiting for rescue while doing just enough to stay alive.

[P20]
But things were different now.

[P21]
*I need more internal energy.*

[P22]
If I wanted to escape on my own, I had to fulfill the Logout Quest’s condition: reaching the First Rate realm.

[P23]
I also knew that I needed internal energy on the level of Lee Seogeun’s to become First Rate.

[P24]
*I’ll make it mine.*

[P25]
I cautiously began moving my internal energy.

[P26]
The moment I sent it toward the unidentified energy, half anxious and half expectant, I realized something.

[P27]
*Not even close.*

[P28]
Internal energy was, strictly speaking, qi itself—something without a physical form. And yet the instant the two energies touched, I felt powerful rejection and resistance.

[P29]
No. It was even pulling me in. At this rate, it was going to eat me alive.

[P30]
*Hey, hey, hey! Wait a second!*

[P31]
I hurriedly withdrew my internal energy and shook off the unidentified energy, which clung to me until the very end. At the same time, a System notification rang out.

[P32]
Ding.

[P33]
> **System**
>
> - You have trained the **Jin Family’s Cultivation Technique**. Internal energy has risen slightly.
>
> - As a result of repeated training, **Sinews** and **Bones** have each increased by 1.

[P34]
“What the hell was that?”

[P35]
I calmed my pounding heart and opened my Status Window.

[P36]
> **Status Window**
>
> **Lv. 17 Jin Taekyung**
>
> **Class:** Second Rate martial artist  
> **Fame:** 73  
> **Titles:** 4 (Title effects active)
>
> - **Scion of a Prestigious Family** — All stats +5, Fame +50
> - **Family’s Shame** — All stats –5, Fame –50
> - **Novice Trainee** — Training speed +10%
> - **Gambler** — Combat-related stats +10% in one-on-one matches
>
> **Strength:** 65  **Stamina:** 65  
> **Agility:** 75  **Intelligence:** 10  
> **Charm:** 10  **Internal Energy:** 10 years
>
> **Remaining Points:** 0

[P37]
The numbers in my Status Window were fairly impressive by now.

[P38]
I had gained three levels all at once through the Duel Quest, then distributed the thirty points equally among Strength, Stamina, and Agility.

[P39]
But looking at the Status Window still left a bitter taste in my mouth.

[P40]
*My internal energy is the only thing that hasn’t changed.*

[P41]
This damn System kept saying that my internal energy had risen, but the amount displayed in the Status Window remained exactly the same.

[P42]
*Do I need to take a spirit pill, an elixir, something like that?*

[P43]
I thought of Jin Wikyung. If I screwed up my courage and said, *Big brother, just give me one spirit pill,* I didn’t think he would refuse me outright.

[P44]
I’d ask him the next time I saw him. I would also ask about the unidentified energy inside my dantian.

[P45]
Krrrummble.

[P46]
At that moment, the entrance to the training hall opened, and two people stepped inside.

[P47]
“Um, Young Master Jin?”

[P48]
It was Han Yeop. Behind him stood a martial artist I had never seen before. The man spoke in a blunt tone that matched his appearance.

[P49]
“The Lesser Family Head commands you to attend the family council.”

[P50]
“The Lesser Family Head?”

[P51]
That worked out perfectly. There was something I wanted to ask him about.

[P52]
* * *

[P53]
“It is beyond doubt. A few bones were broken, and there was some minor internal damage, but that level of injury could never—”

[P54]
“Are you sure? You swear that on the name of the Medicine King Hall Leader?”

[P55]
“I said it’s true! I examined him myself!”

[P56]
“Then why are you talking down to me? I treated you with respect because you’re another Hall Leader, and now you think I’m a joke!”

[P57]
“You were the one who started talking down to me, White Tiger Hall Leader!”

[P58]
I stared blankly at the ceiling of the meeting room. The shouts and curses flying from every direction made my ears ring.

[P59]
*What the hell is this?*

[P60]
This wasn’t what I had imagined a family council would be like. I had pictured a quiet, orderly atmosphere where everyone exchanged opinions and searched for common ground…

[P61]
“You think every Hall Leader is your equal? You’re nothing but some quack doctor!”

[P62]
“Listen to this young bastard. I ought to shove a large needle straight into his perineal acupoint!”

[P63]
Two men in their forties or fifties, both with receding, M-shaped hairlines, were grabbing each other by the collars and shaking one another. Just watching them made my head hurt.

[P64]
The problem was that scenes like this were unfolding all over the room.

[P65]
Maybe that was why most of the people there didn’t seem to notice me opening the door and taking my seat.

[P66]
—You came?

[P67]
The voice sounded as if it had entered through my head rather than my ears. It was Sound Transmission.

[P68]
I turned my head and met Jin Wikyung’s gaze from the seat of honor. He gave me a tired smile.

[P69]
—It’s a madhouse, isn’t it?

[P70]
*You said it. Why did you call me to this madhouse, you old man?*

[P71]
When I shot him a reproachful look, Jin Wikyung sent another message through Sound Transmission, his expression turning sheepish.

[P72]
—I couldn’t help it. The Elder Council demanded your attendance. In any case… you are involved in this matter.

[P73]
*The Elder Council? I’m involved in this matter?*

[P74]
*What matter am I involved in…? Oh. The Mount Heng Sword Sect?*

[P75]
I quickly pieced things together amid the shouting and cursing.

[P76]
If there was one recent incident connected to me, it was the Mount Heng Sword Sect. And because of that incident, this thing called the Elder Council had summoned me.

[P77]
That had to be it.

[P78]
*Come to think of it, there are some old men here I’ve never seen before.*

[P79]
There were four of them. Every one had a face covered in age spots and hair that had gone completely white.

[P80]
They watched the men with the M-shaped hairlines grab each other by the collars with cold eyes. Anyone could see it was a nursing home—or rather, the Elder Council.

[P81]
—And… the Head Elder is here.

[P82]
I turned toward Jin Wikyung without thinking, then flinched.

[P83]
*What the hell? Where did that old man come from?*

[P84]
I had only just noticed that there were two seats of honor today. An old man was sitting to Jin Wikyung’s right, staring at me. His gaze made my face prickle.

[P85]
*Is that old man the Head Elder?*

[P86]
White hair, a white beard, and white eyebrows. He looked like an immortal who had stepped out of an old painting. His back was straight, his shoulders broad, and his skin taut enough to make his age seem meaningless.

[P87]
*But why is he staring at me so intently?*

[P88]
I gathered strength in my eyes and tried to glare back at the Head Elder…

[P89]
Then I quietly looked away.

[P90]
Not because I thought I would lose if we locked eyes. It was respect for my elders. Respect for my elders. Really.

[P91]
*I’ll just keep my head down.*

[P92]
Jin Wikyung’s Sound Transmission continued in the meantime.

[P93]
—You may not know this because you lost your memory, but the Head Elder is your great-uncle and the most senior elder in the family. Be especially careful with your words and actions.

[P94]
I hadn’t even seen my father’s face, and now I had a great-uncle.

[P95]
*Maybe this place has relatives by marriage, distant cousins, and every kind of obscure uncle, too.*

[P96]
I gave Jin Wikyung a small nod.

[P97]
—And… you must not be flustered by what happens from this point onward. Calmly tell them only the truth. Do you understand?

[P98]
I didn’t know exactly what was going on, but one thing was certain: Jin Wikyung was on my side.

[P99]
I nodded again, and Jin Wikyung rose with a faint smile.

[P100]
“Silence, everyone.”

[P101]
His voice, infused with internal energy, swept across the meeting hall.

[P102]
“This is a family council of the Jin Family of Taiyuan, and we have gathered to discuss a grave matter. Since our witness has arrived, I intend to begin the interrogation.”

[P103]
The meeting hall had gone quiet without me noticing. With everyone’s attention focused on him, Jin Wikyung spoke.

[P104]
“By the authority of the Lesser Family Head and current acting Family Head, I begin this interrogation. Third Young Master Jin Taekyung, step forward.”

[P105]
I felt everyone’s eyes on me as I walked forward. I had expected this much. They hadn’t summoned me for no reason.

[P106]
But…

[P107]
“I ask you this. Did you poison Lee Seogeun of the Mount Heng Sword Sect?”

[P108]
That was something I hadn’t expected.

[P109]
* * *

[P110]
“No.”

[P111]
I barely managed to force the word out. My thoughts were a mess from the sudden question.

[P112]
*Lee Seogeun was dead? Poisoned, at that?*

[P113]
“Tell us the truth. If it turns out to be a lie…”

[P114]
“I have nothing to do with Lee Seogeun’s poisoning.”

[P115]
My answer was as sharp as a blade. Jin Wikyung let out a sigh of relief.

[P116]
—Keep doing exactly this.

[P117]
The interrogation proceeded quickly. They asked questions, and I answered them.

[P118]
Starting with Jin Wikyung, they fired one question after another at me.

[P119]
About half of the questions concerned whether I had been involved in poisoning Lee Seogeun, and I continued to deny it.

[P120]
*Because it was true.*

[P121]
Just in case, I secretly opened my System Window to check. I was certain of it. None of my martial arts or abilities had anything to do with poison. I didn’t have any such Items, either.

[P122]
That was why I could answer without hesitation.

[P123]
“No.”

[P124]
The problem was that, at some point, the atmosphere in the meeting hall began to grow strange.

[P125]
“Do you have any evidence to prove it?”

[P126]
“Evidence?”

[P127]
White Tiger Hall Leader, was it? The man whose name I didn’t even know stared at me with obvious displeasure.

[P128]
“That is correct. Evidence. I mean evidence that would prove the Third Young Master’s innocence.”

[P129]
*What the hell is this bastard talking about?*

[P130]
“Why do I have to prove it?”

[P131]
“What?”

[P132]
“Don’t talk down to me.”

[P133]
“Listen here, Third Young Master!”

[P134]
“You’re free to suspect me, but shouldn’t you be the ones looking for evidence? Am I wrong?”

[P135]
I’d been letting it slide, and these bastards thought they could wrap me up like a cloth?[^1]

[P136]
Fuming, I glared at the White Tiger Hall Leader as he sat down, then noticed something strange.

[P137]
*Well, well. Look at this.*

[P138]
The White Tiger Hall Leader kept stealing glances at the old men of the Elder Council.

[P139]
The strange thing was that everyone who had been pressing and interrogating me was doing something similar.

[P140]
Nearly half the people in attendance were acting this way. It was getting difficult to pretend I hadn’t noticed.

[P141]
*So this is a factional struggle.*

[P142]
The Elder Council and Jin Wikyung.

[P143]
Even now, a power struggle was taking place between the senior members of the family and the Lesser Family Head who was young enough to be their grandson.

[P144]
*What a family.*

[P145]
Only a few people remained to question me. The problem was who those people were.

[P146]
Faces covered in age spots. Canny, experienced eyes.

[P147]
The old men of the Elder Council.

[P148]
The oldest and fattest of them opened his mouth.

[P149]
“Enough of this empty questioning. There is only one thing this old man wishes to ask. Where did this matter begin?”

[P150]
The senior members allied with the Elder Council answered as if they had been waiting for the question.

[P151]
“The Third Young Master.”

[P152]
“Who was it that dragged our family’s reputation through the mud with disorderly words and conduct?”

[P153]
“The Third Young Master.”

[P154]
The same answer came from several places around the room.

[P155]
“Then who was it that provoked the Mount Heng Sword Sect’s prized treasure and brought us to this crisis?”

[P156]
“…”

[P157]
*Just kill me already, you bastards.*

[P158]
[^1]: In Korean, the line puns on *boja* (“let’s see / wait and see”) and *bojagi*, a wrapping cloth.
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 17,
  "passed": true,
  "metrics": {
    "source_characters": 5375,
    "translation_characters": 12800,
    "length_ratio": 2.381,
    "source_paragraphs": 162,
    "translation_paragraphs": 159
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "기세",
        "preferred": "aura / momentum"
      }
    },
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
        "korean": "제자",
        "preferred": "Disciple"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진가심법",
        "preferred": "Jin Family's Cultivation Technique"
      }
    },
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
