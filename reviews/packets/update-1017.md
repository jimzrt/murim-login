<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1017.txt",
      "sha256": "b97c28e3e1f12b2b9da55fafd5ec995e53353f8d3274d3f46f2abafd6e4662d8",
      "bytes": 13181
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "603a447d9a082ddc1914928b6837ab7cb4686349f09222fc01580a804618bf7b",
      "bytes": 1472
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "611b5144e394205d82ab664a36e903511377554b9737ac63e0571a7866e56564",
      "bytes": 238256
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "28094c33a794961e0db95e7ba9f6bca638ec970e686bfc4d74a3543c98bb083b",
      "bytes": 1408
    },
    {
      "path": "characters/Ma Junggeol.md",
      "sha256": "da390377bf02b853d58fc0ee93f8eb427c90d3668e5c0de651e767c64a40f2fd",
      "bytes": 673
    },
    {
      "path": "characters/Namho.md",
      "sha256": "0fbcbb56a0a410741bd0073c9630346803ccd88a197dc62d64f2ec9fdb1f3f53",
      "bytes": 1092
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "9357cdc998c65cfe7091b990556cbe883e4da39bdfc6d9efbf32f6a063bb3f89",
      "bytes": 904
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "94825422f6de94b8c557e5fcb34565e95b7cfdf18b3153ab8c087997ee0fc2dc",
      "bytes": 778
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "706c907345fbaa91b6a9ff884731cb31d30e2e19a69c34d1b41132549cb093d5",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e9febd618486b99b8ff4e9220ac86edf486c2abc2fc0dc1a17734b20ec6f79fd",
      "bytes": 276986
    }
  ],
  "estimated_tokens": 11114
}
-->

# Durable State Update — Chapter 1017

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 1017. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1017. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
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
  "chapter": 1017,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1017,
    "continuity_sources": [1017],
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
    "Taekyung’s allied force has reached the Qilian Mountains, where Gansu’s troops are spread across three fronts.",
    "Sima Gong’s strategy knowingly risks the rear population being devastated if Dark Heaven uses the Moving Formation to bypass the front; he expects Dark Heaven to be trapped behind the lines.",
    "Wolhwa’s affectionate missive to Taekyung could be misunderstood by Ju Hwaran.",
    "Namho has an important matter he says he can only disclose to Taekyung now.",
    "Six Baekma Bang men left to fetch the Lord within five days of the march’s halt; Ma Junggeol remains with Taekyung’s group.",
    "Sama Pyo disobeyed Sima Gong’s order to return to Gansu; consequences are unknown.",
    "Sima Gong ordered two martial artists dealt with for making a taboo remark about Sama Pyo’s succession."
  ],
  "continuity_sources": [
    1015,
    1016
  ],
  "open_questions": [
    "Who is the Lord, and what are his motives and connection, if any, to Dark Heaven?",
    "Will the six Baekma Bang men return with the Lord within Taekyung’s deadline?",
    "What does Namho need to tell Taekyung, and why can he only tell him now?",
    "What is Dark Heaven’s full strength and objective, and will it use the Moving Formation to attack the rear?",
    "What consequences, if any, will Sama Pyo face for disobeying Sima Gong’s order?"
  ],
  "safe_through": 1016,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 사마공    | **Sima Gong**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 태원진가   | **Jin Family of Taiyuan**        |
| 종남파    | **Zhongnan Sect**                |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 사파     | **unorthodox faction**                           |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 선배     | **Senior**                                   |
| 태원     | **Taiyuan**            |
| 감숙     | **Gansu**              |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 본문      | **our sect / this sect**                                        |
| 대사      | **Master** for a senior Buddhist monk                           |
| 마중걸 | **Ma Junggeol** |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 장유 | **Jangyu** | Martial artist eliminated during the fist-and-foot assessment. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 마방 | **horse caravans** | Descendants of northern mounted tribes who traveled ancient trade routes between the Outer Lands and the Central Plains. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 적천강 | junior_to_senior | Senior | respectful and formal | Namho refers to Jeok as 노선배님 while agreeing with him. |
| 적천강 | 풍운검군 | legendary_elder_to_Zhongnan_sect_leader | Wind-and-Cloud Sword Lord | familiar and commanding | Jeok Cheongang tells him to get the Zhongnan disciples moving. |
| 노호검객 | 적천강 | senior_martial_artist_to_legendary_elder | Senior Jeok | deferential and cautious | Addresses Jeok as 노 선배 while explaining his actions. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |
| 마중걸 | 적천강 | visiting horse-caravan chief to legendary martial master | Great Hero Jeok Cheongang | polite and deferential | Recognizes Jeok as the Fire King. |
| 풍운검군 | 적천강 | Zhongnan Sect Leader to legendary martial master | Senior Jeok | respectful | Refers to Jeok as 적 대협. |
| 마중걸 | 사마공 | visiting group leader to sect leader | Sect Leader Sima | polite and respectful | Addresses him as 사마 문주 while explaining Ningxia and Baekma Bang. |
| 사마공 | 마중걸 | sect leader to visiting group leader | you | formal and probing | Uses 자네 while questioning Ma Junggeol about following Dark Heaven. |
| 사마공 | 사마표 | father to son | Pyo | intimate and familiar | Sima Gong calls him 표야 and 내 아들아. |

## Listed compact profiles

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1016
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Ma Junggeol.md

# Ma Junggeol (마중걸)

- **Safe through:** Chapter 1013
- **Aliases:** Chief of Baekma Bang
- **Role:** Ma Junggeol is the chief of Baekma Bang, a horse-caravan group founded by reformed Ningxia mounted-bandit leaders.
- **Personality:** Though timid by nature, he is earnest and protective of his sworn brothers, loyal to the benefactor who helped them reform, and willing to bear personal risk for their mission.
- **Voice:** Not established
- **Relationships:** He leads six sworn brothers who, with him, are known as the Seven Masters of Baekma Bang, and trusts the benefactor they call the Lord.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 1015
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he guides the Fire Dragon Pavilion and represents Jin Taekyung and the Murim Alliance in negotiating the survivors’ chance to rebuild the Murong household.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1016
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1016
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet outwardly gentle; he calmly accepts sacrificing the rear population as the cost of a strategy he believes offers the best odds of victory.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1015
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1017화



사마공과 감숙 무림의 영수들이 주장하는 바는 실로 간단명료했다.

- 남의 구역에서 감 내놔라, 배 내놔라 하지 마라.

솔직히 말하자면, 딱히 반박의 여지가 없는 주장이다.

저들 한 사람, 한 사람이 짧게는 수십 년에서 길게는 백 년 이상 감숙 무림을 지배해 온 터줏대감들이고, 정마대전 이후 타 문파에 대한 과한 간섭은 금기시되어 있으니까.

더군다나 그 중심에 선 흑룡마문(黑龍魔門)이 어떤 곳인가.

수십여 년 정도의 비교적 짧은 역사를 가졌음에도 감숙 일대에 엄청난 영향력을 행사하고 있는, 명실상부한 사파 무림의 기둥이다.

최소한 감숙성에 한해서만큼은 구파일방의 일익인 공동파와도 어깨를 나란히 하는, 아니 어쩌면 현재로서는 그보다도 더 강력한 세력을 구축한 패자(霸者).

그런 흑룡마문의 시작이자 끝이라 할 수 있는 사마공이 이토록 거침없이 발언하니, 잠시 격한 감정을 내비치던 풍운검군조차 한 걸음 물러날 수밖에 없었다.

물론, 또 눈썹 하나 까딱하지 않은 채 이 모든 광경을 지켜보던 누군가는 아니었지만.

“뭘 그리 으르렁대느냐. 밥그릇 빼앗긴 누렁이도 아니고.”

천하의 흑야왕을 누렁이에 빗댈 수 있는 사람은 이 자리에 단 한 명밖에 없다.

화왕(火王) 적천강.

아득한 무림사에 자신만의 족적을 새긴 거인이 마침내 입술을 떼자, 시린 빛을 뿜어내던 사마공의 안광이 착 가라앉았다.

“마땅히 그래야지요. 밥그릇을 지킬 수 있다면야 얼마든지.”

“그 밥그릇이, 누군가의 목숨줄이라는 생각은 안 해 봤고?”

“대의(大意)를 위해서입니다.”

“사의(私意)겠지. 네놈과 흑룡마문을 따르는 소수에게만 보장된.”

적천강이 천천히 좌중을 훑었다.

종남파와 흑룡마문을 제외한 그들의 숫자는 스물 남짓.

그런 감숙 무림의 영수들을 차례대로 응시하는 적천강의 입가에는 명백한 조소가 맺혀 있었다.

“그러고 보면 참 희한하지 않느냐. 노부가 알기로 감숙성에는 최소 오십여 개에 달하는 문파와 무가(武家)가 있는데, 지금 이 자리에는 그중 절반도 자리하고 있지 않으니…… 아, 이미 다른 전선에 배치됐나?”

사마공이 건조한 목소리로 대꾸했다.

“그들은 이미 다른 임무를 수행 중입니다.”

“뒤에 남았다는 뜻이군. 암천이 이동진을 이용해서 후방에 나타났을 시, 고작 한나절이라도 시간을 지체시킬 목적으로.”

“이미 모두가 동의한 사안입니다.”

“네놈이 말하는 그 동의를 받기에 앞서, 모든 사실을 털어놓기는 했고? 아니, 혹시 그전에 칼부터 들이민 것은 아니더냐?”

“외람되지만, 이참에 한 말씀 드리지요.”

“외람된 말이라고 하니 벌써부터 기분이 엿 같아지지만, 그러라고 뚫린 입이니 어디 한번 지껄여 보거라.”

계속해서 쏟아지는 적천강의 독설에 짧게 숨을 내뱉은 사마공이, 이내 담담한 표정으로 입을 열었다.

“저희 감숙 무림은 이번 결정에 있어 어떤 식으로든 외인(外人)의 간섭을 받아들이지 않습니다. 설령 그것이 구파일방과 오대세가. 혹은…….”

풍운검군과 나를 스치듯이 지나친 사마공의 시선이, 마침내 다시 적천강에 이르러 우뚝 멈췄다.

“노 선배라 할지라도 말입니다.”

“……!”

“……!”

순간, 주위를 둘러싼 공기가 크게 요동쳤다.

뻣뻣하게 굳어 버린 손발은 기본이고, 작게 일렁이는 목울대는 옵션이다.

제아무리 사마공이라지만, 상대가 누구인가.

바로 그 화왕 적천강이다.

무공으로는 중원에서 다섯 손가락 안에 들고, 성질 더럽기로는 첫손가락에 꼽는다는 무시무시한 노괴(老怪).

그런 적천강에게 도전적이기까지 한 어투로 대답했으니, 모두가 불에 덴 것처럼 반응하는 것은 당연했다.

단 한 사람, 나만 빼고.

‘오늘은, 딱 이 정도까지.’

줄곧 흘러가는 상황을 주시하던 나는 마음의 결정을 내렸다.

그리고 돌연, 아무도 예상하지 못한 그 시점에 양 손바닥을 힘차게 부딪쳤다.

짝!

갑작스럽게 울려 퍼진 손뼉 소리에 짧지만 길었던 침묵이 깨져 나간다. 막 꿈에서 깬 것처럼 화들짝 놀라며 고개를 돌린 사람들을 향해, 나는 천연덕스럽게 눈을 깜빡거렸다.

“아, 죄송합니다. 갑자기 웬 모기 새끼가 얼쩡거리길래.”

물론 거짓말이다.

만년설(萬年雪)이 끼어 있는 마당에 모기는 무슨 얼어 죽을.

하지만 중요한 점은 조금 전의 돌발 행동으로 인해 끝없이 나락을 향해 치닫던 분위기가 순식간에 해소되었다는 것이다.

그리고 그 중심에 서 있던 두 사람은, 내 손뼉에 담긴 의미를 즉각 알아차렸다.

“제법 머리가 굵어졌구먼. 많이 컸어.”

마침내 적천강의 입술 사이로 흘러나온 나지막한 음성에, 사마공이 언제 그랬냐는 듯이 공손히 포권지례를 올렸다.

“아직 갈 길이 멉니다. 부족한 후배를 조금이나마 어여삐 봐주시길.”

뭔가 마음에 들지 않는 듯, 나를 보며 짐짓 눈살을 찌푸린 적천강이 입을 열었다.

“갈 길이 멀긴 하지. 앞으로의 일만 생각해도 첩첩산중이니. 그렇지 않으냐?”

“저희야 노선배께서 함께 계시니, 천군만마가 대수겠습니까.”

함께, 라는 두 글자에 유독 힘을 실어 대답한 사마공이 문득 고개를 들고 나를 응시했다.

“참으로 영민한 제자를 두셨습니다.”

“영민한지는 모르겠고, 눈치 하나는 빠르지.”

“뛰어난 신위에 깊은 심계까지 지녔으니, 천하 무림의 홍복(洪福)이지요. 제 아들놈이 그간 옆에서 많이 보고 배웠어야 할 터인데…… 자네가 보기에는 어떻던가?”

불현듯 던져진 사마공의 물음에, 나는 망설임 없이 대꾸했다.

“쓸 만하던데요.”

“뭐?”

“겪어 보니까 애가 나름대로 괜찮습니다. 좀 어두컴컴한 거 빼면.”

무림에서의 나이로 따지면 나보다 한참 앞서는 사마표다.

하지만 장유유서(長幼有序) 따위는 개나 줘 버린 내 대답에도, 사마공은 뜻 모를 웃음만 입가에 띄울 뿐이었다.

“좋게 말해 줘서 고맙군. 공들여 키운 보람이 있어.”

그런 그의 어깨너머, 무표정하게 서 있는 사마표의 모습을 보던 나는 문득 생각했다.

공들여 키웠다는 저 표현이 한 사람의 아버지로서 자식을 키운 것이 아니라, 마치 어느 장인(匠人)이 작품을 대하는 것 같다고.

그러나 그 짧은 생각은 떠오른 것만큼이나 금세 사라졌고, 나는 재차 입을 열었다.

“그래서, 현재의 판단을 바꾸실 생각은 없으신 겁니까?”

“결정(決定). 행동이나 태도를 결단하여 정했다는 뜻이지.”

“없으시다는 거군요. 그럼 공동파의 의사 역시 마찬가지라고 생각해도 되겠습니까?”

“공동파는 반대했지만, 그렇다 한들 달라지는 것은 아무것도 없네. 이건 감숙 무림 전체가 깊은 논의 끝에 결정한 사안이니까.”

글쎄. 과연 그것이 감숙 무림의 뜻일까.

아니면…….

‘오직 흑룡마문의 뜻일까.’

혀끝에서 맴도는 말을 삼킨 나는 잠시 고민했다.

인벤토리.

깊이를 알 수 없는 그 컴컴한 아공간(亞空間) 어딘가에 넣어두었던 한 가지 물건을 마음속으로 만지작거리며.

하지만 이내 고개를 저었다.

아무리 생각해도, 아직은 적기(適期)가 아니다.

적어도 지금은.

“그럼, 그렇게 하시죠.”

“뭐라?”

어딘가에서 불현듯 튀어나온 반문은 눈살을 찌푸리고 있던 적천강도, 사마공의 것도 아니었다.

풍운검군.

종남파의 장문인인 그가 크게 뜬 눈으로 나를 바라보고 있었다.

“이대로 받아들이겠다니, 진심인가?”

바로 그때였다.

내가 뭐라 대답하기도 전, 또 다른 두 줄기의 목소리가 풍운검군을 가로막은 것은.

“어디에 가나 그들만의 규율이 있는 법이지. 우리 종남이 그렇듯이.”

“대사형의 말씀이 옳네. 장문 사제. 본문의 장문인으로서 어떤 언행을 보여야 하는지 다시 한번 명심하게.”

노호검객과 태을무정검.

바로 그들이다.

그리고 차례대로 입을 연 두 사형의 모습에, 풍운검군은 신음하듯 뇌까렸다.

“사형들. 그래도 어찌 이런.”

“장문인께서 어떤 마음이신지는 충분히 짐작하오만, 더 이상의 분란은 대사(大事)를 그르칠 수 있다는 사실을 말씀드리고 싶구려.”

침착하지만 단호한 음성으로 풍운검군의 뒷말을 끊어 낸 사마공이 좌중을 쓸어보며 말을 이었다.

“모두들 기억해주셨으면 하오. 우리는 무림맹의 깃발 아래에 하나가 된 아군이고, 이미 내려진 결정에 관한 분란은 없어야 한다는 것을. 하물며…….”

깊게 가라앉은 사마공의 시선이, 문득 내게 이르러 멈춰섰다.

“모두의 동의를 구하지 않은 독단적인 판단이라면, 더더욱 있어서는 안 되겠지. 그렇지 않나?”

사마공이 무엇을 말하는지 이미 알고 있던 나는 고개를 끄덕였다.

“기억해 두겠습니다.”

“그 마방들을 돌려보낸 것이 아군에게 있어 뼈아픈 실책이 아니었으면 좋겠군.”

“아무런 문제도 없을 겁니다. 적어도 제가 예상하는 바가 맞다면.”

“마중걸이라고 했나? 만약 그자마저 풀어주었다면……우리는 자네에게 실망했을 걸세. 아주 많이.”

순간 착 가라앉은 그의 음성에 적천강이 눈썹을 꿈틀거렸지만, 보이지 않는 곳에서 슬쩍 소매를 잡아당긴 나는 어깨를 으쓱해 보였다.

“명심하죠.”

그 후, 회의는 불과 일각도 더 이어지지 않고 마무리되었다.

감숙 무림의 영수들은 자리를 빠져나가면서도 불안한 눈빛으로 적천강을 힐끗거렸지만, 그는 악성 변비에 걸린 것 같은 표정으로 침묵을 지켰다.

그리고 마침내 주위의 이목을 벗어나, 나와 단둘이 남게 된 후에야 비로소 입을 열었다.

“무슨 속셈이냐?”

“뭐가요?”

“말 돌리지 말거라. 염두에 둔 생각이 있으니 그토록 노부를 뜯어말렸을 터.”

“뜯어말리진 않았는데요. 그냥 진정하시라고 눈짓만 좀 한 것뿐이지.”

“뭐라?”

“그럼 뭐, 그 자리에서 멱살 잡고 줘 패실 생각이셨습니까? 그것도 흑룡마문의 문주를?”

“왜, 노부가 못 할 것 같으냐?”

“…….”

그건 그러네.

잠시 말문이 막힌 나는 한숨을 푹 내쉰 뒤, 잠시 멈췄던 걸음을 옮겼다.

“찝찝한 부분이 있어서 그랬습니다.”

“그거야 사마공. 저놈 면상만 봐도 느껴지는 것 아니더냐.”

“그게 아닙니다. 뭔가를 숨기고 있어요.”

내 나직한 목소리에, 적천강의 얼굴이 덩달아 굳었다.

“그게 무슨…… 잠깐, 설마?”

끝에 이르러 점차 커져 가는 목소리에, 나는 작게 고개를 내저었다.

“괜한 억측은 자제하세요. 아직 확실치 않으니.”

“더 자세히. 하나도 빠짐없이 말하거라.”

“하루 전, 남 노인이 갑자기 찾아와서 할 얘기가 있다고 했던 거 기억하세요?”

“물론이다. 갑자기 소피가 급해서 듣지 못했지만.”

적천강이 미간을 좁히며 말을 이었다.

“그토록 중요한 일이었다면 나중에라도 네 녀석이 말해 주었을 터인데, 왜 하루가 넘게 아무런 언급도 하지 않았던 것이냐?”

그의 말이 맞다.

나는 늘 대부분의 중대사를 적천강과 의논해 왔고, 그 안에서 답을 찾기도 했다.

하지만…….

‘예외도 있기 마련이지.’

그날, 그 순간이 그랬다.



‘중요한 이야기일세. 지금이 아니라면 할 수 없는.’



불현듯 내게 다가온 남호는, 한껏 숨죽인 목소리로 예상치 못했던 이야기를 들려 주었다.



‘태원진가에서 출발하기 직전, 사마표가 보이지 않아 찾아갔었네. 태산이 그놈과 함께.’



그리고 그곳에서, 은영각의 늙은 요원은 익숙하면서도 낯선 냄새를 맡았다.



‘아무런 흔적도 없었지만, 분명 사마표는 전서(傳書)를 태우고 있었네.’



아니, 사마표가 그 사실을 숨기고자 했을 때부터, 그것은 단순한 전서가 아니었다.

밀서(密書)였다.
```

## Final English reading copy

```markdown
# Chapter 1017

Sima Gong and the leaders of Gansu Murim had made their position perfectly clear:

- Don’t go demanding this and that in someone else’s territory.

Honestly, there wasn’t much room to argue with that.

Every one of them was an old fixture who’d ruled Gansu Murim for decades at the very least, and some for more than a century. Besides, ever since the Great Faction War, interfering too much in another sect’s affairs had been taboo.

And then there was the Black Dragon Demon Gate, standing at the center of it all. What kind of place was it?

Despite its relatively short history of only a few decades, it wielded tremendous influence throughout Gansu. It was, without question, a pillar of the unorthodox faction.

At least in Gansu, it stood shoulder to shoulder with the Kongtong Sect, one of the Nine Sects and One Gang. In fact, it might have built an even stronger power base by now—a true regional overlord.

With Sima Gong, the beginning and end of the Black Dragon Demon Gate, speaking so frankly, even the Wind-and-Cloud Sword Lord had no choice but to back down after briefly letting his anger show.

But not the one who had watched it all without so much as twitching an eyebrow.

“Why are you growling so much? You sound like a yellow dog whose food bowl’s been taken away.”

There was only one person here who could compare the Black Night King himself to a yellow dog.

The Fire King, Jeok Cheongang.

At last, the giant who’d left his mark on the distant history of Murim parted his lips. The icy gleam in Sima Gong’s eyes settled.

“I suppose I should. If I can protect my food bowl, I’ll do whatever it takes.”

“And it never crossed your mind that someone else’s life might depend on that food bowl?”

“It’s for the greater good.”

“You mean your own good. The good of a select few who follow you and the Black Dragon Demon Gate.”

Jeok Cheongang slowly looked around the room.

There were around twenty people here, not counting the Zhongnan Sect and the Black Dragon Demon Gate.

As Jeok Cheongang looked from one leader of Gansu Murim to the next, an unmistakable sneer curled his lips.

“Come to think of it, isn’t it strange? As I understand it, Gansu has at least fifty sects and martial families, yet not even half of them are here. Ah… were the others already sent to the other fronts?”

“They’re already carrying out other assignments,” Sima Gong answered in a dry voice.

“So they were left behind. To delay Dark Heaven for even half a day if it uses the Moving Formation to appear in the rear.”

“Everyone agreed to it.”

“And before you got that agreement, did you lay out all the facts? Or did you go straight to drawing your sword?”

“With all due respect, there’s something I’d like to say while we’re at it.”

“‘With all due respect’ already puts me in a shitty mood, but I suppose that’s what you’ve got a mouth for. Go on, then. Spit it out.”

At Jeok Cheongang’s continued string of barbs, Sima Gong let out a short breath. Then, with a calm expression, he began.

“We of Gansu Murim will not accept interference from outsiders in this decision, in any form. Even if that interference comes from one of the Nine Sects and One Gang or the Five Great Families. Or…”

Sima Gong’s gaze swept past the Wind-and-Cloud Sword Lord and me, then finally came to a dead stop on Jeok Cheongang.

“Even if it comes from you, Senior.”

“……!”

“……!”

The air around us lurched.

Stiffened hands and feet came standard. The slight bobbing of people’s throats was an added bonus.

Even if it was Sima Gong, who was he speaking to?

Jeok Cheongang, the Fire King himself.

A terrifying old monster who ranked among the top five in the Central Plains in martial arts—and was said to be number one when it came to having a foul temper.

He’d answered Jeok Cheongang in a tone that was downright challenging. No wonder everyone reacted as if they’d been burned.

Everyone except me.

*This is far enough for today.*

I’d been watching events unfold the whole time, and I made up my mind.

Then, at a moment nobody could have expected, I suddenly clapped my hands together with all my strength.

*Clap!*

The sharp sound broke the silence, short and yet seemingly endless. Everyone turned toward me, startled as if they’d just woken from a dream. I blinked at them with perfect composure.

“Oh, sorry. A damn mosquito was buzzing around.”

Of course, I was lying.

With perennial snow on the ground, what damn mosquito?

But the point was that my sudden outburst had instantly relieved the tension, which had been plunging toward the abyss.

And the two men at the center of it understood the meaning behind my clap at once.

“You’ve grown some brains, I see. You’ve come a long way.”

At last, Jeok Cheongang’s low voice slipped from between his lips. Sima Gong, as if nothing had happened, respectfully clasped his hands in salute.

“I still have a long way to go. I hope you’ll look kindly on this inadequate junior.”

Jeok Cheongang looked at me, put on a frown, and spoke.

“You certainly do have a long way to go. The road ahead is full of trouble, after all. Isn’t it?”

“With you here beside us, who needs an army?”

Sima Gong put particular emphasis on the word *beside*, then suddenly lifted his head and looked at me.

“You truly have an exceptionally perceptive Disciple.”

“I don’t know about perceptive. He’s got a good sense for reading a room.”

“Remarkable martial prowess, and a mind that sees several moves ahead. He’s a blessing to all Murim. My son ought to have spent more time watching and learning from you while he had the chance… What do you think of him?”

At Sima Gong’s sudden question, I answered without hesitation.

“He’s useful.”

“What?”

“Now that I’ve spent some time with him, he’s a pretty decent kid. A little gloomy, though.”

By Murim’s reckoning, Sama Pyo was much older than me.

But even though I’d just thrown the whole idea of respecting my elders to the dogs, Sima Gong only smiled in a way I couldn’t quite read.

“Thank you for saying so. It makes all the effort I put into raising him worthwhile.”

Over his shoulder, I saw Sama Pyo standing there without a trace of expression. It made me wonder if Sima Gong meant he’d raised his son as a father—or if he sounded more like a craftsman talking about a piece he’d made.

But the thought vanished as quickly as it had come, and I spoke again.

“So, you don’t plan to change your current judgment?”

“Decision. A choice made by firmly settling on a course of action or attitude.”

“So that’s a no. Then can I assume the Kongtong Sect’s position is the same?”

“The Kongtong Sect opposed it, but that changes nothing. All of Gansu Murim reached this decision after extensive discussion.”

Maybe. Was this really what Gansu Murim wanted?

Or…

*Was it only what the Black Dragon Demon Gate wanted?*

I swallowed the words hovering on the tip of my tongue and thought for a moment.

*Inventory.*

I mentally felt for an item stowed somewhere in that bottomless, pitch-black subspace.

But then I shook my head.

No matter how I looked at it, the timing wasn’t right yet.

Not now, at least.

“Then let’s do that.”

“What?”

The surprised question came from neither Jeok Cheongang, who was frowning, nor Sima Gong.

It was the Wind-and-Cloud Sword Lord. He stared at me with wide eyes.

“You’re willing to accept this as it stands? Are you serious?”

Right then, before I could answer, two other voices cut the Wind-and-Cloud Sword Lord off.

“Every group has its own rules, wherever you go. Just as our Zhongnan does.”

“Senior Brother is right. Junior Brother, as the Sect Leader of our sect, remember once more how you should conduct yourself.”

The Roaring Fury Swordsman and the Taeeul Merciless Sword.

Those were the two.

After his Senior Brothers spoke in turn, the Wind-and-Cloud Sword Lord muttered as though groaning.

“Senior Brothers. But how can we let this happen?”

“We can well imagine how you feel, Sect Leader. But we must tell you that further discord may jeopardize the greater cause.”

Sima Gong calmly but firmly cut off the Wind-and-Cloud Sword Lord before he could continue. Then he surveyed the room and went on.

“I hope everyone will remember this. We are allies united beneath the Murim Alliance’s banner, and we must not create discord over a decision that has already been made. Much less…”

Sima Gong’s deeply lowered gaze suddenly came to rest on me.

“Should anyone act unilaterally without seeking everyone’s agreement. Wouldn’t you say?”

I already knew what Sima Gong meant, so I nodded.

“I’ll keep that in mind.”

“I hope sending those horse caravans away wasn’t a grievous mistake for our allies.”

“There won’t be any problem. At least, if my expectations are right.”

“His name was Ma Junggeol, wasn’t it? If you’d let that man go as well… we would’ve been disappointed in you. Very disappointed.”

At the sudden drop in his voice, Jeok Cheongang’s eyebrow twitched. But I discreetly tugged at his sleeve from where Sima Gong couldn’t see, then shrugged.

“I’ll remember.”

After that, the meeting wrapped up in less than another fifteen minutes.

As the leaders of Gansu Murim filed out, they kept stealing anxious glances at Jeok Cheongang. He stayed silent, his face like someone suffering from a particularly nasty case of constipation.

Only after we’d escaped the eyes of everyone around us, leaving just the two of us, did he finally speak.

“What are you plotting?”

“What do you mean?”

“Don’t change the subject. You had something in mind, or you wouldn’t have tried so hard to hold this old man back.”

“I didn’t try to hold you back. I just gave you a look to calm you down.”

“What?”

“Were you planning to grab him by the collar and beat the crap out of him right there? The Sect Leader of the Black Dragon Demon Gate, no less?”

“Why? You think this old man couldn’t do it?”

“……”

Fair point.

My words caught in my throat for a moment. I let out a deep sigh, then resumed walking.

“There was something bothering me.”

“That would be Sima Gong. You can tell just by looking at that bastard’s face.”

“That’s not it. He’s hiding something.”

At my quiet words, Jeok Cheongang’s expression hardened too.

“What do you mean… Wait. Don’t tell me—”

His voice grew louder as he reached the end of the sentence. I gave a small shake of my head.

“Don’t jump to conclusions. I’m not sure yet.”

“Tell me everything. Don’t leave anything out.”

“Do you remember how Elder Nam suddenly came to see me a day ago and said he had something to discuss?”

“Of course. I suddenly had to relieve myself, so I didn’t hear him out.”

Jeok Cheongang furrowed his brow and continued.

“If it was that important, you’d have told me later. Why haven’t you said a word about it for more than a day?”

He was right.

I’d always discussed most important matters with Jeok Cheongang, and sometimes we’d even found the answer together.

But…

*There are exceptions.*

That day, that moment, was one of them.

*“It’s important. Something I can only tell you now.”*

Namho had approached me suddenly and, speaking in a hushed voice, told me something I hadn’t expected.

*“Just before we left the Jin Family of Taiyuan, I went looking for Sama Pyo because he was missing. Taishan was with him.”*

And there, the old agent of the Hidden Shadow Pavilion had caught a smell that was both familiar and strange.

*“There wasn’t a trace of anything, but I’m certain Sama Pyo was burning a missive.”*

No—by the time Sama Pyo had tried to hide it, it had already been more than an ordinary missive.

It was a secret letter.
```
