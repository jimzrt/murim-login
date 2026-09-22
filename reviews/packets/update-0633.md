<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0633.txt",
      "sha256": "c858652f63c644f8982321d2e9047b6ddc2df26274c2f2ed782ddab166e375b7",
      "bytes": 13325
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "79645b5f7e824407c893adb598b397f5490a893627857919c185f7ecf03593b2",
      "bytes": 2593
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2f3f19aceeb45c027e60e99df2cf1920f422688d555180cfce48f788a648c643",
      "bytes": 194555
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0c0e68b7ad1c43188fa33ac9338f76a28985199685cbd4ffb6410ae1a802a96f",
      "bytes": 553
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "bb539e289625f2f3c2fc0750106de621cfb65ef32dcfbad2f389fa8606012ee5",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "073873072154977e77dcd29c1e61d090953a70586e6916342521d48b4efce421",
      "bytes": 1936
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "a4f4535a0149c0908bf95305d9ede3824f5b967565f51fae4401a758308b346b",
      "bytes": 622
    },
    {
      "path": "characters/Namho.md",
      "sha256": "ff27309c923d32670bcc0ee247249b24d8de2f7ae67450736a84a25e71cf3fcf",
      "bytes": 843
    },
    {
      "path": "characters/Yayul Cheok.md",
      "sha256": "f3ebf296a26589c8855ca250919f590ac2e240071422ef787c170ddb8ebfd7fb",
      "bytes": 912
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "237a91df921cfc7f73cc2f2291611ffdc51d5e666308a92e94be22ac16860178",
      "bytes": 871
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "de6b7ccbed3e8cac823ccafa1f949c1d5fe29e593a0315637a6fedbffc956075",
      "bytes": 200854
    }
  ],
  "estimated_tokens": 12063
}
-->

# Durable State Update — Chapter 633

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 633. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 633. Profile updates may replace only one
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
  "chapter": 633,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 633,
    "continuity_sources": [633],
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
    "The Fire Dragon Pavilion remains in temporary lodging within the Nanman Beast Palace.",
    "Nanman's first tribal council opposed joining the Murim Alliance; the second council, involving all thirty-two tribes, is tomorrow.",
    "Jin Taekyung is in Nanman to contain a spreading crisis and assess whether Nanman can be persuaded to join the Murim Alliance.",
    "Jin's tiger mask has been privately identified by Yohi and recognized by Baeksang.",
    "Baeksang is the great chieftain of the Bai people, opposes Nanman joining the Murim Alliance, and bears a burn scar from Jeok Cheongang.",
    "The Miao, Bai, Yi, and Yao peoples are Nanman's four great tribes; Yohi seeks Yao dominance while Heugung remains easily manipulated.",
    "Jin has confirmed through Qi Sense that Yohi is fundamentally different from the Southern Heaven Demon Empress.",
    "The Fire Dragon Pavilion has spent two days investigating the Nanman Beast Palace and its surroundings without finding a trace of Dark Heaven, but betrayal remains possible.",
    "Yayul Cheok secretly summoned Jin and Namho before dawn to a ruined shrine because he is under pressure from the tribal chiefs and cannot safely meet them openly.",
    "Yayul Cheok and Baeksang were lifelong childhood friends and sworn brothers, but their present trust is under scrutiny.",
    "Jin is certain that the Southern Heaven Demon Empress will not leave Nanman alone.",
    "An unidentified urgent warning and System alert interrupted Jin's meeting with Yayul Cheok."
  ],
  "continuity_sources": [
    632,
    631
  ],
  "open_questions": [
    "What promise did Yohi and Baeksang make, and what does Yohi intend to gain from it?",
    "Why does Baeksang believe Yayul Cheok's judgment was wrong, and can Jin change his position on the alliance?",
    "Is Baeksang's rage at Jin's mention of someone's son connected to Jin Baekyang?",
    "Will Nanman's tribal council agree to join the Murim Alliance, and is one of its thirty-two chiefs a Dark Heaven traitor?",
    "Who delivered the urgent warning at the shrine, and what triggered the System alert?"
  ],
  "safe_through": 632,
  "temporary_decisions": [
    "Use Baeksang for 백상 and do not treat White Elephant as a separate alias.",
    "Use sworn younger brother for 불알 동생 in the relationship between Yayul Cheok and Baeksang.",
    "Render 화왕손파이 as Fire King hand pie.",
    "Render 풍둔 주둥아리룡 as Wind Style: Mouth Dragon.",
    "Render 초절정 초입 as the early stage of Supreme Peak."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 열화문    | **Fire Gate Clan**               |
| 소림     | **Shaolin**                      |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 중원     | **Central Plains**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 하남     | **Henan**              |
| 정마대전   | **Great Faction War**         |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 야율척 | **Yayul Cheok** | Beast Miao King and lord of the Nanman Beast Palace. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 사자후 | **lion's roar** | Taekyung's term for Song Il's crowd-shattering roar. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 오독문 | **Five Poisons Sect** | Formerly dominant Nanman faction destroyed by the Fire Gate Clan. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
| 야율목 | 야율척 | Young_Palace_Lord_to_Palace_Lord | Palace Lord | ceremonial and deferential | Yayul Mok kneels with his guards and formally greets Yayul Cheok upon his arrival. |
| 야율척 | 야율목 | Palace_Lord_to_Young_Palace_Lord | Mok | authoritative and familiar | Yayul Cheok questions Mok's unannounced departure and later addresses him as 목아 while discussing Nanman's tribes. |
| 야율척 | 진태경 | Nanman_Beast_Palace_Palace_Lord_to_Jeok_Cheongang's_Disciple | you / Disciple of Old Master Jeok / Jin Taekyung | rough, testing, and later welcoming | Yayul Cheok questions Taekyung as a suspected culprit, strikes him as a test, and then welcomes him after recognizing Jeok's Disciple. |
| 진태경 | 야율척 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Palace_Lord | Great Hero Yayul Cheok | formal and deferential | Taekyung gives Yayul Cheok a formal greeting as the nineteenth successor of the Fire Gate Clan. |
| 야율척 | 남호 | Palace_Lord_to_Hidden_Shadow_Pavilion_agent_and_guest | old man | blunt and inquisitive | Yayul Cheok calls on the old man beside Taishan to identify him. |
| 야율목 | 남호 | Nanman Young Palace Lord to elderly guest and Hidden Shadow Pavilion agent | old man | respectful and familiar | Yayul Mok uses the honorific 노인장 while praising Namho's knowledge of White Tigers. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 632
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 631
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 632
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 632
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 632
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Yayul Cheok.md

# Yayul Cheok (야율척)

- **Safe through:** Chapter 632
- **Aliases:** Beast Miao King
- **Role:** Yayul Cheok is the over-eighty Beast Miao King, lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and great chieftain representing the Miao people.
- **Personality:** Boisterous, warmhearted, forthright, playful, and politically conscious of the tribal coalition he leads.
- **Voice:** Rough, loud, convivial, and teasing, becoming authoritative when discussing Nanman's laws or political decisions.
- **Relationships:** Jeok Cheongang is an old acquaintance whom he respects; Baeksang is his sworn younger brother and childhood companion, and they fought together during the Great Faction War; Yayul Mok serves as his Young Palace Lord; Jin Taekyung is Jeok's Disciple whom he welcomes into the Nanman Beast Palace.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 632
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and Yayul Mok's father; Yayul Mok is his only surviving son after three older siblings died in the Great Faction War, Baeksang is his father's sworn younger brother, and his white tiger is a long-bonded companion.

## Korean source

```text
＃633화



밖에서 들려온 목소리는 한껏 숨죽인 상태였지만, 목소리에 실린 다급함과 인기척은 그렇지 못했다.

“구, 궁주님!”

호위로 짐작되는 누군가의 부름에 야수묘왕과 야율목이 고개를 번쩍 치켜든 그때.

“지금 애뇌산(哀牢山)에서 변고가……!”

쾅!

갑작스럽게 뻗어 나온 강맹한 기파가 사당 내부를 휩쓸었다.

낡아 빠진 문을 산산조각 낸 야수묘왕이 부릅뜬 눈으로 자신의 수하를 바라보며 외쳤다.

“애뇌산에서 변고가 생기다니! 그게 무슨 소리냐!”

그리고 그 순간, 목소리보다 앞서 귓가를 파고드는 나직한 종소리가 있었다.

띠링.



- 돌발 퀘스트, [알 수 없는 징조]가 생성되었습니다!

퀘스트



[알 수 없는 징조]



남만의 금지(禁地). 애뇌산이 비명을 지르고 있습니다.

높고 험한 수많은 봉우리에는 갈가리 찢긴 사체가 내걸리고, 그 사이에 놓인 천길 절벽에는 알 수 없는 무언가의 핏물이 흐릅니다. 검은 구름과 안개에 휩싸인 그곳으로부터 끝없이 흘러나오는 괴성이 모두를 두렵게 만들고 있습니다.

그리고 이제, 당신의 앞에 새로운 길이 나타났습니다.



등급 : 돌발 퀘스트

제한 : 진태경

임무 : 제한 시간 안에 애뇌산 조사 (미완료)

보상 : ???

실패 : ???



- 퀘스트를 수락하시겠습니까?



알 수 없는 징조라.

내심 중얼거린 나는 문득 퀘스트 제목을 바꿔야 한다는 생각이 들었다. ‘알 수 없는’ 징조가 아니라, ‘존나 확실한’ 징조로.

물론 그것과는 별개로 이 상황에서 내가 해야 할 대답은 이미 정해져 있었다.

‘퀘스트 수락.’

띠링.



- 돌발 퀘스트, [알 수 없는 징조]를 수락하셨습니다!

- 제한 시간이 생성되었습니다!



남은 시간 : 4시간 59분 59초



멈춰 있던 시간이 흐르기 시작하고 촌각(寸刻)이 채 지나기도 전, 우리는 깊은 새벽을 가로지르며 애뇌산으로 출발했다.



* * *



남만야수궁의 전사들은 용맹한 맹수와 함께 성장한다고 한다.

어릴 적부터 함께 자라며 유대감을 쌓다가, 성인식을 치른 뒤 한 사람의 전사로 인정받게 되면 정식으로 그 맹수의 주인이자 동료가 되는 것이다.

그러나 수백 년의 유구한 역사를 지닌 이 전통에도, 어디에나 그렇듯 예외는 있었다.

쉬쉭! 파스스슥!

야수묘왕 야율척은 맹수의 도움이 필요 없는 존재였다. 아마도 어렸을 때부터 그랬을 테고, 지금도 마찬가지다.

그는 남만이 낳은 가장 위대한 전사이자 맹수 그 자체였다.

어둠과 풀숲으로 가득한 밀림을 누구보다 앞장서서 돌파한 야수묘왕의 입에서, 거센 포효가 터져 나왔다.

크와아앙!

그것은 말 그대로 맹수의 포효였다. 항마의 힘을 지닌 소림사의 절공인 사자후(獅子吼)보다 거칠고 포악하며, 훨씬 더 원초적인.

그리고 이러한 야수묘왕의 포효는 짙은 어둠 속을 찢으며 더 멀리, 빠르게 퍼져 나가며 경고를 알렸다.

까마득한 산등성이 아래, 곳곳에서 솟구치는 수백의 횃불을 바라본 야수묘왕이 어느덧 주위를 감싸며 달리는 호위들을 향해 외쳤다.

“기산. 도곡. 외궁(外宮)으로 가라. 외궁에 머무르는 부족장들을 찾아 사람들을 안심시키고 전사들을 동원하여 혹시 모를 외침(外侵)을 방비하라 일러라!”

“옛!”

“원후. 만적. 너희는 내궁(內宮)이다. 묘족의 전사들을 동원하여 궁 내부를 지켜라!”

“존명!”

“나머지 셋은 다른 대족장들을 찾아가 지금의 상황을 알리고, 각각 일백의 정예 전사를 동원하여 애뇌산으로 향하라 전해라!”

묘족 내에서 가장 뛰어난 전사들로 구성되어 있다는 궁주 직속의 호위대 칠묘호(七苗虎)에게 일사불란한 지시를 내린 야수묘왕의 시선이, 열심히 자신의 뒤를 따르는 늦둥이 아들을 향해 미끄러졌다.

“목아.”

“……예. 아버님.”

야율목의 안색이 어두워 보이는 건 주위에 내려앉은 어둠 때문이 아니다.

그리고 이미 뒤에 나올 말을 예상했다는 듯, 흐린 목소리로 대답하는 아들을 향해 야수묘왕은 단호한 어조로 말을 이었다.

“저들과 함께 가라. 묘족 휘하의 전사들을 소집하고, 만일의 상황을 대비하여 일군(一群)을 일으켜야 할 것이다.”

“하지만…….”

“잊었느냐? 넌 묘족의 소족장이자, 남만야수궁의 소궁주다.”

왜 야수묘왕이 남만야수궁의 궁주인지 새삼 깨닫게 되는 부분이다.

처음 만났을 때만 해도 배부른 수사자처럼 느슨한 모습을 보였던 야수묘왕이지만, 지금의 그는 먹잇감을 코앞에 둔 맹수와 같았다.

그리고 야율목은 지금 같은 상황에서 추상같은 아버지의 지시를 거스를 만큼 철부지가 아니었다.

“……궁주님의 명을 받듭니다.”

하지만 대답과는 달리, 야율목은 곧장 대열을 이탈하지 않았다.

녀석은 야수묘왕과 나란히 달려 나가던 내 옆으로 바짝 다가와 뜻밖의 제안을 건넸다.

“이 녀석과 함께 가라.”

“어?”

- 크릉?

여기서 야율목이 말하는 이 녀석이라는 건 다름 아닌 백호였고, 그래서 더 의외일 수밖에 없었다.

남만의 전사들은 자신과 함께하는 맹수를 가장 소중한 전우이자, 가족이라고 생각하니까.

쉬쉭!

코앞까지 들이닥친 나뭇가지를 피한 나는 조심스럽게 물었다.

“이거 혹시 분양해 주는 거냐? 가정 분양 그런 거야?”

“말도 안 되는 소리!”

- 크르르!

“깜짝이야. 왜 그렇게 화를 내. 아니면 아니라고 하면 되지.”

“아니다! 네놈이 조금이라도 힘을 아껴야 아버님께 보탬이 될 것이 아니냐!”

- 크아아앙!

이심전심(以心傳心)이 괜히 있는 말이 아닌지, 사람과 짐승이 쌍으로 지랄이다.

뭐, 그나저나…….

‘확실히 타고 가면 훨씬 낫긴 하지.’

내가 지닌 공력의 양은 중원에서도 결코 쉽게 찾아볼 수 없는 수준이지만, 그렇다고 화수분처럼 끊임없이 샘솟는 정도는 아니다.

만약 애뇌산에서 남천마후가 이끄는 암천을 상대하게 된다면 야율목의 말처럼 최대한 힘을 비축하는 게 좋겠지.

‘기특한 놈일세.’

남만에 온 지 그리 오래되지는 않았지만, 이곳에서 자신의 맹수를 내어준다는 게 어떤 의미인지는 잘 안다.

대견한 눈빛으로 야율목을 바라본 나는 녀석에게 한 가지 선물을 주기로 했다.

“자, 여기. 부담스럽다고 사양하지는 마. 원래 오는 게 있으면 가는 게 있는 법이니까.”

파스스슥!

스치는 바람과 나뭇가지 사이를 감도는 침묵. 내 양손에 짐짝처럼 들려 있던 남호가 무거운 표정으로 입을 열었다.

“내가 물건이냐?”

“물건이면 던져서 공격이라도 할 수 있죠. 남 노인은 그러지도 못해요.”

“이런 위아래 없는 불한당을 보았나. 감히 노인 공격을…….”

“군말하지 말고 가십쇼. 앞으로의 노후 계획도 창창하신데 괜히 휘말리지 마시고. 그리고 저희 애들도 손 놓고 있을 수만은 없지 않습니까.”

이건 무시가 아니라 배려다. 남호가 제아무리 산전수전 다 겪은 은영각 요원이라고 하지만, 결국 무공이라고는 일초반식도 익히지 않은 노인일 뿐이니까.

그리고 그 사실을 누구보다 잘 아는 남호는 근심 어린 얼굴로 한숨을 푹 내쉬었다.

“화룡각에 똑똑히 전하지. 각주가 찾는다고.”

“그 정도면 충분합니다. 뭘 경계해야 하는지도 알려 주실 거라 믿고요.”

마침내 남만이라는 도화선에 불이 붙었다.

중요한 건 그 불을 누가 붙인 것이 외부의 적이냐. 내부의 적이냐는 것이다.

노쇠한 몸과는 달리 두뇌는 조금도 늙지 않은 남호는 작게 고개를 끄덕였다.

“각주, 마지막으로 한마디만 하지.”

“네?”

“다치지 말게.”

“아.”

“물론 죽는 건 더더욱 안 돼.”

걱정이 전해지는 그의 한 마디에 난 대답 대신 슬쩍 웃었고, 내게서 남호를 건네받은 야율목은 눈짓과 함께 백호의 등을 박차고 날아올랐다.

탁, 쉬쉭!

흐린 달빛 아래 그림자가 스친다.

칠묘호와 함께 대열을 이탈한 그들이 어둠 너머로 파묻히자, 마치 거대한 불곰처럼 두 팔과 다리로 바람처럼 내달리던 야수묘왕이 한층 속도를 높였다.

파파파팟! 콰직!

두꺼운 나뭇가지가 꺾이고 우거진 풀숲이 짓밟힌다.

야율목이 남기고 간 백호의 등에 올라탄 나는, 맹렬하게 귓가를 스쳐 지나가는 바람 사이로 전해지는 목소리를 들었다.

“암천의 소행이라고 생각하느냐?”

“가 봐야 알겠지만 그럴 가능성이 높겠죠. 최소한 어떤 식으로든 연관되어 있을 겁니다.”

딱딱하게 굳은 얼굴을 한 야수묘왕을 향해, 내가 재차 입을 열었다.

“그런데 애뇌산이 정확히 어떤 곳입니까?”

“금지(禁地)다. 허락된 자들이 아니라면 누구도 드나들 수 없는.”

애뇌산이 금지라는 것은 이미 알고 있었다. 오는 길에 남호에게서, 그리고 조금 전에 시스템으로부터.

그렇기에 야수묘왕의 대답은 그리 명쾌하지 못했다.

“그건 남만야수궁도 마찬가지 아닙니까? 아니, 야수궁뿐만이 아니라 남만 대부분이 그런 것 같던데요.”

“다르다. 확실히 다르지. 그곳은 각 부족 내에서도 가장 뛰어난 전사들이 출입하며 경계하는 곳이니까.”

“도대체 무슨 이유로…….”

“자그마치 삼백여 년 전의 일이다. 내 선조의 선조, 그 선조의 선조가 남만에서 살아가고 있었을 때. 이 땅에는 백여 개가 넘는 부족이 오래전부터 죽고 죽이는 전쟁을 이어 가고 있었다. 그 과정에서 수십 개의 부족이 사라졌고, 간신히 살아남은 후손들은 남만 가장 깊숙한 곳에서 자신들만의 문파를 세웠다. 그리고 어떤 날카로운 무기나 맹수보다 위험한 것을 다루기 시작했지.”

그 순간, 몇 달 전 하남에서 적천강과 나누었던 대화가 뇌리를 스쳤다.

열화문의 옛 문주들의 행적과 연관되어 있던 남만야수궁의 역사에 대하여.

그것은 남만야수궁이 정마대전에 참여했던 이유 중 하나이기도 했다.

‘그렇다면.’

답은 하나다. 나는 나직하게 중얼거렸다.

“독(毒). 독이군요.”

“그래. 그것이 향후 백 년간 남만을 공포로 물들였던 오독문(五毒門)의 시작이었다.”

우리는 높이 솟은 봉우리를 넘고, 언덕을 박차고 뛰어올라 울창한 나무를 밟으며 내달렸다.

발톱처럼 그러모은 손으로 두꺼운 나무를 후려쳐 날려 보낸 야수묘왕이 말을 이었다.

“실로 많은 사람이 죽었다고 했다. 강가에는 죽은 물고기들로 가득했고, 떠내려온 물고기를 멋모르고 먹은 짐승들도 죽었지. 우물에는 독이 퍼졌고 알 수 없는 전염병이 돌았다. 수천, 수만에 달하는 이들이 죽어 나가자, 분열되었던 부족들은 마침내 한 깃발 아래에 모여 새로운 전쟁을 시작했지.”

그것이 남만야수궁의 탄생이었다.

하지만 죽음은 죽음을 낳았고, 복수는 복수로 돌아왔다.

그리고 끊임없이 굴러가는 복수의 고리에 갇힌 남만야수궁과 오독문이 치열한 전쟁을 벌이고 있던 그때.

머나먼 중원으로부터 이방인이 도착했다.

“그는 자신을 열화문의 문주라고 밝혔다. 난생처음 들었을 생소한 이름이었지만 선조들에게는 상관없었겠지. 그는 남만 땅에 들어오자마자 자신을 습격한 오독문의 전사 일백을 태워 죽여 버렸으니까.”

당대의 열화문주는 오독문의 예상치도 못한 성대한 환영 인사가 마음에 들지 않았고, 여느 무림인들처럼 독을 혐오했다.

그리고 팽팽하던 전력의 저울추를 엉덩이로 깔아뭉개며, 남만야수궁을 이끌고 오독문을 잿더미로 만들었다.

“문제는 그가 떠난 후였다.”

오독문의 문도들은 백골이 되었지만, 그들이 마지막 순간 풀어놓은 독물과 맹수들은 오독문의 본거지였던 산속 깊은 곳에서 개체 수를 불려 나갔다. 천천히. 은밀하게.

그리고 오독문의 본거지였던 그곳이 바로…….

“바로 저곳이다. 애뇌산.”

나는 야수묘왕이 손끝을 따라 고개를 들었다.

까마득히 멀리, 구름과 안개에 휩싸인 봉우리로 가득한 검은 산이 모습을 드러내고 있었다.
```

## Final English reading copy

```markdown
# Chapter 633

The voice from outside was hushed as much as possible, but neither its urgency nor the presence behind it could be concealed.

“P-Palace Lord!”

At the call, presumably from one of his guards, the Beast Miao King and Yayul Mok sharply raised their heads.

“Something has happened at Ailao Mountain…!”

*Boom!*

A powerful wave of qi suddenly shot out and swept through the shrine.

The Beast Miao King shattered the decrepit door and shouted at one of his men with wide, blazing eyes.

“Something happened at Ailao Mountain? What do you mean?”

And at that very moment, a low ringing tone pierced my ears before the voice could reach me.

*Ding.*

> **System**
>
> - A sudden quest, **Unknown Omen**, has been generated!
>
> **Quest**
>
> **Unknown Omen**
>
> Nanman’s forbidden land, Ailao Mountain, is screaming.
>
> Across its countless high and treacherous peaks, bodies torn to pieces hang in the open air. Blood from something unknown flows along the thousand-foot cliffs between them. The endless howls rising from that place, shrouded in black clouds and mist, have filled everyone with fear.
>
> And now, a new path has appeared before you.
>
> **Grade:** Sudden Quest
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Investigate Ailao Mountain within the time limit (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???
>
> - Would you like to accept the quest?

*An unknown omen, huh?*

I muttered inwardly, then suddenly thought the quest title needed to be changed.

Not *Unknown Omen*, but *Fucking Obvious Omen*.

Of course, putting that aside, I already knew what answer I had to give in this situation.

*Accept quest.*

*Ding.*

> **System**
>
> - You have accepted the sudden quest, **Unknown Omen**!
>
> - A time limit has been created!
>
> **Time Remaining:** 4 hours 59 minutes 59 seconds

Time, which had been frozen, began to flow again. Before even a moment had passed, we set out for Ailao Mountain, racing through the predawn darkness.

* * *

They said that the warriors of the Nanman Beast Palace grew up alongside fierce beasts.

They grew up together from childhood, forming bonds along the way. After completing their coming-of-age ceremony and being recognized as full-fledged warriors, they officially became the beasts’ owners and companions.

However, even this venerable tradition, with its history of several hundred years, had exceptions, as everything did.

*Whoosh! Rustle!*

The Beast Miao King Yayul Cheok was someone who had no need for the help of a beast.

He had probably been that way since childhood, and he was the same even now.

He was the greatest warrior Nanman had ever produced—and a beast himself.

Leading the way through a jungle filled with darkness and tangled grass, the Beast Miao King let out a mighty roar.

*Gwaaaar!*

It was quite literally the roar of a beast. Rougher, more savage, and far more primal than the lion’s roar, the supreme technique of Shaolin Temple imbued with the power to subdue demons.

The Beast Miao King’s roar tore through the deep darkness and spread farther and faster, announcing a warning.

Looking down at the hundreds of torches rising in various places beneath a distant mountain ridge, the Beast Miao King shouted at the guards running around him.

“Gisan. Dogok. Go to the Outer Palace. Find the tribal chiefs staying there, reassure the people, and mobilize the warriors to prepare for a possible foreign invasion!”

“Yes, sir!”

“Wonhu. Manjeok. You’re going to the Inner Palace. Mobilize the Miao warriors and protect the inside of the palace!”

“At your command!”

“The remaining three of you, find the other great chieftains and inform them of the situation. Tell each of them to mobilize one hundred elite warriors and head for Ailao Mountain!”

The Beast Miao King gave a series of precise orders to the Seven Miao Tigers, his personal guard made up of the finest warriors among the Miao people.

Then his gaze slid toward his late-born son, who was running hard behind him.

“Mok.”

“……Yes, Father.”

Yayul Mok’s grim expression had nothing to do with the darkness settling around us.

As though he had already anticipated what his father was about to say, he answered in a dull voice. The Beast Miao King continued in a firm tone.

“Go with them. Gather the warriors under the Miao people and raise a force in case something happens.”

“But…”

“Have you forgotten? You’re the Young Chieftain of the Miao people and the Young Palace Lord of the Nanman Beast Palace.”

This was when I realized once again why the Beast Miao King was the lord of the Nanman Beast Palace.

When I had first met him, he had seemed relaxed, like a well-fed male lion. But now, he was a beast with its prey right in front of it.

And Yayul Mok wasn’t immature enough to disobey his father’s unyielding orders in a situation like this.

“……I obey, Palace Lord.”

But contrary to his answer, Yayul Mok did not immediately leave the formation.

Instead, he moved right beside me as I ran alongside the Beast Miao King and made an unexpected proposal.

“Take this one with you.”

“Huh?”

*Grrr?*

The one Yayul Mok was talking about was none other than White Tiger, which made the offer all the more surprising.

The warriors of Nanman considered the beasts who fought alongside them their most precious comrades—and their family.

*Whoosh!*

I dodged a branch that shot right into my face and asked carefully.

“Are you giving him away? Like, to a new family?”

“What nonsense!”

*Grrrr!*

“Whoa. Why are you getting so angry? If it’s not, just say no.”

“No! If you conserve even a little of your strength, you can be of greater help to Father!”

*Gwaaaar!*

It wasn’t for nothing that they said hearts could communicate without words. Man and beast were both being fucking ridiculous as a pair.

*Anyway…*

*It would definitely be much better to ride him.*

The amount of internal energy I possessed was a level that could not easily be found even in the Central Plains. But it wasn’t as though it sprang up endlessly from some bottomless reservoir.

If I ended up facing Dark Heaven under the command of the Southern Heaven Demon Empress at Ailao Mountain, then, as Yayul Mok had said, it would be best to conserve as much strength as possible.

*What a good kid.*

I hadn’t been in Nanman for very long, but I understood what it meant for someone here to lend me their beast.

I looked at Yayul Mok with an approving gaze and decided to give him a present in return.

“Here. Don’t refuse just because you feel burdened. If something comes in, something should go out.”

*Rustle!*

Silence flowed between the passing wind and swaying branches.

Namho, who was being held in both my arms like a piece of luggage, spoke with a grim expression.

“Am I an object?”

“If you were an object, we could throw you and use you to attack. Old Man Namho can’t even do that.”

“Have you ever seen such a lawless thug with no respect for his elders? How dare you attack an old man…”

“Quit complaining and go. Your retirement plans are looking bright, so don’t get dragged into this for no reason. And our kids can’t just sit around doing nothing either.”

This wasn’t me ignoring him. It was consideration.

No matter how much hardship Namho, an agent of the Hidden Shadow Pavilion, had endured, he was still an old man who had never learned even a single move of martial arts.

And Namho knew that better than anyone else. He let out a deep sigh, his face filled with worry.

“I’ll make sure to tell the Fire Dragon Pavilion. That the Pavilion Master is looking for you.”

“That should be enough. I trust you’ll tell them what they need to be wary of, too.”

At last, the fuse attached to the Nanman powder keg had been lit.

The important question was whether the one who had lit it was an outside enemy or an enemy within.

Unlike his aging body, Namho’s mind had not grown old in the slightest. He gave a small nod.

“Pavilion Master, there’s one last thing I want to say.”

“Yes?”

“Don’t get hurt.”

“Ah.”

“Of course, you absolutely mustn’t die, either.”

I answered his concern with a faint smile instead of words.

Yayul Mok took Namho from me, then, with a glance, kicked off White Tiger’s back and sprang away.

*Tap. Whoosh!*

A shadow swept beneath the hazy moonlight.

As Yayul Mok and the Seven Miao Tigers disappeared into the darkness, the Beast Miao King, who had been charging on all fours like a gigantic brown bear, increased his speed.

*Crack-crack-crack! Smash!*

Thick branches snapped, and dense grass was trampled beneath us.

I climbed onto White Tiger’s back, which Yayul Mok had left behind, and heard the Beast Miao King’s voice through the wind rushing violently past my ears.

“Do you think this was Dark Heaven’s doing?”

“We’ll have to get there to know for sure, but the possibility is high. At the very least, it’ll be connected somehow.”

I spoke again to the Beast Miao King, whose face had hardened.

“But what exactly is Ailao Mountain?”

“It is a forbidden land. No one may enter unless they have permission.”

I already knew that Ailao Mountain was a forbidden land. Namho had told me on the way here, and the System had confirmed it moments ago.

That was why the Beast Miao King’s answer didn’t feel particularly clear.

“But isn’t the Nanman Beast Palace the same? No, now that I think about it, most of Nanman seems to be like that.”

“It’s different. Completely different. The most outstanding warriors from each tribe enter that place and stand guard.”

“Why on earth…?”

“It happened more than three hundred years ago. Back when my ancestor’s ancestor—and his ancestor before him—were living in Nanman. At that time, more than a hundred tribes had been waging wars of life and death across this land for generations. Dozens of tribes vanished in the process, and the descendants who barely survived established a sect of their own in the deepest reaches of Nanman. Then they began handling something more dangerous than any sharp weapon or beast.”

At that moment, a conversation I had shared with Jeok Cheongang in Henan several months ago flashed through my mind.

It had been about the history of the Nanman Beast Palace, which was connected to the deeds of the former Sect Leaders of the Fire Gate Clan.

That history was also one of the reasons the Nanman Beast Palace had taken part in the Great Faction War.

*If that’s the case…*

There was only one answer.

I muttered softly.

“Poison. It was poison.”

“That’s right. That was the beginning of the Five Poisons Sect, which terrorized Nanman for the next hundred years.”

We crossed towering peaks, leaped over hills, and raced through the dense forest, stepping on the tops of trees.

The Beast Miao King curled his hands like claws, struck a thick tree, and sent it flying before continuing.

“They say an enormous number of people died. The riverbanks were littered with dead fish, and the beasts that unwittingly ate the fish washed downstream died as well. Poison spread through the wells, and an unknown epidemic broke out. When thousands upon tens of thousands had died, the tribes that had once been divided finally gathered beneath a single banner and began a new war.”

That was the birth of the Nanman Beast Palace.

But death bred death, and revenge returned as revenge.

And just as the Nanman Beast Palace and the Five Poisons Sect were waging a fierce war, trapped in an endlessly turning cycle of vengeance, an outsider arrived from the distant Central Plains.

“He claimed to be the Sect Leader of the Fire Gate Clan. It was an unfamiliar name, one my ancestors had probably never heard in their lives, but that likely didn’t matter to them. The moment he entered Nanman, he burned to death the one hundred warriors of the Five Poisons Sect who had ambushed him.”

The Fire Gate Clan’s Sect Leader of that era had not appreciated the Five Poisons Sect’s unexpectedly grand welcome.

Like most martial artists, he also hated poison.

He planted his ass on the scales of power and crushed the balance between them, then led the Nanman Beast Palace and reduced the Five Poisons Sect to ashes.

“The problem came after he left.”

The disciples of the Five Poisons Sect had turned to white bones, but the venomous beasts and fierce beasts they released in their final moments continued multiplying deep in the mountains where the sect had once made its headquarters.

Slowly.

Secretly.

And that former headquarters of the Five Poisons Sect was none other than…

“That place right there. Ailao Mountain.”

I followed the Beast Miao King’s fingertip and raised my head.

Far in the distance, a black mountain filled with peaks shrouded in clouds and mist came into view.
```
