# Fidelity Gate — Chapter 135

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
  1|＃135화
  2|
  3|
  4|
  5|쫙!
  6|
  7|“도, 도와주시오!”
  8|
  9|“너 도와줄 사람 없다.”
 10|
 11|쫙쫙!
 12|
 13|“사, 살려 주시오!”
 14|
 15|“싫어, 안 돼. 돌아가.”
 16|
 17|쫙쫙쫙!
 18|
 19|“차, 차라리 죽여…….”
 20|
 21|“아냐, 너 아직 괜찮아. 주둥이에서 말이 나오고 있잖아.”
 22|
 23|쫙쫙쫙쫙!
 24|
 25|“흐윽, 흐그으윽.”
 26|
 27|“그래, 바로 이 반응이지.”
 28|
 29|나는 그제야 비로소 손을 멈췄다.
 30|
 31|그럭저럭 봐줄 만했던 귀공자의 얼굴은 찐빵처럼 부풀었고, 양 뺨에는 발그레한 홍조 대신 검푸른 멍이 새겨져 있었다.
 32|
 33|“우리 진태. 잘못했어, 안 했어.”
 34|
 35|“흐그윽.”
 36|
 37|엉망이 된 몰골로 흐느끼는 녀석을 보니 문득 안쓰럽다는 생각이 들었다.
 38|
 39|그래, 얘도 남의 집 귀한 아들인데…….
 40|
 41|“잘못했지?”
 42|
 43|“흐극, 흐그그극!”
 44|
 45|“그러니까 왜 사람 말을 무시해. 사과하라고 했을 때 바로 사과했으면 얼마나 좋아. 안 그래?”
 46|
 47|“흐으으.”
 48|
 49|“앞으로 착하게 살자. 알겠지?”
 50|
 51|“흐그극.”
 52|
 53|나는 맹렬하게 고개를 끄덕이는 우진태를 가만히 바라보다가 입을 열었다.
 54|
 55|“그런데 너…….”
 56|
 57|“흐으?”
 58|
 59|“아까부터 대답이 왜 그따위야? 사람 말 못 해?”
 60|
 61|순간 녀석의 흐느낌이 뚝 멎었다.
 62|
 63|“죄, 죄송합니다.”
 64|
 65|“할 수 있네? 할 수 있는데 안 한 거네? 왜 운 거야? 내가 이 정도로 아프고 힘들다. 뭐 그런 거 티 내는 거야?”
 66|
 67|“아닙니다!”
 68|
 69|“이젠 목소리도 커지네? 성량 좋다, 너. 복식 호흡 연습해? 내 고막을 터트려서 이 위기를 모면해 보겠다, 이거야?”
 70|
 71|“아닙니다. 정말 아닙니다. 제발 이제 그만해 주십시오, 흐흐흑…….”
 72|
 73|“어? 또 우네? 지금 울음이 나와? 네가 뭐 잘했다고 울어. 울면 인생이 끝나? 그리고 그만해 달라니. 누가 보면 내가 가해자인 줄 알겠다?”
 74|
 75|“죄송합니다. 안 울겠습니다.”
 76|
 77|“와, 바로 울음 그치는 것 봐. 소름 돋는 놈이네, 이거. 내가 너였으면 죄 없는 사람 건드렸다는 죄책감에 울다 지쳐서 실신했을 텐데. 너 정말 미안하긴 해?”
 78|
 79|“자, 잠시만. 잠시만 제 얘기를 들어 주시면…….”
 80|
 81|“듣긴 뭘 들어. 네가 말할 자격이나 있어? 여기가 무슨 연예 대상 시상식이야? 너 말하는 동안 나는 잠자코 기다리다가 훈훈하게 웃으면서 박수 쳐 주면 돼?”
 82|
 83|“…….”
 84|
 85|“이제는 대답도 안 하네. 넌 밥 안 먹어도 배부르겠다. 그치? 지금처럼 남의 말 아작아작 씹어 먹으면 기분 좋…….”
 86|
 87|말을 이어 가려던 그 순간, 우진태가 번개 같은 속도로 자신의 뒤통수를 바닥에 내리찍었다.
 88|
 89|쿵! 털썩.
 90|
 91|안타깝다. 최소한 한 시진은 더 갈굴 수 있었는데.
 92|
 93|혼절한 우진태를 두고 돌아서는 나에게 수많은 시선이 우수수 날아와 꽂힌다.
 94|
 95|“성운표국의 소국주가 저렇게 간단하게…….”
 96|
 97|“저 젊은 놈, 도대체 정체가 뭐야?”
 98|
 99|“손속도 손속이지만, 혓바닥이 독사가 따로 없구먼.”
100|
101|놀람과 두려움이 섞인 웅성거림이 일파만파 퍼져 나갔다.
102|
103|1층에 자리한 손님만 자그마치 백여 명. 내 얼굴을 알아보는 이들이 나타난 것도 사실 결코 놀라운 일은 아니었다.
104|
105|“사, 산서잠룡이다!”
106|
107|“뭐? 태원진가의?”
108|
109|“그럼 산서잠룡이 둘이겠나! 어쩐지 아까부터 눈에 익더라니.”
110|
111|산서잠룡의 명성이 아주 하늘을 떨어 울리는구나.
112|
113|내가 흐뭇한 미소와 함께 사람들에게 손을 흔들어 주려던 그때였다.
114|
115|“확실한가? 산서잠룡이라면 작년 이맘때쯤에 홍화루에서 한 번 본 적이 있는데, 내가 기억하는 모습과는 좀…….”
116|
117|“이 사람아, 그때 우리 둘이 같이 있었던 건 기억 안 나나?”
118|
119|“어, 그랬던가?”
120|
121|“그래, 체격이나 분위기가 많이 달라져서 그렇지, 산서잠룡이 확실하네. 태원진가의 자제라는 놈이 가문에 기녀를 데려가겠다고 온갖 진상을 부리던 모습이 아직도 눈앞에 선해.”
122|
123|“…….”
124|
125|젠장. 별걸 다 기억하네.
126|
127|내가 머쓱한 얼굴로 손을 내리자 자기들끼리 수군거리던 손님 중 몇 명이 손을 번쩍 치켜들었다.
128|
129|“그때 나도 있었소!”
130|
131|“형장도?”
132|
133|“똑똑히 기억하오. 저놈, 아니 저분이 계단에서 넘어지면서 내 아래 물건을 쭉 잡아당겼…… 후우, 그때만 생각하면 지금도 아찔하구려.”
134|
135|“허어어, 망측한지고. 지금은 괜찮소?”
136|
137|“다행히도 멀쩡하오. 뿐만 아니라 그 후로 살짝 길어진 느낌이오.”
138|
139|“…….”
140|
141|그게 가능해?
142|
143|나는 방금 입을 연 사람에게 얼마나 커졌는지 물어보고 싶은 마음을 간신히 억눌렀다. 산서오문인지 나발인지 하는 찌꺼기들의 처리가 아직 남아 있었기 때문이다.
144|
145|그런데…….
146|
147|“어라?”
148|
149|내 시선에 들어온 것은 나란히 대가리를 박고 있는 네 명의 후기지수와 어쩐지 목이 빳빳하게 선 혁무진이었다.
150|
151|“준비 끝났습니다.”
152|
153|“네가 이러라고 시킨 거냐?”
154|
155|“서당 개 삼 년이면 풍월을 읊는다 했습니다. 이제 척 하면 착 아닙니까?”
156|
157|“너 이 녀석……!”
158|
159|나는 형용할 수 없는 감정에 사로잡혔다.
160|
161|처음에는 멍청한 놈인 줄 알았는데, 갈수록 똑똑해지는 것 같다.
162|
163|나 대신 지력 스탯을 찍는 게 아닌지 의심될 정도다.
164|
165|“성장했구나. 매우 칭찬한다.”
166|
167|“과찬의 말씀이십니다. 그보다 이들은 어찌할까요?”
168|
169|“검갑 줘 봐.”
170|
171|“존명.”
172|
173|대하 사극의 한 장면이 따로 없다. 나는 혁무진이 내민 검갑을 받아 들고 손바닥을 내리쳤다. 그립감 좋고, 타격감도 좋다.
174|
175|“다들 기상.”
176|
177|말이 떨어지기가 무섭게 후기지수 네 사람이 벌떡 일어났다.
178|
179|두려움 가득한 시선을 무시하며 다시 레벨창을 쭉 훑어보니 역시나 이제 간신히 일류가 될까 말까 한 녀석들이다.
180|
181|“뭘 잘못했는지는 이미 알 테고…… 너희가 산서오문의 후계자들이라고?”
182|
183|“예, 옛!”
184|
185|“셋째 아들, 막내딸. 뭐 그런 거 아냐?”
186|
187|“아닙니다!”
188|
189|“확실해?”
190|
191|“예, 그렇습니다!”
192|
193|기합이 제대로 들어간 목소리가 객잔 내부를 쩌렁쩌렁하게 울린다. 나는 검갑을 탁탁 두드리며 중얼거렸다.
194|
195|“그래? 그럼 산서오문도 별거 아니네?”
196|
197|“…….”
198|
199|“…….”
200|
201|하나같이 수치심으로 얼굴이 붉게 달아올랐지만 아무 말도 하지 못한다.
202|
203|이제는 놈들도 내 신분을 아니까.
204|
205|당장 나와의 무력 차이는 둘째치고서라도, 산서오문 정도로는 태원진가의 이름 앞에서 고개를 빳빳하게 들 수 없다.
206|
207|“그동안 세월 좋았다. 그치?”
208|
209|“……아닙니다.”
210|
211|“아니긴 뭐가 아니야. 돈 걱정 없고, 뒷배 든든하고. 그거 믿고 지금까지 짱짱하게 잘나갔을 거 아냐. 응? 여기저기 시비도 걸고 다니고.”
212|
213|“…….”
214|
215|“그런데 태원진가랑 항산검문 사이에 전쟁이 일어났네? 평소에 잘해 준 건 태원진가인데, 항산검문이 이기면 돌아올 보복이 무서워서 눈치 살살 보다가 여기까지 왔고. 맞지?”
216|
217|“그, 그게 저희는 잘…….”
218|
219|“너희 후계자라면서? 각자 소문주, 소가주. 뭐 그런 거 아니냐? 아, 저기 저놈은 소국주였지.”
220|
221|엉겁결에 내가 가리키는 방향을 바라본 네 사람이 몸을 부르르 떨었다.
222|
223|모진 따귀 세례와 트래쉬 토크를 견디지 못하고 스스로 기절을 택한 우진태가 죽은 것처럼 바닥에 누워 있었다.
224|
225|“아무튼, 상황이 이러면 적당히 쭈그려 있지 뭐 잘났다고 여기까지 와서 기고만장하게 굴어. 태원진가가 우스워? 내가 이마에 산서잠룡이라고 문신 새기고 다녀야 해?”
226|
227|“죄, 죄송합니다.”
228|
229|“죄송하면 다 끝나? 내가 너희 죽사발 낸 다음에 사과해 줘?”
230|
231|“히익!”
232|
233|저 공포에 찬 눈빛들을 보라. 걸어 다니는 재앙이 된 기분이다.
234|
235|더 이상 말이 필요 없는 상황. 나는 검갑을 들어 올렸다.
236|
237|“역사적으로도 이게 약이었다. 다들 엎드려뻗쳐.”
238|
239|그리고 오들오들 떨면서 엎드린 네 명의 후기지수에게 스산한 목소리로 물었다.
240|
241|“몇 대 맞아야 반성할래? 각자 말해 봐.”
242|
243|“예, 예?”
244|
245|“말해 보라고. 우진태 저놈은 너무 나대서 저렇게 팬 거지, 너희는 자진 납세 했으니까 정상참작 해 준다.”
246|
247|무거운 침묵이 흘렀다. 빠르게 시선을 교환한 네 사람이 한입으로 외쳤다.
248|
249|“하, 한 대만 맞겠습니다!”
250|
251|“한 대? 그걸로 되겠어?”
252|
253|“옛!”
254|
255|“한 대 맞으면 다시는 이런 일 없게 할 거야?”
256|
257|“천지신명께 맹세하겠습니다!”
258|
259|나는 검갑을 단단히 말아 쥐었다.
260|
261|“좋아. 그럼 각자 열 대씩.”
262|
263|“……!”
264|
265|“……!”
266|
267|“방금 천지신명한테 물어봤는데, 너희는 한 대로 어림도 없대. 그러니까 열 대.”
268|
269|내가 살면서 이런 상황을 겪게 될 줄이야. 학창 시절, 틈만 나면 빠따를 휘두르던 체대 입시 선생이 된 기분이다.
270|
271|나는 묘한 향수에 젖은 채 빠따, 아니 검갑을 휘둘렀다.
272|
273|빡! 빡! 빡! 딱!
274|
275|“크헉!”
276|
277|“움직이지 마. 뼈 다친다. 자, 다시.”
278|
279|빡! 빡! 빡!
280|
281|홍화 객잔을 가득 메운 사람들에게는 진귀한 광경일 것이다. 산서오문의 후계자라는 자들이 굼벵이처럼 바닥을 기어 다니고 있었으니까. 심지어 그중에는 여자도 둘이나 끼어 있었다.
282|
283|우리를 빙 둘러싼 사람들이 수군거리는 소리가 귓가를 파고들었다.
284|
285|“저거, 저래도 되는 거여?”
286|
287|“그러게 말이여. 아무리 그래도 산서오문인데…… 이러다가 또 무림의 은원이니 뭐니 하면서 큰 싸움 일어나는 거 아닌가 모르겄네.”
288|
289|“거, 답답하기는. 요즘 상황을 몰라도 너무 모르는 거 아니오? 항산검문이 건재했다면 모를까, 지금 태원진가를 막으려면 산서 땅에 있는 중소 문파가 죄다 뭉쳐도 될까 말까요.”
290|
291|“그 정도여?”
292|
293|“다 끌어모으면 머릿수야 앞설지 몰라도 수준이 다르지. 저기 산서잠룡만 봐도 알 수 있는 사실 아니오?”
294|
295|“그렇긴 하네. 산서오문의 후계자니, 후기지수니 뭐니 하면서 거들먹거리더니 산서잠룡한테는 쥐뿔도 안 되는 거 보면.”
296|
297|“따지고 보면 먼저 시비 건 것도 저쪽 아니오?”
298|
299|“그것도 맞는 말이지.”
300|
301|“그리고 기왕 말이 나왔으니 말인데, 지금 산서오문이라고 하고 다니는 것들 보면 죄다 냄새가 구려.”
302|
303|“구리다니?”
304|
305|“말이 정파지 알게 모르게 양민 등골이나 빨아먹는다, 이 말이오. 당장 성운표국만 봐도 상인들 사이에서 얼마나 말이 많은데?”
306|
307|“그 소문들이 사실이었나?”
308|
309|“반면에 태원진가는 어떻소? 십 년 전에 기근(飢饉)이 들었을 때는 구휼미도 풀고, 그보다 훨씬 전에는 마교 놈들도 막아 냈지. 그놈들은 우리 같은 양민들도 죽이고 다니는 흉악한 살귀(殺鬼)들이니 만약 태원진가가 아니었다면…… 으, 생각하기도 싫소.”
310|
311|“맞다, 이번에 고원에서 넘어온 마적들을 쫓아 보낸 것도 태원진가라고 들었는데.”
312|
313|“그 소문 아직 못 들은 사람도 있소? 진천검과 산서잠룡이 싹 다 몰살을 시켜 버렸다고 합디다.”
314|
315|“허어어.”
316|
317|“그러니 만에 하나 다시 전쟁이 일어난들 문제 될 것이 무에 있겠소? 내 맹세컨대, 산서오문이 이 문제를 걸고넘어지면 당장 태원진가에 입문(入門)하여 싸우겠소!”
318|
319|“오오!”
320|
321|“아직 젊은 친구가 협기(俠氣)가 대단하군. 내 듣고 보니 자네 말이 맞는 것 같네. 여기 내 술 한 잔 받게!”
322|
323|빡! 빡! 빡!
324|
325|후기지수 넷 중 세 명을 굼벵이로 만든 나는 말소리가 들려오는 쪽으로 고개를 돌렸다.
326|
327|얼마나 힘써서 태원진가를 변호해 주는지, 이야기를 듣다 보니 내가 술을 사 주고 싶어질 정도다.
328|
329|‘마인드만 보면 이미 우리 태원진가 사람인데?’
330|
331|레벨만 좀 받쳐 준다면 영입 1순위다. 나는 흐뭇하게 웃으며 저 위대한 웅변가의 레벨창을 확인했다.
332|
333|
334|
335|[Lv.15 장칠득]
336|
337|
338|
339|“……뭐여, 시벌.”
340|
341|장칠득? 내가 아는 그 장칠득?
342|
343|다시 잘 보니 분명 아는 얼굴이다. 진무경에게 일대일 집중 수련을 받던 시절, 우리한테 꼬박꼬박 식사를 가져다주던 하인.
344|
345|바로 그 장칠득이 위대한 웅변가의 정체였다.
346|
347|‘와 씨, 소름.’
348|
349|어쩐지 너무 태원진가 편만 들더라.
350|
351|물론 틀린 말은 없었지만 이런 식으로 여론 조작을 하다니.
352|
353|뭔가 정치계의 엄청난 음모를 발견한 것 같은 기분에 몸이 부르르 떨리던 그때였다.
354|
355|“저기…….”
356|
357|잠시 잊고 있던 한 사람, 청풍이 맑은 눈으로 입을 열었다.
358|
359|“아직 한 분 남았는데요.”
360|
361|“헉.”
362|
363|엎드려 있던 마지막 한 놈이 움찔했다. 청풍 이놈도 은근히 순진한 것 같으면서 무서운 놈이다.
364|
365|어차피 마지막이라고 봐줄 생각 따위는 없었지만.
366|
367|“안 그래도 지금 때리려고요.”
368|
369|검갑을 휘두르려던 그때, 청풍이 재차 입을 열었다.
370|
371|“저기. 어려운 부탁 하나만 말씀드려도 되겠습니까?”
372|
373|“빙당호로 이제 없어요.”
374|
375|“그게 아니고, 저어.”
376|
377|머뭇거리던 청풍이 조용히 검갑을 가리켰다.
378|
379|“마지막 분은 제가 한번 때려 보고 싶어서요.”
380|
381|“예?”
382|
383|“제가 아직 이런 걸 한 번도 안 해 봐서…….”
384|
385|“…….”
386|
387|살면서 별의별 또라이를 다 봤지만, 첫 경험 빌런은 처음이다.
```

## Assembled English

```markdown
[P1]
# Chapter 135

[P2]
*Smack!*

[P3]
“P-please, help me!”

[P4]
“No one’s coming to help you.”

[P5]
*Smack-smack!*

[P6]
“P-please, spare me!”

[P7]
“Nope. Not happening. Go away.”

[P8]
*Smack-smack-smack!*

[P9]
“Th-then just kill me…”

[P10]
“No, you’re still fine. Words are still coming out of your mouth.”

[P11]
*Smack-smack-smack-smack!*

[P12]
“Hhk… Hhrrgh…”

[P13]
“Yes. That’s the reaction I was looking for.”

[P14]
Only then did I finally stop.

[P15]
The young master’s once reasonably presentable face had puffed up like a steamed bun. Instead of a rosy flush, dark blue bruises covered both cheeks.

[P16]
“Our Jintae. Did you do something wrong or not?”

[P17]
“Hhrrgh.”

[P18]
Seeing him sob in such a miserable state, I suddenly felt a little sorry for him.

[P19]
*Right. He’s someone else’s precious son, too…*

[P20]
“You did something wrong, didn’t you?”

[P21]
“Hhk! Hhrrgh!”

[P22]
“Then why did you ignore what I was saying? You should’ve apologized the moment I told you to. Wouldn’t that have been better? Don’t you think?”

[P23]
“Hhrrr.”

[P24]
“Let’s be good from now on. Understand?”

[P25]
“Hhrrgh.”

[P26]
I quietly watched Woo Jintae nod furiously, then spoke.

[P27]
“But you…”

[P28]
“Hh?”

[P29]
“Why have you been answering like that this whole time? Can’t you speak like a person?”

[P30]
His sobbing stopped dead.

[P31]
“I-I’m sorry.”

[P32]
“So you can talk. You could talk all along, but you chose not to? Why were you crying? Were you trying to show how much pain and hardship you were in?”

[P33]
“No!”

[P34]
“Now your voice is getting louder, too. You’ve got some volume. Have you been practicing diaphragmatic breathing? Were you planning to burst my eardrums and escape this crisis?”

[P35]
“No. Absolutely not. Please, stop now. Hh-hhng…”

[P36]
“Oh? You’re crying again? You can still cry? What have you done to deserve tears? Is your life over because you’re crying? And ‘please stop’? Anyone watching would think I was the one attacking you.”

[P37]
“I’m sorry. I won’t cry.”

[P38]
“Wow, look at him stop crying right away. You’re a creepy bastard, aren’t you? If I were you, I’d feel so guilty for picking on an innocent person that I’d cry until I passed out from exhaustion. Are you really sorry?”

[P39]
“P-please, just listen to me for a moment…”

[P40]
“Listen to what? Do you even have the right to speak? Is this some kind of entertainment awards ceremony? Am I supposed to wait quietly while you talk, then smile warmly and applaud when you’re finished?”

[P41]
“…”

[P42]
“Now you’re not even answering. You must feel full even without eating. Right? If you keep crunching through other people’s words like that, it must feel good…”

[P43]
Just as I was about to continue, Woo Jintae slammed the back of his head into the floor with lightning speed.

[P44]
*Thud! Flop.*

[P45]
What a shame. I could have kept chewing him out for at least another shichen.[^1]

[P46]
[^1]: A shichen is a traditional time unit equal to approximately two hours.

[P47]
As I turned away from the unconscious Woo Jintae, countless gazes came flying toward me and stuck fast.

[P48]
“The Young Bureau Head of the Seongun Escort Bureau went down that easily…”

[P49]
“Who the hell is that young man?”

[P50]
“His hands are vicious enough, but his tongue is a venomous snake all on its own.”

[P51]
Murmurs of shock and fear rippled through the room.

[P52]
There were more than a hundred guests on the first floor alone. It was hardly surprising that some of them recognized me.

[P53]
“I-it’s the Sleeping Dragon of Shanxi!”

[P54]
“What? The one from the Jin Family of Taiyuan?”

[P55]
“Do you think there are two Sleeping Dragons of Shanxi? I knew he looked familiar.”

[P56]
*My reputation as the Sleeping Dragon of Shanxi really does shake the heavens.*

[P57]
I was just about to give the crowd a pleased smile and wave when someone spoke up.

[P58]
“Are you sure? I saw the Sleeping Dragon of Shanxi at Honghwaru around this time last year, but he looks a little…”

[P59]
“You don’t remember that the two of us were there together?”

[P60]
“Oh. Were we?”

[P61]
“Yes. His build and overall impression have changed quite a bit, but it’s definitely him. I can still picture that young master from the Jin Family making a scene because he wanted to bring a courtesan back to the family.”

[P62]
“…”

[P63]
*Damn. Why do people remember such useless things?*

[P64]
As I awkwardly lowered my hand, several guests who had been whispering among themselves suddenly raised theirs.

[P65]
“I was there, too!”

[P66]
“You were, Brother?”

[P67]
“I remember it clearly. That bastard—no, that gentleman—fell down the stairs, grabbed the thing between my legs, and gave it a long yank… Whew. Just thinking about it still makes me dizzy.”

[P68]
“My goodness, how indecent. Are you all right now?”

[P69]
“Fortunately, I’m perfectly fine. Not only that, I think it’s gotten a little longer since then.”

[P70]
“…”

[P71]
*Can that happen?*

[P72]
I barely suppressed the urge to ask exactly how much longer it had gotten. I still had the trash from the so-called Five Gates of Shanxi to deal with.

[P73]
But then…

[P74]
“Huh?”

[P75]
Four young prodigies were lined up with their heads planted on the floor, while Hyuk Mujin stood beside them with his neck held strangely stiff.

[P76]
“We’re ready.”

[P77]
“Did you order them to do this?”

[P78]
“They say even a village-school dog can recite poetry after three years. By now, I can tell what you want at a glance.”

[P79]
“You little…”

[P80]
I was seized by an indescribable emotion.

[P81]
At first, I’d thought he was an idiot, but he seemed to be getting smarter by the day.

[P82]
I was starting to suspect he was putting points into Intelligence on my behalf.

[P83]
“You’ve grown. I’m very proud of you.”

[P84]
“You’re too kind. More importantly, what should we do with them?”

[P85]
“Give me the sword case.”

[P86]
“At your command.”

[P87]
It was straight out of a historical drama. I took the sword case Hyuk Mujin held out and slapped it against my palm.

[P88]
Good grip. Good impact, too.

[P89]
“Everyone, on your feet.”

[P90]
The four young prodigies sprang to their feet the moment I spoke.

[P91]
Ignoring their terrified gazes, I scanned their Level Windows again. Just as I’d thought, they were barely First Rate, if that.

[P92]
“You already know what you did wrong… You’re the heirs of the Five Gates of Shanxi?”

[P93]
“Y-yes, sir!”

[P94]
“You’re not third sons or youngest daughters or anything like that?”

[P95]
“No, sir!”

[P96]
“You’re sure?”

[P97]
“Yes, sir!”

[P98]
Their voices, filled with proper martial spirit, rang through the inn. I tapped the sword case against my palm and muttered,

[P99]
“Really? Then the Five Gates of Shanxi aren’t anything special, are they?”

[P100]
“…”

[P101]
“…”

[P102]
Every one of their faces flushed with shame, but none of them dared to answer.

[P103]
They knew who I was now.

[P104]
The difference in our martial prowess aside, the Five Gates of Shanxi couldn’t hold their heads high before the Jin Family of Taiyuan.

[P105]
“You’ve had it good all this time, haven’t you?”

[P106]
“…No, sir.”

[P107]
“What do you mean, no? You never had to worry about money, and you had powerful backing. You relied on that and strutted around like big shots, didn’t you? Picking fights wherever you went.”

[P108]
“…”

[P109]
“But then a war broke out between the Jin Family of Taiyuan and the Mount Heng Sword Sect. The Jin Family was the one that had always treated you well, but you were afraid of the retaliation that would come if Mount Heng won, so you kept watching the situation and ended up here. Right?”

[P110]
“Th-that’s… We…”

[P111]
“You’re the heirs, aren’t you? Young Sect Leaders, Lesser Family Heads, things like that. Ah, that fellow over there was the Young Bureau Head.”

[P112]
The four of them reflexively followed my finger and shuddered.

[P113]
Unable to withstand the merciless barrage of slaps and trash talk, Woo Jintae had chosen to knock himself unconscious. He lay on the floor like a corpse.

[P114]
“Anyway, given the situation, you should’ve kept your heads down. What did you come all the way here for, acting so high and mighty? Do you think the Jin Family of Taiyuan is a joke? Do I need to tattoo ‘Sleeping Dragon of Shanxi’ on my forehead and walk around with it?”

[P115]
“I-I’m sorry.”

[P116]
“Does apologizing make everything go away? Should I beat you into a bloody mess and then apologize to you?”

[P117]
“Eek!”

[P118]
Just look at those terrified eyes. I felt like a walking disaster.

[P119]
There was no need for any more words. I raised the sword case.

[P120]
“Historically, this has always been the best medicine. Everyone, get down.”

[P121]
Then I asked the four trembling young prodigies lying face down before me in a chilling voice,

[P122]
“How many blows will it take for you to reflect? Each of you, give me a number.”

[P123]
“W-what?”

[P124]
“Give me a number. I beat that Woo Jintae so badly because he was acting too high and mighty. Since you paid up voluntarily, I’ll take that into consideration.”

[P125]
A heavy silence descended.

[P126]
The four exchanged hurried glances, then shouted in unison.

[P127]
“J-just one!”

[P128]
“One? Will that really be enough?”

[P129]
“Yes, sir!”

[P130]
“If you take one hit, will you swear never to do anything like this again?”

[P131]
“We swear it before Heaven and Earth and all the divine spirits!”

[P132]
I tightened my grip on the sword case.

[P133]
“Good. Then ten each.”

[P134]
“…!”

[P135]
“…!”

[P136]
“I just asked Heaven and Earth, and they said one wouldn’t come close to being enough for you. So ten it is.”

[P137]
I never thought I’d find myself in a situation like this.

[P138]
I felt like one of those physical-education entrance-exam instructors from my school days who swung a bat whenever he got the chance.

[P139]
Sinking into a strange sense of nostalgia, I swung the bat—or rather, the sword case.

[P140]
*Whack! Whack! Whack! Crack!*

[P141]
“Guh!”

[P142]
“Don’t move. You’ll hurt your bones. All right, again.”

[P143]
*Whack! Whack! Whack!*

[P144]
It must have been a rare sight for everyone packed into Honghwa Inn. The heirs of the Five Gates of Shanxi were crawling across the floor like grubs.

[P145]
Two of them were even women.

[P146]
The whispers of the people surrounding us cut into my ears.

[P147]
“Is that really okay?”

[P148]
“I know, right? Even if they are the Five Gates of Shanxi… Couldn’t this turn into another one of those big fights over Murim gratitude and grudges?”

[P149]
“Don’t be so clueless. Are you really that out of touch with what’s happening these days? Maybe things would be different if the Mount Heng Sword Sect were still standing, but now, every small and medium-sized sect in Shanxi could join forces and still might not stop the Jin Family of Taiyuan.”

[P150]
“It’s that bad?”

[P151]
“They might outnumber them if they gathered everyone, but the caliber is completely different. You only have to look at the Sleeping Dragon of Shanxi over there to see that.”

[P152]
“That’s true. Those Five Gates heirs swaggered around like big shots, but they’re nothing before the Sleeping Dragon of Shanxi.”

[P153]
“If you think about it, they were the ones who picked the fight first.”

[P154]
“That’s true, too.”

[P155]
“And since we’re on the subject, there’s something rotten about everyone calling themselves the Five Gates of Shanxi these days.”

[P156]
“Rotten?”

[P157]
“They call themselves an orthodox faction, but they’re really just sucking the marrow out of ordinary people without anyone noticing. Just look at the Seongun Escort Bureau. How many complaints have merchants made about them?”

[P158]
“Were all those rumors true?”

[P159]
“What about the Jin Family of Taiyuan? When famine struck ten years ago, they released relief grain. Long before that, they even held off the Demonic Cult. Those bastards were vicious murderous fiends who went around killing ordinary people like us. If not for the Jin Family of Taiyuan…”

[P160]
“Ugh. I don’t even want to think about it.”

[P161]
“That’s right. I also heard it was the Jin Family of Taiyuan that drove off the mounted bandits who crossed over from Gaoyuan this time.”

[P162]
“Is there anyone who hasn’t heard that rumor yet? They say the Heaven Shaking Sword and the Sleeping Dragon of Shanxi slaughtered every last one of them.”

[P163]
“My goodness.”

[P164]
“So even if another war breaks out, what’s there to worry about? I swear, if the Five Gates of Shanxi try to make an issue of this, I’ll join the Jin Family of Taiyuan immediately and fight!”

[P165]
“Oh!”

[P166]
“That’s some impressive chivalrous spirit for such a young man. Now that I’ve heard you out, I think you’re right. Here, have a drink on me!”

[P167]
*Whack! Whack! Whack!*

[P168]
After turning three of the four young prodigies into grubs, I turned toward the voices.

[P169]
The speaker had defended the Jin Family of Taiyuan so passionately that, by the time he finished, I wanted to buy him a drink myself.

[P170]
*In terms of mindset, he’s already one of our Jin Family.*

[P171]
If his Level were high enough, he’d be my first recruitment pick. Smiling with satisfaction, I checked the great orator’s Level Window.

[P172]
> **System**
>
> **Level 15: Jang Childeuk**

[P173]
“…What the fuck?”

[P174]
*Jang Childeuk? The Jang Childeuk I know?*

[P175]
Looking again, I realized I definitely recognized him.

[P176]
He was the servant who had faithfully brought us meals while I was receiving one-on-one intensive training from Jin Mukyung.

[P177]
That Jang Childeuk was the great orator’s true identity.

[P178]
*Holy shit. Goose bumps.*

[P179]
No wonder he’d been taking the Jin Family’s side so aggressively.

[P180]
Nothing he’d said was wrong, of course, but manipulating public opinion like this…

[P181]
I was trembling as though I’d uncovered some enormous political conspiracy when someone spoke.

[P182]
“Um…”

[P183]
It was Cheongpung, the one person I had momentarily forgotten. He spoke up, his eyes clear.

[P184]
“There’s still one person left.”

[P185]
“Ah.”

[P186]
The last man lying face down flinched. Cheongpung seemed innocent in his own way, but he was also strangely frightening.

[P187]
Not that I had any intention of going easy on him just because he was last.

[P188]
“I was just about to hit him.”

[P189]
I was about to swing the sword case when Cheongpung spoke again.

[P190]
“Excuse me. May I ask you one difficult favor?”

[P191]
“We’re out of candied hawthorn skewers[^2] now.”

[P192]
[^2]: Candied hawthorn skewers are a traditional snack of fruit skewers coated in hardened sugar.

[P193]
“That’s not it. I, uh…”

[P194]
Cheongpung hesitated, then quietly pointed at the sword case.

[P195]
“I’d like to try hitting the last gentleman.”

[P196]
“What?”

[P197]
“I’ve never done anything like this before…”

[P198]
“…”

[P199]
I had seen every kind of nutcase in my life, but this was my first time seeing a first-experience villain.
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
# Chapter 135

[P2]
*Smack!*

[P3]
“P-please, help me!”

[P4]
“No one’s coming to help you.”

[P5]
*Smack-smack!*

[P6]
“P-please, spare me!”

[P7]
“No. Not happening. Go back.”

[P8]
*Smack-smack-smack!*

[P9]
“Th-then just kill me…”

[P10]
“No, you’re still fine. Words are still coming out of your mouth.”

[P11]
*Smack-smack-smack-smack!*

[P12]
“Hhk… Hhrrgh…”

[P13]
“Yes. That’s the reaction I was looking for.”

[P14]
Only then did I finally stop my hand.

[P15]
The young master’s face, which had been reasonably presentable until now, had puffed up like a steamed bun. Instead of a healthy flush, both cheeks were covered in dark blue bruises.

[P16]
“Our Jintae. Did you do something wrong or not?”

[P17]
“Hhrrgh.”

[P18]
Seeing him sob with his face in such a mess, I suddenly felt a little sorry for him.

[P19]
*Right. He’s someone else’s precious son, too…*

[P20]
“You did something wrong, didn’t you?”

[P21]
“Hhk! Hhrrgh!”

[P22]
“Then why did you ignore what I was saying? You should’ve apologized the moment I told you to. Wouldn’t that have been better? Don’t you think?”

[P23]
“Hhrrr.”

[P24]
“Let’s live properly from now on. Understand?”

[P25]
“Hhrrgh.”

[P26]
I quietly watched Woo Jintae nod furiously before opening my mouth.

[P27]
“But you…”

[P28]
“Hh?”

[P29]
“Why have you been answering like that this whole time? Can’t you speak like a normal person?”

[P30]
His sobbing stopped dead.

[P31]
“I-I’m sorry.”

[P32]
“You could do it? You could speak, but you chose not to? Why were you crying? Were you trying to show everyone how much pain and hardship you were in?”

[P33]
“No!”

[P34]
“Your voice is getting louder, too. You’ve got some volume. Have you been practicing diaphragmatic breathing? Were you planning to blow out my eardrums and escape this crisis?”

[P35]
“No. Absolutely not. Please, stop now. Hh-hhng…”

[P36]
“Oh? You’re crying again? You can still cry? What have you done to deserve tears? Is your life over because you’re crying? And ‘please stop’? Anyone watching would think I was the one attacking you.”

[P37]
“I’m sorry. I won’t cry.”

[P38]
“Wow, look at him stop crying right away. You’re a creepy one, aren’t you? If I were you, I’d feel so guilty for picking on an innocent person that I’d cry until I passed out from exhaustion. Are you really sorry?”

[P39]
“P-please, just listen to me for a moment…”

[P40]
“Listen to what? Do you even have the right to speak? Is this some kind of entertainment awards ceremony? Am I supposed to sit quietly while you talk, then smile warmly and applaud when you’re finished?”

[P41]
“…”

[P42]
“Now you’re not even answering. You must feel full even without eating. Right? If you keep crunching through other people’s words like that, it must feel good…”

[P43]
Just as I was about to continue, Woo Jintae slammed the back of his head into the floor with lightning speed.

[P44]
*Thud! Plop.*

[P45]
What a shame. I could have kept chewing him out for at least another shichen.[^1]

[P46]
[^1]: A shichen is a traditional time unit equal to approximately two hours.

[P47]
As I turned away from the unconscious Woo Jintae, countless gazes came flying toward me and stuck fast.

[P48]
“The Young Bureau Head of the Seongun Escort Bureau went down that easily…”

[P49]
“Who the hell is that young man?”

[P50]
“His hands are vicious enough, but his tongue is a venomous snake all on its own.”

[P51]
A murmur mixed with shock and fear spread through the room like a wave.

[P52]
There were more than a hundred guests on the first floor alone. It was hardly surprising that some of them recognized my face.

[P53]
“It’s the Sleeping Dragon of Shanxi!”

[P54]
“What? The one from the Jin Family of Taiyuan?”

[P55]
“Do you think there are two Sleeping Dragons of Shanxi? I knew his face looked familiar.”

[P56]
*My reputation as the Sleeping Dragon of Shanxi really does reach the heavens.*

[P57]
I was just about to give the crowd a pleased smile and wave when someone spoke up.

[P58]
“Are you sure? I saw the Sleeping Dragon of Shanxi at Honghwaru around this time last year, but he looks a little…”

[P59]
“You don’t remember that the two of us were there together?”

[P60]
“Oh. Were we?”

[P61]
“Yes. His build and overall impression have changed quite a bit, but it’s definitely him. I can still see him causing a scene because he wanted to bring a courtesan back to the Jin Family.”

[P62]
“…”

[P63]
*Damn. Why do people remember such useless things?*

[P64]
As I awkwardly lowered my hand, several of the guests who had been whispering among themselves suddenly raised their hands.

[P65]
“I was there, too!”

[P66]
“You were, Brother?”

[P67]
“I remember it clearly. That guy—no, that gentleman—fell down the stairs, grabbed the thing between my legs, and gave it a long yank… Whew. Just thinking about it still makes me dizzy.”

[P68]
“My goodness, how indecent. Are you all right now?”

[P69]
“Fortunately, I’m perfectly fine. Not only that, I think it’s gotten a little longer since then.”

[P70]
“…”

[P71]
*Can that happen?*

[P72]
I barely managed to suppress my urge to ask the man who had just spoken exactly how much longer it had gotten. There was still the trash from the so-called Five Gates of Shanxi to deal with.

[P73]
But then…

[P74]
“Huh?”

[P75]
What came into view were four young prodigies with their heads planted on the floor in a row—and Hyuk Mujin standing there with his head held oddly high.

[P76]
“We’re ready.”

[P77]
“Did you order them to do this?”

[P78]
“They say that even a village-school dog can recite poetry after three years. Now, if you give me a hint, I know exactly what to do.”

[P79]
“You little…”

[P80]
I was seized by an indescribable emotion.

[P81]
At first, I had thought he was an idiot, but he seemed to be getting smarter by the day.

[P82]
I was almost suspicious that he was putting points into Intelligence for me.

[P83]
“You’ve grown. I’m very proud of you.”

[P84]
“You’re too kind. More importantly, what should we do with them?”

[P85]
“Give me the sword case.”

[P86]
“At your command.”

[P87]
It was straight out of a historical drama. I took the sword case Hyuk Mujin held out and brought it down against my palm.

[P88]
The grip was good, and the impact felt good, too.

[P89]
“Everyone, get up.”

[P90]
The four young prodigies sprang to their feet the moment I spoke.

[P91]
Ignoring their terrified gazes, I scanned their Level Windows again. Just as I thought, they were barely First Rate, if that.

[P92]
“You already know what you did wrong… You’re the heirs of the Five Gates of Shanxi?”

[P93]
“Y-yes, sir!”

[P94]
“The third son, the youngest daughter, that sort of thing?”

[P95]
“No!”

[P96]
“Are you sure?”

[P97]
“Yes, we are!”

[P98]
Their voices, filled with proper martial spirit, rang through the inn. I tapped the sword case against my palm and muttered,

[P99]
“Really? Then the Five Gates of Shanxi aren’t anything special, are they?”

[P100]
“…”

[P101]
“…”

[P102]
Every one of their faces flushed with shame, but none of them dared to answer.

[P103]
They knew who I was now.

[P104]
Their difference in martial power was only the second issue. Even putting that aside, people from the Five Gates of Shanxi couldn’t hold their heads high in front of the Jin Family of Taiyuan.

[P105]
“You’ve had it good all this time, haven’t you?”

[P106]
“…No.”

[P107]
“What do you mean, no? You never had to worry about money, and you had powerful backing. You relied on that and lived large all this time, didn’t you? Picking fights wherever you went.”

[P108]
“…”

[P109]
“But then a war broke out between the Jin Family of Taiyuan and the Mount Heng Sword Sect. The Jin Family was the one that had always treated you well, but you were afraid of the retaliation that would come if Mount Heng won, so you kept watching the situation and ended up here. Right?”

[P110]
“Th-that’s… We…”

[P111]
“You’re the heirs, aren’t you? A Young Sect Leader, a Lesser Family Head—something like that, right? Ah, that fellow over there was the Young Bureau Head.”

[P112]
The four people I pointed toward reflexively glanced in that direction and shuddered.

[P113]
Unable to endure the merciless barrage of slaps and trash talk, Woo Jintae had chosen to pass out. He lay on the floor as though he were dead.

[P114]
“Anyway, given the situation, you should’ve kept your heads down. What did you come all the way here for, acting so high and mighty? Do you think the Jin Family of Taiyuan is a joke? Do I need to tattoo ‘Sleeping Dragon of Shanxi’ on my forehead and walk around with it?”

[P115]
“I-I’m sorry.”

[P116]
“Does apologizing make everything go away? Should I beat you into a bloody mess and then apologize to you?”

[P117]
“Eek!”

[P118]
Just look at those terrified eyes. I felt like a walking disaster.

[P119]
This was a situation that no longer required words. I raised the sword case.

[P120]
“Historically, this has always been an effective remedy. Everyone, get down.”

[P121]
Then I asked the four trembling young prodigies who lay face down in a chilling voice,

[P122]
“How many blows will it take for you to reflect? Each of you, give me a number.”

[P123]
“W-what?”

[P124]
“Give me a number. I beat that Woo Jintae so badly because he was acting too high and mighty. Since you paid up voluntarily, I’ll take that into consideration.”

[P125]
A heavy silence descended.

[P126]
The four of them exchanged hurried glances before shouting as one.

[P127]
“J-just one!”

[P128]
“One? Will that really be enough?”

[P129]
“Yes, sir!”

[P130]
“If you take one hit, will you swear never to do anything like this again?”

[P131]
“We swear it before Heaven and Earth and all the divine spirits!”

[P132]
I gripped the sword case tightly.

[P133]
“Good. Then ten each.”

[P134]
“……!”

[P135]
“……!”

[P136]
“I just asked Heaven and Earth, and they said one wouldn’t come close to being enough for you. So ten it is.”

[P137]
I never thought I’d find myself in a situation like this.

[P138]
Back in school, I felt like one of those physical-education entrance-exam teachers who swung a bat whenever he got the chance.

[P139]
Wallowing in a strange sense of nostalgia, I swung the bat—or rather, the sword case.

[P140]
*Whack! Whack! Whack! Crack!*

[P141]
“Guh!”

[P142]
“Don’t move. You’ll hurt your bones. All right, again.”

[P143]
*Whack! Whack! Whack!*

[P144]
It must have been a rare sight for everyone filling Honghwa Inn. The heirs of the Five Gates of Shanxi were crawling across the floor like grubs.

[P145]
There were even two women among them.

[P146]
The whispers of the people surrounding us cut into my ears.

[P147]
“Is that really okay?”

[P148]
“I know, right? Even if they are the Five Gates of Shanxi… Couldn’t this turn into one of those big fights over Murim gratitude and grudges?”

[P149]
“Don’t be so clueless. Are you really that out of touch with what’s happening these days? Maybe things would be different if the Mount Heng Sword Sect were still standing, but to stop the Jin Family of Taiyuan now, every small and medium-sized sect in Shanxi would have to join forces—and even then, they might not manage it.”

[P150]
“It’s that bad?”

[P151]
“They might have the numbers if they gathered everyone, but the caliber is completely different. You only have to look at the Sleeping Dragon of Shanxi over there to know that.”

[P152]
“That’s true. Those Five Gates heirs swaggered around acting so important, but they’re completely worthless in front of the Sleeping Dragon of Shanxi.”

[P153]
“If you think about it, they were the ones who picked the fight first.”

[P154]
“That’s true, too.”

[P155]
“And since we’re on the subject, there’s something rotten about all those people who call themselves the Five Gates of Shanxi these days.”

[P156]
“Rotten?”

[P157]
“They call themselves an orthodox faction, but they’re really just sucking the marrow out of ordinary people without anyone noticing. Just look at the Seongun Escort Bureau. How many complaints have merchants made about them?”

[P158]
“Were all those rumors true?”

[P159]
“What about the Jin Family of Taiyuan? When there was a famine ten years ago, they released relief grain. Long before that, they even held off the Demonic Cult. Those bastards were vicious murderers who went around killing ordinary people like us. If not for the Jin Family of Taiyuan…”

[P160]
“Ugh. I don’t even want to think about it.”

[P161]
“That’s right. I also heard it was the Jin Family of Taiyuan that drove off the mounted bandits who came over from Gaoyuan this time.”

[P162]
“Is there anyone who hasn’t heard that rumor yet? They say the Heaven Shaking Sword and the Sleeping Dragon of Shanxi slaughtered every last one of them.”

[P163]
“My goodness.”

[P164]
“So even if another war breaks out, what’s there to worry about? I swear, if the Five Gates of Shanxi try to make an issue of this, I’ll join the Jin Family of Taiyuan and fight alongside them!”

[P165]
“Oh!”

[P166]
“That’s some impressive chivalrous spirit for such a young man. Now that I’ve heard you out, I think you’re right. Here, have a drink on me!”

[P167]
*Whack! Whack! Whack!*

[P168]
I had turned three of the four young prodigies into grubs when I turned my head toward the voices.

[P169]
They were defending the Jin Family of Taiyuan with such passion that, by the time I finished listening, I almost wanted to buy them a drink.

[P170]
*In terms of mindset, he’s already one of our Jin Family.*

[P171]
If his Level were high enough, he’d be my first pick for recruitment. Smiling with satisfaction, I checked the Level Window of the great orator.

[P172]
> **System**
>
> **Level 15: Jang Childeuk**

[P173]
“…What the fuck?”

[P174]
*Jang Childeuk? The Jang Childeuk I know?*

[P175]
Looking again, I realized that I definitely knew the face.

[P176]
He was the servant who had brought us meals every day while I was receiving one-on-one intensive training from Jin Mukyung.

[P177]
That Jang Childeuk was the great orator’s true identity.

[P178]
*Holy shit. Goose bumps.*

[P179]
No wonder he had been taking the Jin Family’s side so aggressively.

[P180]
He hadn’t said anything incorrect, of course, but manipulating public opinion like this…

[P181]
Just as I trembled at the feeling that I had uncovered some enormous conspiracy in the political world, someone spoke up.

[P182]
“Um…”

[P183]
It was Cheongpung, the one person I had momentarily forgotten. He opened his mouth with his clear eyes shining.

[P184]
“There’s still one person left.”

[P185]
“Ah.”

[P186]
The last man lying face down flinched. Cheongpung seemed innocent in his own way, but he was also strangely frightening.

[P187]
Not that I had any intention of going easy on him just because he was last.

[P188]
“I was just about to hit him.”

[P189]
I was about to swing the sword case when Cheongpung spoke again.

[P190]
“Excuse me. May I ask you one difficult favor?”

[P191]
“We’re out of candied hawthorn skewers[^2] now.”

[P192]
[^2]: Candied hawthorn skewers are a traditional snack of fruit skewers coated in hardened sugar.

[P193]
“That’s not it. I, uh…”

[P194]
Cheongpung hesitated, then quietly pointed at the sword case.

[P195]
“I’d like to try hitting the last gentleman once.”

[P196]
“What?”

[P197]
“I’ve never done anything like this before…”

[P198]
“…”

[P199]
I had seen every kind of nutcase in my life, but this was my first time seeing a first-experience villain.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 산서오문   | **Five Gates of Shanxi**         |
| 일류     | **First Rate**    |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 표국     | **Escort Bureau**                            |
| 소국주    | **Young Bureau Head**                        |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 형장      | **Brother** / **Brother [Name]**                                |
| 공자      | **Young Master**                                                |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 135,
  "passed": true,
  "metrics": {
    "source_characters": 6081,
    "translation_characters": 13782,
    "length_ratio": 2.266,
    "source_paragraphs": 191,
    "translation_paragraphs": 199
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "후기지수",
        "preferred": "young prodigy / rising martial artist"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "명성",
        "preferred": "Fame"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "홍화",
        "romanization": "honghwa"
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
