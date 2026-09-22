<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0733.txt",
      "sha256": "4eb1910a3de8eec11a7255c733c1e15251abc8964e646ff29402e63d60d328cb",
      "bytes": 12660
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "060e93f43c10be300c991649e483e7fde8ee693d31ff41721f3972d0ceb0a4fb",
      "bytes": 1899
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "7cc5f2e64b6a3d737cd369d235640e5b04186128234704acc4020f1e15131bb4",
      "bytes": 210876
    },
    {
      "path": "characters/Baek Hanseong.md",
      "sha256": "94bc8d37461037e9df68593efb21df349901b55338032f5e4f3e6af9366a3e7c",
      "bytes": 861
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "591e4992ae3ba577da1ce9bc8422dceb3e47e1a2e9b0dd1d7fb7de3a332d59ea",
      "bytes": 752
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "e0f2e5e4de73afb0fab22cb8c85e730a480e1cbf54e3a72abc42dc91c0881104",
      "bytes": 553
    },
    {
      "path": "characters/Felix.md",
      "sha256": "15a0d4f758d951cda6986296b20d2bfece3a77bb7ee3859c60f8f5a1477606f4",
      "bytes": 464
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "7dc40cf588c2c89bc5b1c6fb16cec7227dde453889009abaf9ea316b9d71d04e",
      "bytes": 2011
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "b892de5c2af320972dc57fd274a814a0a8a5fe350f7e7a6b3ac3c168120e23c2",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "c0537ebd5ea1f7653749dd24d2f97109d02ad7bea0d15d8ffa45c0eb69dafc6a",
      "bytes": 1384
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0c8d65442d376074d887e6f86d09eefba91cdde4e689a737e9829b32cff714fc",
      "bytes": 223368
    }
  ],
  "estimated_tokens": 10958
}
-->

# Durable State Update — Chapter 733

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 733. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 733. Profile updates may replace only one
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
  "chapter": 733,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 733,
    "continuity_sources": [733],
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
    "Jin Taekyung publicly posted the prepared file through his personal social-media account, whose follower count exceeds five hundred million.",
    "Huginn delivered Odin Guild's opposition, displayed S-rank-level power, and withdrew after Team Leader Choi warned him against escalating the confrontation.",
    "Team Leader Choi suspects Huginn came to confirm Cheon Taemin's absence rather than merely oppose the Mana Cultivation Method.",
    "Only six people currently know that Cheon Taemin is in a vegetative state; Lee Jungryong, Song Cheonwoo, and Go Jun were among the former holders of the secret and are dead.",
    "A Grand Mage-level mage constructed Ares Guild's Area A, creating a possible route by which the secret could have leaked.",
    "Team Leader Choi now regards Jin Taekyung as a Joker card and is willing to act more boldly because Jin is present.",
    "Odin Guild may possess hidden S-rank Hunters, and Jin expects other major Guilds may support Odin.",
    "Go Jun's necklace disappeared from secured evidence storage without triggering its protective Magic."
  ],
  "continuity_sources": [
    732
  ],
  "open_questions": [
    "Who is the Guild Master of Odin?",
    "Does Odin already know Cheon Taemin's condition, and was the Grand Mage-level mage connected to Lee Jungryong the source of a leak?",
    "What repercussions will Odin Guild and the other major Guilds impose after the Mana Cultivation Method is released?",
    "How did Go Jun's necklace disappear without triggering the storage room's protective Magic?"
  ],
  "safe_through": 732,
  "temporary_decisions": [
    "Render 아크 리치 as Arch-Lich.",
    "Render 벙어리 삼룡이 as Samryong the Mute with a brief explanatory footnote.",
    "Render 최 팀장님 as Team Leader Choi and 진태경 씨 as Mr. Jin Taekyung in formal dialogue."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 사형     | **Senior Brother**                           |
| 상태               | **Status**                     |
| 지능               | **Intelligence**               |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 사천     | **Sichuan**            |
| 백한성 | **Baek Hanseong** | Twenty-seventh President of Korea and youngest president elected in Korean history. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 필릭스 | **Felix** | British prince and S-rank Hunter. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 대한민국 | **Korea** | Country reference. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 청와대 | **Blue House** | Presidential office mentioned in an online comment about proposed legislation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 계도 | **precept blades** | Blades carried by the Hundred and Eight Arhats. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 영국 | **United Kingdom** | Country associated with BCC. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 중화인민공화국 | **People's Republic of China** | Formal country name shouted by the Chinese Hunters. |
| 대통령 | **President** | Title for Korea's head of state. |
| 주석 | **Chairman** | Political title used for Xiao Yang. |
| 중화 | **Zhonghua** | Patriotic term used in Shao Shen’s rallying speech. |
| 태자당 | **Crown Prince Party** | The faction associated with General Liao. |
| 도람프 | **Doramp** | Parodic name for the U.S. president in a forum headline. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 인자 | **ninja** | Japanese assassin skilled in concealment and concealed weapons. |
| 마비 | **Paralyzed** | Status abnormality inflicted by Kraken's Ink. |
| 정룡 | **Jungryong** | Cheon Taemin's trusted associate who joined the Peace Guild. |
| 철옹성 | **impregnable fortress** | Metaphor for Ares Guild's entrenched defenses. |
| 펜타곤 | **Pentagon** | Headquarters of the United States Department of Defense and source of intelligence about terrorist experiments. |
| 신인 | **divine man** | Descriptive term for a human who became something beyond humanity. |
| 오딘 | **Odin** | The name of the world's greatest Guild, invoking the Norse god. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
| 이정룡 | 백한성 | Ares authority to national head of state | Mr. President | formal-polite | Uses 대통령 각하 while greeting Baek Hanseong. |
| 백한성 | 이정룡 | President to Ares Guild Vice Guild Master | Vice Guild Master Lee | formal-polite | Uses 이정룡 부길드장님 while discussing the Chinese proposal. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 필릭스 | 이정룡 | British prince to senior S-rank Hunter | Jungryong Lee | formal through a translation device | Felix permits Lee to omit His Highness and gives his own preferred form of address. |
| 진태경 | 필릭스 | Korean S-rank Hunter addressing a British prince | His Highness | mock-formal and sarcastic | Felix demands formal address, and Jin complies by calling him His Highness while continuing to mock him. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 필릭스 | 진태경 | British prince and S-rank Hunter to allied Korean S-rank Hunter | Jin | lofty and aristocratic | Felix addresses Jin while discussing royal duty and their teleport. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |
| 팀장 | 중년인 | Hunter_team_leader_to_stranger | Boss | casual and polite | The Team Leader mistakes disguised Song for an ordinary raid customer and warns him not to proceed. |

## Listed compact profiles

### Baek Hanseong.md

# Baek Hanseong (백한성)

- **Safe through:** Chapter 729
- **Aliases:** None
- **Role:** Twenty-seventh President of Korea and the youngest president elected in Korean history who leads the government's public response to the Mutated Gate crisis, supports Jin Taekyung in public appearances, and publicly backs the national project to release Cheon Taemin's Mana Cultivation Method.
- **Personality:** Confident, politically shrewd, composed, and willing to needle Lee Jungryong while advancing his anti-Ares stance.
- **Voice:** Polite, self-assured, calm, and lightly teasing.
- **Relationships:** Political counterpart to Lee Jungryong who has established a cooperative relationship with Jin Taekyung and Choi Minwoo while seeking to restrain the power concentrated in their two Guilds.

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 732
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he remains unconscious after more than twenty years in a wired mechanical capsule at his former mansion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 731
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Felix.md

# Felix (필릭스)

- **Safe through:** Chapter 434
- **Aliases:** Prince Felix
- **Role:** British prince and S-rank Hunter who joins the reinforcement force against the Arch Lich.
- **Personality:** Haughty, self-important, and conscious of royal duty.
- **Voice:** Formal, lofty, and aristocratic.
- **Relationships:** Travels with Faye Chen and Magic Johnson and is allied with Jin Taekyung.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 732
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, a traveler between Murim and another world resembling the realm of immortals, and the creator of the beginner-accessible Smiling Mana Cultivation Method.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 732
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 732
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regarded Cheon Taemin as an older brother despite no blood relation and long held him in respect and fear; secretly supported the orphanage where Lee Dongseok grew up and was regarded by Dongseok as a father; operated as Ares Guild's senior authority beneath its Guild Master; concealed Taemin's condition with Song Cheonwoo and participated in purging aides who knew the truth.

## Korean source

```text
＃733화



언제부턴가 사흘 밤낮을 버텨도 멀쩡한 몸이 되었다지만, 그래도 충분한 숙면을 취할 수 있다는 건 행복한 일이다.

개운하게 눈을 뜬 그곳이, 소중한 가족들과 함께 머무르는 장소라면 더더욱.

“역시 집이 최고라니까.”

상쾌한 목소리와 함께 자리에 앉은 나를, 커다란 식탁 맞은편의 최 팀장이 떨떠름하게 바라보았다.

“여긴 제집입니다만.”

“지금 그게 중요해요?”

“사소한 건 아니지 않습니까. 명의 문제인데.”

“이거 집 없는 사람은 서러워서 살겠나.”

“누가 들으면 정말 집도 돈도 없는 사람인 줄 알겠습니다.”

그럴 리가 있나.

이제는 내 명의로 된 집도 있고, 돈도 썩어나게 많다.

하지만 계좌에 조 단위의 돈이 잠들어 있다 해도, 나와 가족들이 머무르기에 이보다 더 안전한 장소를 찾기란 결코 쉬운 일이 아니다.

‘아니, 적어도 대한민국에서는 이만한 곳이 없지.’

겉보기에는 그저 거대한 저택이지만, 실상은 수많은 보호 마법으로 겹겹이 둘러싸인 철옹성이나 다름없다.

게다가 대중들에게는 아직까지도 천태민의 저택으로 알려져 있으니, 그 상징성은 청와대 이상이라 해도 과언이 아니었다.

‘사람들의 시선이 있으니 침입하는 것 자체도 불가능에 가깝고, 설령 S급 헌터가 쳐들어와도 충분히 시간을 벌 수 있어.’

어떤 상황에서도 가족들의 안전을 최우선으로 생각하는 내게는 그야말로 최적의 장소다.

물론 뜬금없이 동거하게 된 최 팀장의 입장은 좀 다를 수도 있겠지만.

“생각해 보니까 좀 염치가 없긴 하네. 이번 달부터 월세라도 드려요?”

“주시면 받겠습니다. 인당 천만 원으로 계산해서, 한 달에 사천만 원 정도면 되겠군요.”

나는 햇빛이 쏟아지는 창밖을 바라보며 중얼거렸다.

“아, 날씨 좋다.”

“…….”

“그나저나 뭐가 그렇게 비싸요. 이 와중에 심지어 계산도 틀렸는데?”

“제 계산은 늘 정확합니다.”

“뭔 소리야. 인당 천이면 사천이 아니라 삼천이어야죠. 우리 아버지 돌아가신 게 언젯적 일인데.”

“한 사람 더 있지 않습니까.”

최 팀장의 말이 끝나기가 무섭게, 복도 끝에서 휘적휘적 걸어온 금발의 외국인이 의자에 털썩 주저앉았다.

“밥 줘.”

이 새끼도 양반은 못 되겠구나.

다른 건 둘째치고, 일어나서 얼굴 보자마자 처음으로 하는 말부터가 이미 훌륭한 상놈이다.

“알아서 처먹을래. 아니면 한 대 맞고 처먹을래.”

신중하게 고민하던 스켈레톤 킹이 대답했다.

“알아서 처먹도록 하지.”

“좋은 선택이야. 가는 김에 내 것도 가져오고.”

“……?”

“아, 특히 국은 꼭 챙겨 와. 깜빡하면 죽는다.”

이 저택의 가장 큰 장점 중 하나는 조리실에 설치된 인공 지능이 언제나 따끈따끈한 음식을 준비 중이라는 거다.

잠시 후 스켈레톤 킹은 투덜거리면서도 내 몫의 식사를 챙겨 왔고, 최 팀장은 육개장을 게눈 감추듯 해치우는 내 모습을 빤히 바라봤다.

“진태경 씨는 언제나 잘 드시는군요.”

“사람이 기계도 아니고, 먹어야 살죠.”

“잠은 푹 주무셨습니까?”

“예, 오랜만에. 거의 눕자마자 쓰러졌을걸요?”

최 팀장이 그럴 줄 알았다는 듯 고개를 끄덕였다.

“그래서 전화를 못 받으신 모양입니다.”

“전화요?”

“간밤에 여러 군데에서 연락이 왔었습니다. 혹시 아직도 확인 안 해 보셨습니까?”

“어?”

나는 그제야 스마트폰을 확인했다. 하도 진동이 울리길래 무음으로 바꿔 놨었는데, 어젯밤부터 지금까지 쌓인 부재중 전화와 메시지가 백 통도 넘게 쌓여 있었다.

‘뭐야, 이거.’

대충 광고나 스팸으로 취급하기에는 중간중간 보이는 이름들이 제법 익숙하면서도 화려하다.

아크 리치 진압 과정에서 인연을 맺게 된 영국의 필릭스 왕자. S급 헌터 파이 첸.

현대의 시간으로 불과 2주 전, 함께 테러 단체를 박살 냈었던 미국의 척 헤이글과 이제는 빠지면 섭섭한 이름인 매직 존슨까지.

하지만 여기에서 끝이 아니다.

백한성 대통령은 물론이고, 펜타곤 초청 당시 안면을 텄던 미국의 도람프 주니어 대통령과 샤오 양 중국 주석도 부재중 전화 목록에 한몫을 보탠 상황이었다.

“긴 밤이었습니다. 생각했던 것 이상으로.”

피곤한 표정으로 커피잔을 기울인 최 팀장이 말을 이었다.

“물론 그 덕분에 여러 가지 소식을 전해 들을 수 있었습니다.”

“소식이요?”

“네. 특히 샤오 양 주석이 제법 흥미로운 정보를 전해 주더군요.”

툭툭.

최 팀장이 길쭉한 손가락으로 앞에 놓인 태블릿 PC를 두드리자, 화면 위로 솟구친 홀로그램이 수십여 장의 이미지를 투영했다.

파앗.

“……이건.”

마침내 완성된 이미지를 확인한 나는 미간을 좁히며 수저를 내려놨다.

아무리 비위가 좋고 잔인한 것에 익숙한 나라고 해도, 이런 걸 보면서 식사를 이어 나갈 수는 없다.

“웬 시체들이에요?”

“불과 어젯밤까지만 해도 멀쩡히 살아서 베이징 특별 구치소에 수감 되어 있던 죄수들이었습니다. 그리고 저들 중에는 진태경 씨께서 아는 얼굴도 있고요.”

“제가 아는 사람이라고요?”

슥.

최 팀장이 대답 대신 손을 내저었다. 수십여 장의 이미지가 흩날리듯 사라지고, 유일하게 남은 단 하나의 이미지가 확대된다.

“이제 알아보시겠습니까?”

나는 대답 대신 이미지 파일을 물끄러미 바라보았다.

마치 깊은 잠에 빠진 것처럼 평온하게 쓰러져 있는 중년인의 얼굴은 분명 낯이 익었고, 나보다 먼저 그의 이름을 떠올린 것은 다름 아닌 스켈레톤 킹이었다.

“그 인간이로군. 이름이 아마, 어…… 우 쉐이밍? 뭐 그런 괴상한 이름이었던 것 같은데.”

나와 최 팀장의 시선에 녀석이 자신만만하게 웃었다.

“후후, 이 몸의 정보력을 무시하는군. 나는 게으른 너희와는 달리 잠자는 시간까지 아껴 가며 스마트폰에 몰두했느니라.”

“못 잔 거겠지. 어차피 죽은 몸이니까.”

“…….”

내 일침에 시무룩해진 스켈레톤 킹이 육개장을 깨작거리던 그때, 고개를 끄덕인 최 팀장이 입을 열었다.

“전(前) 중화인민공화국 국무원 총리이자 중앙 정치국 상무위원. 그리고…….”

비로소 우 쉐이밍에 관한 모든 것을 떠올린 내가 말을 받았다.

“이정룡과 합세해서 저를 죽이려고 했던 그놈, 우 헤이싱의 아버지죠.”

“맞습니다. 사실상 중국의 이 인자인 동시에 샤오 양 주석의 가장 큰 정적(政敵)이라 할 수 있는 태자당 일파의 우두머리였던, 바로 그 우 쉐이밍입니다.”

나 역시 모를 수가 없는 사실이다.

아크 리치 진압 이후, 우 쉐이밍이 아들의 죽음에 대한 의혹을 제기하면서 나 역시 그에 대해 자세히 알게 되었으니까.

애초에 우 헤이싱이 온갖 문제를 일으키면서도 무사할 수 있었던 가장 큰 이유 중 하나는, 놈의 친가인 우씨 일가가 중국에서도 손꼽히는 명문가였기 때문이기도 했다.

그런데…….

“우 쉐이밍 저 양반, 지금까지 비리 저지른 거 싹 다 밝혀져서 역풍 맞고 나가떨어지지 않았어요? 마지막으로 뉴스 봤을 때는 재판 기다린다고 했었는데.”

“사실입니다. 샤오 양 주석이 틈을 놓치지 않았고, 우 쉐이밍을 비롯한 태자당 일파 대부분이 수감되었죠.”

“그런데 그런 우 쉐이밍이 갑자기 죽었다?”

“우 쉐이밍은 아직 중년의 나이고 건강을 위해 수십여 년간 포션을 물처럼 마셔 온 사람입니다. 사인은 심장 마비에 의한 급사(急死)지만, 그를 비롯한 일가친척 오십여 명이 한날한시에 같은 방식으로 죽음을 맞이할 수는 없죠.”

“일가친척이라고요? 그럼 아까 본 사진들이…….”

“샤오 주석이 파악한 바에 의하면 모두 우씨 가문의 사람들입니다. 그중에는 아이들도 있었고요.”

“……!”

멸문지화(滅門之禍).

무림에서나 들어 볼 법한 그 네 글자와 함께 등골이 서늘해진다. 동시에 믿기 힘든 어떤 생각이 뇌리를 스쳤다.

“최 팀장님. 그럼 설마…….”

그러나 말을 꺼내기도 전에 최 팀장이 고개를 내저었다.

“샤오 주석의 소행이 아닙니다. 오히려 그는 누구보다 우 쉐이밍을 회유하고 싶었을 겁니다.”

회유. 회유라.

우 쉐이밍은 샤오 양에게 있어 가장 강력한 정적이었던 자.

재기 불능 상태에 빠진 이상 구태여 죽일 필요도 없지만, 그렇다고 살려 둘 이유는 눈곱만큼도 없다.

그렇다면 도대체 무엇을 얻기 위한 회유인가. 우 쉐이밍은 무엇을 갖고 있었나.

이미 폭삭 주저앉은 태자당의 세력? 아니면 압류가 예정된 것이나 다름없는 막대한 재산?

나는 말 없이 회유라는 두 글자를 마음속으로 곱씹었고, 이내 정답을 깨달았다.

“……마나 연공법.”

신음처럼 흘러나온 한마디에 스켈레톤 킹은 눈을 깜빡거렸고, 최 팀장이 가라앉은 목소리로 대답했다.

“네. 샤오 주석은 우 헤이싱을 S급 헌터로 만들어 주었던, 바로 그 마나 연공법을 얻기 위해 그를 회유하고 있었습니다.”

S급 헌터 정도의 강자라면 어느 순간 자연스럽게 고유의 수련법을 스스로 터득하기 마련이다.

하지만 우 헤이싱은 달랐다. 그는 이미 가문으로부터 전해져 내려오는 마나 연공법을 익힌 상태였고, 나는 그의 죽음과 우 쉐이밍의 몰락 이후 그 사실에 더는 큰 관심을 두지 않았다.

‘그런데 어젯밤, 우 쉐이밍을 비롯한 일가친척 모두가 갑작스럽게 죽었다는 건.’

샤오 양이 마나 연공법을 얻어 무엇을 하려 했는지는 관심 없다.

중요한 것은 우씨 가문의 멸문지화로 회유가 수포로 돌아갔다는 것과, 누가 이런 짓을 벌였느냐다.

그리고 나는…… 이미 그 의문에 대한 답을 알고 있다.

“오딘 길드군요.”

남의 것처럼 낯선, 메마른 목소리가 입술 사이로 흘러나온다. 최 팀장이 차갑게 식은 커피잔을 매만졌다.

“아마도 그럴 확률이 높습니다.”

“…….”

“샤오 양 주석이 말한 바에 의하면, 별다른 선택지가 없던 우 쉐이밍은 회유에 응할 생각이 있던 모양입니다. 마나 연공법을 넘기지 않으면 적어도 종신형, 혹은 사형을 당해도 이상하지 않을 상황이었으니까요. 하지만…….”

문득 말꼬리를 흐린 최 팀장이 입술을 깨물었다.

“다른 누군가는 그것을 원치 않았을 겁니다.”

전신의 피가 차갑게 식는 기분이다.

놈들이 움직였다. 생각했던 것보다도 훨씬 빠르고, 잔인한 방법으로.

‘아무리 그래도 멸문지화라니.’

나는 아직 꺼지지 않은 홀로그램을 바라보았다. 여자, 아이, 노인. 그들 모두가 깨어나지 않을 깊은 잠에 빠져 있었다.

단지 우씨 가문에서 태어났다는 사실 하나만으로.

‘이렇게라도 마나 연공법의 유출을 막겠다는 건가, 아니면…….’

어젯밤 일에 대한 답신인가.

여러 생각이 혀끝에서 맴돌다 흩어진다. 말없이 죽은 이들의 얼굴을 바라보던 나는, 문득 입을 열었다.

“최 팀장님.”

“네, 말씀하십시오.”

“시간 되시면 같이 커피나 한잔하러 가실래요?”

“저야 괜찮습니다만. 갑자기 어디로…….”

“글쎄요. 거기가 아마 파리였나?”

“네?”

의아한 얼굴로 되묻는 최 팀장을 향해, 나는 담담하게 말을 이었다.

“오딘 길드요. 거기 주인장 면상이나 한 번 보러 가고 싶네?”

“……!”
```

## Final English reading copy

```markdown
# Chapter 733

At some point, my body had become sturdy enough to stay perfectly fine even after going three days and nights without rest. Even so, being able to get a full night’s sleep was a wonderful thing.

Especially when I woke up refreshed in a place where I was staying with my precious family.

“Home really is the best.”

Sounding refreshed, I took my seat, and Team Leader Choi looked at me sourly from across the enormous dining table.

“This is my home, technically.”

“Is that what matters right now?”

“It is not a trivial matter. We are discussing legal ownership.”

“I’m starting to wonder if homeless people can even bear to live.”

“Anyone listening to you would think you truly had neither a home nor money.”

As if.

I had a house under my own name now, and more money than I knew what to do with.

But even if trillions of won were sleeping in my bank account, finding a safer place for my family and me to stay would be nearly impossible.

*No. At least not anywhere in Korea.*

From the outside, it looked like nothing more than an enormous mansion. In reality, it was an impregnable fortress wrapped in layer upon layer of protective Magic.

And since the public still knew it as Cheon Taemin’s mansion, it would not be an exaggeration to say that it carried more symbolic weight than even the Blue House.

*With everyone watching, breaking in is practically impossible. Even if an S-rank Hunter attacked, we could buy more than enough time.*

For someone like me, who put my family’s safety above all else in every situation, it was the perfect place.

Of course, Team Leader Choi’s perspective might have been a little different, considering he had suddenly ended up living with us.

“Now that I think about it, I am taking advantage of you a bit. Should I start paying rent this month?”

“I will accept it if you offer. At ten million won per person, forty million won a month should be about right.”

I gazed out the window at the sunlight pouring down and muttered:

“Ah, the weather’s nice.”

“……”

“By the way, why is it so expensive? You even got the calculation wrong.”

“My calculations are always accurate.”

“What are you talking about? Ten million per person means thirty million, not forty. My father died ages ago.”

“There is one more person.”

No sooner had Team Leader Choi finished speaking than a blond foreigner came shambling down the hall and dropped heavily into a chair.

“Give me food.”

Speak of the fucking devil.

Putting everything else aside, the very first thing he said after getting up and seeing our faces made it clear he was a first-rate lout.

“You gonna get your own damn food, or eat after I smack you?”

After considering the question carefully, the Skeleton King answered:

“I shall get my own food.”

“Good choice. While you’re at it, bring mine, too.”

“……?”

“Oh, and make sure you bring the soup. If you forget, you’ll die.”

One of the mansion’s greatest advantages was that the artificial intelligence installed in the kitchen was always preparing hot food.

A short while later, the Skeleton King returned with my meal despite grumbling the whole way, and Team Leader Choi stared intently as I devoured the yukgaejang.[^1]

“Mr. Jin Taekyung, you always eat well.”

“People aren’t machines. You have to eat to live.”

“Did you sleep well?”

“Yes. It’s been a while. I probably collapsed almost the moment I lay down.”

Team Leader Choi nodded as if he had expected that answer.

“So that is why you could not answer your phone.”

“My phone?”

“You received calls from several places during the night. Have you still not checked?”

“Huh?”

Only then did I check my smartphone. It had vibrated so much that I had switched it to silent, but there were now more than a hundred missed calls and messages that had piled up since last night.

*What the hell is this?*

The names appearing among them were far too familiar and illustrious to dismiss as advertisements or spam.

Prince Felix of the United Kingdom, whom I had met during the operation to suppress the Arch-Lich. Faye Chen, an S-rank Hunter.

Chuck Hagel of the United States, with whom I had destroyed a terrorist organization only two weeks ago by modern reckoning, and Magic Johnson, a name that had become impossible to leave out.

But it did not end there.

President Baek Hanseong was on the list, of course. So were President Doramp Jr. of the United States, whom I had met during my visit to the Pentagon, and Chairman Xiao Yang of China.

“It was a long night. Longer than I expected.”

Team Leader Choi tilted his coffee cup with a tired expression before continuing.

“Of course, that also allowed me to hear several pieces of news.”

“News?”

“Yes. Chairman Xiao Yang, in particular, gave me some rather interesting information.”

Tap, tap.

Team Leader Choi tapped the tablet PC in front of him with one long finger. A hologram rose above the screen and projected dozens of images.

Flash.

“……What is this?”

When the images finally finished loading, I narrowed my eyes and put down my spoon.

No matter how strong my stomach was or how accustomed I was to gruesome sights, I couldn’t keep eating while looking at something like this.

“Why are there so many corpses?”

“They were prisoners who were alive and well and incarcerated at Beijing Special Detention Center as recently as last night. And among them are some faces you know, Mr. Jin Taekyung.”

“People I know?”

Swish.

Instead of answering, Team Leader Choi waved his hand. The dozens of images scattered and vanished, leaving only one behind. That image expanded.

“Do you recognize him now?”

I stared silently at the image.

The face of the middle-aged man lying peacefully, as though he had fallen into a deep sleep, was unmistakably familiar. But the first person to recall his name was not me. It was the Skeleton King.

“That man. His name was, uh…… Wu Shaiming? Something like that. An odd name, in any case.”

The Skeleton King smiled confidently under the gaze of Team Leader Choi and me.

“Ha-ha. You underestimate the information-gathering abilities of this body. Unlike lazy creatures such as yourselves, I devoted myself to my smartphone even at the expense of my sleeping hours.”

“You just couldn’t sleep. You’re dead, after all.”

“……”

The Skeleton King grew dejected and began picking at his yukgaejang. Team Leader Choi nodded before speaking.

“Former Premier of the State Council of the People’s Republic of China and member of the Standing Committee of the Politburo. And……”

I finally remembered everything about Wu Shaiming and cut in.

“He was Wu Heixing’s father—the man who joined forces with Lee Jungryong and tried to kill me.”

“Correct. Wu Shaiming was China’s de facto second-in-command and the leader of the Crown Prince Party, the faction whose head was Chairman Xiao Yang’s greatest political rival.”

There was no way I wouldn’t know that.

After the operation to suppress the Arch-Lich, Wu Shaiming had raised suspicions about his son’s death, which had led me to learn more about him.

One of the main reasons Wu Heixing had been able to cause all kinds of trouble and still escape unscathed was that his father’s family, the Wu clan, was one of China’s most prestigious families.

But then……

“Didn’t that old man Wu Shaiming get knocked out after all the corruption he’d committed came to light? The last time I saw the news, he was waiting for trial.”

“That is correct. Chairman Xiao Yang did not miss the opportunity, and most of the Crown Prince Party—including Wu Shaiming—was imprisoned.”

“But Wu Shaiming suddenly died?”

“Wu Shaiming was still middle-aged, and he had spent decades drinking potions like water for the sake of his health. His cause of death was sudden cardiac arrest, but there is no way he and some fifty of his relatives could all die the same way at the exact same time.”

“His relatives? Then the pictures I saw earlier……”

“According to Chairman Xiao Yang’s information, they were all members of the Wu family. There were children among them, too.”

“……!”

*The annihilation of an entire household.*[^2]

The words, the sort of phrase one might only hear in Murim, sent a chill down my spine. At the same time, an unbelievable thought flashed through my mind.

“Team Leader Choi. Could it be that……”

But before I could finish, Team Leader Choi shook his head.

“It was not Chairman Xiao Yang’s doing. If anything, he must have wanted to persuade Wu Shaiming more than anyone.”

Persuade him.

Wu Shaiming had been Xiao Yang’s most powerful political rival.

Now that he had been rendered incapable of making a comeback, there was no particular reason to kill him—but there was not the slightest reason to keep him alive, either.

So what exactly had Xiao Yang wanted to gain by persuading him? What had Wu Shaiming possessed?

The Crown Prince Party’s influence, which had already collapsed? Or the enormous fortune that was practically destined to be seized?

I silently rolled the word *persuade* around in my mind. Before long, I realized the answer.

“……The Mana Cultivation Method.”

At the single word that escaped like a groan, the Skeleton King blinked, and Team Leader Choi answered in a low voice.

“Yes. Chairman Xiao Yang was trying to win Wu Shaiming over in order to obtain the very Mana Cultivation Method that had turned Wu Heixing into an S-rank Hunter.”

An S-rank Hunter with that level of power would naturally discover a unique training method of his own at some point.

But Wu Heixing had been different. He had already learned a Mana Cultivation Method passed down through his family, and after his death and Wu Shaiming’s downfall, I had stopped paying much attention to the matter.

*But the fact that Wu Shaiming and all his relatives suddenly died last night means……*

I had no interest in what Xiao Yang intended to do with the Mana Cultivation Method.

What mattered was that the annihilation of the Wu family had caused his attempt at persuasion to fail—and who had committed such an atrocity.

And I already knew the answer to that question.

“It must have been Odin Guild.”

A dry voice, unfamiliar even to me, slipped between my lips. Team Leader Choi ran his fingers over his coffee cup, which had gone cold.

“That is the most likely possibility.”

“……”

“According to Chairman Xiao Yang, Wu Shaiming had been prepared to accept the offer because he had no other choice. If he refused to hand over the Mana Cultivation Method, it would have been perfectly possible for him to receive at least a life sentence, or even the death penalty. But……”

Team Leader Choi suddenly let his words trail off and bit his lip.

“Someone else would not have wanted that.”

It felt as though the blood throughout my body had frozen.

*They had made their move.*

Much faster than I had expected, and in a far more brutal way.

*But even so, to wipe out an entire household……*

I stared at the hologram that had yet to disappear. Women, children, and old people. Every one of them had fallen into a deep sleep from which they would never wake.

Simply because they had been born into the Wu family.

*Were they willing to go this far to prevent the Mana Cultivation Method from leaking, or……*

*Was this a reply to what happened last night?*

Several thoughts lingered on the tip of my tongue before scattering. As I silently gazed at the faces of the dead, I suddenly spoke.

“Team Leader Choi.”

“Yes. Please, go ahead.”

“If you have time, would you like to go out for a cup of coffee with me?”

“I have no objection. But where are we suddenly going……”

“I wonder. Was it Paris?”

“What?”

As Team Leader Choi looked at me in confusion, I continued calmly.

“Odin Guild. I feel like going to see the boss’s ugly mug.”

“……!”

[^1]: Yukgaejang is a spicy Korean soup made with shredded beef, vegetables, and red pepper seasoning.

[^2]: A classical expression for the complete destruction of a family and its relatives, often including children.
```
