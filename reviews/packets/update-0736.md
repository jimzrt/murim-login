<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0736.txt",
      "sha256": "c3814addfdf08583071bf443e789404aba26d0f5fa8a0839df7191bed70bad5f",
      "bytes": 15478
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "bf67e70223004a825f49120038044cc384d9d5d6c4f9f0207032b3ca3561afba",
      "bytes": 1839
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "aa041f20c3608b0941ccb414ed9f786d21c3207b25c207ac9a8ea40d1146b892",
      "bytes": 211535
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "411f8ce71ca47834f019a883bde738ca8840fe05f77a2d9f5a7ce951833e281c",
      "bytes": 553
    },
    {
      "path": "characters/Huginn.md",
      "sha256": "ec427c25ad287cd5e9f865f76a884cdbe0ce76730a33c98f0852228126296b5e",
      "bytes": 674
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "036c43f28d3f51fde77916c39ae9f04a71c847ed0779898d35de31ef429bd94c",
      "bytes": 2011
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f00629c78f5b7f7ca09ae27f3d7627ded2e17c62da75f3c0752ce8125bf777e3",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "ff9b8a278cd2ec1f484a046b19a3332d12916e88ca6b05640bc2d5923ececd22",
      "bytes": 655
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f11417b870b2fef7c2194b4e425e829d7e0d56c86f936ae4ffdf5f3ae1ed029f",
      "bytes": 224639
    }
  ],
  "estimated_tokens": 11198
}
-->

# Durable State Update — Chapter 736

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 736. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 736. Profile updates may replace only one
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
  "chapter": 736,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 736,
    "continuity_sources": [736],
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
    "Jin Taekyung, Team Leader Choi, and the Skeleton King remain together at Cheon Taemin's heavily protected mansion.",
    "Jin and Team Leader Choi have decided not to immediately confront Odin Guild because they lack a defensible pretext and would risk an Interpol wanted notice.",
    "Public sentiment supporting Jin, Ares, and the Mana Cultivation Method remains a major strategic weapon and shield.",
    "Michael is Odin Guild's Guild Master and commands a powerful hidden alliance of major figures.",
    "Michael considers the public release of the Mana Cultivation Method a foolish threat to the existing order but intends to exploit the resulting political situation.",
    "Michael regards Jin Taekyung as a dangerous and unusually daring S-rank-level power.",
    "Michael personally selected and trained Huginn as Odin Guild's fixer.",
    "Huginn recruited foreign collaborators and delivered gifts as part of Michael's operation.",
    "The Paris branch of Ares Guild was engulfed in an explosion, after which space began tearing apart around it."
  ],
  "continuity_sources": [
    734,
    735
  ],
  "open_questions": [
    "What is the source of Michael's unusually reliable intelligence?",
    "Why is Michael so certain that Cheon Taemin will not intervene?",
    "What were the gifts delivered by Huginn, and what purpose did they serve?",
    "What caused the spatial distortion centered on Ares Guild's Paris branch?",
    "How did Odin Guild obtain or prepare its Mana Cultivation Method?"
  ],
  "safe_through": 735,
  "temporary_decisions": [
    "Render 최 팀장 as Team Leader Choi.",
    "Render 샤오 양 주석 as Chairman Xiao Yang.",
    "Render 메이산 as Meishan, 쯔양 as Ziyang, and 쑤이닝 as Suining.",
    "Render 미카엘 as Michael."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 후긴 | **Huginn** | One of the two ravens associated with Odin in Norse mythology. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 마계어 | **Demon Realm language** | Language spoken by monsters from the Demon Realm. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 황하 | **Yellow River** | River along which civilization began. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 성경 | **Bible** | Proposed scripture containing Nanman's history and the word of God. |
| 오딘 | **Odin** | The name of the world's greatest Guild, invoking the Norse god. |
| 파리 | **Paris** | The city containing Ares Guild's branch attacked at the chapter's end. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 미미 | rescuer to companion snake | Mimi or Mimi-chan | informal, pleading | Taekyung calls to Mimi while asking the snake to carry him and the survivors. |
| 후긴 | 진태경 | Odin Guild messenger to an Ares Guild ally and adversary | Mr. Jin | formal-polite, increasingly coercive | Huginn addresses Jin while questioning his presence and later warns him not to lose his temper. |
| 진태경 | 후긴 | Ares Guild ally to an Odin Guild messenger and adversary | Mr. Crow | insulting-casual and profane | Jin uses the crow nickname while mocking Huginn's theatrics and threatening posture. |
| 미카엘 | 후긴 | Odin Guild Master to personally selected fixer | Huginn | formal, familiar, and commanding | Michael calls Huginn by name while inviting him into the study. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 735
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Huginn.md

# Huginn (후긴)

- **Safe through:** Chapter 735
- **Aliases:** None
- **Role:** Huginn is a powerful Odin Guild messenger, trusted field operative, and elite fixer personally selected and trained by Michael.
- **Personality:** Polished, condescending, calculating, overconfident, and absolutely loyal to his Guild Master.
- **Voice:** Formal and gentlemanly in presentation, indirect and theatrical at first, then blunt and coercive when delivering an ultimatum.
- **Relationships:** Huginn serves Odin Guild's Guild Master with absolute loyalty and acts as an adversary to Jin Taekyung and Choi Minwoo.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 735
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, a traveler between Murim and another world resembling the realm of immortals, and the creator of the beginner-accessible Smiling Mana Cultivation Method.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 735
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 735
- **Aliases:** None
- **Role:** Michael is the Guild Master of Odin Guild and one of the world's most powerful absolute authorities.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, and regards Jin Taekyung as a serious adversary.

## Korean source

```text
＃736화



분명 시작은 미미했다. 그저 약간의 떨림. 그 이상도 이하도 아니었으니까.

하지만 그것은 작은 전조(前兆)에 불과했다.

드드드득.

지면이 뒤흔들렸다.

루브르 박물관 앞에 줄지어 서 있던 관람객들이 본능적으로 몸을 숙였고, 서로의 멱살을 붙잡으며 싸움을 벌이던 파리 10구의 하층민들은 욕설과 함께 뿔뿔이 흩어졌다.

그리고 파리 6구의 시민들은…….

“아아…….”

비명을 지르는 것도 잊은 채, 넋 나간 눈빛으로 자신들의 눈앞에 펼쳐진 광경을 바라보았다.

고오오옹.

아득한 높이의 고층 빌딩을 휘감으며 솟구치는 검붉은 어둠.

지금껏 겪어 본 적 없는 그 불길하고도 막대한 기운에 모두가 숨을 삼킨 그 순간.

콰아아아앙!

한때 아레스 길드의 파리 지부였던 마천루(摩天樓)가 터지듯 폭발했다.

건물 외관을 겹겹이 두르고 있던 방어 마법도. 미사일 포격에도 버틸 수 있게 설계된 견고한 골조(骨組)도. 그 모든 것이 산산조각이 되어 터져 나갔다.

한때 50여 층에 달하는 건물의 일부였던 크고 작은 파편들이 불길에 휩싸인 채 쏟아져 내렸다.

화륵, 후우우우웅!

“……!”

믿을 수 없는, 그러나 동시에 부정할 수 없는 현실.

하늘을 가리며 쏟아져 내리는 무수한 파편들 앞에서, 사람들은 문득 생각했다.

성경에서 말하던 종말의 날이, 바로 오늘일지도 모른다고.

뒤이어 기이하게 일그러지는 허공을 보며 그 짐작은 절망 어린 확신으로 굳어졌다.

화아아아악!

실제로 목격한 적은 단 한 번도 없었으나, 어느 때보다 찬란한 문명을 누리며 살아온 사람들은 저 현상의 명칭을 알고 있었다.

“몬스터 웨이브(Monster Wave)…….”

신음처럼 흘러나온 누군가의 목소리.

하지만 무수한 파편들이 머리 위로 쏟아지고, 일그러진 공간 너머에서 걸어 나오는 괴물들을 보면서도 그 누구도 도망치지 못했다.

자전거를 타고 등교하던 소르본 대학교의 학생들도. 유모차를 끌며 뤽상부르크 공원을 산책하던 젊은 부부도. 시민들을 진정시키기 위해 바쁘게 움직이던 경찰들도.

각자의 위치에서 바삐 움직이던 모든 이들이, 파리 6구 전체가, 뼛속까지 스며드는 공포와 한기에 잠겨 제자리에 얼어붙었다.

그리고 다음 순간.

콰콰콰쾅!

반경 백여 미터를 뒤덮은 불의 비와 함께, 지옥문의 입구가 열렸다.

쿵. 쿠웅.

마치 신전의 기둥처럼 두꺼운 팔과 다리. 한 몸뚱어리에 두 개의 머리를 지닌 거대한 괴물들이 가슴을 두드리며 포효했다.

― 그워어어어어!

차차창!

포효에 담긴 파동을 이기지 못한 유리가 사방에서 깨져 나간다.

상위 몬스터만이 발산할 수 있는 피어(Fear)가 보이지 않는 밧줄처럼 날아가 수천에 달하는 인간들을 속박했다.

― 크르르.

짙은 만족감이 어린 울음소리.

바야흐로 사냥의 시간이었다.

아니, 분명 그랬을 터였다.

쐐애애액, 퍼엉!

그 순간 번뜩이는 섬광과 함께, 선두에 있던 괴물이 비틀거렸다. 어깨 위에 있던 모든 것이 사라져 있었다.

쿠웅!

지축이 뒤흔들렸다. 어느덧 일백을 헤아리는 괴물들이 약속이라도 한 것처럼 고개를 들었다.

제자리에 못 박힌 것처럼 서 있는 수천의 인간들 속, 양 떼 사이에 숨어 있던 맹수들이 모습을 드러내고 있었다.

눈으로도 좇을 수 없는 눈부신 섬광과 함께.

쐐애애액, 뻑!

후두두둑.

살과 뼈가 짓뭉개지고, 푸른색 핏물이 사방으로 흩뿌려졌다.

두 개의 머리 중 하나를 바친 대가로 살아남은 트윈 헤드 오우거(Twin Head Ogre)가 자신도 모르게 뒷걸음질 쳤다.

그곳에 어떤 위협이 기다리는지도 모르는 채.

콰직!

거대한 주먹이 하나밖에 남지 않은 머리를 수박처럼 터트렸다.

다른 오우거와는 격이 다른 무시무시한 완력과 체구.

주먹에 붙은 부하의 뇌수를 핥아먹은 거인의 커다란 동공에, 황금빛 눈동자를 지닌 한 인간의 모습이 고스란히 비쳤다.

― 카르쉬. 마르토.

흡사 저주처럼 들리는 마계어(魔界語)였다.

그러나 황금빛 눈동자의 인간, 후긴은 아랑곳하지 않고 고개를 돌려 등 뒤의 누군가에게 정중히 고개를 숙였다.

“네임드 몬스터인 자이언트 오우거(Giant Ogre)입니다. 어찌하시겠습니까?”

담담한 목소리가 돌아왔다.

“나쁘지 않군. 보여 주기에는 이 정도가 적당해.”

“그 말씀은?”

“놈은 내가 맡지. 나머지는 치워.”

그게 전부였다.

명령이 떨어진 그 순간, 후긴과 일백의 헌터들이 한 몸이 되어 공간을 가로질렀다. 마치 그들의 갑옷에 그려진 폭풍과 번개처럼.

고대의 신이자 그들을 상징하는, 오딘(Odin)이라는 두 글자처럼.

쐐애애애액! 촤아악!

격돌. 그리고 학살.

통나무처럼 두꺼운 팔다리가 허공으로 솟구치고 눈부신 오러가 넘실거리던 마력을 갈라 낸다.

그것은 마치 신화 속 한 장면과도 같았다.

수많은 인물이 등장하는 신화에도 홀로 빛나는 주인공은 있기 마련.

― 쿠워어어어어!

퍼걱!

단 일격.

도시를 집어삼킬 것만 같던 괴성이 사라지고.

쿠우우웅!

수십 미터에 이르는 자이언트 오우거가 무릎을 꿇었다.

산과 같은 괴물의 몸뚱어리에 비하면 보잘것없이 자그마한 한 인간 앞에.

하지만 이 모든 광경을 빠짐없이 지켜본 사람들의 눈에는 절대 보잘것없어 보이지 않았다.

위험으로부터 자신들을 지켜 준 영웅. 진정한 거인(巨人)이 그곳에 있었다.

죽음의 문턱에서 살아 돌아온 사람들은 영웅의, 혹은 영웅들의 이름을 한목소리로 외쳤다.

“미카엘! 미카엘!”

“오딘 길드!”

들불처럼 번져 나가는 거대한 함성 속, 미카엘은 힘 있는 목소리로 선언했다.

“안심하십시오. 저와 오딘 길드가 여러분을 지키는 한, 그 어떤 위험도 없을 것입니다.”

그리고 콘크리트 더미에 뒤덮인 폐허를 바라보며, 아무에게도 들리지 않을 만큼 작은 목소리로 덧붙였다.

“적어도 오늘만큼은.”

희미한 미소를 지은 그는 남아 있는 몬스터 무리를 향해 걸음을 내디뎠다.

아레스(Ares).

반짝이던 윤기를 잃은 채, 무수한 파편들과 함께 건물에서 떨어져 나온 그 이름을 짓밟으며.



* * *



[오딘 길드, 아레스 지지 선언]

[오딘 길드장 미카엘 실베르트, “공공의 이익을 위한 아레스의 행보에 아낌없는 박수를 보내며, 그들과 함께 발맞춰 걸어갈 것”]

[오딘 길드, 새로운 마나 연공법 기습 공개!]

[오딘 길드 고위 관계자, “이미 수년 전부터 준비해 왔던 대형 프로젝트. 여론을 의식한 공개라고 생각한다면 유감이나 감내할 것……” 공개 전 논란 일축]



이른 아침, 스켈레톤 킹을 통해 알게 된 뉴스 속보는 분명 놀라웠다.

문제는 그 놀라움이 채 가시기도 전에 새로운 파도가 밀려들었다는 사실이었다.

그것도 훨씬 크고, 무시무시한 파도가.

징. 지이잉.

테이블 위에 올려 두었던 최 팀장의 스마트폰이 진동했다.

몇 초 뒤 홀로그램 TV에서 흘러나온 또 다른 속보는 믿기 힘든 것이었다.

― 프랑스 파리에서 몬스터 웨이브가 발생했습니다. 사건이 벌어진 장소는 파리 6구의 한 고층 빌딩이며, 아레스 길드의 파리 지부로 밝혀져 큰 충격을…….

― 현재 프랑스 정부는 국제 긴급 법령에 따라 파리 6구 봉쇄 작전을 시작했으며, 정확한 사상자와 진압 과정은 아직 알려지지 않은 상황입니다.

― 인근에 위치한 오딘 길드가 가장 먼저 사건 현장으로 향했다는 현지인들의 증언이…….

식당에 설치된 여러 개의 TV에서 흘러나오는 뉴스들.

하지만 피부색도, 사용하는 언어도 각기 다른 그들의 입술 사이로 흘러나오는 수많은 낱말 중에서도 세 개의 단어만이 귓가를 파고들었다.

몬스터 웨이브. 아레스 길드 파리 지부.

그리고…….

오딘.

띠링.



― 돌발 퀘스트, [파리에 드리운 어둠]이 생성되었습니다!

― 해당 퀘스트는 승낙 여부를 결정할 수 없습니다. 시스템의 권한으로 퀘스트가 강제 진행됩니다!

퀘스트



[파리에 드리운 어둠]



모든 선택에는 항상 결과가 뒤따르는 법.

당신의 적들은 아레스 길드 파리 지부를 무너뜨렸고, 활기가 가득하던 도시에는 몬스터의 괴성과 어둠이 내리깔렸습니다.

한시라도 빨리 그들을 구하고, 몬스터 군단을 격퇴하여 무고한 희생자를 막으십시오!



등급 : 초절정

제한 : 진태경

임무 : 파리 지부의 생존자 구출 (미완료)

 몬스터 웨이브 진압 (미완료)

보상 : 결과에 따라 정해짐

실패 : 결과에 따라 정해짐





“……!”

모든 것이 갑작스러웠다.

귓가를 울리는 시스템 알림도, 눈앞의 허공에 떠오른 홀로그램 창들도.

하지만 그 모든 것들을 보고 들은 순간, 나는 이미 본능에 따라 움직이고 있었다.

아니, 우리 모두가.

“저를 중심으로 모이십시오. 어서!”

다급한 외침을 토해 낸 최 팀장이 품에서 꺼낸 매직 스크롤(Magic Scroll)을 찢은 그 순간.

화아악!

불현듯 터져 나온 눈부신 섬광이 우리를 감싸안았다.



* * *



‘만약 내가 도우러 올 수 없을 때, 최대한 빨리 어딘가로 이동해야 한다면 꼭 이걸 사용하도록 해. 정확한 좌표를 알고 있다면 목적지까지 안전하게 도착할 수 있을 거야.’



몇 주 전 중동 소탕 작전이 마무리될 즈음, 매직 존슨이 매직 스크롤과 함께 건넸던 당부다.

그리고 그때 받았던 수십여 장의 텔레포트(Teleport) 스크롤은, 지금 이 순간 몇 초 단위로 소모되고 있었다.

찌익!

특수 처리된 질긴 양피지가 찢겨 나간다. 동시에 그 안에 잠들어 있던 마나가 깨어나고, 환하게 뿜어져 나온 섬광이 다시 한번 우리를 끌어안고 정해진 좌표를 향해 도약한다.

파아앗!

쉴 새 없이 터져 나오는 섬광.

가까이로는 수십, 멀게는 수백 킬로미터에 달하는 공간을 계속해서 뛰어넘자, 어느 순간부터 몸뚱어리가 삐걱거리고 정신이 피로를 호소하기 시작했다.

‘흡.’

연달아 발현된 공간 이동 마법이 불러온 과부하(過負荷).

하지만 그 누구도 멈추지 않았다. 심지어는 우리 중 가장 큰 부담을 얻고 있을 최 팀장조차 마찬가지였다.

으득.

이를 악문 그가 또 한 장의 스크롤을 꺼내 든다.

허가받지 않은 공간 이동에 당황하는 외국 공항 헌터들을 무시하고 한 장, 그리고 그 후유증이 채 가시기도 전에 또 다시 한 장.

끊임없이 스크롤을 찢고 또 찢었다.

섬광이 번쩍일 때마다 주위를 둘러싼 풍경이 변하고, 사람들의 피부와 언어가 바뀌었다.

그리고 도무지 몇 번째인지 모를 섬광이 사그라들었을 때.

우리는 마침내 볼 수 있었다.

한때 아레스 길드 파리 지부라 불리었던 폐허를.

곳곳에 널브러진 거대한 괴물들의 사체와 단 한 줌의 생명조차 느껴지지 않는 콘크리트와 철근의 무덤을.

그와 동시에, 오직 나만이 들을 수 있는 소리가 귓가를 파고들었다.

삐빅.



― 당신은 어떤 임무도 달성하지 못했습니다.

― 돌발 퀘스트, [파리에 드리운 어둠]이 실패로 돌아갑니다.

― 모든 일에는 항상 보상과 대가가 따르는 법. 퀘스트 실패로 인한 패널티가 주어집니다.

― 경험치가 대폭 하락합니다.

― 명성치가 대폭 하락합니다.

― 특수 칭호, [수수방관(袖手傍觀)]이 향후 30일간 적용됩니다.

― 특수 칭호, [수수방관]의 패널티 효과로 인해 모든 능력치가 10% 하락합니다.



“……아.”

나는 짤막한 신음을 흘렸다.

퀘스트 실패?

막대한 패널티?

그런 것 따위는 아무것도 아니었다.

뒤늦게 우리의 모습을 발견하고 웅성거리기 시작한 주위의 분위기도. 폐허를 가로지르는 일단의 무리도 마찬가지다.

내 오감(五感)이 향하고 있는 것은 허공에 떠 있는 여러 개의 홀로그램 창 중에서도 오직 하나.



― 당신은 어떤 임무도 달성하지 못했습니다.



그뿐이었다.

저 냉정하고 딱딱한 한 줄의 문장은 눈과 머릿속을 관통하며 헤집었고, 나는 그것이 의미하는 바를 이미 알고 있었다.

‘죽었다. 전부.’

그것이 현실이었다.

아레스 길드의 파리 지부는 더 이상 존재하지 않는다.

인근에서 평화롭게 하루를 시작하던 사람들도 마찬가지다.

한때 구름과 닿아 있던 마천루(摩天樓)는 죽음만이 내리깔린 폐허가 되었고, 불과 수십 분 전만 하더라도 이곳에서 웃고 떠들던 사람들은 두 번 다시 돌아올 수 없는 강을 건넜다.

지금 내가 바라보고 있는, 건물의 잔해 속에 파묻힌 이름 모를 누군가의 시신처럼.

무슨 생각이었을까.

멍하니 이름 모를 시신을 내려다보던 나는 불현듯 손을 뻗어 그의 팔을 붙잡았고, 잡아당긴 후에야 또 다른 시신의 팔이라는 것을 깨달았다.

그것이 끝이 아니다.

하나의 시신을 끌어 올리면 세 구의 시신이 보였고, 그들마저 끌어올리면 몸에서 떨어져 나간 사지(四肢)들이 모습을 드러냈다.

“어, 어떻게.”

“간악한 인간이여. 이건, 이건 정말…….”

멀게만 느껴지는 최 팀장과 스켈레톤 킹의 목소리를 들으며, 나는 말 없이 주위를 둘러보았다.

파리 지부가 있던 장소를 중심으로 초토화된 거리. 살 타는 냄새가 섞인 연기가 매캐하게 피어오르고, 아직 수습하지 못한 사람들의 시신이 곳곳에 널브러져 있었다.

그렇다면 내가 딛고 선 이 폐허 밑에는, 얼마나 많은 이들이 잠들어 있을까.

그리고 그들은 왜.

‘왜 죽어야 했나.’

불덩이를 삼킨 것처럼 뱃속이 뜨겁다.

나는 부서질 듯이 이를 악물었다. 찢어진 입술에서 흐른 피를 삼키며 단전에서 몸부림치는 삼 갑자의 열양지기를 애써 가라앉혔다.

이 이상으로 흥분해서는 안 된다. 조금이라도 더 침착하고 냉정해야 한다.

그렇지 못한다면, 지금 내 등 뒤로 다가오는 저 거대한 기운의 주인을 제정신으로 마주할 수 없을 테니까.

‘미카엘 실베르트.’

한 사람의 이름을 떠올리며, 나는 천천히 돌아섰다.
```

## Final English reading copy

```markdown
# Chapter 736

It had certainly started out insignificant. Just a slight tremor. Nothing more, nothing less.

But that had only been a small omen.

*Rumble…*

The ground shook.

The visitors standing in line outside the Louvre instinctively ducked, while the lower-class residents of Paris’s 10th arrondissement, who had been fighting as they clutched one another by the collars, scattered in all directions with curses.

And the citizens of the 6th arrondissement…

“Ah…”

They forgot even to scream. With vacant eyes, they stared at the scene unfolding before them.

*Gooooom.*

A crimson-black darkness coiled around a skyscraper that soared to dizzying heights before surging upward.

At the moment everyone held their breath before that ominous, overwhelming energy unlike anything they had ever experienced—

*BOOOOOM!*

The skyscraper that had once housed Ares Guild’s Paris branch exploded as though it were bursting apart.

The defensive Magic layered over the building’s exterior. The sturdy frame designed to withstand missile bombardments. Every last bit of it shattered and blew outward.

Large and small fragments that had once been part of a building roughly fifty stories tall came pouring down, engulfed in flames.

*Fwoosh. Whoooooosh!*

“……!”

It was an unbelievable reality, yet one that could not be denied.

As countless fragments rained down and blocked out the sky, people suddenly thought:

*Maybe today really is the day of the apocalypse described in the Bible.*

Then they saw the air twisting strangely, and that suspicion hardened into despairing certainty.

*Fwoooooosh!*

They had never witnessed it with their own eyes, but people who had lived through the brightest civilization in history knew the name of the phenomenon.

“Monster Wave…”

Someone’s voice slipped out like a groan.

Yet even as countless fragments fell over their heads and monsters stepped out from beyond the warped space, no one could run.

The Sorbonne University students riding their bicycles to class. The young couple strolling through the Luxembourg Gardens with a stroller. The police rushing around to calm the citizens.

Everyone who had been moving busily in their respective places—and the entire 6th arrondissement with them—froze where they stood, submerged in a fear and chill that seeped into their bones.

And then.

*BOOM! BOOM! BOOM!*

Amid a rain of fire covering a radius of more than a hundred meters, the doorway to hell opened.

*Thud. Thud.*

Monsters with arms and legs as thick as the pillars of a temple, each bearing two heads on a single massive body, pounded their chests and roared.

—Gwooooooar!

*Crash!*

Glass shattered in every direction, unable to withstand the waves contained in their roar.

Fear, something only High-Rank monsters could release, flew out like invisible ropes and bound thousands of humans.

—Grrrr.

A cry filled with deep satisfaction.

It was time to hunt.

No—it should have been.

*Whoooooosh! Boom!*

At that moment, accompanied by a flash of light, the monster at the front staggered. Everything that had been atop its shoulders had vanished.

*Thud!*

The ground shook. By then, the hundred or so monsters had raised their heads as though they had made a silent pact.

Among the thousands of humans standing frozen in place, predators hiding among the flock were revealing themselves.

Alongside dazzling flashes too fast for the eye to follow.

*Whoooooosh! Crack!*

*Rattle, rattle.*

Flesh and bone were crushed, and blue blood sprayed in every direction.

The Twin Head Ogre that had survived by sacrificing one of its two heads unknowingly took a step backward.

It did not know what threat awaited it there.

*Crunch!*

A gigantic fist burst the only head it had left like a watermelon.

A giant whose terrifying strength and physique were on an entirely different level from the other ogres.

The giant licked the brain matter of its subordinate from its fist. Reflected in its enormous pupils was the figure of a human with golden eyes.

—Karsh. Marto.

It was Demon Realm language, and it sounded almost like a curse.

But Huginn, the golden-eyed human, paid it no attention. He turned around and bowed politely to someone behind him.

“It is a Named Monster—a Giant Ogre. What shall we do?”

A calm voice answered:

“Not bad. This is about right for putting on a show.”

“What do you mean?”

“I’ll take that one. Clear out the rest.”

That was all.

The moment the order was given, Huginn and a hundred Hunters crossed the space as one body, like the storm and lightning painted across their armor.

Just like Odin, the name of the ancient god who symbolized them.

*Whooooooosh! Slash!*

Clash.

Then slaughter.

Limbs as thick as logs flew into the air, while dazzling aura cut through the magical energy surging around them.

It was like a scene from a myth.

Even myths filled with countless figures had a protagonist who shone alone.

—Gwooooooar!

*Crack!*

One Strike.

The roar that had seemed capable of swallowing the entire city vanished.

*Ruuuuumble!*

The Giant Ogre, dozens of meters tall, dropped to its knees.

Before a single human who looked insignificant compared to the monster’s mountain-sized body.

But to the people who had watched the entire scene without missing a moment, that human did not look insignificant at all.

A hero who had protected them from danger.

A true giant stood there.

The people who had returned alive from the brink of death shouted the hero’s—or heroes’—name with one voice.

“Michael! Michael!”

“Odin Guild!”

Amid the enormous roar spreading like wildfire, Michael declared in a powerful voice:

“Please rest assured. As long as Odin Guild and I are here to protect you, no danger will befall you.”

Then, as he looked toward the ruins buried beneath heaps of concrete, he added in a voice too quiet for anyone to hear:

“At least today.”

With a faint smile, he stepped toward the remaining group of monsters.

Toward the name Ares, which had fallen from the building alongside countless fragments, stripped of its former shine.

And he trampled it beneath his feet.

* * *

**Odin Guild Declares Support for Ares**

**Odin Guild Master Michael Silbert: “We Offer Our Heartfelt Applause for Ares Guild’s Actions in the Public Interest and Will Walk Forward Alongside Them”**

**Odin Guild Makes a Surprise Release of a New Mana Cultivation Method!**

**Senior Odin Guild Official: “A Large-Scale Project We Have Been Preparing for Years. If You Think We Released It with Public Opinion in Mind, That Is Regrettable, but We Will Endure It…”—Dismisses Controversy Before Release**

The breaking news I learned from the Skeleton King early that morning was certainly astonishing.

The problem was that before the shock had even faded, another wave came crashing in.

A much larger and more terrifying wave.

*Bzzzt. Bzzzt.*

Team Leader Choi’s smartphone, which had been lying on the table, began to vibrate.

A few seconds later, another breaking-news report flowed from the holographic television. It was almost impossible to believe.

—A Monster Wave has occurred in Paris, France. The incident took place at a skyscraper in the 6th arrondissement of Paris, which has been identified as the Paris branch of Ares Guild, causing tremendous shock…

—The French government has begun an operation to seal off the 6th arrondissement under international emergency law. The exact number of casualties and the details of the suppression operation remain unknown…

—Local residents have testified that Odin Guild, which was located nearby, was the first to head toward the scene…

News reports flowed from the several televisions installed throughout the restaurant.

But among the countless words spilling from the lips of people with different skin colors and speaking different languages, only three terms pierced my ears.

Monster Wave.

Ares Guild’s Paris branch.

And…

Odin.

*Ding.*

> **System**
>
> A sudden Quest, **The Darkness Over Paris**, has been generated!
>
> You cannot choose whether to accept this Quest. By the authority of the System, the Quest will proceed by force!
>
> **Quest**
>
> **The Darkness Over Paris**
>
> Every choice is always followed by consequences.
>
> Your enemies have brought down Ares Guild’s Paris branch, and the city that once overflowed with life is now shrouded in the roars of monsters and darkness.
>
> Rescue them as quickly as possible and repel the monster army to prevent innocent casualties!
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:**
>
> Rescue the survivors of the Paris branch (Incomplete)
>
> Suppress the Monster Wave (Incomplete)
>
> **Reward:** Determined by the outcome
>
> **Failure:** Determined by the outcome

“……!”

Everything happened so suddenly.

The System notification ringing in my ears. The holographic windows floating in the air before me.

But the instant I saw and heard all of it, I was already moving on instinct.

No—all of us were.

“Gather around me. Quickly!”

The moment Team Leader Choi shouted urgently and tore a Magic Scroll from inside his coat—

*Fwoosh!*

A blinding flash suddenly burst forth and wrapped around us.

* * *

*If I can’t come to help and you need to move somewhere as quickly as possible, make sure you use this. If you know the exact coordinates, you’ll be able to reach your destination safely.*

That was what Magic Johnson had told me several weeks earlier, around the time the Middle East cleanup operation was coming to an end, when he handed me the Magic Scrolls.

And the several dozen Teleport scrolls I had received back then were now being consumed at intervals of only a few seconds.

*Rip!*

The specially treated, durable parchment tore apart. At the same time, the mana sleeping inside it awakened, and the brilliant flash that poured out once again embraced us before leaping toward the predetermined coordinates.

*Flash!*

Flashes erupted without pause.

As we continued leaping through space—sometimes tens of kilometers away, sometimes hundreds—the body began to creak, and my mind started to cry out from exhaustion.

*Hup.*

The spatial-transit Magic cast in rapid succession had brought on an overload.

But no one stopped. Not even Team Leader Choi, who was probably bearing the greatest burden among us.

*Grind.*

Clenching his teeth, he pulled out another scroll.

Ignoring the foreign airport Hunters thrown into confusion by our unauthorized spatial movement, he tore one scroll, then another before the aftereffects of the first had even faded.

He continued tearing scroll after scroll without pause.

Every time the light flashed, the scenery around us changed, along with the skin and languages of the people nearby.

And when a flash whose number I had long since lost count of finally faded—

we could see it at last.

The ruins that had once been called Ares Guild’s Paris branch.

The enormous corpses of monsters scattered everywhere. The graveyard of concrete and rebar, from which not even a handful of life could be felt.

At the same time, a sound only I could hear pierced my ears.

*Beep.*

> **System**
>
> You have not completed a single mission.
>
> The sudden Quest, **The Darkness Over Paris**, has failed.
>
> Every event is always accompanied by a reward and a price. You will receive penalties for failing the Quest.
>
> EXP decreases drastically.
>
> Fame decreases drastically.
>
> The special Title **Idle Bystander** will apply for the next 30 days.
>
> Due to the penalty effect of the special Title **Idle Bystander**, all stats decrease by 10%.

“……Ah.”

I let out a short groan.

Quest failure?

A massive penalty?

None of that mattered.

The atmosphere around us, which had begun to murmur after belatedly noticing our arrival, did not matter either. Neither did the group making its way across the ruins.

Of the several holographic windows floating in the air, all five of my senses were drawn toward only one.

> **System**
>
> You have not completed a single mission.

That was all.

That cold, rigid sentence pierced through my eyes and tore through my mind. I already knew what it meant.

*They’re dead. All of them.*

That was reality.

Ares Guild’s Paris branch no longer existed.

Neither did the people who had been peacefully beginning their day nearby.

The skyscraper that had once reached the clouds had become a ruin blanketed in death, and the people who had been laughing and talking here only a few dozen minutes ago had crossed a river from which they could never return.

Just like the unidentified corpse buried beneath the wreckage of the building before me.

*What was I thinking?*

As I stared blankly down at the unidentified corpse, I suddenly reached out and grabbed his arm. Only after pulling on it did I realize that it was the arm of another corpse.

And that was not the end.

When I dragged one corpse out, three more appeared. When I pulled those away, severed limbs emerged from beneath them.

“H-how…”

“Wicked human. This… this is truly…”

Hearing Team Leader Choi and the Skeleton King’s voices, which felt impossibly distant, I silently looked around.

The streets around the former branch had been reduced to a wasteland. Smoke laced with the smell of burning flesh rose acridly into the air, and the bodies of people who had not yet been recovered lay scattered everywhere.

Then how many people were sleeping beneath the ruins where I stood?

And why had they—

*Why did they have to die?*

My stomach burned as if I had swallowed a ball of fire.

I clenched my teeth so hard they felt ready to break. Swallowing the blood flowing from my split lips, I forced down the three jiazi of Scorching Yang Qi struggling in my dantian.

I could not get any more agitated. I had to remain calm and composed—more than ever.

Because if I failed to do so, I would not be able to face the master of that enormous energy approaching from behind me with a clear mind.

*Michael Silbert.*

As I recalled one man’s name, I slowly turned around.
```
