<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0730.txt",
      "sha256": "12a07f7592ebcd271ccc85b556191ad18dc610797b1f42a8a869f58dbc75dc74",
      "bytes": 13259
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "09658c41a4a9346dcb773b4b41ae08fa70d13494925f79fed4653cc70df1fb6e",
      "bytes": 1761
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0626337c423d0316dce9b5a5dd73a02ebc00abeeb7b97fb5eb26980c5688c635",
      "bytes": 210392
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "37258e4982d62d9b060d0712ef1541ddb291b7825bbd22e39c4fd47f92c0d59e",
      "bytes": 752
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d3b72eccaff7e87b1b929c7e67dc969768cc349cc1c29077b08b112494d313f1",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "cd88e4b9b58f188a28dc8da3681f31d65615b6c7a08786e2e49e31190799a5a2",
      "bytes": 817
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "f913d52807e8b409ef4da9fa1dc85e6caa32a6b677794d92d8819d5991531e64",
      "bytes": 2011
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "5eb47c31157f59cd35d8fe2d986361e7f2f787f185a2116d4fa9e0485b79acac",
      "bytes": 622
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "8770277341204d5b1fc2fb846b4ac53784524811d81fb2ebd806f734b1136440",
      "bytes": 626
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "3497720d7f07b6368dec81e0ee6a5e1a3872ffd9c0c10123eba3bea44ecd7836",
      "bytes": 967
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "01412479394cb034c67e5e4710c1871400d5ddf6519aa23cd2d568f17438a0c3",
      "bytes": 221090
    }
  ],
  "estimated_tokens": 10608
}
-->

# Durable State Update — Chapter 730

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 730. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 730. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 730,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 730,
    "continuity_sources": [730],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "Jin Taekyung and Choi Minwoo are preparing a public release of Cheon Taemin's Heaven and Earth Cultivation Technique.",
    "The technique is safe and versatile enough for even the lowest-ranking Hunters to learn, though its immediate effects are limited.",
    "Baek Hanseong has committed the government to cooperation and announced an imminent major announcement through an emergency Blue House press conference.",
    "The release is being presented as a national project associated with Korea and Cheon Taemin.",
    "Jin and Choi are concealing Cheon Taemin's unconscious condition and Jin's authorship of the technique.",
    "The announcement has caused worldwide media upheaval and broad public praise.",
    "Ares Guild executives are uneasy about Choi's unilateral decision-making but are constrained by Cheon Taemin's legitimacy.",
    "Jin has confronted the executives after Choi apologized for withholding advance notice."
  ],
  "continuity_sources": [
    729
  ],
  "open_questions": [
    "What will be revealed in the major announcement two days later?",
    "How will the Heaven and Earth Cultivation Technique be distributed and regulated after its public release?",
    "Will the Ares executives accept Choi's authority or continue challenging his decisions?",
    "How long can Jin and Choi conceal the truth about Cheon Taemin and Jin's authorship?",
    "Who is leaking the unidentified sources that are fueling media speculation?"
  ],
  "safe_through": 729,
  "temporary_decisions": [
    "Render 천지심법 as The Heaven and Earth Cultivation Technique.",
    "Render 국뽕 as patriotic high.",
    "Preserve Jin's profane comic banter and the online forum's informal tone."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 천태민    | **Cheon Taemin**  |
| 무신     | **Martial God**               | —              |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 지부장    | **Branch Leader**                            |
| 명성               | **Fame**                       |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 귀면 | **Ghost Face** | Taekyung's joking alternate epithet for Wipeng. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 석고준 | 최민우 | Ares security leader to rival Guild Master | Team Leader Choi Minwoo | formal but barbed | Uses 평화 길드 최민우 팀장님 while belittling Choi and blaming the Peace Guild for Taekyung's apparent death. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 팀장 | 중년인 | Hunter_team_leader_to_stranger | Boss | casual and polite | The Team Leader mistakes disguised Song for an ordinary raid customer and warns him not to proceed. |
| 보안팀장 | 진태경 | Ares Security Team Leader to an intruding Hunter | Mr. Jin | formal-polite under pressure | The Security Team Leader repeatedly addresses Jin as 진태경 씨 while ordering him to withdraw. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 729
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he remains unconscious after more than twenty years in a wired mechanical capsule at his former mansion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 729
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 729
- **Aliases:** Team Leader Seok
- **Role:** Go Jun was Ares Guild's Vice Guild Master, Lee Jungryong's Disciple and former Head of Security, the de facto successor to Lee's Ares legacy, and a mutated monster who was killed by Jin Taekyung in Area A.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Go Jun inherited Lee Jungryong's Ares legacy after becoming his Disciple and regarded Jin Taekyung and Choi Minwoo as enemies before his death.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 729
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, a traveler between Murim and another world resembling the realm of immortals, and the creator of the beginner-accessible Smiling Mana Cultivation Method.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 729
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 684
- **Aliases:** None
- **Role:** The Martial God is an unidentified legendary martial artist who defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone more than fifty years ago.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, appearing first as a white-bearded elder and later as a young boy; his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 729
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Cheon Taemin's only living blood relative, a formidable aura-wielding swordsman who wields Hero's Soul, and the current Guild Master of the Peace Guild and Vice Guild Master of Ares Guild after a unanimous board vote.
- **Personality:** Strategic, candid, controlled, and possessive of the power and influence he intends to inherit.
- **Voice:** Dry, formal, and direct, with calm candor and carefully chosen metaphors.
- **Relationships:** Choi Minwoo is Cheon Taemin's maternal grandson and only living blood relative, was kept out of public knowledge by Lee Jungryong, is closely integrated with Jin Taekyung's family, seeks to acquire the Ares Guild intact, knows that Song Cheonwoo and Lee concealed Taemin's collapse and purged aides, and is Kim Hwajong's grandson.

## Korean source

```text
＃730화



똑. 똑.

갑작스럽게 울려 퍼진 노크 소리에 사람들의 시선이 문을 향해 쏠렸다.

회의실에 수뇌부 모두가 모여 중요한 이야기를 나누고 있다는 것은 아레스 길드의 청소부도 아는 사실.

그러니 이런 상황에서 누군가 문을 두드렸다는 것은 딱 두 가지 경우뿐이었다.

그만큼 중요한 사안이거나, 혹은 이미 사표를 써 놨거나.

그리고 우선 쌍욕부터 뱉고 봤을 석고준과 달리 그들의 새로운 성주는 자신에게 유리한 흐름을 방해받았음에도 눈썹 하나 까딱하지 않았다.

“들어오세요.”

달칵.

반쯤 열린 문틈 사이로 한 중년인이 모습을 드러낸다.

비서 실장이라는 직함을 지닌 그는 곧장 최민우를 향해 다가와 고개를 숙였다.

“회의 중에 죄송합니다, 부길드장님.”

최민우가 담담하게 대답했다.

“괜찮습니다. 그럴 만한 이유가 있다면요.”

비서 실장이 마른침을 꿀꺽 삼켰다.

비록 얼마 되지는 않았지만, 그는 눈앞의 고용주가 신상필벌이 확실하다는 사실을 잘 알고 있었다.

덧붙여 불과 1분 전 로비의 보안팀으로부터 올라온 보고가 자신의 선에서 처리할 수 없는 사안이라는 것 역시도.

“중요한 손님께서 찾아오셨습니다.”

슥.

떨리는 목소리와 함께 내밀어지는 손.

비서 실장이 건넨 무언가를 바라보는 최민우의 눈동자가 깊숙이 가라앉았다.

‘이건.’

깨달음과 동시에 뇌리를 스치는 여러 가지 생각들.

그러나 망설임은 짧았고, 최민우는 마음의 결정을 내렸다.

“손님은 어디에 계십니까?”

“아직 로비에…….”

“제 개인 집무실로 안내해 드리세요. 곧 가겠습니다.”

“알겠습니다.”

기다렸다는 듯이 대답한 비서 실장이 회의실을 빠져나가자, 최민우는 자리에 앉아 있는 임원들을 향해 고개를 돌렸다.

“당장 급했던 이야기는 얼추 끝난 듯싶은데, 어떻게들 생각하십니까?”

“예?”

“부길드장님, 혹시 그 말씀은…….”

“여러분들께서 양해해 주신다면 오늘 회의는 이쯤에서 끝마쳐야 할 것 같습니다.”

몇몇 임원들이 황당하다는 얼굴로 최민우를 바라보았다.

해도 해도 이건 너무한 처사다.

아무리 중요한 손님이 왔어도 그렇지, 해외 지부장들까지 전부 모인 회의를 이런 식으로 끝낸다는 것이 말이 되나.

드르륵.

“부길드장님!”

용기를 낸 임원 하나가 벌떡 일어난 그 순간.

쾅!

갑작스러운 굉음이 목소리를 집어삼켰다.

합금으로 만들어진 테이블에 손바닥 자국을 새겨 넣은 진태경이 중얼거렸다.

“아니, 알이라도 깠나. 뭔 놈의 벌레 새끼들이 자꾸 날아다녀. 회의실 다시 한번 싹 갈아 엎어야 하나.”

“……!”

“아, 죄송합니다. 하시려던 말씀 계속하세요. 부길드장님, 그다음에 뭐라고요?”

진태경의 물음에 홀로 일어난 임원이 굳은 얼굴로 최민우를 바라보았다.

“기왕 이렇게 된 거 한 말씀 드리겠습니다.”

이번만큼은 절대 물러서지 않겠다는 결의가 담긴 목소리에 몇몇 임원들이 눈을 번뜩였고, 최민우는 담담하게 고개를 끄덕였다.

“네, 말씀하십시오.”

“그럼 일찍 퇴근해도 되겠습니까?”

“…….”

“사실 오늘이 결혼기념일이라…….”

다른 임원들이 짜게 식은 눈빛으로 동료를 바라보았다.

그는 이미 삼 년 전에 이혼한 돌싱이었다.



* * *



내가 아는 최 팀장은 퍽 합리적인 사람이다.

설령 상대를 찍어 누를 힘이 있어도 적당한 선에서 물러날 줄 알고, 최대한 침착하고 부드러운 분위기 속에서 일을 마무리 짓고는 했다.

말인즉슨, 어지간한 일로는 수십여 명의 임원들을 말 몇 마디로 돌려보낼 사람이 아니라는 뜻이다.

그래서 더더욱 궁금할 수밖에 없었다. 갑작스럽게 찾아왔다는 손님의 정체가.

띵.

“그 사람 때문이죠? 중요한 손님이라는.”

전용 엘리베이터 문이 닫히자마자 입을 연 내게, 최 팀장이 대답했다.

“반반입니다. 임원들을 불러 모은 건 다독이기 위해서였으니까요. 말썽이 일어날 만한 소지는 처음부터 없었습니다.”

“하긴 지금까지 남아 있는 임원들은 대부분 우호적이긴 하죠.”

“설령 불만을 품은 자가 있더라도 이번 공공화 건은 길드 차원에서 반대할 이유가 없었습니다.”

“천태……. 아니, 최 팀장님 외조부께서 아직 건재하다는 뜻이기도 하니까?”

“네. 지금껏 아레스 길드의 위상이 예전만큼 못했던 이유는 외조부님의 부재 때문이었습니다. 그런 의미에서 보자면 그분의 명성을 이용하자는 진태경 씨의 제안이 우리 모두에게 최선이었던 셈이죠.”

확실히 이 세상에서 천태민이라는 사람의 존재는 치트키나 다름없다.

그는 이름 석 자만으로 전 세계의 이목을 집중시키고, 어딘가에 숨어 빈틈을 노리고 있을 승냥이들을 뒷걸음질 치게 만드는 거인이니까.

마치…….

‘그래, 무신(武神)처럼.’

문득 머릿속을 스친 생각이 혀끝을 맴돌다 흩어진 그때.

최 팀장이 나직한 목소리로 말을 이었다.

“하지만 아레스 길드의 임원들과는 달리, 다른 누군가에게는 썩 달갑지 않은 소식이었을 겁니다.”

“다른 누군가라면…….”

최 팀장이 손을 내밀어 무언가를 건넸다.

“이 명함의 주인이죠.”

띵.

엘리베이터 문이 열렸다. 우리는 이미 지시에 따라 텅 비워진 복도를 가로지르며 대화를 이어 갔다.

“명함? 이게요?”

나는 미간을 좁힌 채 막 받아 든 물건을 바라보았다.

크기나 형태는 딱 명함이긴 한데, 이걸 정말 명함이라고 부를 수 있는지가 의문이다.

백금색으로 번쩍이는 그것에는 이름이나 직책, 심지어는 번호조차 적혀 있지 않았으니까.

그나마 짐작할 수 있는 건 이 명함의 소유자가 엄청난 대부호라는 것 정도였다.

“이거, 생각보다 묵직한 걸 보니까 겉만 그런 게 아니라 진짜 백금 같은데. 혹시 상대가 중동 왕족이에요?”

“그랬다면 회의를 끝마치고 왔을 겁니다.”

“그럼?”

“명함 끄트머리 부분을 잘 살펴보십시오.”

나는 최 팀장의 말을 따라 다시 한번 명함을 유심히 관찰했다.

그제야 앞뒷면으로 두 마리의 새가 음각(陰刻)되어 있는 것이 보였다.

“이건.”

“어떤 종류의 새인지 알아보시겠습니까?”

“글쎄요.”

“까마귀입니다.”

“까마귀?”

“정확한 이름은 후긴(Huginn)과 무닌(Muninn)이죠.”

“아니, 무슨 까마귀가 이름이 있어요? 까마귀면 까마귀인 거지.”

“관심이 없는 사람이라면 모를 수도 있습니다. 신화 속에 등장하는 존재니까요.”

“신화?”

“예, 고대 북유럽 신화 말입니다.”

저벅. 저벅.

유난히도 크게 울려 퍼지는 발소리. 서서히 가까워지는 집무실 문을 바라보며 최 팀장이 말을 이었다.

“후긴과 무닌. 이 두 까마귀는 바로 그 북유럽 신화에 등장하는 어느 신을 상징하는 존재입니다.”

“그게 누군데요?”

“오딘(Odin).”

“……!”

“많이 들어 본 이름이죠. 아닙니까?”

잠시 침묵하던 나는 고개를 끄덕였다.

후긴과 무닌이라는 이름은 오늘 처음 들어 봤지만, 오딘은 다르다.

‘그래, 아주 다르지.’

단지 어디선가 한 번쯤 들어 봤을 만큼 유명한 신이라서, 혹은 어릴 적 재미있게 봤던 히어로 영화에 등장했던 캐릭터여서가 아니다.

오딘이라는 두 글자는 전 세계를 막론하고 누구나 아는 이름이었다.

바로 그 오딘이야말로…… 모두가 인정하는 세계 최고의 길드(Guild)니까.

저벅.

어느덧 찾아온 마지막 발걸음.

우리 앞을 가로막은 문 너머에서 정갈하게 갈무리된 거대한 기운이 느껴진다.

최 팀장의 담담한 목소리가 조용한 복도 위를 미끄러졌다.

“갑시다.”

달칵.

마침내 문이 열리고.

벽난로 앞에 서 있던 한 사람이 천천히 돌아섰다.



* * *



처음에는 모두가 사소한 해프닝이라고 생각했다.

일은 바빴고, 당장 처리해야 할 여러 가지 문제로 정신이 없었으며, ‘그 일’은 눈 깜짝할 사이에 일어나고 끝났었으니까.

하지만 그것은 결코 사소한 해프닝이 아니었고, 그 사실을 가장 먼저 알아차린 것은 증거 보관실에서 근무하던 막내 직원이었다.

“저어, 과장님. 증거품이 비는 것 같은데요?”

“뭐? 그게 무슨 소리야?”

“아니, 지금 막 수량 체크를 해 보니까 하나가 비는 것 같아서…….”

“인마, 헛소리할 시간에 다시 체크해. 일주일 넘게 보관실에서 물건 뺀 적도 없는데 무슨.”

눈살을 찌푸린 과장은 다리를 꼰 채 주식 창을 훑어봤다.

불과 삼십 분 후, 뒤통수를 긁적이며 사라졌던 막내 직원의 한마디를 듣기 전까지는.

“과장님, 정말 비는 것 같습니다. 석고준 관련 품목에서 하나가 사라졌어요.”

“야, 아까 내가 말했지. 일주일 동안 보관실 잠겨 있었다고. 가뜩이나 하한가라 열 받는데 자꾸 헛소…….”

신경질적으로 대꾸하던 과장이 문득 말을 멈췄다.

“지금 뭐라고?”

막내 직원이 주눅 든 얼굴로 대답했다.

“말씀드렸잖아요. 진짜 사라졌다니까요.”

“아니, 그거 말고. 바로 뒤에, 뭐라고?”

“네? 아, 석고준 관련 품목이요?”

“……!”

다시 한번 막내 직원의 입에서 흘러나온 이름 석 자에, 과장은 등골이 서늘해지는 것을 느꼈다.

석고준이라니.

다른 것도 아니고, 석고준 사건 관련 증거품이 사라졌다니.

“야, 문. 문! 보관실 당장 열어! 애들도 당장, 아니다. 아직은 부르지 마!”

황급히 자리에서 일어난 과장은 증거 보관실로 달려갔다.

그리고 막내 직원과 함께 몇 시간에 걸쳐 보관실을 이 잡듯이 뒤진 후, 비로소 깨달았다.

‘이런 씨바…….’

없다. 정말로 사라져 버렸다.

저 어리바리한 막내 직원의 보고는 단순한 헛소리가 아니었고, 엊그제 자신이 샀던 주식이 하한가를 치는 것 따위는 이제 아무런 문제도 되지 못했다.

이 사실이 알려지면 그의 인생 자체가 하한가를 쳐 버릴 테니까.

‘도대체 이게 무슨.’

넋이 반쯤 나간 과장은 멍한 얼굴로 증거 보관실을 둘러보았다. 도무지 이해할 수 없는 일이었다.

마지막으로 품목을 체크했던 것이 불과 지난주의 일이다.

그런데 지난 일주일간 누구도 드나들지 않았던 보관실에서 물건 하나가 감쪽같이 사라졌다.

심지어는 증거품 하나하나에 설치된 도난 방지 마법과 보관실 전체에 걸린 경보 마법도 작동하지 않았다.

‘그것도 하필이면 석고준 관련 증거라니.’

증거품이 사라진 것만으로도 이미 시말서를 써야 할 일이지만, 석고준에 관련된 증거품이 사라졌다면 어지간한 징계로는 끝나지 않는다.

이미 중요한 것들은 상부에서 수거해 갔다고는 해도 워낙에 큰 사건이었으니.

“……돌겠네, 진짜.”

과장은 눈앞이 캄캄해지는 것을 느꼈다. 공무원 명줄이 아무리 길어도 쇠심줄이 아닌 이상 잘리기 마련이다.

집에서 기다리고 있을 호랑이 같은 마누라와 토끼 같은 자식들을 생각하니 도무지 이 사실을 알릴 엄두가 나지 않았다.

‘그래, 묻자. 지금 당장은 묻고 상황을 살펴보는 거야.’

아직 뭣도 모르는 막내 직원만 잘 구슬리면 나중에라도 수를 낼 수 있다.

마음을 굳힌 과장은 세상에서 가장 친절한 목소리로 넓은 보관실 어딘가에 있을 막내 직원을 불렀다.

“거기 있니?”

“아, 예. 방금 왔어요.”

“어디 다녀왔구나. 그래, 일단 이리 좀 와 봐. 내가 너한테 긴히 할 이야기가 있는데…….”

그리고 돌아선 그 순간, 과장은 볼 수 있었다.

초롱초롱하게 눈을 빛내고 있는 막내 직원과 그의 뒤에서 철탑처럼 서 있는 보안팀장을.

“뭡니까? 문제가 생겼다고 들었는데.”

“……?”

“김 과장님?”

시발, 좆 됐다.

간신히 욕설을 삼킨 과장이 절망적인 어조로 입을 열었다.

“사라졌습니다.”

“예?”

“석고준의 유품으로 들어왔던 목걸이. 그게 사라졌다고요.”
```

## Final English reading copy

```markdown
# Chapter 730

Knock. Knock.

The sudden sound of someone knocking drew everyone’s eyes toward the door.

Even the janitor at Ares Guild knew that the entire leadership was gathered in the conference room to discuss something important.

So if someone knocked on the door under circumstances like these, there were only two possibilities.

Either the matter was that important—or they had already written their resignation letter.

And unlike Seok Go Jun, who would have started by spitting out every curse in the book, their new City Lord didn’t so much as twitch an eyebrow despite having his favorable momentum interrupted.

“Come in.”

Click.

A middle-aged man appeared through the half-open door.

He held the title of Chief Secretary, and he immediately approached Choi Minwoo and bowed.

“I’m sorry to interrupt the meeting, Vice Guild Master.”

Choi Minwoo answered calmly.

“It’s fine. Assuming you have a good reason.”

The Chief Secretary swallowed hard.

Although he had only been employed for a short time, he knew very well that the employer before him was clear about rewarding and punishing people.

On top of that, the report that had just come up from the lobby’s Security Team one minute earlier was not something he could handle on his own.

“An important guest has arrived.”

The Chief Secretary extended a trembling hand.

Choi Minwoo’s eyes sank as he looked at the object being offered to him.

*This is…*

Several thoughts flashed through his mind the instant he realized what it was.

But his hesitation was brief. Choi Minwoo made up his mind.

“Where is the guest?”

“Still in the lobby…”

“Take them to my private office. I’ll be there shortly.”

“Yes, sir.”

The Chief Secretary answered as though he had been waiting for those words and left the conference room. Choi Minwoo turned toward the executives seated around the table.

“It seems we’ve more or less finished discussing the urgent matters. What do you all think?”

“Pardon?”

“Vice Guild Master, are you saying…?”

“If you would all understand, I think we should end today’s meeting here.”

Several executives stared at Choi Minwoo with stunned expressions.

This was too much, no matter how they looked at it.

Even if an important guest had arrived, how could he end a meeting attended by every overseas Branch Leader like this?

Scrape.

“Vice Guild Master!”

The moment one executive gathered his courage and shot to his feet—

Bam!

A sudden thunderclap swallowed his voice.

Jin Taekyung had left the imprint of his palm in the alloy table. He muttered:

“Did they lay eggs or something? What kind of damn bugs keep flying around? Should we tear up the conference room again?”

“……!”

“Oh, sorry. Please continue what you were saying. Vice Guild Master, what was it after that?”

At Jin Taekyung’s question, the executive who was still standing looked at Choi Minwoo with a stiff expression.

“Since things have turned out this way, I’d like to say something.”

His voice carried the determination not to back down this time. Several executives’ eyes gleamed, and Choi Minwoo calmly nodded.

“Yes, go ahead.”

“Then may I leave work early?”

“…….”

“Today is my wedding anniversary, actually…”

The other executives looked at their colleague with eyes that had gone ice-cold.

He had been divorced for three years already.

* * *

The Team Leader Choi I knew was a very reasonable person.

Even if he had the power to crush someone, he knew when to back off, and he usually wrapped things up in an atmosphere that was as calm and gentle as possible.

In other words, he wasn’t the sort of person who would send dozens of executives home with a few words over just any matter.

Which only made me more curious about the identity of the guest who had arrived so suddenly.

Ding.

“You ended the meeting because of that person, right? The important guest?”

The moment the private elevator doors closed, I spoke up. Team Leader Choi answered:

“Half and half. I called the executives together to reassure them. There was never any room for trouble to begin with.”

“True. Most of the executives who remain are friendly, after all.”

“Even if someone had complaints, there was no reason for the Guild to oppose making this public.”

“Because it also suggests that Cheon Tae… no, that your maternal grandfather is still going strong, Team Leader Choi. Right?”

“Yes. The reason Ares Guild hasn’t enjoyed its former standing is my maternal grandfather’s absence. In that sense, Mr. Jin’s proposal to use his fame was the best option for all of us.”

There was no denying that the existence of a man named Cheon Taemin was practically a cheat code in this world.

With only his name, he could draw the attention of the entire world and make the hyenas lurking somewhere, waiting for an opening, take a step backward.

Just like…

*That’s right, like the Martial God.*

The thought that had suddenly crossed my mind lingered at the tip of my tongue before scattering.

Team Leader Choi continued in a low voice.

“But unlike the executives of Ares Guild, this must have been unwelcome news to someone else.”

“Someone else being…”

Team Leader Choi held out his hand and gave me something.

“The owner of this business card.”

Ding.

The elevator doors opened. We continued our conversation as we crossed the empty corridor that had been cleared according to his instructions.

“A business card? This is?”

I frowned as I looked at the object I had just received.

Its size and shape were exactly those of a business card, but I wondered whether it could really be called one.

The shining platinum-colored card did not have a name, a title, or even a phone number written on it.

The only thing I could guess was that its owner was an unimaginably wealthy magnate.

“This is heavier than I expected. It’s not just the appearance—it’s actually platinum. Is the other person Middle Eastern royalty?”

“If that were the case, I would have finished the meeting and come.”

“Then what?”

“Take a close look at the edge of the card.”

Following Team Leader Choi’s words, I examined the card again.

Only then did I notice that two birds had been engraved on the front and back.

“This is…”

“Do you recognize what kind of birds they are?”

“Not really.”

“They’re ravens.”

“Ravens?”

“Their exact names are Huginn and Muninn.”

“What, ravens have names? A raven is a raven.”

“Someone without an interest in the subject might not know. They’re creatures from mythology.”

“Mythology?”

“Yes. Ancient Norse mythology.”

Step. Step.

The footsteps rang unusually loudly as they drew closer. Looking toward the office door that was slowly approaching, Team Leader Choi continued.

“Huginn and Muninn are two ravens from that very Norse mythology. They symbolize one of its gods.”

“Who?”

“Odin.”

“……!”

“It’s a name you’ve heard many times, isn’t it?”

I remained silent for a moment before nodding.

I had heard the names Huginn and Muninn for the first time today, but Odin was different.

*Yes, very different.*

Not merely because he was a famous god whose name everyone had heard at least once, or because he had appeared as a character in the superhero movies I had enjoyed as a child.

The two syllables of Odin were known by everyone, regardless of where they lived in the world.

Because that Odin was…

the world’s greatest Guild, recognized by everyone.

Step.

The final footstep arrived.

Beyond the door blocking our way, I could feel a massive energy neatly contained.

Team Leader Choi’s calm voice slid across the quiet corridor.

“Let’s go.”

Click.

At last, the door opened.

A person standing before the fireplace slowly turned around.

* * *

At first, everyone thought it was a minor incident.

Work had been busy, everyone had been preoccupied with various problems that needed immediate attention, and *the incident* had happened and ended in the blink of an eye.

But it was no minor incident at all.

The first person to realize that was the youngest employee working in the evidence storage room.

“Um, Manager. I think some of the evidence is missing.”

“What? What are you talking about?”

“I just checked the inventory, and it looks like one item is missing…”

“You idiot, check again instead of wasting time talking nonsense. Nothing’s been taken out of the storage room in over a week.”

The manager frowned and continued scrolling through his stock screen with his legs crossed.

That was what he was doing until thirty minutes later, when he heard the words of the youngest employee, who had disappeared while scratching the back of his head.

“Manager, I really think something’s missing. One item from the Go Jun-related evidence is gone.”

“Hey, I told you before. The storage room has been locked for a week. I’m already pissed because my stock hit limit down, so stop talking no—”

The manager stopped speaking mid-sentence.

“What did you just say?”

The youngest employee answered with a cowed expression.

“I told you. It really is gone.”

“No, not that. What did you say right before that?”

“Huh? Oh, the Go Jun-related evidence?”

“……!”

At the three syllables that once again slipped from the youngest employee’s mouth, the manager felt a chill run down his spine.

Go Jun.

Not just anything, but evidence related to the Go Jun incident had disappeared.

“Hey, the door. The door! Open the storage room right now! Get the others too—no, wait. Don’t call them yet!”

The manager leaped to his feet and ran toward the evidence storage room.

Then, after spending several hours tearing the place apart with the youngest employee, he finally realized the truth.

*For fuck’s sake…*

It was gone.

It had really disappeared.

The report from that clueless youngest employee had not been nonsense, and the stock he had bought two days ago hitting the limit-down price no longer mattered at all.

If this became known, his entire life would hit the limit-down price.

*What the hell is this?*

Half out of his mind, the manager stared blankly around the evidence storage room. It was completely incomprehensible.

The last time the inventory had been checked was only last week.

Yet an item had vanished without a trace from a storage room no one had entered during the past week.

Even the anti-theft Magic installed on each piece of evidence and the alarm Magic covering the entire storage room had not activated.

*And it had to be evidence related to Go Jun.*

The mere disappearance of evidence was already enough to require him to write an incident report, but if evidence related to Go Jun had disappeared, this would not end with ordinary disciplinary action.

Even if the higher-ups had already collected the important items, it had been an enormous case.

“Seriously, I’m screwed.”

The manager felt the future go dark before his eyes. A civil servant’s lifeline might be long, but it wasn’t a steel cable. It could still be cut.

When he thought of his tiger-like wife and rabbit-like children waiting at home, he couldn’t bring himself to report what had happened.

*That’s right. Bury it. For now, bury it and see how things develop.*

If he could just sweet-talk the clueless junior employee, he might still be able to figure something out later.

Having made up his mind, the manager called out to the youngest employee somewhere in the vast storage room in the kindest voice he could muster.

“Are you there?”

“Ah, yes. I just got here.”

“You went somewhere. Come over here for a moment. I have something important to discuss with you…”

Then the manager turned around—and saw them.

The youngest employee, his eyes shining brightly, and behind him, the Security Team Leader standing like an iron tower.

“What is it? I heard there was a problem.”

“……?”

“Manager Kim?”

*Shit. I’m fucked.*

The manager barely swallowed the curse and spoke in a desperate tone.

“It’s gone.”

“Pardon?”

“The necklace that came in with Go Jun’s personal effects. It’s gone.”
```
