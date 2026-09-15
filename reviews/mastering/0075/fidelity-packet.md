# Fidelity Gate — Chapter 75

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
  1|＃75화
  2|
  3|
  4|
  5|현대와 무림을 구분하는 방법은 우습게도 냄새와 온도다.
  6|
  7|VR 헬멧 안의 땀 냄새. 창문 너머에서 비춰 오는 햇살 때문에 적당히 달궈진 캡슐 안의 열기.
  8|
  9|“후아.”
 10|
 11|헬멧을 벗고 캡슐을 빠져나오자 좀 살 것 같다. 그래 봤자 열탕에서 온탕으로 바뀐 정도지만.
 12|
 13|‘얼마나 지난 거지?’
 14|
 15|손목에 찬 시계를 확인했다. 약 7년 전, 헌터 훈련소 앞 가판대에서 샀던 만이천 원짜리 싸구려 디지털시계는 알람과 스톱워치 기능이 있다는 장점이 있었다.
 16|
 17|삑.
 18|
 19|
 20|
 21|[02:05:35]
 22|
 23|
 24|
 25|두 시간 하고도 5분 35초.
 26|
 27|무림에서 20일 정도를 머물렀으니 지난번과 비교해 얼추 시간이 맞아떨어진다.
 28|
 29|‘현대로 왔으니 시간 배율이 역전되었을 거고.’
 30|
 31|로그아웃을 한 지금은 현대에서의 열흘이 무림의 한 시간이다. 나는 고시원 공용 샤워장에서 몸을 씻은 다음 방으로 돌아왔다.
 32|
 33|방문을 닫으려던 찰나, 검은 그림자가 휙 솟구쳤다.
 34|
 35|“왁!”
 36|
 37|그래, 성진호 이 인간일 줄 알았다.
 38|
 39|“어.이.구. 깜.짝. 놀.랐.네.”
 40|
 41|“……뭐냐 그 반응은. 알고 있었어?”
 42|
 43|“들숨 날숨이 아주 격렬하시던데. 진호 씨, 흥분하셨나 봐.”
 44|
 45|날이 지날수록 예리해진 오감은 굳이 [기감]이 아니어도 주위의 소리와 움직임을 잡아낼 수 있다.
 46|
 47|나름 숨죽인 채 기다리고 있었던 모양이지만 내 귀에는 그의 작은 움직임과 숨소리 하나하나가 천둥처럼 들렸다.
 48|
 49|“숨 좀 작게 쉬어. 명색이 고시원 총무인데 숨소리가 커서 민원 들어오면 곤란하지.”
 50|
 51|“젠장. 어떻게 알았지? F급 헌터 주제에…… 아, 너 얼마 전에 C급 됐지. 참.”
 52|
 53|“인성 봐라. F급이라고 놀리는 게 아주 입에 붙었구만.”
 54|
 55|“야, 네가 내 나이 돼 봐라. 어제 먹은 반찬도 기억 안 나는데 겨우 일주일 전에 있었던 일이 팍팍 떠오르겠냐?”
 56|
 57|“일주일?”
 58|
 59|겨우 그것밖에 안 됐나?
 60|
 61|내게는 한 달도 훨씬 지난 일이 진호 형에게는 고작 지난주에 있었던 일이다. 미묘한 괴리감이 느껴졌다.
 62|
 63|“어. 표정이 왜 그래? 문제라도 있냐?”
 64|
 65|“문제는 무슨. 그런데 무슨 일로 찾아왔어?”
 66|
 67|“이 자식 이거 말 뽄새 보게. 우리가 볼일 있어야 볼 수 있는 비즈니스 관계야? 어?”
 68|
 69|“본론만. 짧게.”
 70|
 71|진호 형의 얼굴이 굳어졌다. 장난이 너무 심했나?
 72|
 73|생각해 보니 요즘 내가 너무 무심했던 것 같기도 하다. 무림으로 돌아가기 전에도 여러 가지 문제로 얼굴도 자주 못 봤는…….
 74|
 75|“저녁. 사 줘.”
 76|
 77|“…….”
 78|
 79|“삼겹살. 철판구이. 치맥.”
 80|
 81|시바. 그럼 그렇지.
 82|
 83|그 와중에 메뉴도 자기가 고르고 자빠졌네.
 84|
 85|“나한테 돈 맡겨 뒀어?”
 86|
 87|“네 돈이 내 돈. 내 돈이 내 돈 아니냐.”
 88|
 89|“발음 똑바로 해라. C급 헌터 주먹맛 보고 싶지 않으면.”
 90|
 91|움찔한 진호 형이 손바닥을 싹싹 비볐다.
 92|
 93|“부탁드립니다. 선생님의 돈으로 제 메마른 위장에 기름칠 좀 해 주십시오.”
 94|
 95|“…….”
 96|
 97|태세 전환 봐라. 우디르도 울고 가겠다.
 98|
 99|어이가 없었지만 한편으로는 피식 웃음이 나왔다. 한 달 가까이 제대로 된 진짜 음식을 못 먹은 위장도 비명을 질러 대던 차였다.
100|
101|‘간만에 제대로 먹어 보자.’
102|
103|나는 엄숙한 목소리로 말했다.
104|
105|“태도가 마음에 드는군. 앞장서라.”
106|
107|“어디로 모실까요?”
108|
109|“삼겹살이나 철판구이는 질렸다. 오늘은 좀 더 비싸게 먹어 보자꾸나.”
110|
111|“서, 선생님. 그렇다면!”
112|
113|진호 형이 눈을 부릅떴다.
114|
115|“한우! 방목으로 키워져 환상적인 마블링을 자랑하는 그것?”
116|
117|“뭔 개소리야. 곱창 먹으러 갈 건데.”
118|
119|“…….”
120|
121|“싫으면 굶든가.”
122|
123|턱.
124|
125|내 어깨를 붙잡은 진호 형이 비장한 얼굴로 말했다.
126|
127|“예전부터 꼭 그렇게 먹어 보고 싶었습니다.”
128|
129|그날 오후 다섯 시부터 시작된 이른 식사는 3차 막걸리 집에서 끝났고, 진호 형은 술에 떡이 됐다.
130|
131|“크워어어.”
132|
133|“…….”
134|
135|이거 어디서 많이 본 장면인데.
136|
137|묘한 기시감을 느끼며 진호 형을 들쳐 업었을 때, 휴대폰이 울렸다.
138|
139|
140|
141|〈 명품충
142|
143|
144|
145|명품충
146|
147|내일 같은 시간, 같은 장소에서 뵙죠.
148|
149|
150|
151|짤막한 문자 한 통. 발신인은 최 팀장이었다.
152|
153|
154|
155|* * *
156|
157|
158|
159|수면 모드의 단점이자 장점은 수면 시간이 줄어든다는 점이다. 조필과의 싸움에서 큰 부상을 입었을 때를 제외하면 세 시간을 넘긴 적이 없다.
160|
161|‘수련하기에는 좋지.’
162|
163|새벽 세 시.
164|
165|최적의 컨디션으로 눈을 뜬 나는 가부좌를 틀었다. 언제부턴가 하루의 시작과 끝은 늘 운기조식이다.
166|
167|솨아아.
168|
169|공력의 물결이 흐르기 시작했다.
170|
171|단전에서 솟구친 15년의 공력이 신체 내부에 쌓인 노폐물을 정화시키며 잠들어 있던 혈도에 생기를 불어넣었다.
172|
173|띠링.
174|
175|
176|
177|- [운기조식]을 마쳤습니다.
178|
179|- [공력]이 아주 약간 증가했습니다.
180|
181|
182|
183|시스템 알림과 함께 눈을 떴을 때는 두 시간이 훌쩍 지난 후였다. 무림이었다면 곧장 연무장으로 나가 몸을 풀었겠지만 현실은 여러 가지 제약이 많다.
184|
185|양계장처럼 다닥다닥 붙어 있는 고시원에서는 더더욱.
186|
187|‘망할 놈의 고시원. 빨리 탈출하든가 해야지.’
188|
189|수련도 돈으로 하는 시대다. 잘 버는 놈들이야 널찍한 개인 트레이닝 룸을 몇 개씩 가지고 있지만 나처럼 없는 놈들은 열악한 환경에 맞추는 수밖에.
190|
191|“후읍. 흡.”
192|
193|오전 내내 동네를 뛰고, 돌아와서는 기본적인 맨몸 운동을 쉬지 않고 이어 갔다. 능력치가 높아진 덕분인지 지치기는커녕 오히려 활력이 샘솟는다.
194|
195|그런 나를 보며 진호 형이 질린 얼굴로 물었다.
196|
197|“지치지도 않냐?”
198|
199|“별로.”
200|
201|“한 손 팔 굽혀 펴기를 너처럼 쉽게 하는 놈은 처음 본다. 몇 개째야?”
202|
203|“몰라. 삼백까지 세고 귀찮아서 안 셌어.”
204|
205|“괴물이네. 원래 C급 헌터쯤 되면 그 정도는 하는 거냐?”
206|
207|“그런데, 성진호 씨.”
208|
209|“어?”
210|
211|“왜 왔어?”
212|
213|십여 분 전 퀭한 몰골로 나타나더니 아직도 내 방에서 안 나가는 진호 형이었다.
214|
215|“보면 모르냐. 라면 먹으려고 왔지.”
216|
217|톡톡. 촤아악.
218|
219|다 익어 가는 면발 위로 날계란을 투하하는 모습이 자연스럽다.
220|
221|반숙을 만들기 위한 버너 화력 컨트롤은 절정 고수라고 해도 좋을 정도다.
222|
223|“그걸 굳이 여기서 처먹어야 하는 이유 세 가지만 대 봐.”
224|
225|“첫째. 내 방에 TV가 없으니까. 둘째. 네 방에 TV가 있으니까. 셋째. 라면은 TV를 보면서 먹어야 제맛이니까.”
226|
227|청산유수로 흘러나오는 말을 들으니 피가 거꾸로 솟는다.
228|
229|“차라리 하나 사! 돈 없으면 그냥 가져가!”
230|
231|“아, 그건 좀. 어차피 나갈 건데 짐 늘려 봤자 뭐하냐.”
232|
233|“그럼 귀찮게 자꾸 들락거리지 말고…… 응? 방금 뭐라고?”
234|
235|“뭐가?”
236|
237|“아니, 나간다고?”
238|
239|“아, 그거.”
240|
241|진호 형이 떡이 진 머리를 긁적였다.
242|
243|“그냥 그렇게 됐다. 뭐, 날짜까지 확정된 건 아닌데 조만간 방 빼려고. 언제까지 여기 처박혀 있을 수도 없는 노릇이고.”
244|
245|“…….”
246|
247|“뭘 그런 눈으로 쳐다봐?”
248|
249|“아니, 뭐. 그냥.”
250|
251|나는 머쓱한 얼굴로 시선을 피했다.
252|
253|고시원에 사는 사람들 중 사연 없는 사람이 어디 있겠나. 나도 그렇고 진호 형도 마찬가지다. 구태여 이유를 묻는 건 실례다.
254|
255|‘그래도 아쉽긴 하네.’
256|
257|몇 년간 친구처럼, 형제처럼 지냈던 사람이다. 이렇게 갑자기 나간다니.
258|
259|복잡 미묘한 기분에 사로잡혀 있던 나는 조심스레 입을 열었다.
260|
261|“형, 혹시…….”
262|
263|“네 마음은 알겠는데. 정중하게 거절한다.”
264|
265|무슨 말을 하려는지 알아챈 걸까? 내 말을 단칼에 잘라 낸 진호 형이 말을 이었다.
266|
267|“인마, 형 나이가 서른이야. 내 밥그릇은 내가 챙겨.”
268|
269|“그렇다면 어쩔 수 없고.”
270|
271|진호 형이라면 같이 살아도 될 것 같았는데, 섣부른 오지랖이 그의 자존심을 건드린 모양이었다.
272|
273|형이 구겨진 얼굴로 냄비 뚜껑을 열었다.
274|
275|“차라리 처음부터 말을 하든가.”
276|
277|“애초에 생각도 없었으면서 무슨.”
278|
279|“무슨 헛소리야. 네가 안 먹는다고 해서 하나만 끓였는데.”
280|
281|“……?”
282|
283|아니, 잠깐만. 이거 이야기 흐름이 어떻게 되는 거냐.
284|
285|몇 초간의 침묵 끝에 내가 입을 뗐다.
286|
287|“무슨 얘기야 그게. 갑자기 뭘 끓여.”
288|
289|“당연히 라면이지.”
290|
291|진호 형이 흉흉한 눈빛으로 나를 노려봤다.
292|
293|“꼭 안 먹는다고 해 놓고 맛있게 끓이면 한 젓가락 달라는 놈이 있어요. 내가 너한테 한두 번 당해?”
294|
295|“…….”
296|
297|“C급 헌터라는 놈이 가난한 형님 밥그릇에 손을 뻗쳐? 네가 그러고도 사람이냐?”
298|
299|“…….”
300|
301|앞에서 밥그릇 운운한 게, 진짜 밥그릇이었구나.
302|
303|방금 들은 말 그대로 돌려주고 싶다.
304|
305|‘저게 사람이냐.’
306|
307|저런 인간하고 같이 살 생각을 한 내가 병신이지.
308|
309|나는 자괴감을 느끼며 옷을 걸쳐 입었다. 슬슬 최 팀장을 만나러 갈 시간이다.
310|
311|쾅!
312|
313|부서져라 방문을 닫고 빠져나오는 내 등 뒤로 마지막 외침이 울려 퍼졌다.
314|
315|- 마트 가는 거면 김치 좀!
316|
317|아, 죽이고 싶다.
318|
319|
320|
321|* * *
322|
323|
324|
325|‘장소가 어디였지?’
326|
327|약 20일 전의 기억을 더듬어 약속 장소에 도착했다.
328|
329|빌딩 숲 중심부에 위치한 대형 카페. 창가에 앉아 있던 잘생긴 남자가 나를 발견하고 손을 흔들었다.
330|
331|“여깁니다.”
332|
333|굳이 말하지 않아도 알 수 있었다. 매장 안에 수십 개의 테이블이 있는데도 앉아 있는 손님은 오직 최 팀장 혼자였으니까.
334|
335|‘여전히 잘생겼네.’
336|
337|얇은 캐주얼 정장을 걸친 최 팀장은 방금 화보에서 튀어나온 것 같았다. 20대에 모든 걸 가진 성공한 인생. 외모, 재력, 성격…… 아니다. 성격은 빼자.
338|
339|가벼운 악수를 나눈 우리는 자리에 앉았다.
340|
341|“식사는 하셨습니까?”
342|
343|“아뇨.”
344|
345|최 팀장이 고개를 갸웃했다.
346|
347|“그래요? 라면 드신 것 같은데.”
348|
349|“…….”
350|
351|젠장, 이 자식 완전 개코네.
352|
353|고시원에서 있었던 이야기를 구구절절하게 설명하기에는 너무 부끄럽다. 나는 황급히 화제를 돌렷다.
354|
355|“점심시간인데 사람이 없네요.”
356|
357|“영업을 안 하니까요.”
358|
359|“예?”
360|
361|“유리창도 커튼으로 가리고 문에 클로즈(Closed) 팻말도 걸어 놨는데 당연히 안 들어오죠.”
362|
363|주위를 둘러보니 정말 최 팀장의 말대로였다.
364|
365|약속 장소가 여기니, 당연히 열려 있을 거라고 생각하고 들어와서 눈치를 못 챈 모양이다. 이 상황 자체가 너무 이상해서 눈을 깜빡였다.
366|
367|“그런데 지금 영업하는 중이잖아요.”
368|
369|매장 안의 불빛은 환하고, 에어컨 바람으로 시원하다. 언뜻 보이는 직원들만 열 명인데 왜 문을 닫아 놓은 거지?
370|
371|최 팀장은 태연하게 대꾸했다.
372|
373|“해야죠. 손님이 있으니까.”
374|
375|“영업 안 한다면서요?”
376|
377|“그거야 사장 마음 아니겠습니까.”
378|
379|“어…… 팀장님. 혹시나 해서 물어보는 건데요.”
380|
381|“굳이 안 물어보셔도 됩니다. 이 카페 제 거니까요.”
382|
383|그래, 그럴 것 같더라.
384|
385|곰곰이 생각해 보니 지난번에 만났을 때도 카페 안에는 우리 둘뿐이었다.
386|
387|‘파도 파도 끝이 없네.’
388|
389|나는 혀를 내두르며 말했다.
390|
391|“팀장님, 돈 많으시네요.”
392|
393|“부족하지 않을 만큼 있습니다. 그러니까 이런 계약서도 내밀 수 있는 거고요.”
394|
395|최 팀장이 부드럽게 웃으며 서류철을 내밀었다.
396|
397|“자, 이제 일 얘기를 해 볼까요?”
398|
399|더 이상 망설일 이유는 없다. 나는 힘차게 고개를 끄덕였다.
400|
401|“그러시죠.”
402|
403|한 시간 후, 내가 마지막 서명을 끝마침과 동시에 시스템 알림이 울렸다.
404|
405|띠링.
```

## Assembled English

```markdown
[P1]
# Chapter 75

[P2]
The way to tell the modern world apart from Murim is, oddly enough, by smell and temperature.

[P3]
The smell of sweat inside a VR helmet. The heat inside a capsule warmed just right by sunlight streaming through the window.

[P4]
“Phew.”

[P5]
Once I took off the helmet and climbed out of the capsule, I finally felt like I could breathe. It was still only the difference between a scalding bath and a hot one, though.

[P6]
*How much time has passed?*

[P7]
I checked the watch on my wrist. The cheap twelve-thousand-won digital watch I’d bought from a street stall in front of the Hunter training center about seven years ago had the advantage of an alarm and a stopwatch.

[P8]
Beep.

[P9]
[02:05:35]

[P10]
Two hours, five minutes, and thirty-five seconds.

[P11]
I had spent around twenty days in Murim, so the timing roughly matched what had happened last time.

[P12]
*Now that I’m back in the modern world, the time ratio must have reversed.*

[P13]
With Logout complete, ten days in the modern world amounted to one hour in Murim. I washed up in the goshiwon’s[^1] communal shower and returned to my room.

[P14]
Just as I was about to close the door, a black shadow sprang up.

[P15]
“Boo!”

[P16]
Knew it. Of course it was Seong Jinho.

[P17]
“Oh. My. God. What. A. Surprise.”

[P18]
“…What’s with that reaction? You knew I was here?”

[P19]
“Your inhales and exhales were extremely intense. Mr. Jinho, were you excited?”

[P20]
My five senses had grown sharper with each passing day. I could pick up the sounds and movements around me without even using Qi Sense.

[P21]
He seemed to have been keeping his breathing quiet as he waited, but to my ears, every tiny movement and breath he made sounded like thunder.

[P22]
“Try breathing a little more quietly. You’re supposed to be the goshiwon manager. It’d be a problem if people started filing noise complaints about you.”

[P23]
“Damn it. How did you know? You’re just an F-rank Hunter… Oh, right. You became C-rank a while ago.”

[P24]
“Listen to you. Making fun of me for being F-rank has really become a habit.”

[P25]
“Hey, wait until you’re my age. I can’t even remember what side dishes I ate yesterday. You think something that happened barely a week ago is going to pop right into my head?”

[P26]
“A week?”

[P27]
Was that really all the time that had passed?

[P28]
To me, it had been well over a month. To Jinho-hyung, it had happened just last week. I felt a subtle sense of disconnect.

[P29]
“Hey. What’s with that look? Is something wrong?”

[P30]
“Nothing’s wrong. Anyway, what brings you here?”

[P31]
“Listen to the way you talk. Are we in some kind of business relationship where we only see each other when there’s business involved?”

[P32]
“Just get to the point. Keep it short.”

[P33]
Jinho-hyung’s face hardened. Had I taken the teasing too far?

[P34]
Come to think of it, I had been too indifferent lately. Even before returning to Murim, I hadn’t been able to see him often because of all sorts of problems…

[P35]
“Buy me dinner.”

[P36]
“…”

[P37]
“Grilled pork belly. Teppanyaki. Fried chicken and beer.”

[P38]
Shit. Of course.

[P39]
And he even had the nerve to choose the menu himself.

[P40]
“Did you leave money with me?”

[P41]
“Your money is my money. And my money is my money, isn’t it?”

[P42]
“Pronounce that properly. Unless you want a taste of a C-rank Hunter’s fist.”

[P43]
Jinho-hyung flinched and rubbed his palms together.

[P44]
“Please, sir. Use your money to grease my parched stomach.”

[P45]
“…”

[P46]
That stance switch would make Udyr weep.

[P47]
It was ridiculous, but a quiet laugh escaped me. My stomach had also been screaming after nearly a month without a proper meal.

[P48]
*Let’s eat something decent for once.*

[P49]
I spoke in a solemn voice.

[P50]
“I approve of your attitude. Lead the way.”

[P51]
“Where would you like to go, sir?”

[P52]
“I’m tired of grilled pork belly and teppanyaki. Let’s have something a little more expensive today.”

[P53]
“Th-then, sir!”

[P54]
Jinho-hyung’s eyes widened.

[P55]
“Hanwoo![^2] That pasture-raised beef with the incredible marbling?”

[P56]
“What the hell are you talking about? We’re going out for gopchang.[^3]”

[P57]
“…”

[P58]
“If you don’t like it, starve.”

[P59]
Thump.

[P60]
Jinho-hyung grabbed my shoulder and declared with a solemn expression, “I’ve always wanted to try it.”

[P61]
Our early dinner began at five that afternoon and ended at a makgeolli bar on our third round. By then, Jinho-hyung was completely plastered.

[P62]
“Krroooorr.”

[P63]
“…”

[P64]
I had seen this scene somewhere before.

[P65]
As a strange sense of déjà vu came over me and I hoisted Jinho-hyung onto my back, my phone rang.

[P66]
〈Designer-Brand Junkie

[P67]
> **Designer-Brand Junkie**
>
> See you tomorrow at the same time, same place.

[P68]
A single short text. The sender was Team Leader Choi.

[P69]
* * *

[P70]
The downside—and upside—of Sleep Mode was that it reduced how much sleep I needed. Except when I’d been badly injured in the fight with Jopil, I had never slept for more than three hours.

[P71]
*It’s useful for training.*

[P72]
Three in the morning.

[P73]
I woke up in peak condition and sat cross-legged. At some point, circulating my qi had become how I began and ended every day.

[P74]
Whoosh.

[P75]
A wave of internal energy began to flow.

[P76]
The fifteen years of internal energy surging from my dantian cleansed the waste accumulated inside my body and breathed vitality into dormant acupoints.

[P77]
Ding.

[P78]
> **System**
>
> - You have finished circulating your qi.
>
> - Your internal energy has increased very slightly.

[P79]
When the System notification sounded and I opened my eyes, more than two hours had passed. If I were in Murim, I would have gone straight to the training ground to warm up, but the real world came with all sorts of restrictions.

[P80]
Especially in a goshiwon, where the rooms were packed together like a chicken farm.

[P81]
*Damn goshiwon. I need to get out of here soon.*

[P82]
Even training cost money these days. People who earned enough had several spacious private training rooms, while broke people like me had no choice but to make do with lousy conditions.

[P83]
“Hup. Huff.”

[P84]
I spent the entire morning running through the neighborhood. When I returned, I moved straight into basic bodyweight exercises without taking a break. Maybe it was because my Stats had increased, but instead of getting tired, I felt more energized by the minute.

[P85]
Jinho-hyung watched me with an appalled expression.

[P86]
“Don’t you ever get tired?”

[P87]
“Not really.”

[P88]
“I’ve never seen anyone do one-arm push-ups as easily as you. How many have you done?”

[P89]
“I don’t know. I counted to three hundred, then got too lazy to keep counting.”

[P90]
“You’re a monster. Is that normal for a C-rank Hunter?”

[P91]
“By the way, Seong Jinho.”

[P92]
“Huh?”

[P93]
“Why are you here?”

[P94]
Jinho-hyung had shown up about ten minutes earlier looking haggard, and he still hadn’t left my room.

[P95]
“Can’t you tell? I came to eat ramen.”

[P96]
Tap tap. Ssshhk.

[P97]
The way he dropped a raw egg onto the almost-cooked noodles looked completely natural.

[P98]
His control of the burner flame to leave the egg perfectly runny was worthy of a Peak master.

[P99]
“Give me three reasons why you need to stuff your face with that in here.”

[P100]
“First, there’s no TV in my room. Second, there’s a TV in your room. Third, ramen tastes best when you eat it while watching TV.”

[P101]
He rattled it all off without hesitation, and my blood started boiling.

[P102]
“Just buy one! If you don’t have the money, just take mine!”

[P103]
“Ah, I’d rather not. I’m leaving soon anyway. Why bother adding to my luggage?”

[P104]
“Then stop coming in and out of here and bothering me… Huh? What did you just say?”

[P105]
“What?”

[P106]
“Wait. You’re leaving?”

[P107]
“Ah, that.”

[P108]
Jinho-hyung scratched his matted hair.

[P109]
“It just worked out that way. The date isn’t set yet, but I’m planning to move out soon. I can’t stay holed up here forever.”

[P110]
“…”

[P111]
“Why are you looking at me like that?”

[P112]
“No, it’s nothing.”

[P113]
I awkwardly looked away.

[P114]
Who lived in a goshiwon without a story of their own? I had mine, and Jinho-hyung had his. It would be rude to pry.

[P115]
*Still, it’s a shame.*

[P116]
He was someone I’d spent years with, like a friend and a brother. And now he was leaving so suddenly.

[P117]
Caught up in complicated feelings, I cautiously opened my mouth.

[P118]
“Hyung, by any chance…”

[P119]
“I know how you feel, but I respectfully decline.”

[P120]
Had he realized what I was going to say? Jinho-hyung cut me off decisively and continued.

[P121]
“Kid, I’m thirty years old. I can take care of my own bowl.”

[P122]
“Then there’s nothing I can do.”

[P123]
I’d thought I could probably live with Jinho-hyung, but sticking my nose in too soon seemed to have pricked his pride.

[P124]
His face scrunched up as he lifted the lid off the pot.

[P125]
“You should’ve just said so from the start.”

[P126]
“What are you talking about? You never had any intention of it.”

[P127]
“What nonsense. I only cooked one because you said you weren’t eating.”

[P128]
“…?”

[P129]
Wait a second. How had the conversation ended up here?

[P130]
After several seconds of silence, I finally asked, “What are you talking about? What’s this about cooking something all of a sudden?”

[P131]
“Obviously, ramen.”

[P132]
Jinho-hyung glared at me menacingly.

[P133]
“There’s always someone who says he isn’t eating, then asks for a chopstickful when you cook it well. How many times have I fallen for that one with you?”

[P134]
“…”

[P135]
“So a C-rank Hunter reaches into his poor hyung’s bowl? Are you even human?”

[P136]
“…”

[P137]
So when he’d mentioned his bowl earlier, he’d meant his actual bowl.

[P138]
I wanted to throw his own words right back at him.

[P139]
*Is that thing even human?*

[P140]
I was a fucking idiot for thinking I could live with someone like him.

[P141]
Ashamed of myself, I threw on some clothes. It was almost time to meet Team Leader Choi.

[P142]
Bang!

[P143]
I slammed the door hard enough to break it and left. One last shout rang out behind me.

[P144]
“If you’re going to the supermarket, get some kimchi!”

[P145]
Ah, I wanted to kill him.

[P146]
* * *

[P147]
*Where was the place again?*

[P148]
I dredged up my memories from about twenty days ago and arrived at the meeting place.

[P149]
It was a large café in the heart of a forest of skyscrapers. A handsome man sitting by the window spotted me and waved.

[P150]
“Over here.”

[P151]
I didn’t need him to say anything. There were dozens of tables in the café, yet Team Leader Choi was the only customer sitting inside.

[P152]
*He’s still handsome.*

[P153]
Dressed in a lightweight casual suit, Team Leader Choi looked as though he had just stepped out of a fashion shoot. A successful man in his twenties who had everything: looks, money, personality…

[P154]
No. Leave personality out of it.

[P155]
After exchanging a brief handshake, we sat down.

[P156]
“Have you eaten?”

[P157]
“No.”

[P158]
Team Leader Choi tilted his head.

[P159]
“Really? You seem to have eaten ramen.”

[P160]
“…”

[P161]
Damn it. This bastard had a bloodhound’s nose.

[P162]
It was too embarrassing to explain the whole story about what had happened at the goshiwon, so I hurriedly changed the subject.

[P163]
“It’s lunchtime, but no one’s here.”

[P164]
“We’re closed.”

[P165]
“What?”

[P166]
“The windows are covered with curtains, and there’s a ‘Closed’ sign on the door. Of course no one’s coming in.”

[P167]
I looked around. Sure enough, everything was exactly as Team Leader Choi had described.

[P168]
I had assumed the café would be open since it was the meeting place, so I hadn’t noticed. The whole situation was so strange that I blinked.

[P169]
“But you’re open right now.”

[P170]
The lights inside were bright, and the air-conditioning kept the place cool. I could glimpse at least ten employees, so why had they closed the door?

[P171]
Team Leader Choi answered calmly.

[P172]
“We have to be open. There’s a customer.”

[P173]
“You just said you were closed.”

[P174]
“That’s up to the owner, isn’t it?”

[P175]
“Uh… Team Leader, I’m asking just to be sure.”

[P176]
“You don’t need to ask. This café is mine.”

[P177]
Right. I’d figured as much.

[P178]
Thinking back, the café had also been empty except for the two of us the last time we met.

[P179]
*I keep digging, and the hole never ends.*

[P180]
I said in amazement, “Team Leader, you have a lot of money.”

[P181]
“I have enough that I don’t need to worry about running short. That’s why I can put a contract like this in front of you.”

[P182]
Team Leader Choi smiled gently and handed me a folder.

[P183]
“Now, shall we talk business?”

[P184]
There was no reason to hesitate any longer. I nodded firmly.

[P185]
“Let’s.”

[P186]
An hour later, just as I finished adding my final signature, the System alert rang out.

[P187]
Ding.

[P188]
[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement, often with shared facilities.

[P189]
[^2]: Hanwoo is a Korean breed of native cattle whose beef is prized for its marbling.

[P190]
[^3]: Gopchang is a Korean dish made from grilled intestines, usually beef intestines.
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
# Chapter 75

[P2]
The way to tell the modern world apart from Murim is, oddly enough, by smell and temperature.

[P3]
The smell of sweat inside a VR helmet. The heat inside a capsule warmed just right by sunlight streaming through the window.

[P4]
“Phew.”

[P5]
Once I took off the helmet and climbed out of the capsule, I finally felt like I could breathe. It was still only the difference between a scalding bath and a hot bath, though.

[P6]
*How much time has passed?*

[P7]
I checked the watch on my wrist. The cheap twelve-thousand-won digital watch I had bought from a street stall in front of the Hunter training center about seven years ago had the advantage of coming with an alarm and stopwatch function.

[P8]
Beep.

[P9]
[02:05:35]

[P10]
Two hours, five minutes, and thirty-five seconds.

[P11]
I had spent around twenty days in Murim, so the timing roughly matched what had happened last time.

[P12]
*Since I came to the modern world, the time ratio must have been reversed.*

[P13]
Now that I had logged out, ten days in the modern world amounted to one hour in Murim. I washed myself in the communal shower of the goshiwon[^1] and returned to my room.

[P14]
Just as I was about to close the door, a black shadow shot upward.

[P15]
“Wah!”

[P16]
Of course. It was Seong Jinho.

[P17]
“Oh. My. God. What a surprise.”

[P18]
“……What’s with that reaction? You knew I was here?”

[P19]
“Your inhaling and exhaling were extremely intense. Mr. Jinho, were you excited?”

[P20]
My five senses had grown sharper with each passing day. I could pick up every sound and movement around me without even using Qi Sense.

[P21]
He seemed to have been waiting in silence, but to my ears, every tiny movement and breath he made sounded like thunder.

[P22]
“Breathe a little more quietly. You’re supposedly the goshiwon manager, so it would be a problem if people filed complaints because your breathing was too loud.”

[P23]
“Damn it. How did you know? You’re just an F-rank Hunter…… Oh, right. You became C-rank a while ago.”

[P24]
“Look at the way you talk. Making fun of me for being F-rank has really become a habit.”

[P25]
“Hey, if you were my age, would you remember something that happened barely a week ago? I can’t even remember what side dishes I ate yesterday.”

[P26]
“A week?”

[P27]
Was that really all the time that had passed?

[P28]
To me, it had been well over a month. To Jinho-hyung, it had been barely a week. I felt a subtle sense of disconnect.

[P29]
“Hey. Why do you look like that? Is something wrong?”

[P30]
“What do you mean, something’s wrong? Anyway, what brings you here?”

[P31]
“Listen to the way you talk. Are we some kind of business relationship that we can only see each other when there’s business involved?”

[P32]
“Just get to the point. Keep it short.”

[P33]
Jinho-hyung’s face hardened. Had I gone too far with the teasing?

[P34]
Come to think of it, I had been too indifferent lately. Even before returning to Murim, I hadn’t been able to see him often because of all sorts of problems……

[P35]
“Buy me dinner.”

[P36]
“…….”

[P37]
“Grilled pork belly. Teppanyaki. Fried chicken and beer.”

[P38]
Shit. Of course.

[P39]
And he even had the nerve to choose the menu himself.

[P40]
“Did I leave money with you?”

[P41]
“Your money is my money. And my money is my money, isn’t it?”

[P42]
“Pronounce that properly. Unless you want to feel the fist of a C-rank Hunter.”

[P43]
Jinho-hyung flinched and rubbed his palms together.

[P44]
“Please, sir. Use your money to put some grease on my parched stomach.”

[P45]
“…….”

[P46]
Talk about changing his tune. Even Udyr would weep.

[P47]
It was absurd, but I let out a quiet laugh. My stomach had also been screaming after going nearly a month without a proper meal.

[P48]
*Let’s eat something decent for once.*

[P49]
I spoke in a solemn voice.

[P50]
“I approve of your attitude. Lead the way.”

[P51]
“Where would you like to go, sir?”

[P52]
“I’m tired of grilled pork belly and teppanyaki. Let’s go for something pricier today.”

[P53]
“Th-then, sir!”

[P54]
Jinho-hyung’s eyes widened.

[P55]
“Hanwoo![^2] The pasture-raised beef famous for its incredible marbling?”

[P56]
“What the hell are you talking about? We’re going out for gopchang.[^3]”

[P57]
“…….”

[P58]
“If you don’t like it, starve.”

[P59]
Thump.

[P60]
Jinho-hyung grabbed my shoulder and spoke with a solemn expression.

[P61]
“I’ve always wanted to eat that.”

[P62]
The early dinner that began at five that afternoon ended at a third-round makgeolli bar, and Jinho-hyung was completely plastered.

[P63]
“Krroooorr.”

[P64]
“…….”

[P65]
I had seen this scene somewhere before.

[P66]
As I felt a strange sense of déjà vu and hoisted Jinho-hyung onto my back, my phone rang.

[P67]
〈Designer-Brand Junkie

[P68]
**Designer-Brand Junkie**

[P69]
See you tomorrow at the same time, same place.

[P70]
It was a short text message. The sender was Team Leader Choi.

[P71]
* * *

[P72]
The downside—and upside—of Sleep Mode was that it reduced the amount of time I needed to sleep. Other than when I had suffered serious injuries fighting Jopil, I had never slept for more than three hours.

[P73]
*It’s useful for training.*

[P74]
Three in the morning.

[P75]
I woke up in peak condition and sat cross-legged. At some point, circulating my qi had become how I began and ended every day.

[P76]
Fwoosh.

[P77]
A wave of internal energy began to flow.

[P78]
The fifteen years of internal energy surging from my dantian cleansed the waste products accumulated inside my body and breathed vitality into dormant acupoints.

[P79]
Ding.

[P80]
> **System**
>
> - You have finished circulating your qi.
>
> - Your internal energy has increased very slightly.

[P81]
By the time I opened my eyes at the System notification, more than two hours had passed. If I were in Murim, I would have gone straight to the training yard to warm up, but the real world came with all sorts of restrictions.

[P82]
Especially in a goshiwon, where the rooms were packed together like a chicken farm.

[P83]
*Damn goshiwon. I need to get out of here soon.*

[P84]
This was an age when training was done with money, too. People who made good money had several spacious private training rooms, while people like me had no choice but to adapt to poor conditions.

[P85]
“Huff. Inhale.”

[P86]
I spent the entire morning running around the neighborhood, then continued with basic bodyweight exercises without taking a break after I returned. Maybe it was because my Stats had increased, but instead of getting tired, I felt more and more energized.

[P87]
Watching me, Jinho-hyung asked with a horrified look:

[P88]
“Don’t you get tired?”

[P89]
“Not really.”

[P90]
“I’ve never seen anyone do one-arm push-ups as easily as you. How many have you done?”

[P91]
“I don’t know. I counted to three hundred, then got too lazy to keep counting.”

[P92]
“You’re a monster. Is that normal for a C-rank Hunter?”

[P93]
“By the way, Seong Jinho.”

[P94]
“Huh?”

[P95]
“Why are you here?”

[P96]
Jinho-hyung had appeared ten minutes earlier with a haggard face, and he still hadn’t left my room.

[P97]
“Can’t you tell? I came to eat ramen.”

[P98]
Tap tap. Ssshhk.

[P99]
He naturally dropped a raw egg onto the noodles, which were almost cooked.

[P100]
His control of the burner flame to leave the egg perfectly runny was worthy of a Peak master.

[P101]
“Give me three reasons you have to stuff your face with that here.”

[P102]
“First, there’s no TV in my room. Second, there’s a TV in your room. Third, ramen tastes best when you eat it while watching TV.”

[P103]
The words poured out of him like a flowing stream, and my blood started boiling.

[P104]
“Just buy one! If you don’t have money, take mine!”

[P105]
“Ah, maybe not. I’m leaving soon anyway. Why bother adding to my luggage?”

[P106]
“Then stop coming in and out of here and bothering me…… Huh? What did you just say?”

[P107]
“What?”

[P108]
“No, wait. You’re leaving?”

[P109]
“Ah, that.”

[P110]
Jinho-hyung scratched his matted hair.

[P111]
“It just worked out that way. The date isn’t set yet, but I’m planning to move out soon. I can’t stay holed up here forever.”

[P112]
“…….”

[P113]
“Why are you looking at me like that?”

[P114]
“No, it’s nothing.”

[P115]
I awkwardly looked away.

[P116]
Who living in a goshiwon didn’t have a story of their own? I had mine, and Jinho-hyung had his. It would be rude to ask for the reason.

[P117]
*Still, it’s a shame.*

[P118]
He was someone I’d spent years with, like a friend and a brother. And now he was leaving so suddenly.

[P119]
Caught up in complicated feelings, I cautiously opened my mouth.

[P120]
“Hyung, by any chance……”

[P121]
“I know what you’re about to say, but I respectfully decline.”

[P122]
Had he realized what I was going to say? Jinho-hyung cut me off decisively and continued.

[P123]
“Kid, I’m thirty years old. I’ll fill my own bowl.”

[P124]
“Then there’s nothing I can do.”

[P125]
I had thought I could probably live with Jinho-hyung, but my premature meddling seemed to have pricked his pride.

[P126]
With a crumpled expression, he opened the lid of the pot.

[P127]
“You should’ve just said so from the start.”

[P128]
“What are you talking about? You weren’t even planning to.”

[P129]
“What nonsense. I only cooked one because you said you weren’t eating.”

[P130]
“……?”

[P131]
Wait a second. How had the conversation suddenly ended up here?

[P132]
After several seconds of silence, I finally spoke.

[P133]
“What are you talking about? What’s this about cooking something all of a sudden?”

[P134]
“Obviously, ramen.”

[P135]
Jinho-hyung glared at me with a threatening look.

[P136]
“There’s always someone who says he isn’t eating, then asks for a bite when you cook it well. How many times have I fallen for that one with you?”

[P137]
“…….”

[P138]
“So a C-rank Hunter reaches into his poor hyung’s bowl? Are you even human?”

[P139]
“…….”

[P140]
So when he had been talking about his bowl earlier, he had meant an actual bowl.

[P141]
I wanted to throw his own words right back at him.

[P142]
*Is that thing even human?*

[P143]
I was a fucking idiot for thinking I could live with someone like him.

[P144]
Feeling deeply ashamed of myself, I threw on some clothes. It was almost time to meet Team Leader Choi.

[P145]
Bang!

[P146]
I slammed the door hard enough to break it and left. One last shout rang out behind me.

[P147]
“If you’re going to the market, get some kimchi!”

[P148]
Ah, I wanted to kill him.

[P149]
* * *

[P150]
*Where was the place again?*

[P151]
I dredged up my memories from about twenty days ago and arrived at the meeting place.

[P152]
It was a large café in the heart of a forest of skyscrapers. A handsome man sitting by the window spotted me and waved.

[P153]
“Over here.”

[P154]
I didn’t need him to say anything. There were dozens of tables in the café, yet Team Leader Choi was the only customer sitting inside.

[P155]
*He’s still handsome.*

[P156]
Wearing a thin casual suit, Team Leader Choi looked as though he had just stepped out of a fashion shoot. A successful man in his twenties who had everything: looks, money, personality……

[P157]
No. Leave personality out of it.

[P158]
After exchanging a brief handshake, we sat down.

[P159]
“Have you eaten?”

[P160]
“No.”

[P161]
Team Leader Choi tilted his head.

[P162]
“Really? You look like you’ve eaten ramen.”

[P163]
“…….”

[P164]
Damn it. This guy’s nose was incredible.

[P165]
It was too embarrassing to explain the whole story about what had happened at the goshiwon, so I hurriedly changed the subject.

[P166]
“It’s lunchtime, but there’s no one here.”

[P167]
“We’re closed.”

[P168]
“What?”

[P169]
“The windows are covered with curtains, and there’s a ‘Closed’ sign on the door. Of course no one’s coming in.”

[P170]
I looked around. Just as Team Leader Choi had said, everything was covered up.

[P171]
I had assumed the café would naturally be open since it was the meeting place, so I hadn’t noticed. The whole situation was so strange that I blinked.

[P172]
“But you’re open right now.”

[P173]
The lights inside were bright, and the air-conditioning kept the place cool. I could glimpse at least ten employees, so why had they closed the door?

[P174]
Team Leader Choi answered calmly.

[P175]
“We have to. There’s a customer.”

[P176]
“You said you weren’t open.”

[P177]
“That’s up to the owner, isn’t it?”

[P178]
“Uh…… Team Leader, I’m asking just to be sure.”

[P179]
“You don’t need to ask. This café is mine.”

[P180]
Right. I had figured as much.

[P181]
Thinking back, the café had also been empty except for the two of us the last time we met.

[P182]
*I keep digging, and the hole never ends.*

[P183]
I clicked my tongue and said:

[P184]
“Team Leader, you have a lot of money.”

[P185]
“I have enough that I don’t need to worry about running short. That’s why I can put a contract like this in front of you.”

[P186]
Team Leader Choi smiled gently and handed me a folder.

[P187]
“Now, shall we talk business?”

[P188]
There was no reason to hesitate any longer. I nodded firmly.

[P189]
“Let’s.”

[P190]
An hour later, the System alert rang out just as I finished signing the last page.

[P191]
Ding.

[P192]
[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement, often with shared facilities.

[P193]
[^2]: Hanwoo is a Korean breed of native cattle whose beef is prized for its marbling.

[P194]
[^3]: Gopchang is a Korean dish made from grilled intestines, usually beef intestines.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 조필     | **Jopil**          |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 시스템              | **System**                     |
| 로그아웃             | **Logout**                     |
| 헌터      | **Hunter**            |
| 팀장      | **Team Leader**       |
| 성진호 | **Seong Jinho** |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 75,
  "passed": true,
  "metrics": {
    "source_characters": 5441,
    "translation_characters": 12212,
    "length_ratio": 2.244,
    "source_paragraphs": 191,
    "translation_paragraphs": 190
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "무인",
        "preferred": "martial artist"
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
        "korean": "화시",
        "preferred": "fire arrow"
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
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "곱창",
        "romanization": "gopchang"
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
