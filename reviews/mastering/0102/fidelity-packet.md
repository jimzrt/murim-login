# Fidelity Gate — Chapter 102

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
  1|＃102화
  2|
  3|
  4|
  5|사람마다 전문 분야가 다르기 마련이다.
  6|
  7|게이트에서의 포메이션과 위기 상황이 닥쳤을 때 취해야 할 행동, 몬스터들의 약점 등을 달달 꿰고 있는 내가 법 관련 사항에서는 문외한인 것도 같은 맥락이었다.
  8|
  9|“고생하셨습니다.”
 10|
 11|“법무사님도요.”
 12|
 13|각진 뿔테 안경을 쓴 이 남자는 내게 부동산 매매를 위임받은 법무사다. 맞은편에선 집주인과 공인중개사 아저씨가 인사를 나누며 막 자리에서 일어나고 있었다.
 14|
 15|“계약 축하해요. 젊은 분이 성공하셨네.”
 16|
 17|“아, 네. 감사합니다.”
 18|
 19|집주인과 악수를 나누며 그제야 새로운 사실을 깨달았다.
 20|
 21|‘이젠 내 집이구나.’
 22|
 23|그리고 우리 가족의 집이다. 자그마치 11년 만에 되찾은.
 24|
 25|
 26|
 27|* * *
 28|
 29|
 30|
 31|좁은 방 안을 돌아봤다.
 32|
 33|오래전 스프링이 나간 침대. 몇 벌 들어가지도 않는 작은 옷장과 군데군데 칠이 벗겨진 책상 하나. 그 위에 놓인 소형 TV.
 34|
 35|두고 가야 할 것을 제외하고 옷이며 자질구레한 물건들을 주워 담으니 종이 박스 하나를 꽉 채웠다.
 36|
 37|‘겨우 박스 하나.’
 38|
 39|지난 7년이 그 안에 담겨 있다. 어쩐지 먹먹한 심정이 되어 하염없이 방을 둘러보고 있던 그때였다.
 40|
 41|“가냐?”
 42|
 43|굳이 돌아보지 않아도 알 수 있다.
 44|
 45|내 7년에서 빼놓을 수 없는 사람이니까.
 46|
 47|“응.”
 48|
 49|“집은?”
 50|
 51|“구했으니까 나가지.”
 52|
 53|“새끼, 빠르네. 가족들은 이미 새집으로 이사했고?”
 54|
 55|“아니. 아직까지는 비밀이야. 내가 먼저 들어가서 살다가 동생 수능 끝나면 알려 주려고.”
 56|
 57|“하긴, 한창 중요한 시기니까.”
 58|
 59|“응. 그 전에 리모델링도 해야 하고.”
 60|
 61|잠깐 침묵이 흘렀다. 우리 둘은 굳이 대화를 나누지 않아도 편안한 사이, 눈빛만으로도 서로의 마음을 읽을 수 있는 사이지만 지금은 무슨 말을 해야 할지 모르겠다.
 62|
 63|“형.”
 64|
 65|“야, 야. 됐어. 분위기 잡지 마.”
 66|
 67|진호 형이 내 등을 세게 두드렸다.
 68|
 69|“무슨 전학 가는 초등학생도 아니고. 너 이사 가면 내 얼굴 안 볼 거냐?”
 70|
 71|“봐야지. 꼭 봐야지.”
 72|
 73|“그럼 됐어. 어차피 나도 오늘 중으로 짐 뺀다.”
 74|
 75|“형도?”
 76|
 77|“지난번에 말했잖아. 기억 안 나냐?”
 78|
 79|“아, 그랬었지.”
 80|
 81|몇 년씩이나 동고동락한 진호 형만 고시원에 두고 가는 게 마음에 걸렸는데, 이제야 한결 편해진다.
 82|
 83|“형은 어디로 이사 가는데?”
 84|
 85|“그냥 뭐 아는 사람 집에 얹혀살게 됐어. 너 이번에 산 집이 어디 있다고 했지?”
 86|
 87|“고양시. 여기서 30분 거리라 그렇게 멀진 않아.”
 88|
 89|“고양시?”
 90|
 91|진호 형이 눈을 크게 떴다.
 92|
 93|“나도 그 근처야, 인마!”
 94|
 95|“어? 진짜?”
 96|
 97|뜻밖의 이야기에 내심 반가웠다. 이제는 하루라도 안 보면 섭섭한 얼굴이다. 사는 곳이 가까우면 앞으로도 자주 만날 수 있겠지.
 98|
 99|“형, 그럼 정확한 주소가 어디…….”
100|
101|막 주소를 물어보려던 찰나, 주머니에 넣어 둔 스마트폰이 울렸다. 전화를 받으니 수화기 너머로 걸걸한 목소리가 흘러나온다.
102|
103|- 어, 진태경 씨 맞죠? 지금 고시원 앞이에요.
104|
105|“아, 예. 기사님.”
106|
107|미리 불러 둔 개인 이삿짐 기사다. 흘끗 창문 밖을 바라보니 고시원 앞에서 기다리고 있는 파란색 용달차 한 대가 보였다.
108|
109|- 짐 많아요? 무거운 거면 제가 도와드리고.
110|
111|“아닙니다. 제가 들고 갈게요.”
112|
113|짐이라고 해 봤자 두 개뿐이다.
114|
115|소소한 물건들을 챙겨 넣은 종이 박스, 그리고…….
116|
117|‘캡슐.’
118|
119|로그아웃 기능이 활성화된 지금은 굳이 캡슐을 사용하지 않아도 무림과 현대를 넘나들 수 있다.
120|
121|이제는 공간만 차지하는 애물단지가 됐지만 내게는 그 어떤 것보다 특별한 의미가 있었다. 짐이 별로 없는데도 용달차를 부른 것 역시 다 이거 때문이다.
122|
123|‘이 캡슐이 아니었다면 어떻게 됐을까.’
124|
125|천천히 캡슐 표면을 쓰다듬었다. 손을 통해 전해지는 금속의 차가움과 거칠거칠한 촉감.
126|
127|이 낡은 캡슐 하나가 내 인생을 송두리째 바꿨다.
128|
129|아, 맞다. 거기에 큰 역할을 해 준 사람도 있었지.
130|
131|“진호 형.”
132|
133|“응?”
134|
135|어리둥절한 표정을 보고 있자니 실소가 절로 나온다.
136|
137|그날, 진호 형이 술에 떡이 되지 않았더라면 내가 캡슐에 들어갈 일도 없었을 것이다.
138|
139|“아냐, 아무것도.”
140|
141|“싱겁기는. 그나저나 너 이제 가 봐야 하는 거 아니냐? 밖에 트럭 서 있던데.”
142|
143|“어. 그런 김에 거기 박스 좀 들어 주라. 난 캡슐 들어야 해서 손이 부족해.”
144|
145|“으, 응?”
146|
147|“뭐야, 그 반응은? 이사 가는 동생을 위해서 박스 하나 못 들어 줘?”
148|
149|“그게 아니고…… 어우, 생각해 보니까 나도 짐 싸야 되네. 귀찮아도 그냥 한 번 왔다 갔다 해라. 그럼 수고!”
150|
151|“…….”
152|
153|미꾸라지처럼 빠져나가는 것 보소. 나는 슬금슬금 멀어지는 진호 형의 뒷모습을 바라보다 결국 박스를 집어 들었다.
154|
155|기다림에 지친 이삿짐 아저씨의 클랙슨 소리가 귀를 때린다.
156|
157|빵빵!
158|
159|“예, 지금 내려가요!”
160|
161|
162|
163|* * *
164|
165|
166|
167|“헌터신가 봐요?”
168|
169|계속 나를 흘끗거리던 이삿짐 아저씨가 말을 던졌다. 박스와 캡슐을 실은 용달차는 내비게이션의 안내에 따라 새로운 집을 향해 달리고 있었다.
170|
171|“어떻게 아셨어요?”
172|
173|“그거야 보면 딱 알죠. 나도 예전에는 헌터였거든. F급.”
174|
175|“어, 정말요?”
176|
177|“아마 내가 손님보다 훈련소 기수로는 선배일걸? 아, 꼰대짓 하려는 건 아니에요. 딱 한 달 만에 때려치우고 자격증 반납한 놈이 그러는 것도 우습잖아.”
178|
179|아저씨가 넋두리처럼 말을 이었다.
180|
181|“헌터 훈련소 때는 할 만했어요. F급이지만 헌터가 된다는 자부심도 있었고. 그런데 수료 후에 길드 들어가자마자 사고가 터진 거지.”
182|
183|게이트에서 사고가 터졌다는 말은 사망과 동의어다.
184|
185|설령 팔다리가 날아가도 돈만 있다면 회복할 수 있는 세상이니까. 헌터들끼리는 그 정도를 사고라고 말하진 않는다.
186|
187|“같이 입사한 훈련소 동기 녀석이었는데…… 어어, 하는 사이에 끌려가더니 그렇게 죽었어. 무슨 수를 써서라도 쫓아가서 구했어야 했는데 차마 발이 안 떨어지더라고. 그 녀석 장례식 마치고 은퇴 신청했지. 나 같은 놈은 레이드 뛰면 안 되니까.”
188|
189|그는 애써 덤덤한 척하려 했지만 잘게 떨리는 목소리까지 감추지는 못했다.
190|
191|“이거 헌터 손님 앞에서 너무 재수 없는 소리를 했네. 이게 뭐 좋은 얘기라고. 미안합니다.”
192|
193|“별말씀을요.”
194|
195|아저씨의 심정이 충분히 이해가 갔다.
196|
197|나도 비슷한 경험이 있었으니까. 가족에 대한 책임감이 없었다면, 옆에서 위로해 준 진호 형이 없었다면 2년 전 그때 은퇴했을지도 모른다.
198|
199|‘그럼 내 인생도 크게 달라졌겠지.’
200|
201|헌터는 치열한 직업이다. 언론에서는 인류의 수호자요, 방패라며 치켜세워 주지만 늘 죽음을 옆에 끼고 살아간다.
202|
203|- 50m 앞에서 우회전입니다.
204|
205|내비게이션의 안내 음성에 아저씨가 멈칫하더니 중얼거렸다.
206|
207|“어, 그러고 보니까 여기 안전 구역이네.”
208|
209|“맞으니까 쭉 가 주세요.”
210|
211|“아, 예.”
212|
213|용달차는 얼마 지나지 않아 목적지에 도착했다.
214|
215|푸른색 지붕의 2층짜리 단독주택. 너무 높지 않은 돌담과 잔디가 깔린 마당이 보인다. 이 집을 처음 봤던 며칠 전과는 또 느낌이 달랐다.
216|
217|‘우리 집이라 그런 거겠지.’
218|
219|우리 집.
220|
221|곱씹을수록 기분 좋은 말이다. 물론 집이 워낙 예뻐서 그런 것도 있겠지만.
222|
223|“이야…… 집 좋네.”
224|
225|운전석에서 내린 아저씨가 혀를 내둘렀다. 다른 사람의 입에서 나오는 소리는 더 달콤하게 들리는 법. 참으려고 해도 자꾸 입꼬리가 올라간다.
226|
227|“잘나가는 헌터인가 봐요. 내 꿈이 이런 집에서 사는 거였는데.”
228|
229|“저도요.”
230|
231|“소원 성취 하셨네. 좋으시겠어.”
232|
233|당연히 좋아 죽지.
234|
235|연신 감탄사를 터트리며 돌담도 만져 보고, 잔디밭도 바라보던 그가 물었다.
236|
237|“잠깐 들어가서 구경해 봐도 될까요? 캡슐도 옮겨 드릴 겸.”
238|
239|“네, 그러세요.”
240|
241|의도치 않게 새집의 첫 손님이 된 이삿짐 아저씨가 짐칸으로 올라갔다. 캡슐을 옮기기 위해서다.
242|
243|“그런데 그거 무게가 꽤 나갈 텐데.”
244|
245|“괜찮아요. 저도 많이 옮겨 봐서 알아요. 게임 캡슐 무게야 거기서 거긴데요 뭘.”
246|
247|“아니, 진짜 무거울 건데.”
248|
249|아까 직접 들어 봐서 안다. 근력 스탯이 세 자리가 넘어가는 나한테도 적당히 묵직한 정도였는데 저 아저씨라면 더더욱 얘기가 다르다.
250|
251|“사장님, 그냥 제가 옮길게요.”
252|
253|캡슐을 끌어안은 그가 씩 웃었다.
254|
255|“에헤이. 너무 무시하신다. 내가 그래도 왕년에 헌터였는데 겨우 이 정도로…… 끄응!”
256|
257|“오오.”
258|
259|역시 전직 헌터. 한 번에 들긴 들었다.
260|
261|약간 변한 게 있다면 아저씨의 얼굴에서 웃음이 사라졌다는 것 정도?
262|
263|“먼저 가서 문 열어요. 빨리!”
264|
265|긴박한 목소리에 후다닥 달려가 대문과 현관문을 열어젖혔다. 이게 뭐라고 나까지 긴장되는지 모르겠다.
266|
267|“그냥 제가 들…….”
268|
269|“비켯!”
270|
271|“아, 네.”
272|
273|경보에 버금가는 속도로 거실에 들어간 그가 비명처럼 외쳤다.
274|
275|“어느 방!”
276|
277|“캡슐은 2층…….”
278|
279|“뭣이?”
280|
281|“……에 놓으려고 했는데 그냥 가까운 방에 놔 주세요.”
282|
283|다행히 방문은 열려 있었다. 쿵, 소리와 함께 캡슐을 내려놓은 아저씨가 숨을 헐떡였다.
284|
285|“이거, 왜, 이렇게, 허억. 무거워요?”
286|
287|“…….”
288|
289|내가 무겁다고 말해 주지 않았나?
290|
291|
292|
293|* * *
294|
295|
296|
297|이삿짐 아저씨가 떠나자마자 거실 소파에 털썩 걸터앉았다.
298|
299|한 번에 잔금을 지급하는 조건으로 전 주인에게 양도받은 가구 중 하나다.
300|
301|‘몇 달 동안은 혼자 살아야 하니까.’
302|
303|가족들에게는 다시 부천으로 돌아간다고 말해 둔 상태.
304|
305|하연이의 수능 전까지는 이곳에서 먹고 자며 출퇴근을 할 작정이다.
306|
307|‘집 리모델링도 하고, 차도 사고. 아, 어차피 차는 길드에서 지원해 준다고 했으니 면허부터 따야겠구나.’
308|
309|그밖에도 할 일이 태산이다. 그러나 지치기는커녕 힘이 솟았다. 전에는 하고 싶어도 못 했던 일들이니까.
310|
311|게이트와 고시원을 오가며 고생만 하던 게 불과 몇 달 전인데, 참 많은 게 바뀌었다.
312|
313|‘많이 컸다, 진태경.’
314|
315|문득 생각나는 한 사람이 있다.
316|
317|적지 않은 나이에도 늘 소년처럼 웃던 사람. 아내에게, 자식들에게 최선을 다하며 친구처럼 다가와 주었던 그가 떠오른다.
318|
319|‘아버지, 나 집 샀어요. 예전에 우리가 살던 곳은 이미 없더라고. 그래도 이 정도면 잘한 거 맞죠?’
320|
321|아이처럼 자랑하고 싶어도 칭찬해 줄 사람은 이미 오래전에 떠났다. 내가 할 수 있는 거라곤 마음속으로 닿지 않을 말을 되뇌는 것뿐이었다.
322|
323|그렇게 시간이 얼마나 흘렀을까?
324|
325|정신을 차려 보니 벌써 오후 여덟 시. 여름철의 해가 서서히 저물고 있었다.
326|
327|‘휴가 마지막 날이 이렇게 끝나네.’
328|
329|장장 일주일의 휴가. 상동 길드와 엮여 소란스럽기도 했지만 헌터 생활을 시작한 이래 처음으로 누리는 최고의 휴식이었다.
330|
331|이제는 다시 일상으로 돌아가야 할 시간이다.
332|
333|‘정확히 열두 시간 후에 말이지.’
334|
335|앉아 있던 소파에 반듯이 누웠다. 캡슐에 들어갈까 하는 생각도 들었지만 이내 지워 버렸다.
336|
337|11년 만에 돌아온 집이다. 이번만큼은 후덥지근한 캡슐 안이 아니라 우리 집 거실에서 깨어나고 싶었다.
338|
339|‘로그인(Login).’
340|
341|내 부름에 시스템이 응답한다.
342|
343|띠링.
344|
345|
346|
347|[무림]에 접속하시겠습니까?
348|
349|Y   /   N
350|
351|
352|
353|물론 내 대답은 예스다.
354|
355|
356|
357|* * *
358|
359|
360|
361|진태경이 의식을 잃은 지 한참 후, 현관문 옆 방 안에서는 누구도 예상 못 한 일이 벌어지고 있었다.
362|
363|치이이익.
364|
365|마치 거대한 알처럼 보이는 금속 물체, 캡슐의 문이 천천히 열리기 시작한 것이다.
366|
367|가장 먼저 드러난 것은 두 발이었다.
368|
369|종아리까지 덮는 긴 스포츠 양말에 프린팅된 붉은 글씨.
370|
371|
372|
373|희망 고시원 조기축구회
374|
375|
376|
377|이어 반쯤 말아 올린 추리닝 바지를 지나 희고 마른 양손까지 드러났다. 성서라도 되는 것처럼 꼭 붙잡고 있는 책 표지가 창밖으로 흘러들어온 노을빛을 받아 번쩍 빛난다.
378|
379|
380|
381|행정고시 완전 정복
382|
383|
384|
385|그리고 마침내 드러나는 그의 얼굴.
386|
387|장장 몇 시간의 고통을 인내한 그는 사도세자처럼 초췌했으나 알을 깨고 태어난 박혁거세처럼 후련해 보였다.
388|
389|바짝 마른 입술 사이로 메마른 음성이 새어 나온다.
390|
391|“이곳이 나의 새로운 보금자리인가…….”
392|
393|넓은 방을 바라보는 성진호의 입가에 흐뭇한 웃음이 맺혔다.
```

## Assembled English

```markdown
[P1]
# Chapter 102

[P2]
Everyone has their own area of expertise.

[P3]
I knew Gate formations, how to respond in a crisis, and the weaknesses of various monsters like the back of my hand. By the same token, I knew next to nothing about legal matters.

[P4]
“Thank you for your hard work.”

[P5]
“You too.”

[P6]
The man in the angular horn-rimmed glasses was the legal scrivener I had hired to handle the purchase of the house. Across from me, the homeowner and the realtor were exchanging farewells and getting to their feet.

[P7]
“Congratulations on the contract. You’ve done well for yourself at such a young age.”

[P8]
“Ah, yes. Thank you.”

[P9]
As I shook hands with the homeowner, something finally sank in.

[P10]
*This is my house now.*

[P11]
And it was my family’s house.

[P12]
A home we had reclaimed after no less than eleven years.

[P13]
* * *

[P14]
I looked around the cramped room.

[P15]
The bed whose springs had given out long ago. A small wardrobe that could barely hold a few outfits. A desk with paint peeling off in places, with a small TV sitting on top.

[P16]
Once I packed my clothes and assorted belongings, aside from the things I had to leave behind, they filled a single cardboard box.

[P17]
*Just one box.*

[P18]
The past seven years were contained inside it. I was staring around the room, my chest strangely tight, when a voice came from behind me.

[P19]
“You leaving?”

[P20]
I knew who it was without turning around.

[P21]
He was someone I couldn’t leave out of my seven years.

[P22]
“Yeah.”

[P23]
“What about the house?”

[P24]
“I found one, so I’m moving out.”

[P25]
“Bastard, that was fast. Has your family already moved into the new place?”

[P26]
“No. It’s still a secret. I’m planning to move in first and tell them after my sister finishes her college entrance exam.”

[P27]
“Fair enough. She’s at an important stage.”

[P28]
“Yeah. I need to remodel the place first, too.”

[P29]
A brief silence followed. We were comfortable enough not to need conversation, the kind of people who could read each other’s thoughts from a look alone. But right now, neither of us seemed to know what to say.

[P30]
“Hyung.”

[P31]
“Hey, hey. That’s enough. Don’t make this all sentimental.”

[P32]
Jinho hyung slapped me hard on the back.

[P33]
“You’re not some elementary school kid transferring schools. Just because you’re moving, you’re not going to stop seeing me, are you?”

[P34]
“Of course I’ll see you. I definitely will.”

[P35]
“Then it’s fine. Besides, I’m moving my stuff out by the end of today, too.”

[P36]
“You are?”

[P37]
“I told you last time. Don’t you remember?”

[P38]
“Oh, right. You did.”

[P39]
I had felt bad about leaving Jinho hyung alone in the goshiwon after all the years we had spent living together. Now I finally felt a little more at ease.

[P40]
“Where are you moving?”

[P41]
“Well, I ended up crashing at someone I know’s place. Where did you say the house you bought was?”

[P42]
“Goyang. It’s only thirty minutes from here, so it’s not that far.”

[P43]
“Goyang?”

[P44]
Jinho hyung’s eyes widened.

[P45]
“I’m in that area too, you punk!”

[P46]
“Huh? Really?”

[P47]
The unexpected news secretly pleased me. By now, I missed his face if I went even a day without seeing it. If we lived close by, we could still meet often.

[P48]
“Hyung, then what’s the exact address—”

[P49]
Just as I was about to ask, the smartphone in my pocket rang. When I answered, a gravelly voice came through the receiver.

[P50]
—Hello, is this Mr. Jin Taekyung? I’m in front of the goshiwon right now.

[P51]
“Ah, yes. Driver.”

[P52]
It was the private moving-truck driver I had called in advance. I glanced out the window and saw a blue light truck waiting in front of the goshiwon.

[P53]
—Do you have a lot of stuff? If anything’s heavy, I can help you carry it.

[P54]
“No, it’s fine. I’ll carry it myself.”

[P55]
I only had two things to move.

[P56]
A cardboard box filled with small belongings, and…

[P57]
*The capsule.*

[P58]
Now that the Logout function had been activated, I no longer needed the capsule to travel between Murim and the modern world.

[P59]
It had become nothing more than a bulky nuisance, but it meant more to me than anything else. It was the only reason I had called a moving truck despite having so little luggage.

[P60]
*What would have happened if it weren’t for this capsule?*

[P61]
I slowly ran my hand over its surface. The coldness of the metal and its rough texture traveled through my fingers.

[P62]
This one old capsule had completely changed my life.

[P63]
*Oh, right. Someone else played a big part in that too.*

[P64]
“Jinho hyung.”

[P65]
“Yeah?”

[P66]
A laugh escaped me at his puzzled expression.

[P67]
If Jinho hyung hadn’t gotten plastered that day, I never would have entered the capsule in the first place.

[P68]
“Never mind. It’s nothing.”

[P69]
“You’re no fun. Anyway, shouldn’t you get going? There’s a truck waiting outside.”

[P70]
“Yeah. Since you’re here, carry that box down for me. I have to carry the capsule, so I don’t have a free hand.”

[P71]
“Uh, what?”

[P72]
“What’s with that reaction? Can’t you carry one box for your little brother who’s moving away?”

[P73]
“That’s not it… Ah, now that I think about it, I need to pack my own stuff too. Even if it’s a hassle, just make one trip back and forth. Well, good luck!”

[P74]
“……”

[P75]
Look at him slithering away like a loach.

[P76]
I watched Jinho hyung’s back inch into the distance, then finally picked up the box myself.

[P77]
The moving driver, tired of waiting, honked the truck’s horn. The sound struck my ears.

[P78]
Honk, honk!

[P79]
“Yes, I’m coming down!”

[P80]
* * *

[P81]
“Are you a Hunter?”

[P82]
The moving driver, who had been sneaking glances at me, finally spoke. With the box and capsule loaded in the back, the truck followed the navigation toward my new home.

[P83]
“How did you know?”

[P84]
“You can tell at a glance. I used to be a Hunter, too. F-rank.”

[P85]
“Oh, really?”

[P86]
“I’m probably your Senior by training-center class. Ah, I’m not trying to pull rank. It’d be ridiculous for a guy who quit after exactly one month and handed back his license to act like some old-timer.”

[P87]
The driver continued as though airing a long-held grievance.

[P88]
“Being a Hunter at the training center was manageable. Even though I was only F-rank, I took pride in becoming a Hunter. But the moment I joined a Guild after graduating, an accident happened.”

[P89]
An accident at a Gate was synonymous with death.

[P90]
Even if someone lost an arm or a leg, they could recover as long as they had enough money. Hunters didn’t call something like that an accident.

[P91]
“He was one of my training-center classmates, and he joined the Guild at the same time as me… Before I knew what was happening, he was dragged away and died just like that. I should have chased after him and saved him, no matter what it took, but I couldn’t make my feet move. After his funeral, I applied for retirement. Someone like me had no business going on raids.”

[P92]
He tried to sound calm, but he couldn’t hide the slight tremor in his voice.

[P93]
“Listen to me saying something so ominous in front of a Hunter customer. It’s not even a pleasant story. Sorry about that.”

[P94]
“Don’t worry about it.”

[P95]
I understood how he felt.

[P96]
I had experienced something similar. If I hadn’t felt responsible for my family, and if Jinho hyung hadn’t been there to comfort me, I might have retired two years ago.

[P97]
*Then my life would have turned out completely differently.*

[P98]
Being a Hunter was a brutal profession. The media praised them as humanity’s guardians and shields, but they lived with death always at their side.

[P99]
—Turn right in fifty meters.

[P100]
The driver paused at the navigation’s voice, then muttered, “Oh, come to think of it, this is a safe zone.”

[P101]
“That’s right. Just keep going.”

[P102]
“Ah, yes.”

[P103]
The truck arrived at its destination soon afterward.

[P104]
A two-story detached house with a blue roof. A low stone wall and a yard covered in grass. It felt different from when I had first seen it a few days ago.

[P105]
*It must be because it’s ours now.*

[P106]
Our house.

[P107]
The more I repeated those words in my head, the better they sounded. Of course, the fact that the house itself was beautiful probably helped.

[P108]
“Wow… It’s a nice house.”

[P109]
The driver climbed out of the cab and clicked his tongue in admiration. Praise always sounded sweeter coming from someone else. No matter how hard I tried to suppress it, the corners of my mouth kept rising.

[P110]
“You must be a successful Hunter. Living in a house like this was my dream.”

[P111]
“Mine too.”

[P112]
“Your wish came true. You must be happy.”

[P113]
*Of course. I was ecstatic.*

[P114]
The driver continued exclaiming over the place, touching the stone wall and looking over the lawn, before asking,

[P115]
“Would it be all right if I took a quick look inside? I can help move the capsule while I’m at it.”

[P116]
“Sure. Go ahead.”

[P117]
The moving driver became the new house’s first guest by accident as he climbed into the truck bed to move the capsule.

[P118]
“That thing must weigh quite a bit.”

[P119]
“It’s fine. I’ve moved plenty of them, so I know. Game capsules all weigh about the same.”

[P120]
“No, it’s seriously heavy.”

[P121]
I knew because I had lifted it myself earlier. It had felt reasonably hefty even to me, with my Strength stat in the triple digits. For the driver, it would be a different story entirely.

[P122]
“Boss, I’ll move it myself.”

[P123]
The driver wrapped his arms around the capsule and grinned.

[P124]
“Come on. You’re underestimating me. I was a Hunter back in the day. Something like this is—nnngh!”

[P125]
“Oh, wow.”

[P126]
As expected of a former Hunter, he did manage to lift it in one go.

[P127]
The only change was that the smile had vanished from his face.

[P128]
“Go ahead and open the doors. Quickly!”

[P129]
At the urgency in his voice, I dashed ahead and threw open the front gate and the front door. I had no idea why I was getting nervous too.

[P130]
“I can carry it—”

[P131]
“Move!”

[P132]
“Ah, yes.”

[P133]
He barreled into the living room at a speed fit for an alarm and screamed, “Which room?!”

[P134]
“I was going to put the capsule upstairs…”

[P135]
“What?!”

[P136]
“…but just leave it in the nearest room.”

[P137]
Fortunately, the door to one of the rooms was already open. The driver set the capsule down with a thud and began panting.

[P138]
“Why… is this… huff… so heavy?”

[P139]
“……”

[P140]
Hadn’t I told him it was heavy?

[P141]
* * *

[P142]
As soon as the moving driver left, I dropped onto the living room sofa.

[P143]
It was one of the pieces of furniture the previous owner had transferred to me on the condition that I pay the remaining balance all at once.

[P144]
*I’ll have to live alone for a few months.*

[P145]
I had told my family that I was going back to Bucheon.

[P146]
Until Hayeon finished her college entrance exam, I planned to eat and sleep here while commuting to work.

[P147]
*I need to remodel the house and buy a car too. Ah, the Guild said they’d provide me with a car anyway, so I need to get my license first.*

[P148]
There was a mountain of other things to do. But instead of feeling tired, I felt energized. These were all things I hadn’t been able to do before, no matter how much I wanted to.

[P149]
It had only been a few months since I had done nothing but suffer while going back and forth between Gates and the goshiwon, yet so much had changed.

[P150]
*You’ve come a long way, Jin Taekyung.*

[P151]
One person suddenly came to mind.

[P152]
A man who had always smiled like a boy despite his age. A man who had done his best for his wife and children and approached them like a friend.

[P153]
*Dad, I bought a house. The place we used to live in was already gone. But I did well enough, right?*

[P154]
I wanted to brag about it like a child, but the person who would have praised me had passed away long ago. All I could do was repeat words in my heart that would never reach him.

[P155]
How much time passed like that?

[P156]
When I came to my senses, it was already eight in the evening. The summer sun was slowly setting.

[P157]
*So this is how my last day of vacation ends.*

[P158]
An entire week of vacation. It had been hectic because of everything involving the Sangdong Guild, but it was still the best rest I had enjoyed since becoming a Hunter.

[P159]
Now it was time to return to my daily life.

[P160]
*In exactly twelve hours.*

[P161]
I lay flat on the sofa where I had been sitting. I briefly considered entering the capsule, but soon dismissed the thought.

[P162]
After eleven years, I finally had a home again. Just this once, I wanted to wake up in our living room instead of inside that stuffy capsule.

[P163]
*Login.*

[P164]
The System responded to my call.

[P165]
Ding.

[P166]
> **System**
>
> Would you like to connect to Murim?
>
> Y / N

[P167]
Of course, my answer was yes.

[P168]
* * *

[P169]
Long after Jin Taekyung lost consciousness, something no one could have expected was happening in the room beside the front door.

[P170]
Hissssss.

[P171]
The door of the metal object that looked like a gigantic egg—the capsule—slowly began to open.

[P172]
The first thing to emerge was a pair of feet.

[P173]
Red letters were printed across a pair of long athletic socks that reached up to the calves.

[P174]
**Hope Goshiwon Early-Morning Soccer Club**

[P175]
Next came sweatpants rolled up halfway, followed by a pair of pale, skinny hands. The cover of the book he clutched tightly, as though it were scripture, gleamed in the sunset pouring through the window.

[P176]
**Complete Mastery of the Civil Service Exam**

[P177]
And finally, his face emerged.

[P178]
After enduring several long hours of agony, he looked as haggard as Crown Prince Sado[^1] yet as relieved as Park Hyeokgeose emerging from an egg.[^2]

[P179]
A parched voice slipped between his bone-dry lips.

[P180]
“Is this my new nest…?”

[P181]
As Seong Jinho gazed around the spacious room, a satisfied smile spread across his lips.

[P182]
[^1]: Crown Prince Sado was an eighteenth-century Joseon royal who died after being confined in a wooden rice chest.

[P183]
[^2]: Park Hyeokgeose is the legendary founder of the ancient Korean kingdom of Silla, said to have been born from an egg.
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
# Chapter 102

[P2]
Everyone has their own area of expertise.

[P3]
I knew the formations used at Gates, what to do when a crisis struck, and the weaknesses of various monsters like the back of my hand. My being clueless about legal matters was simply another example of everyone having their own specialty.

[P4]
“Thank you for your hard work.”

[P5]
“You too.”

[P6]
The man in the angular horn-rimmed glasses was the legal scrivener I had hired to handle the real-estate transaction. Across from me, the homeowner and the licensed realtor were exchanging farewells and getting to their feet.

[P7]
“Congratulations on the contract. A young man making it big.”

[P8]
“Ah, yes. Thank you.”

[P9]
As I shook hands with the homeowner, I realized something for the first time.

[P10]
*This is my house now.*

[P11]
And it was my family’s house.

[P12]
A home we had reclaimed after no less than eleven years.

[P13]
* * *

[P14]
I looked around the cramped room.

[P15]
The bed, whose springs had broken long ago. A small wardrobe that could barely hold a few outfits. A desk with its paint peeling off in places. A small TV sitting on top of it.

[P16]
After packing up my clothes and assorted belongings, excluding the things I had to leave behind, I filled one cardboard box.

[P17]
*Just one box.*

[P18]
The past seven years were contained inside it. I was staring around the room with a strange tightness in my chest when a voice came from behind me.

[P19]
“You leaving?”

[P20]
I knew who it was without turning around.

[P21]
He was someone I couldn’t leave out of my seven years.

[P22]
“Yeah.”

[P23]
“What about the house?”

[P24]
“I found one, so I’m moving out.”

[P25]
“Bastard, that was fast. Has your family already moved into the new place?”

[P26]
“No. It’s still a secret. I’m planning to move in first and tell them after my sister finishes her college entrance exam.”

[P27]
“Fair enough. She’s at an important stage.”

[P28]
“Yeah. I need to remodel the place first, too.”

[P29]
A brief silence followed. We were comfortable enough not to need conversation, the kind of people who could read each other’s thoughts from a look alone. But right now, neither of us seemed to know what to say.

[P30]
“Hyung.”

[P31]
“Hey, hey. Don’t set the mood.”

[P32]
Jinho hyung slapped me hard on the back.

[P33]
“It’s not like you’re an elementary school kid transferring schools. Just because you’re moving, you’re not going to stop seeing me, are you?”

[P34]
“Of course I’ll see you. I definitely will.”

[P35]
“Then it’s fine. Besides, I’m moving my stuff out by the end of today, too.”

[P36]
“You are?”

[P37]
“I told you last time. Don’t you remember?”

[P38]
“Oh, right. You did.”

[P39]
I had felt bad about leaving Jinho hyung alone in the goshiwon after all the years we had spent living together. Now I finally felt a little more at ease.

[P40]
“Where are you moving?”

[P41]
“Well, I ended up crashing at someone I know’s place. Where did you say the house you bought was?”

[P42]
“Goyang. It’s only thirty minutes from here, so it’s not that far.”

[P43]
“Goyang?”

[P44]
Jinho hyung’s eyes widened.

[P45]
“I’m in that area too, you punk!”

[P46]
“Huh? Really?”

[P47]
I was secretly pleased by the unexpected news. By now, his was a face I felt lonely not seeing for even a single day. If we lived close by, we could keep meeting often.

[P48]
“Hyung, then where exactly is your address—”

[P49]
Just as I was about to ask, the smartphone in my pocket rang. When I answered, a gravelly voice came from the other end.

[P50]
—Hello, is this Mr. Jin Taekyung? I’m in front of the goshiwon right now.

[P51]
“Ah, yes. Driver.”

[P52]
It was the private moving-truck driver I had called in advance. I glanced out the window and saw a blue light truck waiting in front of the goshiwon.

[P53]
—Do you have a lot of luggage? If anything’s heavy, I can help you carry it.

[P54]
“No, it’s fine. I’ll carry it myself.”

[P55]
I only had two things to move.

[P56]
A cardboard box filled with small belongings, and…

[P57]
*The capsule.*

[P58]
Now that the Logout function had been activated, I no longer needed to use the capsule to travel between the Murim and modern worlds.

[P59]
It had become nothing more than a bulky nuisance, but it held a more special meaning for me than anything else. That was the entire reason I had called a moving truck despite having so little luggage.

[P60]
*What would have happened if I hadn’t had this capsule?*

[P61]
I slowly ran my hand over its surface. The coldness of the metal and its rough texture traveled through my fingers.

[P62]
This one old capsule had completely changed my life.

[P63]
*Oh, right. There was also someone who played a major role in that.*

[P64]
“Jinho hyung.”

[P65]
“Yeah?”

[P66]
I couldn’t help letting out a quiet laugh at his puzzled expression.

[P67]
If Jinho hyung hadn’t gotten dead drunk that day, I never would have had a reason to enter the capsule.

[P68]
“Never mind. It’s nothing.”

[P69]
“You’re no fun. Anyway, shouldn’t you get going? There’s a truck waiting outside.”

[P70]
“Yeah. Since you’re here, carry that box down for me. I have to carry the capsule, so I’m short on hands.”

[P71]
“Uh, what?”

[P72]
“What’s with that reaction? Can’t you carry one box for your little brother who’s moving away?”

[P73]
“That’s not it… Ah, now that I think about it, I need to pack my own stuff too. Even if it’s a hassle, just make one trip back and forth. Well, good luck!”

[P74]
“……”

[P75]
Look at him slither away like a loach.

[P76]
I watched Jinho hyung’s back as it slowly disappeared into the distance, then eventually picked up the box myself.

[P77]
The moving driver, tired of waiting, honked the truck’s horn. The sound struck my ears.

[P78]
Honk, honk!

[P79]
“Yes, I’m coming down!”

[P80]
* * *

[P81]
“Are you a Hunter?”

[P82]
The moving driver, who had been sneaking glances at me, finally spoke. The light truck, carrying the box and capsule, was heading toward my new home according to the navigation.

[P83]
“How did you know?”

[P84]
“You can tell at a glance. I used to be a Hunter, too. F-rank.”

[P85]
“Oh, really?”

[P86]
“I’m probably your Senior by training-center class. Ah, I’m not trying to pull rank. It would be ridiculous for a guy who quit after exactly one month and handed back his license to act like some old-timer.”

[P87]
The driver continued, sounding as though he were simply airing a long-held grievance.

[P88]
“Being a Hunter at the training center was manageable. Even though I was only F-rank, I took pride in becoming a Hunter. But the moment I joined a Guild after graduating, an accident happened.”

[P89]
An accident at a Gate was synonymous with death.

[P90]
Even if someone lost an arm or a leg, they could recover as long as they had enough money. Hunters didn’t call something that minor an accident.

[P91]
“He was one of my training-center classmates, and he joined the Guild at the same time as me… Before I knew what was happening, he was dragged away and died just like that. I should have chased after him and saved him, no matter what it took, but I just couldn’t make myself move. After his funeral, I applied for retirement. Someone like me shouldn’t be going on raids.”

[P92]
He tried to sound calm, but he couldn’t hide the tremor in his voice.

[P93]
“I said something awfully ominous in front of a Hunter customer. It’s not exactly a pleasant story. Sorry about that.”

[P94]
“Don’t worry about it.”

[P95]
I understood how he felt.

[P96]
I had experienced something similar. If I hadn’t felt responsible for my family, and if Jinho hyung hadn’t been there to comfort me, I might have retired two years ago.

[P97]
*Then my life would have turned out completely differently.*

[P98]
Being a Hunter was a brutal profession. The media praised them as humanity’s guardians and shields, but they lived with death always at their side.

[P99]
—Turn right in fifty meters.

[P100]
The driver flinched at the navigation’s voice, then muttered,

[P101]
“Oh, come to think of it, this is a safe zone.”

[P102]
“That’s right. Just keep going.”

[P103]
“Ah, yes.”

[P104]
The light truck arrived at its destination soon afterward.

[P105]
It was a two-story detached house with a blue roof. A low stone wall surrounded a yard covered in grass. The house felt different from when I had first seen it a few days ago.

[P106]
*It must be because it’s ours now.*

[P107]
Our house.

[P108]
The more I repeated those words in my head, the better they sounded. Of course, the fact that the house itself was beautiful probably helped.

[P109]
“Wow… It’s a nice house.”

[P110]
The driver climbed out of the cab and clicked his tongue in admiration. Praise sounded sweeter coming from someone else. No matter how hard I tried to suppress it, the corners of my mouth kept rising.

[P111]
“You must be a successful Hunter. My dream was to live in a house like this.”

[P112]
“Mine too.”

[P113]
“Your wish came true. You must be happy.”

[P114]
*Of course I was ecstatic.*

[P115]
The driver continued exclaiming over the place, touching the stone wall and looking over the lawn, before asking,

[P116]
“Would it be all right if I took a quick look inside? I can help move the capsule while I’m at it.”

[P117]
“Sure. Go ahead.”

[P118]
The moving driver became the new house’s first guest by accident as he climbed into the truck’s cargo bed.

[P119]
He was going to move the capsule.

[P120]
“That thing must weigh quite a bit.”

[P121]
“It’s fine. I’ve moved plenty of them, so I know. Game capsules are all roughly the same weight.”

[P122]
“No, it’s seriously heavy.”

[P123]
I knew because I had lifted it myself earlier. It had been moderately heavy even for me, with my Strength stat in the triple digits. For the driver, it would be a different story entirely.

[P124]
“Boss, I’ll move it myself.”

[P125]
The driver hugged the capsule and grinned.

[P126]
“Come on. You’re underestimating me. I may be an ex-Hunter, but something like this shouldn’t—nnngh!”

[P127]
“Oh, wow.”

[P128]
As expected of a former Hunter, he did manage to lift it in one go.

[P129]
The only thing that had changed was that the smile had disappeared from his face.

[P130]
“Go ahead and open the doors. Quickly!”

[P131]
His voice suddenly urgent, I hurried over and threw open the front gate and the house’s entrance door. I had no idea why this had me feeling tense, too.

[P132]
“I can carry it—”

[P133]
“Move!”

[P134]
“Ah, yes.”

[P135]
He charged into the living room with the urgency of an alarm and shouted like he was screaming for his life.

[P136]
“Which room?!”

[P137]
“I was going to put the capsule upstairs…”

[P138]
“What?!”

[P139]
“…but just leave it in the nearest room.”

[P140]
Fortunately, the door to one of the rooms was already open. With a heavy thud, the driver set down the capsule and began panting.

[P141]
“Why… why is this… huff… so heavy?”

[P142]
“……”

[P143]
Hadn’t I told him it was heavy?

[P144]
* * *

[P145]
As soon as the moving driver left, I dropped onto the living room sofa.

[P146]
It was one of the pieces of furniture the previous owner had transferred to me on the condition that I pay the remaining balance all at once.

[P147]
*I’ll have to live alone for a few months.*

[P148]
I had told my family that I was going back to Bucheon.

[P149]
Until Hayeon finished her college entrance exam, I planned to eat and sleep here and commute to work.

[P150]
*I need to remodel the house and buy a car, too. Ah, the Guild said they’d provide the car anyway, so I need to get my license first.*

[P151]
There was a mountain of other things to do. But instead of feeling tired, I felt energized. These were all things I hadn’t been able to do before, no matter how much I wanted to.

[P152]
It had only been a few months since I had done nothing but suffer while going back and forth between Gates and the goshiwon, yet so much had changed.

[P153]
*You’ve come a long way, Jin Taekyung.*

[P154]
One person suddenly came to mind.

[P155]
A man who had always smiled like a boy despite his age. A man who had done his best for his wife and children and approached them like a friend.

[P156]
*Dad, I bought a house. The place we used to live in was already gone. But I did well enough, right?*

[P157]
I wanted to brag about it like a child, but the person who would have praised me had passed away long ago. All I could do was repeat, in my heart, words that could no longer reach him.

[P158]
How much time passed like that?

[P159]
When I came to my senses, it was already eight in the evening. The summer sun was slowly sinking.

[P160]
*So this is how my last day of vacation ends.*

[P161]
An entire week of vacation. It had been hectic because of everything involving the Sangdong Guild, but it was still the best rest I had enjoyed since becoming a Hunter.

[P162]
Now it was time to return to my daily life.

[P163]
*Precisely twelve hours from now.*

[P164]
I lay flat on the sofa where I had been sitting. I briefly considered entering the capsule, but soon dismissed the thought.

[P165]
After eleven years, I finally had a home of my own again. Just this once, I wanted to wake up in our living room instead of inside the stuffy capsule.

[P166]
*Login.*

[P167]
The System responded to my call.

[P168]
Ding.

[P169]
> **System**
>
> Would you like to connect to Murim?
>
> Y / N

[P170]
Of course, my answer was yes.

[P171]
* * *

[P172]
A long time after Jin Taekyung lost consciousness, something no one could have expected was taking place in the room beside the front door.

[P173]
Hissssss.

[P174]
The door of the metal object that looked like a gigantic egg—the capsule—slowly began to open.

[P175]
The first thing to emerge was a pair of feet.

[P176]
Red letters were printed across a pair of long athletic socks that reached up to the calves.

[P177]
**Hope Goshiwon Early-Morning Soccer Club**

[P178]
Next came sweatpants rolled up halfway to the knees, followed by a pair of pale, skinny hands. The cover of the book he clutched tightly, as though it were scripture, gleamed in the sunset pouring through the window.

[P179]
**Complete Mastery of the Civil Service Exam**

[P180]
And finally, his face emerged.

[P181]
After enduring several long hours of agony, he looked as haggard as Crown Prince Sado[^1] yet as relieved as Park Hyeokgeose emerging from an egg.[^2]

[P182]
A parched voice slipped between his bone-dry lips.

[P183]
“Is this my new nest…?”

[P184]
As Seong Jinho gazed around the spacious room, a satisfied smile spread across his lips.

[P185]
[^1]: Crown Prince Sado was an eighteenth-century Joseon royal who died after being confined in a wooden rice chest.

[P186]
[^2]: Park Hyeokgeose is the legendary founder of the ancient Korean kingdom of Silla, said to have been born from an egg.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 생도     | **cadet**                                    |
| 선배     | **Senior**                                   |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 로그인              | **Login**                      |
| 로그아웃             | **Logout**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 성진호 | **Seong Jinho** |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 사도세자 | **Crown Prince Sado** | Joseon crown prince used in the comparison for Jinho's haggard appearance; footnoted. |
| 박혁거세 | **Park Hyeokgeose** | Legendary founder of Silla, used in the comparison to Jinho emerging from the capsule; footnoted. |
| 꼰대 | **boomer** | Modern slang for a hidebound older person; used by Cheongpung. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 102,
  "passed": true,
  "metrics": {
    "source_characters": 5899,
    "translation_characters": 13321,
    "length_ratio": 2.258,
    "source_paragraphs": 182,
    "translation_paragraphs": 183
  },
  "errors": [],
  "warnings": [
    {
      "code": "semantic_probe",
      "message": "생도 should use the established term 'cadet'",
      "details": {}
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "생도",
        "preferred": "cadet"
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
        "korean": "꼰대",
        "preferred": "boomer"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "소원",
        "preferred": "Sowon"
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
