# Fidelity Gate — Chapter 374

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
  1|＃374화
  2|
  3|
  4|
  5|독룡각(毒龍閣)의 각주인 당호룡은 자리에서 일어나 손님을 맞이했다.
  6|
  7|지금 막 문을 열고 들어온 장대한 체구의 사내에게서는 알 수 없는 위압감이 흘러넘쳤다.
  8|
  9|“먼 길 오느라 노고 많으셨소.”
 10|
 11|“사천당문이 겪은 고초에 비하면 아무것도 아니지요. 다시 한번 심심한 유감을 표합니다.”
 12|
 13|거친 용모와는 달리 사내의 목소리는 낮고 부드러웠으며, 동시에 듣는 이로 하여금 집중하게 만드는 힘이 있었다.
 14|
 15|무리를 이끄는 지도자만이 가지는 기세라고 할까? 온화하면서도 깊게 가라앉은 사내의 눈빛에, 당호룡은 문득 한 사람을 떠올렸다.
 16|
 17|‘이건…… 또 다른 종형(從兄)과 마주한 느낌이로군.’
 18|
 19|그 사실은 당호룡을 적잖이 당혹스럽게 했다.
 20|
 21|듣기로 눈앞의 사내는 불혹도 채 되지 않은 젊은 나이라고 했다.
 22|
 23|반면 그의 종형은 연배는 물론이거니와 무림에서의 입지도 대단한 인물이었다.
 24|
 25|정마대전이라는 전란 속에서 숱한 전공을 쌓고, 무너졌던 가문을 더욱 단단하게 일으켜 세운 철혈의 가주이기도 했다.
 26|
 27|만독수라(萬毒修羅) 당사독.
 28|
 29|사천당문의 가주 대행, 당호룡은 아직도 의식을 회복하지 못한 자신의 종형을 떠올리며 내심 한숨을 내쉬었다.
 30|
 31|‘어서 일어나서 우리를 이끌어 주십시오. 가주.’
 32|
 33|당호룡은 천생 무인이었다.
 34|
 35|독과 암기에 관해서는 일가를 이루었다고 자부하는 그였지만, 가문을 이끄는 것은 또 다른 영역이었다.
 36|
 37|특히 최근에는 곳곳에서 밀려드는 온갖 사안들에 혈육을 잃은 슬픔과 분노를 떠올릴 틈조차 없을 정도였다.
 38|
 39|‘차라리 이런 자가 지금 내 자리에 있었다면 좋았을 것을.’
 40|
 41|그런 의미에서 당호룡은 눈앞의 사내가 못내 부러웠다.
 42|
 43|단순히 첫인상만을 가지고 판단하는 것이 아니라, 사내에 관한 소문을 익히 들었기 때문이었다.
 44|
 45|그 소문의 반의반만 사실이라 해도 사내는 능히 일가를 이끌 역량의 소유자였다.
 46|
 47|“당 대협. 혹시 제 얼굴에 뭐라도 묻었습니까?”
 48|
 49|“아, 아무것도 아니오. 워낙 경황이 없어 무례를 범했구려.”
 50|
 51|당호룡의 황급한 사과에 사내가 진중한 얼굴로 고개를 끄덕였다.
 52|
 53|“아닙니다. 그럴 만도 하지요. 그토록 참담한 일을 겪으셨으니.”
 54|
 55|사실 이번에 사천당문이 입은 피해는 참담이라는 말로도 부족했다.
 56|
 57|구 할에 달하는 식솔들이 유명을 달리했고, 사천당문의 경내 대부분이 파괴되었으니까.
 58|
 59|가문의 명맥을 보존했다는 것이 그나마 위안이었지만, 과거의 성세를 회복하기 위해서는 아주 오랜 시간이 필요할 터였다.
 60|
 61|“사천 무림의 동도들이 발 벗고 나서 도와주고는 있으나…… 앞으로의 일이 우려되는구려.”
 62|
 63|가주인 당사독이라면 어떤 상황에서도 약한 모습을 보이지 않았을 것이나, 당호룡은 달랐다.
 64|
 65|그의 솔직한 말에 사내는 긴 손가락으로 찻잔을 어루만졌다.
 66|
 67|“제가 이곳에 온 이유는 당 대협께서도 잘 아시리라 생각합니다.”
 68|
 69|“삼문혈사를 조사하기 위해 온 것으로 알고 있소만.”
 70|
 71|“정확히 말하자면, 처음 하남을 떠났을 때는 작고하신 독왕 당사독 대협과 경천신니를 시해한 흉수를 색출하기 위함이었습니다. 하지만 오는 길에 상황이 크게 바뀌었지요.”
 72|
 73|“맞소. 암천, 그 천인공노할 놈들이 마수를 드러냈소.”
 74|
 75|“비록 하남에서의 전례가 있기는 하나 이토록 대담하게, 그것도 천하에 명성이 자자한 세 곳의 명문 대파를 일거에 습격했다는 것은 전란이 코앞까지 들이닥쳤다는 증거입니다.”
 76|
 77|작은 혼란은 더 큰 혼란을 낳는다.
 78|
 79|그러나 암천의 존재는 이미 숨길 수 있는 수준의 것이 아니었고, 숨길 이유도 없었다.
 80|
 81|참혹했던 삼문혈사의 그날로부터 어언 칠 주야.
 82|
 83|지금쯤 발 없는 말은 천리를 달리고, 무수히 많은 전서구가 천하 각지로 날아가고 있을 것이다.
 84|
 85|그리고 혼란이 아닌 전란은, 결집을 낳았다.
 86|
 87|“소림혈사 직후 하남에서 정파 무림이 결집하고 있다 들었소. 그럼 혹시…….”
 88|
 89|“아직은 준비 과정일 뿐입니다. 하지만 기정사실이지요.”
 90|
 91|사내가 묵직한 음성으로 말을 이었다.
 92|
 93|“그런 연유로 드리는 말씀인데, 하남으로 가시는 것이 어떻겠습니까.”
 94|
 95|“하남이라.”
 96|
 97|“예. 곧 생각하시는 그 일이 일어날 겁니다.”
 98|
 99|짧은 침묵 끝에 당호룡이 입을 뗐다.
100|
101|“영광스러운 자리에 초청해 준 것은 감사하나, 지금은 내가 자리를 비울 수 없소. 그대도 알다시피 가주 대행으로서 본가의 식솔들을…….”
102|
103|“당 대협.”
104|
105|“말씀하시오.”
106|
107|“방금 말씀하신 것처럼 당 대협께서는 가주 대행이십니다. 당연히 당문의 식솔들을 놔두고 가실 수 없겠지요.”
108|
109|“……!”
110|
111|그제야 사내의 제안에 담긴 뜻을 알아차린 당호룡이 입을 벌렸다.
112|
113|그로서는 감히 생각도 해 본 적 없는 일이었다.
114|
115|“그러니까 지금…… 본가를 옮기라는 말이오?”
116|
117|“글쎄요.”
118|
119|사람의 속을 훤히 들여다보는 듯한 사내의 투명한 눈빛이 당호룡을 향했다.
120|
121|“매종학 대협께서 제게 그런 말씀을 하시더군요. 곧 정마대전보다 더 거대한 전란이 발발할 것이라고.”
122|
123|“검성께서…….”
124|
125|당호룡은 침음성을 삼켰다.
126|
127|저것은 비단 검성 한 사람만의 의견이 아닐 것이다.
128|
129|지난 소림혈사는 수많은 정파 무림인들의 분노와 경각심을 일깨웠고, 새로운 무림맹(武林盟)은 이미 태동의 준비를 끝마쳤다.
130|
131|정파 무림 전체가 곧 닥칠 전란에 대비하는 것이다.
132|
133|‘이런 상황에서 본가가 살아남을 수 있을까.’
134|
135|순간 뇌리를 스친 의문에 그의 가슴이 덜컥 내려앉았다.
136|
137|이미 사천당문은 가문 역사상 유례없는 타격을 입었다.
138|
139|더욱이 청성파와 아미파 역시 만만치 않은 전력을 잃은 상황.
140|
141|다시 한번 적들이 쳐들어온다면 막을 방법은 요원했다.
142|
143|“허어.”
144|
145|망연자실한 얼굴로 한숨을 내쉬는 당호룡의 귓가에 나직한 목소리가 닿았다.
146|
147|“당 대협께서는 사천당문이 지난 수백 년간 이어질 수 있었던 이유가 뭐라 생각하십니까.”
148|
149|“그것은.”
150|
151|“오직 당문(唐門)이었기 때문입니다. 앞의 두 글자를 떼어 낸다 한들 그 사실은 변하지 않습니다.”
152|
153|“……!”
154|
155|“결심하신다면, 정파 무림이 당문을 돕겠습니다.”
156|
157|말을 잇지 못하고 파르르 몸을 떨던 당호룡이 어렵게 입을 열었다.
158|
159|“우리는 지금껏 수많은 적을 만들었소. 구파일방과 오대세가에도 본가를 불편하게 생각하는 이들이 있지. 아무 문제 없겠소?”
160|
161|“모든 일은 공명정대(公明正大)하게 이루어질 터. 안심하시고 새로운 둥지를 트십시오. 하남, 섬서, 아니면…….”
162|
163|사내의 입가에 부드러운 웃음이 맺혔다.
164|
165|“산서도 좋겠군요.”
166|
167|“산서?”
168|
169|“제게 말씀만 하십시오. 남는 땅 많습니다.”
170|
171|당호룡은 문득 잊고 있던 사실 한 가지를 떠올렸다.
172|
173|바로 눈앞의 사내가 산서 무림을 일통한 맹주이며, 산서성 제일의 지주이자 대부호라는 사실을.
174|
175|“고맙소. 정말 고맙소, 진 대협!”
176|
177|“별말씀을.”
178|
179|사내, 태원진가의 소가주 진위경이 공손하게, 그러나 위엄 있는 태도로 사천당문 가주 대행의 포권에 답한 그 순간이었다.
180|
181|덜컥.
182|
183|“저기, 부르셨다고 들었는데요.”
184|
185|전각의 문틈 사이로 빼꼼 고개를 내민 한 청년을 발견한 진위경이 사자후를 내질렀다.
186|
187|“막내야아-!”
188|
189|두두두두두, 퍼억!
190|
191|흡사 성난 황소와도 같은 돌진이었다.
192|
193|포옹인지 격돌인지 모를 두 형제의 상봉을 목격한 당호룡은 진위경에 관한 소문 중 하나를 떠올렸다.
194|
195|‘아우들이라면 껌뻑 죽는다더니.’
196|
197|산서 무림을 일통한 맹주이자 산서성 제일의 지주는 온데간데없고, 웬 팔불출 하나만 남아 있었다.
198|
199|‘역시 아직 나이가 젊다 보니 연륜이 부족해. 언제 어디서나 냉철하신 종형에 비할 바가 아니지. 암, 그렇고말고.’
200|
201|미미쨩의 존재를 알 리 없는 당호룡이었다.
202|
203|
204|
205|* * *
206|
207|
208|
209|“막내야아!”
210|
211|축축한 눈물을 흩뿌리며 돌진한 진위경이 나를 덥석 끌어안았다.
212|
213|이래 봬도 무림 짬밥 2년. 지금까지 지긋지긋하게 당한 일이라 이 정도 반응은 충분히 예상했다.
214|
215|콰드득!
216|
217|……그런데 이걸 예상 못 했네.
218|
219|아니, 이게 뭐라고 뼈 어긋나는 소리가 들리냐. 나는 아마존 밀림의 아나콘다처럼 전신을 꽉꽉 조여 오는 포옹에 한숨을 내쉬었다.
220|
221|어쨌거나 반가운 마음에 순순히 안겨 주긴 했는데, 반응이 역대 최고로 격렬했다.
222|
223|“잠깐, 형님. 이것 좀 놓고 얘기합시다, 놓고.”
224|
225|“형님이라니! 그런 딱딱한 호칭 말고 편하게 형이라고 부르라 하지 않았더냐! 변했구나, 변했어!”
226|
227|“아, 알겠으니까 이제 좀 놔 봐요.”
228|
229|“어릴 때는 반말하더니 존댓말은 왜 쓰는 것이냐! 변했구나, 변했어!”
230|
231|“놔, 시벌.”
232|
233|“헉, 아무리 삐뚤어졌을 때도 욕은 안 했는데! 변했구……!”
234|
235|“와, 추임새 돌겠네.”
236|
237|혹시 본업이 무림인이고 부업이 디멘터신가.
238|
239|영혼이 빨려 나가는 듯한 기분에 진저리를 치며 손을 뻗었다.
240|
241|휘릭, 쿵!
242|
243|진위경의 거구가 거꾸로 땅에 처박히자 육중한 소리가 울려 퍼졌다.
244|
245|지켜보던 사천당문의 장년 사내가 헉, 하고 신음을 흘렸다.
246|
247|“괜찮습니다, 괜찮아요. 이거 그냥 저희끼리 노는 거예요.”
248|
249|“아, 아니 그래도…….”
250|
251|“보세요. 멀쩡히 일어나잖아요.”
252|
253|내 말처럼 아무렇지 않게 벌떡 일어난 진위경은 감격의 눈물을 글썽이고 있었다.
254|
255|“그사이 더 강해졌구나. 역시 우리 막내다.”
256|
257|그 변함없는 모습에 나는 피식 실소를 흘렸다.
258|
259|“참, 여전하네요.”
260|
261|“여전하기는. 지난 두 달 동안 얼마나 걱정을 했는지 아느냐? 밤에 잠도 못 이루고 입맛도 없어서 피골이 상접했다.”
262|
263|나는 우람한 근육질의 덩치를 보며 중얼거렸다.
264|
265|“피골이 풍족해 보이는데.”
266|
267|그나저나 두 달이라, 벌써 그렇게 시간이 흘렀구나.
268|
269|나는 새삼 돌아갈 때가 임박했음을 깨달았다.
270|
271|어느 한쪽의 세상에 열흘을 머무른다 쳤을 때 다른 한쪽에서는 한 시간 남짓이 소모되는 걸 감안한다면…….
272|
273|‘얼추 여섯 시간 정도가 흘렀군. 슬슬 비행기가 착륙할지도 모르겠어.’
274|
275|때마침 잘됐다. 서천마군이라는 큰 산을 넘으며 피로가 쌓인 차였으니까.
276|
277|나는 말 길게 할 것 없이 대뜸 본론을 들이밀었다.
278|
279|“언제 출발합니까?”
280|
281|“우리 막내, 얼마나 고초가 컸을…… 응?”
282|
283|안절부절못하며 내 몸을 살피던 진위경이 멈칫했다.
284|
285|“지금 뭐라고?”
286|
287|“저 데려가려고 오신 거잖아요. 아, 삼괴도.”
288|
289|진위경의 눈이 휘둥그레졌다.
290|
291|“그걸 네가 어떻게?”
292|
293|사천당문의 중요 인물로 보이는 장년 사내도 놀란 얼굴로 입을 열었다.
294|
295|“진 대협. 일의 전말에 대해 조사하러 오신 것이 아니었소?”
296|
297|“맞습니다만, 조사단 중 저를 포함한 몇몇은 다시 하남으로 복귀할 겁니다. 사천에 도착하기 직전, 삼문혈사를 일으킨 주범 중 하나인 삼괴를 호송하라는 임무를 받았습니다.”
298|
299|“그럼 본가에 관한 이야기는…….”
300|
301|“물론 유효합니다. 단, 지금 당장은 당문으로서도 힘들겠지요.”
302|
303|“그렇소. 가주께서도 아직 먼 거리를 이동할 수 없는 상황이니 말이오. 다른 식솔들에게도 동의를 구해야 하고.”
304|
305|“예. 그리고…….”
306|
307|잠시 장년인과 두런두런 이야기를 나누던 진위경이 내게 은밀히 전음을 날려 보냈다.
308|
309|- 한데, 어찌 알고 있었더냐?
310|
311|- 척 하면 착이죠. 그냥 정황상 이럴 것 같았어요.
312|
313|- 아아, 우리 막내. 얼마나 큰 고비를 넘겼길래 머리까지 좋아졌단 말이냐!
314|
315|- …….
316|
317|뭔가 기분 나쁘네.
318|
319|사실 정황상 알아차린 것도 아니다. 삼괴 호송 관련한 퀘스트가 떠서 안 거지.
320|
321|“그래서 언제 출발합니까?”
322|
323|내 물음에 막 대화를 끝마친 진위경이 입을 열었다.
324|
325|“알고 있었다니 이야기가 쉽겠구나. 빠르면 빠를수록 좋다. 준비는 되었느냐?”
326|
327|“어차피 가져온 거라고는 불알 두 짝밖에 없는데요. 몸만 가면 됩니다.”
328|
329|거기에 더해 붕대를 칭칭 감은 짐 덩이 둘까지.
330|
331|고개를 끄덕인 진위경이 입을 열었다.
332|
333|“당 대협. 삼괴는 어디 있습니까?”
334|
335|당 대협이라 불린 장년 사내가 대답했다.
336|
337|“사지를 결박하고 철저한 감시 속에 가둬 두었소. 불알을 터트린 후로 틈만 나면 자결하려고 하니 주의해야 할 거요.”
338|
339|“……저런.”
340|
341|저건 나 같아도 죽고 싶을 것 같은데.
342|
343|어찌 되었건 신속하게 움직일 수 있는 여건은 갖춰졌다.
344|
345|잠시 무언가를 생각하던 진위경이 시원하게 대답했다.
346|
347|“그렇다면 반 시진. 반 시진 안에 출발하는 것으로 하지. 괜찮으냐?”
348|
349|“문제없습니다.”
350|
351|망설임 없이 대답한 그 순간, 전각 밖에서 다급한 인기척과 함께 누군가의 외침이 들렸다.
352|
353|“가주께서! 가주님께서 깨어나셨습니다!”
354|
355|진위경이 미지근한 목소리로 말을 정정했다.
356|
357|“한 시진. 한 시진으로 하자.”
358|
359|“……예. 그게 좋겠네요.”
360|
361|아깝다. 만독지환 먹튀 할 수 있었는데.
```

## Assembled English

```markdown
[P1]
# Chapter 374

[P2]
Tang Horyong, the Pavilion Master of the Poison Dragon Pavilion, rose from his seat to greet his guest.

[P3]
An imposing man had just opened the door and entered, and an indescribable pressure poured from him.

[P4]
“You’ve gone to a great deal of trouble coming such a long way.”

[P5]
“Compared to what the Sichuan Tang Clan has endured, it was nothing. Once again, please accept my deepest condolences.”

[P6]
Despite his rugged features, the man’s voice was low and gentle, yet it carried a force that compelled anyone listening to pay attention.

[P7]
*Could it be the aura possessed only by a leader who commands others?*

[P8]
At the man’s gentle yet deeply composed gaze, Tang Horyong suddenly thought of someone.

[P9]
*It feels as though I’m facing another version of my older cousin.*

[P10]
The realization left Tang Horyong more than a little bewildered.

[P11]
From what he had heard, the man before him was not even forty yet.

[P12]
His older cousin, on the other hand, was considerably older and held an eminent position in Murim.

[P13]
He had achieved countless military feats during the Great Faction War and was also an iron-blooded Family Head who had rebuilt his ruined family on an even stronger foundation.

[P14]
The Myriad-Poison Asura, Tang Sadok.

[P15]
Tang Horyong, acting Family Head of the Sichuan Tang Clan, sighed inwardly as he thought of his older cousin, who had yet to regain consciousness.

[P16]
*Please wake up soon and lead us, Family Head.*

[P17]
Tang Horyong was a martial artist to his very bones.

[P18]
He prided himself on having attained mastery in poisons and hidden weapons, but leading a family was an entirely different matter.

[P19]
Especially lately, problems had come pouring in from every direction, leaving him no time even to dwell on the grief and anger of losing his own kin.

[P20]
*If only a man like this were in my position.*

[P21]
In that sense, Tang Horyong could not help but envy the man before him.

[P22]
It was not a judgment based solely on first impressions. He had already heard plenty of rumors about the man.

[P23]
Even if only a quarter of them were true, the man was more than capable of leading a family.

[P24]
“Sir Tang, is there something on my face?”

[P25]
“Ah, no. I was distracted by everything going on and acted rudely. My apologies.”

[P26]
At Tang Horyong’s hurried apology, the man nodded gravely.

[P27]
“Not at all. It’s understandable. You’ve suffered something truly devastating.”

[P28]
In truth, even the word *devastating* was insufficient to describe the damage the Sichuan Tang Clan had suffered.

[P29]
Nearly nine-tenths of its household members had died, and most of the Tang Clan’s grounds had been destroyed.

[P30]
The fact that the family line had survived was their one consolation, but it would take a very long time to restore the prosperity they had once enjoyed.

[P31]
“Our fellow martial artists in Sichuan have gone out of their way to help us, but… I fear for what lies ahead.”

[P32]
If the Family Head, Tang Sadok, had been in his place, he would never have shown weakness in any situation.

[P33]
Tang Horyong was different.

[P34]
At his frank words, the man gently stroked his teacup with his long fingers.

[P35]
“I believe you know very well why I came here, Sir Tang.”

[P36]
“I understand that you came to investigate the Three-Sect Bloodbath.”

[P37]
“To be precise, when I first left Henan, my purpose was to track down the murderers who killed the late Poison King Tang Sadok and the Heaven-Shaking Divine Nun. But the situation changed considerably along the way.”

[P38]
“That’s right. Dark Heaven—that bunch of accursed bastards—has finally revealed its claws.”

[P39]
“Although there was a precedent in Henan, attacking three prestigious great sects renowned throughout the land so boldly and all at once is proof that the war has reached our doorstep.”

[P40]
Small unrest begets greater unrest.

[P41]
But Dark Heaven’s existence could no longer be concealed, and there was no reason to conceal it.

[P42]
Seven days and nights had already passed since the horrific day of the Three-Sect Bloodbath.

[P43]
By now, word of it would have traveled a thousand li, and countless carrier pigeons would be flying to every corner of the land.

[P44]
And war, unlike mere chaos, brought people together.

[P45]
“I heard that the orthodox Murim is rallying in Henan in the immediate aftermath of the Shaolin Bloodbath. Then, perhaps…”

[P46]
“It is still only in the preparation stage. But it is a foregone conclusion.”

[P47]
The man continued in a heavy voice.

[P48]
“That is why I’m making this suggestion. Why don’t you go to Henan?”

[P49]
“Henan…”

[P50]
“Yes. What you’re thinking of will happen soon.”

[P51]
After a brief silence, Tang Horyong spoke.

[P52]
“Thank you for inviting me to such an honored occasion, but I cannot leave right now. As you know, as the acting Family Head, the members of our family…”

[P53]
“Sir Tang.”

[P54]
“Please, speak.”

[P55]
“As you just said, Sir Tang, you are the acting Family Head. Naturally, you cannot leave the members of the Tang Clan behind and go.”

[P56]
“…!”

[P57]
Only then did Tang Horyong grasp the meaning behind the man’s proposal. His mouth fell open.

[P58]
It was something he had never dared even consider.

[P59]
“So, are you saying… that we should relocate our family?”

[P60]
“Well…”

[P61]
The man’s clear eyes, seeming to see straight through him, turned toward Tang Horyong.

[P62]
“Great Hero Mae Jonghak once told me that a war even greater than the Great Faction War would soon erupt.”

[P63]
“The Sword Saint…”

[P64]
Tang Horyong swallowed a groan.

[P65]
That could not be the Sword Saint’s opinion alone.

[P66]
The Shaolin Bloodbath had awakened the anger and vigilance of countless orthodox martial artists, and the new Murim Alliance had already finished preparing to take shape.

[P67]
The entire orthodox Murim was preparing for the coming war.

[P68]
*Can our family survive under these circumstances?*

[P69]
The question flashed through his mind, and his heart sank.

[P70]
The Sichuan Tang Clan had already suffered a blow unprecedented in its history.

[P71]
Moreover, the Qingcheng Sect and Emei Sect had lost considerable strength as well.

[P72]
If the enemy invaded once again, there would be little hope of stopping them.

[P73]
“Haah…”

[P74]
As Tang Horyong sighed with a vacant expression, a quiet voice reached his ears.

[P75]
“Sir Tang, why do you think the Sichuan Tang Clan has endured for hundreds of years?”

[P76]
“That is…”

[P77]
“It was solely because it was the Tang Clan. Even if you took away the ‘Sichuan’ from its name, that fact would not change.”

[P78]
“…!”

[P79]
“If you make up your mind, the orthodox Murim will help the Tang Clan.”

[P80]
Tang Horyong trembled, unable to continue speaking. At last, he forced out the words.

[P81]
“We have made countless enemies over the years. Even among the Nine Sects and One Gang and the Five Great Families, there are those who find our family troublesome. Will that really be all right?”

[P82]
“Everything will be handled fairly and aboveboard. Set your mind at ease and establish a new nest. Henan, Shaanxi, or perhaps…”

[P83]
A gentle smile touched the man’s lips.

[P84]
“Shanxi would work too.”

[P85]
“Shanxi?”

[P86]
“Just say the word. I have plenty of land to spare.”

[P87]
Tang Horyong suddenly remembered one fact he had forgotten.

[P88]
The man standing before him was the leader who had unified the Murim of Shanxi, the foremost landowner in Shanxi Province, and a great tycoon.

[P89]
“Thank you. Truly, thank you, Sir Jin!”

[P90]
“Think nothing of it.”

[P91]
The man—Jin Wikyung, Lesser Family Head of the Jin Family of Taiyuan—was respectfully yet majestically returning the acting Family Head of the Sichuan Tang Clan’s fist-and-palm salute when—

[P92]
Clunk.

[P93]
“Um, I heard you called for me.”

[P94]
A young man cautiously poked his head through the gap in the pavilion door.

[P95]
The instant Jin Wikyung spotted him, he unleashed a lion’s roar.

[P96]
“Youngest—!”

[P97]
Thud-thud-thud-thud—wham!

[P98]
He charged like an enraged bull.

[P99]
Watching the two brothers reunite in what might have been an embrace or a collision, Tang Horyong recalled one of the rumors about Jin Wikyung.

[P100]
*They say he’s a complete pushover when it comes to his younger brothers.*

[P101]
The leader who had unified the Murim of Shanxi and the foremost landowner in Shanxi Province was nowhere to be seen.

[P102]
All that remained was some hopelessly doting fool.

[P103]
*He is still young, after all. He lacks experience. He cannot compare to my older cousin, who is so cool-headed at all times. Of course. Absolutely.*

[P104]
Tang Horyong had no way of knowing that Mimi-chan existed.

[P105]
* * *

[P106]
“Youngest!”

[P107]
Jin Wikyung charged at me, scattering tears from his damp eyes, and grabbed me in a tight embrace.

[P108]
I had two years of Murim experience under my belt. After enduring this sort of thing time and again, I’d expected a reaction this dramatic.

[P109]
Crack!

[P110]
…But I hadn’t expected this.

[P111]
What the hell was that? Why could I hear my bones going out of alignment?

[P112]
I sighed as his embrace tightened around my entire body like an anaconda from the Amazon jungle.

[P113]
In any case, I let him hug me because I was glad to see him. But his reaction was more violent than ever before.

[P114]
“Hold on, hyungnim. Let go so we can talk. Let go.”

[P115]
“Hyungnim?! Didn’t I tell you to call me hyung instead of using such a stiff formality? You’ve changed, you’ve changed!”

[P116]
“Ah, fine, I get it. Now let me go.”

[P117]
“You used to speak informally when you were little, so why are you using polite speech now? You’ve changed, you’ve changed!”

[P118]
“Let go, fuck.”

[P119]
“Gasp! Even during your rebellious phase, you never swore! You’ve chang—!”

[P120]
“Wow. That running commentary is driving me insane.”

[P121]
*Is his day job a Murim martial artist and his side job a Dementor?*

[P122]
Feeling as though my soul were being sucked out, I shuddered in revulsion and reached out.

[P123]
Whirl—crash!

[P124]
Jin Wikyung’s huge body slammed headfirst into the ground, upside down, and a heavy impact rang out.

[P125]
A middle-aged man from the Sichuan Tang Clan who had been watching let out a startled groan.

[P126]
“It’s okay, it’s okay. We’re just playing around.”

[P127]
“Ah, but still…”

[P128]
“Look. He’s getting up just fine.”

[P129]
Just as I’d said, Jin Wikyung sprang to his feet as though nothing had happened, tears of emotion glimmering in his eyes.

[P130]
“You’ve gotten even stronger in the meantime. That’s our youngest.”

[P131]
His complete lack of change made me snort.

[P132]
“You’re still the same.”

[P133]
“Still the same? Do you know how worried I’ve been these past two months? I couldn’t sleep at night, and I had no appetite. I was reduced to skin and bones.”

[P134]
I looked over his massive, muscular frame and muttered, “Your bones look pretty well padded.”

[P135]
In any case, two months.

[P136]
So much time had already passed.

[P137]
It struck me anew that it was almost time to return.

[P138]
Given that spending ten days in one world meant only about an hour passed in the other…

[P139]
*About six hours must have passed. The plane might be landing soon.*

[P140]
The timing was perfect. I had accumulated quite a bit of fatigue after overcoming the massive obstacle that was the Western Heaven Demon Lord.

[P141]
Rather than drag out the conversation, I got straight to the point.

[P142]
“When are we leaving?”

[P143]
“Our youngest, you must have suffered so much… Hm?”

[P144]
Jin Wikyung, who had been anxiously looking me over, froze.

[P145]
“What did you say?”

[P146]
“You came to take me with you, didn’t you? Oh, and Samgoe too.”

[P147]
Jin Wikyung’s eyes widened.

[P148]
“How did you know that?”

[P149]
The middle-aged man, who appeared to be an important figure in the Sichuan Tang Clan, also spoke with a startled expression.

[P150]
“Sir Jin, did you not come to investigate the full circumstances of the incident?”

[P151]
“I did. However, several members of the investigative party, myself included, will be returning to Henan. Just before we reached Sichuan, I received a mission to escort Samgoe, one of the principal culprits behind the Three-Sect Bloodbath.”

[P152]
“Then what about the matter concerning our family…”

[P153]
“It still stands, of course. It would simply be difficult for the Tang Clan to act on it immediately.”

[P154]
“That’s true. The Family Head is still unable to travel a long distance. We must also seek the consent of the other members of the family.”

[P155]
“Yes. And…”

[P156]
After quietly conversing with the middle-aged man for a moment, Jin Wikyung sent me a discreet Sound Transmission.

[P157]
*But how did you know?*

[P158]
*I can take a hint. It just seemed likely from the circumstances.*

[P159]
*Ah, our youngest. What enormous ordeal did you have to overcome to make you clever, too?*

[P160]
*…*

[P161]
*That somehow rubs me the wrong way.*

[P162]
In truth, I hadn’t figured it out from the circumstances. I knew because a Quest related to escorting Samgoe had popped up.

[P163]
“So when are we leaving?”

[P164]
Having just finished his conversation, Jin Wikyung answered me.

[P165]
“You already knew? That makes things easier. The sooner, the better. Are you ready?”

[P166]
“The only things I brought with me are my two balls. I just need to bring my body.”

[P167]
On top of that, I had two bundles of luggage wrapped tightly in bandages.

[P168]
Jin Wikyung nodded.

[P169]
“Sir Tang, where is Samgoe?”

[P170]
The middle-aged man he had addressed as Sir Tang replied, “We bound all four of his limbs and imprisoned him under strict guard. Ever since his balls were crushed, he has tried to kill himself whenever he gets the chance. You’ll need to be careful.”

[P171]
“Oh dear…”

[P172]
*Even I would want to die if I were him.*

[P173]
In any case, everything was in place for a swift departure.

[P174]
Jin Wikyung considered it for a moment, then gave a decisive answer.

[P175]
“Then half a shichen.[^1] We’ll leave within half a shichen. Is that all right?”

[P176]
“No problem.”

[P177]
The moment I answered without hesitation, hurried footsteps sounded outside the pavilion, followed by someone shouting.

[P178]
“The Family Head! The Family Head has awakened!”

[P179]
Jin Wikyung corrected himself in a lukewarm voice.

[P180]
“One shichen. Let’s make it one shichen.”

[P181]
“…Yes. That sounds better.”

[P182]
What a shame. I could’ve taken the Myriad Poison Ring and bolted.

[P183]
[^1]: A shichen is a traditional two-hour period.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 374

[P2]
Tang Horyong, the Pavilion Master of the Poison Dragon Pavilion, rose from his seat to greet his guest.

[P3]
An imposing man had just opened the door and entered, and an indescribable aura poured from him.

[P4]
“You’ve gone to a great deal of trouble coming such a long way.”

[P5]
“Compared to what the Sichuan Tang Clan has endured, it was nothing. Once again, please accept my deepest condolences.”

[P6]
Despite his rough features, the man’s voice was low and gentle. At the same time, it possessed a force that made anyone who heard it pay close attention.

[P7]
*Could it be the aura possessed only by a leader who commands others?*

[P8]
At the man’s gentle yet deeply composed gaze, Tang Horyong suddenly thought of someone.

[P9]
*This feels like meeting another older cousin.*

[P10]
The realization left Tang Horyong more than a little bewildered.

[P11]
He had heard that the man standing before him was still a young man who had yet to reach forty.

[P12]
His older cousin, on the other hand, was considerably older and held an eminent position in Murim.

[P13]
He had achieved countless military feats during the Great Faction War and was also an iron-blooded Family Head who had rebuilt his ruined family on an even stronger foundation.

[P14]
The Myriad-Poison Asura, Tang Sadok.

[P15]
Tang Horyong, acting Family Head of the Sichuan Tang Clan, let out a silent sigh as he thought of his older cousin, who still had not regained consciousness.

[P16]
*Please wake up soon and lead us, Family Head.*

[P17]
Tang Horyong had been born a martial artist.

[P18]
He prided himself on having made himself an authority in poisons and hidden weapons, but leading a family was an entirely different matter.

[P19]
Especially lately, so many issues had been pouring in from every direction that he had not even had time to dwell on the grief and anger of losing his family members.

[P20]
*If only someone like this man were in my position.*

[P21]
In that sense, Tang Horyong could not help but envy the man before him.

[P22]
He was not judging him solely by his first impression. He had already heard plenty of rumors about the man.

[P23]
Even if only a quarter of those rumors were true, the man clearly possessed the ability to lead a family.

[P24]
“Sir Tang, is there something on my face?”

[P25]
“Ah, no. I was distracted by everything going on and acted rudely. My apologies.”

[P26]
At Tang Horyong’s hurried apology, the man nodded with a serious expression.

[P27]
“Not at all. It’s understandable. You’ve suffered something truly devastating.”

[P28]
In truth, even the word *devastating* was insufficient to describe the damage the Sichuan Tang Clan had suffered.

[P29]
Nearly nine-tenths of its household members had died, and most of the Tang Clan’s grounds had been destroyed.

[P30]
The fact that the family line had survived was their one consolation, but it would take an extremely long time to restore the glory they had once enjoyed.

[P31]
“The fellow martial artists of Sichuan have stepped forward to help, but… I’m worried about what lies ahead.”

[P32]
If the Family Head, Tang Sadok, had been in his place, he would never have shown weakness in any situation.

[P33]
Tang Horyong was different.

[P34]
At his frank words, the man gently stroked his teacup with his long fingers.

[P35]
“I believe you know very well why I came here, Sir Tang.”

[P36]
“I understand that you came to investigate the Three-Sect Bloodbath.”

[P37]
“To be precise, when I first left Henan, my purpose was to find the murderers who killed the late Poison King Tang Sadok and the Heaven-Shaking Divine Nun. But the situation changed considerably along the way.”

[P38]
“That’s right. Dark Heaven—that bunch of inhuman bastards—has finally revealed its claws.”

[P39]
“Although there was a precedent in Henan, attacking three prestigious great sects renowned throughout the land so boldly and all at once is proof that the war has reached our doorstep.”

[P40]
Small unrest begets greater unrest.

[P41]
But Dark Heaven’s existence was no longer something that could be concealed, nor was there any reason to conceal it.

[P42]
Seven days and nights had already passed since the horrific day of the Three-Sect Bloodbath.

[P43]
By now, word of it would have traveled a thousand li, and countless carrier pigeons would be flying to every corner of the land.

[P44]
And unlike mere chaos, war brought people together.

[P45]
“I heard that the orthodox Murim is rallying in Henan in the immediate aftermath of the Shaolin Bloodbath. Then, perhaps…”

[P46]
“It is still only in the preparation stage. But it is a foregone conclusion.”

[P47]
The man continued in a heavy voice.

[P48]
“That is why I’m making this suggestion. Why don’t you go to Henan?”

[P49]
“Henan.”

[P50]
“Yes. The thing you’re thinking of will happen soon.”

[P51]
After a brief silence, Tang Horyong spoke.

[P52]
“Thank you for inviting me to such an honored occasion, but I cannot leave right now. As you know, as the acting Family Head, I must remain here for the members of my family…”

[P53]
“Sir Tang.”

[P54]
“Please, speak.”

[P55]
“As you just said, Sir Tang, you are the acting Family Head. Naturally, you cannot leave the members of the Tang Clan behind and go.”

[P56]
“...!”

[P57]
Only then did Tang Horyong understand what lay behind the man’s proposal. His mouth fell open.

[P58]
It was something he had never dared even consider.

[P59]
“So, are you saying that we should relocate our family headquarters?”

[P60]
“Well.”

[P61]
The man’s clear eyes, seeming to see straight through him, turned toward Tang Horyong.

[P62]
“Sword Saint Mae Jonghak said something to me. He said that a war even greater than the Great Faction War would soon break out.”

[P63]
“The Sword Saint…”

[P64]
Tang Horyong swallowed a groan.

[P65]
That could not be the opinion of the Sword Saint alone.

[P66]
The Shaolin Bloodbath had awakened the anger and vigilance of countless orthodox martial artists, and the new Murim Alliance had already finished preparing to take shape.

[P67]
The entire orthodox Murim was preparing for the war that would soon arrive.

[P68]
*Can our family survive in a situation like this?*

[P69]
The question flashed through his mind, and his heart dropped.

[P70]
The Sichuan Tang Clan had already suffered a blow without precedent in the history of the family.

[P71]
Moreover, the Qingcheng Sect and Emei Sect had lost considerable strength as well.

[P72]
If the enemy invaded once again, there would be little hope of stopping them.

[P73]
“Haah.”

[P74]
As Tang Horyong sighed with a vacant expression, a quiet voice reached his ears.

[P75]
“Sir Tang, why do you think the Sichuan Tang Clan has managed to continue for the past several hundred years?”

[P76]
“That is…”

[P77]
“It was solely because it was the Tang Clan. Even if you took away the ‘Sichuan’ from its name, that fact would not change.”

[P78]
“...!”

[P79]
“If you make up your mind, the orthodox Murim will help the Tang Clan.”

[P80]
Tang Horyong trembled, unable to continue speaking. At last, he forced his mouth open.

[P81]
“We have made countless enemies over the years. There are people among the Nine Sects and One Gang and the Five Great Families who find our family troublesome. Will that really be all right?”

[P82]
“Everything will be handled fairly and aboveboard. Set your mind at ease and establish a new nest. Henan, Shaanxi, or perhaps…”

[P83]
A gentle smile appeared around the man’s lips.

[P84]
“Shanxi would work too.”

[P85]
“Shanxi?”

[P86]
“Just say the word. There is plenty of land available.”

[P87]
Tang Horyong suddenly remembered one fact he had forgotten.

[P88]
The man standing before him was the leader who had unified the Murim of Shanxi, the foremost landowner in Shanxi Province, and a great tycoon.

[P89]
“Thank you. Truly, thank you, Sir Jin!”

[P90]
“Think nothing of it.”

[P91]
At that moment, the man—Jin Wikyung, the Lesser Family Head of the Jin Family of Taiyuan—respectfully but majestically returned the acting Family Head of the Sichuan Tang Clan’s fist-and-palm salute.

[P92]
Clunk.

[P93]
“I heard you called for me.”

[P94]
When Jin Wikyung spotted a young man cautiously poking his head through the gap in the pavilion door, he let out a lion’s roar.

[P95]
“Youngest—!”

[P96]
Thud-thud-thud-thud—wham!

[P97]
It was a charge like that of an enraged bull.

[P98]
As Tang Horyong watched the brothers reunite in an embrace—or perhaps a collision—he remembered one of the rumors about Jin Wikyung.

[P99]
*They say he’s a complete pushover when it comes to his younger brothers.*

[P100]
The leader who had unified the Murim of Shanxi and the foremost landowner in Shanxi Province was nowhere to be seen.

[P101]
All that remained was some hopelessly doting fool.

[P102]
*He is still young, after all. He lacks experience. He cannot compare to my older cousin, who is so cool-headed at all times. Of course. Absolutely.*

[P103]
Tang Horyong had no idea that Mimi-chan existed.

[P104]
* * *

[P105]
“Youngest!”

[P106]
Jin Wikyung charged at me, scattering tears from his damp eyes, and grabbed me in a tight embrace.

[P107]
I had been in Murim for two years, so I had plenty of experience with this sort of thing. I had suffered through it so many times that I could easily predict a reaction like this.

[P108]
Crack!

[P109]
…But I hadn’t expected this.

[P110]
What the hell was that? Why could I hear my bones going out of alignment?

[P111]
I sighed as his embrace tightened around my entire body like an anaconda from the Amazon jungle.

[P112]
In any case, I let him hug me because I was glad to see him. But his reaction was more violent than ever before.

[P113]
“Hold on, hyung. Let’s talk after you let go. Let go.”

[P114]
“Hyungnim?! Didn’t I tell you to call me hyung instead of using such a stiff formality? You’ve changed, you’ve changed!”

[P115]
“Ah, fine, I get it. Now let me go.”

[P116]
“You used to speak informally when you were little, so why are you using polite speech now? You’ve changed, you’ve changed!”

[P117]
“Let go, fuck.”

[P118]
“Gasp! You never swore, even when you were going through your rebellious phase! You’ve changed—!”

[P119]
“Wow, your running commentary is killing me.”

[P120]
*Is his day job a Murim martial artist and his side job a Dementor?*

[P121]
Feeling as though my soul were being sucked out, I shuddered in revulsion and reached out.

[P122]
Whirl—crash!

[P123]
Jin Wikyung’s huge body slammed headfirst into the ground, upside down, and a heavy impact rang out.

[P124]
A middle-aged man from the Sichuan Tang Clan who had been watching let out a startled groan.

[P125]
“It’s okay, it’s okay. We’re just playing around.”

[P126]
“Ah, but still…”

[P127]
“Look. He’s getting up just fine.”

[P128]
Just as I said, Jin Wikyung sprang to his feet as though nothing had happened. Tears of emotion glimmered in his eyes.

[P129]
“You’ve gotten even stronger in the meantime. That’s our youngest.”

[P130]
At his unchanged behavior, I let out a snort of amusement.

[P131]
“You’re still the same.”

[P132]
“Still the same? Do you know how worried I’ve been these past two months? I couldn’t sleep at night, and I had no appetite. I was reduced to skin and bones.”

[P133]
I looked at his enormous, muscular body and muttered, “You look pretty well-fleshed-out to me.”

[P134]
In any case, two months.

[P135]
So much time had already passed.

[P136]
I realized anew that it was almost time for me to return.

[P137]
If ten days spent in one world amounted to roughly an hour passing in the other…

[P138]
*About six hours must have passed. The plane might be landing soon.*

[P139]
The timing was perfect. I had accumulated quite a bit of fatigue after overcoming the massive obstacle that was the Western Heaven Demon Lord.

[P140]
Without wasting time on a long conversation, I got straight to the point.

[P141]
“When are we leaving?”

[P142]
“Our youngest. You must have suffered so much… Hm?”

[P143]
Jin Wikyung, who had been anxiously examining me, suddenly stopped.

[P144]
“What did you say?”

[P145]
“You came to take me with you, didn’t you? Oh, and Samgoe too.”

[P146]
Jin Wikyung’s eyes widened.

[P147]
“How did you know that?”

[P148]
The middle-aged man, who appeared to be an important figure in the Sichuan Tang Clan, also spoke with a startled expression.

[P149]
“Sir Jin, did you not come to investigate the full circumstances of the incident?”

[P150]
“I did. However, some of us, including me, will be returning to Henan. Just before we reached Sichuan, I received a mission to escort Samgoe, one of the principal culprits behind the Three-Sect Bloodbath.”

[P151]
“Then what about the matter concerning our family…”

[P152]
“Of course, that still stands. It would simply be difficult for the Tang Clan to do so right now.”

[P153]
“That’s true. The Family Head is still unable to travel a long distance. We must also seek the consent of the other members of the family.”

[P154]
“Yes. And…”

[P155]
After quietly speaking with the middle-aged man for a while, Jin Wikyung sent me a discreet Sound Transmission.

[P156]
*But how did you know?*

[P157]
*You hint, I catch on. It just seemed likely from the circumstances.*

[P158]
*Ah, our youngest. What enormous ordeal did you have to overcome to make you clever, too?*

[P159]
*…*

[P160]
*That somehow rubs me the wrong way.*

[P161]
In truth, I hadn’t figured it out from the circumstances. I knew because a Quest related to escorting Samgoe had popped up.

[P162]
“So when are we leaving?”

[P163]
Jin Wikyung had just finished his conversation and answered my question.

[P164]
“You already knew? That makes things easier. The sooner, the better. Are you ready?”

[P165]
“The only things I brought with me are my two balls. I just need to bring my body.”

[P166]
On top of that, I had two bundles of luggage wrapped tightly in bandages.

[P167]
Jin Wikyung nodded and spoke.

[P168]
“Sir Tang, where is Samgoe?”

[P169]
The middle-aged man addressed as Sir Tang answered.

[P170]
“He is being held with all four limbs bound and under strict guard. Ever since his balls were crushed, he has been trying to kill himself whenever he gets the chance, so you will need to be careful.”

[P171]
“Oh dear.”

[P172]
*Even I would want to die if I were him.*

[P173]
In any case, everything was in place for a swift departure.

[P174]
After thinking for a moment, Jin Wikyung gave a brisk answer.

[P175]
“Then half a shichen.[^1] We’ll leave within half a shichen. Is that all right?”

[P176]
“No problem.”

[P177]
The moment I answered without hesitation, a frantic commotion arose outside the pavilion, followed by someone shouting.

[P178]
“The Family Head! The Family Head has awakened!”

[P179]
Jin Wikyung corrected himself in a lukewarm voice.

[P180]
“One shichen. Let’s make it one shichen.”

[P181]
“…Yes. That sounds better.”

[P182]
What a shame. I could’ve taken the Myriad Poison Ring and bolted.

[P183]
[^1]: A shichen is a traditional two-hour period.
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 374,
  "passed": true,
  "metrics": {
    "source_characters": 6032,
    "translation_characters": 13615,
    "length_ratio": 2.257,
    "source_paragraphs": 178,
    "translation_paragraphs": 183
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
        "korean": "명성",
        "preferred": "Fame"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "청해",
        "preferred": "Qinghai"
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

## Chapter 374 Expedition

- This branch intentionally starts at Chapter 374. Chapters 65–370 have no accepted local English translation here; Chapters 371–373 are source-only bridge summaries.
- Treat `docs/EXPEDITION_SEED.md` and `summaries/0369-0373.md` as bounded orientation, not as a substitute for missing translations.
- When the current Korean source conflicts with bridge context, the current source wins. Preserve uncertainty instead of inventing skipped-range backstory.
- From Chapter 374 onward, the ordinary workflow update, names ledger, profiles, summaries, QA, hashes, and mastering artifacts are authoritative for this branch.

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
