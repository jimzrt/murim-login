# Fidelity Gate — Chapter 99

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
  1|＃99화
  2|
  3|
  4|
  5|보안팀장이 한 통의 전화를 받은 것은 사우나를 막 끝마친 직후였다.
  6|
  7|- 팀장님. 접니다, 김권동.
  8|
  9|“어, 녹취록이랑 소견서 다 썼냐?”
 10|
 11|- 아뇨. 그게 아니라…….
 12|
 13|“이 자식이 진짜. 최고참이라고 편의 봐줬더니 정신 못 차리지? 당장 10분 안에 소견서 작성해서 보내.”
 14|
 15|- 아이 참, 그게 아니고요. 특이 사항 때문에 보고드리려고 전화한 겁니다.
 16|
 17|잠시 후, 보안팀장은 들고 있던 맥반석 계란을 툭 떨궜다.
 18|
 19|“USB를 갖고 있었다고?”
 20|
 21|- 네. 통화 상대가 누군지는 모르지만 물건 잘 갖고 있다면서, 본인도 슬쩍 꺼내서 확인했다고 합니다. 준수가 직접 봤다니까 확실합니다.
 22|
 23|“그, 그래서?”
 24|
 25|- 표적이 직접 보관 중이라는데…… 당장은 준수도 어떻게 할 방법이 없어서 보고드립니다.
 26|
 27|“준수, 준수는? 당장 바꿔 봐.”
 28|
 29|- 지금 패밀리어로 표적 감시 중이라 곤란할 것 같은데요.
 30|
 31|보안팀장은 입술을 질끈 깨물었다. 방금 보고받은 내용으로 머릿속은 뒤죽박죽이었다.
 32|
 33|‘전화 상대는 누구지? 표적의 정체는? USB 안에는 대체 뭐가 들어 있을까?’
 34|
 35|보안팀장의 본능이 꿈틀거리기 시작했다.
 36|
 37|“김권동이. 이거 길드장님께서 특별 지시 하신 거야. 알지? 내가 몇 번이나 말했잖아.”
 38|
 39|- 그거야 다들 알죠.
 40|
 41|“뭐 하나라도 건지면 다 같이 대박 나는 거라고. 나도 위로 올라가고, 너도 짬 먹을 만큼 먹었으니까 팀장 달아야 할 거 아냐.”
 42|
 43|- ……그게 제 맘처럼 되나요. 적어도 B급은 되어야 팀장 달아 주는 거 모르는 처지도 아니고.
 44|
 45|“내 생각에 이거 충분히 건수 된다. 진태경 그놈이 어디에서 굴러먹다 온 놈인지는 모르겠는데 그림 딱 나와. 우리 상동 길드 언급하면서 대화하는 내용만 들어 봐도 알잖아. 그치?”
 46|
 47|- 저도 좀 그렇게 생각하긴 했습니다.
 48|
 49|계획은 차질 없이 진행되는 중이며, 상동 길드는 아직 눈치채지 못했다. 그리고 물건은 잘 간수하고 있다.
 50|
 51|정체를 알 수 없는 상대와 진태경의 대화는 제삼자가 듣기에도 충분히 의미심장한 내용이었다.
 52|
 53|하물며 상동 길드의 보안팀이라면 말할 것도 없다.
 54|
 55|“그 USB가 핵심이야. 막말로 진태경이 소속된 평화 길드건, 어느 경쟁 길드건 간에 우리 길드 한번 엎으려고 수 쓰는 거면…….”
 56|
 57|- 그런 거면 진짜 특급 정보죠.
 58|
 59|보너스는 기본이고 승진은 옵션이다. 길드장의 눈에 든다면 무난하게 길드 임원까지 노려 볼 수 있다.
 60|
 61|지금 이 순간, 보안팀장은 길드장의 오른팔이 된 자신의 모습을 상상했고 김권동은 상동 길드 최초의 C급 팀장이 되는 꿈에 젖었다.
 62|
 63|“계속 주시해. 난 일단 윗선에 보고하고 진태경 통화 내역부터 조회할 테니까.”
 64|
 65|- 넵!
 66|
 67|“나 옷만 갈아입고 바로 간다. 아무리 늦어도 저녁 먹기 전에 표적이 어떤 놈이랑 통화했는지 뜰 테니까 그전까지 대책을 세워 보자고.”
 68|
 69|보안팀장이 탈의실로 달려가려던 그때였다.
 70|
 71|- 아, 팀장님. 그런데 한 가지 걱정되는 부분이…….
 72|
 73|“뭔데.”
 74|
 75|김권동의 목소리에서 불안함이 읽힌다. 그리고 불길한 예감은 빗나가지 않고 적중했다.
 76|
 77|- 홍우진이 있잖습니까.
 78|
 79|“아, 젠장.”
 80|
 81|실수다. 너무 흥분한 나머지 홍우진의 존재를 잠시 잊고 있었다. 보안팀장은 마음이 조급해졌다.
 82|
 83|‘그놈이 먼저 움직이면 곤란한데.’
 84|
 85|그가 아는 길드장, 임춘수는 상벌이 명확한 인물이었다.
 86|
 87|신입이어도 실력을 입증한다면 출셋길에 아스팔트를 깔아 주고, 아니다 싶으면 10년을 근무한 길드원이라도 망설임 없이 쳐 내는 성격.
 88|
 89|‘한두 번 본 게 아니지.’
 90|
 91|단순히 홍우진에게 공(公)만 뺏기고 끝날 리가 없다. 보안팀장 자신의 밥그릇이 달려 있다.
 92|
 93|돈? 그따위 문제가 아니다. 반평생을 몸담은 길드, 올라갈 수 있는 데까지는 가 보고 싶었다.
 94|
 95|“권동아.”
 96|
 97|- 예.
 98|
 99|“그놈, 지금 집에 혼자랬지?”
100|
101|- 팀장님, 설마? 안 됩니다!
102|
103|“아직 말 안 끝났다.”
104|
105|목소리가 커진 김권동과는 달리 보안팀장은 침착했다.
106|
107|“이 일, 표적 제압하고 물건 챙겨서 가면 깔끔하게 끝난다. 어차피 C급이야, 쫄 거 없어.”
108|
109|- 구린내가 풀풀 나는 C급이죠. 잘못 건드렸다가 저희가 역으로 당할 수도 있습니다.
110|
111|“당해? 이제 겨우 C급으로 각성한 풋내기한테 B급 베테랑인 내가? 이거 자존심 상하네.”
112|
113|- …….
114|
115|“너, 설마 임창수가 했던 말 믿는 건 아니지? 그게 사실이면 진태경이 사실은 A급 헌터라는 소린데…… 그럴 거면 차라리 길드장님이 첩자라고 해라. 응?”
116|
117|- 아니, 무슨 말씀을 그렇게까지 하세요.
118|
119|“됐고. 할 거야, 말 거야?”
120|
121|- 하, 씨. 미치겠네.
122|
123|깊은 한숨을 푹푹 내쉬던 김권동이 마음의 결정을 내린 것은 잠시 후였다.
124|
125|- 우리 이거 걸리면 범죄자 되는 겁니다. 아시죠?
126|
127|“알지. 안 걸리면 무죄라는 것도.”
128|
129|- 팀장님, 진짜 간도 크시네요.
130|
131|“그러니까 팀장이지. 애들은?”
132|
133|- 지금 다 모여 있습니다. CCTV 파악은 투입된 첫날에 끝냈고 간단한 변장 장비도 있어요.
134|
135|“좋아.”
136|
137|- 언제 시작합니까?
138|
139|보안팀장은 마른 입술을 핥았다.
140|
141|“내가 도착하는 즉시.”
142|
143|옛말에 이르기를 쇠뿔도 단김에 빼라고 했다. 그에게 있어 C급 헌터는 한 손으로도 뽑을 수 있을 만큼 물렁한 뿔이다.
144|
145|
146|
147|* * *
148|
149|
150|
151|낚시가 성공했다고 느낀 것은 얼마 지나지 않아서였다.
152|
153|야옹.
154|
155|미야옹.
156|
157|내 환심을 사기 위한 두 패밀리어의 애교 세례. 그러나 이번에는 좀 다르다.
158|
159|짧은 다리로 버둥버둥 소파에 올라오더니 다른 곳도 아닌 허벅지 위에 자리 잡는 모습을 보니 확신이 들었다.
160|
161|‘미끼를 물었구나.’
162|
163|주머니에 들어 있는 USB가 미끼다. 감시자들은 지금쯤 궁금해서 미칠 지경일 거다.
164|
165|내가 통화에서 말한 계획과 전화를 받은 상대방은 누군지, 이 USB에는 도대체 뭐가 들어 있는지.
166|
167|‘생각보다 과감한 놈들이었으면 좋겠는데.’
168|
169|그들이나 나나, 오래 끌어서 좋을 게 없다. 평일 오후, 아파트 단지는 한적했고 TV에서는 재미없는 귀농 다큐멘터리가 방영되고 있었다.
170|
171|“아, 오랜만에 뒷산이나 갈까…….”
172|
173|혼잣말을 중얼거리고 현관문을 나서려던 그때, 기다리던 변화가 일어났다.
174|
175|
176|
177|[Lv.2 고양이]
178|
179|[Lv.2 고양이]
180|
181|
182|
183|패밀리어 마법의 해제. 이 현상이 뜻하는 바는 명백했다.
184|
185|‘이제야 본격적으로 움직이는구나.’
186|
187|새끼 고양이의 몸으로는 내게서 USB를 훔칠 수 없다. 하지만 표적인 내가 직접 인적이 드문 곳으로 이동한다면 이야기가 달라진다.
188|
189|‘누가 봐도 고만고만한 C급 헌터, 마음 놓고 뺏을 수 있다고 생각하겠지.’
190|
191|물론 그 과정에 적당한 폭력과 협박도 포함되어 있을 거라는 건 충분히 예상할 수 있었다.
192|
193|단, 감시자들은 가장 중요한 한 가지를 착각했다.
194|
195|바로 나라는 존재다. 항상 가해자였던 그들은 자신들이 피해자가 될 수도 있을 거라는 생각을 하지 못한다.
196|
197|‘기대되네. 어떤 놈들일지.’
198|
199|허락 없이 불법 스토킹을 하면 어떻게 되는지 똑똑히 보여 줄 생각이다.
200|
201|
202|
203|* * *
204|
205|
206|
207|진태경이 부동산에서 얻은 정보는 절반만 맞았다. 상동 길드의 보안팀과는 달리 홍우진의 아지트는 그가 전혀 예상치 못한 곳에 있었다.
208|
209|바로 진태경이 사는 아파트 옥상이었다.
210|
211|“후우.”
212|
213|패밀리어와의 링크를 해제한 홍우진은 옥상에 딸린 자그마한 비품 창고에서 눈을 떴다.
214|
215|그는 경비원에게 약간의 돈을 찔러 주는 것으로 5평 남짓한 최적의 공간을 며칠간 마련할 수 있었다.
216|
217|“이거 일이 더럽게 꼬였네.”
218|
219|심상치 않은 진태경의 통화, 뭐가 담겼는지 모를 USB.
220|
221|드디어 정보라고 할 만한 걸 알아냈지만 그건 상동 길드 쪽도 마찬가지다.
222|
223|비품 창고에서 나온 그는 옥상 밑을 내려다봤다. 까마득한 저 아래, 막 아파트 입구를 나서는 진태경이 보였다.
224|
225|‘따라가야 하나, 말아야 하나.’
226|
227|의뢰를 생각한다면 따라가는 게 맞는데, 어쩐지 꺼림칙하다. 홍우진이 갈등하는 눈빛으로 멀어져 가는 진태경을 지켜보던 그때였다.
228|
229|“허, 이것 보게?”
230|
231|한 명, 그리고 다시 한 명. 슬금슬금 기어 나오는 꼴이 딱 먹이를 노리는 뱀의 그것과 다르지 않다.
232|
233|그 숫자가 도합 여섯.
234|
235|각자 복장도 다르고 행동거지도 일반인과 다름없지만 업계 동업자인 홍우진의 눈에는 똑똑히 보였다.
236|
237|“상동 길드 놈들이군.”
238|
239|한두 명도 아니고 자그마치 여섯이 몰려나왔다.
240|
241|더군다나 표적의 목적지는 인적이 드문 야산. 곧 벌어질 일을 짐작한 그가 미간을 찡그렸다.
242|
243|“가지가지 한다. 아주.”
244|
245|무력행사는 홍우진의 기준에서 벗어나는 일이다. 처음 의뢰를 맡을 당시 신신당부를 했음에도 보안팀을 투입시켰을 때 관뒀어야 했는데……. 이건 도를 지나쳤다.
246|
247|‘진태경, 저놈은 내 손으로 털고 싶었는데.’
248|
249|정체가 궁금해지는 놈이지만 딱 여기까지다. 더 이상 얽히면 안 될 것 같다는 예감이 들었다.
250|
251|‘상동 길드, 이 양아치 새끼들.’
252|
253|혀를 찬 홍우진이 스마트폰을 꺼내 문자를 발송했다.
254|
255|수신인은 1팀장. 문자 내용은 짧고 간략했다.
256|
257|
258|
259|〈 1팀장
260|
261|
262|
263|일 접습니다.
264|
265|
266|
267|옥상을 떠나기 전, 이미 사라진 진태경의 명복을 빌어 주는 것도 잊지 않았다.
268|
269|‘거, 더러웠고 다신 보지 말자.’
270|
271|그로서는 여러모로 재수 옴 붙은 의뢰였다.
272|
273|
274|
275|* * *
276|
277|
278|
279|묵묵히 산길을 올랐다. 이미 등산로를 벗어난 지 오래다.
280|
281|하지만 멈추지 않는다. 깊숙이, 더 깊숙이 계속해서 걸음을 옮길 뿐.
282|
283|그러던 어느 순간 너른 평지가 모습을 드러냈다. 무릎에 닿을 정도로 높이 자란 잡초가 무성한 그곳에서, 나는 천천히 돌아섰다.
284|
285|“아직도 산책 중이신가 봐요?”
286|
287|앞서 두 차례 마주친 바가 있는 중년인, 김권동은 말없이 얼굴을 굳혔다.
288|
289|“대답이 없으시네. 옆에 계신 분은 누구?”
290|
291|“친구.”
292|
293|김권동이 어디서나 찾아볼 수 있는 흔한 인상이라면 지금 대답한 이 남자는 정반대였다.
294|
295|조폭도 울고 갈 만큼 험악한 인상에 거구의 소유자. 그의 입술 사이로 걸걸한 음성이 흘러나왔다.
296|
297|“다 알면서 왜 여기까지 왔지?”
298|
299|“뒤에서 졸졸 따라오시길래. 어디까지 따라오나 본 거죠. 똥개 훈련이라고 생각하시면 편해요.”
300|
301|남자가 너털웃음을 터트렸다.
302|
303|“어린놈이 당돌하네. 몇 살이냐?”
304|
305|“역마살이요.”
306|
307|“매를 버는 재주가 있구나.”
308|
309|“칭찬 감사합니다, 최병일 씨.”
310|
311|남자, 최병일이 입을 다물었다. 그의 눈동자가 흔들렸다.
312|
313|“……어떻게 알았지?”
314|
315|“그거야 영업 비밀이죠. 그런데 김권동 씨랑 친구 맞아요? 외관상으로 봤을 때는 투샷이 영 아닌데.”
316|
317|이번에는 김권동이 당황할 차례다. 하지만 내 말은 아직 끝나지 않았다.
318|
319|“친구가 아니라 대답하기 곤란한가? 그럼 다른 네 분한테 물어볼게요. 박형진, 오규현, 이민철, 김준수 씨는 솔직하게 대답해 주셨으면 좋겠네요.”
320|
321|우우웅.
322|
323|허공이 일렁이더니 네 사람이 뚝 떨어져 내린다. 머리 위로 레벨창을 각자 달고 있는 그들은 귀신이라도 본 듯한 얼굴이었다.
324|
325|“다들 뭘 그렇게 놀라시나. 숨이라도 편하게 쉬시라고 배려해 드린 건데.”
326|
327|최병일이 이를 악물었다. 처음의 여유는 온데간데없고 초조함과 당황에 물든 얼굴이다.
328|
329|“이런 씨팔…… 너 뭐 하는 새끼야?”
330|
331|먼저 욕 박았으니까 어른 공경은 여기서 끝이다. 나는 최병일을 보며 피식 웃었다.
332|
333|“아직도 몰라? 내 정보 싹 긁었을 텐데. 패밀리어까지 붙여 놓을 정도면 말 다 한 거지.”
334|
335|“……!”
336|
337|“집에 나 혼자였으면 그러려니 했겠는데, 가족들까지 감시당할 거 생각하니까 좀 열받더라고. 그래서 미끼 한번 던져 봤더니 덥석 물데?”
338|
339|여섯 명의 감시자들이 몸을 부르르 떨었다.
340|
341|“그, 그럼 USB도?”
342|
343|“아, 그거? 내가 평생을 바쳐 모은 야동 컬렉션.”
344|
345|인벤토리에 소중히 보관해 놨던 인류의 보물이다.
346|
347|“말도 안 돼! 분명히 촉이 왔는데.”
348|
349|“음. 말도 안 되는 작품들이 수두룩하긴 하지. 남자라면 촉이 오는 것도 당연한 거고.”
350|
351|하나같이 망연자실한 얼굴로 서 있는 그들을 향해 말했다.
352|
353|“성실하게 대답해 줬으니까 나도 하나만 물어보자.”
354|
355|한 명, 한 명. 나와 눈이 마주칠 때마다 몸을 움찔거린다.
356|
357|마침내 내 시선이 멈춘 곳에는 빼빼 마른 20대 남성이 서 있었다. 아마도 이놈이 패밀리어 마법사겠지.
358|
359|
360|
361|[Lv.41 김준수]
362|
363|
364|
365|“준수야. 너희 상동 길드에서 보내서 왔지?”
366|
367|“입 닥쳐!”
368|
369|최병일이 외쳤지만 김준수는 이미 대답을 끝낸 후였다.
370|
371|핏기 하나 없이 창백해진 얼굴이 바로 그의 대답이다.
372|
373|“오케이, 상동 길드. 그럴 줄 알았다.”
374|
375|내 말을 들은 최병일의 얼굴이 딱딱하게 굳었다.
376|
377|“그 이름은 입에 담지 말았어야지.”
378|
379|“왜, 죽이게?”
380|
381|“……널 사로잡고 생각해 보지.”
382|
383|“그거 되게 힘들 텐데.”
384|
385|최병일의 레벨은 60대 중반. 느껴지는 기세는 임창수와 비등하고 나머지는 그저 그런 3, 40레벨 정도의 C급이었다.
386|
387|전문적인 레이드 팀도 아닌 이들이 나를 사로잡을 확률은 매우 희박하다.
388|
389|“죽을 각오로 덤벼. 그래야 내 손목에 나비매듭이라도 묶을 수 있지.”
390|
391|“쳐!”
392|
393|최병일의 외침과 함께 상동 길드의 감시자들이 사방에서 달려들기 시작한다.
394|
395|쉬이이익!
396|
397|어깨 위로 떨어지는 단검 한 자루가 시작이다.
398|
399|나는 느릿느릿하게만 보이는 그 궤적을 향해 손을 뻗었다.
400|
401|그와 동시에…….
402|
403|‘인벤토리 오픈. 장착.’
404|
405|콰직!
406|
407|공력을 한껏 머금은 검날이 적의 단검을 부쉈다. 이름 모를 잡초 위로 조각난 날붙이와 누군가의 핏물이 쏟아진다.
408|
409|“들어와, 이 스토커 새끼들아!”
410|
411|쐐애애액!
```

## Assembled English

```markdown
[P1]
# Chapter 99

[P2]
The Security Team Leader received a phone call just after finishing up at the sauna.

[P3]
“Team Leader, it’s me, Kim Gwondong.”

[P4]
“Yeah. You finish the transcript and assessment?”

[P5]
“No, sir. That’s not it…”

[P6]
“You little shit. I cut you some slack because you’re the most senior one there, and now you’re getting careless? Write up that assessment and send it to me within ten minutes.”

[P7]
“Come on, that’s not it. I’m calling to report something unusual.”

[P8]
A moment later, the Security Team Leader dropped the roasted egg he was holding.

[P9]
“He had a USB?”

[P10]
“Yes. We don’t know who he was talking to, but he said he was keeping the item safe, and he even slipped it out and checked it himself. Junsu saw it with his own eyes, so we’re certain.”

[P11]
“Th-then what?”

[P12]
“The target is keeping it on him, apparently… Junsu has no way to do anything about it for now, so I’m reporting it.”

[P13]
“Junsu—where’s Junsu? Put him on right now.”

[P14]
“He’s monitoring the target through his Familiar, so that might be difficult.”

[P15]
The Security Team Leader bit down hard on his lip. His head was a complete mess after hearing the report.

[P16]
*Who was on the other end of that call? Who is the target really? And what the hell is on that USB?*

[P17]
The Security Team Leader’s instincts began to stir.

[P18]
“Gwondong. This was a special order from the Guild Master. You know that, right? I’ve told you so many times.”

[P19]
“Everyone knows.”

[P20]
“If we manage to get even one thing out of this, we all hit the jackpot. I’ll move up, and you’ve put in enough years that you ought to make Team Leader yourself.”

[P21]
“…It’s not as simple as wishing for it. You know perfectly well they won’t make someone a Team Leader unless they’re at least B-rank.”

[P22]
“I think this is more than enough to make a real score. I don’t know where that Jin Taekyung bastard crawled out from, but the picture’s obvious. You can tell just by listening to him talk about our Sangdong Guild. Right?”

[P23]
“I was thinking the same thing.”

[P24]
The plan was proceeding without a hitch. Sangdong Guild still hadn’t noticed anything. And the item was being kept safe.

[P25]
The conversation between Jin Taekyung and the unidentified person on the other end of the line was meaningful enough even to a third party.

[P26]
To Sangdong Guild’s Security Team, it was unmistakably significant.

[P27]
“That USB is the key. To put it bluntly, whether it’s the Peace Guild Jin Taekyung belongs to or some rival Guild, if they’re making a move to bring down our Guild…”

[P28]
“Then that’s seriously high-value intel.”

[P29]
The bonus was a given, and promotion was an option. If he caught the Guild Master’s eye, he might even be able to aim for a position among the Guild executives.

[P30]
At that very moment, the Security Team Leader imagined himself as the Guild Master’s right-hand man, while Kim Gwondong became lost in a dream of becoming Sangdong Guild’s first C-rank Team Leader.

[P31]
“Keep watching him. I’ll report this up the chain and start by checking Jin Taekyung’s call records.”

[P32]
“Yes, sir!”

[P33]
“I’ll change and head over right away. We’ll know who the target spoke to by dinner at the latest, so let’s work out a plan before then.”

[P34]
The Security Team Leader was about to run to the changing room when Kim Gwondong spoke again.

[P35]
“Ah, Team Leader. There’s one thing I’m worried about…”

[P36]
“What?”

[P37]
Anxiety could be heard in Kim Gwondong’s voice. And his ominous premonition proved accurate.

[P38]
“There’s Hong Woojin.”

[P39]
“Ah, damn it.”

[P40]
It was a mistake. He had been so excited that he had briefly forgotten about Hong Woojin’s existence. The Security Team Leader grew impatient.

[P41]
*It’ll be a problem if that bastard moves first.*

[P42]
The Guild Master he knew, Im Chunsoo, was a man who made rewards and punishments absolutely clear.

[P43]
If a newcomer proved their ability, he would pave the road to advancement for them. But if he decided someone was no good, he would cut them loose without hesitation—even if they had been a Guild member for ten years.

[P44]
*I’ve seen it more than once or twice.*

[P45]
This wouldn’t end with Hong Woojin merely stealing the credit. The Security Team Leader’s own position was at stake.

[P46]
Money? That wasn’t the issue. He had devoted half his life to this Guild, and he wanted to see how high he could climb.

[P47]
“Gwondong.”

[P48]
“Yes.”

[P49]
“That bastard’s home alone right now, isn’t he?”

[P50]
“Team Leader, surely not? We can’t!”

[P51]
“I’m not finished.”

[P52]
Unlike Kim Gwondong, whose voice had grown loud, the Security Team Leader remained calm.

[P53]
“If we subdue the target, take the item, and leave, this ends cleanly. He’s only C-rank, after all. There’s nothing to be afraid of.”

[P54]
“He’s a C-rank who reeks of trouble. If we make the wrong move, we could be the ones who get taken down.”

[P55]
“Taken down? Me, a veteran B-rank, by some rookie who only just awakened as a C-rank? Now that hurts my pride.”

[P56]
“…”

[P57]
“You don’t actually believe what Im Changsoo said, do you? If that were true, it would mean Jin Taekyung was really an A-rank Hunter… If that’s the case, you might as well say the Guild Master is a spy. Huh?”

[P58]
“Come on, why take it that far?”

[P59]
“Enough. Are you in or not?”

[P60]
“Fuck, this is driving me crazy.”

[P61]
Kim Gwondong heaved several deep sighs. After a moment, he made his decision.

[P62]
“If we get caught, we’re criminals. You know that, right?”

[P63]
“I do. I also know we’re innocent if we don’t get caught.”

[P64]
“Team Leader, you’ve really got some nerve.”

[P65]
“That’s why I’m the Team Leader. What about the others?”

[P66]
“They’re all gathered right now. We mapped out the CCTV coverage on the first day we were deployed, and we have some simple disguise Equipment, too.”

[P67]
“Good.”

[P68]
“When do we start?”

[P69]
The Security Team Leader licked his dry lips.

[P70]
“The moment I arrive.”

[P71]
As the old saying went, you had to pull the ox’s horn while it was hot. To him, a C-rank Hunter was a soft horn he could yank out one-handed.

[P72]
* * *

[P73]
It didn’t take long for me to realize that the bait had worked.

[P74]
*Meow.*

[P75]
*Myaow.*

[P76]
The two Familiars showered me with affection, trying to win me over. But this time was different.

[P77]
They had struggled up onto the sofa with their short legs, then settled down—not just anywhere, but on my thighs.

[P78]
*They took the bait.*

[P79]
The USB in my pocket was the bait. By now, the watchers must have been dying of curiosity.

[P80]
What was the plan I’d mentioned on the phone? Who had I been talking to? And what the hell was on the USB?

[P81]
*I hope they’re more daring than I expect.*

[P82]
Neither they nor I stood to gain anything by dragging this out. It was a weekday afternoon, the apartment complex was quiet, and the TV was showing a boring documentary about moving to the countryside to become a farmer.

[P83]
“Ah, maybe I should visit the hill out back for the first time in a while…”

[P84]
I muttered to myself and was about to step through the front door when the change I had been waiting for finally came.

[P85]
> **System**
>
> Level 2 Cat
>
> Level 2 Cat

[P86]
The Familiar magic had been dispelled. The meaning was obvious.

[P87]
*They’re finally making their move.*

[P88]
In a kitten’s body, they couldn’t steal the USB from me. But if I, their target, went somewhere secluded on my own, that changed things.

[P89]
*Anyone looking at me would see some middling C-rank Hunter. They’d think they could take it without worry.*

[P90]
Of course, I fully expected a certain amount of violence and intimidation in the process.

[P91]
But the watchers had gotten one crucial thing wrong.

[P92]
Me.

[P93]
They had always been the perpetrators. It had never occurred to them that they might become the victims.

[P94]
*I’m looking forward to this. What kind of bastards are they?*

[P95]
I was going to show them exactly what happened when they stalked someone illegally and without permission.

[P96]
* * *

[P97]
The information Jin Taekyung had obtained from the real-estate office was only half right. Unlike Sangdong Guild’s Security Team, Hong Woojin’s hideout was somewhere Taekyung had never expected.

[P98]
The rooftop of the apartment building where Jin Taekyung lived.

[P99]
“Whew.”

[P100]
After severing his Link with the Familiar, Hong Woojin opened his eyes inside the tiny supply closet attached to the rooftop.

[P101]
By slipping the security guard a little money, he had secured the ideal space—roughly five pyeong[^1]—for several days.

[P102]
“This job got horribly tangled up.”

[P103]
Jin Taekyung’s suspicious phone call. A USB with unknown contents.

[P104]
He had finally uncovered something worthy of being called intelligence, but Sangdong Guild had discovered it too.

[P105]
Hong Woojin stepped out of the supply closet and looked down from the rooftop. Far below, he could see Jin Taekyung just leaving the apartment entrance.

[P106]
*Should I follow him or not?*

[P107]
Considering the job, he should. But something about this felt wrong.

[P108]
Hong Woojin was watching Jin Taekyung recede into the distance, his eyes conflicted, when—

[P109]
“Well, look at this.”

[P110]
One person, then another. The way they slowly crawled out was no different from snakes stalking their prey.

[P111]
Six of them in total.

[P112]
Each wore different clothes and behaved like an ordinary civilian, but Hong Woojin was in the same line of work. He saw them for what they were.

[P113]
“Sangdong Guild bastards.”

[P114]
Not one or two, but six of them had come out.

[P115]
What was more, the target’s destination was a deserted hillside. Realizing what was about to happen, Hong Woojin furrowed his brow.

[P116]
“They’re really pulling every dirty trick in the book.”

[P117]
Using force crossed Hong Woojin’s line. He should have quit when they deployed the Security Team, despite his repeated warnings when he first accepted the job. But this had gone too far.

[P118]
*I wanted to uncover Jin Taekyung’s secrets myself.*

[P119]
He was a man whose identity had made Hong Woojin curious, but this was where it ended. He had a feeling that he shouldn’t get involved any further.

[P120]
*Sangdong Guild, you goddamn thugs.*

[P121]
Clicking his tongue, Hong Woojin pulled out his smartphone and sent a text.

[P122]
The recipient was the Team 1 Leader. The message was short and simple.

[P123]
> **Team 1 Leader**
>
> I’m dropping the job.

[P124]
Before leaving the rooftop, he didn’t forget to pray for the already-vanished Jin Taekyung’s soul.

[P125]
*Well, that was filthy. Let’s never see each other again.*

[P126]
In every possible way, the job had brought him nothing but bad luck.

[P127]
* * *

[P128]
I climbed the mountain path in silence. I had left the hiking trail behind long ago.

[P129]
But I didn’t stop. I kept walking deeper and deeper into the mountain.

[P130]
At some point, a broad clearing came into view. Weeds had grown thick there, reaching up to my knees. I slowly turned around.

[P131]
“Looks like you’re still out for a walk?”

[P132]
Kim Gwondong, the middle-aged man I had run into twice before, said nothing. His face hardened.

[P133]
“No answer? Who’s the man beside you?”

[P134]
“A friend.”

[P135]
If Kim Gwondong had the sort of ordinary face you could see anywhere, the man who answered was his complete opposite.

[P136]
He was huge, with a vicious face fierce enough to make gangsters cry. A gravelly voice rumbled from between his lips.

[P137]
“You already know everything, so why did you come all the way here?”

[P138]
“You kept trailing me from behind, so I wanted to see how far you’d follow. Think of it as training a mutt.”

[P139]
The man burst into a hearty laugh.

[P140]
“Young punk’s got nerve. How old are you?”

[P141]
“*Yeokmasal*.”[^2]

[P142]
“You’ve got a real talent for asking for a beating.”

[P143]
“Thanks for the compliment, Mr. Choi Byungil.”

[P144]
The man, Choi Byungil, closed his mouth. His eyes wavered.

[P145]
“…How did you know?”

[P146]
“That’s a trade secret. But are you and Mr. Kim Gwondong really friends? Judging by appearances, you two don’t exactly look like a matching pair.”

[P147]
This time, it was Kim Gwondong’s turn to panic. But I wasn’t finished.

[P148]
“Is that hard to answer because you’re not friends? Then I’ll ask the other four. Mr. Park Hyungjin, Mr. Oh Gyuhyeon, Mr. Lee Mincheol, and Mr. Kim Junsu, I’d appreciate an honest answer.”

[P149]
Bzzzzzz.

[P150]
The air rippled, and four people dropped straight down.

[P151]
Each had a Level window floating above his head, and all four looked like they’d seen a ghost.

[P152]
“Why is everyone so surprised? I was just being considerate so you could breathe easy.”

[P153]
Choi Byungil gritted his teeth. All traces of his earlier composure had vanished, leaving his face colored by anxiety and bewilderment.

[P154]
“What the fuck… What kind of bastard are you?”

[P155]
He had cursed first, so that was the end of respecting my elders. I gave a quiet laugh as I looked at Choi Byungil.

[P156]
“You still don’t know? You must have dug up every scrap of information about me. If you went so far as to attach Familiars, that says everything.”

[P157]
“…!”

[P158]
“I could’ve let it go if I’d been alone at home. But the thought of my family being watched too pissed me off. So I threw out some bait, and you snapped it right up.”

[P159]
The six watchers trembled.

[P160]
“Th-then the USB…”

[P161]
“Oh, that? It’s the porn collection I’ve spent my whole life assembling.”

[P162]
A treasure of humanity, carefully preserved in my Inventory.

[P163]
“No way! I definitely had a feeling!”

[P164]
“Well, there are plenty of works in there that defy belief. And any man would get a gut feeling about it.”

[P165]
I addressed the six of them as they stood there looking utterly crushed.

[P166]
“You answered honestly, so let me ask you one thing, too.”

[P167]
One by one, they flinched whenever their eyes met mine.

[P168]
At last, my gaze settled on a painfully skinny man in his twenties. He was probably the Familiar mage.

[P169]
> **System**
>
> Level 41 Kim Junsu

[P170]
“Junsu. Sangdong Guild sent you, didn’t they?”

[P171]
“Shut your mouth!”

[P172]
Choi Byungil shouted, but Kim Junsu had already answered.

[P173]
His bloodless, ashen face was answer enough.

[P174]
“Okay, Sangdong Guild. I figured as much.”

[P175]
Choi Byungil’s face stiffened at my words.

[P176]
“You shouldn’t have said that name out loud.”

[P177]
“Why? You going to kill me?”

[P178]
“…I’ll capture you first. Then I’ll think about it.”

[P179]
“That’s going to be pretty hard.”

[P180]
Choi Byungil’s Level was in the mid-sixties. His aura was comparable to Im Changsoo’s, while the rest were unremarkable C-ranks around Levels 30 or 40.

[P181]
The odds of a group that wasn’t even a professional raid team managing to capture me were extremely low.

[P182]
“Come at me prepared to die. That’s the only way you’ll manage to tie so much as a butterfly knot around my wrist.”

[P183]
“Get him!”

[P184]
At Choi Byungil’s shout, the Sangdong Guild watchers began charging at me from all directions.

[P185]
Whoosh!

[P186]
The opening move was a dagger dropping toward my shoulder.

[P187]
I reached toward the trajectory that looked slow to me.

[P188]
At the same time…

[P189]
*Inventory open. Equip.*

[P190]
Crunch!

[P191]
The blade, brimming with internal energy, shattered the enemy’s dagger. Shards of metal and someone’s blood spilled across the nameless weeds.

[P192]
“Come on, you stalker bastards!”

[P193]
Ssshhhhh!

[P194]
[^1]: *Pyeong* is a traditional Korean unit of floor area; five pyeong is roughly 16.5 square meters.

[P195]
[^2]: *Yeokmasal* is a traditional Korean notion of a fate that compels someone to wander. Here it also puns on *sal*, the Korean word used when asking someone’s age.
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
# Chapter 99

[P2]
The Security Team Leader received a phone call just after finishing up at the sauna.

[P3]
“Team Leader. It’s me, Kim Gwondong.”

[P4]
“Oh, did you finish writing the transcript and assessment?”

[P5]
“No, sir. That’s not it…”

[P6]
“You little shit. I went easy on you because you’re the most senior one here, and now you’re getting careless? Write up your assessment and send it to me within ten minutes.”

[P7]
“Come on, that’s not it. I’m calling to report something unusual.”

[P8]
A moment later, the Security Team Leader dropped the roasted egg he was holding.

[P9]
“He had a USB?”

[P10]
“Yes. We don’t know who he was talking to, but he said he was keeping the item safe, and he even slipped it out to check it himself. Junsu saw it directly, so it’s certain.”

[P11]
“Th-then?”

[P12]
“The target is keeping it on him, apparently… Junsu has no way to do anything about it for now, so I’m reporting it.”

[P13]
“Junsu? Put Junsu on right now.”

[P14]
“He’s watching the target with his Familiar, so that might be difficult.”

[P15]
The Security Team Leader bit down hard on his lip. His head was a complete mess after hearing the report.

[P16]
*Who was the person on the phone? What was the target’s true identity? And what on earth is inside that USB?*

[P17]
The Security Team Leader’s instincts began to stir.

[P18]
“Gwondong. This was a special order from the Guild Master. You know that, right? I’ve told you so many times.”

[P19]
“Everyone knows that.”

[P20]
“If we manage to get even one thing out of this, we all hit the jackpot. I’ll move up, and you’ve been around long enough that you ought to become a Team Leader, too.”

[P21]
“…It’s not as simple as wishing for it. You know perfectly well they won’t make someone a Team Leader unless they’re at least B-rank.”

[P22]
“I think this is more than enough to make a real score. I don’t know where that Jin Taekyung bastard came from, but the picture is obvious. You can tell just by listening to him talk about our Sangdong Guild. Right?”

[P23]
“I did think it looked that way.”

[P24]
The plan was proceeding without a hitch. Sangdong Guild still hadn’t noticed anything. And he was keeping the item safe.

[P25]
The conversation between Jin Taekyung and the unknown person on the other end of the line was suspicious enough to sound meaningful even to a third party.

[P26]
For Sangdong Guild’s Security Team, there was no question.

[P27]
“That USB is the key. To put it bluntly, whether it’s the Peace Guild Jin Taekyung belongs to or some rival Guild, if they’re making a move to bring down our Guild…”

[P28]
“Then that’s seriously high-value intel.”

[P29]
The bonus was a given, and promotion was an option. If he caught the Guild Master’s eye, he might even be able to aim for a position among the Guild executives.

[P30]
At that very moment, the Security Team Leader imagined himself as the Guild Master’s right-hand man, while Kim Gwondong became lost in a dream of becoming Sangdong Guild’s first C-rank Team Leader.

[P31]
“Keep watching him. I’ll report this up the chain and start by checking Jin Taekyung’s call records.”

[P32]
“Yes, sir!”

[P33]
“I’ll change clothes and head over immediately. No matter how late it is, we’ll know who the target spoke with before dinner. Let’s come up with a plan before then.”

[P34]
Just as the Security Team Leader was about to hurry to the changing room, Kim Gwondong spoke again.

[P35]
“Ah, Team Leader. There’s one thing I’m worried about…”

[P36]
“What is it?”

[P37]
Anxiety could be heard in Kim Gwondong’s voice. And his ominous premonition proved accurate.

[P38]
“You know Hong Woojin, right?”

[P39]
“Ah, damn it.”

[P40]
It was a mistake. He had been so excited that he had briefly forgotten about Hong Woojin’s existence. The Security Team Leader grew impatient.

[P41]
*It’ll be a problem if that bastard makes the first move.*

[P42]
The Guild Master he knew, Im Chunsoo, was a man who made rewards and punishments absolutely clear.

[P43]
If a newcomer proved their ability, he would pave the road to advancement for them. But if he decided someone was no good, he would cut them loose without hesitation—even if they had been a Guild member for ten years.

[P44]
*I’ve seen it more than once or twice.*

[P45]
This wouldn’t simply end with Hong Woojin taking the credit. The Security Team Leader’s own livelihood was on the line.

[P46]
Money? That wasn’t the issue. He had devoted half his life to this Guild and wanted to climb as high as he possibly could.

[P47]
“Gwondong.”

[P48]
“Yes.”

[P49]
“That bastard is alone at home right now, isn’t he?”

[P50]
“Team Leader, surely not? You can’t!”

[P51]
“I’m not finished talking.”

[P52]
Unlike Kim Gwondong, whose voice had grown loud, the Security Team Leader remained calm.

[P53]
“If we subdue the target, take the item, and leave, this ends cleanly. He’s only C-rank, after all. There’s nothing to be afraid of.”

[P54]
“He’s a C-rank who reeks to high heaven. If we make the wrong move, we could be the ones getting taken down.”

[P55]
“Taken down? By a rookie who only just awakened as a C-rank? Me, a B-rank veteran? That’s insulting.”

[P56]
“…”

[P57]
“You don’t actually believe what Im Changsoo said, do you? If that were true, it would mean Jin Taekyung was really an A-rank Hunter… If that’s the case, you might as well say the Guild Master is a spy. Huh?”

[P58]
“Come on, why are you taking it that far?”

[P59]
“Enough. Are you doing it or not?”

[P60]
“Fuck, this is driving me crazy.”

[P61]
Kim Gwondong let out several deep sighs before finally making up his mind.

[P62]
“If we get caught, we become criminals. You know that, right?”

[P63]
“I know. I also know that if we don’t get caught, we’re innocent.”

[P64]
“Team Leader, you really have some nerve.”

[P65]
“That’s why I’m the Team Leader. What about the others?”

[P66]
“They’re all gathered right now. We finished checking the CCTV on the first day we were deployed, and we have some simple disguise Equipment, too.”

[P67]
“Good.”

[P68]
“When do we start?”

[P69]
The Security Team Leader licked his dry lips.

[P70]
“The moment I arrive.”

[P71]
As the old saying went, you had to pull the ox’s horn while it was hot. To him, a C-rank Hunter was a soft horn he could yank out one-handed.

[P72]
* * *

[P73]
It didn’t take long for me to realize that the bait had worked.

[P74]
*Meow.*

[P75]
*Myaow.*

[P76]
The two Familiars showered me with affection, trying to win my favor. But this time, something was different.

[P77]
They had struggled up onto the sofa with their short legs, then settled down—not just anywhere, but on my thighs.

[P78]
*They took the bait.*

[P79]
The USB in my pocket was the bait. By now, the watchers must have been going crazy with curiosity.

[P80]
What plan I had mentioned during the call, who I had been speaking to, and what on earth was inside the USB.

[P81]
*I hope they’re more daring than I expect.*

[P82]
Neither they nor I had anything to gain by dragging this out. It was a weekday afternoon, the apartment complex was quiet, and the TV was showing a boring documentary about returning to farming.

[P83]
“Ah, should I go to the hill behind the apartment for the first time in a while…?”

[P84]
I muttered to myself and was about to leave through the front door when the change I had been waiting for occurred.

[P85]
> **System**
>
> Level 2 Cat
>
> Level 2 Cat

[P86]
The Familiar magic had been dispelled. The meaning of this phenomenon was obvious.

[P87]
*They’re finally making their move.*

[P88]
In the body of a kitten, they couldn’t steal the USB from me. But if I, the target, moved somewhere sparsely populated on my own, that would change things.

[P89]
*Anyone looking at me would see an ordinary C-rank Hunter. They’d think they could take it from me without worry.*

[P90]
Of course, it wasn’t hard to predict that a suitable amount of violence and threats would be part of the process.

[P91]
But the watchers had made one crucial mistake.

[P92]
What they had misjudged was me. They had always been the perpetrators, and had never imagined that they could become the victims.

[P93]
*I’m looking forward to this. What kind of bastards are they?*

[P94]
I intended to show them exactly what happened when someone illegally stalked another person without permission.

[P95]
* * *

[P96]
The information Jin Taekyung had obtained from the real-estate office was only half right. Unlike Sangdong Guild’s Security Team, Hong Woojin’s hideout was in a place Taekyung had never expected.

[P97]
The rooftop of the apartment building where Jin Taekyung lived.

[P98]
“Whew.”

[P99]
After severing his Link with the Familiar, Hong Woojin opened his eyes inside the tiny supply closet attached to the rooftop.

[P100]
By slipping the security guard a little money, he had secured this optimal space of roughly five pyeong[^1] for several days.

[P101]
“This job got horribly tangled up.”

[P102]
Jin Taekyung’s suspicious phone call. A USB whose contents were unknown.

[P103]
He had finally discovered something that could be called information, but Sangdong Guild had discovered the same thing.

[P104]
Hong Woojin stepped out of the supply closet and looked down over the edge of the roof. Far below, he could see Jin Taekyung just leaving the apartment entrance.

[P105]
*Should I follow him or not?*

[P106]
If he thought about the job, following him was the right choice. But something about it felt wrong. Hong Woojin was watching Jin Taekyung grow smaller in the distance with a conflicted look in his eyes when—

[P107]
“Huh. What do we have here?”

[P108]
One person, then another. The way they slowly crawled out was no different from snakes stalking their prey.

[P109]
There were six of them in total.

[P110]
Their clothes were all different, and their behavior was no different from ordinary people’s. But to Hong Woojin, a fellow professional in the industry, it was obvious.

[P111]
“They’re from Sangdong Guild.”

[P112]
Not one or two of them—six had emerged.

[P113]
What was more, the target’s destination was a deserted hillside. Realizing what was about to happen, Hong Woojin furrowed his brow.

[P114]
“They really pull every dirty trick in the book.”

[P115]
Using force crossed Hong Woojin’s line. He should have quit when they deployed the Security Team, despite his repeated warnings when he first accepted the job. But this had gone too far.

[P116]
*I wanted to uncover Jin Taekyung’s secrets myself.*

[P117]
He was a man whose identity had made Hong Woojin curious, but this was where it ended. He had a feeling that he shouldn’t get involved any further.

[P118]
*Sangdong Guild, you goddamn thugs.*

[P119]
Clicking his tongue, Hong Woojin took out his smartphone and sent a text.

[P120]
The recipient was the Team 1 Leader. The message was short and simple.

[P121]
> **Team 1 Leader**
>
> I’m dropping the job.

[P122]
Before leaving the rooftop, he also remembered to wish the already-vanished Jin Taekyung a peaceful rest.

[P123]
*Well, that was filthy. Let’s never see each other again.*

[P124]
In every respect, it had been a cursed job.

[P125]
* * *

[P126]
I climbed the mountain path in silence. It had been a long time since I’d left the hiking trail behind.

[P127]
But I didn’t stop. I kept walking deeper and deeper into the mountain.

[P128]
At some point, a broad clearing came into view. Weeds had grown thick there, reaching up to my knees. I slowly turned around.

[P129]
“Looks like you’re still out for a walk?”

[P130]
Kim Gwondong, the middle-aged man I had run into twice before, said nothing. His face hardened.

[P131]
“No answer? Who’s the person with you?”

[P132]
“My friend.”

[P133]
If Kim Gwondong had an ordinary, forgettable face, the man who answered me was the complete opposite.

[P134]
He was huge, with a vicious expression fierce enough to make gangsters cry. A rough voice rumbled from between his lips.

[P135]
“You already know everything, so why did you come all the way here?”

[P136]
“You kept trailing me from behind, so I wanted to see how far you’d follow. Think of it as training a mutt.”

[P137]
The man let out a hearty laugh.

[P138]
“Young punk’s got nerve. How old are you?”

[P139]
“*Yeokmasal*.”[^2]

[P140]
“You’ve got a real talent for earning a beating.”

[P141]
“Thanks for the compliment, Mr. Choi Byungil.”

[P142]
The man, Choi Byungil, closed his mouth. His eyes shook.

[P143]
“…How did you know?”

[P144]
“That’s a trade secret. But are you and Mr. Kim Gwondong really friends? Judging by appearances, you two don’t exactly look like a matching pair.”

[P145]
This time, it was Kim Gwondong’s turn to panic. But I wasn’t finished.

[P146]
“Is it difficult to answer because you’re not friends? Then I’ll ask the other four. Mr. Park Hyungjin, Mr. Oh Gyuhyeon, Mr. Lee Mincheol, and Mr. Kim Junsu, I’d appreciate an honest answer.”

[P147]
Bzzzzzz.

[P148]
The air rippled, and four people dropped straight down.

[P149]
Each of them had a Level window floating over their head, and their faces looked as if they had seen a ghost.

[P150]
“Why is everyone so surprised? I was just being considerate so you could breathe comfortably.”

[P151]
Choi Byungil gritted his teeth. All traces of his earlier composure had vanished, leaving his face colored by anxiety and bewilderment.

[P152]
“What the fuck… What kind of bastard are you?”

[P153]
Since he had started with profanity, my respect for my elders ended there. I let out a quiet laugh as I looked at Choi Byungil.

[P154]
“You still don’t know? You must have dug up every scrap of information about me. If you went so far as to attach Familiars, that says everything.”

[P155]
“…”

[P156]
“I could’ve let it go if I’d been alone at home. But the thought of my family being watched pissed me off. So I threw out some bait, and you snapped it up.”

[P157]
The six watchers trembled.

[P158]
“Th-then what about the USB?”

[P159]
“Oh, that? It’s my collection of porn I’ve spent my whole life putting together.”

[P160]
It was a treasure of humanity that I had carefully stored in my Inventory.

[P161]
“No way! I definitely had a feeling!”

[P162]
“Well, there are plenty of works in there that defy belief. And any man would get a gut feeling about it.”

[P163]
I looked at them, standing there with faces full of despair.

[P164]
“You answered honestly, so let me ask you one thing, too.”

[P165]
One by one, they flinched whenever their eyes met mine.

[P166]
At last, my gaze stopped on a painfully thin man in his twenties. He was probably the Familiar mage.

[P167]
> **System**
>
> Level 41 Kim Junsu

[P168]
“Junsu. You were sent here by Sangdong Guild, weren’t you?”

[P169]
“Shut your mouth!”

[P170]
Choi Byungil shouted, but Kim Junsu had already answered.

[P171]
His face had gone completely pale. That was answer enough.

[P172]
“Okay, Sangdong Guild. I figured as much.”

[P173]
Choi Byungil’s face stiffened at my words.

[P174]
“You shouldn’t have said that name out loud.”

[P175]
“What, you’re going to kill me?”

[P176]
“…I’ll capture you first and think about it.”

[P177]
“That’ll be pretty hard.”

[P178]
Choi Byungil’s Level was in the mid-sixties. His aura was comparable to Im Changsoo’s, while the others were ordinary C-ranks around Levels 30 or 40.

[P179]
The odds of a group that wasn’t even a professional raid team managing to capture me were extremely low.

[P180]
“Come at me prepared to die. That’s the only way you’ll manage to tie even a butterfly knot around my wrist.”

[P181]
“Get him!”

[P182]
At Choi Byungil’s shout, the Sangdong Guild watchers began charging at me from all directions.

[P183]
Whoosh!

[P184]
A dagger dropping toward my shoulder was the opening move.

[P185]
I reached toward the trajectory that looked slow to me.

[P186]
At the same time…

[P187]
*Inventory open. Equip.*

[P188]
Crunch!

[P189]
A blade brimming with internal energy shattered the enemy’s dagger. Broken metal and someone’s blood spilled across the nameless weeds.

[P190]
“Come on, you stalker bastards!”

[P191]
Ssshhhhh!

[P192]
[^1]: *Pyeong* is a traditional Korean unit of floor area; five pyeong is roughly 16.5 square meters.

[P193]
[^2]: *Yeokmasal* is a traditional Korean notion of a fate that compels someone to wander. Here it also puns on *sal*, the Korean word used when asking someone’s age.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 진태경    | **Jin Taekyung**   |
| 임춘수    | **Im Chunsoo**    |
| 임창수    | **Im Changsoo**   |
| 홍우진    | **Hong Woojin**   |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 레벨               | **Level**                      |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 최병일 | **Choi Byungil** | B-rank Security Team leader; his Level is in the mid-sixties. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 평화 | **Peace Guild** | Guild name. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 박형진 | **Park Hyungjin** | One of the C-rank Sangdong Guild watchers. |
| 오규현 | **Oh Gyuhyeon** | One of the C-rank Sangdong Guild watchers. |
| 이민철 | **Lee Mincheol** | One of the C-rank Sangdong Guild watchers. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 99,
  "passed": true,
  "metrics": {
    "source_characters": 6528,
    "translation_characters": 14816,
    "length_ratio": 2.27,
    "source_paragraphs": 192,
    "translation_paragraphs": 195
  },
  "errors": [],
  "warnings": [
    {
      "code": "numbers",
      "message": "Arabic numerals from the source are absent",
      "details": {
        "values": [
          "3"
        ]
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
        "korean": "진태",
        "preferred": "Jintae"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "나비",
        "preferred": "Nabi"
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
