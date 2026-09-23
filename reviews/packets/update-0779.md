<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0779.txt",
      "sha256": "2ead222165a28bfb2707bac8643fff7907041019c7ec7fe1143d0e3eecb4fd04",
      "bytes": 19272
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4bc0d84757f14c76ea6d6dc0366ba532d3173a8817c85cfaf914709b285925ab",
      "bytes": 1107
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "45e50ae77be3c073d1488a74f8e2d08bfe6cbdb99494ab42a6437874780008c2",
      "bytes": 223212
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "4dbe46bc4bff6d1883ba20b7150625660e5b57b45fa11ec4e539fd3221f7fe5f",
      "bytes": 752
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "c0adceb0b7a813f97a7722bc7cec05d7660ab46a6fe5a1cf0f414ae04e6f660f",
      "bytes": 553
    },
    {
      "path": "characters/Felix.md",
      "sha256": "86eb45a37c572efbc5ce213d1878d9f7398dff1cd9adfb6a3c5432dfa5930e27",
      "bytes": 464
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "8376e74d91acd78150f6a6156486b73f3fbc22c6196693209b517075b953cf51",
      "bytes": 2096
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "135d8edd30ededae76e54a67b533bbfe2d6fcc292e0f744db1ec4482f683de4a",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "057fa82d0f93a9fa564fa2d08fd97f69a904c0f0c9d6410cb9f3eaecf48caae0",
      "bytes": 859
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "38eec7756883acc92d17c228ca7c4dbc05df156858ce2f76f338022e8142d08f",
      "bytes": 645
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ca25852247b0967292f3efc8a331825e0f45c463483805d28390e1f779daeb8b",
      "bytes": 242444
    }
  ],
  "estimated_tokens": 13102
}
-->

# Durable State Update — Chapter 779

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 779. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 779. Profile updates may replace only one
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
  "chapter": 779,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 779,
    "continuity_sources": [779],
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
    "Cheon Taemin is in a coma and too ill to join the coming war; Team Leader Choi publicly revealed this at the Federation’s inaugural ceremony, and Magic Johnson confirmed it.",
    "Michael Silbert is positioning himself to lead the World Hunter Federation and intends to eliminate Jin Taekyung as soon as possible.",
    "The World Hunter Federation leadership gathering is disrupted after Jin destroys the central seat and declares that the Stone King is a monster; who will lead the Federation remains unresolved.",
    "The Skeleton King says Jin was the first friend he made after coming into this world; he once sacrificed himself to save Jin from the Arch Lich."
  ],
  "continuity_sources": [
    778,
    777
  ],
  "open_questions": [
    "Who will be elected to lead the World Hunter Federation?",
    "Will Michael act on his intention to eliminate Jin?",
    "Can Cheon Taemin recover from his coma?",
    "What consequences will follow Jin’s public declaration about the Stone King?"
  ],
  "safe_through": 778,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 천태민    | **Cheon Taemin**  |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 사숙     | **Martial Uncle**                            |
| 선배     | **Senior**                                   |
| 명성               | **Fame**                       |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 필릭스 | **Felix** | British prince and S-rank Hunter. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 위압 | **Intimidation** | System attribute strengthened by the achievement reward. |
| 도산검림 | **a mountain of sabers and a forest of swords** | Idiom describing the lethal life of martial artists. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 인시 | **Insi** | The traditional time period from three to five in the morning. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 필릭스 | Korean S-rank Hunter addressing a British prince | His Highness | mock-formal and sarcastic | Felix demands formal address, and Jin complies by calling him His Highness while continuing to mock him. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 필릭스 | 진태경 | British prince and S-rank Hunter to allied Korean S-rank Hunter | Jin | lofty and aristocratic | Felix addresses Jin while discussing royal duty and their teleport. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |
| 필릭스 | 존슨 | prince_to_allied_grand_mage | Mr. Johnson | formal-polite | Felix uses a respectful address while speaking with Magic Johnson. |
| 최민우 | 필릭스 | allied_operations_lead_to_prince | Your Highness | polite-formal | Choi greets Felix during the secret meeting. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 777
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he remains unconscious after more than twenty years in a wired mechanical capsule at his former mansion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 776
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Felix.md

# Felix (필릭스)

- **Safe through:** Chapter 778
- **Aliases:** Prince Felix
- **Role:** British prince and S-rank Hunter who joins the reinforcement force against the Arch Lich.
- **Personality:** Haughty, self-important, and conscious of royal duty.
- **Voice:** Formal, lofty, and aristocratic.
- **Relationships:** Travels with Faye Chen and Magic Johnson and is allied with Jin Taekyung.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 778
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license, as well as a traveler between Murim and another world resembling the realm of immortals and the principal Hunter opposing Michael Silbert's terrorist campaign.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 778
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 778
- **Aliases:** None
- **Role:** Michael Silbert is Odin Guild Master and a public hero positioning himself to lead the World Hunter Federation; he intends to eliminate Jin Taekyung as soon as possible.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 777
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Jin Taekyung's meticulous intelligence and operations lead, a trusted ally and natural leader capable of guiding the reestablished World Hunter Federation.
- **Personality:** Calm, pragmatic, meticulous, and emotionally steady under pressure.
- **Voice:** Measured, professional, and reassuring without minimizing responsibility.
- **Relationships:** A trusted ally and operational adviser to Jin Taekyung, and the maternal grandson of Cheon Taemin.

## Korean source

```text
＃779화



순간, 세상이 멈춘 듯했다.

만약 주기적으로 깜빡이는 카메라의 불빛과 시계 초침이 아니었다면, 사람들은 정말 시간이 정지되었다고 생각했을 것이다.

하지만 그 침묵은 그리 오래가지 않았다.

“미쳤군.”

불쑥 튀어나온 누군가의 목소리.

헛웃음을 띤 얼굴로 진태경과 스톤 킹을 번갈아 바라보는 이들 역시 부지기수였다.

그럴 수밖에 없었다. 스톤 킹이 누구인지는 이 자리의 모두가 알고 있었으니까.

아니, 길거리의 아무에게나 물어도 마찬가지일 것이다.

어느 날을 기점으로 혜성처럼 등장한 미국 국적의 S급 헌터.

외모만큼이나 뛰어난 실력을 지닌 그는 항상 진태경의 곁에 있었고, 그로 인해 처음부터 적지 않은 관심을 받으며 여러 가지 굵직한 사건에서 두각을 드러냈다.

이른바 ‘자경단 사건’이라 불리는 테러리스트 소탕 작전에 참여함으로써 진태경과 함께 비난의 대상이 된 적도 있었으나, 자세한 공과(功過)를 따져 보자면 전공이 월등히 앞선다는 것이 중론이었다.

그런데 그런 스톤 킹이, 어느덧 신세대를 대표하는 젊은 영웅 중 한 사람으로 인정받아 원탁에 앉을 자격까지 부여받은 그가 몬스터라니.

사람들 사이로 혼란 대신 실소가 번졌다.

“헛소리도 정도껏 해야지.”

한 번이 어렵지, 두 번부터는 쉽다.

진태경의 엄청난 실력과 입지를 생각하여 말을 아끼던 이들이 점차 목소리를 높이기 시작했다.

“보자 보자 하니 젊은 친구가 너무 막 나가는 것 아닌가?”

“이보게, 진. 나 역시 한 사람의 헌터로서 자네를 존중하지만…… 오늘 이 자리에서 보인 여러 행동에 대해서는 합당한 해명이 필요할 걸세.”

“외상 후 스트레스 장애에 시달린다더니, 그게 사실이었던 모양입니다.”

도화선의 심지가 빠르게 타들어 간다.

처음부터 진태경에게 우호적인 눈빛을 보냈던 원로들조차 침음성을 흘렸고, 이미 그 반대편에 서 있던 이들은 이때다 싶었는지 노골적인 비난도 서슴지 않았다.

“여러분, 그가 무슨 짓을 했는지 보십시오. 인류를 구원할 연맹의 대표를 선출하는 중요한 시간에 난동을 일으키고, 원탁을 훼손하기까지 했습니다.”

“거기에 헛소리마저 지껄이고 있군.”

“도대체 이게 무슨 무례인가?”

사방에서 쏟아지는 비난들.

하지만 이 모든 것의 중심에 있는 한 사람, 진태경은 아무것도 듣지 못한 것처럼 좌중을 향해 입을 열었다.

다시 한번.

앞서 했던 말에서 토씨 하나 틀리지 않고.

“스톤 킹은, 몬스터다.”

“고작 한다는 말이, 또 그 헛소린가?”

“미쳤군. 단단히 미쳤어.”

진태경은 천천히 주위를 둘러보았다.

헛웃음을 흘리는 이들, 눈살을 찌푸린 이들, 깊게 가라앉은 눈빛으로 사태를 주시하는 이들까지.

그 반응은 각양각색이었지만, 다음 순간 또다시 진태경의 입술 사이로 흘러나온 말의 내용은 변함없었다.

“스톤 킹은, 몬스터다.”

“이 무슨!”

“당장 저자의 자격을 박탈하시오!”

비난하던 목소리들은 이제 외침이 되었다. 그러나 진태경은 아랑곳하지 않고 재차 입을 열었다.

“스톤 킹은…….”

마치 그 한 마디밖에 모르는 사람처럼. 오직 그것 하나만을 사람들의 머릿속에 각인시키는 것이 삶의 유일한 목표인 사람처럼.

쉼 없이. 자신을 향해 쏟아지는 모든 시선과 비난들을 무시한 채.

자신의 가장 큰 약점이 될지도 모르는 그 사실을, 진태경은 또다시 담담하게 읊조렸다.

거대한 원탁 전체를 집어삼킨 이 소란 속에서도 침묵을 지키는 한 사람. 미카엘 실베르트를 바라보며.

“몬스터다.”

벌써 세 번째.

기계처럼 같은 말만을 반복하는 그의 모습에 사람들의 입가에 맺혀 있던 비웃음이 희미해졌다.

시끄럽게 울려 퍼지던 고함도, 삿대질도 멎었다. 이제는 그 누구도 움직이거나 입을 열지 않았다.

어느샌가 찾아온 적막.

그리고 침 삼키는 소리 하나 들려오지 않는 그 완전한 침묵 속에서, 사람들은 불현듯 한 가지 사실을 깨달았다.

지금 진태경은 진실을 말하고 있다는 것을.

그의 표정, 목소리. 눈빛. 모든 것 하나하나가 거짓과는 한참이나 동떨어져 있다는 것을.

더불어 그것이 의미하는 바가 무엇인지도.

‘……설마.’

모두의 뇌리를 스친, 믿을 수 없는 의문.

동시에 수백 쌍의 눈동자가 한 사람을 향해 움직였다.

아니, 어쩌면 사람이 아닌 다른 무언가일지도 모르는 존재를 향해.

스톤 킹.

수려한 외모를 지닌 미국인은 변함없이 처음 그 자리에 앉아 있었지만, 사람들은 볼 수 있었다. 느낄 수 있었다.

잘게 흔들리는 그의 눈동자와 그 안에 스며 있는 미약한 두려움을. 자신들이 품었던 이 의문에 대한 확신을.

그리고 마침내 받아들인 진실과 함께 찾아온, 보이지 않는 거대한 충격이 파도처럼 좌중을 휩쓸었다.

아니, 망치가 되어 후려쳤다.

“……!”

“……!”

이 믿을 수 없는 진실 앞에 모두가 멍하니 입을 벌렸다.

이제 부릅뜬 삼백여 쌍의 눈동자에 비친 것은 수려한 외모의 젊은이도, 뛰어난 실력과 명성을 지닌 S급 헌터도 아니었다.

결코 양립할 수 없는, 한때 인류를 재앙의 구렁텅이로 몰아넣었던 저주받은 존재가 그곳에 있었다.

“……몬스터.”

그리고 신음과도 같은 누군가의 뇌까림이 침묵을 깨트린 그 순간.

차차차차창!

드넓은 공간을 밝히고 있던 조명 아래, 수백에 달하는 병장기가 빛을 받아 번쩍였다.

인류가 신으로부터 선물 받은 힘. 오라(Aura)의 광휘가 온 사방을 물들였고, 이내 한 존재를 향해 겨누어졌다.

손으로 만질 수 있을 것처럼 선명한 살기(殺氣)와 함께.

스아아아.

어디선가 바람이 휘몰아쳤다. 차갑게 얼어붙은 공기 속에서, 송곳과도 같은 무수한 시선이 스톤 킹을 꿰뚫었다.

이 자리의 모두는 오직 몬스터와 대적하기 위해 신에게 선택받고, 인류로부터 사냥꾼(Hunter)이라는 이름을 부여받은 이들.

처음부터 그들에게 주어진 의무는 하나뿐이었다.

‘몬스터를, 죽인다.’

후우우웅.

그리고 하나로 합쳐진 수백의 기운과 살기가 공간을 짓누르며 쏘아지던 그 순간.

“그만-!”

파앙!

마치 맹수의 포효와도 같은 외침이, 그 안에 실린 깊은 울림이 찰나의 틈을 파고들어 모든 것을 안개처럼 흩어지게 했다.

그와 동시에 당장이라도 병장기를 휘두를 것 같던 사람들의 얼굴이 딱딱하게 굳었다.

‘이게 도대체.’

막대한 살기와 마나가 휘몰아치는 공간은 그 자체로 사지(死地)나 다름없다.

그러나 목소리의 주인은 그 흐름을 깨트렸다. 공격을 펼치려던 그 마지막 순간에서 보이지 않는 틈새를 파고들며.

그것도 손쉬울 만큼 간단하게.

저벅. 저벅.

나직하게 울려 퍼지는 발소리가 숨 막히는 침묵을 깨트렸다.

무수한 병장기로 가득한 도산검림(刀山劍林)을 헤집듯 가로지르며 모두의 앞을 막아선 한 청년의 모습에, 백발이 성성한 원로 헌터가 무거운 얼굴로 입을 열었다.

“이게 무슨 짓인가.”

상대를 알아본 진태경이 예의를 갖추어 대답했다.

“제가 해야 할 일을 하고 있습니다, 선배님.”

“그 해야 할 일이라는 것이, 설마 저 몬스터를 지키는 것은 아니겠지?”

“맞습니다.”

한 치의 망설임도 없는 대답에, 원로 헌터가 이해할 수 없다는 표정으로 물었다.

“어째서?”

“제 친구니까요.”

“……친구?”

“동시에 목숨을 빚진 전우(戰友)이기도 합니다. 그러니 제가 지켜야죠. 저 녀석이 그랬던 것처럼.”

친구? 전우?

몬스터를 칭하는 수식어로는 상상치도 못했던 단어에 모두가 할 말을 잃어버린 그때, 어느덧 자연스럽게 갖춰진 포위망 속에서 한 사람이 불쑥 입을 열었다.

“그렇게까지 말하니, 더 들을 필요도 없겠군.”

번쩍이는 전신 갑주와 손에 들린 거대한 워 해머(War Hammer).

묵직한 기세와 위압감을 흩뿌리며 앞으로 나선 중년인의 시선은 진태경을 응시하고 있었지만, 그의 목소리는 모두를 향하고 있었다.

“이건 우리 인류에 대한 반역이자, 용서할 수 없는 배반 행위다. 네놈도 그에 대한 처벌은 알고 있겠지?”

진태경이 고개를 끄덕였다.

“당연히.”

“이미 알고 있다니 됐군. 지금 이 시간부로 네게 주어진 헌터 자격을 박탈하고, 배신자를 즉결 처분한다.”

우우웅.

짙은 빛무리가 워 해머를 겹겹이 뒤덮었다.

대격변 시기부터 활약해 온 S급 헌터이자, 크로노스(Kronos)라는 이름을 세계 10대 길드 중 하나로 각인시킨 거물다운 위용.

그러나 다음 순간 진태경이 보인 반응은, 이 상황을 지켜보던 모두의 예상을 훌쩍 뛰어넘는 것이었다.

“거 시발, 지랄도 정도껏 해야지.”

“뭐?”

“개소리가 하도 구구절절해서 일일이 넘겨짚기도 힘드네. 하지만 그전에 한 가지만 물어보자.”

진태경이 착 가라앉은 시선으로 크로노스 길드장을 응시했다.

“이렇게 발작 버튼 눌려서 지랄 염병을 떨어 댈 거였으면, 방금 전에는 왜 그렇게 날 미친놈 취급한 건데?”

“그건…….”

“그건, 뭐?”

크로노스 길드장은 문득 말문이 막혔다.

비단 그뿐만 아니라, 그 말을 들은 모두가 마찬가지였다.

예상치도 못하게 정곡을 찌르는 한 마디.

맞다. 그들은 처음부터 진태경의 말을 헛소리 취급했고, 그는 사람들의 비난 속에서도 묵묵히 세 번이나 되새기듯 알려 주었다.

그들의 입가에 맺힌 비웃음이 사라질 때까지. 이 모든 것이 진실이라는 것을 깨달을 때까지.

하지만 그토록 진심을 다해 말했음에도, 어째서 자신들은 저 젊은이를 믿지 않았을까.

의문에 대한 답은 간단했다.

아니, 그것은 어쩌면 이미 알면서도 모른 척할 수밖에 없는 진실이었다.

“딱 까놓고 말합시다. 막상 진실을 알고 나니까 인정하기 싫었던 거잖아. 저기 앉아 있는 저 녀석이, 감히 몬스터 따위가 별다른 자격도 없이 여기 끼어 있는 몇몇 병신들보다도 더 인간을 위해 싸웠다는 사실을.”

“……!”

“하긴. 한편으로는 충분히 이해가 돼. 어느 누가 스톤 킹이 몬스터라는 말을 넙죽 믿겠어. 안 그래요?”

어디에서도 돌아오지 않는 대답에, 진태경은 웃었다.

“아주 블랙 코미디가 따로 없어. 막상 인간 같지도 않은 새끼들은 세상에 널리고 널렸는데, 한 사람이라도 더 구하겠답시고 뭐 빠지게 싸운 어디의 누구는 정체가 밝혀지자마자 바로 저승 문턱이잖아.”

한껏 솟구친 입꼬리 위로 드러난 청년의 눈동자에 차가운 불꽃이 일렁였다.

사방을 에워싼 무수한 병장기들. 당장이라도 날아들 것 같은 그 도검의 숲을 보며 피어오른 감정의 이름은, 바로 분노와 씁쓸함이었다.

“이런 상황을 바란 게 아니었는데, 그렇게 많은 걸 원한 것도 아니었는데. 단지…… 충분히 해명할 시간 정도는 줄 거라고 믿었던 것뿐인데.”

진태경은 공허하게 중얼거렸다.

물론 이해한다. 분명 이들 중 상당수는 몬스터에 의해 가까운 사람을 잃었을 테니까.

당장 그가 그러했듯이.

하지만…… 그럼에도 마음 한구석이 울렁거렸다.

인간들을 위해 자신을 희생하며 싸워 온 스켈레톤 킹에게 미안했고, 한 치의 망설임도 없이 죽이려 드는 저들의 모습에 씁쓸했으며, 이런 상황에서조차 명백한 적의(敵意)를 드러내는 이들의 숫자가 적지 않음을 깨닫고 분노가 솟구쳤다.

그들의 적의가, 단지 자신이 몬스터인 스켈레톤 킹을 친구이자 전우로 생각해서가 아니라는 것을 알기 때문에.

그리고 이 적의가 향하는 방향과 목적이, 꼭두각시나 다름없는 그들의 뒤에 누가 있는지 알기 때문에 더더욱 그러했다.

저벅.

진태경은 불현듯 걸음을 뗐다.

이 갑작스러운 움직임의 의미를 가장 먼저 깨달은 크로노스 길드장이 벼락처럼 워 해머를 휘둘렀다.

아니, 휘두르려 했다.

불쑥 귓가를 파고든 누군가의 목소리가 아니었다면.

“그쯤에서 멈추는 게 좋을 거야, 파비안.”

우우웅.

파르르 떨리는 공기.

어느새 자리에서 일어난 거구의 흑인을 바라본 크로노스 길드장이 얼굴을 굳혔다.

“존슨.”

“오랜만이네. 나이가 드니까 더 매력적인데.”

익살맞게 눈을 찡긋한 매직 존슨이 오러로 넘실거리는 워 해머를 향해 스태프를 까딱였다.

“워. 섣부르게 움직이지 마. 이건 함께 목숨 걸고 싸웠던 전우로서 건네는 충고야.”

“자네, 지금 이 행동이 어떤 의미인지 알고 있나?”

“물론. 그러니까 굳이 알려 줄 필요는 없어. 우리는 앞으로 가야 할 길을 확실히 알고 있거든.”

“……우리?”

반사적으로 되물은 그 순간. 그는 그 의문에 대한 답을 두 눈으로 똑똑히 확인할 수 있었다.

스륵. 쿵.

조용히. 시끄럽게. 혹은 기품 있게 각자의 자리에서 일어나는 이들.

그 낯익으면서도 화려한 얼굴들을 마주한 크로노스 길드장의 눈빛이 깊게 가라앉았다.

매직 존슨을 시작으로 척 헤이글. 파이 첸. 필릭스 왕자.

거기에 더하여 천태민의 유일한 혈육이라는 상징성을 지닌 최민우와, 마지막으로 굳은 얼굴로 자신을 향해 겨누어진 병장기들을 바라보던 스톤 킹까지.

‘상황이 좋지 않다. 미카엘에게 들었던 예상 범위를 이미 벗어났어.’

그러나 그의 예상을 가장 크게 벗어난 것은, 어느덧 코앞에까지 다가온 한 청년이었다.

“비켜.”

“그럴 수는 없…….”

“비키라고 했다.”

“……!”

그 순간.

크로노스 길드장은 실로 오랜만에 뼛속 깊이 파고드는 한기(寒氣)을 느꼈다.

자신의 인생의 반도 살아오지 않은, 젊은이로부터 흘러나오는 그 기세를.

동시에 앞서 매직 존슨에게서 들었던 충고가 뇌리를 스쳤다.

그쯤에서 멈추는 게 좋을 거라는, 섣부르게 움직이지 말라는 그 말이 누구를 위해서였는지도.

저벅.

정신을 차렸을 때는 이미 늦은 후였다. 크로노스 길드장은 본능적으로 옆으로 몸을 틀었고, 진태경은 당연하다는 듯 나아갔다.

사방을 빽빽하게 에워싼 삼백여 명 중 절반은 그런 그를 막으려 했으나 이내 자신도 모르게 길을 텄고, 남은 이들 중 절반은 그저 지켜보거나 혹은 진태경을 호위하듯 감쌌다.

그리고 차갑게 얼어붙은 공기와 팽팽한 긴장감 속, 마침내 원탁의 중심에서 둘은 다시 마주했다.

진태경과 미카엘 실베르트.

미카엘 실베르트와 진태경.

서늘하지만 불꽃 같고, 불꽃 같으면서도 서늘한 두 시선이 서로를 향해 맞닿는 동시에 타올랐다.

모두의 귓가를 파고들만큼 선명한 목소리와 함께.

“자네가 오늘 이 자리에서 보인 행동과 진실이, 어떤 결과를 불러올지 알고 있나?”

“글쎄. 잘은 모르겠네. 아마 이제 별의별 새끼들이 날 물어뜯을 거라는 것 정도?”

진태경이 담담하게 덧붙였다.

“그리고 그중에서 가장 악질인 새끼가, 바로 내 앞에 있다는 것 정도.”

미카엘 실베르트의 볼 근육이 꿈틀거렸다.

이미 진태경이 모두의 앞에서 스스로 진실을 밝힌 그 순간부터 그의 평정심은 흔들리고 있었다.

하지만, 하지만 괜찮다.

왕좌(王佐)는 아직 고스란히 남아 있으니까.

이제 개표가 시작되면, 자신이 앉는 그곳이 바로 왕좌가 될 테니까.

그러나 진태경은, 놈은 아니다.

이제 이 원탁 어디에도 놈이 앉을 자리는 없다.

머지않아 전 세계 어디에도.

“당장 확실한 것 한 가지는 알려 주지. 스톤 킹의 정체가 밝혀진 이상, 안타깝지만 우리 세계 헌터 연맹의 첫 번째 표결은 바로 자네의 영구 퇴출 건이 될 거야.”

“그래? 어째서?”

“그가 정말 일반적인 몬스터의 상식을 벗어난 존재였다면, 그리고 즉각 그 사실을 알렸다면 나를 포함한 모두가 심사숙고했을걸세. 하지만 늦었어. 이런 중대한 비밀을 숨긴 이상 누구도 자네를 신뢰하지 못하니까.”

“저런. 계속해 봐.”

“모든 것은 합법적인 절차에 따라 진행될 걸세. 이 안건에 관련된 이들은 정식으로 기소되어 재판을 받을 것이고, 만약 반항한다면…….”

미카엘 실베르트가 모두를 향해 외치듯 말을 이었다.

“즉결 처분이지.”

숨 막히는 정적.

그러나 천천히 진태경을 향해 고개를 돌린 그 순간. 미카엘 실베르트는 그 정적 속에서 울려 퍼지는 천둥 같은 소리를 들을 수 있었다.

쿵.

가슴이 덜컥 내려앉는다.

쿵. 쿵쿵.

심장 박동이 가파르다. 초승달처럼 휘어진 진태경의 눈매가, 송곳이 되어 가슴 한가운데를 찌르는 듯했다.

뭘까. 무엇일까.

도대체 왜, 놈은 이런 상황에서도 웃고 있을까.

왜?

“한 가지 묻고 싶은 게 있는데.”

문득, 세상이 느려졌다.

두방망이질 치는 가슴과 떨리는 맥박이 귓가를 가득 채우고, 오직 한 사람을 향해 집중된 오감(五感)이 이어지는 말을 받아들인다.

“만약 몬스터와 결탁한 것이 아니라…….”

흐려지는 말꼬리에 미카엘 실베르트가 숨을 삼킨 그 순간. 나직한 한 마디가 그의 세상을 뒤흔들었다.

“이미 몬스터나 다름없다면, 그럼 어떻게 되는 거지?”

“……!”

아니, 모두의 세상을 뒤흔들었다.

인간도, 몬스터도 아닌 무언가를 향한 경멸의 눈빛. 그리고 종지부를 찍는 마지막 한 마디와 함께.

“목의 상처는 다 나았나, 미카엘?”
```

## Final English reading copy

```markdown
# Chapter 779

For a moment, it was as if the world had stopped.

If not for the camera flashes blinking at regular intervals and the second hands ticking, people might really have thought time had frozen.

But the silence didn’t last long.

“Crazy.”

Someone’s voice burst out.

Plenty of people looked back and forth between Jin Taekyung and the Stone King with incredulous smiles on their faces.

They couldn’t help it. Everyone here knew who the Stone King was.

No—ask anyone on the street, and they’d know, too.

An S-rank Hunter with United States citizenship who had appeared like a comet one day.

As skilled as he was handsome, he’d always been by Jin Taekyung’s side. That had drawn considerable attention from the start, and he’d distinguished himself in several major incidents.

He’d once become a target of criticism alongside Jin after taking part in an operation to eliminate terrorists—the one often called the “vigilante incident.” But the general consensus was that, on balance, his contributions far outweighed his faults.

And now the Stone King—by this point recognized as one of the young heroes representing a new generation, and granted a seat at the round table—was a monster?

Instead of confusion, incredulous laughter spread through the crowd.

“Don’t talk nonsense.”

It was hard the first time. After that, it got easier.

The people who had held their tongues out of consideration for Jin Taekyung’s extraordinary skill and standing gradually began to raise their voices.

“Now that we’ve let you go on this long, aren’t you taking things a little too far, young man?”

“Mr. Jin. I respect you as a Hunter, but… you’ll need to give a reasonable explanation for the things you’ve done here today.”

“They said he was suffering from post-traumatic stress disorder. Looks like that was true.”

The fuse was burning down fast.

Even the elders who had looked favorably on Jin from the start let out troubled sighs, while those already on the other side took the opportunity to criticize him openly.

“Everyone, look at what he’s done. He caused a disturbance during this crucial moment when we’re electing the leader of the Federation that will save humanity, and he even damaged the round table.”

“And now he’s spouting nonsense on top of that.”

“What kind of disrespect is this?”

Criticism poured in from every direction.

But the man at the center of it all, Jin Taekyung, opened his mouth to address the room as if he hadn’t heard a thing.

Once again.

Without changing a single word from what he’d said before.

“The Stone King is a monster.”

“That’s all you’ve got? That same nonsense again?”

“He’s crazy. Completely crazy.”

Jin Taekyung slowly looked around.

There were those who laughed in disbelief, those who frowned, and those who watched with grave, steady eyes.

Their reactions varied, but the words that slipped between Jin Taekyung’s lips the next moment remained unchanged.

“The Stone King is a monster.”

“What is this—!”

“Strip him of his qualifications at once!”

The voices of criticism had become shouts. But Jin paid them no mind and opened his mouth again.

“The Stone King is…”

As if those were the only words he knew. As if imprinting those words on people’s minds were the sole purpose of his life.

Without pause, ignoring every gaze and every accusation pouring toward him.

Once again, Jin Taekyung calmly repeated the fact that might become his greatest weakness.

While looking at Michael Silbert, the one man who remained silent amid the commotion that had swallowed the enormous round table.

“A monster.”

That was the third time.

The mocking smiles on people’s lips faded as he repeated the same words like a machine.

The shouts ringing through the room stopped. So did the pointing fingers. Now, no one moved or spoke.

Silence had settled in before anyone knew it.

And in that perfect silence—not even the sound of someone swallowing—a realization suddenly came to them.

Jin Taekyung was telling the truth.

His expression, his voice, his eyes. Every last thing about him was utterly unlike a lie.

And they realized what that meant.

*…No way.*

An unbelievable question crossed everyone’s mind.

At the same time, hundreds of pairs of eyes turned toward one person.

No—toward something that might not even be human.

The Stone King.

The handsome American was still sitting right where he had been from the beginning. But people could see it. They could feel it.

The slight trembling of his eyes and the faint fear seeping through them. The certainty that this was the answer to their question.

Then the truth they had finally accepted came with an enormous unseen shock that swept through the room like a wave.

No—a hammer blow.

“……!”

“……!”

Faced with this unbelievable truth, everyone stared with their mouths agape.

What was reflected now in the wide-open eyes of more than three hundred people was neither a handsome young man nor an S-rank Hunter with outstanding skills and Fame.

There stood a cursed being who could never coexist with humanity, one who had once driven mankind to the brink of disaster.

“…A monster.”

At that moment, someone’s muttered words—more of a groan—broke the silence.

*Clang, clang, clang!*

Beneath the lights illuminating the vast room, hundreds of weapons flashed as they caught the light.

The radiance of Aura, the power God had gifted to humanity, spread in every direction, then turned toward one being.

Along with killing intent so vivid it seemed tangible.

*Ssssss.*

A wind whipped up from somewhere. In the freezing air, countless needle-sharp gazes pierced the Stone King.

Everyone here had been chosen by God for the sole purpose of fighting monsters, and given the name Hunter by humanity.

From the very beginning, they had been given only one duty.

*Kill monsters.*

*Whoooosh.*

And just as hundreds of powers and murderous intentions converged, bearing down on the room and shooting toward their target—

“Stop!”

*Bang!*

A roar like a wild beast’s, its deep resonance wedging into that split-second gap, scattered everything like mist.

At the same time, the faces of the people who had looked ready to swing their weapons at any moment went rigid.

*What the hell…*

A place where immense killing intent and mana were surging was as good as a death trap.

But the voice’s owner had broken that flow. At the very last moment, just as an attack was about to be unleashed, he had slipped through an invisible gap.

And he’d done it so easily it seemed effortless.

*Step. Step.*

The low thud of footsteps broke the suffocating silence.

As one young man cut through the mountain of sabers and forest of swords formed by countless weapons and stood in front of everyone, an elder Hunter with a full head of white hair spoke with a stern expression.

“What do you think you’re doing?”

Recognizing him, Jin Taekyung answered with due respect.

“I’m doing what I have to do, Senior.”

“And what you have to do is… protect that monster?”

“That’s right.”

At Jin’s unhesitating reply, the elder Hunter asked with an expression of disbelief.

“Why?”

“Because he’s my friend.”

“…Your friend?”

“And he’s a comrade-in-arms who saved my life. So I have to protect him. Just as he did for me.”

Friend? Comrade-in-arms?

Everyone was at a loss for words at terms they’d never imagined hearing used for a monster. Then, from within the encirclement that had naturally formed, someone spoke up.

“If you’re going that far, there’s no need to hear anything more.”

A shining suit of full-body armor. A massive war hammer in his hand.

The middle-aged man stepped forward, trailing a heavy aura and an oppressive presence. His eyes were fixed on Jin Taekyung, but his voice was aimed at everyone.

“This is treason against humanity. An unforgivable act of betrayal. You know the punishment for that, don’t you?”

Jin Taekyung nodded.

“Of course.”

“Good. Then you already know. As of this moment, your Hunter license is revoked, and the traitor will be summarily executed.”

*Rumble.*

A thick glow layered itself over the war hammer.

An S-rank Hunter who had fought since the Great Cataclysm, and a heavyweight who had made the name Kronos known as one of the world’s top ten Guilds.

But the reaction Jin Taekyung showed the next moment far exceeded everyone’s expectations.

“Fuck, don’t be so damn ridiculous.”

“What?”

“That speech was so long-winded I couldn’t even follow every stupid point. But first, I want to ask you one thing.”

Jin Taekyung fixed his lowered gaze on the Guild Master of Kronos.

“If you were going to throw this kind of fit, why did you treat me like a lunatic a minute ago?”

“That’s…”

“That’s what?”

The Guild Master of Kronos suddenly found himself at a loss for words.

And not just him. Everyone who had heard Jin’s words was the same.

A remark that struck unexpectedly close to the mark.

That was right. They’d treated Jin Taekyung’s words as nonsense from the start. And even as people criticized him, he’d silently repeated them three times, as if making sure they understood.

Until the mocking smiles vanished from their lips. Until they realized all of it was true.

But even though he’d spoken with such sincerity, why hadn’t they believed that young man?

The answer was simple.

No, perhaps it was a truth they had already known, but had been forced to pretend they didn’t.

“Let’s be honest. Now that you’ve learned the truth, you don’t want to accept it. That the guy sitting over there—some lowly monster, for God’s sake—has fought harder for humanity than some of the assholes who don’t even have any real business being here.”

“……!”

“Of course, I can understand that much. Who’d just take it on faith that the Stone King was a monster? Right?”

No one answered from anywhere in the room. Jin Taekyung smiled.

“This is a black comedy if I’ve ever seen one. There are assholes everywhere who aren’t even human, but the guy who nearly worked himself to death trying to save one more person is standing at death’s door the moment his identity comes out.”

Cold flames flickered in the young man’s eyes, visible above his raised smile.

Countless weapons surrounded them. As he looked at that forest of blades, poised to come flying at any moment, the emotion rising inside him had a name: anger and bitterness.

“I didn’t want things to turn out like this. I wasn’t asking for that much. I just… thought you’d give me enough time to explain.”

Jin Taekyung muttered hollowly.

Of course he understood. Surely many of them had lost someone close to them to a monster.

Just as he had.

But… even so, something churned inside him.

He felt sorry for the Skeleton King, who had fought while sacrificing himself for humanity. He felt bitter watching those people try to kill him without a moment’s hesitation, and his anger rose when he realized how many of them still showed outright hostility, even in this situation.

Because he knew their hostility wasn’t just because he thought of the Skeleton King, a monster, as his friend and comrade-in-arms.

And all the more so because he knew where that hostility was aimed, what its purpose was, and who was behind them, pulling their strings like puppets.

*Step.*

Jin Taekyung suddenly started walking.

The Guild Master of Kronos, the first to realize what that sudden movement meant, swung his war hammer like a bolt of lightning.

No—he tried to swing it.

If not for a voice that suddenly slipped into his ear.

“You’d better stop there, Fabian.”

*Rumble.*

The air quivered.

The Guild Master of Kronos looked at the towering Black man who had risen from his seat, his expression hardening.

“Johnson.”

“It’s been a while. You’ve gotten even more charming with age.”

Magic Johnson gave him a playful wink and flicked his staff toward the war hammer rippling with Aura.

“Whoa. Don’t do anything rash. This is advice from a comrade-in-arms who’s risked his life fighting alongside you.”

“Do you know what your actions mean right now?”

“Of course. So there’s no need to explain it to me. We know exactly where we need to go from here.”

“…We?”

The instant he echoed the word without thinking, he saw the answer with his own eyes.

*Rustle. Thud.*

One after another, people rose from their places quietly, noisily, or with an air of dignity.

The Guild Master of Kronos’s gaze sank as he faced those familiar yet splendid faces.

Starting with Magic Johnson: Chuck Hagel. Faye Chen. Prince Felix.

And then Choi Minwoo, whose symbolic significance as Cheon Taemin’s only blood relative was unmistakable. Finally, even the Stone King, who had been watching the weapons aimed at him with a hard expression, stood up.

*This is bad. It’s already beyond the range Michael predicted.*

But what exceeded his expectations the most was the young man now standing right in front of him.

“Move.”

“I can’t—”

“I said move.”

“……!”

In that moment,

the Guild Master of Kronos felt a chill pierce him to the bone for the first time in a long while.

It was the presence of a young man who hadn’t even lived half as long as he had.

At the same time, the warning he’d heard from Magic Johnson came back to him.

It would be better to stop there. Not to do anything rash.

He understood, too, who that warning had been for.

*Step.*

By the time he came to his senses, it was already too late. The Guild Master of Kronos instinctively shifted to the side, and Jin Taekyung walked on as if that were only natural.

Of the three hundred people packed tightly around them, half had tried to stop him, but soon found themselves moving aside without knowing why. Half of those remaining either watched or surrounded Jin as if to protect him.

And amid the cold air and taut tension, the two finally faced each other again at the center of the round table.

Jin Taekyung and Michael Silbert.

Michael Silbert and Jin Taekyung.

Their gazes met and flared—cold yet fiery, fiery yet cold.

Then came a voice clear enough to pierce everyone’s ears.

“Do you know what consequences your actions and this truth will bring, after what you’ve done here today?”

“Who knows. I don’t know exactly. Maybe a whole lot of assholes will come after me now?”

Jin Taekyung added calmly,

“And the nastiest one of them all is standing right in front of me.”

The muscles in Michael Silbert’s cheek twitched.

From the moment Jin Taekyung had revealed the truth in front of everyone, Michael’s composure had already begun to falter.

But it was fine. It was fine.

The throne was still intact.

Once the vote began, the place where he sat would become the throne.

But Jin Taekyung wouldn’t be fine. Not him.

There was no seat for him anywhere at this round table now.

Soon, there wouldn’t be anywhere in the world for him.

“I’ll tell you one thing for certain. Now that the Stone King’s identity has been revealed, I’m afraid the first vote of our World Hunter Federation will be to expel you permanently.”

“Really? Why?”

“If he truly was unlike any ordinary monster, and you’d told us right away, everyone—including me—would have considered the matter carefully. But it’s too late. After you hid such a grave secret, no one can trust you.”

“Too bad. Go on.”

“Everything will proceed through legal channels. Those involved in this matter will be formally indicted and brought to trial. And if you resist…”

Michael Silbert continued, his voice raised as if to call out to everyone.

“Summary execution.”

A suffocating silence followed.

But the moment he slowly turned his head toward Jin Taekyung, Michael Silbert could hear a thunderous sound echoing through it.

*Thump.*

His heart lurched.

*Thump. Thump-thump.*

His heartbeat quickened. Jin Taekyung’s eyes, curved like crescents, seemed to drive an awl into the middle of his chest.

What was it? Why was it?

Why was that bastard smiling even in a situation like this?

Why?

“There’s one thing I want to ask.”

Suddenly, the world slowed down.

His heart pounded, his pulse trembled, and his five senses, all focused on one person, took in the words that followed.

“What if you hadn’t colluded with a monster, but…”

Michael Silbert swallowed as Jin’s words trailed off. Then a quiet remark shook his world.

“You were already no different from one? What would happen then?”

“……!”

No—it shook everyone’s world.

With a contemptuous gaze fixed on something neither human nor monster, Jin delivered one final line.

“Has the wound on your neck healed, Michael?”
```
