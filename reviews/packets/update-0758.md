<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0758.txt",
      "sha256": "1777b6378ad29b0ad9e2fde6a7398a7756b14672db3ee8d273566db003284f05",
      "bytes": 13311
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "432ff1e47d53b43da9d2cb46a41034fd3561f070cf3d95ea2a59c67a0f1d60c1",
      "bytes": 1807
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3765724f3ba8cb5acb79dc4fe9443e9bb8af6292d2c28966b2266cb2eeb28555",
      "bytes": 219337
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "0462d3ac439c46aac408a536f8a20c601d5595a06ff054ef45b869c461bcf447",
      "bytes": 752
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "dc4fdab67566601b11ba515bbc12476879553d34d3bb50713cb390561d27a106",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "fa107251bbc7a5d404012edfc8f3e99d5f5ea00c1aae87895bcec2be6a0c5fdb",
      "bytes": 2299
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "07a1ec40b6890ba3cba676839894208668ae1fbfd493c09cfb71e2d9ffa449d0",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "73f2c8fa4ebffd513275bf69569dbb49b4d86cea92e74b9d8a3f33b354b114a7",
      "bytes": 1012
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c637d4bb5b9f4daf19c6c2fe8ff494ff32ff818f07978ef90359bdda3ce1d1c3",
      "bytes": 234511
    }
  ],
  "estimated_tokens": 9952
}
-->

# Durable State Update — Chapter 758

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 758. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 758. Profile updates may replace only one
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
  "chapter": 758,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 758,
    "continuity_sources": [758],
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
    "Leviathan is dead after Jin Taekyung's final strike, ending the deep-sea hunt.",
    "Jin secretly stored Leviathan's corpse and the two Japanese-government S-rank Magic Gems in his Inventory while publicly claiming they were destroyed.",
    "Jin suspects Michael Silbert lured Leviathan with an unrefined S-rank Magic Gem, but he has no proof.",
    "Jin's Broken Body debuff and battle fatigue remain active.",
    "Jin acquired the Hope of the Sea Title after the Aquatic Rescue Worker Title was enhanced and renamed.",
    "The Main Quest: Cataclysm remains unresolved.",
    "Jin accepted Germany's request for assistance with the probable Berlin Monster Wave.",
    "Germany also requested Michael Silbert's assistance, setting up a possible confrontation in Berlin.",
    "Global media and public opinion are turning back toward Jin, and the anti-Jin protest has collapsed."
  ],
  "continuity_sources": [
    757
  ],
  "open_questions": [
    "What does the Main Quest: Cataclysm require, and what vast change is approaching?",
    "Can Jin prove that Michael Silbert lured Leviathan with an unrefined S-rank Magic Gem?",
    "What did Leviathan mean by saying that humanity and the world awakened it?",
    "What are the full effects of the Hope of the Sea Title?",
    "How will Jin and Michael Silbert's simultaneous involvement affect the Berlin Monster Wave operation?"
  ],
  "safe_through": 757,
  "temporary_decisions": [
    "Render 망가진 신체 as Broken Body.",
    "Render 수상 구조대원 as Aquatic Rescue Worker.",
    "Render 바다의 희망 as Hope of the Sea.",
    "Render 격변 as Cataclysm in the Main Quest title, distinct from 대격변 as Great Cataclysm.",
    "Render 때가 되었다 as The time has come."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 삼류     | **Third Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 평화 | **Peace Guild** | Guild name. |
| 대한민국 | **Korea** | Country reference. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 뮌헨 | **Munich** | Second word in one of the necromantic chants. |
| 아프리카 | **Africa** | Region where terrorist organizations are reportedly conducting Gate and Magic Gem experiments. |
| 재생 | **Regeneration** | The masked man's rapid recovery from shattered bones and severe wounds. |
| 오딘 | **Odin** | The name of the world's greatest Guild, invoking the Norse god. |
| 파리 | **Paris** | The city containing Ares Guild's branch attacked at the chapter's end. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 독일 | **Germany** | Country requesting assistance with the Berlin Monster Wave. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 756
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he remains unconscious after more than twenty years in a wired mechanical capsule at his former mansion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 757
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 757
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, a traveler between Murim and another world resembling the realm of immortals, the creator of the beginner-accessible Smiling Mana Cultivation Method, and a practitioner of the Turtle Breath Technique learned from the Slaughter Saint who has acquired the Hope of the Sea Title, triggered the Cataclysm Main Quest, secretly stored Leviathan's corpse and two S-rank Magic Gems in his Inventory, and accepted Germany's request for aid in Berlin.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 757
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 757
- **Aliases:** None
- **Role:** Michael Silbert is the Guild Master of Odin Guild, a public hero who helped suppress five Monster Waves, the hidden architect of a coordinated terrorist campaign designed to isolate Ares Guild, the leader of a Guild controlling more than two hundred effectively owned Gates through permanent leases, and a feared rival whom Germany has also asked to assist with the Berlin Monster Wave.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, and regards Jin Taekyung as a serious adversary.

## Korean source

```text
＃758화



“동시에…… 미카엘 실베르트에게도 지원을 요청했습니다.”

최 팀장으로부터 불쑥 튀어나온 이름.

미카엘 실베르트.

순간 멈칫했지만, 크게 놀랍지는 않았다.

물에 빠진 사람이 사방에 손을 뻗는 건 당연한 일이니까.

지금의 독일 정부는 곧 들이닥칠 재앙을 감지했고, 자신들을 구해 줄 최고의 안전 요원을 목놓아 불렀을 뿐이다.

나, 그리고 미카엘 실베르트를.

“그 칙칙하고 불쾌한 인간 놈 말이냐?”

스켈레톤 킹이 께름칙하다는 표정으로 말을 이었다.

“그놈이랑 마주치는 건 되도록 피하고 싶은데.”

“이 자리에 그러고 싶은 사람 아무도 없어.”

내 대꾸에 녀석은 입맛을 다셨다.

“그거야 그렇지만, 그 인간은 정말 처음 본 그 순간부터 느낌이 영……. 아니, 됐다. 여하튼 그놈들보다는 우리가 일찍 도착해야겠군.”

이건 누가 더 많은 인명을 구하는지 겨루는 스포츠 따위가 아니었지만, 스켈레톤 킹이 마지막으로 덧붙인 말에는 나 역시 동의하는 바였다.

‘이대로 흘러간다면 누구도 놈을 막지 못해.’

철저하게 조작된 이 재앙의 가장 큰 수혜자는 누가 뭐라 해도 미카엘 실베르트다.

오딘 길드는 첫 테러부터 지금까지 전 세계 곳곳에서 10회가 넘는 몬스터 웨이브를 진압했고, 미카엘 실베르트는 그중 대부분의 전투에서 S급 몬스터를 쓰러트리며 엄청난 전공을 세워 환호를 받았다.

잠시나마 사람들로부터 천태민이라는 이름을 잊게 할 정도로.

‘지금이라도 멈춰야 한다. 어떻게든.’

나는 미카엘 실베르트가 원하는 궁극적인 목표가 무엇인지는 모른다.

그러나 저런 괴물이 이대로 무소불위의 명성과 권력을 손에 넣는다면, 천태민과 같은 신성불가침(神聖不可侵)의 반열에 도달한다면…….

지금보다 더한 재앙이 일어나리라는 것쯤은 확신할 수 있었다.

“최 팀장님.”

내 부름의 의미를 이해한 최 팀장이 고개를 끄덕였다.

“이미 파일럿들이 대기 중입니다.”

한시라도 빨리 움직여야만 하는 상황.

나와 최 팀장, 그리고 스켈레톤 킹은 이미 준비되어 있는 항공기를 향해 걸음을 재촉하며 대화를 주고받았다.

“현재 독일 쪽 상황은요?”

“뮌헨을 중심으로 2급 재난 경보가 발령됐습니다. 독일 정부가 제공한 정보에 따르면, 늦어도 다섯 시간 안에는 몬스터 웨이브가 발생할 겁니다.”

“정부가 말하는 맥시멈이 다섯 시간이라는 건…….”

최 팀장이 고개를 끄덕였다.

“사실상 언제 터져도 이상하지 않은 수준이죠.”

불행 앞에서 희망 회로를 돌리는 건 만국 공통이다. 아니, 적어도 사람들을 대피시켜야 하는 정부는 그렇게 해야만 한다.

당장 이런 상황에서 독일 정부가 “우린 좆 됐습니다.”를 공식적으로 인정하는 순간, 뮌헨이라는 대도시가 단숨에 혼란으로 아수라장이 되어 버릴 테니까.

“빌어먹을.”

“다행히도 지금까지의 대처는 훌륭한 편입니다. 파리 지부 테러 사건 이후로 전 세계 각국이 촉각을 곤두세우고 있었고, 2급 재난 경보 발령 이후 지금까지 삼천 명이 넘는 헌터가 뮌헨에 집결했습니다. 저희 아레스 길드도 그중 하나고요.”

“그나마 낫군. 그럼 오딘, 아니 그 인간은?”

스켈레톤 킹의 물음에 최 팀장이 대답했다.

“물론 뮌헨에도 오딘 길드 지부의 헌터들이 대기 중이지만…… 미카엘 실베르트가 이끄는 핵심 전력은 현재 아프리카에 있습니다.”

“아프리카?”

“예. 입수한 정보에 따르면, 현재 남아공에서 발생한 몬스터 웨이브를 진압하고 있다더군요. 그곳에서의 일을 마무리 짓고 즉시 뮌헨으로 향할 겁니다.”

“팔자 좋은 인간이군. 우선 여기저기 일을 벌여 놓고 차례대로 수습하겠다 이건가?”

스켈레톤 킹이 비아냥거렸지만, 나는 고개를 저었다.

“그게 아냐.”

“응?”

“애초에 계산에 들어 있던 거라면 지금쯤 뮌헨으로 출발했겠지. 그러니까 적어도 뮌헨에서의 일은, 놈의 손이 닿은 테러가 아니었던 거야.”

“맞습니다. 그래서 더 위험한 거고요.”

“그게 왜 더 위험하지? 놈의 의도가 아니라면 오히려…….”

흐려지는 말꼬리.

나와 최 팀장이 주고받는 말에 의아한 표정으로 되묻던 스켈레톤 킹의 얼굴이 굳었다.

“아.”

녀석도 이제야 눈치챈 모양이다.

이번 사태가 무엇을 의미하는지, 또 얼마나 거대한 위험과 불안감을 품고 있는지.

‘이제는 인위적인 테러가 아니어도, 몬스터 웨이브가 자연히 발생할 수 있다.’

물론 평화가 찾아온 이후에도 몬스터 웨이브 현상은 있었다.

그러나 문제가 되는 점은, ‘아주 가끔’이었던 재앙의 빈도가 ‘종종’ 혹은 ‘자주’라는 단어로 교체될 만한 수준에 다다랐다는 사실이었다.

시체가 산처럼 쌓이고, 핏물이 강이 되어 흐르던 그 시절을 인류로 하여금 떠올리게 할 만큼.

대격변(大激變).

인류는 그 참혹했던 과거를 저 세 글자에 담아 기록했다. 하지만 지금 이 순간, 나는 문득 의문이 들었다.

지금부터 시작될, 어쩌면 이미 시작되었을 새로운 재앙의 시대는 어떤 이름으로 기억될까.

그리고…….

내게 행복과 고통을 동시에 안겨 준 이 시스템은, 도대체 내게 무엇을 말하고 싶은 걸까.

‘퀘스트창 오픈.’

띠링.



퀘스트



[격변]



어느덧 새로운 시대는 눈앞까지 다가왔고, 이 길고도 치열한 이야기의 마지막 단어는 아직 정해지지 않았습니다.

희망. 혹은 절망.

그리고 지금 이 순간, 펜을 쥔 유일한 사람은 당신입니다.

무운(武運)을 빕니다.



등급 : 메인 퀘스트

제한 : 진태경

임무 : ???

보상 : ???

실패 : ???





정확한 답이 없는 퀘스트 설명과 물음표로 채워진 임무.

그러나 다른 무엇보다 내 가슴을 무겁게 짓누르는 것은 바로 퀘스트 등급에 적힌 짤막한 한 줄이었다.

아프도록 눈을 파고드는 저 다섯 글자.

‘메인 퀘스트(Main Quest).’

나는 지금까지 헤아릴 수 없이 많은 퀘스트를 받았다.

가장 쉬운 삼류부터 목숨을 걸어야 하는 초절정에 이르기까지. 난이도에 따라 등급도 달랐고 돌발 퀘스트와 같은 종류도 있었다.

하지만…… 메인 퀘스트는 처음이다.

정확히는, 처음으로 무림이라는 낯선 세상에서 눈을 떴던 그때 이후로 처음이다.

그래, 모든 것이 시작되었던 그날 이후로.

‘이게 도대체 뭘 의미하는 거지?’

임무가 뭔지는 모른다. 곧 다가올 새로운 시기가 무엇을 뜻하는지도 알지 못한다.

아니, 내심 짐작하면서도 애써 그것만은 아닐 것이라 부정하고 있다.

두려우니까.

시스템이 말한 것처럼, 지금 이 순간 펜을 쥔 사람은 오직 나뿐이니까.

사이다로 가득한 웹소설을 보며 낄낄거렸던 것은 이미 오랜 과거의 일. 이제는 내가 직접 이야기를 써 내려가야 한다.

펜으로. 창으로.

누구의 것인지 모를 피와 죽음으로.

“……간. 인간?”

저 멀리서 들려오는 듯하던 목소리가 생각에 잠겨 있던 정신을 일깨웠다.

눈을 깜빡이며 둘러본 주위는 새로운 얼굴들과 소음으로 가득했다.

요란한 소리를 내며 회전 중인 프로펠러. 전투기의 창 너머로 보이는 파일럿들의 긴장한 얼굴.

그리고 걱정스러운 표정으로 나를 바라보는 두 사람.

아니, 한 사람과 한 몬스터.

“진태경 씨, 괜찮으십니까?”

“간악한 인간이여. 잘 봐라. 지금 내가 편 손가락이 몇 개지?”

나는 코앞에서 천천히 손을 흔드는 스켈레톤 킹을 바라보았다.

“하나도 안 보이는데.”

“틀렸다. 하나다. 이거 생각보다 상태가 심각…….”

“아, 지금 흔들고 있는 손가락은 곧 내가 뽑아 버릴 거라서 일부러 안 센 건데.”

“…….”

“아직도 흔들고 있네. 좋게 말할 때 손가락 접어라.”

신나게 중지를 흔들어 대던 스켈레톤 킹이 조용히 손가락을 접는 사이, 최 팀장이 가라앉은 목소리로 입을 열었다.

“혹시 문제가 있다면 휴식 후 이동하겠습니다. 어떤 S급 몬스터가 출현할지는 모르지만, 일단 현지에도 그에 대응할 만한 병력이 있으니…….”

“아닙니다. 괜찮아요.”

나는 단호하게 최 팀장의 말을 가로막았다.

비록 정신적인 피로에 [망가진 신체]의 디버프 효과로 몸이 예전 같지는 않지만, 늦으면 늦을수록 피해가 커질 것이 불 보듯 뻔하다.

지금 내게 주어진 임무는 재앙을 막는 것이다.

뮌헨에서 일어날 재앙. 더 나아가 이 세상을 집어삼킬 재앙을.

“출발하죠. 더 늦기 전에.”

나는 짤막한 말과 함께 전투기에 올랐다.

재앙의 중심에 있는 한 사람의 이름. 곧 다시 마주할 적을 떠올리며.

‘미카엘 실베르트.’

와라, 뮌헨으로.

놈에게 닿지 않을 그 중얼거림이 입 안을 맴돌다 흩어졌다.



* * *



남아프리카 공화국.

대한민국에서는 흔히들 남아공이라 부르는 이 나라는 아프리카에서도 가장 고도화된 산업국이자, 게이트가 적어 대격변부터 지금까지 몬스터에 의한 피해가 가장 적은 국가 중 하나였다.

적어도 반나절 전까지는.

쿠구구궁!

화염을 동반한 매연이 쾌청한 하늘을 가린다.

전 세계의 부호와 수많은 관광객들이 드나드는 남아공의 수도, 케이프 타운(Cape Town)은 현재 비명과 죽음, 그리고 몬스터가 내지르는 괴성으로 가득했다.

퍼걱! 콰직!

“크아아아아!”

“커헉!”

도로를 점거하며 달려든 트롤 무리가 손에 쥔 곤봉을 닥치는 대로 휘둘렀다.

대형 몬스터 특유의 강력한 힘이 실린 강철 곤봉에, 뿔뿔이 흩어져 도망치던 사람들이 단말마와 함께 쓰러졌다.

우지지직!

- 크워어어어!

쓰러진 시신의 머리통을 밟아 터트린 우두머리가 흉포한 괴성을 내질렀다. 오랜만에 인간의 피 맛을 본 휘하의 몬스터들은 본능에 따라 움직였다.

콰드드득!

달려가던 자동차를 잡아 그대로 땅에 메다꽂고, 수십 마리가 달려들어 크고 작은 건물들을 부수어 무너트린다. 수없이 많은 폭발이 일어났으나 질긴 피부와 트롤 특유의 엄청난 재생력은 끄떡도 하지 않았다.

콰앙!

폭발과 함께 맹렬하게 솟구치는 화염.

조금의 상처도 용납하지 않겠다는 듯, 상한 가죽을 순식간에 재생시킨 우두머리가 흡족하게 웃었다.

우두머리의 크고 두꺼운 발 앞에는, 사지가 뒤틀리거나 몸통이 반으로 갈라진 헌터의 시체가 쌓여 있었다.

- 크르륵.

쉽다. 너무나 쉬웠다.

얼마 전이었다면 게이트를 넘어 자신의 영역에 쳐들어오는 인간들을 상대로 이토록 손쉽게 처리할 수 없었을 테지만, 이제는 이야기가 달라졌다.

- 그. 하. 하. 하!

세상이 변하고 있었다.

몬스터들의 육체에는 그 어느 때보다 순수하고 강력한 마력이 충만했고, 인간들은 그들을 막을 수 없었다.

모든 것이 제자리를 찾아가고 있었다.

지난 수십 년간 사냥감에서 사냥꾼으로 변모했던 인간들은…… 다시금 사냥감으로 전락했다.

- 모. 조. 리.  죽. 여. 주. 마!!

기나긴 억압의 세월.

영역마저 침범당하며 인간들에게 사냥당했던 과거의 분노가 포효가 되어 터져 나온 그 순간이었다.

쐐액, 퍼엉!

시야가 깜깜하게 물들었다. 아니, 머리가 사라졌다.

그래도 우두머리는 놀라지 않았다.

머리가 날아간다 해도 살아남는 것이 트롤이다. 몸뚱어리를 분쇄하지 않는 한, 막대한 재생력으로 살아남을 수 있었…….

쉬쉬쉬쉭, 퍼퍼펑!

파공성과 함께 우두머리의 의식이 끊겼다.

가공할 재생력도, 강철만큼이나 단단한 육신도 이 순간만큼은 무용지물이었다.

스륵, 쿵!

의문을 느낄 새도 없이 죽음을 맞이한 몸뚱어리가 무릎을 꿇었다.

우두머리의 죽음과 함께 찾아온 침묵.

- 크워?

그리고 의문과 함께 주위를 둘러보는 트롤 무리의 귓가로, 담담한 음성이 파고들었다.

“빨리 끝내지.”

저벅.

앞으로 내딛는 발걸음과 함께, 거대한 기운이 사방을 짓눌렀다.

“친구가 날 기다리고 있거든.”
```

## Final English reading copy

```markdown
# Chapter 758

“At the same time… we also requested assistance from Michael Silbert.”

The name that Team Leader Choi suddenly blurted out.

Michael Silbert.

I hesitated for a moment, but I wasn’t particularly surprised.

When someone is drowning, it’s only natural for them to reach out in every direction.

The German government had sensed the disaster that was about to descend upon them and was simply crying out for the best people who could save them.

Me, and Michael Silbert.

“You mean that gloomy, unpleasant human bastard?”

The Skeleton King continued with a displeased expression.

“I’d rather avoid running into him if possible.”

“No one here wants to run into him.”

At my retort, he clicked his tongue.

“Well, that’s true, but that human gave me a terrible feeling from the moment I first saw him… No, never mind. In any case, we need to arrive before those bastards do.”

This wasn’t some kind of sport to see who could save more lives, but I agreed with the Skeleton King’s final remark.

*If things continue like this, no one will be able to stop him.*

The greatest beneficiary of this meticulously engineered catastrophe was, without question, Michael Silbert.

From the first terrorist attack until now, Odin Guild had suppressed more than ten Monster Waves around the world. Michael Silbert had personally slain S-rank monsters in most of those battles, accomplishing spectacular feats and receiving thunderous applause.

For a while, he had even made people forget the name Cheon Taemin.

*I have to stop him now, while there’s still time. Somehow.*

I didn’t know what Michael Silbert’s ultimate goal was.

But if a monster like that gained unchecked fame and power, if he reached the same level of inviolable sanctity as Cheon Taemin…

I was certain that a disaster even worse than the current one would occur.

“Team Leader Choi.”

Understanding the meaning behind my call, Team Leader Choi nodded.

“The pilots are already waiting.”

We were in a situation where we had to move as quickly as possible.

Team Leader Choi, the Skeleton King, and I hurried toward the aircraft that had already been prepared, exchanging words as we went.

“What’s the situation in Germany?”

“A Class 2 disaster warning has been issued, centered around Munich. According to the information provided by the German government, a Monster Wave will occur within five hours at the latest.”

“The government saying five hours at the maximum means…”

Team Leader Choi nodded.

“It could happen at any moment, in practical terms.”

Running on wishful thinking in the face of disaster was a universal human trait. Or at least governments responsible for evacuating people had no choice but to do so.

The moment the German government officially admitted, “We’re fucked,” a major city like Munich would descend into chaos in an instant.

“Damn it.”

“Fortunately, their response so far has been excellent. Every country in the world has been on high alert since the terrorist attack on the Paris branch, and more than three thousand Hunters have gathered in Munich since the Class 2 disaster warning was issued. Our Ares Guild is one of them.”

“That’s something, at least. What about Odin—or rather, that man?”

Team Leader Choi answered the Skeleton King’s question.

“Of course, Hunters from the Odin Guild branch in Munich are standing by as well, but… the core forces led by Michael Silbert are currently in Africa.”

“Africa?”

“Yes. According to the information we received, they’re currently suppressing a Monster Wave that occurred in South Africa. They’ll finish up there and head straight to Munich.”

“That man has it easy. He starts trouble everywhere, then cleans it up one place at a time?”

The Skeleton King sneered, but I shook my head.

“That’s not it.”

“Hm?”

“If it had been part of his calculations from the beginning, he would have left for Munich by now. So at least the incident in Munich wasn’t a terrorist attack he had a hand in.”

“That’s right. Which is why it’s even more dangerous.”

“Why is that more dangerous? If it wasn’t his intention, then wouldn’t that actually—”

The Skeleton King’s voice trailed off.

His face, which had been filled with confusion as he questioned Team Leader Choi and me, hardened.

“Ah.”

It seemed he had finally realized it, too.

What this incident meant, and how much danger and anxiety it contained.

*Even without an artificial terrorist attack, Monster Waves can now occur naturally.*

Of course, Monster Waves had still occurred after peace had arrived.

But the problem was that disasters which had once happened *very rarely* had reached a point where their frequency could now be described as *occasionally* or even *often*.

Enough to make humanity remember the days when corpses piled up like mountains and rivers flowed red with blood.

The Great Cataclysm.

Humanity had recorded that horrific past in those three characters. But at this very moment, a question suddenly occurred to me.

What name would be given to the new age of disaster that was about to begin—or perhaps had already begun?

And…

What was this System, which had given me happiness and pain at the same time, trying to tell me?

*Open Quest window.*

*Ding.*

> **System**
>
> **Quest**
>
> **Cataclysm**
>
> The new era has already drawn close, and the final word of this long and fierce story has yet to be decided.
>
> Hope. Or despair.
>
> And at this very moment, you are the only person holding the pen.
>
> May martial fortune be with you.
>
> **Grade:** Main Quest
>
> **Restriction:** Jin Taekyung
>
> **Mission:** ???
>
> **Reward:** ???
>
> **Failure:** ???

A quest description with no clear answer, and a mission filled with question marks.

But more than anything else, what weighed heavily on my chest was the brief line written under the quest’s grade.

Those five characters that stabbed painfully into my eyes.

*Main Quest.*

I had received more quests than I could count.

They had ranged from the easiest Third Rate quests to Supreme Peak quests that required me to stake my life. Their grades differed according to difficulty, and there had been various types, such as sudden quests.

But…

This was my first Main Quest.

More precisely, it was my first one since the day I opened my eyes in the unfamiliar world of Murim.

Yes, since the day everything had begun.

*What the hell does this mean?*

I didn’t know what the mission was. I didn’t know what this new era that was about to arrive meant, either.

No. Deep down, I had an inkling, but I was desperately insisting it couldn’t be that.

Because I was afraid.

Just as the System had said, I was the only person holding the pen at this very moment.

The days when I had laughed as I read web novels packed with exhilarating wish fulfillment were long gone. Now I had to write the story myself.

With a pen. With a spear.

With blood and death whose owners I didn’t know.

“…man. Human?”

The voice that seemed to come from far away awakened my mind from its thoughts.

I blinked and looked around.

The area around me was filled with unfamiliar faces and noise.

The propeller spinning with a roar. The pilots’ tense faces visible beyond the aircraft windows.

And two people looking at me with worried expressions.

No. One person and one monster.

“Mr. Jin Taekyung, are you all right?”

“Wicked human. Look carefully. How many fingers am I holding up?”

I looked at the Skeleton King, who was slowly waving his hand in front of my face.

“I can’t see a single one.”

“Wrong. One. Your condition is more serious than I thought—”

“I deliberately didn’t count the finger you’re waving because I’m going to pull it out soon.”

“……”

“You’re still waving it. Fold that finger while I’m asking nicely.”

As the Skeleton King quietly folded the middle finger he had been enthusiastically waving, Team Leader Choi spoke in a subdued voice.

“If there’s a problem, we can move after you’ve rested. We don’t know what kind of S-rank monster will appear, but there are forces on-site capable of responding to it, so…”

“No. I’m fine.”

I cut Team Leader Choi off firmly.

Although the mental fatigue and the effects of the Broken Body debuff had left my body weaker than before, it was obvious that the later we arrived, the greater the damage would be.

The mission given to me now was to stop the disaster.

The disaster that would occur in Munich.

And, beyond that, the disaster that would swallow this world.

“Let’s go. Before we lose any more time.”

With those few words, I climbed aboard the fighter jet.

I thought of the name of the man at the center of the disaster—the enemy I would soon face again.

*Michael Silbert.*

*Come to Munich.*

The mutter that would never reach him lingered in my mouth before scattering away.

* * *

South Africa.

Commonly known in Korea by the abbreviation Nam-agong, this country was Africa’s most highly developed industrial nation. Because it had few Gates, it was also one of the countries that had suffered the least damage from monsters, from the Great Cataclysm until now.

At least until half a day ago.

*Rumble!*

Smoke mixed with flames blotted out the clear sky.

Cape Town, the capital of South Africa, where the wealthy and countless tourists from around the world came and went, was now filled with screams, death, and the grotesque cries of monsters.

*Crunch! Crash!*

“Graaah!”

“Ghk!”

A group of Trolls charged in after taking over the road, swinging the clubs in their hands indiscriminately.

The steel clubs, wielded with the powerful strength unique to large monsters, struck the people fleeing in all directions. They collapsed with dying cries.

*Crack!*

—Kwoooaar!

The leader stomped down on a fallen corpse’s head and crushed it, then let out a savage roar.

After tasting human blood for the first time in a long while, the monsters under its command moved according to instinct.

*Craaaack!*

They grabbed a moving car and slammed it into the ground. Dozens of them rushed in and smashed buildings of all sizes, bringing them down.

Countless explosions erupted, but their tough skin and the Trolls’ incredible Regeneration were completely unaffected.

*Boom!*

Flames surged fiercely with another explosion.

The leader smiled with satisfaction as its damaged hide regenerated in an instant, as if it refused to tolerate even the slightest wound.

At the leader’s large, thick feet lay the corpses of Hunters whose limbs had been twisted or whose torsos had been split in half.

—Grrrk.

Easy.

Far too easy.

If this had happened not long ago, it would not have been able to deal with the humans who crossed through the Gate and invaded its territory so effortlessly.

But things were different now.

—Ha. Ha. Ha!

The world was changing.

The monsters’ bodies were filled with purer and more powerful magical power than ever before, and the humans could not stop them.

Everything was returning to its proper place.

The humans who had transformed from prey into hunters over the past several decades…

Had once again fallen back into the role of prey.

—I. WILL. KILL. EVERY. LAST. ONE!!

It was the moment when the rage of the long years of oppression—of having their territories invaded and being hunted by humans—erupted as a roar.

*Whoosh! Boom!*

The leader’s vision suddenly went black.

No. Its head had disappeared.

But the leader was not surprised.

Trolls could survive even if their heads were blown off. Unless their bodies were pulverized, their immense Regeneration would allow them to survive—

*Whoosh-whoosh-whoosh! Boom-boom-boom!*

Along with the sound of air splitting, the leader’s consciousness snapped off.

Its terrifying Regeneration and body as hard as steel were useless at this moment.

*Slip. Thud.*

Without even having time to wonder what had happened, its body dropped to its knees.

Silence descended with the leader’s death.

—Kwo?

As the Trolls looked around in confusion, a calm voice reached their ears.

“Let’s finish this quickly.”

*Step.*

With the footstep moving forward, a colossal force bore down on everything around them.

“My friend is waiting for me.”
```
