# Fidelity Gate — Chapter 129

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
  1|＃129화
  2|
  3|
  4|
  5|띠링.
  6|
  7|
  8|
  9|- 퀘스트가 생성되었습니다.
 10|
 11|
 12|
 13|퀘스트
 14|
 15|
 16|
 17|[성주의 초청]
 18|
 19|높은 명성을 가진 이에게는 관심이 뒤따르기 마련.
 20|
 21|산서잠룡에 관한 소문을 들은 산서성의 성주(城主)가 당신을 내일 있을 후기지수들과의 오찬에 초청합니다.
 22|
 23|
 24|
 25|등급 : 삼류
 26|
 27|제한 : 진태경
 28|
 29|임무 : 성주가 주최하는 오찬에 참석 (미완료)
 30|
 31|보상 : 성주의 반응에 따라 달라집니다.
 32|
 33|실패 : 성주가 무척 우울해합니다.
 34|
 35|
 36|
 37|퀘스트를 수락하시겠습니까?
 38|
 39|Y   /   N
 40|
 41|※ 퀘스트 거절 시, 성주가 삐질 수 있습니다.
 42|
 43|
 44|
 45|‘성주가 나를?’
 46|
 47|분명 뜻밖이지만 그리 놀랍지는 않다. 누군가의 유명세는 종종 정치인들에게 이용되기 마련이니까.
 48|
 49|물론 미디어의 파급력이 거의 없는 세상이니만큼 개인적인 호기심이 더 크긴 할 것이다.
 50|
 51|그런데…….
 52|
 53|‘퀘스트를 거절하면 삐지는 건 또 뭐야.’
 54|
 55|삐지긴 뭘 삐져. 턱살이 다섯 겹 정도 접힌 아저씨가 삐지는 광경을 상상하니 전신에 소름이 돋는다.
 56|
 57|“소협?”
 58|
 59|현령의 의아한 표정을 못 본 척하며 턱을 긁적였다.
 60|
 61|‘음. 귀찮은데.’
 62|
 63|고작해야 삼류 등급의 퀘스트. 얻을 수 있는 경험치나 명성도 적을 것이고 보상은 성주 비위를 살살 맞춰 줘야 얻을 수 있다.
 64|
 65|그러느니 그 시간에 차라리 무공 수련을 하는 게 낫지 않을까.
 66|
 67|‘내가 뭐, 성주가 부르면 냉큼 달려가야 하는 사람도 아니고.’
 68|
 69|목숨을 잃을 뻔한 전투를 마치고 복귀하는 길인데, 당장 내일 얼굴도 모르는 성주라는 아저씨와 점심을 먹고 싶진 않다.
 70|
 71|퀘스트를 거절해도 삐지는 걸로 끝날 텐데, 뭘. 많이 삐져라.
 72|
 73|내가 최대한 정중하게 거절하려던 그때였다.
 74|
 75|덥석.
 76|
 77|“가겠습니다. 무조건!”
 78|
 79|불쑥 나서서 초청장을 잡은 혁무진의 모습에 현령이 눈살을 찌푸렸다.
 80|
 81|“그대를 초청하는 것이 아닐 텐데?”
 82|
 83|방금과 다르게 싸늘한 목소리. 하지만 혁무진이 아랑곳하지 않고 넉살 좋게 웃어 보였다.
 84|
 85|“아이고, 당연합죠. 다만 저희 공자님께서 평소 성주님을 워낙 존경해 온 터라 감격하셨는지 말을 못 하시기에.”
 86|
 87|현령이 게슴츠레한 눈으로 나를 응시했다.
 88|
 89|“흠, 사실이오?”
 90|
 91|당연히 아니지.
 92|
 93|그렇게 대답하려던 찰나, 현령을 등지고 돌아선 혁무진이 내게 입을 벙긋거렸다.
 94|
 95|‘무조건 가라고?’
 96|
 97|평소와는 다르게 어쩐지 필사적인 모습이다.
 98|
 99|나는 빠르게 판단을 내렸다.
100|
101|“물론입니다. 산서 사람 중에 성주님을 존경하지 않는 이가 어디 있겠습니까?”
102|
103|“허허, 과연 대국(大國)의 백성답구려. 성주님께서 들으시면 아주 좋아하실 거요.”
104|
105|그제야 얼굴을 펴고 흐뭇하게 웃은 현령이 돌아섰다.
106|
107|“그럼 승낙한 것으로 알고 이만 가 보겠소. 진 소가주님과 진천검에게도 안부 전해 주시오.”
108|
109|“아, 물론이죠.”
110|
111|띠링.
112|
113|
114|
115|- [성주의 초청] 퀘스트를 수락했습니다!
116|
117|
118|
119|시스템 알림이 울렸다. 이젠 취소도 못 하겠네.
120|
121|현령을 위시한 관군들이 멀어지자, 나는 혁무진을 꾹 밟으며 속삭였다.
122|
123|“나한테 할 말이 있을 것 같은데, 응?”
124|
125|“설명드릴게요. 일단 여기부터 빠져나간 후에.”
126|
127|아직 주위에 지켜보는 눈이 너무 많다. 우리는 사람들의 환호 속에서 다시 말에 올랐다.
128|
129|마을 안쪽으로 더 들어가 목적지에 도착하니 꼬마 점소이가 총알처럼 튀어나와 허리를 굽혔다.
130|
131|“어서 옵쇼…… 헉.”
132|
133|녀석은 오십 기의 기마, 호위대의 위압감에 한 번 놀라고 나와 혁무진을 보고 두 번 놀랐다.
134|
135|며칠 전에 본 적이 있는, 봉황객잔의 점소이다.
136|
137|“별채가 하룻밤에 은자 오십 냥. 맞지?”
138|
139|“어어, 그때 그?”
140|
141|“어허, 이놈이 하늘 같은 손님한테 삿대질을 해?”
142|
143|준엄한 목소리로 점소이를 꾸짖은 혁무진이 묵직한 전낭을 던졌다.
144|
145|꼬마는 우리의 눈치를 보다가 전낭에 가득한 은자를 보고 헛숨을 들이켰다.
146|
147|“헛. 이, 이렇게 많이요?”
148|
149|“지금부터 봉황객잔은 태원진가가 접수한다.”
150|
151|“……너 쌍칼이니?”
152|
153|누가 보면 조직 폭력배인 줄 알겠다.
154|
155|
156|
157|* * *
158|
159|
160|
161|마차에서 내린 좀비 세 마리는 음식이 나오자마자 허겁지겁 국물부터 들이켰다.
162|
163|자그마치 사흘 동안 하루도 쉬지 않고 과음을 했으니 저럴 만도 하다. 아니, 무공을 익히지 않았다면 첫날에 바로 주독(酒毒)으로 죽었을지도 모르겠다.
164|
165|“크허어어, 이제 좀 살겠네.”
166|
167|해장을 끝낸 진위경이 의자에 몸을 기대자마자 위팽의 잔소리가 날아들었다.
168|
169|“주군, 체통을 지키십시오. 체통을.”
170|
171|“뭐 어떤가, 어차피 우리밖에 없는데.”
172|
173|“그래도 자꾸 이런 모습을 보이시면 수하들이 어찌 생각하겠습니까?”
174|
175|“괜찮네. 난 토하진 않았거든.”
176|
177|단 한 마디로 위팽의 입을 닥치게 만든 진위경이 이번엔 내게 물었다.
178|
179|“그래, 현령이 다녀갔다고?”
180|
181|“네, 성주가 내일 오찬에 초청한다고 그러더라고요.”
182|
183|“성주가?”
184|
185|“왠지는 모르겠는데 저한테 관심이 있던데요. 거절할 생각이었는데 어떤 생각 없는 놈이 냉큼 받아 버리는 바람에.”
186|
187|“그랬느냐? 도대체 누가?”
188|
189|탁자 구석에서 눈치만 살피고 있던 혁무진이 쥐방울만 한 목소리로 대답했다.
190|
191|“접니다, 소가주님.”
192|
193|“아하, 우리 막내 오른팔이라는 그 친구구먼. 얼마 전까지 수문각에 있던. 자네 이름이 아마…… 혁무진이었던가?”
194|
195|현대와 비교하자면 태원진가는 재벌 기업이고 진위경은 회장의 장남이자 실질적인 경영자다.
196|
197|맨날 성질 더러운 상사 밑에서 구박만 받던 혁 대리가 감격한 목소리로 대답했다.
198|
199|“아, 알아봐 주셔서 감사합니다.”
200|
201|“오히려 내가 감사하지. 우리 막내가 아직 서투른 구석이 있으니 오늘처럼 잘 도와주게.”
202|
203|“조, 존명!”
204|
205|“하하, 씩씩해서 보기 좋군.”
206|
207|유쾌하게 웃은 진위경이 내게 고개를 돌렸다.
208|
209|“성주의 초청을 받아들인 건 백번 잘한 일이다.”
210|
211|“그런가요? 제가 지금까지 겪어 본 바로는 그쪽은 무림과 별 관계도 없어 보이던데.”
212|
213|“오래전부터 관(官)과 무림은 불가침의 관계다. 알고 있느냐?”
214|
215|“네, 어느 정도는.”
216|
217|무림을 소설로 배운 나다. 무협 소설에서 자주 쓰이는 설정은 이곳, 무림에서도 별반 다르지 않았다.
218|
219|“서로의 영역을 인정하지만, 관의 심기를 거슬리게 해서 좋을 것이 없다. 무림은 천하의 일부일 뿐, 천하가 무림인 것이 아니니까.”
220|
221|진위경이 앞에 놓인 그릇을 가리켰다. 반쯤 차 있는 국물과 커다란 고기 한 덩어리가 보인다.
222|
223|“무슨 말인지 알겠느냐?”
224|
225|나는 고개를 끄덕였다.
226|
227|그릇은 천하, 무림은 그 안에 들어있는 고깃덩어리다.
228|
229|“우리는 무림인이지만 천하를 다스리는 것은 황제다. 백성들 사이에서 천자(天子)의 권위는 절대적이야. 바로 그 황제의 명을 받들어 각 성을 다스리는 자가 성주이니 상당한 힘과 권한이 있지.”
230|
231|“우리 태원진가 이상으로요?”
232|
233|“권한만 보면 그렇다. 그저 서로의 세력을 인정하고 존중하는 것이지. 무림 문파는 관이 해결할 수 없는 치안을 맡기도 하고, 관군에 무공 교두를 파견하기도 한다. 관에서는 그에 상응하는 도움을 주면서 상부상조하고 있다.”
234|
235|관과 무림은 악어와 악어새의 관계라는 말이군.
236|
237|잠시 생각하던 나는 아까부터 자꾸만 들던 의문을 입 밖으로 꺼냈다.
238|
239|“그런데 왜 마적들이 개판 치고, 문파끼리 대규모 전투가 벌어질 때도 가만히 있는 겁니까? 지난번 전쟁 때야 무림인끼리의 일이니 가만히 있었다 쳐도, 마적 놈들은 아니잖아요?”
240|
241|이천백도 삭주지부를 몰살시키고 아이들을 죽이는 미친 짓거리를 하긴 했지만, 어쨌든 피해자들은 태원진가 소속이었다.
242|
243|엄연히 말하면 무림 문파 간의 은원(恩怨)에 희생된 이들이라 할 수 있겠다.
244|
245|하지만 마적 놈들은 그런 거 없이 닥치는 대로 죽이고 불태우는 놈들 아닌가?
246|
247|‘마적 입장에서는 만만한 게 양민이니까.’
248|
249|강자에게 약하고, 약자에게 강한 놈들이 바로 마적이다.
250|
251|아무튼 중요한 건 항산검문으로 가던 길에 마주친 마적들만 수십 명인데, 관군은 구경도 못 해 봤다는 거다.
252|
253|“그건…….”
254|
255|진위경이 말꼬리를 흐리자, 조용히 음식만 흡입하던 진무경이 툭 내뱉었다.
256|
257|“성주가 무능해서지. 아니, 이 경우는 황제가 무능한 건가?”
258|
259|말이 끝나는 순간 혁무진은 경기를 일으켰고, 진위경과 위팽은 짐짓 얼굴을 굳혔다.
260|
261|“어허, 무경아.”
262|
263|“어차피 우리뿐이라 엿들을 사람도 없습니다. 제가 틀린 말 한 것도 아니고요.”
264|
265|“이공자, 본 가는 아직 구파일방도, 오대세가도 되지 못합니다. 자칫 문제가 생길 말은 삼가십시오.”
266|
267|나는 마지못해 고개를 끄덕이는 진무경에게 물었다.
268|
269|“성주가 무능하다는 게 무슨 소리지?”
270|
271|“무능이라는 단어를 모르나?”
272|
273|“확 그냥, 황제 욕했다고 관아에 고발해 버릴까.”
274|
275|“역모죄는 최소 삼족(三族)이 처벌받지. 축하한다, 아우야.”
276|
277|진무경 이 자식, 말발이 제법 늘었는데.
278|
279|“지금 성주가 누구인지 알고 있나?”
280|
281|“김춘배?”
282|
283|“……모르면 모른다고 해라.”
284|
285|나를 벌레 보듯 바라본 녀석이 다시 입을 열었다.
286|
287|“현 산서 성주는 주씨 성을 쓴다.”
288|
289|“그래서?”
290|
291|“그래서라니? 황족이란 말이다. 황족!”
292|
293|“아, 그래?”
294|
295|주씨 왕조였던 모양이다. 한순간에 황제 성씨도 모르는 무식한 놈으로 낙인찍혔지만.
296|
297|그래도 뭐, 이런 일이 한두 번이 아니라 이제는 별로 부끄럽지도 않다.
298|
299|“알겠으니까 계속해.”
300|
301|한숨을 푹 내쉰 진무경이 말을 이었다.
302|
303|“지금의 성주는 황상의 막내아우로, 황실 관직으로는 친왕(親王)이다. 황실의 직계이니 성주들과는 격이 달라. 억지로라도 초청에 응해서 체면을 세워 줘야 하는 인물이지.”
304|
305|“오오.”
306|
307|확실히 격이 다르긴 하다. 그냥 성주가 아니라 황제의 아우. 무려 진짜 왕.
308|
309|천자의 아들로 태어나 천자의 동생이 되었으니 금수저 정도가 아니라 비브라늄 수저라고 할 수 있겠다.
310|
311|현대에 있는 북한의 핵수저, 그 이상.
312|
313|“그런데 왕씩이나 되는 양반이 왜 그렇게 무능해? 형한테 편지 한 통 쓰면 위에서 지원 빵빵하게 해 주겠구먼. 둘이 사이 안 좋나?”
314|
315|“글쎄, 그 집안 사정이야 정확히는 모르지만, 딱히 우애가 좋을 것 같지는 않군. 현 황제도 바로 위의 형인 태자를 암살하고 황위에 올랐다는 소문이 도니까.”
316|
317|“권력욕 보소.”
318|
319|“만두 하나에 살인도 일어나는데, 황위는 오죽할까.”
320|
321|진위경과 위팽은 입을 딱 벌렸고, 혁무진은 다시 한번 경기를 일으켰다.
322|
323|“판관님, 저는 아무것도 듣지 못했습니다. 정말 아무것도 모릅니다. 사실 이미 오래전부터 귀가 들리지 않습니다…….”
324|
325|미친놈처럼 중얼거리는 혁무진의 뒤통수를 후려치는 진무경을 향해 내가 물었다.
326|
327|“황제랑 사이가 안 좋아서 지원을 안 해 주는 건가? 아니면 그냥 술과 여자에 빠져서?”
328|
329|“술? 여자?”
330|
331|녀석이 또 피식 웃었다.
332|
333|“이제 겨우 열 살이다. 주지육림에 빠지기에는 너무 이른 나이지.”
334|
335|“뭐, 열 살? 열 살짜리가 성주란 말이야?”
336|
337|“황실 직계니까. 성주가 아니라 그 이상도 될 수 있는 핏줄이야.”
338|
339|문득 아까 봤던 시스템 메시지가 생각난다.
340|
341|
342|
343|※ 퀘스트 거절 시, 성주가 삐질 수 있습니다.
344|
345|
346|
347|나이도 먹을 만큼 먹은 아저씨가 주책이다 싶었는데, 열 살짜리 어린애라니 이제야 납득이 간다.
348|
349|떨어지는 낙엽에도 삐질 나이 아닌가?
350|
351|“더 재밌는 사실은 처음 성주로 부임했던 게 오 년 전이라는 거지.”
352|
353|“……다섯 살? 미쳤군.”
354|
355|다섯 살짜리가 뭘 알겠나. 산서성 치안이 개판이 된 이유도 대충 짐작이 간다. 진무경이 왜 성주가 아니라 황제가 더 무능한 거라고 했는지도.
356|
357|동네 구멍가게도 아니고, 능력과 책임감이 필요한 막중한 자리에 어린아이를 앉혀 놨으니 제대로 돌아갈 리 만무하지.
358|
359|“그런데 어떻게 그렇게 잘 알아?”
360|
361|무공에만 미쳐 있던 진무경이 정세에 제법 빠삭한 것이 신기해서 물어본 건데, 뜻밖의 대답이 돌아왔다.
362|
363|“직접 만난 적이 있으니까. 불려갔다고 해야 맞겠군.”
364|
365|“어, 진짜?”
366|
367|“삼 년 전이었지.”
368|
369|하긴, 내가 근래 들어 떠오르는 슈퍼 루키라면 진무경은 이미 입지를 다진 절정 고수다. 나보다 앞서 초청을 받는 게 당연했다.
370|
371|“어땠어?”
372|
373|진무경이 묘한 눈빛으로 나를 바라봤다.
374|
375|그러더니 웃음과 빡침이 뒤섞인, 보는 것만으로도 불길해지는 표정으로 말한다.
376|
377|“개 같았다.”
```

## Assembled English

```markdown
[P1]
# Chapter 129

[P2]
Ding.

[P3]
> **System**
>
> A **Quest** has been created.
>
> **Quest**
>
> **The City Lord’s Invitation**
>
> High renown is bound to attract attention.
>
> The City Lord of Shanxi Province, having heard rumors about the Sleeping Dragon of Shanxi, invites you to a luncheon with several young prodigies tomorrow.
>
> **Grade:** Third Rate
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Attend the luncheon hosted by the City Lord (Incomplete)
>
> **Reward:** Varies according to the City Lord’s reaction.
>
> **Failure:** The City Lord becomes extremely depressed.
>
> Would you like to accept the Quest?
>
> **Y / N**
>
> ※ If you reject the Quest, the City Lord may sulk.

[P4]
*The City Lord wants me?*

[P5]
It was certainly unexpected, but not all that surprising. Politicians often made use of other people’s fame, after all.

[P6]
Of course, this was a world where media had almost no reach, so personal curiosity was probably the greater factor.

[P7]
But…

[P8]
*What do you mean, the City Lord might sulk if I reject the Quest?*

[P9]
What was there to sulk about? Imagining a middle-aged man with five folds under his chin sulking sent goose bumps all over my body.

[P10]
“Young Hero?”

[P11]
Pretending not to notice the county magistrate’s puzzled expression, I scratched my chin.

[P12]
*Hmm. What a pain.*

[P13]
It was only a Third Rate Quest. The EXP and Fame I could gain would probably be minimal, and I’d have to carefully flatter the City Lord to obtain the reward.

[P14]
Wouldn’t I be better off spending that time practicing martial arts?

[P15]
*It’s not like I have to come running the instant the City Lord calls.*

[P16]
I was on my way back after a battle in which I had nearly lost my life. I didn’t particularly want to have lunch tomorrow with some middle-aged man called the City Lord whose face I had never even seen.

[P17]
If I rejected the Quest, the worst that could happen was that he’d sulk. Whatever. Let him sulk all he wanted.

[P18]
I was just about to turn him down as politely as possible when—

[P19]
Snatch.

[P20]
“We’ll go. Absolutely!”

[P21]
Hyuk Mujin suddenly stepped forward and grabbed the invitation. The county magistrate frowned.

[P22]
“I don’t believe I invited you.”

[P23]
His voice had turned cold. Hyuk Mujin didn’t care in the slightest and flashed him a shameless smile.

[P24]
“Oh my, of course not. It’s just that our Young Master has always respected the City Lord so deeply that he was too moved to speak.”

[P25]
The county magistrate stared at me through narrowed eyes.

[P26]
“Hmm. Is that true?”

[P27]
Of course it wasn’t.

[P28]
I was about to say so when Hyuk Mujin turned his back to the county magistrate and silently mouthed at me.

[P29]
*You absolutely have to go?*

[P30]
Unlike usual, he looked strangely desperate.

[P31]
I made a quick decision.

[P32]
“Of course. Is there anyone in Shanxi who doesn’t respect the City Lord?”

[P33]
“Ha-ha, spoken like a true citizen of a Great Nation. The City Lord will be delighted to hear it.”

[P34]
Only then did the county magistrate’s expression soften into a satisfied smile. He turned around.

[P35]
“Then I’ll take that as your acceptance and be on my way. Please convey my regards to the Lesser Family Head and the Heaven Shaking Sword as well.”

[P36]
“Ah, of course.”

[P37]
Ding.

[P38]
> **System**
>
> You have accepted **The City Lord’s Invitation** Quest!

[P39]
The System notification rang out.

[P40]
*Now I can’t even cancel it.*

[P41]
Once the county magistrate and the government troops had moved away, I pressed my foot down on Hyuk Mujin’s and whispered,

[P42]
“I think you have something to tell me. Don’t you?”

[P43]
“I’ll explain. Let’s get out of here first.”

[P44]
There were still too many eyes watching us. Amid the people’s cheers, we mounted our horses again.

[P45]
We continued farther into the village until we reached our destination. A little errand boy shot out like a bullet and bowed at the waist.

[P46]
“Welcome—gasp.”

[P47]
The fifty mounted riders and the escort force’s intimidating presence startled him once. Recognizing Hyuk Mujin and me startled him a second time.

[P48]
He was the errand boy from the Phoenix Inn. I had seen him a few days ago.

[P49]
“The private annex is fifty silver nyang a night. Right?”

[P50]
“Uh, you’re the one from back then?”

[P51]
“Hey, you little brat. How dare you point at a guest as lofty as the heavens?”

[P52]
After sternly scolding the boy, Hyuk Mujin tossed him a heavy money pouch.

[P53]
The little boy glanced nervously between us, then sucked in a breath when he saw the pouch packed with silver.

[P54]
“Gasp. Th-this much?”

[P55]
“From this moment on, the Jin Family of Taiyuan is taking over the Phoenix Inn.”

[P56]
“…Are you some kind of two-knife gangster?”

[P57]
Anyone watching would have thought we were members of organized crime.

[P58]
* * *

[P59]
The three zombies climbed out of the carriage and began frantically gulping down the broth first the moment the food arrived.

[P60]
It was understandable, considering they had spent three days drinking to excess without taking a single day off. No—if they hadn’t practiced martial arts, they might have died of alcohol poisoning on the first day.

[P61]
“Guhhh, I feel alive again.”

[P62]
The instant Jin Wikyung leaned back in his chair after finishing his hangover cure, Wipeng’s nagging flew at him.

[P63]
“My lord, please maintain your dignity. Your dignity.”

[P64]
“What does it matter? We’re the only ones here.”

[P65]
“Even so, what will your subordinates think if you keep letting them see you like this?”

[P66]
“It’s fine. I didn’t throw up.”

[P67]
That single sentence silenced Wipeng. Jin Wikyung then turned to me.

[P68]
“So, the county magistrate came by?”

[P69]
“Yes. He said the City Lord was inviting me to a luncheon tomorrow.”

[P70]
“The City Lord?”

[P71]
“I don’t know why, but he seemed interested in me. I was planning to reject it, but some thoughtless idiot accepted it without hesitation.”

[P72]
“Did he? Who on earth would do that?”

[P73]
Hyuk Mujin, who had been sitting in the corner of the table and nervously watching our expressions, answered in a tiny voice.

[P74]
“That would be me, Lesser Family Head.”

[P75]
“Ah, I see. You’re the fellow they call our youngest brother’s right-hand man. The one who served at the Gate Guard Pavilion until recently. Your name was… Hyuk Mujin, wasn’t it?”

[P76]
Compared to the modern world, the Jin Family of Taiyuan was a conglomerate, while Jin Wikyung was the chairman’s eldest son and the actual head of the company.

[P77]
Assistant Manager Hyuk, who had spent every day getting bullied by his foul-tempered boss, answered in a deeply moved voice.

[P78]
“Ah, thank you for remembering me.”

[P79]
“I should be thanking you. Our youngest brother still has some rough edges, so keep helping him as you did today.”

[P80]
“A-as you command!”

[P81]
“Ha-ha. It’s good to see such spirit.”

[P82]
Jin Wikyung laughed cheerfully, then turned back to me.

[P83]
“Accepting the City Lord’s invitation was absolutely the right thing to do.”

[P84]
“Really? From what I’ve experienced so far, he doesn’t seem to have much to do with the Murim.”

[P85]
“For a long time, the government and the Murim have maintained a relationship of noninterference. Do you know that?”

[P86]
“Yes, more or less.”

[P87]
I had learned about the Murim through novels. The common conventions of martial-arts fiction weren’t all that different from how things worked here.

[P88]
“They recognize each other’s domains, but nothing good can come from offending the government. The Murim is only one part of the world. The world itself is not the Murim.”

[P89]
Jin Wikyung pointed to the bowl in front of him. It was half-filled with broth and contained one large chunk of meat.

[P90]
“Do you understand what I mean?”

[P91]
I nodded.

[P92]
The bowl was the world, and the chunk of meat inside it was the Murim.

[P93]
“We are martial artists, but it is the Emperor who rules the world. Among the people, the authority of the Son of Heaven is absolute. The City Lords govern their respective provinces under the Emperor’s command, so they possess considerable power and authority.”

[P94]
“More than the Jin Family of Taiyuan?”

[P95]
“In terms of authority alone, yes. We simply acknowledge and respect each other’s power. Murim sects sometimes maintain public order where the government cannot, and they also send martial arts instructors to train government troops. The government provides assistance in return. The two sides help each other.”

[P96]
So the government and the Murim were like the crocodile and the crocodile bird.

[P97]
After thinking for a moment, I voiced the question that had been nagging at me since earlier.

[P98]
“Then why does the government sit back and do nothing when mounted bandits run wild or large-scale battles break out between sects? I can understand staying out of the last war because it was a matter between martial artists, but the mounted bandits are different, aren’t they?”

[P99]
Even Lee Cheonbaek had massacred everyone at the Sakju Branch and committed the insane act of killing children, but the victims had belonged to the Jin Family of Taiyuan.

[P100]
Strictly speaking, they could be considered people who had been sacrificed to the gratitude and grudges between Murim sects.

[P101]
But the mounted bandits killed indiscriminately and burned everything in their path without any of that, didn’t they?

[P102]
*To mounted bandits, commoners are easy prey.*

[P103]
Weak before the strong and strong before the weak. That was what mounted bandits were.

[P104]
The important point was that I had encountered dozens of mounted bandits on the way to the Mount Heng Sword Sect, yet I hadn’t even seen a government soldier.

[P105]
“That’s…”

[P106]
Jin Wikyung let his voice trail off. Jin Mukyung, who had been silently inhaling his food until then, suddenly blurted,

[P107]
“Because the City Lord is incompetent. No, in this case, is the Emperor incompetent?”

[P108]
The moment he finished speaking, Hyuk Mujin had a fit, while Jin Wikyung and Wipeng deliberately hardened their expressions.

[P109]
“Hey, Mukyung.”

[P110]
“It’s just us here. No one can overhear us. Besides, I didn’t say anything untrue.”

[P111]
“Second Young Master, our family does not yet stand alongside the Nine Sects and One Gang or the Five Great Families. Please refrain from saying anything that could cause trouble.”

[P112]
I asked Jin Mukyung, who reluctantly nodded.

[P113]
“What do you mean, the City Lord is incompetent?”

[P114]
“Do you not know what the word *incompetent* means?”

[P115]
“Should I report you to the authorities for insulting the Emperor?”

[P116]
“Treason gets at least three clans punished. Congratulations, little brother.”

[P117]
*This bastard Jin Mukyung has gotten pretty good with words.*

[P118]
“Do you know who the current City Lord is?”

[P119]
“Kim Chunbae?”

[P120]
“…If you don’t know, just say you don’t know.”

[P121]
He looked at me as if I were a bug, then continued.

[P122]
“The current City Lord of Shanxi has the surname Zhu.”

[P123]
“So?”

[P124]
“What do you mean, *so*? He’s a member of the imperial family. The imperial family!”

[P125]
“Oh, really?”

[P126]
Apparently, this was a Zhu dynasty. In the span of a moment, I had been branded an ignorant fool who didn’t even know the Emperor’s surname.

[P127]
Still, it wasn’t as if this sort of thing had only happened once or twice. I wasn’t even embarrassed anymore.

[P128]
“Fine, I get it. Keep going.”

[P129]
Jin Mukyung let out a deep sigh and continued.

[P130]
“The current City Lord is the Emperor’s youngest brother, and his imperial title is Prince. As a direct member of the imperial family, he stands on a different level from the other City Lords. He’s someone whose invitation we must accept, even if we have to force ourselves, if only to preserve his dignity.”

[P131]
“Oh.”

[P132]
He really was on a different level. Not just an ordinary City Lord, but the Emperor’s brother. An actual king, no less.

[P133]
Born the son of the Son of Heaven and then becoming the younger brother of the Son of Heaven, he hadn’t merely been born with a silver spoon in his mouth. His spoon was made of vibranium.

[P134]
He was the modern North Korean nuclear spoon—and then some.

[P135]
“Then how can someone who’s practically a king be so incompetent? One letter to his brother should get him all the support he needs from above. Are they on bad terms?”

[P136]
“Who knows? I don’t know the details of that family’s affairs, but I doubt they’re particularly close. There are rumors that the current Emperor assassinated the Crown Prince, his immediately older brother, before ascending the throne.”

[P137]
“Talk about a hunger for power.”

[P138]
“People kill over a single dumpling. Imagine what they’d do for the imperial throne.”

[P139]
Jin Wikyung and Wipeng’s mouths fell open, while Hyuk Mujin had another fit.

[P140]
“Your Honor, I didn’t hear anything. I truly know nothing. In fact, I haven’t been able to hear for a long time…”

[P141]
As Hyuk Mujin muttered like a madman, Jin Mukyung smacked him across the back of the head. I asked,

[P142]
“Does he not get any support because he’s on bad terms with the Emperor? Or is he simply lost in wine and women?”

[P143]
“Wine? Women?”

[P144]
Jin Mukyung gave another short laugh.

[P145]
“He’s only ten years old. It’s too early for him to lose himself in wine and women.”

[P146]
“What, ten? You mean a ten-year-old is the City Lord?”

[P147]
“He’s a direct member of the imperial family. With his bloodline, he could become far more than a City Lord.”

[P148]
The System message I’d seen earlier suddenly came to mind.

[P149]
> If you reject the Quest, the City Lord may sulk.

[P150]
I had thought it was ridiculous for a middle-aged man to act so childish, but now that I knew he was a ten-year-old boy, it finally made sense.

[P151]
Wasn’t that the age when even a falling leaf could make you sulk?

[P152]
“What’s even more amusing is that he was first appointed City Lord five years ago.”

[P153]
“…Five years old? That’s insane.”

[P154]
What could a five-year-old possibly know? I could roughly guess why the public order in Shanxi Province had become such a mess. I also understood why Jin Mukyung had said that the Emperor, rather than the City Lord, was more incompetent.

[P155]
This wasn’t some neighborhood corner store. They had put a child in a position that demanded ability and responsibility. There was no way things could run properly.

[P156]
“How do you know all this?”

[P157]
I asked because it was surprising that Jin Mukyung, who had been obsessed with martial arts and nothing else, was so well-informed about current affairs.

[P158]
His answer was unexpected.

[P159]
“Because I’ve met him before. More accurately, I was summoned.”

[P160]
“Oh, really?”

[P161]
“Three years ago.”

[P162]
Well, if I was the rising super rookie of the moment, Jin Mukyung was already an established Peak master. It made sense that he would have been invited before me.

[P163]
“What was he like?”

[P164]
Jin Mukyung looked at me with a strange glint in his eyes.

[P165]
Then, wearing an ominous expression that mixed laughter with irritation, he spoke.

[P166]
“It was fucking awful.”
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
# Chapter 129

[P2]
Ding.

[P3]
> **System**
>
> A **Quest** has been created.
>
> **Quest**
>
> **The City Lord’s Invitation**
>
> High renown is bound to attract attention.
>
> The City Lord of Shanxi Province, having heard rumors about the Sleeping Dragon of Shanxi, invites you to a luncheon with several young prodigies tomorrow.
>
> **Grade:** Third Rate
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Attend the luncheon hosted by the City Lord (Incomplete)
>
> **Reward:** Varies according to the City Lord’s reaction.
>
> **Failure:** The City Lord becomes extremely depressed.
>
> Would you like to accept the Quest?
>
> **Y / N**
>
> ※ If you reject the Quest, the City Lord may sulk.

[P4]
*The City Lord wants me?*

[P5]
It was certainly unexpected, but not all that surprising. A person’s fame was often used by politicians, after all.

[P6]
Of course, this was a world where media had almost no reach, so personal curiosity was probably the greater factor.

[P7]
But…

[P8]
*What do you mean, the City Lord might sulk if I reject the Quest?*

[P9]
What was there to sulk about? The thought of a five-chin-folded middle-aged man sulking sent goose bumps all over my body.

[P10]
“Young Hero?”

[P11]
Pretending not to notice the county magistrate’s puzzled expression, I scratched my chin.

[P12]
*Hmm. What a pain.*

[P13]
It was only a Third Rate Quest. The EXP and Fame I could gain would probably be minimal, and I’d have to carefully flatter the City Lord to obtain the reward.

[P14]
Wouldn’t it be better to spend that time practicing martial arts instead?

[P15]
*It’s not like I’m someone who has to come running the instant the City Lord calls.*

[P16]
I was on my way back after a battle in which I had nearly lost my life. I didn’t particularly want to have lunch tomorrow with some middle-aged man called the City Lord whose face I had never even seen.

[P17]
If I rejected the Quest, the worst that could happen was that he’d sulk. Whatever. He could sulk as much as he wanted.

[P18]
I was just about to turn him down as politely as possible when—

[P19]
Grab.

[P20]
“We’ll go. Absolutely!”

[P21]
Hyuk Mujin suddenly stepped forward and snatched the invitation. The county magistrate frowned.

[P22]
“I don’t believe I invited you.”

[P23]
His voice was cold, unlike before. Hyuk Mujin didn’t care in the slightest. He simply flashed a shameless smile.

[P24]
“Oh my, of course you didn’t. It’s just that our Young Master has always respected the City Lord so deeply that he was too moved to speak.”

[P25]
The county magistrate stared at me through narrowed eyes.

[P26]
“Hmm. Is that true?”

[P27]
Of course it wasn’t.

[P28]
I was about to say so when Hyuk Mujin, having turned his back to the county magistrate, silently mouthed at me.

[P29]
*You absolutely have to go?*

[P30]
Unlike usual, he looked strangely desperate.

[P31]
I made a quick decision.

[P32]
“Of course. Is there anyone in Shanxi who doesn’t respect the City Lord?”

[P33]
“Ha-ha, truly the words of a citizen of a great nation. The City Lord will be delighted to hear that.”

[P34]
Only then did the county magistrate relax his face and smile with satisfaction. He turned around.

[P35]
“Then I’ll consider it accepted and take my leave. Please convey my regards to the Lesser Family Head and the Heaven Shaking Sword.”

[P36]
“Ah, of course.”

[P37]
Ding.

[P38]
> **System**
>
> You have accepted the **The City Lord’s Invitation** Quest!

[P39]
The System notification rang out.

[P40]
*Now I can’t even cancel it.*

[P41]
Once the county magistrate and the government troops had moved away, I whispered as I pressed my foot down on Hyuk Mujin’s.

[P42]
“I think you have something to tell me, don’t you?”

[P43]
“I’ll explain. First, let’s get out of here.”

[P44]
There were still too many eyes watching us. Amid the people’s cheers, we mounted our horses again.

[P45]
We proceeded farther into the village and reached our destination. A little errand boy shot out like a bullet and bowed at the waist.

[P46]
“Welcome—gasp.”

[P47]
He was startled once by the fifty mounted riders and the intimidating presence of the escort, then a second time when he recognized Hyuk Mujin and me.

[P48]
He was the errand boy from the Phoenix Inn. I had seen him a few days ago.

[P49]
“The private annex is fifty nyang of silver for one night. That’s right, isn’t it?”

[P50]
“Uh, you’re the one from back then?”

[P51]
“Hey, you little brat. Are you pointing at a guest as lofty as the heavens?”

[P52]
After scolding the boy in a stern voice, Hyuk Mujin tossed him a heavy money pouch.

[P53]
The little boy glanced nervously between us, then inhaled sharply when he saw the pouch packed with silver.

[P54]
“Gasp. Th-this much?”

[P55]
“From this moment on, the Phoenix Inn is under the control of the Jin Family of Taiyuan.”

[P56]
“…Are you some kind of two-knife gangster?”

[P57]
Anyone watching would have thought we were members of organized crime.

[P58]
* * *

[P59]
The three zombies climbed out of the carriage and began gulping down the broth the moment the food arrived.

[P60]
It was understandable, considering they had spent three days drinking to excess without taking a single day off. No—if they hadn’t practiced martial arts, they might have died of alcohol poisoning on the first day.

[P61]
“Guhhh, I feel alive again.”

[P62]
The instant Jin Wikyung leaned back in his chair after finishing his hangover cure, Wipeng’s nagging flew at him.

[P63]
“My lord, please maintain your dignity. Your dignity.”

[P64]
“What does it matter? We’re the only ones here.”

[P65]
“Even so, what will your subordinates think if you keep showing them this side of yourself?”

[P66]
“It’s fine. I didn’t throw up.”

[P67]
With a single sentence, Jin Wikyung silenced Wipeng. Then he turned to me.

[P68]
“So, the county magistrate came by?”

[P69]
“Yes. He said the City Lord was inviting me to a luncheon tomorrow.”

[P70]
“The City Lord?”

[P71]
“I don’t know why, but he seemed interested in me. I was planning to reject it, but some thoughtless idiot accepted it without hesitation.”

[P72]
“Did he? Who on earth would do that?”

[P73]
Hyuk Mujin, who had been sitting in the corner of the table and nervously watching our expressions, answered in a tiny voice.

[P74]
“That would be me, Lesser Family Head.”

[P75]
“Ah, I see. You’re the fellow who’s supposed to be our youngest brother’s right-hand man. The one who was in the Gatekeeper Pavilion until recently. Your name was… Hyuk Mujin, wasn’t it?”

[P76]
Compared to the modern world, the Jin Family of Taiyuan was a conglomerate, while Jin Wikyung was the chairman’s eldest son and the actual head of the company.

[P77]
Assistant Manager Hyuk, who had spent all his time being bullied under a foul-tempered boss, answered in a deeply moved voice.

[P78]
“Ah, thank you for remembering me.”

[P79]
“I should be thanking you. Our youngest brother still has some rough edges, so continue helping him as you did today.”

[P80]
“A-as you command!”

[P81]
“Ha-ha. It’s good to see such spirit.”

[P82]
Jin Wikyung laughed cheerfully, then turned back to me.

[P83]
“Accepting the City Lord’s invitation was absolutely the right thing to do.”

[P84]
“Really? From what I’ve experienced so far, he doesn’t seem to have much to do with the Murim.”

[P85]
“For a long time, the government and the Murim have maintained a relationship of noninterference. Do you know that?”

[P86]
“Yes, more or less.”

[P87]
I had learned about the Murim through novels. The common settings in martial-arts fiction weren’t all that different here in the Murim.

[P88]
“They recognize each other’s domains, but there is nothing to be gained by offending the government. The Murim is merely one part of the world. The world is not the Murim.”

[P89]
Jin Wikyung pointed toward the bowl in front of him. It contained half a bowl of broth and one large chunk of meat.

[P90]
“Do you understand what I mean?”

[P91]
I nodded.

[P92]
The bowl was the world, and the chunk of meat inside it was the Murim.

[P93]
“We are martial artists, but it is the Emperor who rules the world. Among the people, the authority of the Son of Heaven is absolute. The City Lords govern their respective provinces under the Emperor’s command, so they possess considerable power and authority.”

[P94]
“More than the Jin Family of Taiyuan?”

[P95]
“In terms of authority alone, yes. We simply recognize and respect each other’s power. Murim sects sometimes take responsibility for maintaining public order when the government cannot resolve a problem, and they also dispatch martial arts instructors to train government troops. The government offers assistance in return, so the two sides help each other.”

[P96]
So the government and the Murim were like the crocodile and the crocodile bird.

[P97]
After thinking for a moment, I finally voiced the question that had been bothering me since earlier.

[P98]
“Then why do you sit back and do nothing when mounted bandits run wild or large-scale battles break out between sects? I can understand staying out of the last war because it was a matter between martial artists, but the mounted bandits are different, aren’t they?”

[P99]
Lee Cheonbaek had massacred everyone at the Sakju Branch and committed the insane act of killing children, but the victims had belonged to the Jin Family of Taiyuan.

[P100]
Strictly speaking, they could be considered people who had been sacrificed to the gratitude and grudges between Murim sects.

[P101]
But the mounted bandits killed indiscriminately and burned everything in their path, didn’t they?

[P102]
*From the mounted bandits’ perspective, commoners were easy prey.*

[P103]
They were weak before the strong and strong before the weak. That was what mounted bandits were.

[P104]
The important point was that I had encountered dozens of mounted bandits on the way to the Mount Heng Sword Sect, yet I hadn’t even seen a government soldier.

[P105]
“That’s…”

[P106]
Jin Wikyung let his voice trail off. Jin Mukyung, who had been silently inhaling his food until then, suddenly spoke.

[P107]
“Because the City Lord is incompetent. No, in this case, is the Emperor incompetent?”

[P108]
The moment he finished speaking, Hyuk Mujin had a fit, while Jin Wikyung and Wipeng deliberately hardened their expressions.

[P109]
“Hey, Mukyung.”

[P110]
“It’s just us here. No one can overhear us. And I haven’t said anything untrue.”

[P111]
“Second Young Master, our family does not yet stand alongside the Nine Sects and One Gang or the Five Great Families. Please refrain from saying anything that could cause trouble.”

[P112]
I asked Jin Mukyung, who reluctantly nodded.

[P113]
“What do you mean, the City Lord is incompetent?”

[P114]
“Do you not know the meaning of the word incompetent?”

[P115]
“Should I report you to the authorities for insulting the Emperor?”

[P116]
“Treason gets at least three clans punished. Congratulations, little brother.”

[P117]
*This guy Jin Mukyung has gotten pretty good with words.*

[P118]
“Do you know who the City Lord is right now?”

[P119]
“Kim Chunbae?”

[P120]
“…If you don’t know, just say you don’t know.”

[P121]
He looked at me as if I were a bug, then continued.

[P122]
“The current City Lord of Shanxi has the surname Zhu.”

[P123]
“So?”

[P124]
“What do you mean, ‘so’? He’s a member of the imperial family. The imperial family!”

[P125]
“Oh, really?”

[P126]
It seemed to be a Zhu dynasty. I had been branded an ignorant fool who didn’t even know the Emperor’s surname in the space of a moment.

[P127]
Still, it wasn’t as if this sort of thing had only happened once or twice. I wasn’t even embarrassed anymore.

[P128]
“Fine, I get it. Continue.”

[P129]
Jin Mukyung sighed deeply and went on.

[P130]
“The current City Lord is the Emperor’s youngest brother. His imperial title is a Prince. He is a direct member of the imperial family, so he stands on a different level from the other City Lords. He is someone whose invitation we must accept, even if only to preserve his dignity.”

[P131]
“Oh.”

[P132]
He really was on a different level. Not just an ordinary City Lord, but the Emperor’s brother. An actual king, no less.

[P133]
Born the son of the Son of Heaven and then becoming the younger brother of the Son of Heaven, he wasn’t merely born with a silver spoon in his mouth. He had a vibranium spoon.

[P134]
The North Korean nuclear spoon of the modern world—and then some.

[P135]
“Then how can someone who’s practically a king be so incompetent? If he writes his brother a single letter, he could get all the support he needs from above. Are they on bad terms?”

[P136]
“Who knows? I don’t know the details of that family’s circumstances, but they don’t seem particularly close. There are rumors that the current Emperor assassinated the Crown Prince, the brother immediately older than him, before ascending the throne.”

[P137]
“Talk about a hunger for power.”

[P138]
“People kill over a single dumpling. Imagine what they’d do for the imperial throne.”

[P139]
Jin Wikyung and Wipeng’s mouths fell open, while Hyuk Mujin had another fit.

[P140]
“Judge, I didn’t hear anything. I truly know nothing. In fact, I haven’t been able to hear for a long time…”

[P141]
As Hyuk Mujin muttered like a madman, Jin Mukyung smacked him across the back of the head. I asked,

[P142]
“Does he not receive support because he’s on bad terms with the Emperor? Or is he simply lost in alcohol and women?”

[P143]
“Alcohol? Women?”

[P144]
Jin Mukyung let out another quiet laugh.

[P145]
“He’s only ten years old. It’s too early for him to lose himself in wine and women.”

[P146]
“What, ten? You mean a ten-year-old is the City Lord?”

[P147]
“He’s a direct member of the imperial family. He has the bloodline to become more than a City Lord.”

[P148]
The System message I’d seen earlier suddenly came to mind.

[P149]
> If you reject the Quest, the City Lord may sulk.

[P150]
I had thought it was ridiculous for a middle-aged man to act so childish, but now that I knew he was a ten-year-old boy, it finally made sense.

[P151]
Wasn’t that the age when you’d sulk at a falling leaf?

[P152]
“The more amusing fact is that he was first appointed City Lord five years ago.”

[P153]
“…Five years old? That’s insane.”

[P154]
What could a five-year-old possibly know? I could roughly guess why the public order in Shanxi Province had become such a mess. I also understood why Jin Mukyung had said that the Emperor, rather than the City Lord, was more incompetent.

[P155]
This wasn’t some neighborhood convenience store. They had put a child in a position that demanded ability and responsibility. There was no way things could run properly.

[P156]
“How do you know all this?”

[P157]
I asked because it was surprising that Jin Mukyung, who had been obsessed with martial arts and nothing else, was so well-informed about current affairs.

[P158]
The answer I received was unexpected.

[P159]
“Because I’ve met him before. More accurately, I was summoned.”

[P160]
“Oh, really?”

[P161]
“Three years ago.”

[P162]
Well, if I was the rising super rookie of the moment, Jin Mukyung was already an established Peak master. It made sense that he would have been invited before me.

[P163]
“What was he like?”

[P164]
Jin Mukyung looked at me with a strange glint in his eyes.

[P165]
Then, wearing an ominous expression that mixed laughter with irritation, he spoke.

[P166]
“He was a fucking nightmare.”
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 삼류     | **Third Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 시스템              | **System**                     |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 귀가      | **your family**                                                 |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 삭주 | **Sakju** | Jin Family branch location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 현령 | **county magistrate** | County official who greets Jin Taekyung and delivers the City Lord's invitation. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 주씨 | **Zhu** | Surname of the imperial ruling house. |
| 친왕 | **Prince** | Imperial title held by the Shanxi City Lord. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 은자 | **silver nyang** | Silver currency unit. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 수문각 | **Gate Guard Pavilion** | Jin Family gate complex at the main entrance. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 129,
  "passed": true,
  "metrics": {
    "source_characters": 5886,
    "translation_characters": 14334,
    "length_ratio": 2.435,
    "source_paragraphs": 176,
    "translation_paragraphs": 166
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
        "korean": "귀가",
        "preferred": "your family"
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
        "korean": "기해",
        "preferred": "qi sea"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "세가",
        "preferred": "great family"
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
