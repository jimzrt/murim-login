<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0773.txt",
      "sha256": "f62a6f5580069b188bf7be268bd139499bd2a0783185c30c9cc0b261c19e5e5a",
      "bytes": 13847
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d3b6fcb57cb73c34db7e5c1d15b33bb8642e16ef2f46086d33e80b608bd11396",
      "bytes": 1894
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "7f1782ba7a45fb761291534917139ffcb877474998bbbfbd616a9476b54249d7",
      "bytes": 222793
    },
    {
      "path": "characters/Baek Hanseong.md",
      "sha256": "c198b614643050ff733401f19112e3d69bb4dfdcf169b974b353bc905d4e627c",
      "bytes": 847
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "55fc60da1b5436bcf225b4d3ec7d1a64cc1df25a1d3016850f7b0bbf7c11ba72",
      "bytes": 752
    },
    {
      "path": "characters/Felix.md",
      "sha256": "c70cd3f5cf0a1272a941b020315d56c03e81caed9e8166d8713e158125bfcd05",
      "bytes": 464
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "4de19b0feb0bf300e9fd890c7b02f43e9ce48a07e63224c9ca20145cf259f4d4",
      "bytes": 1774
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "76c97504674788ce51df3f3c42e8bb5c5abe021f6d2e15c1e50adf25141126a6",
      "bytes": 2096
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "5ac09f7b6b24f9d436238b73521368f2c533ea2fce8ffb7b00943178d2ade0d9",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "995252beccfe609fba6383ddc47a27d8176a797d6b7bd269791c9cfa6aad1ee7",
      "bytes": 1015
    },
    {
      "path": "characters/Song Song.md",
      "sha256": "48d2d60d2936e71a0dc5998a21f9bc428cee2c6032db8fd17846223aea9ff570",
      "bytes": 939
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "68b68bf9e6e29ee657c53fc6411983fd40da554b574a9d5325ddeb8c8201d5d3",
      "bytes": 602
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "db5fe402e0d2350ca6996725992eea293bf837d8df1f2c478255b252d32103a8",
      "bytes": 693
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e1151d16b3c1102b7097d2586a1a8f4c76973a94a74899ddb18af8ee071f8523",
      "bytes": 240482
    }
  ],
  "estimated_tokens": 12332
}
-->

# Durable State Update — Chapter 773

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 773. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 773. Profile updates may replace only one
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
  "chapter": 773,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 773,
    "continuity_sources": [773],
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
    "The Skeleton King remains Jin Taekyung's friend, and Jin refuses to sacrifice him.",
    "Jin, Team Leader Choi, and Magic Johnson are pursuing a possible fourth path against Michael's plan.",
    "Magic Johnson's documents triggered Jin's new hypothesis, but their decisive contents remain unexplained.",
    "The World Hunter Federation has been approved for reestablishment by the UN.",
    "Michael Silbert has converted worldwide fear into public support and scheduled the Federation's inaugural ceremony for tomorrow.",
    "Michael's sensed qi outburst confirms that Jin's hotel disturbance reached across several kilometers.",
    "Michael has ordered continuous surveillance of the monster and increased security before the ceremony.",
    "Michael knows Jin regards the monster as a friend and intends to use that attachment against him.",
    "Michael is secretly communicating with The Prophet through a magic mirror.",
    "Jin is traveling to Korea for the inaugural ceremony."
  ],
  "continuity_sources": [
    772
  ],
  "open_questions": [
    "What did Magic Johnson's documents reveal, and is Jin's fourth path viable?",
    "How will Jin and his allies act before the World Hunter Federation's ceremony tomorrow?",
    "What coordinated plan do Michael and The Prophet have for the Federation and the coming crisis?",
    "Can Jin protect his monster friend if Michael forces him to choose between that friend and the world?"
  ],
  "safe_through": 772,
  "temporary_decisions": [
    "Render 네 번째 길 as fourth path.",
    "Render 발족식 as inaugural ceremony.",
    "Render 기파 as qi wave and preserve 공력이 실린 as infused with internal energy.",
    "Retain World Hunter Federation, Hero's Sword, Magic Johnson, and Cheon Taemin as established renderings.",
    "Render 스톤 킹 as Stone King."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 송송이    | **Song Song**     |
| 천태민    | **Cheon Taemin**  |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 백한성 | **Baek Hanseong** | Twenty-seventh President of Korea and youngest president elected in Korean history. |
| 필릭스 | **Felix** | British prince and S-rank Hunter. |
| 임꺽정 | **Im Kkeokjeong** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 녹림맹주 | **Green Forest Alliance Leader** | Leader title for the Green Forest Alliance. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 청와대 | **Blue House** | Presidential office mentioned in an online comment about proposed legislation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 시벌좌 | **Lord Fuck** | Crude online nickname created from Taekyung's accidental broadcast profanity. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 대통령 | **President** | Title for Korea's head of state. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 꺽정 | **Kkeokjeong** | Jin's injured ally, addressed as Uncle Kkeokjeong. |
| 인천 | **Incheon** | Location of the airport welcome and presidential greeting. |
| 국회의사당 | **National Assembly** | Government building visible from the skyscraper. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 필릭스 | Korean S-rank Hunter addressing a British prince | His Highness | mock-formal and sarcastic | Felix demands formal address, and Jin complies by calling him His Highness while continuing to mock him. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 필릭스 | 진태경 | British prince and S-rank Hunter to allied Korean S-rank Hunter | Jin | lofty and aristocratic | Felix addresses Jin while discussing royal duty and their teleport. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |
| 백한성 | 최민우 | President_to_trusted_political_ally | Team Leader Choi | formal-polite, warm, and politically attentive | Baek addresses Choi as 최 팀장님 during the private Blue House breakfast. |
| 최민우 | 백한성 | political_subordinate_to_President | Mr. President | formal-polite | Choi addresses Baek as 대통령님 during the breakfast and departure. |
| 팀장 | 중년인 | Hunter_team_leader_to_stranger | Boss | casual and polite | The Team Leader mistakes disguised Song for an ordinary raid customer and warns him not to proceed. |
| 송송이 | 최민우 | guild_member_to_guild_master | Team Leader Choi | formal-polite | Song Song addresses Choi by his former title while urging him to rest. |
| 임꺽정 | 최민우 | guild_member_to_guild_master | Team Leader Choi | casual-but-concerned | Im Kkeokjeong uses Choi's former title while warning him about overwork. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |

## Listed compact profiles

### Baek Hanseong.md

# Baek Hanseong (백한성)

- **Safe through:** Chapter 768
- **Aliases:** None
- **Role:** Twenty-seventh President of Korea and the youngest president elected in Korean history who opposed the immediate reestablishment of the World Hunter Federation, tried to buy time for preparations for war, and cast the final vote in the decision that approved its reestablishment.
- **Personality:** Confident, politically shrewd, composed, and willing to needle Lee Jungryong while advancing his anti-Ares stance.
- **Voice:** Polite, self-assured, calm, and lightly teasing.
- **Relationships:** Political counterpart to Lee Jungryong who has established a cooperative relationship with Jin Taekyung and Choi Minwoo while seeking to restrain the power concentrated in their two Guilds.

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 771
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he remains unconscious after more than twenty years in a wired mechanical capsule at his former mansion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Felix.md

# Felix (필릭스)

- **Safe through:** Chapter 734
- **Aliases:** Prince Felix
- **Role:** British prince and S-rank Hunter who joins the reinforcement force against the Arch Lich.
- **Personality:** Haughty, self-important, and conscious of royal duty.
- **Voice:** Formal, lofty, and aristocratic.
- **Relationships:** Travels with Faye Chen and Magic Johnson and is allied with Jin Taekyung.

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 732
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** D-rank Hunter and veteran tank in the Peace Guild; after recovering from the Black Hunters’ attack and having both arms reattached, he continues as a Hunter while nearing the end of rehabilitation.
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother, recommends him to Team Leader Choi, and remembers that Taekyung protected him during an E-Rank Gate attack; married with two children

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 772
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license, as well as a traveler between Murim and another world resembling the realm of immortals and the principal Hunter opposing Michael Silbert's terrorist campaign.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 772
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 772
- **Aliases:** None
- **Role:** Michael Silbert is the Guild Master of Odin Guild, a public hero who helped suppress five Monster Waves, the hidden architect of a coordinated terrorist campaign, and a feared rival whose warning about a second Great Cataclysm triggered worldwide panic and led the UN to approve the World Hunter Federation's reestablishment.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### Song Song.md

# Song Song (송송이)

- **Safe through:** Chapter 746
- **Aliases:** Miss Song
- **Role:** Founding member of the Peace Guild; B-rank healer whose buff magic is powerful enough to be mistaken for an A-rank healer's; Healer Team Leader and temporary head of the Peace Guild's emergency rescue team, which is piloting free public-safety rescues for medium- and low-grade Gates in the capital region.
- **Personality:** Calm, practical, capable, and attentive; speaks briefly and handles domestic work with practiced skill
- **Voice:** Calm, concise, polite, and capable of devastatingly blunt candor
- **Relationships:** Works alongside Team Leader Choi, Butler Kim, Im Kkeokjeong, and Jin Taekyung as a member of the Peace Guild; Jin recruited her to help run its emergency rescue team, while she remains his same-age friend and guildmate after rejecting his confession.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 770
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Jin Taekyung's meticulous intelligence and operations lead, a trusted ally and natural leader capable of guiding the reestablished World Hunter Federation.
- **Personality:** Calm, pragmatic, meticulous, and emotionally steady under pressure.
- **Voice:** Measured, professional, and reassuring without minimizing responsibility.
- **Relationships:** A trusted ally and operational adviser to Jin Taekyung.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 772
- **Aliases:** None
- **Role:** The Prophet is the mysterious leader of the revived Hasasin, a Middle Eastern terrorist organization preparing further attacks against apostates and Western heretics.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors, is revered by the followers, and secretly communicates with Michael Silbert through a magic mirror.

## Korean source

```text
＃773화



돌아갈 곳이 있다는 건 좋은 거다. 그곳에 나를 기다려 주는 사람들이 있다면 더더욱.

“최 팀자아앙! 태경아아아!”

몇 시간의 비행 끝에 인천공항에 도착한 우리를 향해, 저 멀리서부터 쿵쿵거리며 달려온 털북숭이 거한이 양팔을 활짝 벌렸다.

퍽!

숨이 턱 막혔다.

하지만 포옹을 빙자한 바디 초크에도 나와 최 팀장은 울먹거리는 임꺽정의 어깨를 두드려 주었다.

그냥, 그래야 할 것 같아서,

“왜 울어요. 벌써 갱년기야?”

“잘 지냈, 으헝. 다친 곳은 없, 으허허헝!”

“저희는 괜찮습니다. 진정하세요.”

“내가 얼마나 걱정, 걱정했는, 크흐흑!”

겉모습만 보면 녹림맹주도 한 수 접어 줘야 할 것 같은데, 감수성 하나는 따라올 사람이 없다.

겉과 속이 따로 노는 사람이라고 해야 하나.

그리고 그런 임꺽정의 어깨너머에서는, 인상만큼이나 시원시원한 목소리가 들려오고 있었다.

“내가 아니라 우리가 걱정했다고 하셔야지. 그렇게 말씀하시면 제가 뭐가 돼요?”

걸음을 멈춘 송송이가 신중한 눈빛으로 나와 최 팀장을 훑었다.

“음. 둘 다 생각보다 괜찮아 보이네.”

내가 되물었다.

“확실해? 이대로면 5분 안에 질식할 것 같은데.”

“그건 5분 뒤고. 지금은 괜찮아 보여.”

“눈 시뻘겋게 충혈된 거 안 보이냐. 사흘 동안 잠도 제대로 못 잤다.”

“왜, 며칠 전에 TV에서 봤던 것보단 훨씬 괜찮아 보이는데?”

송송이가 덧붙였다.

“그때는 눈이 맛이 가 있더라. 당장 죽어 가는 사람처럼.”

“……지금은?”

“글쎄. 한 백 년쯤 후에 죽을 것 같은 느낌?”

뭐라 대꾸할 말이 떠오르지 않아 씩 웃었다.

송송이의 말처럼, 몸은 피곤해도 정신은 며칠 전과 비교도 할 수 없을 만큼 또렷했다.

나도, 그리고 최 팀장도.

“제가 부탁드린 부분은 어떻게 됐습니까?”

최 팀장의 물음에 송송이가 목소리를 낮췄다.

“팀장님 지시는 제대로 전달했어요. 평화, 아레스 두 곳 모두. 막상 추려 보니까 열 명도 안 되더라고요. 그만큼 충성파지만.”

“정보가 새어 나갔을 가능성은 없습니까?”

“두 길드의 중진 중에서는 확실히 믿을 만한 사람들로만 선별했어요. 가족들도 전부 국내에 머무르고 있고.”

“잘하셨습니다. 이후부터는 제가 직접 지시를 내리도록 할 테니, 송이 씨께서는 기밀 유지에 신경 써 주십시오.”

고개를 끄덕인 송송이가 조심스럽게 입을 열었다.

“그런데 정말 미카엘 실베르트가…….”

“쉿.”

언제 울먹였냐는 듯 멀쩡한 얼굴로 송송이의 말을 가로막은 임꺽정이, 우리만 들을 수 있을 만큼 작은 목소리로 속삭였다.

“저기 온다.”

그의 말대로였다.

한적한 활주로를 부드럽게 가로지른 여러 대의 리무진이 우리 앞에서 멈췄고, 잠깐 못 본 사이 십 년쯤 늙어 버린 백한성 대통령이 차에서 내렸다.

“두 분 모두, 귀국을 환영합니다.”

얼굴만큼이나 피곤에 찌든 목소리였다.



* * *



평일 오후.

평소였다면 인산인해를 이루었을 공항 내부는 조용했다. 아니, 내부뿐만 아니라 바깥의 상황도 그리 다르지 않았다.

리무진 창밖으로 스쳐 지나가는 풍경 속에는 어딜 가나 경찰과 군인들이 보였고, 드문드문 검은 정장과 이어 마이크를 찬 이들이 눈에 띄었다.

물론 그들의 가슴팍에 달린 청와대 배지도 함께.

“조용해서 좋네요.”

“말씀하신 대로, 보안을 위해 사전에 모두 해산시켰습니다.”

백한성 대통령이 다 마신 홍삼즙을 버리며 말을 이었다.

“물론 그 테러리스트를 생각해서라도 당연히 해야 할 조치였고요.”

여기서 말하는 그 테러리스트란 바로 선지자를 일컬음이다.

불과 몇 시간 전만 해도 엄청난 숫자의 취재진과 환영 인파가 인근을 에워싸고 있었다는 이야기를 덧붙인 백한성 대통령이 중얼거렸다.

“대통령으로서 할 말은 아니지만, 최근 들어서는 다들 제정신이 아닌 것 같습니다. 분위기가 너무 극단적으로 흘러가고 있어요.”

그의 말에 동의하고, 동시에 저들을 이해한다.

스스로를 지킬 힘이 없는 이들은 위기 앞에서 극단적일 수밖에 없다.

당장 내일 인류가 멸망할 것처럼 공포에 떨고, 희망이라는 단어에 맹목적으로 돌변하는 것이다.

“……그걸 노렸겠지.”

“네?”

“아닙니다. 그냥 혼잣말이었어요.”

무심코 흘러나온 중얼거림에 뭔가를 느낀 백한성 대통령이 복잡한 표정을 지었지만, 나는 말 없이 창밖으로 시선을 돌렸다.

지금까지 그가 상당한 도움을 준 것은 사실이다. 더불어 향후 벌어질 일들을 생각한다면 더 많은 도움을 줄 수도 있다.

하지만 백한성 대통령에게 모든 사실을 털어놓을 수 없는 이유는, 그를 믿지 못해서가 아니라 그의 주변 상황을 믿지 못해서였다.

‘방법이야 많으니까.’

미카엘 실베르트의 눈과 귀는 지천에 깔려 있다.

백한성 대통령의 최측근 중 프락치가 있을 수도 있고, 감시당할 가능성도 충분하다.

믿을 수 없는 진실을 마주하는 순간 누구나 동요하기 마련.

단지 노련한 정치인이라고 해서 모든 감정을 숨길 수 있는 것은 아니었고, 그로 인해 적이 낌새를 알아차린다면 전황(戰況)은 더더욱 불리해진다.

‘우리가 발견한 그 실마리가, 진실이 아닐 가능성 역시 배제할 수 없고.’

자연스럽게 마주친 최 팀장의 시선에서도 나와 같은 생각이 읽혔다.

그 역시 평화 길드와 아레스 길드에 속한 중진 중에서도 가장 믿을 만한 극소수의 인물들에게만 지시를 내린 상태.

최 팀장의 지시는 매우 은밀한 방식으로 전해졌고, 그마저도 우리가 알아낸 진실과는 무관한 내용이었다.

다만 이건 만일의 경우를 대비한 안전장치다. 수류탄의 핀이 뽑히기 전에, 혹은 폭발의 여파가 뻗어 나가는 것을 막을 안전장치.

그러나 현재로서 확신할 수 있는 것은 아무것도 없다.

이제 24시간도 남지 않은 발족식이 어떻게 끝나느냐에 따라, 모두의 운명이 결정된다.

미카엘 실베르트와 나.

적들과 우리라는 단순한 개념을 넘어, 이 세상이 앞으로 흘러갈 방향이.

부우우웅.

이토록 복잡한 마음과는 달리 우리를 태운 리무진은 뻥 뚫린 도로를 시원하게 질주했고, 백한성 대통령은 여러 가지 소식들을 전해 주었다.

현재의 국제 정세. 발족식의 장소로 국회의사당을 지정했다는 것과 지금까지 정해진 참여 인원의 명단 등.

그리고 철통같은 경호 속에서 지내고 있는 어머니와 하연이의 소식까지도.

“가족분들께서 소식을 듣고 많이 걱정하고 계십니다. 혹시 원하신다면 지금 바로…….”

흐려지는 말꼬리에 담긴 뜻을 알아차린 내가 고개를 저었다.

“아닙니다. 발족식이 끝난 후에 찾아뵐 생각이라서.”

“그래도 괜찮으시겠습니까?”

“그럼요.”

세상 누구보다 그립고 보고 싶은 가족들이었지만, 지금 같은 모습으로 가족들을 만날 수는 없었다.

아니, 만나서는 안 된다.

가족들을 만나면 내 자신이 흐트러질까 두려웠다.

모든 일을 해결한 후에, 편안한 마음으로 어머니와 하연이를 마주하고 싶었다. 그들의 따뜻한 품에 안겨 쉬고 싶었다.

‘……그럴 수 있다면.’

차마 덧붙일 수 없었던 그 한 마디가 혀끝에서 맴돌다 흩어진 그때, 백한성 대통령이 문득 생각났다는 듯이 물었다.

“그런데, 다른 한 분은 어디 계십니까?”

“아.”

“전달받은 입국 명단에는 분명 있었던 것 같은데…… 혹시 무슨 일이라도?”

잠시 망설이던 나는 최 팀장과 눈이 마주쳤다. 그리고 쓴웃음을 지으며 대답했다.

“좀 늦을 겁니다. 사정이 생기는 바람에.”

거짓말이었다.

스켈레톤 킹은 지금 우리와 함께 있으니까.

다만 다른 이들은 볼 수 없고, 느낄 수 없는 미지의 공간에서 끝나지 않는 침묵만을 지키고 있을 뿐이다.

지금 이 순간조차도.

- 언제까지 거기 처박혀 있을 거냐.

그러나 이번에도 돌아오는 대답은 없었다.



* * *



그날, 전 세계의 모든 관심은 동아시아의 작은 반도에 집중되어 있었다.

TV에서는 웃고 떠드는 예능 프로그램을 찾아볼 수 없었고, 수많은 뉴스와 시사 채널. 그리고 인터넷 커뮤니티는 코앞으로 다가온 세계 헌터 연맹의 첫 발족식으로 뜨겁게 달아올랐다.



이번 발족식 때 누구누구 오냐.

└ 모른다. 애초에 테러 위험 때문에 명단 공개도 안 한다고 못 박았음. 공항도 싹 비워 놨고.

└ 실시간 송출도 안 한다던데. 그래도 녹화는 할 테니까 다 끝난 후에야 알게 되지 않을까.

└ 그걸 왜 공개 안 함? 애초에 테러 걱정되면 UN 때처럼 화상 회의로 하든가.

└ 팩트) 대격변 때도 직접 참여했다.

└ 무슨 일이 있어도 물러서지 않겠다는 의미 표명임. 지금까지가 각개 전투였다면, 연맹 설립된 이상 선지자도 ㅈ 됨.

└ 근데 아무래도 대표는 천태민이 유력하겠지?

└ ㅇㅇ태민좌 아니면 누가 하냐.

└ 미카엘 실베르트.

└ 진태경.

└ 시벌좌 좋아하긴 하는데, 미카엘 실베르트에 비하면 확실히 밀림. 짬도 짬이고 최근 보이는 행보가 어마무시함.

└ 무슨 상관이냐. 어차피 천태민인데.

└ 그건 그렇지.

└ 천태민이 너무 오랫동안 안 나타나서 그런가. 난 좀 쎄한데. 나만 그럼?

└ 그럼 보일러를 틀어.



누가 발족식에 참여할지. 그들이 한자리에 모여 누구를 자신들의 대표로 선출할지에 대한 이야기가 끊임없이 이어졌다.

그리고 천천히 흘러가는 시간 속. 수천, 수만 킬로미터를 가로질러 반도를 찾아온 손님들이 있었다.

“잠시 간단한 신원 확인 절차가 있겠습니다.”

잘 정돈된 갈색 머리와 은은한 초록빛 눈동자.

지금 막 동화 속에서 튀어나온 것 같은 청년이 위엄 어린 목소리로 입을 열었다.

“케임브리지 공작, 스트래선 백작. 캐릭퍼거스 남작. 가터 훈장의 기사, 사슬 훈장의 기사인 필릭스 알렉산더 루이라고 한다.”

“예?”

“허울뿐인 직함이니 편하게 부르게.”

“아, 알겠습니다. 그럼 미스터 필릭스…….”

“편하게 필릭스 알렉산더 루이 전하라고 부르게. 편하게.”

“……예.”

필릭스 왕자가 스캔을 통해 간단한 신원 확인 절차를 끝마친 그때, 그의 머리 위로 커다란 그림자가 드리워졌다.

“오랜만이야. 필릭스. 아, 전하라고 불러야 하나?”

한참 위에서 내려다보는 낯익은 얼굴에, 문득 눈살을 찌푸리는가 싶던 필릭스 왕자가 표정을 누그러트렸다.

다른 사람이었다면 호통을 쳤겠지만, 상대는 어느 정도의 무례를 저질러도 용납할 수 있는 몇 안 되는 인물이었으니까.

“미스터 존슨.”

매직 존슨이 슬쩍 웃었다.

“이제 막 도착했나?”

“그렇소.”

“곧 파이 첸도 올 거야. 중국에서 함께 싸웠던 전우들이 한자리에 모이겠군.”

“그런 셈이오. 그런데 뒤에 계신 신사분은?”

“동행이야. 물론 신사는 아니고.”

실제로 마주하는 건 처음이었지만, 필릭스 왕자는 금세 매직 존슨과 함께 온 중년인의 정체를 알아볼 수 있었다.

매직 존슨만큼이나 거대한 덩치에, 서부 개척 시대에서 막 튀어나온 것 같은 복장. 거기에 더해 입가에 문 시가까지.

“……척 헤이글.”

금연 표식 앞에서 시가를 뻑뻑 피워 대던 척 헤이글이 대답했다.

“지금 나 불렀나, 왕자?”

신경질적인 어조에 매직 존슨이 슬쩍 앞으로 나섰다.

“마침 만난 김에, 가볍게 한 잔 어때? 파이 첸까지 함께.”

잠시 두 사람을 물끄러미 응시하던 필릭스 왕자가 고개를 저었다.

“생각 없소.”

“저런. 아쉽네.”

“내일 봅시다. 두 분 다.”

“그래. 그럼 그러자고.”

평소와 다름없는 대화.

가볍게 고개를 까딱인 필릭스 왕자는 곧장 수행원들과 함께 걸음을 옮겼다.

삼엄한 호위 아래에 배정된 숙소에 도착하여 짐을 풀고, 발족식이 열릴 내일을 위하여 일찍 잠자리에 들었다.

아니, 모두의 눈엔 그렇게 보였다.

하지만…….

달칵.

잠겨 있던 문이 열리고, 불이 켜졌을 때.

은밀히 숙소를 빠져나온 필릭스 왕자는 볼 수 있었다.

어둠 속에서 그를 기다리고 있던 인영들의 정체를. 그리고 그들의 중심에 앉아 있는 한 청년을.

“오랜만이네. 왕자 전하.”

필릭스는 피식 웃었다.

최민우도, 매직 존슨과 척 헤이글도. 파이 첸도 따라 웃었다.

아무도 모르는, 그들만의 밤이 깊어 가고 있었다.
```

## Final English reading copy

```markdown
# Chapter 773

It was good to have somewhere to return to. Even better if there were people waiting for me there.

“Team Leader Choi! Taekyung!”

After several hours of flying, we arrived at Incheon Airport. From far away, a hairy giant came thundering toward us with both arms spread wide.

Whump!

The air caught in my throat.

Even while being subjected to a body choke disguised as a hug, Team Leader Choi and I patted Im Kkeokjeong on the shoulder as he sobbed.

Just because it felt like we should.

“Why are you crying? Have you hit menopause already?”

“You’ve been okay—waaah! You’re not hurt anywhere—waaaah!”

“We’re fine. Please calm down.”

“I was so worried, so worried that—sniff!”

Judging by his appearance alone, even the Green Forest Alliance Leader would have to step aside for him. But when it came to sensitivity, no one could compare.

You could say his outside and inside were two entirely different people.

And from over Im Kkeokjeong’s shoulder came a voice as clear and direct as the impression its owner gave.

“You should say *we* were worried, not *I*. What does that make me when you put it like that?”

Song Song stopped walking and carefully looked Team Leader Choi and me up and down.

“Hmm. You both look better than I expected.”

I asked in return,

“Are you sure? At this rate, I’ll be suffocated in five minutes.”

“That’ll be in five minutes. You look fine right now.”

“You don’t see how bloodshot my eyes are? I haven’t slept properly in three days.”

“Why? You look much better than you did on TV a few days ago.”

Song Song added,

“Your eyes looked completely out of it back then. Like you were about to drop dead.”

“…And now?”

“Who knows? You look like you’ll die in about a hundred years.”

I couldn’t think of anything to say, so I just grinned.

Just as Song Song had said, my body was exhausted, but my mind was clearer than it had been a few days ago—by an incomparable margin.

Mine, and Team Leader Choi’s.

“What happened with the matter I asked you to handle?”

At Team Leader Choi’s question, Song Song lowered her voice.

“I delivered your instructions properly—to both the Peace and Ares Guilds. Once I narrowed the list down, there weren’t even ten people. But the ones I chose are all staunch loyalists.”

“Is there any chance the information leaked?”

“I selected only the people among the two Guilds’ senior members whom we could trust without question. Their families are all staying in Korea, too.”

“Well done. From this point on, I’ll issue the instructions myself, so please focus on maintaining secrecy, Miss Song.”

Song Song nodded, then cautiously opened her mouth.

“But is it really Michael Silbert…?”

“Shh.”

As though he had never been crying, Im Kkeokjeong cut her off with a perfectly composed face. He whispered so quietly that only we could hear.

“He’s coming.”

He was right.

Several limousines smoothly crossed the deserted runway and came to a stop in front of us. Baek Hanseong, the President, stepped out of one of them. In the short time since we had last seen him, he seemed to have aged by about ten years.

“I welcome you both back home.”

His voice was as worn out as his face.

* * *

A weekday afternoon.

The airport would normally have been packed with people, but the interior was quiet. No, the situation outside was not much different.

Through the limousine window, we saw police officers and soldiers everywhere we looked. Here and there, people in black suits wearing earpieces caught our eyes.

The Blue House badges on their chests were visible, of course.

“It’s nice and quiet.”

“As you requested, we dismissed everyone in advance for security reasons.”

Baek Hanseong continued as he threw away the red ginseng juice he had finished drinking.

“Of course, it was also the obvious thing to do considering that terrorist.”

The terrorist he was referring to was The Prophet.

Baek Hanseong added that only a few hours earlier, enormous numbers of reporters and well-wishers had surrounded the area. Then he muttered,

“This may not be something I should say as President, but lately, everyone seems to have lost their minds. The atmosphere is becoming far too extreme.”

I agreed with him, and at the same time, I understood them.

People who lacked the power to protect themselves had no choice but to become extreme in the face of a crisis.

They trembled in fear as though humanity would perish tomorrow, then turned blindly fanatical at the word *hope*.

“…That’s what he was aiming for.”

“Pardon?”

“Nothing. I was just talking to myself.”

Baek Hanseong seemed to sense something in my thoughtless mutter and wore a complicated expression, but I silently turned my gaze toward the window.

It was true that he had helped us considerably so far. And considering what would happen in the future, he might be able to help us even more.

But the reason I couldn’t tell Baek Hanseong everything was not that I didn’t trust him. It was that I didn’t trust the circumstances surrounding him.

*There are plenty of ways.*

Michael Silbert’s eyes and ears were everywhere.

There could be a mole among Baek Hanseong’s closest advisers, and there was every chance he was being watched.

The moment anyone was confronted with an unbelievable truth, they were bound to be shaken.

Being an experienced politician did not mean he could hide every emotion. If the enemy noticed something because of that, the situation would become even more disadvantageous.

*And we can’t rule out the possibility that the clue we found isn’t the truth.*

I could read the same thought in Team Leader Choi’s eyes when our gazes naturally met.

He, too, had given instructions only to the smallest handful of the most trustworthy senior members of the Peace and Ares Guilds.

Team Leader Choi’s instructions had been delivered in an extremely covert manner, and even those instructions had nothing to do with the truth we had uncovered.

They were merely a safeguard against the worst-case scenario—a safeguard for use before the grenade’s pin was pulled, or to stop the effects of the explosion from spreading.

But at present, there was nothing we could be certain of.

With less than twenty-four hours remaining before the inaugural ceremony, everyone’s fate would be decided by how it ended.

Michael Silbert and me.

Beyond the simple concept of enemies and allies, the direction in which this world would move from here on out.

Vroooom.

In contrast to my tangled thoughts, the limousine carrying us sped smoothly down the wide-open road, and Baek Hanseong brought us up to date on several matters.

The current international situation. The decision to designate the National Assembly as the location of the inaugural ceremony. The list of participants decided so far.

He even told us how my mother and Hayeon were doing under ironclad protection.

“Your family is very worried after hearing the news. If you wish, we can go see them right now…”

I understood the meaning contained in his trailing words and shook my head.

“No. I plan to visit them after the inaugural ceremony.”

“Are you sure that will be all right?”

“Of course.”

They were the family I missed and longed to see more than anyone else in the world, but I couldn’t meet them in my current state.

No, I shouldn’t meet them.

I was afraid that seeing my family would make me lose my composure.

Once everything was resolved, I wanted to face my mother and Hayeon with a peaceful mind. I wanted to rest in their warm embrace.

*…If that’s possible.*

That one thought, which I couldn’t bring myself to add aloud, lingered on the tip of my tongue before scattering.

Then Baek Hanseong suddenly asked, as though he had just remembered something,

“But where is the other person?”

“Ah.”

“I’m fairly certain he was on the list of people entering the country… Has something happened?”

I hesitated for a moment, then met Team Leader Choi’s eyes. With a bitter smile, I answered,

“He’ll be late. Something came up.”

It was a lie.

The Skeleton King was with us right now.

He was simply maintaining an endless silence within a mysterious space no one else could see or sense.

Even at this very moment.

*How long are you going to stay holed up in there?*

But this time, too, there was no answer.

* * *

That day, the attention of the entire world was focused on a small peninsula in East Asia.

There were no variety shows full of laughter and chatter on television. Countless news and current-affairs channels, along with internet communities, were burning with the first inaugural ceremony of the World Hunter Federation, which was now right before them.

Who’s coming to the inaugural ceremony?

└ No idea. They flat-out said they wouldn’t release the list in the first place because of the terrorist threat. They cleared out the airport, too.

└ I heard they aren’t broadcasting it live, either. They’ll record it, though, so won’t we find out only after it’s over?

└ Why not make it public? If they’re worried about terrorism, they should hold a video conference like they did with the UN.

└ Fact) They participated in person even during the Great Cataclysm.

└ It means they’re declaring that they won’t back down no matter what happens. Until now, it was everyone fighting separately, but now that the Federation is being established, The Prophet is fucked.

└ But Cheon Taemin is obviously the most likely representative, right?

└ Yeah. Who else would do it if not Lord Taemin?

└ Michael Silbert.

└ Jin Taekyung.

└ I like Lord Fuck, but he’s definitely outmatched by Michael Silbert. Michael’s got seniority, and his recent moves have been insane.

└ What does that have to do with anything? It’s obviously Cheon Taemin.

└ That’s true.

└ Maybe it’s because Cheon Taemin hasn’t shown up in so long, but I’m getting chills. Anyone else?

└ Then turn on the boiler.

The conversation over who would attend the inaugural ceremony continued without end. Who would gather in one place, and whom they would choose as their representative.

And as time flowed slowly onward, guests who had crossed thousands, even tens of thousands, of kilometers to reach the peninsula began arriving.

“There will be a brief identity-verification procedure.”

With neatly styled brown hair and subtly green eyes, a young man who looked as though he had just stepped out of a fairy tale spoke in a dignified voice.

“I am Felix Alexander Louis, Duke of Cambridge, Earl of Strathearn, Baron Carrickfergus, Knight of the Order of the Garter, and Knight of the Order of the Chain.”

“Pardon?”

“They are merely empty titles, so feel free to address me casually.”

“Ah, understood. Then, Mr. Felix…”

“Feel free to call me His Highness Prince Felix Alexander Louis. Feel free.”

“…Yes.”

Just as Prince Felix finished the brief identity-verification procedure through the scanner, a large shadow fell over his head.

“It’s been a while, Felix. Or should I call you His Highness?”

At the familiar face looking down at him from far above, Prince Felix seemed about to frown, but then relaxed his expression.

Had it been anyone else, he would have shouted at them. But the person in front of him was one of the few people whose rudeness he could tolerate to a certain degree.

“Mr. Johnson.”

Magic Johnson gave a slight smile.

“Did you just arrive?”

“I did.”

“Faye Chen will be here soon, too. The comrades who fought together in China will all be gathered in one place.”

“That is so. But who is the gentleman behind you?”

“He’s with me. Though he isn’t a gentleman, of course.”

It was his first time meeting him in person, but Prince Felix quickly recognized the identity of the middle-aged man who had come with Magic Johnson.

He was as huge as Magic Johnson, dressed as though he had just stepped out of the American frontier era, and had a cigar clamped between his lips.

“…Chuck Hagel.”

Chuck Hagel, who had been puffing away at his cigar in front of a no-smoking sign, answered,

“Did you call me, Prince?”

At his irritable tone, Magic Johnson subtly stepped forward.

“Since we’ve run into each other, how about a drink? With Faye Chen, too.”

Prince Felix stared at the two men for a moment, then shook his head.

“I have no interest.”

“What a shame.”

“See you tomorrow. Both of you.”

“Sure. Then we’ll do that.”

It was an ordinary conversation, no different from usual.

Prince Felix gave a casual nod, then immediately walked away with his attendants.

He arrived at the lodging assigned to him under tight security, unpacked his luggage, and went to bed early in preparation for the inaugural ceremony the next day.

No. That was how it appeared to everyone else.

But…

Click.

When the locked door opened and the lights came on, Prince Felix—having secretly slipped out of his lodging—saw the figures waiting for him in the darkness, and the young man seated at their center.

“It’s been a while, Your Highness.”

Felix let out a quiet laugh.

Choi Minwoo, Magic Johnson, Chuck Hagel, and Faye Chen laughed along with him.

Their private night, known to no one else, was growing deeper.
```
