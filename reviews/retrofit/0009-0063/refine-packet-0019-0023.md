# Retrospective Patch Plan — Chapters 19–23

Create bounded exact-text patches; do not return complete chapters. Every `old`
string must occur exactly once in the identified current chapter. `new` must be
finished replacement prose. Combine adjacent findings when useful, never alter
unreported text, and disposition every finding.

Return exactly one JSON object with no Markdown fence:

{
  "summary": "brief patch summary",
  "patches": [
    {"chapter": 1, "finding_ids": ["R0000-01"], "old": "exact old text", "new": "exact replacement"}
  ],
  "dispositions": [
    {"finding_id": "R0000-01", "status": "applied|rejected|unresolved", "reason": "specific reason"}
  ]
}

Reject a finding only when its proposed change is not supported by the supplied
source. Leave genuinely uncertain findings unresolved. Do not intensify or
sanitize register.

## Audit rubric

# Retrospective Translation Audit Rubric

Audit accepted chapters for defects likely to survive an ordinary review. Do
not retranslate acceptable prose or optimize merely for difference.

Prioritize in this order:

1. Reversed or altered actions, negation, subjects, identities, kinship,
   quantities, causal relations, and physical direction.
2. Omitted source beats, explanatory mechanisms, pragmatic cues, ambiguity,
   jokes, and characterization.
3. Established terminology, Murim concepts, hierarchy, and address.
4. Register mismatch: intensified or sanitized profanity, euphemisms made more
   explicit, stiffness, or flattened comic timing.
5. Clear English defects that materially impede voice or meaning.

Semantic fidelity outranks polish. Preserve the source's degree of explicitness.
Do not report optional synonyms, generic praise, or whole-chapter rewrites.
Every finding must quote an exact current-English span and provide a finished,
bounded replacement. Mark a finding critical only when it changes a scene
fact, action, identity, negation, or consequence; major for meaningful lost
hierarchy, mechanism, characterization, ambiguity, or register; minor for clear
localized defects without changed meaning.

## Structured findings

```json
{
  "summary": "11 findings in chapters 19-23",
  "findings": [
    {
      "chapter": 19,
      "confidence": 0.99,
      "current": "“The situation is not good, either. According to our outside sources, rumors that Lee Seogeun was poisoned have begun spreading, and the main family’s reputation is falling.”",
      "defect": "독살당했다 means Lee Seogeun was poisoned to death, but the translation only says he was poisoned, leaving the fatal consequence unstated.",
      "id": "R0019-01",
      "rationale": "The source explicitly describes fatal poisoning, which is the event driving the war.",
      "replacement": "“The situation is not good, either. According to our outside sources, rumors that Lee Seogeun was poisoned to death have begun spreading, and the main family’s reputation is falling.”",
      "severity": "critical",
      "source": "“상황도 좋지 않습니다. 외부 소식통에 의하면 이소군이 독살당했다는 소문이 퍼지면서 본가의 평판이 추락하고 있답니다.”"
    },
    {
      "chapter": 19,
      "confidence": 0.97,
      "current": "A courtesan at Honghwaru—and my precious little finger. That thing.",
      "defect": "The literal rendering of 새끼손가락 obscures the Korean gesture-based euphemism for a girlfriend or woman, making Taekyung’s comic description unintelligible in English.",
      "id": "R0019-02",
      "rationale": "The source jokingly identifies Wolhwa as Jin Taekyung’s woman through a familiar euphemism; it is not describing an actual finger or calling her precious.",
      "replacement": "A courtesan at Honghwaru—and my, Jin Taekyung’s, girl. You know.",
      "severity": "major",
      "source": "홍화루의 기녀이자 나, 진태경의 새끼손가락. 그거."
    },
    {
      "chapter": 20,
      "confidence": 1.0,
      "current": "“That’s just Returning to the Origin…”",
      "defect": "The established Murim term 반박귀진 is mistranslated and does not match the glossary.",
      "id": "R0020-01",
      "rationale": "The required established rendering of 반박귀진 is “Returning to Simplicity.”",
      "replacement": "“That’s just Returning to Simplicity…”",
      "severity": "minor",
      "source": "“그건 반박귀진…….”"
    },
    {
      "chapter": 21,
      "confidence": 1.0,
      "current": "- As a result of repeated practice, **Sinews** and **Bones** each increase by 1.",
      "defect": "Two distinct System attributes are split into the unrelated labels “Sinews” and “Bones,” changing both attribute identities.",
      "id": "R0021-01",
      "rationale": "근맥 and 근골 are separate established System attributes: “Sinews and Meridians” and “Muscles and Bones.”",
      "replacement": "- As a result of repeated practice, **Sinews and Meridians** and **Muscles and Bones** each increase by 1.",
      "severity": "critical",
      "source": "- 반복 수련의 결과로 근맥과 근골이 1씩 상승합니다."
    },
    {
      "chapter": 21,
      "confidence": 1.0,
      "current": "*My Sinews and Bones improving steadily must be helping, too.*\n\nInternal energy flowed through the body’s meridians. The more I practiced a cultivation technique, and the more my Sinews and Bones improved, the wider and sturdier those pathways became. Compared to when I had started, I could circulate more internal energy at a much faster speed.",
      "defect": "The explanation repeatedly collapses 근골 and 근맥 into one invented attribute, losing the mechanism that both distinct attributes improve internal-energy circulation.",
      "id": "R0021-02",
      "rationale": "The source explicitly credits improvements to both 근골 and 근맥, not to a single combined “Sinews and Bones” attribute.",
      "replacement": "*The steady improvement in my Muscles and Bones and Sinews and Meridians must be helping, too.*\n\nInternal energy flowed through the body’s meridians. The more I practiced my cultivation technique and improved those two attributes, the wider and sturdier the pathways became. Compared to when I had started, I could circulate more internal energy at a much faster speed.",
      "severity": "critical",
      "source": "‘근골, 근맥이 꾸준히 향상되는 덕분인 것도 있겠지.’\n\n공력은 인체의 혈을 타고 흐른다. 심법을 수련하면 할수록, 근골과 근맥이 향상되면 될수록 혈이 넓어지고 튼튼해진다. 처음과 비교하면 보다 더 많은 공력을, 훨씬 빠른 속도로 순환시킬 수 있었다."
    },
    {
      "chapter": 21,
      "confidence": 1.0,
      "current": "**Sinews and Bones:** 105",
      "defect": "The Skill Window assigns the value 105 to the wrong System attribute.",
      "id": "R0021-03",
      "rationale": "The displayed source attribute is 근골, whose established name is “Muscles and Bones”; “Sinews and Meridians” is the separate 근맥 attribute.",
      "replacement": "**Muscles and Bones:** 105",
      "severity": "critical",
      "source": "근골 : 105"
    },
    {
      "chapter": 22,
      "confidence": 0.99,
      "current": "I sharpened my senses and looked over each of them.",
      "defect": "The translation genericizes 기감 and omits Taekyung’s activation of his established named sensory technique.",
      "id": "R0022-01",
      "rationale": "기감 is the established Skill “Qi Sense,” not merely an incidental sharpening of the senses.",
      "replacement": "I activated Qi Sense and looked over each of them.",
      "severity": "major",
      "source": "나는 기감을 일으킴과 동시에 그들의 면면을 훑었다."
    },
    {
      "chapter": 22,
      "confidence": 0.96,
      "current": "“Five. It was during last year’s bandit suppression campaign. One of them was a bandit chieftain. He was quite a strong bastard—”",
      "defect": "부채주 is a specific subordinate rank, Deputy Stronghold Lord, but “bandit chieftain” promotes the victim to the general leader and loses the hierarchy.",
      "id": "R0022-02",
      "rationale": "The prefix 부 marks a deputy position beneath the Stronghold Lord, which matters to Hyuk Mujin’s account of his combat experience.",
      "replacement": "“Five. It was during last year’s bandit suppression campaign. One of them was a Deputy Stronghold Lord. He was quite a strong bastard—”",
      "severity": "major",
      "source": "“다섯. 작년 산적 토벌 때였소. 그중 하나는 부채주였고. 제법 강한 놈이었…….”"
    },
    {
      "chapter": 22,
      "confidence": 1.0,
      "current": "Spreading its enormous wings, the messenger hawk landed by the window of the office. It belonged to the Lower District Sect.",
      "defect": "전서응 is an eagle, not a hawk, and has an established glossary rendering.",
      "id": "R0022-03",
      "rationale": "The source identifies the emergency courier specifically as a messenger eagle.",
      "replacement": "Spreading its enormous wings, the messenger eagle landed by the window of the office. It belonged to the Lower District Sect.",
      "severity": "minor",
      "source": "거대한 날개를 펼치며 집무실 창가에 내려앉은 전서응은 하오문의 그것이었다."
    },
    {
      "chapter": 23,
      "confidence": 1.0,
      "current": "*An eye?*\n\nI raised my head toward the sky. The winter sky was raining down small white scraps of garbage.",
      "defect": "The homonym 눈 is incorrectly read as “eye” even though Taekyung is identifying the snow beginning to fall.",
      "id": "R0023-01",
      "rationale": "The following look at the winter sky and falling white flakes unambiguously establishes 눈 as snow.",
      "replacement": "*Snow?*\n\nI raised my head toward the sky. The winter sky was raining down small white scraps of garbage.",
      "severity": "critical",
      "source": "‘눈?’\n\n고개를 들어 하늘을 바라봤다. 겨울 하늘이 희고 작은 쓰레기들을 쏟아 내는 중이었다."
    },
    {
      "chapter": 23,
      "confidence": 0.98,
      "current": "“Rest easy. I don’t have a taste for tormenting people.”",
      "defect": "The translation sanitizes and changes 간살, which refers to rape and murder, into generic torment, weakening Jopil’s explicit threat and characterization.",
      "id": "R0023-02",
      "rationale": "Jopil is assuring the woman only that he will not sexually violate her before killing her; the source does not claim that he avoids torment generally.",
      "replacement": "“Rest easy. I don’t make a hobby of rape and murder.”",
      "severity": "major",
      "source": "“안심하시오. 나는 간살하는 취미는 없거든.”"
    }
  ]
}
```

## Chapter 19

### Korean source

```text
＃19화



퀘스트



[전쟁]

두 가문의 명운을 건 전쟁이 시작되었습니다.

무림에서 자신을 증명하는 것은 오로지 힘! 살아남는 자가 강하고, 강한 자만이 살아남을 것입니다.

당신의 무운을 빕니다.



등급 : 메인 퀘스트

제한 : 진태경

임무 : 항산검문의 항복 또는 멸문 (미완료)

보상 : ???

실패 : ???





뚫어져라 퀘스트창을 노려보는 내게, 진위경이 말했다.

“많이 피곤한가 보구나.”

피곤? 현재 내 심리 상태를 그렇게 간단한 단어로 정의할 수 있다는 사실에 놀랐다.

나는 대답 대신 김이 모락모락 피어오르는 찻잔을 바라봤다.

‘이미 엎질러진 물이다.’

나름 노력했지만 전쟁을 막을 수는 없었다. 가로회의는 작전 회의로 바뀌었고, 대장로의 전폭적인 지지를 받은 진위경은 망설임 없이 지휘봉을 들었다.



태원진가의 무사들은 지금 즉시 본가로 집결하라!



동틀 무렵 수십 마리의 전서구가 하늘을 날았고, 전령은 말을 달렸다. 철저한 경계망이 그물처럼 펼쳐졌다.

그렇게 바짝 긴장된 분위기에서 가로회의가 파하자 나와 진위경, 위팽은 소가주 집무실로 자리를 옮겼다.

“언젠가 벌어질 일이었다. 태경이 네 탓이 아니야.”

진위경의 따스한 말에 눈물이 날 것 같다. 감동해서가 아니라, 억울해서다.

‘당연히 내 탓이 아니지!’

그리고 말이 나왔으니 말인데, 그 ‘언젠가 벌어질 일’이 왜 하필 지금 벌어지냐고.

내심 분통을 터트리고 있을 때 위팽이 불쑥 입을 열었다.

“그런데 주군.”

“왜 그러나?”

“대장로 말입니다만…… 도무지 의중을 모르겠습니다.”

대장로. 그 이름을 듣는 순간 다른 생각은 내팽개쳤다. 이 게임에서 만난 NPC 중 가장 꺼림칙한 인물이다.

진심으로 가문을 위하는 것 같기도 하고, 자신의 이익을 위해 움직이는 정치인의 냄새도 풍기고.

나는 조심스럽게 입을 열었다.

“대장로는 어떤 사람이죠?”

“높은 경지의 무인이면서 심계도 깊다. 무림에서 가장 위험한 부류라 할 수 있지.”

“그 정도인가요?”

진위경이 무겁게 고개를 끄덕였다.

“다른 장로들조차 대장로의 수족에 불과하다. 그는 모습을 좀처럼 드러내지 않으면서도, 장로원이라는 손발을 이용해 중진들을 포섭하고 휘하로 끌어들였지. 그 세월이 수십 년이다.”

“그럼 가로회의에서 우리 손을 들어 준 것도…….”

“정확한 사실은 알 수 없지만 꿍꿍이가 있을 것이다. 분명해.”

“다 죽였어야 했습니다.”

위팽이 차가운 목소리로 불쑥 끼어들었다.

“불충한 역도들입니다. 대장로가 그들을 죽이자고 제안했을 때, 저는 솔직히 주군께서 받아들이셨으면 했습니다.”

나도 그랬다. 하지만 그것은 대장로의 교묘한 화법에 불과했다. 이 정도에서 물러나는 게 어떻겠냐는.

만약 진위경이 미친 척 그 제안을 수락했다면 결과는 뻔하다.

“혈사가 일어났겠지.”

“압니다. 그래서 참은 거고요.”

태원진가의 수뇌부가 반으로 갈라져 죽고 죽이는 싸움을 계속할 것이다. 지면 죽음이고, 이겨도 큰 피해를 입었을 것이다.

‘어쩌면 그게 대장로가 바랐던 결과일지도.’

대장로. 보이지 않는 손. 문득 떠오른 생각에 등골이 오싹했다. 마침 내가 느낀 대장로의 이미지와도 딱 맞아떨어진다.

한발 물러나 때를 기다리는 하이에나 같은 정치인.

진위경이 찻잔을 기울였다.

“하지만 어디까지나 짐작일 뿐. 대장로의 의중이 무엇인지는 모르는 것이다. 아직 그는 본가의 어른이며 강력한 아군이다. 주의는 하되 적대하지 말거라. 지금은 사람을 경계하기보다 상황을 헤쳐 나가야 할 때야.”

나무가 아니라 숲을 보라는 이야기다.

문제는 그 숲도 썩 좋은 상황이 아니라는 거지.

내 생각을 읽은 것처럼 위팽이 그에 관련된 이야기를 꺼냈다.

“상황도 좋지 않습니다. 외부 소식통에 의하면 이소군이 독살당했다는 소문이 퍼지면서 본가의 평판이 추락하고 있답니다.”

“고작 반나절 만에?”

“예. 산서성 전체가 그 얘기로 들썩거리고 있습니다.”

진위경의 얼굴에 근심이 서렸다.

“빠르군. 소문이 빨라도 너무 빨라. 확실히 뒤에 누군가 있어.”

여기에 인터넷이 있는 것도 아니고, 이 넓은 땅덩어리에 벌써 소문이 퍼졌다는 것은 확실히 이상한 일이다.

‘보이지 않는 적이라.’

도대체 누굴까. 제삼의 세력? 항산검문의 자작극?

나는 가급적 후자이기를 바랐다. 드러나지 않는 적만큼 위험한 건 없으니까.

“민심은 아직까지 반신반의하는 모양이지만 다른 문파들은…….”

“아직도 답이 없나?”

위팽은 대답 대신 고개를 숙였다.

진위경은 이소군의 독살 정보를 입수한 직후 곧장 산서성의 다른 중소 문파들에게 지원 요청을 했다. 하지만 빠짐없이 수포로 돌아간 모양이었다.

‘갈수록 최악인데 이건.’

진짜 도망쳐야 되나.

그런 생각을 하며 창밖을 바라보고 있을 때였다. 푸드득. 홰치는 소리와 함께 비둘기 한 마리가 창가에 내려앉았다.

“……답장, 온 것 같은데요?”



* * *



태원진가.

웅장한 필체로 적힌 현판, 그리고 삼엄한 기세로 정문을 지킨 무사들이 가까워지자 마부는 고삐를 느슨하게 늘어트렸다.

“정지. 신원과 목적을 밝히시오!”

수문위사가 크게 외치며 마차를 가로막았다. 상황이 상황인지라 그의 목소리에는 긴장감이 배어 있었다.

더군다나.

‘범상치 않다.’

고삐를 쥔 마부에게서는 단련된 무인의 냄새가 물씬 풍겼고, 네 마리 준마가 끄는 사두마차는 화려함과 동시에 기품이 있다.

‘그런데 왠지 낯이 익은데?’

마부도 그렇고. 마차도 그렇고. 어디서 봤더라?

잠깐 떠오른 의문은 마부의 날카로운 눈매를 보는 순간 잊혔다. 저 기세, 눈빛. 역시 범상치 않은 손님이다.

꿀꺽 침을 삼킨 수문위사가 재차 입을 열었다.

“신원과 목적을 밝혀 주십시오.”

마차의 문이 열리고, 붉은색 비단신이 사뿐히 내려앉았다.

그리고 봄바람처럼 살랑거리는 목소리가 수문위사의 귓가에 내려앉았다.

“홍화루에서 왔어요. 이름은 비밀.”

목소리와 함께 드러나는 얼굴.

수문위사의 눈이 몽롱하게 풀어졌다. 비단 그 혼자만의 일이 아니었다. 여인의 얼굴을 확인한 모두가 같은 반응이었다.

수문위사의 입에서 넋 나간 목소리가 흘러나왔다.

“아, 비밀…… 그럼 어떤 용무로 오셨는지.”

여인, 월화는 매혹적인 미소와 함께 대답했다.

“음. 외상값 받으러?”



* * *



“잘 지냈어요? 나 안 보고 싶었고?”

나는 엉거주춤 일어선 채로 굳어 버렸다.

잊을 수 없는 얼굴. 그리고 여기 있어서는 안 되는 얼굴이다.

“월화?”

이 게임에서 처음 만난 NPC. 홍화루의 기녀이자 나, 진태경의 새끼손가락. 그거.

누나가 왜 거기서 나와……?

“역시 기억하시네. 우리 진 공자님.”

월화가 까르르 웃는다. 얘는 얼굴도 예쁜데 웃음소리도 예쁘고, 예쁜 애가 웃으니까 더 예뻐…… 아니, 지금 이럴 때가 아닌데.

나는 잔뜩 숨죽인 목소리로 속삭였다.

“여긴 어쩐 일로 왔어요. 아, 됐고. 나가요. 나가.”

팔꿈치로 슬쩍슬쩍 월화의 몸을 밀었다. 와, 진짜 미치겠다.

하필이면 이런 분위기에 나타나다니.

가문 전체에 비상 경계령이 떨어졌는데 기녀 불렀다고 소문이라도 나 봐라. 내 평판이 어떻게 될지 상상만 해도 눈앞이 아찔하다.

“찌르지 마요. 간지럽잖아.”

“알겠으니까 빨리 나가요. 여기 지금 다른 사람들도 있는데 갑자기 와서 뭐 하자는 겁니까? 중요한 손님도 오시기로 했는데.”

타이밍도 참 더럽게 안 좋다. 나는 소가주 집무실에서 하오문이라는 문파의 손님을 기다리는 중이었다.

당연하게도 진위경, 위팽과 함께였다.

“태경아.”

진위경의 부름. 나는 뒤도 돌아보지 않고 황급히 손을 내저었다.

“아, 생각하시는 그런 거 아닙니다. 저 안 불렀어요. 이분도 이제 가실 거래요. 그렇죠?”

월화의 웃음소리가 높아졌다.

“우리 진 공자님은 여전히 귀여우셔. 근데 잘못 짚었어. 나 여기 볼일 있어서 온 거거든.”

“어허, 우리 진 공자는 무슨. 나 오늘부터 순결하게 살 거예요. 이제 그쪽 볼일 없으니까 빨리 나가요.”

“음. 싫은데?”

그럼 어쩔 수 없지. 힘으로 옮기는 수밖에. 나는 절박한 심정으로 월화의 허리를 붙잡고 번쩍 들어서…….

“응?”

뭐야, 이거. 왜 안 들려. 월화가 겉보기에는 늘씬하지만 통뼈라 무게가 많이 나가나?

‘개소리지.’

내 힘 스탯이 몇인데. 단순 근력으로만 해도 돌멩이를 가루로 만들어 버릴 수 있다. 그런데 내가 여자 NPC 하나 못 든다는 건…….

“저, 태경아?”

진위경의 두 번째 부름은 무시한 나는 슬그머니 손을 풀었다. 그리고 [기감]을 끌어올렸다.

“아하하하하! 미치겠다, 진짜.”

웃겨 죽는 월화의 머리 위로 레벨창이 뜸과 동시에, 진위경의 세 번째 부름이 들려왔다.



[Lv.50 은소월]



“태경아, 인사드려라. 하오문 산서 지부장님이시다…….”

아아. 아아아.

죽고 싶다.



* * *



“인사 올립니다. 하오문 산서 지부장, 월화입니다.”

은소월. 아니, 일단은 월화라고 해 두자. 그녀는 지금까지의 모습과는 달랐다. 동작 하나하나에 귀부인 같은 기품과 우아함이 묻어 나왔다.

“태원진가의 진위경이오.”

“위팽입니다.”

“…….”

벙어리 삼룡이마냥 입을 다물고 있는 내게 월화가 씩 웃어 보였다. 불길한 웃음이다.

‘안 돼. 웃지 마.’

말 걸지도 마. 제발 그러지 마.

“한 분 소개를 못 들은 것 같은데요.”

시선이 따갑다. 탁자 아래로 누군가 내 발을 밟았다.

나는 피를 토하는 심정으로 입을 열었다.

“……진태경입니다.”

“네에. 저도 잘 부탁드려요. 진 공자님.”

커흠. 진위경이 헛기침과 함께 힐끔 나를 살폈다.

“내 동생과 친분이 있는 줄은 몰랐소만.”

“저희 가게 단골이시거든요. 태원에 있는 홍화루. 본 문의 산서지부이기도 하지요.”

“아, 단골…….”

나는 사람들의 시선을 회피했다. 풉, 웃음을 터트린 월화가 본론을 꺼내 들었다.

“이제 일 얘기를 해 볼까요?”

여러 번 느끼는 거지만 역시 시원시원한 여자다. 진위경과 위팽도 내게서 시선을 떼고 대화에 임했다.

“우선 하오문의 도움에 진심 어린 감사를 표하오.”

“별말씀을요.”

“한데, 본가를 도우려는 이유를 알 수 있겠소?”

진위경의 말에 월화가 싱긋 웃었다.

“이유라…… 필요하다면 말씀드리지요. 우선 첫째, 본 문의 이득을 위해서입니다.”

“이득이라. 구체적으로 어떤 보상을 원하시오?”

“항산검문이 소유한 점포와 재화의 절반.”

“좋소.”

“주군!”

위팽이 황급히 나섰지만 진위경은 아랑곳하지 않았다.

월화도 살짝 놀란 기색이었다.

“결정이 빠르시군요.”

“가문의 모든 걸 걸었으니까.”

“이미 합의된 내용인가요?”

“나는 소가주고, 아버님이 안 계신 지금 가주 대행의 권한을 갖고 있소.”

“내부의 반발이 꽤 거센 걸로 아는데요. 예를 들면 장로원이라든가?”

“역시 하오문. 정보가 빠르군.”

“어쩔 수 없지요. 이 삭막한 무림에서 살아남으려면 정보가 필수인데. 이런 수완이라도 있어야 먹고살지 않겠어요?”

월화의 웃음을 보면서, 문득 한 가지 생각이 들었다.

‘저 정보. 혹시 내가, 아니 진태경이 흘린 건가?’

하오문, 그 이름을 어디서 들어봤나 했더니 무협 소설에서 단골로 등장하는 정보 문파다. 즉, 지부장인 월화는 베테랑 정보 상인인 셈이고.

거기에 더해 50레벨의 출중한 무인이기도 하다. 저런 여자가 기녀로 위장해서 진태경 같은 놈을 만나?

‘개가 웃을 소리지.’

나는 월화를 응시했다. 여신이 내려왔나 싶을 정도로 눈부신 외모다. 그녀가 웃을 때마다 장미가 생각났다. 그 화려함에 숨겨진 날카로운 가시가 이제야 보인다.

진위경이 굳은 얼굴로 말했다.

“그럼 이제 두 번째 이유를 말하시오.”

월화가 예의 화사한 미소를 지으며 대답했다.

“진 공자가 마음에 들어서요.”

“예?”

“어린 데다가 얼굴 잘생겼고, 몸 좋고, 성격도 귀엽고.”

“…….”

“…….”

도대체 어디까지가 진심이고 농담이야?
```

### Current accepted English

```markdown
# Chapter 19

> **System**
>
> **Quest**
>
> **War**
>
> A war that will decide the fate of two factions has begun.
>
> In Murim, the only way to prove yourself is through strength! Those who survive are strong, and only the strong will survive.
>
> May fortune favor you in battle.
>
> **Grade:** Main Quest  
> **Restriction:** Jin Taekyung  
> **Mission:** Surrender or destruction of the Mount Heng Sword Sect (Incomplete)  
> **Reward:** ???  
> **Failure:** ???

Jin Wikyung spoke to me as I stared fixedly at the Quest Window.

“You look very tired.”

Tired? I was amazed that my current state of mind could be summed up in such a simple word.

Instead of answering, I looked at the steaming teacup.

*The water’s already been spilled.*

I had done my best, but I couldn’t stop the war. The family council had turned into a war council, and with the Head Elder’s full support, Jin Wikyung had taken up command without hesitation.

> Martial artists of the Jin Family of Taiyuan, assemble at the main family residence immediately!

At dawn, dozens of messenger pigeons took to the sky while messengers rode hard on horseback. A tight security net was thrown over the entire area.

When the family council finally broke up in that tense atmosphere, Jin Wikyung, Wipeng, and I moved to the Lesser Family Head’s office.

“It was bound to happen someday. This isn’t your fault, Taekyung.”

I felt like crying at Jin Wikyung’s warm words. Not because I was moved, but because it felt so unfair.

*Of course it wasn’t my fault!*

And since we were on the subject, why the hell did that “bound to happen someday” have to happen now?

While I was fuming inwardly, Wipeng suddenly spoke.

“My lord.”

“Why?”

“The Head Elder… I simply cannot figure out what he’s thinking.”

The Head Elder. The moment I heard that name, I abandoned all other thoughts. He was the most unsettling person among the NPCs I had encountered in this game.

He seemed genuinely devoted to the family, yet he also gave off the unmistakable air of a politician maneuvering for his own benefit.

I cautiously opened my mouth.

“What kind of person is the Head Elder?”

“He is a martial artist of a high realm, and his schemes run deep. You could call him one of the most dangerous types of people in Murim.”

“That dangerous?”

Jin Wikyung nodded heavily.

“Even the other Elders are little more than the Head Elder’s hands and feet. He rarely reveals himself, yet he has used the Elder Council to win over influential members and bring them under his command. He has been doing so for decades.”

“Then his supporting us at the family council…”

“We cannot know the exact truth, but he must have an ulterior motive. Of that, I am certain.”

“We should have killed them all.”

Wipeng cut in abruptly, his voice cold.

“They are disloyal rebels. When the Head Elder proposed killing them, I honestly hoped you would accept.”

I had felt the same way. But that had merely been the Head Elder’s clever way of speaking—a suggestion that perhaps we should back down at this point.

If Jin Wikyung had pretended to be insane and accepted that proposal, the result would have been obvious.

“A bloodbath would have broken out.”

“I know. That’s why I held back.”

The Jin Family of Taiyuan’s leadership would have split in two and continued fighting until they killed one another. If we lost, we would die. Even if we won, we would suffer tremendous damage.

*Maybe that was exactly what the Head Elder wanted.*

The Head Elder. An invisible hand.

A chill ran down my spine at the thought. It fit the image I had formed of him perfectly.

A politician like a hyena, stepping back and waiting for his moment.

Jin Wikyung tilted his teacup.

“But that is only a guess. We do not know what the Head Elder truly intends. He is still one of the family’s elders, and a powerful ally. Be wary of him, but do not make an enemy of him. For now, we need to overcome the situation rather than distrust everyone around us.”

He was telling me to look at the forest, not the trees.

The problem was that the forest itself wasn’t exactly in good shape, either.

As if he had read my thoughts, Wipeng brought up the subject.

“The situation is not good, either. According to our outside sources, rumors that Lee Seogeun was poisoned have begun spreading, and the main family’s reputation is falling.”

“In only half a day?”

“Yes. All of Shanxi is in an uproar over it.”

Concern clouded Jin Wikyung’s face.

“That is fast. Far too fast. Someone is definitely behind this.”

There was no internet here, and yet rumors had already spread across this vast land. It was certainly strange.

*An invisible enemy.*

Who could it be? A third faction? A staged act by the Mount Heng Sword Sect?

I hoped it was the latter if possible. Nothing was more dangerous than an enemy who remained unseen.

“The people are still taking the rumors with a grain of salt, but the other sects…”

“Still no replies?”

Wipeng lowered his head instead of answering.

Immediately after obtaining the information about Lee Seogeun’s poisoning, Jin Wikyung had sent requests for support to the other small and mid-sized sects in Shanxi. But it seemed every one of them had failed.

*This keeps getting worse.*

*Do I really need to run?*

I was looking out the window, thinking that, when—

Flap, flap.

A pigeon landed on the windowsill with the sound of beating wings.

“…It looks like a reply has arrived?”

* * *

The Jin Family of Taiyuan.

As the carriage approached the grand signboard written in magnificent calligraphy and the martial artists standing guard at the main gate with a stern aura, the coachman loosened the reins.

“Stop. State your identity and purpose!”

The gate guard called out loudly and blocked the carriage. Given the circumstances, there was tension in his voice.

More than that—

*This isn’t ordinary.*

The coachman holding the reins gave off the unmistakable air of a trained martial artist, while the four-horse carriage had both luxury and dignity.

*But why does he look familiar?*

The coachman, too. The carriage, too. Where had he seen them?

The question vanished the moment he saw the coachman’s sharp eyes. That aura, that gaze. This was certainly no ordinary visitor.

The gate guard swallowed and spoke again.

“Please state your identity and purpose.”

The carriage door opened, and a red silk slipper stepped lightly onto the ground.

Then a voice as gentle as a spring breeze drifted into the guard’s ear.

“I’m from Honghwaru. My name is a secret.”

Her face appeared along with her voice.

The gate guard’s eyes grew dazed. He wasn’t the only one. Everyone who saw the woman reacted the same way.

A vacant voice escaped the gate guard’s mouth.

“Ah, a secret… Then what brings you here?”

The woman, Wolhwa, answered with a charming smile.

“Hmm. I’m here to collect an unpaid tab?”

* * *

“How have you been? Didn’t you miss me?”

I froze halfway to standing.

A face I could never forget. And a face that had no business being here.

“Wolhwa?”

The first NPC I had met in this game. A courtesan at Honghwaru—and my precious little finger. That thing.

*Why is noona coming out of there…?*

“You remember me after all. Our Young Master Jin.”

Wolhwa giggled. She was beautiful, had a beautiful laugh, and when a beautiful woman laughed, she became even more beautiful…

*No, this is not the time for that.*

I whispered in a tightly restrained voice.

“What brings you here? No, never mind. Leave. Get out.”

I nudged Wolhwa with my elbow.

*This is driving me insane.*

Of all times, she had to show up in this atmosphere.

The entire family was on high alert. If word got out that I had called for a courtesan, I couldn’t even imagine what would happen to my reputation. Just thinking about it made my vision swim.

“Don’t poke me. That tickles.”

“I know, so get out quickly. There are other people here. What are you trying to do by suddenly coming here? We’re expecting an important guest, too.”

The timing was damn awful, too. I was waiting for a guest from a sect called the Lower District Sect in the Lesser Family Head’s office.

Naturally, Jin Wikyung and Wipeng were there with me.

“Taekyung.”

Jin Wikyung called my name. Without even turning around, I hurriedly waved my hands.

“Ah, it’s not what you think. I didn’t call her. She’s leaving now, too. Right?”

Wolhwa’s laughter rose in pitch.

“Our Young Master Jin is still so adorable. But you guessed wrong. I came here because I have business to attend to.”

“Don’t call me ‘our Young Master Jin.’ I’m going to live chastely from today onward. I don’t have any business with you anymore, so get out quickly.”

“Hmm. No.”

Then there was no helping it. I would have to move her by force.

In desperation, I grabbed Wolhwa around the waist and hoisted her up—

“Huh?”

What the hell? Why won’t she lift?

Wolhwa looked slender, but was she so big-boned that she weighed a lot?

*That’s bullshit.*

What was my Strength stat again? With pure physical strength alone, I could grind a rock into powder. And yet I couldn’t lift one female NPC, which meant—

“Taekyung?”

I ignored Jin Wikyung’s second call and furtively let go. Then I heightened my Qi Sense.

“Ahahahahaha! This is driving me insane!”

As Wolhwa laughed herself to death, a Level Window appeared above her head. At the same time, I heard Jin Wikyung call my name for the third time.

> **System**
>
> **Lv. 50 Eun Sowol**

“Taekyung, greet her. She is the Branch Leader of the Lower District Sect’s Shanxi branch…”

Ah. Ahhh.

*I want to die.*

* * *

“Greetings. I am Wolhwa, Branch Leader of the Lower District Sect’s Shanxi branch.”

Eun Sowol.

No, for now, let’s just call her Wolhwa.

She was different from how she had acted until now. Every movement carried the grace and elegance of a noblewoman.

“I am Jin Wikyung of the Jin Family of Taiyuan.”

“I’m Wipeng.”

I kept my mouth shut like mute Samryong,[^1] and Wolhwa flashed me a grin.

It was an ominous grin.

*Don’t. Don’t smile.*

*Don’t talk to me. Please don’t.*

“It seems I haven’t been introduced to one person.”

Her gaze stung. Someone stepped on my foot beneath the table.

I opened my mouth with a feeling like I was coughing up blood.

“…I’m Jin Taekyung.”

“Yes. I hope we get along too, Young Master Jin.”

“Ahem.”

With a cough, Jin Wikyung glanced at me.

“I didn’t realize you were acquainted with my younger brother.”

“He is a regular at our establishment—the Honghwaru in Taiyuan. It also serves as this sect’s Shanxi branch.”

“Ah. A regular…”

I avoided everyone’s gaze. Wolhwa let out a burst of laughter, then brought up the real subject.

“Shall we talk business now?”

I had felt it several times before, but she really was a refreshingly direct woman. Jin Wikyung and Wipeng also turned their attention away from me and joined the conversation.

“First, allow me to offer my sincere thanks for the Lower District Sect’s assistance.”

“Think nothing of it.”

“But may I ask why you wish to help our family?”

Wolhwa smiled sweetly at Jin Wikyung’s question.

“The reason… I will tell you if necessary. First, we are doing this for our sect’s benefit.”

“Benefit. What specific compensation do you want?”

“Half of the shops and assets owned by the Mount Heng Sword Sect.”

“Good.”

“My lord!”

Wipeng hurriedly stepped forward, but Jin Wikyung paid him no heed.

Wolhwa also looked slightly surprised.

“You decide quickly.”

“Because I have staked everything the family has.”

“Has this already been agreed upon?”

“I am the Lesser Family Head, and with Father absent, I possess the authority of the acting Family Head.”

“I hear the internal opposition is quite fierce. The Elder Council, for example?”

“As expected of the Lower District Sect. Your information is fast.”

“It cannot be helped. Information is essential for survival in this bleak Murim. We need skills like these to make a living, don’t we?”

Watching Wolhwa smile, I suddenly had a thought.

*That information. Did I—or rather, did Jin Taekyung—let it slip?*

I had wondered where I had heard the name Lower District Sect before. It was an information-gathering sect that appeared regularly in martial-arts novels. In other words, Wolhwa, its Branch Leader, was a veteran information merchant.

On top of that, she was an outstanding martial artist at Level 50. A woman like that had disguised herself as a courtesan to meet a guy like Jin Taekyung?

*Even a dog would laugh at that.*

I stared at Wolhwa.

Her beauty was dazzling enough to make me wonder if a goddess had descended. Whenever she smiled, roses came to mind. Only now could I see the sharp thorns hidden beneath all that splendor.

Jin Wikyung spoke with a stiff expression.

“Then tell us the second reason.”

Wolhwa answered with her usual radiant smile.

“Because I like Young Master Jin.”

“Excuse me?”

“He’s young, handsome, well-built, and has such a cute personality.”

“…”

“…”

*How much of that was sincere, and how much was a joke?*

[^1]: Samryong is the mute protagonist of a well-known Korean short story; his name literally means “Three Dragons.”
```
## Chapter 20

### Korean source

```text
＃20화



한 시간에 걸친 협상은 어느덧 마무리 단계에 접어들었다.

“항산검문 소유의 점포 절반. 그리고 환락가 독점권. 맞나요?”

“틀림없소. 귀 문은?”

“이 순간부터 태원진가를 제외한 산서성의 어느 문파에게도 정보를 팔지 않을 것이며, 총력을 기울여 전쟁에 관한 정보를 수집, 전달하겠습니다.”

이미 수십 번의 밀고 당기기 끝에 결정된 협의 사항이다.

진위경과 월화는 마지막까지 빈틈이 없는지 꼼꼼하게 점검한 후 문서를 작성, 교환했다.

“이제 정식으로 한배를 타게 됐군요. 잘 부탁드려요, 소가주님.”

“나 역시.”

둘이 손을 맞잡은 순간이었다.

띠링.



- [태원진가]와 [하오문]이 동맹을 맺었습니다.

- 동맹은 전쟁 기간 동안 유지됩니다.



이런 것까지 뜨네. 하긴, 항산검문과의 전쟁이 시작됐을 때도 비슷한 알림이 울렸지.

‘하오문까지 가세했으니 이길 확률이 조금은 올라간 건가?’

하오문은 정보를 전문적으로 취급하는 문파다.

월화가 자신만만하게 말하길, 산서성의 모든 정보가 자신을 거쳐 흐른다는데 그 말이 사실이라면 엄청난 보탬이 될 것이다.

‘정보만큼 중요한 게 없지.’

무림에서는 어떨지 모르지만 나는 알고 있다. 정보는 어떻게 다루느냐에 따라 달라진다. 칼, 방패, 때로는 한번에 전세를 뒤집는 폭탄이 될 수도 있다.

월화가 그런 정보를 물어 온다면 좋을 텐데.

“그럼 저는 이만 물러가지요.”

“눈이 있어 멀리 못 나가는 것을 양해 바라오.”

“당연한 말씀을.”

드디어 끝났구나. 위팽은 무뚝뚝한 얼굴로 고개를 숙였고 나도 엉거주춤 인사했다.

“안녕히 가세요.”

나를 본 월화의 눈이 반달처럼 휘었다.

“진 공자도 같이 가야죠.”

“예?”

“나 배웅 안 해 줘요?”

“……제가 왜요?”

“음. 뜨거운 밤을 함께 보낸 사이니까?”

몸 쪽 꽉 찬 돌직구에 순간 멍해진다. 아니, 이 여자는 정보를 가져오랬더니 뭐 이런 19금 정보부터 뿌리고 있냐.

그것도 사람들 앞에서.

“호오.”

“뜨, 뜨거운 밤? 함께?”

위팽은 흥미롭다는 눈빛으로 나와 월화를 번갈아 바라봤고, 진위경의 동공에는 지진이 일어났다.

“태경아, 사실이냐? 그게 사실이야?”

나는 침묵 끝에 대답했다.

“배웅해 드리고 올게요.”

월화의 손목을 잡고 후다닥 뛰쳐나가는 등 뒤로 진위경의 구슬픈 음성이 메아리쳤다.

“막내야아!”



* * *



월화는 보기 드문 미녀다. 늘씬한 몸매에 화려한 옷차림까지 더해지니 시선이 모일 수밖에 없었다.

“가문에 저런 미인이 있었나?”

“당연히 없지. 외부인이야.”

“외부인?”

“어. 수문각 친구 말로는 홍화루 기녀라던데.”

“아, 그 더럽게 비싸다는 홍화루. 알지. 잠깐, 그런데 기녀가 지금 여기에 올 일이 뭐가 있어?”

“삼공자한테 외상값 받으러 왔대. 본격적으로 전면전이 벌어지기 전에 떼인 돈 미리 받아 두겠다는 거겠지.”

“……허. 삼공자 정말 가지가지 하는구먼.”

사람들의 속삭임이 귓가를 파고든다. 콧노래를 흥얼거리며 앞서 걷던 월화가 문득 뒤를 돌아봤다.

“진 공자, 왜 이렇게 떨어져 있어요?”

나는 퉁명스러운 어조로 대꾸했다.

“같이 걸으면 사람들이 괜히 오해하잖아요. 벌써부터 저런 헛소문이 도는데…….”

“아, 외상값?”

그래, 그거.

“그거 헛소문 아닌데?”

월화가 화사하게 웃었다.

“수문위사들이 왜 왔냐고 묻길래 그냥 외상값 받으러 왔다고 했어요. 뭐, 아예 거짓말도 아니고.”

“예?”

“그럼 동맹 맺었다고 천하에 공표라도 할 생각이었어요?”

“……그건 아닌데.”

왜 하필 내 이름을 팔아. 가뜩이나 이미지도 개판이구만.

당장 전쟁이 일어난 마당에 이런 소문이 퍼져 봐라, 빼도 박도 못 하고 쓰레기 이미지 굳히는 거다.

“독살범 누명까지 쓴 마당에 기둥서방 정도면 양호하죠. 진 공자 평소 행실이 있으니 사람들도 납득할 거고.”

그거 묘하게 설득력 있네. 나도 모르게 고개를 끄덕이다가 월화의 말에서 문득 위화감을 느꼈다.

“누명?”

이제 와 생각해 보니, 그녀는 단 한 번도 이소군과 연관된 이야기를 꺼내지 않았다. 깐깐한 사업가처럼 협의를 조정하고 당연하다는 듯 동맹을 맺었다.

‘도대체 뭘 믿고?’

의혹 어린 눈길에 월화가 빙긋 웃었다.

“진 공자, 내가 누군지 잊었어요?”

“하오문 산서 지부장…….”

눈이 번쩍 뜨였다.

정보, 정보가 있구나. 내가 범인이 아니라는 정보가!

나는 빠르게 월화의 옆으로 붙었다.

“내 누명을 벗길 수 있습니까? 정말 그런 정보가 있어요?”

전쟁의 발단은 이소군의 독살이다. 이 모든 것이 누군가에 의해 벌어진 음모라는 것을 증명한다면, 전쟁을 막을 수 있다.

하지만 그 기대는 월화의 다음 말로 산산조각 났다.

“아뇨, 없어요.”

뭐?

“그럼 왜 우리와 동맹을?”

“장사치니까.”

월화가 경쾌한 어조로 말을 이었다.

“우리 하오문은 기본적으로 장사꾼들이에요. 철저히 이해득실을 따라 움직이죠.”

“그렇다면 더 말이 안 되는 것 같은데요.”

“어머, 왜?”

“항산검문이 우리보다 강하니까. 당신 말대로 이해득실을 따진다면 항산검문 쪽에 붙어야 하는 것 아닙니까?”

“솔직하네요. 아니, 순진하다고 해야 하나?”

월화가 피식 웃었다.

“이건 투자예요. 양측을 저울 위에 올려놓고 냉정하게 분석한 결과죠.”

“이득만 취하면 상관없다는 겁니까? 내가 정말 이소군을 독살했다고 해도?”

“진 공자. 하오문 산서지부가 총력을 기울였는데도 사실을 확인할 수 없었다, 이게 무슨 의미일 것 같아요?”

나는 머뭇거렸고, 월화는 대답을 기다리지 않았다.

“간단해요. 진 공자가 정말 결백하거나, 아니면 우리조차 확인할 수 없을 정도로 잘 감췄거나.”

“아.”

“둘 중 어느 쪽이어도 내겐 손해가 아니에요. 전자라면 정당성이 있으니 그걸로 좋고, 후자라면 태원진가의 수완이 그만큼 뛰어나다는 반증이니까.”

적잖이 놀랐다. 이렇게 바라볼 수도 있구나. 철저한 이해득실과 계산. 월화가 말한 자신들은 장사치라는 의미를 정확히 알겠다.

이런 존재가 아군이라는 사실에 내심 든든한 마음도 들었다.

하지만…….

“중요한 하나가 빠졌네요. 내가 결백하다면 이소군을 독살한 주범은 누구인가?”

그거야말로 이 전쟁의 핵심이다. 월화도 찾아내지 못한 가장 큰 퍼즐 조각.

만약 하오문에서 범인의 정체를 알아차렸다면, 오늘 그 정보를 가져왔을 테니까.

월화가 한숨을 내쉬었다.

“부끄럽지만 아직까지 밝혀진 바가 없네요. 하지만 본 문에서는 최선을 다하고 있어요. 아, 거의 도착했네요.”

묻고 싶은 게 많았지만, 가까워진 수문위사들을 의식해서 입을 다물 수밖에 없었다.

‘아직까지 하오문과의 동맹은 비밀이니까.’

월화가 타고 온 것으로 보이는 사두마차와 그 주위를 넓게 둘러싼 수문위사들이 눈에 들어왔다. 묘한 긴장감이 여기까지 물씬 전해져 온다.

‘무슨 문제라도 생겼나?’

나는 눈과 귀로 공력을 흘려보냈다. 곧 향상된 감각들을 통해 수문위사들의 긴장한 목소리가 들려왔다.

“고수야. 틀림없어. 최소 초일류, 어쩌면 절정 고수일지도 모르지. 허리춤에 채찍 보여? 필시 편(鞭)을 귀신처럼 다루는 자일거야.”

“저 정도 고수가 마부를 자처하다니, 역시 절세가인은 달라.”

제법 경륜 있어 보이는 무사들이 심각한 어조로 말을 주고받았다. 그 말을 들은 어린 무사가 소심하게 중얼거렸다.

“하지만 그런 것치고는 자세에 너무 빈틈이 많은 것 같은데요? 체격도 말랐고…….”

선임 무사들이 그 말에 혀를 찼다.

“마, 나랑 이 친구는 수문각 짬밥만 십 년이야. 눈빛만 봐도 알아. 어린 노무 새끼가 뭘 안다고 어르신들 얘기하는데 끼어들어?”

“허참. 빈틈? 저게 빈틈으로 보이냐? 고수들만이 가지는 여유, 자연스러움. 이런 게 하나도 안 보여?”

“그럼 태양혈은요? 내공이 심후한 고수들은 태양혈이 튀어나와 있잖아요.”

“그건 반박귀진…….”

아쉽게도 말은 거기서 끊어졌다. 수문위사들이 정문 앞에 멀뚱히 서 있는 우리를 발견하고 흩어졌기 때문이다.

덕분에 확인할 수 있었다.

채찍을 귀신처럼 다루는 절정 고수. 월화의 미모에 반해 마부를 자처하는 로맨틱한 무림인의 정체를.

“공자님, 절 기억하십니까?”

“…….”

잊었을 리가 있나.

묵직한 목소리. 날카로운 눈빛에서 풍기는 고수의 향기.

며칠 전 나를 태원진가로 데려다준 그 마부 아저씨다.

저 얼굴을 여기서 볼 줄이야. 순간 말을 잇지 못하는 내게 월화가 말했다.

“진 공자랑 친분이 있다고 하더라고요. 지난번에 함께 생사를 넘나들며 나이와 신분을 초월한 끈끈한 우정을…….”

아니야. 그거 아니야. 제발 그만해.

그런 뜻을 담아 월화의 옷소매를 잡아끌었지만 늦었다. 마부가 잔잔한 미소를 지으며 입을 열었다.

“아직도 눈만 감으면 그날의 기억이 생생합니다. 천력부…… 정말 강한 놈이었죠.”

귀를 쫑긋 세우고 있던 수문위사들이 탄성을 토했다.

“오오.”

“천력부…… 설마 녹림십팔채의 그 천력부?”

“흉명이 자자한 녹림의 절정 고수가 아닌가. 그런 놈을 죽이다니 역시 저분은…….”

“…….”

거 뭔가 대단히 잘못 알고 있는 것 같은데.

어디서부터 어디까지 바로잡아야 하는지도 모르겠다. 멍하니 서 있는 나를 마부가 덥석 끌어안았다.

“공자가 아니었다면 큰 낭패를 당할 뻔했습니다.”

이 아저씨 말 참 묘하게 하네. 나 아니었으면 북망산 정상에서 막걸리 한 잔 하고 있었을 양반이.

“일단 이것 좀 놓고 말씀을…….”

마부를 막 떼어 놓으려던 찰나였다.

“염라편(閻邏鞭). 십여 년 전 홀연히 모습을 감춘 편법의 달인. 맞아. 바로 그가 틀림없어.”

누군가의 중얼거림에 수문위사들 사이로 파문이 일었다.

“염라편? 천하를 주유하며 마도의 잔당들을 때려잡던 그 절정 고수 말인가?”

“그 이름이라면 나도 들어 본 적이 있어. 사문도, 과거도 알려지지 않은 정사지간의 고수…… 그러고 보니 종적이 끊겼던 곳이 산서성 인근이라던데.”

“그럼 저 삼공자가, 아니 우리 공자님이 바로 그 염라편 대협과 친분이 있단 소리잖아.”

“그뿐인가. 천력부를 해치우는 데 크게 일조하신 게 분명해.”

“오오. 오오오.”

뜨거운 눈빛들이 사방에서 쏟아졌다. 뭔가 이상함을 느꼈는지 마부가 몸을 빼려고 했지만 내 손아귀가 그의 어깨를 단단히 붙들고 있었다.

“공자님?”

나는 세상에서 가장 환하게 웃어 보였다.

“이렇게 다시 뵙는군요. 염.라.편. 대협!”

내 한마디는 불길에 기름을 끼얹는 효과를 냈다.

우오오. 잔뜩 달아오른 수문위사들이 발을 굴렀고, 월화는 필사적으로 웃음을 참느라 허리를 숙였다.

띠링.



- [독살범]에 관한 소문이 사그라집니다!

- [산서잠룡]에 관한 소문에 신빙성이 더해집니다!

- 명성이 20 상승합니다!

- 열성적인 지지자들이 생겨납니다!



아름답게 울려 퍼지는 시스템 알림 속에서, 나는 명언 하나를 떠올렸다.

‘완벽한 구라는…… 실화다.’



* * *



청년은 부릅뜬 눈으로 천장을 바라보고 있었다. 한때 반짝이던 검은 눈동자는 빛을 잃었고, 안면은 공포와 고통으로 일그러져 있었다.

“소군아. 내 아들아.”

거칠고 커다란 손이 청년을 얼굴을 매만진다. 피부를 타고 침투한 강렬한 독기를, 자연스럽게 일어난 공력이 막아섰다.

“어찌 이리되었느냐?”

장년인은 한탄했다. 천애 고아로 자라 무림에서의 수십 년.

많은 사람을 만났고, 많은 사람을 떠나보냈다. 약관의 풋내기 낭인이 일문(一門)의 주인이 되기까지, 그런 기억들이 셀 수도 없다.

“고통스러웠느냐? 원통해서 눈도 감지 못했느냐?”

아들의 부릅뜬 눈을 가만히 내려다보며 물었다. 실핏줄이 다 터져 나가 붉게 물든 눈동자다.

이제 겨우 약관. 독살당한 아들을 앞에 둔 아버지의 눈에서 피눈물이 흘렀다.

“아들아.”

손을 통해 침투한 독기가 내부 곳곳으로 퍼져 나가고 있었다. 불과 몇 번의 호흡 만에 머리가 핑 돌고 사지가 저려 온다. 이런 극독이라니. 전신이 굳어 몸부림조차 치지 못했을 아들의 모습이 눈에 선했다.

“이 고통을 기억하마.”

다음 순간, 강대한 공력이 들불처럼 일어나 독기를 몰아붙였다. 마치 수백 마리의 이리 떼에 물어뜯긴 것처럼, 내부를 잠식해 가던 독기는 순식간에 소멸했다.

“그놈들에게 백배 천배로 갚아 주마.”

항산검문주, 혈랑검(血狼劍) 이천백은 아들의 시신을 뒤로하고 걸었다. 전각의 문을 열자 검은 밤하늘과 그 아래 일렁이는 횃불들이 보였다.

철저히 무장한 이백여 명의 무리. 그중 선두에 자리한 사내가 고개를 숙였다.

“아버님.”

이천백은 자신의 장자(長子)에게 고개를 끄덕여 보였다.

“가라. 오늘이…… 복수의 시작이다.”

그날 밤, 이백여 명의 무사가 항산검문을 빠져나왔다.
```

### Current accepted English

```markdown
# Chapter 20

The hour-long negotiation was finally entering its closing phase.

“Half the shops owned by the Mount Heng Sword Sect. And exclusive rights to the pleasure district. Is that correct?”

“Without a doubt. And your sect?”

“From this moment onward, we will not sell information to any sect in Shanxi other than the Jin Family of Taiyuan. We will also devote all our resources to gathering and delivering information about the war.”

The terms had already been decided after dozens of rounds of push and pull.

Jin Wikyung and Wolhwa carefully checked everything one last time for loopholes, then drew up and exchanged the document.

“We’re officially in the same boat now. I look forward to working with you, Lesser Family Head.”

“Likewise.”

That was when they shook hands.

Ding.

> **System**
>
> - The **Jin Family of Taiyuan** and the **Lower District Sect** have formed an alliance.
>
> - The alliance will remain in effect for the duration of the war.

Even this showed up. Then again, a similar notification had appeared when the war with the Mount Heng Sword Sect began.

*With the Lower District Sect joining in, have our odds of winning gone up a little?*

The Lower District Sect specialized in information.

Wolhwa had confidently claimed that all the information in Shanxi passed through her hands. If that was true, their assistance would be enormous.

*Nothing is more important than information.*

I didn’t know how things worked in Murim, but I knew that much. Information could become anything depending on how it was handled. A sword, a shield, or sometimes even a bomb capable of turning the tide in a single stroke.

It would be nice if Wolhwa brought us information like that.

“Then I’ll be taking my leave.”

“Please understand that you cannot go far while there are eyes on us.”

“Of course.”

*It’s finally over.*

Wipeng bowed with his usual impassive expression, and I gave an awkward half-bow of my own.

“Goodbye.”

Wolhwa’s eyes curved like crescent moons when she looked at me.

“Young Master Jin is coming with me.”

“Huh?”

“You’re not going to see me off?”

“…Why would I?”

“Because we spent a hot night together?”

That full-force fastball straight to the body left me momentarily stunned. No, seriously. I’d told this woman to bring information, so why was the first thing she was spreading this kind of adults-only information?

And in front of everyone, too.

“Oh?”

“A hot, hot night? Together?”

Wipeng looked back and forth between Wolhwa and me with interest, while an earthquake shook Jin Wikyung’s pupils.

“Taekyung, is that true? Is it really true?”

After a long silence, I answered.

“I’ll see her out.”

I grabbed Wolhwa by the wrist and dashed out. Behind me, Jin Wikyung’s mournful voice echoed through the hall.

“Little brother!”

* * *

Wolhwa was a rare beauty. Her slender figure, combined with her extravagant clothing, made it impossible for people not to stare.

“Did the family have a beauty like that?”

“Of course not. She’s an outsider.”

“An outsider?”

“Yeah. According to a friend among the gate guards, she’s a courtesan from Honghwaru.”

“Ah, that Honghwaru everyone says is ridiculously expensive. I know the place. Wait, but why would a courtesan come here?”

“They say she came to collect an unpaid tab from the Third Young Master. She probably wants to collect the money before the war turns into a full-scale conflict.”

“…Huh. The Third Young Master really gets up to all kinds of things, doesn’t he?”

The people’s whispers wormed into my ears. Wolhwa, who had been walking ahead of me while humming, suddenly turned around.

“Young Master Jin, why are you walking so far behind?”

I answered in a sullen tone.

“If we walk together, people will get the wrong idea. There are already all kinds of rumors going around…”

“Oh, the unpaid tab?”

Yeah. That.

“That rumor isn’t actually false.”

Wolhwa smiled brightly.

“When the gate guards asked why I came, I simply told them I was here to collect an unpaid tab. It’s not an outright lie.”

“What?”

“Were you planning to announce our alliance to the whole world?”

“…No.”

Why did she have to use my name? My image was already a complete disaster.

If rumors like this spread while we were in the middle of a war, I’d have no way to deny them. My reputation as a piece of trash would be set in stone.

“Considering you’ve already been falsely accused of poisoning someone, being a kept man is comparatively mild. Given your usual behavior, people will believe it.”

That was strangely persuasive. I nodded without thinking, then sensed something off in Wolhwa’s words.

“Falsely accused?”

Now that I thought about it, she had never once mentioned Lee Seogeun. She had adjusted the negotiations like a fastidious businesswoman, then formed an alliance as if it were the most natural thing in the world.

*What exactly is she relying on?*

Wolhwa gave a small smile at my suspicious look.

“Young Master Jin, have you forgotten who I am?”

“The Lower District Sect’s Shanxi Branch Leader…”

My eyes flew open.

Information. She had information.

Information proving I wasn’t the culprit.

I quickly moved alongside Wolhwa.

“Can you clear my name? Do you really have information like that?”

The war had begun with Lee Seogeun’s poisoning. If we could prove that all of this was a conspiracy carried out by someone else, we could stop the war.

But that hope was shattered by Wolhwa’s next words.

“No. I don’t.”

What?

“Then why did you form an alliance with us?”

“Because I’m a merchant.”

Wolhwa continued in a light, cheerful tone.

“We of the Lower District Sect are merchants at heart. We move strictly according to profit and loss.”

“If that’s the case, this makes even less sense.”

“Oh? Why?”

“Because the Mount Heng Sword Sect is stronger than we are. If you’re weighing profit and loss, shouldn’t you be siding with them?”

“You’re honest. No, perhaps I should say naïve.”

Wolhwa snickered.

“This is an investment. It’s the result of placing both sides on a scale and analyzing them coldly.”

“So as long as you profit, it doesn’t matter? Even if I really did poison Lee Seogeun?”

“Young Master Jin, what do you think it means that the Lower District Sect’s Shanxi branch devoted all its resources to investigating this, yet still couldn’t verify the truth?”

I hesitated, but Wolhwa didn’t wait for an answer.

“It’s simple. Either Young Master Jin is truly innocent, or you concealed it so perfectly that even we couldn’t uncover it.”

“Ah.”

“Either way, I don’t lose. If the former is true, then you have legitimacy, which is enough for us. If the latter is true, then it proves the Jin Family of Taiyuan is that capable.”

I was more than a little surprised. So that was one way of looking at it.

Thorough profit-and-loss calculation. I finally understood exactly what Wolhwa meant when she called herself a merchant.

The fact that someone like her was on our side gave me a reassuring feeling.

But…

“You’re overlooking one important thing. If I’m innocent, then who actually poisoned Lee Seogeun?”

That was the heart of the war. The biggest piece of the puzzle—one Wolhwa had failed to find.

If the Lower District Sect had discovered the culprit’s identity, she would have brought that information today.

Wolhwa sighed.

“I’m ashamed to say that nothing has been uncovered yet. But our sect is doing its best. Ah, we’re almost there.”

There were still plenty of things I wanted to ask, but I had no choice but to fall silent when I noticed the approaching gate guards.

*Our alliance with the Lower District Sect is still a secret.*

A four-horse carriage, apparently the one Wolhwa had arrived in, came into view, surrounded by gate guards in a wide circle. The strange tension around it reached us even from here.

*Did something happen?*

I sent internal energy through my eyes and ears. Soon, my enhanced senses picked up the gate guards’ tense voices.

“He’s a master. No doubt about it. At least Super First Rate, maybe even Peak. See the whip at his waist? He must be someone who handles a whip like a ghost.”

“A master of that level volunteering to be a coachman? A peerless beauty really is different.”

The martial artists speaking to each other sounded fairly experienced, and their voices were deadly serious. A younger martial artist cautiously murmured:

“But for someone like that, doesn’t his posture have too many openings? He’s thin, too…”

The senior martial artists clicked their tongues.

“Kid, this fellow and I have ten years of experience at the gate-watch office. We can tell from a person’s eyes alone. What the hell would a little shit like you know, butting into your elders’ conversation?”

“Tsk. Openings? You call that an opening? Can’t you see the ease and naturalness that only masters possess?”

“Then what about his temples? Masters with profound internal energy have bulging temples.”

“That’s just Returning to the Origin…”

Unfortunately, the conversation ended there. The gate guards noticed us standing blankly in front of the main gate and scattered.

Thanks to them, I learned the identity of the Peak master who handled a whip like a ghost—the romantic martial artist who had volunteered to be a coachman after falling for Wolhwa’s beauty.

“Young Master, do you remember me?”

“…”

As if I could forget.

That heavy voice. The sharp eyes of a true master.

He was the coachman who had brought me to the Jin Family of Taiyuan a few days ago.

I never expected to see that face here. I was momentarily speechless, and Wolhwa spoke up.

“I hear you two are acquainted. Last time, you crossed life and death together and formed a deep friendship that transcended age and status…”

*No. That isn’t what happened. Please stop.*

I tugged at Wolhwa’s sleeve, but it was already too late. The coachman opened his mouth with a gentle smile.

“Even now, if I close my eyes, the memories of that day remain vivid. The Heavenly Axe… He was a truly strong bastard.”

The gate guards, who had been listening intently, let out exclamations.

“Oh!”

“The Heavenly Axe… Surely he means that Heavenly Axe of the Eighteen Strongholds of Green Forest?”

“Wasn’t he the infamous Peak master of Green Forest? To kill a man like that, as expected, this gentleman must be…”

“…”

They seemed to have gotten something seriously wrong.

I had no idea where to start correcting them—or where to stop.

While I stood there blankly, the coachman grabbed me in a hug.

“If it weren’t for you, Young Master, I would have been in serious trouble.”

This man had a strange way of putting things. Without me, he would have been drinking a cup of makgeolli at the top of Mount Beimang.[^1]

“Please let go of me first, then we can talk…”

That was when I was just about to pry him off.

“Yama Whip. The master of the whip arts who vanished without a trace more than ten years ago. It’s him. It has to be.”

A ripple passed through the gate guards at someone’s mutter.

“Yama Whip? You mean that Peak master who traveled the realm beating down remnants of the Demonic path?”

“I’ve heard that name, too. A master standing between the orthodox and unorthodox paths, with no known sect or past… Come to think of it, wasn’t the place where his trail disappeared somewhere near Shanxi?”

“Then the Third Young Master—no, our Young Master—is acquainted with Great Hero Yama Whip.”

“And not only that. He must have played a major role in taking down the Heavenly Axe.”

“Oh! Ohhh!”

Hot, admiring gazes poured in from every direction. Perhaps sensing that something was wrong, the coachman tried to pull away, but my hand was gripping his shoulder tightly.

“Young Master?”

I gave him the brightest smile in the world.

“To meet you again like this—Yama. Whip. Great Hero!”

My words had the effect of throwing oil onto a fire.

“Woooah!”

The overheated gate guards stomped their feet, while Wolhwa bent over, desperately trying to hold back her laughter.

Ding.

> **System**
>
> - Rumors about the **Poisoner** are dying down!
>
> - Rumors about the **Sleeping Dragon of Shanxi** are gaining credibility!
>
> - **Fame** increases by 20!
>
> - Passionate supporters have appeared!

As the beautiful System notifications rang out, I remembered a famous saying.

*The perfect lie… is a true story.*

* * *

The young man stared at the ceiling with his eyes wide open. The light had gone out of his once-bright black eyes, and his face was twisted with fear and pain.

“Seogeun. My son.”

A large, rough hand caressed the young man’s face. The intense poisonous energy that had seeped in through the skin was stopped by internal energy that surged up instinctively.

“How did this happen to you?”

The middle-aged man lamented.

He had grown up a complete orphan and spent decades in Murim.

He had met countless people and watched countless people leave. From the days when he was a green twenty-year-old wandering martial artist to the moment he became the master of a sect, his memories were beyond counting.

“Did it hurt? Were you so bitter you couldn’t even close your eyes?”

He quietly looked down at his son’s wide-open eyes. Every blood vessel had burst, staining the irises red.

He was barely twenty. Blood tears flowed from the eyes of a father who stood before his poisoned son.

“My son.”

The poisonous energy that had entered through his hand was spreading throughout his body. Within only a few breaths, his head began to spin and his limbs went numb.

Such a deadly poison.

He could vividly picture his son’s final moments—his entire body stiffening until he couldn’t even struggle.

“I’ll remember this pain.”

The next moment, powerful internal energy rose like a wildfire and drove the poisonous energy away. The poison that had been consuming his insides vanished in an instant, as if it had been torn apart by a pack of hundreds of wolves.

“I’ll make them pay a hundred times over. A thousand.”

The Sect Leader of the Mount Heng Sword Sect, Blood Wolf Sword Lee Cheonbaek, left his son’s corpse behind and walked away.

When he opened the pavilion door, he saw the black night sky and the torches flickering beneath it.

A group of about two hundred fully armed men stood outside. The man at the front bowed his head.

“Father.”

Lee Cheonbaek nodded at his eldest son.

“Go. Tonight… is the beginning of our revenge.”

That night, about two hundred martial artists left the Mount Heng Sword Sect.

[^1]: A Korean image for being dead; Mount Beimang is the legendary mountain of the afterlife.
```
## Chapter 21

### Korean source

```text
＃21화



띠링.



- [진가심법]을 수련했습니다.

- 반복 수련의 결과로 근맥과 근골이 1씩 상승합니다.



“후우.”

심호흡과 함께 눈을 떴다. 어스름한 새벽, 촛불로 밝힌 방 안은 호박빛으로 출렁이고 있었다.

‘이번에도 실패.’

고요 속에서 주먹이 불끈 쥐어진다.

몇 번째 시도였을까. 스무 번? 서른 번? 중요한 건 결과다. 이번에도 굳은 공력을 끌어내는 것에 실패했다.

‘그나마 나아지고 있다는 걸 위안 삼아야 하나?’

공력을 다루는 것에 점점 익숙해지고 있다. 내가 F급 헌터가 아니라 C급. 아니 최소 D급만 되었어도 훨씬 빨리 적응했겠지만, 현실은 냉혹한 법이다.

‘근골, 근맥이 꾸준히 향상되는 덕분인 것도 있겠지.’

공력은 인체의 혈을 타고 흐른다. 심법을 수련하면 할수록, 근골과 근맥이 향상되면 될수록 혈이 넓어지고 튼튼해진다. 처음과 비교하면 보다 더 많은 공력을, 훨씬 빠른 속도로 순환시킬 수 있었다.

‘스킬 포인트 덕분이지.’

레벨 업 한 번에 10씩 주어지는 스킬 포인트는 그 역할을 톡톡히 하고 있었다. 근골과 근맥을 향상시키는 데에는 그만한 양분이 없다.

‘스킬창 오픈.’



스킬창



[LV.17 진태경]

심법 : 진가심법 (사 성)

무공 : 진가창법 (오 성) / 진가보법 (오 성)

근골 : 105

잔여 포인트 :  0





‘가능성이 보인다.’

난공불락의 요새가 점점 작고 허술해지고 있다. 계속해서 두드리다 보면 곧 문을 열 수 있을 것 같은 느낌이다.

다행히 내가 재능은 없어도 끈기는 있는 놈이지.

‘계속 시도한다. 될 때까지.’

다시 가부좌를 틀고 운기조식을 시작하려던 찰나였다.

앞서 수차례의 운기조식 덕분에 잔뜩 곤두선 감각들 사이로, 심상치 않은 소리가 들려왔다.

‘이건…….’

웅웅웅. 언뜻 들으면 벌 떼 우는 소리처럼 들리는 그것은 사람들의 웅성거림이었다.

‘무슨 일이지?’

귓가로 공력을 흘려보냈다. 거리가 멀어서 그런지 완전히 알아듣기에는 턱없이 부족했다. 하지만 그것으로도 충분했다.

웅얼거리는 목소리들 사이에서 한 단어를 들었으니까.

‘전투!’

항산검문이다. 드디어 전투가 벌어진 것이다.

나는 황급히 가부좌를 풀고 일어섰다. 그리고 반쯤 열린 창문 너머로 뛰어내렸다.

고양이처럼 착지한 내 시야에, 차례차례 불이 밝혀지는 전각들이 들어왔다.

‘결국…….’

시작됐구나.



* * *



스물다섯. 가지런히 눕힌 시신의 숫자였다.

모든 생기를 잃은 채 고목처럼 누워 있는 그들을 확인했을 때, 할 말을 잃고 말았다.

“이건.”

나는 헌터다. 무수한 전투를 겪었고 죽음을 지켜봤다.

중독되고, 베이고, 으스러지고, 터지고…….

상대하는 몬스터에 따라 죽음의 종류도 천차만별이다. 하지만 그들에게는 한 가지 공통점이 있었다.

바로 ‘성인’이라는 것.

그건 각성의 기본 조건이었다. 어떤 기준인지, 왜인지는 아무도 몰랐다. 게이트의 존재만큼이나 자연스럽게 자리 잡은 법칙이었다.

그래서 내가 목격한 그 숱한 죽음들 중에는 어린아이의 죽음이 포함되어 있지 않았다.

‘이건 게임이다. 고작 게임이라고.’

마음속으로 계속해서 중얼거렸다. 그러나 단순히 그렇게 치부하기에는 눈앞의 광경이 너무나도 참혹했다.



혈血



이마에 아로새겨진 글자. 말라붙은 핏물 위로 횃불이 비친다. 열 명이 넘는 어린아이들이 그렇게 싸늘하게 식어 있었다.

기껏해야 중학생. 혹은 그 밑으로 보이는 아이들까지 하나도 빠짐없이. 그렇게 죽어 있었다.

“우웁!”

떨리는 손으로 횃불을 들고 있던 무사 하나가 허리를 숙이는 것을 시작으로 곳곳에서 토악질 소리가 울려 퍼졌다.

그때 무사가 떨어트린 횃불을 집어 드는 손이 있었다.

“소미. 분명 그런 이름이었지. 내가 가주 대행이 되던 날, 응현 지부장이 자신의 보물이라며 침이 마르게 자랑했었다.”

진위경이다. 그는 꺼질 듯한 눈동자로 횃불을 들어 아이들의 얼굴을 비췄다. 한 사람. 한 사람. 얼굴이 드러날 때마다 어김없이 각자의 이름이 흘러나왔다.

마지막 아이의 이름을 부른 진위경이 나를 바라봤다.

“이 아이들이 누군지 아느냐?”

“……모릅니다.”

“응현(應現), 산음(山陰), 삭주(朔州) 지부에 파견된 본가의 식솔들이다.”

그곳이 어디인지 나는 모른다. 하지만 이 아이들의 부모들이 어떤 최후를 맞았을지는 짐작할 수 있었다.

더불어 항산검문의 의도에 구역질이 났다.

‘미친 사이코패스 새끼들.’

봐라, 우리는 이런 어린아이까지도 참혹하게 죽일 수 있다. 곧 너희도 이처럼 될 것이다.

얼굴도 모르는 항산검문주의 목소리가 들리는 듯했다.

“모든 게 내 탓이다. 무공을 모르는 아이들까지 이리 참혹하게…….”

진위경이 떨리는 목소리로 자책하던 그때였다.

“그것이 전쟁의 본질이오. 소가주.”

대장로가 은빛 수염을 매만지며 나타났다. 시신들을 바라보는 그의 눈동자는 담담하게 가라앉아 있었다.

“승리와 패배. 둘 중 어디에도 죽음은 빠지지 않는 법. 항산검문주. 혈랑검 이천백이라고 했나? 그는 낭인 출신답게 전쟁을 잘 알고 있소. 이 아이들만 봐도 알 수 있지.”

그 대수롭지 않다는 말투에 나는 소름이 돋았다.

‘어떻게 돼먹은 인공지능이야.’

이 NPC는 어딘가 결여되어 있다. 그래서 더욱 위험하게 느껴진다.

나는 입을 다물었고, 진위경은 일그러진 얼굴로 입을 열었다.

“……말을 삼가시지요. 본가의 식솔들입니다.”

“아니, 저 아이들은 전사자요. 앞으로도 무수한 이들이 죽어 나가겠지. 어쩌면 지금 이 순간에도.”

“대장로. 말을 삼가라 했습니다.”

진위경이 으르렁거렸다. 사람들의 눈만 없었다면 진작 일을 냈을 기세였다. 하지만 대장로는 여전히 담담했다.

“예상하지 못했느냐?”

갑작스러운 하대였다. 하지만 나도, 진위경도 인식하지 못할 정도로 자연스러웠다.

“산음, 응현, 삭주. 모두 항산검문의 손이 닿는 곳이었다. 전날 각 지부에 전서구를 보내면서 이런 일이 벌어질 수 있음을 전혀 염두에 두지 않았단 말이냐?”

“그건…….”

“너는 알고 있었다. 그들에게 화가 미치리라는 사실을 말이다. 전서구를 보냈던 건 단순한 양심의 가책이었을 뿐이지.”

“그만. 그만하십시오.”

“훌륭한 판단이었다. 만약 지부를 구원하고자 했다면 쉬지 않고 칠 주야를 달려야 했을 것이고, 극도로 지친 상태에서 적과 싸워야 했을 테니까. 그렇지 않으냐?”

진위경은 하얗게 질린 얼굴로 대장로를 바라봤다. 꽉 쥔 주먹 사이로 선혈이 흘렀다.

“난, 나는…….”

“모든 것에는 희생이 따르는 법. 대국을 직시해라. 너는 태원진가의 수백 식솔을 책임질 소가주다.”

진위경의 몸이 부르르 떨렸다. 분노와 슬픔이 빠져나간 표정에는 왠지 모를 허탈함이 가득했다.

“희생…….”

“전쟁은 이제 막 시작되었을 뿐이오. 안 그렇소? 소가주.”

포권을 취해 보이는 대장로의 모습에, 나는 입술을 질끈 깨물었다.

‘종잡을 수 없는 노인네.’

대장로는 분명 위험한 인물이다. 가문에서의 위치, 도무지 짐작할 수 없는 속내, 어린아이들을 시체를 보고도 눈썹 하나 깜짝하지 않는 사이코패스적인 면모까지.

하지만…….

‘그의 말이 맞아.’

내 시선에서 진위경은 좋은 소가주다. 인간미도 넘치고 머리도 영특하다.

하지만 시신들을 보는 순간, 누구보다 크게 흔들렸다. 대장로의 싸늘한 일침이 아니었다면 평정심을 되찾기까지 상당한 시간이 걸렸을 것이다.

‘도움을 줬다. 다른 누구도 아닌, 바로 그 대장로가…….’

평화로울 때는 적대 관계지만 전쟁 시에는 뭉친다는 건가?

‘그럼 다행인데.’

의심과 안도가 섞인 눈초리로 대장로를 바라보던 그때였다.

“삼공자도 있었군.”

노회한 잿빛 눈동자에 가슴이 덜컥 내려앉았다. 처음으로 대장로가 내게 말을 걸어온 것이다.

“대장로를 뵙습니다.”

애써 당황을 숨기는 나를 대장로가 묘한 미소를 띠고 바라봤다.

“요새 가문 내에 재미있는 소문이 들리던데, 그게 아마…… 산서잠룡이라던가?”

저 웃기지도 않는 별명을 대장로에게서 들을 줄이야.

“일설에 의하면 염라편과 친분이 있다고도 하더군. 그와 힘을 합쳐 천력부를 쓰러트렸다던데.”

“쿨럭. 쿨럭.”

“어디 아픈가?”

“아, 아닙니다. 그냥 몸이 으슬으슬해서요.”

“저런. 곧 큰 공을 세울 사람이 그래서야 쓰나.”

어색하게 웃던 내 얼굴이 천천히 굳어졌다.

“그게 무슨 말씀이신지.”

“천력부라는 걸출한 마두를 제거하는 데 일조한 실력자라면 귀중한 전력이지. 설마 그 소문이 거짓은 아닐 테고.”

“…….”

“해서, 본가의 직계로서 앞장서서 싸우는 건 당연한 의무라고 생각되는데. 소가주의 생각은 어떠시오?”

빙긋. 대장로의 웃음을 물끄러미 바라보던 진위경이 내게 물었다.

“네 생각은 어떠하냐?”

외통수. 한 단어를 떠올린 순간, 익숙한 알림이 울렸다.

띠링.



* * *



퀘스트



[임무 수행]

당신은 백호당 정찰조장으로 임명되었습니다.

지금부터 휘하에 배속된 부하들을 이끌고 임무를 수행, 공적을 쌓으십시오!



등급 : 반복 퀘스트

제한 : 진태경

임무 : 공적치 100 달성 (0 / 100)

보상 : 성공 정도에 따라 변화합니다.

실패 : 실패 정도에 따라 변화합니다.





퀘스트창을 껐다. 이미 몇 번이나 봤을뿐더러, 잠시 자리를 비웠던 백호당 소속 무사가 지금 막 돌아왔기 때문이었다.

“조장들에게 기본으로 지급되는 물품들입니다.”

검, 그리고 백호가 조잡하게 수놓아진 흑색 무복과 나무 냄새가 물씬 나는 반들반들한 목패(木牌).

그게 전부였다.

“새로 휘하에 배속된 이들은 정찰조 숙소에서 대기 중입니다. 위치는…….”

다행히 내가 아는 곳이었다. 몇 번 오가면서 봤던 전각이 바로 정찰조에 배정된 숙소였다.

백호당을 빠져나온 후 우선 인적이 없는 골목으로 숨었다.

‘인벤토리 오픈.’

모든 복장을 갖추는 데는 10초면 충분했다. 옷을 갈아입고, 검은 인벤토리 깊숙이 처박은 다음 [예리한 창]을 꺼냈다.

지금까지야 으리으리한 개인 전각에서 삼공자의 신분을 톡톡히 누렸지만 지금부터는 다르다.

‘공동 생활이랬지.’

먹는 것도, 자는 것도 함께다. 필요할 때마다 허공에서 2m짜리 철창이 튀어나오는 마술을 보여 줄 수는 없는 법이다.

조장이라고 음각된 목패를 허리춤에 차자 태원진가의 평범한 무사1이 된 것 같았다.

‘그냥 무사는 아니지. 정찰조장이니까.’

백호당 정찰조장. 생각지도 못한 직책을 받게 됐다.

물론 여기에는 나름 치열한 의견 대립이 있었다. 대장로는 나를 장로원 계열의 전투 부대에 넣고 싶어 했고, 진위경은 극렬하게 반대했다.

‘결국 타협을 봤지.’

임무 자체는 어렵지 않은 정찰조장. 하지만 장로원 일파인 백호당주의 휘하로. 결국 어어, 하는 사이에 이런 직책을 받게 됐다.

‘이런 식으로 전쟁에 끼게 될 줄은 몰랐는데.’

배 째라 식으로 나갈 수도 있었지만 참았다. 염라편을 언급할 때마다 번뜩이는 대장로의 눈빛이 첫 번째 이유였고, 두 번째 이유는…… 어린아이들 때문이다.

‘게임이다. 전부 그래픽이고 허상일 뿐이야.’

수없이 되뇌어도 그 시신들이, 이마에 칼로 새겨진 글자가 눈앞에 어른거렸다. 맞다. 이 결정에는 감성적인 부분도 있었다.

이대로라면 좋지 않다.

‘몰입하지 말자. 현실과 게임을 혼동해서는 안 돼.’

언젠가부터 부쩍 그런 일들이 많아졌다. 처음에는 재미 삼아 NPC들을 사람처럼 대했던 것이, 요즘 들어서는 정말 사람이라고 생각하고 관계를 맺고 있었다.

그럴 때마다 깜짝깜짝 놀라곤 한다. 이것도 게임을 오래 하다 보니 생긴 부작용일지도 모르지.

“여긴가?”

어느새 정찰조의 숙소에 도착한 나는 입을 벌렸다.

갈라진 목재와 쾌쾌한 냄새. 세상에, 처마 밑에는 벌집까지 있다. 저렇게 큰 건 또 처음 본다.

‘역시 가족 같은 기업…….’

복지 수준 봐라. 아니, 어쩌면 날 싫어하는 백호당주의 심술일 수도 있겠다. 대놓고 갈구는 건 아직 못 하겠고, 엿 좀 먹어 보라 이건가.

‘그래, 일단 해 보자.’

크게 심호흡한 나는 문을 열고 한 발을 내딛었다.

끼이이익. 오래된 바닥이 울부짖는 소리가 유난히 불길했다.
```

### Current accepted English

```markdown
# Chapter 21

Ding.

> **System**
>
> - Practiced the **Jin Family’s Cultivation Technique**.
>
> - As a result of repeated practice, **Sinews** and **Bones** each increase by 1.

“Whew.”

I opened my eyes, exhaling deeply. Before dawn, the candlelit room glowed amber in the darkness.

*Failed again.*

I clenched my fist.

How many times had I tried? Twenty? Thirty? The result was what mattered. Once again, I had failed to draw out the condensed internal energy.

*Should I take comfort in the fact that I’m getting better?*

I was gradually getting used to handling internal energy. If I had been a C-rank Hunter instead of an F-rank—or at least a D-rank—I would have adapted much faster. But reality was cold and unforgiving.

*My Sinews and Bones improving steadily must be helping, too.*

Internal energy flowed through the body’s meridians. The more I practiced a cultivation technique, and the more my Sinews and Bones improved, the wider and sturdier those pathways became. Compared to when I had started, I could circulate more internal energy at a much faster speed.

*It’s all thanks to the Skill Points.*

The ten Skill Points awarded with every level-up were doing their job well. Nothing could nourish my Sinews and Bones better.

*Open Skill Window.*

> **Skill Window**
>
> **Lv. 17 Jin Taekyung**
>
> **Cultivation Technique:** Jin Family’s Cultivation Technique (Fourth Stage)
>
> **Martial Arts:** Jin Family’s Spear Technique (Fifth Stage) / Jin Family’s Manoeuvre Technique (Fifth Stage)
>
> **Sinews and Bones:** 105
>
> **Remaining Points:** 0

*I can see the possibility.*

The impregnable fortress was cracking and crumbling. If I kept pounding away at it, I felt as if I could open the gate soon.

Fortunately, I might lack talent, but I had persistence.

*I’ll keep trying. Until it works.*

I was just about to sit cross-legged and begin circulating my qi again when it happened.

My senses, sharpened by the earlier rounds of circulating my qi, picked up an unusual sound.

*This is…*

A low, droning hum. At first, it sounded like a swarm of bees, but it was actually the murmur of many people.

*What’s going on?*

I let internal energy flow to my ears. Perhaps because of the distance, I couldn’t make out everything clearly. But I heard enough.

One word stood out among the indistinct voices.

*Battle!*

The Mount Heng Sword Sect. The battle had finally begun.

I hurriedly uncrossed my legs and stood. Then I leaped through the half-open window.

I landed like a cat. Before me, the pavilions lit up one by one.

*In the end…*

It had begun.

* * *

Twenty-five.

That was the number of corpses laid out in orderly rows.

When I saw them lying like dead trees, every trace of vitality gone, I was left speechless.

“This is…”

I was a Hunter. I had fought countless battles and witnessed death countless times.

Poisoned, cut apart, crushed, blown apart…

The kinds of death varied wildly depending on the monster involved. But all those deaths had one thing in common.

They were all adults.

That was one of the basic conditions for awakening. No one knew what the standard was or why it existed. It was a law as naturally established as the existence of Gates.

That was why none of the countless deaths I had witnessed had involved a child.

*This is a game. It’s just a game.*

I kept repeating the words to myself. But the sight before me was too horrific to dismiss so simply.

**BLOOD**

The character had been carved into their foreheads. Torchlight reflected off the dried blood.

More than ten children had gone cold like that.

They were middle-school age at most. Some looked even younger. Every single one of them was dead.

“Urgh!”

One of the martial artists, holding a torch in a shaking hand, doubled over, and soon the sound of retching rang out from all around us.

Then a hand reached down and picked up the torch he had dropped.

“Somi. That was definitely her name. On the day I became acting Family Head, the Branch Leader of Eung-hyeon bragged about her endlessly, calling her his treasure.”

It was Jin Wikyung. With eyes that seemed ready to go out, he lifted the torch and illuminated the children’s faces.

One by one.

As each face was revealed, he unfailingly spoke its name.

After naming the last child, Jin Wikyung looked at me.

“Do you know who these children are?”

“…No.”

“They were members of our family sent to the branches in Eung-hyeon, Saneum, and Sakju.”

I didn’t know where those places were. But I could guess what end the children’s parents had met.

And I was sickened by the Mount Heng Sword Sect’s intentions.

*Those lunatics. Those fucking psychopaths.*

*Look. We can slaughter even children this young. Soon, you’ll end up the same way.*

I could almost hear the voice of the Mount Heng Sword Sect’s Sect Leader, whose face I had never seen.

“This is all my fault. To slaughter even children who don’t know martial arts so cruelly…”

Jin Wikyung was blaming himself in a trembling voice when—

“That is the essence of war, Lesser Family Head.”

The Head Elder appeared, stroking his silver beard. His gaze was calm as he looked over the corpses.

“Victory and defeat—neither comes without death. The Mount Heng Sword Sect’s Leader—Blood Wolf Sword Lee Cheonbaek, was it? As one would expect of a former wandering martial artist, he understands war well. These children alone make that clear.”

The casual way he said it sent a chill through me.

*What the hell is wrong with this AI?*

This NPC was missing something. That made him feel even more dangerous.

I kept my mouth shut, while Jin Wikyung spoke with a twisted expression.

“…Please choose your words carefully. They are members of our family.”

“No. Those children are casualties of war. Countless more will die from now on. Perhaps even at this very moment.”

“Head Elder. I told you to watch your words.”

Jin Wikyung growled. Had we been alone, he would have been ready to start something right then and there.

But the Head Elder remained calm.

“Did you not anticipate this?”

He had suddenly switched to informal speech, yet it was so natural that neither Jin Wikyung nor I even registered it.

“Saneum, Eung-hyeon, Sakju. All of them were places within the Mount Heng Sword Sect’s reach. When you sent messenger pigeons to the branches the day before, did you truly not consider that something like this might happen?”

“That…”

“You knew harm would come to them. Sending those pigeons was nothing more than a way to ease your conscience.”

“Enough. Please, enough.”

“It was an excellent decision. If you had wanted to save the branches, you would have had to run for seven days and nights without rest, then fight the enemy in a state of extreme exhaustion. Isn’t that right?”

Jin Wikyung stared at the Head Elder with a pale face. Fresh blood flowed between his tightly clenched fingers.

“I—I…”

“Everything comes with a sacrifice. Look at the bigger picture. You are the Lesser Family Head responsible for the hundreds of family members of the Jin Family of Taiyuan.”

Jin Wikyung’s body trembled. The anger and sorrow had drained from his face, leaving it filled with a strange emptiness.

“Sacrifice…”

“The war has only just begun. Isn’t that so, Lesser Family Head?”

The Head Elder made a respectful fist-and-palm salute. I bit down hard on my lip.

*What an impossible old man to figure out.*

The Head Elder was clearly dangerous. His position in the family, his utterly unreadable motives, and even his psychopathic side—he didn’t so much as twitch an eyebrow while looking at the corpses of children.

But…

*He was right.*

From my perspective, Jin Wikyung was a good Lesser Family Head. He was deeply humane and sharp-minded.

But the moment he saw the corpses, he had been shaken more than anyone. Without the Head Elder’s cold rebuke, it would have taken him a long time to regain his composure.

*He helped. The Head Elder, of all people…*

*Were they enemies in peacetime but united during war?*

*Then that’s fortunate.*

I was looking at the Head Elder with a mixture of suspicion and relief when he spoke.

“So the Third Young Master is here as well.”

My heart dropped at the sight of those shrewd gray eyes. It was the first time the Head Elder had spoken to me.

“Greetings, Head Elder.”

The Head Elder looked at me with a strange smile as I did my best to hide my surprise.

“I’ve been hearing an interesting rumor within the family lately. Something about… the Sleeping Dragon of Shanxi?”

I never expected to hear that ridiculous nickname from the Head Elder.

“I’ve also heard that you are acquainted with Yama Whip. They say you joined forces with him to defeat the Heavenly Axe.”

“Cough. Cough.”

“Are you ill?”

“N-no. I’m just feeling a little chilly.”

“Oh dear. That won’t do for someone who is about to accomplish great things.”

My awkward smile slowly froze.

“What do you mean?”

“Someone capable of helping eliminate an exceptional demon like the Heavenly Axe is a valuable asset in battle. Surely that rumor isn’t false.”

“…”

“Therefore, as a direct-line member of our family, I believe it is only natural that you take the lead in battle. What do you think, Lesser Family Head?”

The Head Elder smiled faintly. Jin Wikyung, who had been gazing at that smile, asked me,

“What do you think?”

I was cornered.

The moment the word came to mind, a familiar notification rang out.

Ding.

* * *

> **System**
>
> **Quest**
>
> **Mission**
>
> You have been appointed reconnaissance squad leader of White Tiger Hall.
>
> From now on, lead the subordinates assigned under you on missions and build merit!
>
> **Grade:** Repeating Quest  
> **Restriction:** Jin Taekyung  
> **Mission:** Achieve 100 Merit (0 / 100)  
> **Reward:** Changes according to the degree of success.  
> **Failure:** Changes according to the degree of failure.

I closed the Quest Window. I had already seen it several times, and besides, the White Tiger Hall martial artist who had been away for a while had just returned.

“These are the supplies issued to squad leaders.”

A sword.

A black martial uniform with a crude white tiger embroidered on it.

And a smooth wooden plaque that smelled strongly of fresh wood.

That was everything.

“The newly assigned members are waiting at the reconnaissance squad’s quarters. The location is…”

Fortunately, I knew the place. The pavilion I had passed several times was the quarters assigned to the reconnaissance squad.

After leaving White Tiger Hall, I first ducked into an empty alley.

*Open Inventory.*

Ten seconds was enough to put on the full uniform. I changed clothes, shoved the sword deep into my Inventory, then pulled out the *Sharp Spear*.

Until now, I had thoroughly enjoyed the privileges of being the Third Young Master in a lavish private pavilion.

But things were different from here on out.

*It’s communal living, right?*

We would eat together and sleep together. I couldn’t have a two-meter iron spear pop out of thin air whenever I needed one.

Once I hung the wooden plaque engraved with *Squad Leader* at my waist, I felt like I’d become Ordinary Martial Artist #1 of the Jin Family of Taiyuan.

*Not just an ordinary martial artist. I’m a reconnaissance squad leader.*

White Tiger Hall reconnaissance squad leader.

I had never expected to receive a position like this.

Of course, there had been some fierce disagreement over it. The Head Elder wanted to place me in a combat unit under the Elder Council faction, while Jin Wikyung had vehemently opposed him.

*In the end, we reached a compromise.*

The mission itself was easy enough, but I would be serving under the command of White Tiger Hall’s Leader, who belonged to the Elder Council faction.

Before I knew it, I had received this position.

*I never imagined this was how I’d get dragged into the war.*

I could have just told them to do whatever the hell they wanted, but I held back. The first reason was the Head Elder’s eyes, which flashed every time Yama Whip was mentioned.

The second reason was…

The children.

*It’s a game. It’s all graphics and nothing more than an illusion.*

No matter how many times I repeated that to myself, the corpses and the character carved into their foreheads kept flickering before my eyes.

Part of this decision had been emotional.

This wasn’t good.

*Don’t get immersed. I can’t confuse reality with the game.*

Things like this had been happening more and more often lately. At first, I had treated the NPCs like people for fun. But these days, I was actually thinking of them as real people and forming relationships with them.

Every time it happened, I was startled.

Maybe this was a side effect of playing the game for too long.

“Is this it?”

Before I knew it, I had arrived at the reconnaissance squad’s quarters, and my mouth fell open.

Cracked wood and a musty smell.

Good lord, there was even a beehive under the eaves. I had never seen one that big before.

*Just like a company that treats you like family…*

Look at those benefits.

Or maybe it was a mean-spirited prank by the White Tiger Hall Leader, who disliked me. Perhaps he couldn’t openly give me grief yet, so this was his way of telling me to eat shit.

*All right. Let’s give it a shot.*

I took a deep breath, opened the door, and stepped inside.

Creeeak.

The old floor let out a wailing sound that felt especially ominous.
```
## Chapter 22

### Korean source

```text
＃22화



방에 들어서자 곰팡이 냄새가 코를 찔렀다. 과거 군대 내무반을 연상시키는 그곳에 정찰조원들이 대기 중이었다.

‘열 명.’

나는 기감을 일으킴과 동시에 그들의 면면을 훑었다.

시선이 스쳐 갈 때마다 낯선 얼굴들 위로 레벨창이 불쑥불쑥 솟아오른다.

‘14레벨. 15레벨. 14레벨…….’

대부분이 비슷한 수준이었다. 그렇게 아홉 번째 인물로 넘어간 순간이었다.



[Lv.22 혁무진]



숫자가 훌쩍 뛰었다. 심지어 낯익은 얼굴이다.

‘혁무진?’

며칠 전 처음으로 태원진가에 도착했을 때 내게 시비를 걸었던 그 혁무진이 맞다. 시선이 마주치자 녀석이 입꼬리를 말아 올렸다.

“이렇게 또 뵙는군요. 삼. 공. 자.”

나는 적의가 드러나는 웃음을 빤히 쳐다보다 말했다.

“앞으로 조장님, 이라고 불러라.”

“……그리하지요.”

혁무진의 따가운 시선을 흘리고 열 번째 정찰조원을 바라봤다. 내가 처음 등장했을 때부터 환한 웃음을 짓고 있던 청년이 벌떡 일어났다.

“공자, 아니 조장님! 잘 부탁드립니다.”



[Lv.13 한엽]



전시 상황이다 보니 보직이 변경된 모양이다. 앞서 만난 백호당 서기는 정찰조 자체가 여러 곳에서 차출된 무사들로 구성되었다고 했다.

‘혁무진도 원래는 수문각 소속이니까.’

그래서인지 몰라도 방 안의 분위기는 어수선했다.

조원들은 낯선 이들끼리의 어색함과 전쟁에 대한 불안, 기대가 뒤섞인 표정들로 나를 바라보는 중이었다.

처음으로 입을 뗐다.

“백호당 정찰조장으로 임명된 진태경이다. 잘 부탁한다.”

짝짝짝. 누군가의 외로운 박수 소리는 불과 몇 초 만에 사그라지고 한엽이 무안한 얼굴로 손을 내렸다.

생각 이상으로 딱딱한 분위기다.

‘하지만 이것도 나쁘지 않지.’

지금은 전시 상황이다. 서로 웃으며 친목을 도모하는 것보다는 지금처럼 긴장감을 유지하는 게 낫다.

물론 그것도 과하면 독이 되고, 적당한 선에서 풀어 주는 게 조장인 내가 할 일 중 하나다.

‘그거야 뭐, 익숙하니까.’

처음 게이트에 입장한 초짜 헌터들은 말 그대로 얼어붙는다. 실전은 연습과 다르니까. 헌터 훈련소에서 배운 지식, 훈련은 우주 저 멀리 날아가고 원초적인 죽음의 냄새에 압도되는 것이다.

그래서 길드 내 베테랑들이 초짜의 멘탈 케어를 도왔는데, 나도 그중 하나였다.

‘그래 봤자 F급 전담이었지만.’

수준도 엇비슷하다. 내가 느낀 바로는 무림의 이류는 E급과 F급을 오가는 수준이니까.

그러니까 나는 열 명의 F급 파티를 이끄는 파티장이 된 셈이다. 내가 파티장이라, 해 본 적은 없었지만, 뭘 해야 하는지는 질리도록 봐 왔다.

“본인이 전투 경험이 있다. 거수.”

대뜸 던진 말에 정찰조 전원이 손을 들었다. 다들 어리둥절한 얼굴이다.

“5회 이상 전투를 겪었다. 거수.”

절반의 손이 내려갔다. 그중에는 한엽도 포함되어 있었다.

5회 이상 전투 경험자가 다섯 명이라. 이 정도면 나쁘지 않다. 아니, 기대 이상이다.

하지만 가장 중요한 마지막 질문이 남았다.

“살인 경험이 있다. 거수.”

힘없이 내려가는 네 개의 손. 나는 아직까지도 손을 들고 있는 유일한 정찰조원을 바라봤다.



[Lv.22 혁무진]



“얼마나 죽였지?”

녀석이 코웃음 쳤다.

“다섯. 작년 산적 토벌 때였소. 그중 하나는 부채주였고. 제법 강한 놈이었…….”

더 들을 것도 없이 말했다.

“좋아. 지금부터 네가 부조장이다.”

주절거리려던 혁무진의 입이 딱 다물어졌다.

“부조장?”

“어. 싫으면 지금 말해.”

초보들만 모인 지금, 무엇보다 중요한 건 경험자다.

망설임 없이 적에게 무기를 휘두를 수 있는 놈은 혁무진이 유일하다.

‘흑묘백묘.’

흰 고양이든 검은 고양이든, 싸가지 없는 고양이든 쥐만 잘 잡으면 장땡이지.

복잡한 얼굴로 생각에 잠겨 있던 혁무진이 대답했다.

“……흥. 명령이니까 어쩔 수 없군.”

부조장 하고 싶다는 말을 어렵게도 한다.

“그럼 혁무진이 부조장. 앞으로 부를 때는 일 호다.”

“일 호? 그건 또 뭐요?”

“번호 순서. 앞으로 정찰조는 이름 대신 번호로 통칭한다. 혁무진이 일 호. 그 다음에 저기 앉아 있는 너. 그래. 네가 이 호.”

일 호부터 십 호까지. 한 사람씩 가리키며 지명을 끝냈다.

혁무진이 눈살을 찌푸렸다.

“왜 그렇게 하는 거요?”

“이게 편하니까. 오늘 당장 전투가 벌어질지도 모르는데 하루 종일 이름만 외울래?”

“그건.”

“그럼 시키는 대로 해. 명령이다.”

굳은 얼굴로 나를 노려보는 혁무진을, 나는 피하지 않았다.

오히려 그때처럼 건방지게 나와 주기를 기대하는 마음도 있었다. 당장 며칠 안에 전투가 벌어질 수도 있는데 지금 같은 식이라면 곤란하다.

만약 덤빈다면 힘의 격차를 알려 줘야 한다. 확실하게.

“……명령에 따르겠소.”

“네가 뭐라고?”

“일 호, 일 호요.”

대답하는 혁무진의 목소리가 파르르 떨렸다. 생각보다 감이 좋은 놈이다. 산서잠룡에 관한 소문 때문인지도 모르고.

중요한 사실은 혁무진이 나에게 순응했다는 사실이다.

나는 내색하지 않고 말을 이었다.

“지금부터 하는 말이 낯설고 이상하게 들릴 수 있다. 하지만 참아. 그게 칼 맞아 죽는 것보다 낫잖아. 안 그래?”

혁무진만큼 대놓고 불만을 드러내진 않았지만, 다른 정찰조원들도 불안한 표정으로 나를 바라봤다.

한 사람만 빼고.

“저는 조장님 말씀을 따르겠습니다!”

한엽이 소녀 팬처럼 외쳤다. 차이점이 있다면 손에 아이돌 응원봉 대신 창이 들려 있다는 건데…….

‘아, 그렇지.’

나는 정찰조원들을 향해 씩 웃어 보였다.

“자, 본인이 검을 쓴다. 거수.”

파티 사냥의 핵심. 포지션 나누기다.



* * *



현실의 레이드 방식은 이미 교범화된 지 오래다.

탱커 셋. 딜러 넷. 마법사 둘과 힐러 하나. 10인 파티 기준으로 가장 이상적인 조합이다.

‘마법사, 힐러는 당연히 없고.’

탱커, 딜러만으로 최대한 균형을 맞춰야 하는데, 그런데…….

“……방패 쓸 줄 아는 사람이 없다고?”

충격적인 결과에 목소리가 떨렸다. 세상에, 딜러만 열 명이라니. 심지어 아홉이 검이고, 창은 한엽, 한 명밖에 없다.

‘이 무슨 끔찍한 단일종인가.’

차라리 혼종이 낫다. 그건 이것저것 섞여 있기라도 하니까.

혁무진이 뭐 잘못됐냐는 표정으로 말했다.

“사내라면 응당 검을 쥐어야지 않겠소.”

그 말에 고개를 끄덕이는 다른 놈들을 보니 기도 안 찬다.

‘아주 배가 불렀구먼. 배가 불렀어.’

피 웅덩이에 머리 박아 봐라, 저런 말이 나오나.

칼? 창? 그런 거 없다. 엉겁결에 잡은 돌멩이로 찍고, 흙 뿌리고 올라타서 이빨로 깨물고…….

사선(死線)에서는 손에 잡히는 게 무기고 생명줄이다.

기껏해야 산적들이나 상대해 왔던 이 녀석들은 아직 그걸 모른다.

‘당장 내일부터라도 연습시켜야 하나?’

저들을 위해서가 아니라, 내 생존을 위해서.

요령만 가르쳐도 난전에서는 확실한 효과를 발휘할 것이다.

‘7년 동안 개처럼 굴렀는데 초짜들 때문에 죽을 수는 없지.’

그런 생각을 할 때였다. 댕. 댕. 댕. 커다란 종소리가 세 번 울렸다.

개개인이 정확한 시간을 알 수 없는 이곳에서는 특정 시각마다 종을 치는데, 방금 울린 세 번의 종소리는 미시(未時:오후1~3시)가 되었다는 신호였다.

그리고…….

“준비해. 첫 출동이다.”

정찰조의 첫 임무를 알리는 신호탄이기도 했다.



* * *



“잘하고 있을 겁니다.”

위팽의 뜬금없는 말에 진위경이 고개를 들었다. 그는 방금까지 식어 가는 찻잔을 멍하니 바라보고 있던 중이었다.

“무슨 소린가?”

“삼공자 말입니다.”

진태경이 속한 정찰조가 태원진가를 출발한 지 꼬박 하루가 흘렀다. 태원진가 인근 현읍을 정찰하는 것이 이번 임무였다.

“어제 정오 무렵에 출발했으니 이틀 안에는 도착할 겁니다.”

“아. 태경이.”

진위경은 풀썩 웃었다. 어딘가 지쳐 보이는 웃음이었다.

“난 또 뭐라고. 아닐세.”

“아닙니까?”

“언제까지 어린아이 취급 할 텐가? 이제 그 아이도 당당한 사내야. 알아서 잘하겠지.”

“……제 귀가 의심되는군요.”

“그동안 내가 많이 감싸기는 했지. 그때는 많이 어렸거든.”

“저도 어느 정도는 동감입니다. 며칠 사이에 부쩍 달라졌어요.”

“영웅은 역경을 딛고 성장하는 법이니까.”

“…….”

“아무튼 이제 막내에 대해서는 한시름 놨네. 이제 좀 더 본가에 집중할 수 있겠어.”

“잠시 쉬시지요. 힘들어 보이십니다.”

“위팽. 본가의 식솔들이 죽었네.”

슬픔과 결의가 묻어 나오는 목소리에 위팽은 입을 다물었고, 진위경은 다시 업무를 보기 시작했다.

하지만 침묵은 불과 한 시진 만에 깨졌다.

“저건…….”

점점 가까워지는 하늘 위의 검은 점. 거대한 날개를 펼치며 집무실 창가에 내려앉은 전서응은 하오문의 그것이었다.

황급히 자리에서 일어난 진위경은 전서응의 발목에 고정된 통을 열었다. 서신을 펼친 순간 깨알처럼 적힌 글씨가 눈에 들어왔다.



일문일살一問一殺 조필 외 별동대 이십 인. 정양定壤 출현.



“정양……!”

정양을 넘으면 혼주. 혼주를 넘으면 태원이다. 제아무리 별동대라고 하지만 며칠 만에 수백 리를 주파할 줄이야.

그뿐만이 아니다.

아직까지 본가로 복귀하지 않은 지부의 식솔들이 있다. 설마 놈들이 그들을 추적하고 있다면?

‘한시가 급하다.’

진위경이 결단을 내리기까지는 오래 걸리지 않았다.

“지금 당장 무사 오십을 선별하여 정양으로 가게. 일문일살은 잔학무도한 절정 고수. 본가의 식솔들을…….”

아이들이 생각났다. 작은 팔다리, 고통스럽게 일그러진 얼굴과 공허한 그 눈동자. 진위경은 이를 악물었다.

“식솔들을 안전하게 데려와 주게.”

“주군.”

위팽의 표정이 딱딱하게 굳어 있었다. 진위경은 뭔가에 사로잡힌 듯, 멍하니 그의 얼굴을 바라보다가 입을 열었다.

“태경이. 태경이가 어디로 갔다고 했지?”

쥐어 짜낸 목소리가 흘러나왔다.

“……정양입니다.”
```

### Current accepted English

```markdown
# Chapter 22

The smell of mold stabbed at my nose as soon as I entered the room. The place reminded me of a military barracks, and the members of the reconnaissance squad were waiting inside.

*Ten people.*

I sharpened my senses and looked over each of them.

Every time my gaze passed over an unfamiliar face, a Level display popped up.

*Level 14. Level 15. Level 14…*

Most of them were around the same level. Then, as I moved on to the ninth person—

> **Lv. 22 Hyuk Mujin**

The number jumped sharply. The face was familiar, too.

*Hyuk Mujin?*

It was the same Hyuk Mujin who had picked a fight with me when I first arrived at the Jin Family of Taiyuan a few days ago. When our eyes met, he smirked.

“What a pleasure to see you again, Third. Young. Master.”

I stared at his openly hostile smile and said,

“From now on, call me Squad Leader.”

“……As you wish.”

I ignored Hyuk Mujin’s piercing stare and looked at the tenth member of the reconnaissance squad. The young man who had been smiling brightly since I first appeared shot to his feet.

“Young Master—no, Squad Leader! I look forward to working with you.”

> **Lv. 13 Han Yeop**

It seemed some assignments had been changed because of the war. The White Tiger Hall clerk I had met earlier said that the reconnaissance squad itself was made up of martial artists drawn from several different places.

*Hyuk Mujin originally belonged to the Gate Watch Office, too.*

Maybe that was why the atmosphere in the room was so disorganized.

The squad members looked at me with expressions that mixed the awkwardness of strangers meeting for the first time with anxiety and anticipation about the war.

I spoke first.

“I’m Jin Taekyung, appointed leader of White Tiger Hall’s reconnaissance squad. I look forward to working with you.”

Clap, clap, clap.

Someone’s lonely applause died out within a few seconds, and Han Yeop lowered his hand with an embarrassed expression.

The atmosphere was stiffer than I had expected.

*But that isn’t necessarily a bad thing.*

We were in wartime. Maintaining the current tension was better than laughing together and trying to socialize.

Of course, too much tension could become poisonous. Easing it at the right moment was one of my duties as squad leader.

*That much, I’m used to.*

Newbie Hunters froze the moment they entered a Gate for the first time. Real combat was different from practice. Everything they had learned and trained for at the Hunter training center flew off into outer space, and they were overwhelmed by the primal scent of death.

That was why veterans in the Guild handled mental care for the rookies. I had been one of them.

*Though I was assigned exclusively to F-ranks.*

The levels were similar, too. From what I could tell, a second-rate martial artist from Murim was somewhere between an E-rank and an F-rank.

In other words, I had become the leader of a ten-person F-rank party. I had never actually been a party leader, but I had watched what they were supposed to do until I was sick of it.

“Raise your hand if you have combat experience.”

At my abrupt question, every member of the reconnaissance squad raised a hand. They all looked bewildered.

“Raise your hand if you’ve been in combat at least five times.”

Half the hands went down. Han Yeop was among them.

Five people with experience in at least five battles. That wasn’t bad. No, it was better than expected.

But the most important question remained.

“Raise your hand if you’ve killed someone.”

Four hands dropped weakly. I looked at the only member of the reconnaissance squad who still had his hand raised.

> **Lv. 22 Hyuk Mujin**

“How many?”

He snorted.

“Five. It was during last year’s bandit suppression campaign. One of them was a bandit chieftain. He was quite a strong bastard—”

I cut him off before he could continue.

“Good. You’re the deputy squad leader from now on.”

Hyuk Mujin’s mouth, which had been preparing to ramble on, snapped shut.

“Deputy squad leader?”

“Yeah. Speak up now if you don’t like it.”

With nothing but rookies gathered here, experience mattered more than anything.

Hyuk Mujin was the only one who could swing a weapon at the enemy without hesitation.

*Black cat, white cat.*

White cat, black cat, or even a rude cat—it didn’t matter as long as it caught mice.

Hyuk Mujin thought for a while with a complicated expression before answering.

“……Hmph. Since it’s an order, I suppose it can’t be helped.”

He sure had a difficult way of saying he wanted to be deputy squad leader.

“Then Hyuk Mujin is deputy squad leader. From now on, we’ll call you Number One.”

“Number One? What’s that supposed to mean?”

“Number order. From now on, the reconnaissance squad will be referred to by number instead of name. Hyuk Mujin is Number One. Next, you sitting over there. Yes, you’re Number Two.”

I finished assigning numbers one by one, from Number One to Number Ten.

Hyuk Mujin frowned.

“Why are you doing this?”

“It’s more convenient. We might be fighting today. Do you want to spend all day memorizing names?”

“That’s—”

“Then do as you’re told. It’s an order.”

I didn’t look away from Hyuk Mujin as he glared at me with a hard expression.

Part of me even hoped he would act insolent like he had that day. A battle could break out within the next few days. If things continued as they were, that would be a problem.

If he challenged me, I would have to show him the difference in our strength.

Clearly.

“……I will follow your orders.”

“What did you say?”

“Number One. I said Number One.”

Hyuk Mujin’s voice trembled as he answered. He was more perceptive than I had expected. Maybe it was because of the rumors about the Sleeping Dragon of Shanxi.

The important thing was that Hyuk Mujin had submitted to me.

Without showing anything on my face, I continued.

“What I’m about to say may sound strange and unfamiliar. But bear with it. It’s better than getting stabbed to death, isn’t it? Don’t you agree?”

The other reconnaissance squad members didn’t show their displeasure as openly as Hyuk Mujin, but they also looked at me anxiously.

Everyone except one.

“I’ll follow whatever the Squad Leader says!”

Han Yeop shouted like a teenage girl idol fan. The only difference was that he was holding a spear instead of an idol light stick.

*Oh, right.*

I grinned at the reconnaissance squad.

“Now, raise your hand if you use a sword.”

The core of party hunting was dividing up positions.

* * *

Raid strategies in the real world had been standardized into manuals long ago.

Three tanks. Four damage dealers. Two mages and one healer. For a ten-person party, that was the ideal combination.

*Of course, there are no mages or healers.*

I had to balance things as much as possible with tanks and damage dealers alone, but—

“……You’re telling me no one knows how to use a shield?”

My voice trembled at the shocking result. Good lord, there were ten damage dealers. Nine used swords, and the only person with a spear was Han Yeop.

*What kind of horrifying single-species party is this?*

A hybrid would be better. At least that would mean something had been mixed in.

Hyuk Mujin spoke with an expression that suggested he couldn’t understand what was wrong.

“A man ought to wield a sword.”

I was speechless when I saw the others nodding along with him.

*You’re too well-fed. Way too well-fed.*

Try slamming your head into a pool of blood and see if you still talk like that.

Sword? Spear? There was no such distinction. You bashed people with whatever rock you happened to grab, threw dirt, climbed on top of them, and bit them with your teeth.

On the line between life and death, anything in your hand was a weapon and a lifeline.

These people, who had only ever fought bandits at best, still didn’t understand that.

*Do I need to start training them tomorrow?*

Not for their sake. For my survival.

Even teaching them a few tricks would make a real difference in a melee.

*I worked like a dog for seven years. I can’t die because of a bunch of rookies.*

That was when it happened.

Ding. Ding. Ding.

A large bell rang three times.

Since no one could tell the exact time, bells were rung at set intervals. The three tolls that had just sounded marked Mi-si, roughly one to three in the afternoon.[^1]

And—

“Get ready. This is our first deployment.”

The bells also served as the signal announcing the reconnaissance squad’s first mission.

* * *

“He should be doing fine.”

Jin Wikyung looked up at Wipeng’s abrupt comment. Until a moment ago, he had been staring blankly at a teacup as it slowly cooled.

“What are you talking about?”

“The Third Young Master.”

A full day had passed since the reconnaissance squad led by Jin Taekyung departed from the Jin Family of Taiyuan. Their mission was to scout the county towns near the Jin Family.

“They left around noon yesterday, so they should arrive within two days.”

“Ah. Taekyung.”

Jin Wikyung let out a weak laugh. He looked exhausted.

“I thought you meant something else. That’s not it.”

“It’s not?”

“How long are you going to treat him like a child? He’s a grown man now. I’m sure he’ll manage on his own.”

“……I’m beginning to doubt my ears.”

“I did coddle him quite a bit. He was very young back then.”

“I agree, to some extent. He’s changed considerably over the past few days.”

“Heroes grow by overcoming adversity.”

“……”

“Anyway, I can stop worrying about the youngest now. I’ll be able to focus more on the main family.”

“You should rest for a while. You look tired.”

“Wipeng. Members of our family have died.”

At the sorrow and determination in his voice, Wipeng fell silent, and Jin Wikyung returned to his work.

But the silence broke after a mere two hours.

“What is that…?”

A black dot in the sky was gradually drawing closer. Spreading its enormous wings, the messenger hawk landed by the window of the office. It belonged to the Lower District Sect.

Jin Wikyung hurriedly stood and opened the tube fastened to the hawk’s leg. The moment he unfolded the letter, tiny writing caught his eye.

> Jopil, One Question, One Kill, and twenty members of a special detachment have appeared in Jeongyang.

“Jeongyang…!”

Beyond Jeongyang was Honju. Beyond Honju was Taiyuan. Even if they were a special detachment, he had never expected them to cover hundreds of li in only a few days.

That wasn’t all.

There were still family members from the branches who had not returned to the main family. What if the enemy was tracking them?

*Every moment counts.*

It didn’t take Jin Wikyung long to make a decision.

“Select fifty martial artists immediately and send them to Jeongyang. One Question, One Kill Jopil is a brutal Peak master. Bring our family members—”

He thought of the children.

Their small limbs. Their faces twisted in pain. Their vacant eyes.

Jin Wikyung clenched his teeth.

“Bring our family members home safely.”

“My lord.”

Wipeng’s expression had hardened. Jin Wikyung stared blankly at him, as though a thought had seized him, before speaking.

“Taekyung. Where did you say Taekyung went?”

His voice came out strained.

“……Jeongyang.”

[^1]: Mi-si is one of the traditional two-hour divisions of the day, corresponding roughly to 1–3 p.m.
```
## Chapter 23

### Korean source

```text
＃23화



태원진가.

이름에서 알 수 있듯이 그 본거지는 태원이다. 그러나 현실에서의 대기업이 그렇듯, 태원진가의 영향력은 태원 한 곳에 국한되지 않았다.

가문이 세워진 지 200년. 산서성 곳곳에 산재한 현읍에 지부를 설치해 세력권을 넓힌 지 오래였다.



닷새 안에 정양 인근을 정찰하고 복귀할 것.



정찰조에게 내려진 첫 임무다. 명령 내용을 들은 조원들의 첫 반응은 두 가지로 나뉘었다.

“별거 아니군요.”

혁무진처럼 실망하는 자들이 있는가 하면, 한엽처럼 안도의 한숨을 내쉬는 자도 있었다.

물론 둘 다 내 마음에 드는 반응은 아니었다.

혁무진 쪽은 쓸데없는 공명심에 사로잡혀 있고, 한엽 쪽은 싸우는 것을 겁내고 있으니까.

‘그래, 차라리 안전한 임무가 낫지.’

이런 놈들 데리고 적들이랑 맞닥뜨려 봐라. 상상만 해도 끔찍하다. 차라리 믿을 만한 놈들이랑 일선에서 싸우는 게 덜 위험할 것이다.

‘보직 이동이라도 신청해야 되나.’

내심 한숨을 쉬며 주먹을 치켜올렸다. 앞서 숙지시킨 수신호 중 하나다. 뜻은 정지.

푸르륵.

적당한 속도로 달리고 있던 열한 마리의 말이 투레질 소리와 함께 멈췄다. 내 오른편에서 달리고 있던 혁무진이 퉁명스럽게 말했다.

“왜 멈추는 거요?”

“휴식.”

“또?”

“한 시진 이동. 일각 휴식. 내가 미리 말하지 않았나?”

“더 달릴 수 있소!”

“그럼 너 혼자 달리든가.”

나는 슬쩍 뒤를 턱짓했다. 다른 조원들이 거친 숨을 몰아쉬고 있었다. 말을 타고 이동하는 것은 속도가 빠른 대신, 상당한 스태미나를 소모한다.

레벨이 월등히 높은 혁무진은 그럭저럭 버틴다지만, 다른 조원들은 피로가 누적되고 있었다.

“쉬라면 쉬어. 명령이다.”

혁무진의 구겨진 얼굴을 무시하고 조원들을 향해 말했다.

“일각 동안 휴식.”

일각. 15분의 휴식 시간이 주어졌지만 정찰조원들의 표정은 썩 밝지 않았다. 내가 곧장 커다란 가죽 배낭을 꺼냈기 때문이다.

배낭에 손을 집어넣고 생각했다.

‘인벤토리 오픈.’

철그럭 소리와 함께 방패 세 개가 배낭 안으로 소환됐다.

표면에 철을 입힌 나무 방패는 태원진가를 떠나오기 전 무기고에서 얻어 온 것이었는데, 가볍고 단단해서 쓸 만했다.

“칠 호. 팔 호. 구 호.”

지명된 정찰조원 셋이 죽을상을 쓰며 방패를 받아 갔다.

그 셋이 내게 강제로 선택된, 탱커(Tanker)다.

‘딜러 일곱. 탱커 셋. 그리고 나.’

게이트에 들어갔다가는 몰살을 당할 조합이었지만 우선은 이 정도로 만족해야 한다.

“각자 위치로.”

다음은 포메이션이다.

“기본 대형.”

방패를 든 셋이 가장 앞에 서고, 일 호 혁무진부터 육 호까지 여섯 명의 검사가 제2열. 최후방에는 나와 한엽이 있다.

전방 위주의 경계다.

“펼쳐. 헤쳐 모여. 산개.”

불만이 가득한 얼굴들이었지만 이제는 제법 능숙하게 해낸다. 이정도면 이제 막 헌터 훈련소를 졸업한 F급 헌터보다 훨씬 낫다.

‘사람보다 여기 NPC가 낫네.’

공력의 유무에서 나오는 차이일 것이다.

마나 자체를 다루지 못하는 F급 헌터와 달리 무림의 NPC들은 미미하나마 공력을 사용할 줄 아니까.

단지 레벨이 낮고, 경험이 없을 뿐이지.

나는 포메이션의 마지막 단계로 접어들었다.

“전력 후퇴.”

순간 정찰조원들이 멈칫했다.

“예?”

“전력 후퇴는 뭡니까?”

“말 그대로지. 전력을 다해서 후퇴하라고.”

“그럼 어떤 대형을……?”

“그때쯤이면 대형이 무의미하지. 그냥 전력을 다해서 튀어라. 뒤도 돌아보지 말고 최대한 흩어져서.”

“큭큭. 그걸 말이라고 하는 거요?”

비웃음의 주인은, 당연하게도 혁무진이었다.

“이제 도저히 못 참겠군. 삼공자, 전쟁이 소꿉장난이오? 헛소리를 그럴듯하게 하려면 최소한 병법서 한 권 정도는 읽고 왔어야지.”

“병법서?”

“그래. 병법서! 질서정연하게 후퇴하는 것은 병법의 기본중의 기본인데 무슨 망발을 지껄이는 거요?”

혁무진이 대놓고 반발하자 정찰조원들 사이에서도 소극적인 목소리들이 새어 나왔다.

“맞는 말이긴 해.”

“우리가 관아의 군병도 아닌데 대형을 연습시키고, 억지로 방패까지 들게 하고…….”

“전력 후퇴? 그런 건 들어 본 적도 없어.”

봐라, 다들 나랑 같은 생각이다. 혁무진의 득의양양한 얼굴이 말하는 듯했다.

그때 한엽이 더듬거리는 목소리로 끼어들었다.

“저, 저는 그렇게 생각 안 하는데요.”

“뭐?”

“삼공자, 아니 조장님께서 다 생각이 있으셔서 그런 게 아닐까……요?”

“생각?”

혁무진이 눈을 부라렸다.

“생각은 무슨 생각! 어릴 때부터 수련은 뒷전이고 계집 끼고 술만 퍼마시던 게 삼공자다. 그런 주제에 사고란 사고는 다 치고 다녔지. 그뿐인가, 이 전쟁의 원인을 제공한 것도…….”

“그만하지?”

말을 가로막자 혁무진이 움찔한다. 스스로도 말실수를 했다는 걸 깨달은 모양이었다.

하지만 종종 그런 사람들이 있다. 물러서야 할 때, 오히려 한발 나아가는 그런 사람들이.

“원인을 제공한 것도 삼공자 아닌가!”

혁무진은 자신의 말을 멈추기에는 자존심이 너무나 강한 놈이었다.

결국 뱉어 낸 그 말에, 싸늘한 침묵이 내려앉았다.

꿀꺽. 누군가의 목울대가 크게 일렁였다. 아홉 쌍의 눈빛이 나와 혁무진을 바라보고 있었다.

“하, 할 말이라도 있소?”

할 말? 당연히 있지.

“전원 일 다경 더 휴식.”

동시에 곧게 편 손바닥으로 혁무진의 뺨을 후려쳤다.

쫙!

“한 대.”

혁무진의 턱이 돌아간다. 공력이 전혀 실리지 않은 단순한 따귀다. 갑작스러운 상황에 멍해진 그 얼굴로 두 번째 손바닥을 날렸다.

“이, 이게 무슨!”

그래도 영 맹탕은 아닌지, 팔을 들어 막는다. 녀석이 간과한 부분이 있다면 그건 바로 힘의 차이다.

쫙!

“두 대.”

상체 그대로 땅에 처박힌 혁무진이 벌떡 일어났다. 한쪽 뺨에는 내 손바닥 자국이 문신처럼 박혀 있었다.

당황이 분노로 바뀌기까지는 그리 오랜 시간이 걸리지 않았다.

“이 개새끼가!”

제대로 열받았군. 눈이 뒤집혀서 달려드는 녀석의 다리를 걸어 넘어트렸다. 동시에 왼손에 힘을 실어 후려쳤다.

쫙.

“세 대.”

“커헉.”

다리에 힘이 풀리는지 비틀거린다. 이 정도 힘으로 연달아 세 번을 맞았으니 골이 흔들릴 법도 하다.

“공력은 뒀다가 국 끓여 먹을래?”

이 말은 효과가 있었다. 휘청거리던 하체에 힘이 들어가고 몸에서는 힘이 흘러넘친다. 독기가 줄줄 새는 눈빛이 나를 노려봤다.

“후회하게 될 거야.”

“아닐걸.”

얼굴을 향해 날아오는 주먹을 붙잡았다. 속도, 힘, 타이밍.

전부 눈에 보인다. 이소군에 비하면 한참이나 떨어진다.

“네 대.”

혁무진의 얼굴이 뒤로 젖혀진다. 찐득한 핏물이 슬로우 모션처럼 허공에 흩뿌려졌다. 풀린 동공, 축 늘어진 다리.

하지만 용케도 쓰러지지 않았다.

그건 내가 녀석의 주먹을 놔줘야만 가능한 일이니까.

“다섯 대.”

쫙!

거기까지가 한계였다. 혁무진은 더 이상 버티지 못하고 혼절했다. 기이한 자세로 널브러진 혁무진의 몸뚱어리 위로 무언가가 투둑 떨어진다.

‘눈?’

고개를 들어 하늘을 바라봤다. 겨울 하늘이 희고 작은 쓰레기들을 쏟아 내는 중이었다.

“휴식 끝. 출발한다.”

한마디를 툭 던지고 돌아서는 내 등 뒤로, 정찰조원들이 참았던 숨을 토해 냈다.



* * *



두 시간 만에 깨어난 혁무진이 가장 먼저 한 일은 내게 달려드는 것이었다.

“이런 씨발!”

쫙. 털썩.

“치워.”

“예, 옛!”

찰진 따귀 소리와 함께 또 다시 기절한 녀석은, 다른 정찰조원들의 손에 의해 오두막 한 구석에 처박혔다.

‘오두막이라. 운 좋네.’

인근 지리에 빠삭한 조원의 말에 따르면 적어도 오늘 해가 떨어지기 전까지는 정양에 도착했어야 했다.

하지만 갑자기 쏟아지는 폭설에는 어쩔 도리가 없었고, 겨우 찾아낸 곳이 바로 이 오두막이었다.

아는 사람만 아는 사냥꾼 쉼터라던가?

‘턱 없이 작긴 한데, 이 정도면 땡큐지.’

임무가 늦어질 수도 있겠지만, 눈밭에서 밤새 걷다가 기진맥진한 상태에서 적과 마주치는 것보다는 백배 낫다.

그런 생각을 할 때였다.

“저, 조장님.”

한엽이다. 등 뒤로 조원들이 힐끔거리며 내 눈치를 살폈다.

“이제 어떡할까요?”

“응? 자야지.”

“저, 그게 아니라…….”

우물쭈물하는 정찰조원들을 보자 문득 떠오르는 게 있었다.

너희 설마…….

“수련하고 싶냐?”

끄덕끄덕. 맹렬하게 상하를 오가는 고갯짓과 열의에 가득 찬 저 눈빛을 봐라.

‘백문이 불여일퍽이라더니.’

백번 말하는 것보다 한 번 패는 게 낫구나.



* * *



정오 무렵이었다. 검날이 햇빛을 받아 번쩍였고, 그것이 무사가 볼 수 있었던 유일한 것이었다.

“커헉.”

털썩. 무릎이 꺾이고 얼어붙은 땅바닥에 얼굴이 처박힌다.

어깨부터 가슴까지, 쩍 벌어진 상처 사이로 피가 쏟아졌다. 회생 불능의 상처. 무사는 죽음을 직감했다.

“다른 이들은…… 제발 살려.”

힘을 다한 목소리가 뚝 끊겼다. 부릅뜬 무사의 눈동자를 보며 한 중년인이 혀를 찼다.

“어이구, 이 미련한 친구야.”

그렇게 다짜고짜 덤비면 어떡하나. 이어지는 말은 망자에게 닿지 못했다. 주위를 둘러싸고 있던 오십여 명의 낭인들이 낄낄거렸다.

“하필 대형한테 걸리다니, 운도 더럽게 없는 놈일세그려.”

“누가 정파 새끼 아니랄까 봐 마지막까지 협객 놀음은. 어쩔까요, 대형?”

번들거리는 시선들이 남아 있는 생존자들을 향했다. 여자와 아이들로 이루어진 예닐곱 명의 무리였다.

“대협. 아이들은 살려 주십시오.”

가장 연장자로 보이는 여인의 말에 중년인, 일문일살(一問一殺) 조필은 부드럽게 웃었다.

“미안하지만 어쩌지. 나는 대협이 아니라오.”

“하지만 사람이지요. 어찌 사리분별도 하지 못하는 아이들까지 죽이려 하십니까?”

“허, 아녀자의 몸으로 기개가 제법이오. 가만, 삭주 지부장의 일가가 살아남았다고 하던데. 혹시?”

“제 부군 되십니다.”

“아, 역시 그렇구려. 그런 못난 놈에게 이런 현숙한 부인이 있을 줄이야.”

조필은 빙긋 웃었고, 여인은 얼굴을 굳혔다.

“살려 줄 생각이 없군.”

“안심하시오. 나는 간살하는 취미는 없거든.”

“아이들은…….”

“이 험난한 세상. 어린것들이 어미 없이 어찌 살아남겠소?”

“금수만도 못한 놈.”

“유언, 잘 들었소.”

그 말이 신호탄이었다.

검광이 번뜩이고 비명이 울려 퍼졌다.

잠시 후 피를 흠뻑 뒤집어쓴 낭인들이 시체들을 산속 수풀로 던져 넣었다.

“산짐승 놈들만 포식하겠군요.”

뱁새눈이 중얼거렸다. 그는 조필의 오른팔 격인 인물로, 흑산도(黑山刀)라는 별호로 알려진 일급 낭인이었다.

“우리도 포식해야지. 이번 일만 잘 마무리 짓는다면 천금이 별건가?”

조필은 기분 좋게 웃었다. 이번 일로 받게 될 사례도 어마어마했지만, 그는 지금 이 상황 자체를 즐기고 있었다.

“태원진가 놈들을 사냥하는 날이 오다니. 상상도 못 했지.”

더러워진 가죽신이 고꾸라진 무사의 시신을 밟았다.

무사는 태원진가에 속한 십여 개 지부 중 하나인 삭주(朔州) 지부 소속이었다.

“방금 처리한 게 마지막인가?”

“아닙니다, 대형.”

“쥐새끼처럼 잘도 빠져나가는군. 머릿수는?”

“도합 셋. 무사 하나에 아이 둘입니다. 불과 몇 시진 전에 정양을 통과, 혼주로 향하고 있다고 합니다.”

“골치 아프군. 반나절은 걸릴 텐데.”

“대형께서 나서실 필요도 없이 제가 다녀오겠습니다.”

“그래 주겠나?”

조필의 입가에 흐뭇한 미소가 떠올랐다.

“좋아, 절반을 데려가게. 기한은 반나절, 어떤가?”

대답은 이미 정해져 있었다. 흑산도는 깊이 고개를 숙였다.
```

### Current accepted English

```markdown
# Chapter 23

Jin Family of Taiyuan.

As its name suggests, its headquarters were in Taiyuan. But like a conglomerate in the real world, the Jin Family of Taiyuan’s influence was not limited to a single city.

The family had been established for two hundred years. It had long since expanded its sphere of influence by establishing branches in county towns scattered throughout Shanxi.

*Scout the area near Jeongyang and return within five days.*

That was the first mission assigned to the reconnaissance squad. When they heard the order, the squad members’ reactions fell into two categories.

“Doesn’t sound like much.”

Some, like Hyuk Mujin, were disappointed. Others, like Han Yeop, let out sighs of relief.

Of course, neither reaction pleased me.

Hyuk Mujin was caught up in a pointless hunger for glory, while Han Yeop was afraid of fighting.

*Still, I’d rather have a safe mission.*

Try running into the enemy with a bunch of guys like these. It was horrifying just to imagine. I’d be safer fighting on the front lines with people I could trust.

*Should I apply for a transfer?*

Suppressing a sigh, I raised my fist. It was one of the hand signals I had taught them earlier. It meant stop.

Snort.

The eleven horses moving at a moderate pace stopped with a chorus of snorts. Hyuk Mujin, riding to my right, spoke irritably.

“Why are we stopping?”

“Rest.”

“Again?”

“Two hours of travel, fifteen minutes of rest. Didn’t I tell you that beforehand?”

“I can keep going!”

“Then go by yourself.”

I jerked my chin toward the rear. The other squad members were breathing heavily. Riding a horse was faster than traveling on foot, but it consumed a considerable amount of stamina.

Hyuk Mujin’s much higher Level let him endure fairly well, but fatigue was accumulating in the others.

“Rest if I tell you to. That’s an order.”

Ignoring Hyuk Mujin’s crumpled face, I addressed the squad.

“Fifteen minutes of rest.”

They had fifteen minutes to rest, but the reconnaissance squad members didn’t look particularly happy. That was because I immediately pulled out a large leather backpack.

I reached into the backpack and thought,

*Open Inventory.*

With a clatter, three shields were summoned into the backpack.

The wooden shields had been coated with iron on the surface. I had taken them from the armory before leaving the Jin Family of Taiyuan. They were light, sturdy, and perfectly usable.

“Number Seven. Number Eight. Number Nine.”

The three designated reconnaissance squad members accepted the shields with faces that looked ready to die.

Those three had been forcibly selected by me as tanks.

*Seven damage dealers. Three tanks. And me.*

It was a party that would be wiped out the moment it entered a Gate, but for now, I had to be satisfied with this.

“Everyone to your positions.”

Next came formation.

“Basic formation.”

The three shield bearers stood at the front. Six swordsmen, from Number One Hyuk Mujin through Number Six, formed the second row. Han Yeop and I took the rear.

A formation focused on watching the front.

“Spread out. Scatter and assemble. Disperse.”

Their faces were still full of complaints, but they now carried out the commands fairly skillfully. At this point, they were much better than F-rank Hunters who had just graduated from a Hunter training center.

*These NPCs are better than people.*

The difference probably came down to whether they could use internal energy.

Unlike F-rank Hunters, who couldn’t manipulate mana at all, Murim’s NPCs could use internal energy, however faintly.

They were merely low-Level and inexperienced.

I moved on to the final stage of formation training.

“All-out retreat.”

The reconnaissance squad members froze.

“What?”

“What does ‘all-out retreat’ mean?”

“It means exactly what it says. Retreat with all your strength.”

“Then what formation should we—?”

“By then, formation will be meaningless. Just run with all your strength. Don’t even look back. Scatter as much as possible.”

“Heh. You call that an order?”

The owner of the mocking voice was, naturally, Hyuk Mujin.

“I can’t stand this any longer. Third Young Master, is war some children’s game? If you want to make nonsense sound convincing, you should at least have read one military strategy manual before coming here.”

“A military strategy manual?”

“Yes, a military strategy manual! Retreating in good order is one of the most basic principles of warfare. What kind of nonsense are you spouting?”

Hyuk Mujin’s open defiance drew hesitant voices from the other reconnaissance squad members.

“He’s not wrong.”

“We aren’t government soldiers, so why are we practicing formations and being forced to carry shields…?”

“I’ve never heard of an all-out retreat.”

See? Everyone thinks the same way I do. Hyuk Mujin’s smug face seemed to say exactly that.

Then Han Yeop joined in, his voice wavering.

“I-I don’t think that way.”

“What?”

“The Third Young Master—I mean Squad Leader—must have a reason for doing this… right?”

“A reason?”

Hyuk Mujin glared at him.

“What reason could there be? The Third Young Master spent his youth drinking with women instead of training. He caused every kind of trouble despite being like that. And that’s not all. He was also the one who caused this war—”

“Enough.”

Hyuk Mujin flinched when I cut him off. He seemed to realize that he had made a mistake.

But some people were like that. When they needed to back down, they took another step forward instead.

“Wasn’t the Third Young Master the one who caused this war?”

Hyuk Mujin’s pride was too great for him to stop himself.

The words finally left his mouth, and a chilly silence descended.

Gulp.

Someone’s throat bobbed loudly. Nine pairs of eyes turned toward Hyuk Mujin and me.

“D-do you have something to say?”

Something to say? Of course I did.

“Everyone gets another fifteen minutes of rest.”

At the same time, I slapped Hyuk Mujin across the cheek with my flat palm.

Smack!

“One.”

His jaw twisted to the side. It was an ordinary slap, without even a trace of internal energy. His face was still dazed by the sudden turn of events when I struck him a second time.

“What the—!”

He wasn’t completely helpless, at least. He raised his arm to block.

What he had failed to account for was the difference in strength.

Smack!

“Two.”

Hyuk Mujin’s upper body slammed into the ground. He sprang back up, a palm print stamped onto one cheek like a tattoo.

It didn’t take long for his bewilderment to turn into rage.

“You fucking bastard!”

He was properly furious now. As he charged at me with his eyes bulging, I hooked his leg and tripped him. At the same time, I put force into my left hand and struck him.

Smack.

“Three.”

“Urgh.”

His legs seemed to give out, and he staggered. After taking three consecutive blows with this much force, it was only natural that his head would be rattled.

“What, were you saving your internal energy to boil soup?”

That got through to him. Strength filled his wavering legs, and power surged through his body. His eyes glared at me, venom dripping from them.

“You’ll regret this.”

“No, I won’t.”

I caught the fist flying toward my face.

Speed, strength, timing.

I could see all of them. Compared to Lee Seogeun, he was far behind.

“Four.”

Hyuk Mujin’s head snapped back. Sticky blood sprayed through the air in slow motion. His pupils were unfocused, and his legs hung limp.

Yet somehow, he didn’t fall. He couldn’t—not unless I let go of his fist.

“Five.”

Smack!

That was his limit. Hyuk Mujin could no longer endure and passed out. Something fell with a soft thud onto his body, sprawled out in a bizarre position.

*An eye?*

I raised my head toward the sky. The winter sky was raining down small white scraps of garbage.

“Rest is over. We’re leaving.”

I tossed out the words and turned away. Behind me, the reconnaissance squad members finally exhaled the breath they had been holding.

* * *

When Hyuk Mujin woke up two hours later, the first thing he did was charge at me.

“You fucking—!”

Smack. Thud.

“Move him.”

“Y-yes, sir!”

After another ringing slap, he passed out again. The other reconnaissance squad members dragged him into a corner of the cabin.

*A cabin. We got lucky.*

According to one squad member who knew the surrounding area well, we should have reached Jeongyang before sunset at the latest.

But there had been nothing we could do about the sudden blizzard, and this cabin was the only place we had managed to find.

Apparently, it was a hunter’s shelter known only to those familiar with the area.

*It’s ridiculously small, but I’ll take it.*

The mission might be delayed, but this was a hundred times better than walking through the snow all night, collapsing from exhaustion, and then running into the enemy.

That was when—

“Squad Leader?”

It was Han Yeop. The squad members behind him glanced at me, gauging my reaction.

“What should we do now?”

“Hm? Sleep.”

“N-no, that’s not what I meant…”

As I looked at the fidgeting reconnaissance squad members, a thought struck me.

*Don’t tell me…*

“Do you want to train?”

Nod, nod.

Look at the vigorous nodding and those eyes full of passion.

*Seeing is believing, my ass. One beating beats a hundred explanations.*

One beating really was better than explaining a hundred times.

* * *

It was around noon. Sunlight flashed along a sword blade. That was all the martial artist saw.

“Urgh.”

Thud.

His knees buckled, and his face slammed into the frozen ground.

Blood poured from the gaping wound that stretched from his shoulder to his chest. It was a fatal injury. The martial artist knew he was going to die.

“The others… Please, let them live.”

His exhausted voice cut off abruptly. Looking at the martial artist’s wide-open eyes, a middle-aged man clicked his tongue.

“Good grief, you poor fool.”

What were you thinking, charging in like that?

The words that followed never reached the dead man. The fifty-odd wandering martial artists surrounding them snickered.

“Of all people, he had to run into the boss. What rotten luck.”

“Only an orthodox-faction bastard would keep playing the hero right to the end. What should we do, Boss?”

Their gleaming eyes turned toward the survivors. There were six or seven women and children huddled together.

“Great Hero, please spare the children.”

At the plea from the oldest-looking woman, the middle-aged man—Jopil, One Question, One Kill—smiled gently.

“I’m sorry, but what can I do? I’m no Great Hero.”

“But you’re still a person. How can you kill children who can’t even tell right from wrong?”

“Hah. For a woman, you have quite a bit of spirit. Wait. I heard that the family of the Sakju Branch Leader survived. Could it be…?”

“He is my husband.”

“Ah, so he is. I never imagined such a virtuous wife would belong to such a pathetic man.”

Jopil smiled broadly, and the woman’s expression hardened.

“You have no intention of sparing us.”

“Rest easy. I don’t have a taste for tormenting people.”

“The children…”

“This is a harsh world. How are little ones supposed to survive without their mother?”

“You’re worse than a beast.”

“I heard your last words.”

That was the signal.

Swordlight flashed, and screams rang out.

A short while later, the blood-soaked wandering martial artists tossed the corpses into the thickets in the mountains.

“Only the wild animals will feast tonight.”

The man with the tiny birdlike eyes muttered. He was Jopil’s right-hand man, a first-rate wandering martial artist known by the nickname Black Mountain Blade.

“We should feast, too. If we finish this job properly, what’s a mere thousand pieces of gold?”

Jopil laughed with pleasure. The payment for this job would be enormous, but the situation itself was what he enjoyed.

“I never imagined the day would come when we’d hunt the Jin Family of Taiyuan.”

His dirty leather shoe stepped on the fallen martial artist’s corpse.

The martial artist had belonged to the Sakju Branch, one of the ten or so branches of the Jin Family of Taiyuan.

“Was that the last one?”

“No, Boss.”

“They’re slipping away like rats. How many?”

“Three in total. One martial artist and two children. They passed through Jeongyang only a few hours ago and are headed for Honju.”

“That’s troublesome. It’ll take half a day.”

“You don’t need to go yourself. I’ll take care of it.”

“Would you?”

A pleased smile spread across Jopil’s lips.

“Good. Take half of them with you. You have half a day. How does that sound?”

Black Mountain Blade already knew the answer and bowed deeply.
```
