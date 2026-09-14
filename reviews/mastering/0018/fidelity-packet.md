# Fidelity Gate — Chapter 18

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
  1|＃18화
  2|
  3|
  4|
  5|분위기는 점점 최악으로 치닫기 시작했다.
  6|
  7|“중요한 사실은 비무가 정당했다는 것입니다!”
  8|
  9|“정당? 요즘은 독을 쓰는 걸 정당하다고 하나? 여기가 무슨 사천당문이야?”
 10|
 11|“본인이 아니라고 하지 않소! 그리고 앞서 약왕당주가 말했듯이 이소군은 멀쩡했…….”
 12|
 13|“삼공자야 당연히 아니라고 하겠지. 그리고 저 돌팔이 말을 어떻게 믿어?”
 14|
 15|“돌팔이? 이 새끼가 진짜!”
 16|
 17|그때 잔뜩 흥분한 목소리 하나가 귓가를 파고들었다.
 18|
 19|“필요하다면 삼공자의 목을 바쳐서라도 전쟁을 막아야지!”
 20|
 21|……뭐?
 22|
 23|“그 무슨 망발이오!”
 24|
 25|“내 말이 틀렸소? 이제 그만 인정합시다. 항산검문은 본가보다 강하오. 전쟁이 시작되면 수백이 죽거나 다칠 테고, 최악의 경우에는 멸문이오. 모든 원인인 삼공자를 넘기면 끝나는 일 아닌가!”
 26|
 27|저게 말이냐, 방구냐. 모처럼 대단한 개소리를 들었더니 뒷골이 당기고 가슴이 답답해져 온다. 하지만 나보다 먼저 나선 사람이 있었다.
 28|
 29|“방금 뭐라 했소?”
 30|
 31|나직한 목소리지만 힘이 실려 있었다. 오히려 나직하기에 더 선명하게 들린다.
 32|
 33|진위경이다. 그가 무표정한 얼굴로 사람들을 둘러봤다.
 34|
 35|“누구. 목을. 바치자고?”
 36|
 37|한 음절씩 뚝뚝 끊어지는 음성에 서리가 꼈다. 나도 순간적으로 몸이 으슬으슬할 정도의 분위기인데, 백호당주가 냉큼 입을 열었다.
 38|
 39|“그거야 당연히 이 일의 주범인 삼공자…… 아.”
 40|
 41|저 새끼는 모발도 없는데 눈치까지 없네. 백호당주는 말꼬리를 흐렸지만 이미 늦었다.
 42|
 43|“그래서, 확인되지도 않은 일로 삼공자의 목을 항산검문에 갖다 바치시겠다? 그게 가문 당주의 입에서 나올 말이오?”
 44|
 45|“아니, 내 말은 그런 뜻이 아니라…….”
 46|
 47|백호당주가 진위경의 기세에 눌려 그의 눈을 피한다. 진위경이 가만히 백호당주를 노려보았다. 안 그러던 사람이 화가 나니 더 무섭다.
 48|
 49|하얗게 질린 백호당주의 얼굴을 보니 10년 묵은 체증이 내려가는 기분이다. 자리에서 일어난 진위경은 냉엄한 얼굴로 좌중을 내려다봤다.
 50|
 51|“이미 다들 알고 있소.”
 52|
 53|진위경이 모두를 둘러보며 단호히 말했다.
 54|
 55|“비무는 공정했고 이소군의 독살은 음모라는 것을. 그 사실을 알면서도 두려움 때문에 저들에게 굴복하자는 거요?”
 56|
 57|장로원 측 인사들이 시선을 회피했다. 진위경의 냉소가 더욱 짙어졌다.
 58|
 59|“누가 쥐여 줬는지는 모르겠지만, 항산검문은 명분이라는 칼자루를 쥐고 있소. 오늘일지, 내일일지. 아니면 이미 뽑혔는지도 모르지만 우리가 되돌리기에는 늦었소. 방법은 단 하나. 맞서 싸우는 것뿐이오.”
 60|
 61|“…….”
 62|
 63|“살고 싶소? 가문을 지키고 싶소? 진정 그렇다면 무사들을 준비시키고 전쟁을 준비하시오. 아니면 나와 내 아우의 목을 베어 저들에게 바치시든가. 그저 부귀영화만을 바란다면 그것도 나쁘지 않은 방법이겠지.”
 64|
 65|숨 막히는 정적이 대회의장을 점령했다.
 66|
 67|다음 순간, 한 사람이 입을 열지 않았다면 몇 시간이고 그 정적에 짓눌려 있었을지도 몰랐다.
 68|
 69|“훌륭하다.”
 70|
 71|지금까지 말없이 사태를 관망하던 한 사람.
 72|
 73|대장로였다.
 74|
 75|
 76|
 77|* * *
 78|
 79|
 80|
 81|대장로.
 82|
 83|요주의 인물이다. 가문의 최고 웃어른이자 장로원의 수장.
 84|
 85|나는 앞서 들었던 진위경의 전음을 떠올렸다.
 86|
 87|‘조심하라고 했었지.’
 88|
 89|진위경이라는 NPC는 내게 있어 가장 큰 아군이자 조언자다.
 90|
 91|나는 그 말을 허투루 듣지 않았고, 틈틈이 대장로를 주시했다.
 92|
 93|그리고 한 가지 결론을 내렸다.
 94|
 95|‘시바, 도저히 모르겠다.’
 96|
 97|이 거지 같은 게임을 시작한 뒤 한 번이라도 마주친 NPC들의 숫자를 세라고 하면 족히 백은 넘어간다.
 98|
 99|그들에겐 각자의 표정과 성격이 있었다. 기루에서 만난 하인은 삶에 찌든 영업용 미소를 지었고, 나를 데려다준 마부는 허당끼가 있었으며 가문에서 만난 중진들은 의외로 단순하고 과격한 면모가 있다.
100|
101|하지만 대장로는…….
102|
103|‘표정을 못 읽겠어.’
104|
105|그는 그저 묘한 웃음을 지으며 이 모든 것을 지켜볼 뿐이다.
106|
107|심문이 시작되었을 때도, 중진들이 각자의 파벌에서 고함을 내지를 때도, 그리고 지금 이 순간에도.
108|
109|짝. 짝. 짝.
110|
111|대장로의 힘찬 박수 소리가 울려 퍼졌다.
112|
113|“어리게만 생각했건만, 어느새 소가주가 이리 당당한 무인이 되었구려. 훌륭하오. 그래야 본가의 소가주라 할 수 있지.”
114|
115|“못난 꼴을 보여 드려 죄송할 따름입니다.”
116|
117|“과한 겸손은 오만으로 비치는 법. 소가주는 사과할 것 없소.”
118|
119|대장로의 칭찬에도 진위경은 여전히 굳은 얼굴이었다.
120|
121|“이 늙은이도 한마디 보탤까 하는데, 소가주의 생각은 어떠신가?”
122|
123|“새겨듣겠습니다.”
124|
125|천천히 자리에서 일어난 대장로에게 수십 쌍의 시선이 꽂혔다.
126|
127|가문의 최고 웃어른이다. 가문 내 권위나 입지로 치자면 진위경을 뛰어넘을지도 모른다.
128|
129|가장 큰 문제는 그가 반대 세력인 장로원의 수장이라는 거고.
130|
131|‘시발, 좆 됐네.’
132|
133|최악의 상황을 대비해 슬금슬금 문 쪽으로 몸을 돌리는 내 귓가에, 대장로의 첫 마디가 파고들었다.
134|
135|“썩어 빠졌구나.”
136|
137|응?
138|
139|고개를 홱 돌렸다. 대장로는 여전히 특유의 묘한 웃음을 짓고 있었다. 내가 잘못 들었나?
140|
141|하지만 아니었다.
142|
143|“하물며 짐승들조차도, 제 굴에 적이 들어오면 함께 힘을 합쳐 싸우는 법이다. 그런데 가문의 중진씩이나 되는 것들이 직계의 목을 바치고 전쟁을 막겠다는 걸 대책이라고 내어놓고 있구나. 허허. 이런 놈들이 본가의 가로회의에 앉아 있단 말이지.”
144|
145|“노, 노야. 오해십니다. 그것은 그저…….”
146|
147|“백호당주.”
148|
149|서늘한 대장로의 부름에 백호당주가 바짝 긴장했다.
150|
151|“내 외유가 너무 길었던 것인가? 아니면 가주가 자리를 비웠기 때문인가?”
152|
153|“노, 노야.”
154|
155|표정만 보면 밥 먹었냐 물어보는 헬스장 몸짱 할아버진데, 말하는 내용은 살벌하기 그지없다.
156|
157|‘뭐야, 이거.’
158|
159|어떻게 돌아가는 거야? 왜 우리 편을 들어?
160|
161|눈동자를 팽팽 돌려 봤지만, 사람들의 반응도 나와 다르지 않았다. 양측 모두 당황한 기색이 역력했다.
162|
163|“어찌 생각하시오, 소가주?”
164|
165|“무엇을 말씀하시는 것인지.”
166|
167|“전쟁이 기정사실화되었다면 내부를 단속하는 것이 우선이겠지. 그러니 역도나 다름없는 저들의 목을 베는 게 우선일 텐데?”
168|
169|얼어붙은 공기 속, 진위경은 한동안 물끄러미 대장로를 바라보다가 한숨처럼 대답을 토해 냈다.
170|
171|“그럴 수는 없습니다.”
172|
173|휴우. 백호당주가 안도의 한숨을 내쉬었다. 아까 내 목을 갖다 바치느니 마니 했던 걸 생각하면 살짝 아쉽다.
174|
175|……저 자식만 죽이자고 말해 볼까.
176|
177|“저들은 가문의 직계를 모함하는 것으로도 모자라 적들에게 넘기자고 주장했는데, 너무 무른 처사라고 생각하지 않나?”
178|
179|“오랜 세월 본가에 충성한 이들입니다. 흥분해서 나온 실언이라고 생각하겠습니다.”
180|
181|진위경의 대답에 대장로가 껄껄 웃었다.
182|
183|“실언, 실언이라. 그래. 소가주의 그릇은 내 생각 이상으로 크구려. 과연 소가주요. 그렇다면 이들에 대한 책임은 묻지 않기로 하지. 늙은이들의 실언을 담대하게 용서해 준 소가주께 감사를 표하는 바요.”
184|
185|이어 대장로가 고개를 숙이자 사람들이 다급하게 손사래를 치며 마주 허리를 굽혔다.
186|
187|“아이고, 노야. 아닙니다. 저희의 생각이 짧았습니다.”
188|
189|“제발 이러지 마십시오.”
190|
191|“이러시면 저희가 더욱 부끄러워집니다. 부디…….”
192|
193|“노야……!”
194|
195|살려 준 건 진위경인데 난리가 났다. 아주 생쇼를 해라, 생쇼를.
196|
197|내심 혀를 차며 그 모습을 지켜보던 순간이었다.
198|
199|‘아니, 잠깐만. 쇼?’
200|
201|정체 모를 위화감이 온몸을 감싼다. 나는 황급히 대장로 주위에 모여든 이들을 살폈다. 그리고 발견했다.
202|
203|앞서 나를 몰아세웠던 장로원. 그들의 입가에 스치는 웃음을.
204|
205|‘설마…….’
206|
207|계획된 거라고? 이 모든 게 다?
208|
209|도대체 무슨 의도로, 뭘 위해서? 수많은 물음이 떠올랐다 사라진다. 머릿속이 엉망진창이었다.
210|
211|‘진위경은 뭔가 알고 있을까?’
212|
213|고개를 돌려 찾을 필요도 없었다. 대장로가 진위경의 손을 번쩍 들고 외치고 있었으니까.
214|
215|“가주가 자리를 비운 지금, 소가주가 가주나 다름없소. 이 일에 대해서 나는 소가주를 지지하겠소. 그를 중심으로 뭉친다면 저들이 아무리 대단하다 해도 감히 진가를 넘볼 수 없을 것이오!”
216|
217|달아오른 분위기, 사람들의 연호와 함성.
218|
219|이걸 어디서 봤더라, 왠지 모르게 익숙한 느낌이다.
220|
221|그리고.
222|
223|“감사합니다.”
224|
225|파르르 떨리는 진위경의 입꼬리와 대장로의 묘한 웃음을 보는 순간, 나는 익숙한 느낌의 정체를 깨달았다.
226|
227|‘선거 유세.’
228|
229|대장로의 모습과 TV 속 정치인이 겹쳐 보였다.
230|
231|
232|
233|* * *
234|
235|
236|
237|상당히 찜찜하긴 했지만, 일단 대장로가 진위경의 손을 들어 주자 회의는 일사천리로 진행되었다.
238|
239|장로원 측에서 끈질기게 물고 늘어졌던 비무 관련 이야기는 쏙 들어가고, 전쟁을 전제로 한 회의 내용이 주를 이뤘다.
240|
241|“현재 가용 인원은 어떻게 되나?”
242|
243|“외부 파견 중인 무사들까지 불러들인다면…… 이백 남짓입니다.”
244|
245|이백 명이나 된다고? 나는 의외로 많은 숫자에 혀를 내둘렀지만 이어지는 대화에 입을 다물었다.
246|
247|“일류 이상의 정예로 엄선한다면?”
248|
249|“스물이 채 안 됩니다. 물론 이 자리에 계신 분들을 포함하면 다르겠지만 말입니다.”
250|
251|중진들을 포함하면 일류 고수의 숫자는 3, 40명 남짓.
252|
253|이곳 사정은 잘 모르지만, 이 정도면 양호한 수준인 것 같다.
254|
255|역시 뿌리 깊은 명문세가. 200년을 이어 온 저력이 어디 가는 게 아니다.
256|
257|“항산검문 측은?”
258|
259|“우선 확인된 무사들만 최소 삼백입니다.”
260|
261|삼백. 그것도 최소로 잡았으니 백 명 이상의 차이다.
262|
263|하지만 괜찮다. 원래 싸움은 머릿수로 하는 게…….
264|
265|“그리고 일류는 오십 이상입니다.”
266|
267|이 전쟁, 어렵다. 그래도 진위경과 위팽 같은 고수들이 있다면 해 볼 만한 싸움이다. 그들은 기감으로도 읽지 못하는 고레벨의 NPC들이니까. 아마 대장로도 그 범주에 포함되는 존재일 것이다.
268|
269|“본가의 절정 고수는 소가주와 노야, 위 대협까지 총 셋입니다. 그리고 항산검문의 절정 고수는 다섯이지요.”
270|
271|……거지 같아서 못 해 먹겠네. 진짜.
272|
273|‘뭐? 뿌리 깊은 명문세가? 200년 역사?’
274|
275|이 새끼들은 200년 동안 뭘 한 거야. 듣자 하니 항산검문의 역사가 30년도 안 된다는데, 전력 면에서 밀리다 못해 압살이다. 압살.
276|
277|‘작년에 흑사병이라도 돌았나.’
278|
279|흑사병이 돌았건 말건 당장 내가 돌아 버릴 것 같다. 나는 어느새 노래진 회의실 천장을 바라보다 문득 다짐했다.
280|
281|‘튀어야겠다.’
282|
283|새벽 네 시 정도면 적당하겠지. 다들 잠들어 있을 때 몰래 담을 넘어서 멀리 도망가는 거다.
284|
285|지금의 나라면 천력부 정도의 수준은 대여섯이 덤벼도 손쉽게 해치울 수 있다.
286|
287|보이는 산마다 싹 뒤지면서 경험치와 명성을…….
288|
289|“항산, 항산검문에서 전서구가 도착했습니다!”
290|
291|황급히 들이닥친 무사의 외침이었다. 누군가 돌돌 말린 종이를 받아 펼치자 피로 쓴 듯 붉은 글자가 눈에 들어왔다.
292|
293|굳이 시스템이 번역해 주지 않아도 알아볼 수 있는 글자였다.
294|
295|
296|
297|不俱戴天
298|
299|
300|
301|‘불구대천.’
302|
303|하늘 아래 같이 살 수 없는 원수.
304|
305|진위경이 무거운 얼굴로 입을 열었다.
306|
307|“현 시간부로 본가는 전시 상황에 돌입한다. 내 인(印) 없이는 지위 고하를 막론하고 세가 외 출입을 금하며, 삼엄한 경계 태세를 유지해야 할 것이다. 개미 새끼 한 마리도 들이지 말라. 알겠는가!”
308|
309|“옛!”
310|
311|“…….”
312|
313|넋이 반쯤 나간 내 귓가로, 시스템 알림이 울렸다.
314|
315|띠링.
316|
317|
318|
319|- [항산검문]이 [태원진가]에 선전포고했습니다.
320|
321|- [전쟁] 관계가 양측 진영에 성립되었습니다.
322|
323|- [항산검문]이 당신을 문파 공적으로 지목합니다.
324|
325|- 도망칠 경우 심각한 불이익을 받게 될 것입니다.
326|
327|- [메인 퀘스트 - 전쟁]이 생성되었습니다.
328|
329|
330|
331|……허허. 허허허허.
```

## Assembled English

```markdown
[P1]
# Chapter 18

[P2]
The atmosphere went from bad to worse.

[P3]
“The important thing is that the duel was fair!”

[P4]
“Fair? Since when is using poison considered fair? What is this, the Sichuan Tang Clan?”

[P5]
“The man himself said he didn’t do it! And as the Medicine King Hall Leader said earlier, Lee Seogeun was perfectly fine—”

[P6]
“Of course the Third Young Master would deny it. And how can you trust that quack?”

[P7]
“A quack? You bastard!”

[P8]
Then one particularly agitated voice pierced my ears.

[P9]
“If necessary, we should prevent the war even if it means offering up the Third Young Master’s head!”

[P10]
…What?

[P11]
“What outrageous nonsense!”

[P12]
“Am I wrong? Let’s just admit it. The Mount Heng Sword Sect is stronger than our family. If war begins, hundreds will die or be injured, and in the worst case, our family could be destroyed. If we hand over the Third Young Master, who caused all this, won’t everything be over?”

[P13]
Was that supposed to be an argument, or a fart? It had been a while since I’d heard such spectacular bullshit. The back of my neck tightened, and my chest grew tight.

[P14]
But someone else stepped forward before I could.

[P15]
“What did you just say?”

[P16]
The voice was quiet, but it carried power. If anything, its quietness made every word clearer.

[P17]
It was Jin Wikyung. He surveyed the room, his face expressionless.

[P18]
“Whose. Head. Did you say we should offer?”

[P19]
Each syllable fell separately, frost coating his voice. The atmosphere was so chilling that even I shivered.

[P20]
The White Tiger Hall Leader immediately opened his mouth.

[P21]
“Obviously, the Third Young Master, the main culprit behind this—ah.”

[P22]
The bastard had no hair and no tact. The White Tiger Hall Leader trailed off, but it was already too late.

[P23]
“So you intend to hand the Third Young Master’s head over to the Mount Heng Sword Sect over something that has not even been confirmed? Is that something a hall leader of this family should be saying?”

[P24]
“No, that’s not what I meant…”

[P25]
Overwhelmed by Jin Wikyung’s aura, the White Tiger Hall Leader avoided his gaze. Jin Wikyung silently glared at him.

[P26]
He wasn’t normally like this, which made him even scarier now that he was angry.

[P27]
The sight of the White Tiger Hall Leader’s pale face felt like ten years of indigestion finally clearing up. Jin Wikyung rose from his seat and looked down at everyone with a cold expression.

[P28]
“You all already know.”

[P29]
He swept his gaze across the room and spoke firmly.

[P30]
“That the duel was fair, and Lee Seogeun’s poisoning was a conspiracy. Knowing that, are you suggesting we submit to them out of fear?”

[P31]
The members of the Elder Council faction avoided his gaze. Jin Wikyung’s sneer grew deeper.

[P32]
“I don’t know who placed it in their hands, but the Mount Heng Sword Sect now holds the hilt of a sword called justification. Whether they draw it today or tomorrow—or whether it has already been drawn—it is too late for us to turn things back. Only one path remains. We fight.”

[P33]
“…”

[P34]
“Do you want to live? Do you want to protect the family? If you truly do, prepare the martial artists and prepare for war. Or cut off my head and my younger brother’s, then offer them to the Mount Heng Sword Sect. If all you want is wealth and glory, I suppose that isn’t a bad option, either.”

[P35]
A suffocating silence seized the main assembly hall.

[P36]
If one man had not spoken the next moment, that silence might have crushed us for hours.

[P37]
“Excellent.”

[P38]
It was the man who had watched the situation without saying a word until now.

[P39]
The Head Elder.

[P40]
* * *

[P41]
The Head Elder.

[P42]
Someone to watch. The family’s most senior elder and the head of the Elder Council.

[P43]
I recalled Jin Wikyung’s earlier Sound Transmission.

[P44]
*He told me to be careful.*

[P45]
Among all the NPCs, Jin Wikyung was my greatest ally and adviser.

[P46]
I hadn’t taken his warning lightly. I’d watched the Head Elder whenever I had the chance.

[P47]
And I’d reached one conclusion.

[P48]
*Fuck, I can’t figure him out at all.*

[P49]
If someone asked me to count the number of NPCs I had encountered even once since starting this godforsaken game, the number would easily be over a hundred.

[P50]
Each of them had their own expressions and personalities. The servant I’d met at the pleasure house wore a world-weary customer-service smile. The coachman who brought me here had a goofy streak. The family’s senior members were surprisingly simple-minded and aggressive.

[P51]
But the Head Elder…

[P52]
*I can’t read his expression.*

[P53]
He simply watched everything with that strange smile.

[P54]
When the interrogation began. When the senior members of each faction shouted at one another. And even now.

[P55]
Clap. Clap. Clap.

[P56]
The Head Elder’s vigorous applause rang through the hall.

[P57]
“I thought of you as nothing more than a youngster, but before I knew it, the Lesser Family Head had become such a dignified martial artist. Excellent. That is how the Lesser Family Head of our family should be.”

[P58]
“I can only apologize for showing you such an unseemly side.”

[P59]
“Excessive humility can appear arrogant. You have nothing to apologize for.”

[P60]
Despite the Head Elder’s praise, Jin Wikyung’s face remained stiff.

[P61]
“May this old man add a word? What do you think, Lesser Family Head?”

[P62]
“I will take it to heart.”

[P63]
The Head Elder slowly rose from his seat, and dozens of pairs of eyes locked onto him.

[P64]
He was the family’s most senior elder. In terms of authority and standing within the family, he might even surpass Jin Wikyung.

[P65]
The biggest problem was that he was the head of the opposing faction—the Elder Council.

[P66]
*Fuck, I’m screwed.*

[P67]
Preparing for the worst, I started edging toward the door when the Head Elder’s first words reached my ears.

[P68]
“You’re rotten to the core.”

[P69]
Huh?

[P70]
I whipped my head around. The Head Elder still wore that same strange smile.

[P71]
*Did I hear him wrong?*

[P72]
But I hadn’t.

[P73]
“Even beasts join forces and fight when an enemy enters their den. And yet men who are supposedly senior members of this family offer up the head of a direct-line member as a solution to stop a war. Heh. So men like this sit in our family council.”

[P74]
“N-no, Head Elder. You’ve misunderstood. It was merely…”

[P75]
“White Tiger Hall Leader.”

[P76]
At the Head Elder’s chilly call, the White Tiger Hall Leader stiffened.

[P77]
“Have I been away for too long? Or is it because the Family Head is absent?”

[P78]
“N-no, Head Elder.”

[P79]
Judging by his expression alone, he looked like a muscular old man at the gym asking whether you’d eaten. The words coming out of his mouth, however, were vicious beyond belief.

[P80]
*What is this?*

[P81]
What was going on? Why was he taking our side?

[P82]
I looked around frantically, but everyone else was just as confused as I was. Both factions were visibly flustered.

[P83]
“What do you think, Lesser Family Head?”

[P84]
“I’m not sure what you mean.”

[P85]
“If war has become inevitable, then our first priority should be to discipline those within our ranks. Wouldn’t it be best to cut off the heads of those men who are little different from rebels?”

[P86]
In the frozen air, Jin Wikyung stared at the Head Elder for a long moment before forcing out an answer like a sigh.

[P87]
“That cannot be done.”

[P88]
Whew.

[P89]
The White Tiger Hall Leader sighed in relief.

[P90]
Considering how he had just been talking about offering up my head, I was a little disappointed.

[P91]
*Should I suggest killing just him?*

[P92]
“Those men were not content merely to frame a direct-line member of the family. They even argued that we should hand him over to the enemy. Do you not think your response is too lenient?”

[P93]
“They have served our family faithfully for many years. I will consider their words an ill-considered remark made in the heat of the moment.”

[P94]
The Head Elder laughed heartily.

[P95]
“An ill-considered remark. An ill-considered remark, indeed. Yes. The Lesser Family Head’s capacity is greater than I expected. Truly worthy of being the Lesser Family Head. In that case, I will not hold them responsible. I offer my thanks to the Lesser Family Head for magnanimously forgiving the thoughtless words of old men.”

[P96]
When the Head Elder bowed, the others hurriedly waved their hands and bent at the waist in return.

[P97]
“Oh, Head Elder, no. Our thoughts were shallow.”

[P98]
“Please, don’t do this.”

[P99]
“You’re only making us more ashamed. Please…”

[P100]
“Head Elder!”

[P101]
Jin Wikyung was the one who had spared them, yet they were making a huge scene.

[P102]
Go on, put on a show. A real show.

[P103]
I watched the spectacle, clicking my tongue inwardly, when—

[P104]
*Wait. A show?*

[P105]
An inexplicable sense of wrongness settled over me. I hurriedly examined the people gathered around the Head Elder.

[P106]
And then I noticed it.

[P107]
The smiles flickering around the lips of the Elder Council members who had cornered me earlier.

[P108]
*No way…*

[P109]
Had all of this been planned? Every last bit of it?

[P110]
Why? For what purpose? Countless questions rose and vanished. My thoughts were a complete mess.

[P111]
*Does Jin Wikyung know something?*

[P112]
I didn’t even need to turn around to look for him. The Head Elder was already holding Jin Wikyung’s hand high in the air and shouting.

[P113]
“With the Family Head absent, the Lesser Family Head is effectively the Family Head. I support the Lesser Family Head in this matter. If we unite around him, then no matter how formidable they are, they will not dare challenge the Jin Family!”

[P114]
The heated atmosphere. The people’s cheers and shouts.

[P115]
*Where had I seen this before?*

[P116]
It felt strangely familiar.

[P117]
And then—

[P118]
“Thank you.”

[P119]
The moment I saw the corners of Jin Wikyung’s mouth quiver and the Head Elder’s strange smile, I realized where that familiar feeling came from.

[P120]
*A campaign rally.*

[P121]
The Head Elder’s figure overlapped with the politicians I had seen on television.

[P122]
* * *

[P123]
It left a bad taste in my mouth, but once the Head Elder raised Jin Wikyung’s hand, the meeting proceeded swiftly.

[P124]
The discussion about the duel, which the Elder Council faction had stubbornly kept dragging out, disappeared entirely. Instead, the meeting focused on preparing for war.

[P125]
“How many men are currently available?”

[P126]
“If we call back the martial artists stationed outside… roughly two hundred.”

[P127]
As many as two hundred?

[P128]
I was astonished by the unexpectedly large number, but the next question made me shut my mouth.

[P129]
“If we select only elites of First Rate or higher?”

[P130]
“Fewer than twenty. Of course, that number would be different if we included everyone present.”

[P131]
Including the senior members, there were around thirty or forty First Rate masters.

[P132]
I didn’t know much about how things worked here, but that seemed like a decent number.

[P133]
As expected of a prestigious family with deep roots. Two hundred years of accumulated strength didn’t simply vanish.

[P134]
“What about the Mount Heng Sword Sect?”

[P135]
“At least three hundred martial artists have been confirmed so far.”

[P136]
Three hundred. And that was only the minimum, putting the difference at more than a hundred men.

[P137]
But that was fine. It wasn’t as if fights were decided by numbers—

[P138]
“And they have more than fifty First Rate martial artists.”

[P139]
This war was going to be difficult.

[P140]
Still, with masters like Jin Wikyung and Wipeng, it was a fight worth attempting. They were high-level NPCs beyond what my Qi Sense could read. The Head Elder probably belonged to that category, too.

[P141]
“Our family has three Peak masters in total: the Lesser Family Head, the Head Elder, and Sir Wipeng. The Mount Heng Sword Sect has five.”

[P142]
…Fuck this. I couldn’t do it. Seriously.

[P143]
*What? A prestigious family with deep roots? Two hundred years of history?*

[P144]
What the hell had these bastards been doing for two hundred years? I’d heard the Mount Heng Sword Sect was less than thirty years old, yet we weren’t merely outmatched in military strength.

[P145]
We were being steamrolled. Steamrolled.

[P146]
*Did the Black Death sweep through last year or something?*

[P147]
Whether there had been a plague or not, I felt like I was going insane. I was staring at the meeting-hall ceiling, which had yellowed before I knew it, when I suddenly made a decision.

[P148]
*I need to run.*

[P149]
Around four in the morning should do. Once everyone was asleep, I’d sneak over the wall and run as far away as possible.

[P150]
At my current level, I could easily take down five or six martial artists around the Heavenly Axe’s level.

[P151]
I could scour every mountain I came across and rack up EXP and Fame—

[P152]
“Mount Heng—A messenger pigeon has arrived from the Mount Heng Sword Sect!”

[P153]
A martial artist had rushed into the hall and shouted.

[P154]
Someone took the tightly rolled sheet of paper and unrolled it. Red characters, as if written in blood, appeared before my eyes.

[P155]
Even without the System translating them, I could understand what they said.

[P156]
> **Enemies Who Cannot Live Beneath the Same Sky**

[P157]
*Enemies who cannot coexist beneath heaven.*

[P158]
Jin Wikyung spoke, his expression grim.

[P159]
“From this moment onward, our family enters a state of war. Without my seal, no one may enter or leave the family grounds, regardless of rank. Maintain a strict state of vigilance. Do not let so much as a single ant through. Understood?”

[P160]
“Yes!”

[P161]
“…”

[P162]
With my mind half gone, I heard a System notification ring in my ears.

[P163]
Ding.

[P164]
> **System**
>
> - The **Mount Heng Sword Sect** has declared war on the **Jin Family of Taiyuan**.
>
> - A **War** relationship has been established between the two factions.
>
> - The **Mount Heng Sword Sect** has designated you as a public enemy of the sect.
>
> - You will incur severe penalties if you flee.
>
> - The **Main Quest — War** has been created.

[P165]
…Heh. Heh heh heh.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 18

[P2]
The atmosphere grew worse by the second.

[P3]
“The important fact is that the duel was fair!”

[P4]
“Fair? Since when is using poison considered fair? Is this the Sichuan Tang Clan or something?”

[P5]
“The man himself said he didn’t do it! And as the Medicine King Hall Leader said earlier, Lee Seogeun was perfectly fine—”

[P6]
“Of course the Third Young Master would say he didn’t. And how can you believe that quack?”

[P7]
“A quack? You little bastard!”

[P8]
Then one particularly agitated voice pierced my ears.

[P9]
“If necessary, we should stop the war even if it means offering up the Third Young Master’s head!”

[P10]
…What?

[P11]
“What kind of outrageous nonsense is that?”

[P12]
“Am I wrong? Let’s just admit it. The Mount Heng Sword Sect is stronger than our family. If war begins, hundreds will die or be injured, and in the worst case, our family could be destroyed. If we hand over the Third Young Master, who caused all this, won’t everything be over?”

[P13]
What kind of bullshit was that? I hadn’t heard such spectacular nonsense in a long time. The back of my neck tightened, and my chest grew tight.

[P14]
But someone else stepped forward before I could.

[P15]
“What did you just say?”

[P16]
His voice was quiet, but it carried power. In fact, its quietness made it sound even clearer.

[P17]
It was Jin Wikyung. He looked around the room with an expressionless face.

[P18]
“Whose. Head. Did you say we’d offer?”

[P19]
Each syllable fell separately, frost coating his voice. The atmosphere was so chilling that even I shivered.

[P20]
The White Tiger Hall Leader spoke up at once.

[P21]
“Obviously, the Third Young Master, the main culprit behind this—ah.”

[P22]
That bastard was bald, and he couldn’t read the room either. The White Tiger Hall Leader let his words trail off, but it was already too late.

[P23]
“So you intend to hand the Third Young Master’s head over to the Mount Heng Sword Sect over something that has not even been confirmed? Is that something a hall leader of this family should be saying?”

[P24]
“No, that’s not what I meant…”

[P25]
The White Tiger Hall Leader was overwhelmed by Jin Wikyung’s aura and avoided his eyes. Jin Wikyung silently glared at him.

[P26]
He wasn’t normally like this, which made him even scarier now that he was angry.

[P27]
Looking at the White Tiger Hall Leader’s pale face made me feel as if ten years of indigestion had finally been cured. Jin Wikyung rose from his seat and looked down at everyone with a cold expression.

[P28]
“You all already know.”

[P29]
He looked around the room and spoke firmly.

[P30]
“That the duel was fair, and Lee Seogeun’s poisoning was a conspiracy. Knowing that, are you suggesting we submit to them out of fear?”

[P31]
The members of the Elder Council faction avoided his gaze. Jin Wikyung’s sneer grew deeper.

[P32]
“I don’t know who placed it in their hands, but the Mount Heng Sword Sect holds the hilt of a sword called justification. Whether it happens today or tomorrow—or whether the sword has already been drawn—we are already too late to reverse it. There is only one way forward. We fight.”

[P33]
“……”

[P34]
“Do you want to live? Do you want to protect the family? If you truly do, prepare the martial artists and prepare for war. Or cut off my head and my younger brother’s, then offer them to the Mount Heng Sword Sect. If all you want is wealth and glory, I suppose that isn’t a bad option, either.”

[P35]
A suffocating silence took over the main assembly hall.

[P36]
If one person hadn’t opened his mouth the next moment, we might have been crushed beneath that silence for hours.

[P37]
“Excellent.”

[P38]
It was the man who had watched the situation without saying a word until now.

[P39]
The Head Elder.

[P40]
* * *

[P41]
The Head Elder.

[P42]
A person to watch out for. The family’s highest-ranking elder and the head of the Elder Council.

[P43]
I remembered the Sound Transmission Jin Wikyung had sent me earlier.

[P44]
*He told me to be careful.*

[P45]
Jin Wikyung was the greatest ally and adviser I had among the NPCs.

[P46]
I hadn’t taken his warning lightly. Whenever I had the chance, I kept an eye on the Head Elder.

[P47]
And I reached one conclusion.

[P48]
*Fuck, I can’t figure him out at all.*

[P49]
If someone asked me to count the number of NPCs I had encountered even once since starting this godforsaken game, the number would easily be over a hundred.

[P50]
Each of them had their own expressions and personalities. The servant I met at the pleasure house wore a business smile worn down by life. The coachman who brought me here had a goofy side. The senior members I met in the family were surprisingly simple-minded and aggressive.

[P51]
But the Head Elder…

[P52]
*I can’t read his expression.*

[P53]
He merely watched everything with that strange smile of his.

[P54]
When the interrogation began. When the senior members of each faction shouted at one another. And even now.

[P55]
Clap. Clap. Clap.

[P56]
The Head Elder’s vigorous applause rang through the hall.

[P57]
“I thought of you as nothing more than a youngster, but before I knew it, the Lesser Family Head had become such a dignified martial artist. Excellent. That is how the Lesser Family Head of our family should be.”

[P58]
“I can only apologize for showing you such an unseemly side.”

[P59]
“Excessive humility can look like arrogance. You have nothing to apologize for.”

[P60]
Despite the Head Elder’s praise, Jin Wikyung’s face remained stiff.

[P61]
“May this old man add a word? What do you think, Lesser Family Head?”

[P62]
“I will take it to heart.”

[P63]
The Head Elder slowly rose from his seat, and dozens of pairs of eyes locked onto him.

[P64]
He was the family’s highest-ranking elder. In terms of authority and standing within the family, he might even surpass Jin Wikyung.

[P65]
The biggest problem was that he was the head of the opposing faction—the Elder Council.

[P66]
*Fuck, I’m screwed.*

[P67]
Preparing for the worst, I started edging toward the door when the Head Elder’s first words reached my ears.

[P68]
“You’re rotten to the core.”

[P69]
Huh?

[P70]
I whipped my head around. The Head Elder still wore that same strange smile.

[P71]
*Did I hear him wrong?*

[P72]
But I hadn’t.

[P73]
“Even beasts join forces and fight when an enemy enters their den. And yet men who are supposedly senior members of this family offer up the head of a direct-line member as a solution to stop a war. Heh. So men like this sit in our family council.”

[P74]
“N-no, Head Elder. You’ve misunderstood. It was merely…”

[P75]
“White Tiger Hall Leader.”

[P76]
At the Head Elder’s chilly call, the White Tiger Hall Leader stiffened.

[P77]
“Have I been away for too long? Or is it because the Family Head is absent?”

[P78]
“N-no, Head Elder.”

[P79]
Going by the Head Elder’s expression, he looked like a muscular old man at a gym asking whether you’d eaten. But the content of his words was vicious beyond belief.

[P80]
*What is this?*

[P81]
What was going on? Why was he taking our side?

[P82]
I looked around frantically, but everyone else was just as confused as I was. Both factions were visibly flustered.

[P83]
“What do you think, Lesser Family Head?”

[P84]
“I’m not sure what you mean.”

[P85]
“If war has become inevitable, then our first priority should be to discipline those within our ranks. Wouldn’t it be best to cut off the heads of those men who are little different from rebels?”

[P86]
In the frozen air, Jin Wikyung stared at the Head Elder for a long moment before answering in something like a sigh.

[P87]
“That cannot be done.”

[P88]
Whew. The White Tiger Hall Leader let out a relieved sigh.

[P89]
Considering how he had just been talking about offering up my head, I was a little disappointed.

[P90]
*Should I suggest that we kill just him?*

[P91]
“Those men not only framed a direct-line member of the family, but even argued we should hand him over to the enemy. Don’t you think that is too lenient a response?”

[P92]
“They have served our family loyally for many years. I will consider it an ill-considered remark made in the heat of the moment.”

[P93]
The Head Elder laughed heartily.

[P94]
“An ill-considered remark. An ill-considered remark, indeed. Yes. The Lesser Family Head’s capacity is greater than I expected. Truly worthy of being the Lesser Family Head. In that case, I will not hold them responsible. I offer my thanks to the Lesser Family Head for magnanimously forgiving the thoughtless words of old men.”

[P95]
When the Head Elder bowed, the others hurriedly waved their hands and bent at the waist in return.

[P96]
“Oh, Head Elder, no. Our thoughts were shallow.”

[P97]
“Please, don’t do this.”

[P98]
“You’re only making us more ashamed. Please…”

[P99]
“Head Elder!”

[P100]
Jin Wikyung was the one who had spared them, yet they were making a huge scene.

[P101]
Go on, put on a show. A real show.

[P102]
I was watching the spectacle with a private click of my tongue when—

[P103]
*Wait. A show?*

[P104]
An indescribable sense of wrongness settled over me. I hurriedly examined the people gathered around the Head Elder.

[P105]
And then I noticed it.

[P106]
The smiles flickering around the lips of the Elder Council members who had pressured me earlier.

[P107]
*No way…*

[P108]
Was this all planned? Every bit of it?

[P109]
Why? For what purpose? Countless questions rose and vanished. My thoughts were a complete mess.

[P110]
*Does Jin Wikyung know something?*

[P111]
I didn’t even need to turn around to look for him. The Head Elder was already holding Jin Wikyung’s hand high in the air and shouting.

[P112]
“With the Family Head absent, the Lesser Family Head is effectively the Family Head. I support the Lesser Family Head in this matter. If we unite around him, then no matter how formidable they are, they will not dare challenge the Jin Family!”

[P113]
The heated atmosphere. The people’s cheers and shouts.

[P114]
*Where had I seen this before?*

[P115]
It felt strangely familiar.

[P116]
And then—

[P117]
“Thank you.”

[P118]
The moment I saw the corners of Jin Wikyung’s mouth quiver and the Head Elder’s strange smile, I realized where that familiar feeling came from.

[P119]
*An election campaign.*

[P120]
The Head Elder’s figure overlapped with the politicians I had seen on television.

[P121]
* * *

[P122]
It was deeply unsettling, but once the Head Elder raised Jin Wikyung’s hand, the meeting proceeded swiftly.

[P123]
The discussion about the duel, which the Elder Council faction had stubbornly kept dragging out, disappeared entirely. Instead, the meeting focused on preparing for war.

[P124]
“How many men are currently available?”

[P125]
“If we call back the martial artists stationed outside, roughly two hundred.”

[P126]
As many as two hundred?

[P127]
I was astonished by the unexpectedly large number, but the next question made me shut my mouth.

[P128]
“If we select only elites of First Rate or higher?”

[P129]
“Fewer than twenty. Of course, that number would be different if we included everyone present.”

[P130]
Including the senior members, there were around thirty or forty First Rate masters.

[P131]
I didn’t know much about the circumstances here, but that seemed like a decent number.

[P132]
As expected of a prestigious family with deep roots. Two hundred years of accumulated strength didn’t simply vanish.

[P133]
“What about the Mount Heng Sword Sect?”

[P134]
“At least three hundred martial artists have been confirmed so far.”

[P135]
Three hundred. And that was the minimum, meaning there was a difference of more than a hundred men.

[P136]
But it was fine. Fights came down to numbers anyway—

[P137]
“And they have more than fifty First Rate martial artists.”

[P138]
This war was going to be difficult.

[P139]
Still, with masters like Jin Wikyung and Wipeng, it was a fight worth attempting. They were high-level NPCs beyond what my Qi Sense could read. The Head Elder probably belonged to that category, too.

[P140]
“Our family has three Peak masters in total: the Lesser Family Head, the Head Elder, and Sir Wipeng. The Mount Heng Sword Sect has five.”

[P141]
…This was so damn hopeless I couldn’t even deal with it.

[P142]
*What? A prestigious family with deep roots? Two hundred years of history?*

[P143]
What the hell had these bastards been doing for two hundred years? I heard the Mount Heng Sword Sect had existed for less than thirty, but in terms of military strength, we weren’t merely outmatched.

[P144]
We were being steamrolled. Steamrolled.

[P145]
*Did the Black Death sweep through last year or something?*

[P146]
Whether there had been a plague or not, I felt like I was going insane. I was staring at the meeting-hall ceiling, which had yellowed before I knew it, when I suddenly made a decision.

[P147]
*I need to run.*

[P148]
Around four in the morning should do. Once everyone was asleep, I’d sneak over the wall and run as far away as possible.

[P149]
At my current level, I could easily take down five or six martial artists around the Heavenly Axe’s level.

[P150]
I could scour every mountain I came across and rack up EXP and Fame—

[P151]
“Mount Heng—A messenger pigeon has arrived from the Mount Heng Sword Sect!”

[P152]
A martial artist had rushed into the hall and shouted.

[P153]
Someone accepted the tightly rolled sheet of paper and unrolled it. Red words, as if written in blood, appeared before my eyes.

[P154]
Even without a System translation, I could understand them.

[P155]
> **Enemies Who Cannot Live Beneath the Same Sky**

[P156]
*Enemies who cannot coexist beneath heaven.*

[P157]
Jin Wikyung spoke with a grim expression.

[P158]
“From this moment onward, our family enters a state of war. Without my seal, no one may enter or leave the family grounds, regardless of rank. Maintain a strict state of vigilance. Do not let a single ant through. Understood?”

[P159]
“Yes!”

[P160]
“……”

[P161]
With my mind half gone, I heard a System notification ring in my ears.

[P162]
Ding.

[P163]
> **System**
>
> - The **Mount Heng Sword Sect** has declared war on the **Jin Family of Taiyuan**.
>
> - A **War** relationship has been established between both factions.
>
> - The **Mount Heng Sword Sect** has designated you as a public enemy of the sect.
>
> - You will incur severe penalties if you flee.
>
> - The **Main Quest — War** has been created.

[P164]
…Heh. Heh heh heh.
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 18,
  "passed": true,
  "metrics": {
    "source_characters": 5684,
    "translation_characters": 13348,
    "length_ratio": 2.348,
    "source_paragraphs": 157,
    "translation_paragraphs": 165
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
        "korean": "대협",
        "preferred": "Great Hero or Sir depending tone"
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
