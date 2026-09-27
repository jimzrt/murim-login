<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1105.txt",
      "sha256": "eac692b786cb948d29451e2c32eebddc7defc2d3b166b4003b0562bf46ddce00",
      "bytes": 11875
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "fd29d7a4a570ab8da041554743bd51ee8a0ef040e34846652cd58c29dfef282e",
      "bytes": 1209
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2195176fcecc1f2d4760ffbc4a2601370e7609089bc148ea8deda43236c266fc",
      "bytes": 244248
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "206e8f52eff5d8eacc9f3a037c6bd75f7573d4f52986ec22893431fdd6f0a4cd",
      "bytes": 848
    },
    {
      "path": "characters/Dalai Lama.md",
      "sha256": "300812b601210d558981c4f006429f3d4511a9e28ec99cadfbf35cff3506b82c",
      "bytes": 779
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "05f9225b50a81231d652d9b6f164f51230904a5315f6e4216f3a395ec98db215",
      "bytes": 760
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "d62b483734180f4bd2a202a77974477620ddc5a09d97ad9c5af81650f61ce2b9",
      "bytes": 1001
    },
    {
      "path": "characters/Hyeoncheon.md",
      "sha256": "2c742785e31193c02392e21dbf39c708ff38337cb4e3e614644e8edb97d6a55c",
      "bytes": 651
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "e834c246b71dbc08e6ddf96750c755495e043ba41fc9f0b955eee7ea2854ac84",
      "bytes": 1513
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c61dccae9c98c58f19fc334da68767c3dc54a09efba980c0d3c2d837918322f3",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "9e9deac5ac6998909bfb3e822ebb351184c08ba1f55bb83e9488a2582a00c156",
      "bytes": 623
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "71b7be9f8720438f5ed487d2affddfac9bc2ca7a569cb6f638a05df48e58a155",
      "bytes": 716
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "7d5539af1e284a236ad4316839d4d059c5a59a2fab2614f464155afc01f04d84",
      "bytes": 288140
    }
  ],
  "estimated_tokens": 11265
}
-->

# Durable State Update — Chapter 1105

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
1 and safe_through 1105. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1105. Profile updates may replace only one
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
  "chapter": 1105,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1105,
    "continuity_sources": [1105],
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
    "Dark Heaven and the Potala Palace are attacking Xining; fighting continues at the breached western wall.",
    "The Blood Lord has coordinated pressure across Xining’s gates; the siege is underway.",
    "The Blood Lord is fighting Jin Taekyung at the western breach and can command weapons and absorb blood to gain strength.",
    "The Lord of Heaven appears to want Jin Taekyung above all else; the Blood Lord suspects this but attacks Taekyung anyway.",
    "Taekyung is injured but still standing; others have begun to rise behind him."
  ],
  "continuity_sources": [
    1103,
    1104
  ],
  "open_questions": [
    "Why does the Lord of Heaven want Taekyung, and what does he intend to do with him?",
    "Who are the allies approaching by river from the east?",
    "Which of Cheongheoja’s Disciples is the hidden Dark Heaven agent, and what did Cheongheoja ask Taekyung to do?",
    "What happened to Cheongpung after he intercepted the attack?"
  ],
  "safe_through": 1104,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 굉도     | **Hong Dao**       |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 열화문    | **Fire Gate Clan**               |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 사천     | **Sichuan**            |
| 감숙     | **Gansu**              |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 달뢰라마 | **Dalai Lama** | Traditional title of the Potala Palace’s leader. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 현천진인 | **Perfected Being Hyeoncheon** | Current Sect Leader of Wudang and Hyeongong's Senior Brother. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 숭산 | **Mount Song** | Mountain where Shaolin Temple is located. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 일주천 | **complete circulation** | Completion of one full qi circulation. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 포달랍궁 | **Potala Palace** | Palace in Tibet. |
| 내성 | **Inner City** | Fortified inner district of the Murim Alliance. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 조이 | **Joey** | U.S. military or political official introduced by first name only. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |
| 서문 | **West Gate** | One of the Nanman Beast Palace's gates. |
| 북문 | **North Gate** | The gate where Jin Taekyung and Yohi arrive. |
| 진인 | **Perfected One** | Honorific for the two Kongtong Elders killed at Dunhuang. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 서녕 | **Xining** | Capital of Qinghai. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 굉도 | old_friends | Hong Dao | familiar and teasing | Uses Hong Dao's personal name in their casual reunion. |
| 굉도 | 적천강 | old_friends | Fire Gate Sect Leader | familiar and teasing | Teases Jeok as the carefree Fire Gate Sect Leader. |
| 굉도 | 진태경 | senior_monk_to_guest_benefactor | Benefactor | formal-polite and probing | Hong Dao repeatedly addresses Taekyung as 시주 while identifying him as the Master of Morning Star. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 남천마후 | 천주 | devoted_servant_to_revered_master | Lord of Heaven | reverent and prayerful | The Southern Heaven Demon Empress prays that the Lord of Heaven will remember her loyalty and love. |
| 진태경 | 현천진인 | young martial artist addressing a senior Daoist Sect Leader | Perfected Being | polite | Jin responds respectfully to Hyeoncheon's assessment of the retreat. |
| 현천진인 | 진태경 | Kongtong Sect Leader addressing an allied martial artist | Daoist Friend Jin | respectful and measured | Refers to Jin as 진 도우 while discussing the Zhongnan Disciples’ future. |
| 혈주 | 달뢰라마 | allied leader to allied leader | Palace Lord | familiar, then threatening and insulting | Calls him 궁주, then warns him not to speak down to him. |
| 달뢰라마 | 혈주 | allied leader to allied leader | donor; you | formal, then angry and informal | Initially uses the Buddhist honorific 시주 before challenging the Blood Lord. |
| 진태경 | 혈주 | hostile_opponent_to_hostile_opponent | you; you son of a bitch | insulting-casual | Taekyung insults the Blood Lord while challenging his claim that he will kill him. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1104
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure and formidable combatant who commands weapons telekinetically and absorbs blood to restore vitality.
- **Personality:** Cunning and controlling, he avoids costly risks while manipulating allies; beneath his devotion to the Lord of Heaven, he resents being treated as disposable and resents Taekyung’s apparent favor.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven but suspects the Lord wants Jin Taekyung above all else; despite that, he attacks Taekyung, whom he considers a formidable adversary, as well as Cheongpung.

### Dalai Lama.md

# Dalai Lama (달뢰라마)

- **Safe through:** Chapter 1102
- **Aliases:** Palace Lord
- **Role:** The Dalai Lama is the Potala Palace’s leader and ruler of Xizang, commanding its Twelve Secret Monks.
- **Personality:** Fiercely hostile to the Fire Gate Clan and committed to the Potala Palace’s interests; he trusts the Lord of Heaven but distrusts the Blood Lord.
- **Voice:** Uses Buddhist self-reference and addresses others as “donor”; his Han speech is described as halting.
- **Relationships:** He leads the Potala Palace in an unequal alliance with Dark Heaven, accepting its terms to pursue their shared goal of destroying the Fire Gate Clan and avenge the Palace’s longstanding grievance.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1103
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 1099
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang and close friend of Peng Cheolhu; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed, warned Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff, and sent Unnamed to find the Master of Morning Star.

### Hyeoncheon.md

# Perfected Being Hyeoncheon (현천진인)

- **Safe through:** Chapter 1096
- **Aliases:** None
- **Role:** Perfected Being Hyeoncheon is the current Sect Leader of the Kongtong Sect, a veteran Daoist master, and a Supreme Peak martial artist.
- **Personality:** Grave and reflective, he bears the losses of the Great Faction War yet rejects punishing the innocent for their relatives’ crimes.
- **Voice:** Measured, solemn, and calm with the authority of a Sect Leader.
- **Relationships:** Hyeongong is his Junior Brother, and both studied under the same master from childhood.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1102
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1104
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1104
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 1095
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

## Korean source

```text
＃1105화



오랜 세월 동안 끊임없이 이어진 외침(外侵) 때문일까.

현재 서녕을 둘러싼 네 면의 성벽은 그 길이만 무려 십 리에 달하는, 중원에서도 쉽게 찾아볼 수 없는 굳건함과 광활한 면적을 갖추게 되었다.

그러나 모든 것에는 저마다의 장단점이 있는 법.

시간의 흐름에 따라 조금씩 보강된 성벽은 외적의 침입을 효율적으로 막아 낼 수 있었지만, 그만큼 수비해야 할 범위도 증가했다.

그에 따라 수성 측은 상당한 거리 차이로 인해 아군과의 소통이 곤란하지 않도록 방편을 마련해야만 했다.

이를테면, 곳곳에 배치한 전고(戰鼓)와 깃발을 이용한 방식으로.

하지만 적어도 지금 이 순간, 불현듯 서쪽에서 솟구쳐 오른 핏빛 섬광은 그 모든 것을 무의미하게 만들기에 충분했다.

화아아악.

해 질 녘 노을이 수십, 수백 개가 겹쳐진다면 이런 광경일까.

느려진 세상 속, 도무지 뭐라 형용할 수 없는 그 기현상을 목격한 무수한 눈동자가 부릅떠졌다.

십여 개의 망루 위에서 온 힘을 다해 자신이 맡은 전고와 깃발을 치고 휘두르던 병사들도, 서녕 중심부의 내성(內城)에 숨어 제 혈육들을 끌어안은 채 문틈 사이를 엿보던 백성들도.

파도처럼 몰려오는 적들에 맞서 싸우던 관과 무림의 연합군과 그런 그들의 중심이자 선두가 되어 쉴 새 없이 적을 베어 넘기던 초절정 고수들까지도.

그리고 그들 모두가 본능적으로 등골을 타고 솟구치는 오싹한 한기를 느낀 순간.

팟.

마침내, 서쪽 성벽을 타고 솟구친 핏빛 섬광이 크게 부풀어 올랐다.

아니, 선명하고도 섬뜩한 붉은 빛무리와 함께 함께 폭발했다.

구구구구궁!

귓가를 먹먹하게 만드는 굉음.

지면이, 암석으로 이루어진 성벽 전체가 뒤흔들린다.

뒤이어 서쪽 성벽을 넘어 들이닥친 거대한 여파가, 석상처럼 굳어 있던 사람들의 머리 위를 뒤덮었다.

“위험……!”

콰아아아아!

누군가의 외마디 외침을 집어삼키며 사방을 휩쓰는 바람.

그리고 이와 같은 상황은 북문(北門) 역시 다르지 않았다.

수많은 먼지와 부서진 암석, 심지어는 주인 잃은 날붙이까지 뒤섞인 그것을 피하기 위해 모두가 자세를 낮추고 엄폐물을 찾아 몸을 날렸다.

이 순간에도 선두를 지키고 있는 한 사람을 제외하고는.

화륵, 퍼어엉!

거칠게 내뻗은 일권(一拳)과 함께 터져 나온 화염이 공간을 살라 먹는다.

자연재해와도 같았던 폭풍조차 그 열기를 이기지 못하고 고개를 숙이고, 북문을 지키고 있던 수비군을 향해 날아들던 모든 것들이 단숨에 증발했다.

스아아아.

어느덧 온순해진 바람에 실려 천천히 흩어지는 잿가루.

그러나 생각지도 못한 위협 속에서 아군을 지켜 낸 그, 화왕(火王) 적천강의 눈동자는 어느 때보다 침잠하게 가라앉아 있었다.

‘……이건 도대체.’

비록 십왕의 수좌로 머무르고 있으나, 이미 삼성(三星)과 함께 어깨를 나란히 할 정도의 경지에 오른 그다.

그렇기에 온 피부로, 감각으로 느낄 수 있었다.

앞서 서쪽에서 솟구친 저 아득한 핏빛 섬광에, 얼마나 거대한 힘이 담겨 있었는지.

더불어 이백여 장도 넘게 떨어진 북문까지 이 정도의 여파가 미칠 정도라면, 저 기현상의 근원지인 서문의 상황은 어느 정도일지.

‘혈주(血主), 네놈이 어찌.’

적천강은 자신도 모르게 입술을 깨물었다.

과거 숭산에서 맞닥트렸을 때보다도 확연히 진일보한 혈주의 무위도 무위였지만, 가슴 한구석을 짓누르는 불안감과 함께 떠오른 누군가의 목소리 때문이기도 했다.



‘제가 서문을 맡겠습니다.’



진태경.

자신의 제자가 전투 직전에서야 던진 그 한 마디에, 적천강은 일말의 고민조차 하지 않고 대답했었다.



‘불가. 그따위 헛소리를 지껄일 시간에 일주천이라도 한 번 더 하거라. 괜히 까불대다가 칼 맞지 말고.’

‘공력 빵빵하고, 칼은 뭐 적당히 맞겠죠. 그러니까 서문은 제가 책임지겠습니다.’

‘안 된다고 했다.’

‘아니, 왜요?’

‘몰라서 묻느냐? 저 빌어먹을 놈은 오래전부터 노부의 몫이었다. 오늘은 기필코 그날의 혈채(血債)를 받아낼 것이다.’



적천강의 대답은 사실인 동시에, 사실이 아니었다.

이는 오랜 벗이었던 굉도의 복수를 위함이기도 했지만, 서문에는 혈주를 포함한 적들의 주력이 대거 포진해 있었다는 이유가 더욱 컸으니까.

앞뒤 안 가리는 천둥벌거숭이에, 예의라고는 진즉 밥 말아 먹은 놈이지만 하나뿐인 제자다.

어느덧 세상 그 무엇보다 소중해진, 그런 제자를 가장 위험한 곳에 홀로 내버려 둘 수는 없었다.

물론, 그 쑥스러운 마음을 에둘러 표현하기에는 그의 제자 역시 스승을 너무나도 잘 알고 있었지만.



‘또, 또, 괜히 걱정하시네. 이젠 안 그럴 때도 됐는데.’

‘……걱정은 개뿔이. 하여튼 절대 불가인 줄만 알고 있어라.’

‘괜찮다니까요. 비명횡사할 생각은 꿈에도 없습니다. 제가 미쳤어요? 이러는 것도 다 믿는 구석이 있어서 이러는 거지.’

‘믿는 구석이라니?’

‘이미 아시잖아요. 천주가 이렇게까지 절 원하는 이상 저놈들은 제 털끝 하나 못 건드립니다. 음, 뭐 약간 다칠 수는 있겠지만요.’

‘그건.’



그 의견에는 적천강으로서도 쉽게 반박할 수 없었다.

분명 숭산과 사천을 둘러싼 사건 이후부터, 남천마후를 비롯한 강적들은 진태경의 목숨을 취하는 것에 있어 상당히 소극적인 태도를 보였고 이 모든 추측은 감숙성에서의 전투로 확실해졌으니까.

그리고 흔들리는 스승의 모습에, 진태경은 마지막 쐐기를 박았다.



‘어차피 제가 어느 쪽을 맡건, 놈들은 가장 중요한 목적인 저를 따라올 겁니다. 그럴 바에는 제일 방비가 잘 되어 있는 서문을 맡는 게 나아요. 안 그렇습니까?’



처음부터 끝까지 구구절절 맞는 말이었고, 결국 적천강은 뜻을 꺾고 마지못해 북문으로 향할 수밖에 없었다.

하지만.

‘그러지 말았어야 했다.’

지금 이 순간. 적천강은 그때의 결정을 가슴 깊이 후회할 수밖에 없었다.

잘못된 판단이었다.

혈주의 무위는 그가 짐작한 범주를 훌쩍 뛰어넘는 수준이었고, 적천강이 어떤 반응을 보일지 알고 있던 진태경의 거짓말은 너무나도 천연덕스러웠다.

‘이대로는…… 녀석이 위험하다.’

앞서 모두의 눈앞에서 펼쳐진 저 일격은, 결코 살심(殺心)을 품지 않고서는 나올 수 없는 위력.

그렇기에 젊어진 육신과 달리, 여전히 늙은 마음을 지닌 스승은 조급해지는 자신을 느끼며 서쪽을 향해 신형을 돌려세웠다.

아니, 정확히는 그러려고 했다.

바로 다음 순간, 성벽 너머에서 송곳처럼 쏘아진 한 줄기의 예리한 살기(殺氣)를 느끼기 전까지는.

“어딜 그리 급하게 가시는가, 시주.”

나직한 음성.

그러나 그 안에 담긴 수 갑자의 공력은 북문 일대의 공간을 뒤흔들기에 충분했다.

일찍이 남만야수궁에서도 본 적 없는, 거대한 코끼리의 등 위에 우뚝 선 노승(老僧)이 발산하는 그 무시무시한 기파 역시도.

“시주가 이리 가 버리면, 빈승이 먼 길을 달려온 보람이 없지 않겠나.”

한없이 왜소한 체구와 지난 세월을 증명하는 자글자글한 주름들.

하지만 그에게서 뿜어져 나오는 존재감은 거인과도 같았고, 적천강은 이미 눈앞의 상대가 누구인지 직감하고 있었다.

노승, 아니 포달랍궁의 궁주인 달뢰라마가 저 수많은 병력을 이끌고 북문에 나타났다는 것이 어떤 의미인지도.

“……노렸군. 처음부터.”

불현듯 입술 사이로 흘러나온 침음성.

그리고 뒤이어 들려온 달뢰라마의 음성은, 불길한 짐작이 확신으로 굳혀지도록 만들기에 충분했다.

“열화문(烈火門)의 명맥은 끊어질 것이다. 바로 오늘 이 자리에서.”

그 순간.

부우우우우!

뿔피리 소리와 함께 밀려드는 포달랍궁의 군세를 보며, 적천강은 자신도 모르게 이를 악물었다.

으득.

새하얗게 물든 입술. 어느덧 살갗을 깊숙이 파고든 손톱 사이로는 그가 느끼고 있는 갈등 대신 뜨거운 핏물이 흘러내렸다.

아직 늦지 않았다.

가야 한다. 지금이라도.

자신의 제자에게. 진태경에게.

그러나.

“포, 포달랍궁이다! 놈들이 가세했다!”

“화살! 화살을 더 가져와라!”

“방어진을 구축하라! 죽는 한이 있더라도 물러서지 마라!”

“적 대협, 망설일 시간이 없습니다!”

사방에서 빗발치는 고함과 비명이 발목을 붙잡는다.

두려움과 결의. 혹은 믿음으로 가득 찬 눈동자들이 손을 잡아끌고 목을 조이고, 그와 함께 북문을 지키던 현천진인의 다급한 목소리가 귓가를 파고들었다.

‘만약 녀석이었다면, 그 아이였다면 어찌했을까.’

마음속 깊숙이 던지는 물음과 함께, 적천강은 질끈 눈을 감았다.

찰나의 그 짙은 어둠 속에서, 전날 제자와 나누었던 대화를 떠올렸다.



‘영웅 따위, 원한 적도 없습니다.’

‘상관없다. 영웅은 단지 원한다고 이루어지는 것이 아니니까. 세상이 네 녀석을 그리 부를 때 자격을 얻는 것이다.’

‘노야께서 대협이라고 불리시는 것처럼요?’

‘뭐라?’

‘방금 말씀하셨잖습니까. 구태여 대의를 좇지 않아도, 그저 발걸음이 향하는 대로, 바람이 부는 대로 나아갔음에도 어느샌가 대협이라고 불리게 되었다고.’

‘……!’



똑똑히 기억난다.

말문이 막혀 버린 자신을 향하던 그 환한 미소, 장난스러운 표정과 맑은 눈동자까지도.

그렇기에, 다른 그 무엇보다 두려웠을지도 몰랐다.

그 모습을 두 번 다시 볼 수 없을지도 모른다는 생각이 앞섰는지도 몰랐다.

하지만 아직도 적이 두렵냐는 스승의 뒤이은 물음에, 망설임 없이 고개를 끄덕인 제자는 이렇게 덧붙였었다.



‘그렇다 할지라도, 저는 그 두려움을 외면하지 않겠습니다.’



담담했고, 당당했다.

그리고 그날의 모든 것이, 앞서 적천강이 스스로에게 던진 물음에 대한 대답이었다.

화아아악.

일순간, 공간을 집어삼키는 거대한 열기.

천천히 들어 올려지는 눈꺼풀 너머로, 불그스름하게 달구어진 눈동자가 화염과도 같은 안광(眼光)을 토해 냈다.

허공을 가르며 쏘아지는 달뢰라마와 십이 밀승을 향해.

그리고 어느덧 나타난 두 기의 흑귀와, 그 너머에서 물밀듯이 밀려오는 적의 대군을 향해.

그그그극.

끔찍한 열기에 의해 일그러지는 공간 속, 불의 거인은 온 힘을 다해 포효했다.

“오라-!”

마치 온 세상을 불태울 듯이.

“노부가 바로 대 열화문의 십팔 대 문주, 화왕(火王) 적천강이니라!”

이 포효가, 자신의 제자에게 닿기를 바라며.
```

## Final English reading copy

```markdown
# Chapter 1105

Could it be because Xining had faced one foreign invasion after another for so many years?

The four walls surrounding Xining now ran a full ten ri in length, enclosing a vast area with a sturdiness rarely seen even in the Central Plains.

But everything had its pros and cons.

The walls had been reinforced little by little over time, making them effective at keeping out invaders. But that also meant there was more ground to defend.

The defenders had to find ways to keep in touch with one another across such vast distances.

They did so with war drums and flags stationed at various points.

But at least in this moment, the blood-red flash that suddenly erupted in the west was enough to render all of that useless.

*Fwoooosh.*

Would it look like this if dozens, hundreds of sunsets overlapped?

The world slowed. Countless eyes flew wide at the strange sight, impossible to describe.

The soldiers on a dozen or more watchtowers, beating their assigned war drums and waving their flags with all their strength.

The people hiding in Xining’s Inner City, clutching their families and peering through cracks in the doors.

The combined forces of the imperial troops and Murim warriors, fighting back the enemies surging toward them like waves—and even the Supreme Peak masters at the heart of their ranks, at the very front, cutting down enemy after enemy without pause.

And the moment every one of them felt an instinctive chill run up their spines—

*Pop.*

At last, the blood-red flash rising over the western wall swelled.

No—it exploded in a vivid, horrifying burst of red light.

*Rumble-rumble-rumble!*

The deafening roar made everyone’s ears ring.

The ground shook. The entire stone wall trembled.

Then a colossal shock wave surged over the western wall and crashed down on the people frozen like statues.

“Danger—!”

*KA-BOOOOM!*

The rushing wind swallowed someone’s single shout and swept across everything.

The North Gate was no different.

Dust and shattered rock flew through the air, mixed even with ownerless blades. Everyone ducked and threw themselves toward cover.

Everyone except one man, still holding the front line.

*Fwoosh—BOOM!*

Flames burst from a forcefully thrust punch, devouring the space around him.

Even the storm, like a natural disaster, bowed before its heat. Everything flying toward the defenders at the North Gate evaporated in an instant.

*Shhhhh.*

Ash drifted slowly away on the now-gentle breeze.

But the eyes of the man who had protected his allies from the unexpected threat—Fire King Jeok Cheongang—were more somber than ever.

*…What in the world was that?*

Though he held the chief seat among the Ten Kings, he had already reached a realm where he could stand shoulder to shoulder with the Three Saints.

That was why he could feel it with every inch of his skin, every one of his senses.

The immense power contained in that distant blood-red flash that had erupted in the west.

And if its shock wave had reached the North Gate, more than two hundred jang away, what state must the West Gate—the source of that strange phenomenon—be in?

*Blood Lord, how did you…?*

Jeok Cheongang bit his lip without realizing it.

The Blood Lord’s martial prowess had advanced unmistakably since their encounter at Mount Song. But what also weighed on his heart was the voice of someone he couldn’t stop thinking about.

*“I’ll take the West Gate.”*

Jin Taekyung.

When his Disciple had said that just before the battle, Jeok Cheongang had answered without a moment’s hesitation.

*“Absolutely not. Instead of spouting that nonsense, do one more complete circulation. And don’t go getting yourself stabbed just because you’re acting up.”*

*“My internal energy’s in great shape, and I can take a few stabs. So I’ll take responsibility for the West Gate.”*

*“I said no.”*

*“Why not?”*

*“You have to ask? That damned bastard has been mine for a long time. Today, I’ll finally collect the blood debt from that day.”*

Jeok Cheongang’s answer had been both true and untrue.

He did want revenge for Hong Dao, his old friend. But the more important reason was that the enemy’s main force, including the Blood Lord, was stationed at the West Gate.

His Disciple was a reckless brat who’d long since thrown manners out the window. But he was his one and only Disciple.

The person who had become more precious to him than anything else in the world. He couldn’t leave him alone in the most dangerous place.

Of course, Taekyung knew his Master far too well for Jeok Cheongang to hide that bashful concern behind roundabout words.

*“There you go worrying again. You don’t have to do that anymore.”*

*“Worry? Don’t be ridiculous. Just know that it’s absolutely out of the question.”*

*“I’ll be fine. I have no intention of dying a pointless death. Do you think I’m crazy? I’m doing this because I’ve got a good reason.”*

*“A good reason?”*

*“You know already. As long as the Lord of Heaven wants me this badly, those guys can’t lay a finger on me. Well, I might get a little hurt.”*

*“That…”*

Even Jeok Cheongang couldn’t easily argue with that.

Ever since the incidents surrounding Mount Song and Sichuan, powerful enemies—including the Southern Heaven Demon Empress—had been decidedly reluctant to take Jin Taekyung’s life. And the battle in Gansu had made all those suspicions certain.

Seeing his Master waver, Jin Taekyung drove in the final nail.

*“No matter which gate I take, they’ll follow me, since I’m their most important target. In that case, it’s better for me to take the West Gate. It’s the best-defended, isn’t it?”*

Every word he’d said had been right from beginning to end. In the end, Jeok Cheongang had no choice but to give in and head reluctantly to the North Gate.

But—

*I shouldn’t have done it.*

In this moment, Jeok Cheongang couldn’t help but deeply regret his decision.

He’d judged wrong.

The Blood Lord’s martial prowess far exceeded what he’d imagined, and Jin Taekyung’s lie had been so effortless, even though he knew exactly how his Master would react.

*At this rate… that boy’s in danger.*

The attack that had unfolded before everyone’s eyes could only have come from someone with the intent to kill.

So, though his body had grown young again, his heart was still that of an old man. Feeling himself grow impatient, Jeok Cheongang turned toward the west.

No—he was about to.

Until the next instant, when he sensed a sharp thread of killing intent shooting like a needle from beyond the wall.

“Where are you rushing off to, donor?”

The voice was low.

Yet the several jiazi of internal energy within it were enough to shake the entire area around the North Gate.

So was the immense aura emanating from the old monk standing tall atop a colossal elephant, unlike anything Jeok Cheongang had ever seen at the Nanman Beast Palace.

“If you leave like this, donor, all the way I’ve traveled will have been for nothing.”

His frame was tiny, his skin wrinkled with age.

But his presence was like that of a giant, and Jeok Cheongang already knew who he was.

He also knew what it meant that this old monk—the Dalai Lama, Palace Lord of the Potala Palace—had appeared at the North Gate leading all those troops.

“…So this was your plan. From the beginning.”

A low groan slipped from between his lips.

Then the Dalai Lama spoke, turning Jeok Cheongang’s ominous suspicion into certainty.

“The Fire Gate Clan’s line will end. Right here, today.”

At that moment—

*Bwaaaaaaa!*

As the Potala Palace forces surged toward him to the sound of a war horn, Jeok Cheongang gritted his teeth without realizing it.

*Crack.*

His lips went white. His nails dug deep into his skin, and hot blood ran between his fingers—not the conflict he felt.

It wasn’t too late yet.

He had to go. Even now.

To his Disciple. To Jin Taekyung.

But—

“P-Potala Palace! They’ve joined the battle!”

“Arrows! Bring more arrows!”

“Form a defensive line! Don’t retreat, even if it costs us our lives!”

“Sir Jeok, we don’t have time to hesitate!”

Shouts and screams from all sides held him in place.

Eyes filled with fear, resolve, or faith grabbed at his hands and choked at his throat. Along with them, the urgent voice of Perfected Being Hyeoncheon, fighting at his side at the North Gate, pierced his ears.

*What would he have done? That boy—what would he have done?*

With the question buried deep in his heart, Jeok Cheongang squeezed his eyes shut.

In that brief, profound darkness, he recalled the conversation he’d had with his Disciple the day before.

*“I never wanted to be a hero.”*

*“That doesn’t matter. You don’t become a hero just because you want to. You earn the right when the world calls you one.”*

*“Like people call you a Great Hero, Old Master?”*

*“What?”*

*“You just said it yourself. You didn’t set out to follow some great cause. You just went where your feet led you, where the wind took you, and before you knew it, people were calling you a Great Hero.”*

*“……!”*

He remembered it clearly.

The bright smile directed at him when he’d been left speechless. The playful expression. The clear eyes.

Perhaps that was what he feared more than anything else.

Perhaps the thought that he might never see that face again had come first.

But when Jeok Cheongang had asked Taekyung whether he was still afraid of the enemy, his Disciple had nodded without hesitation and added:

*“Even so, I won’t turn away from that fear.”*

Calm. Resolute.

And everything that had happened that day was the answer to the question Jeok Cheongang had just asked himself.

*Fwoooosh.*

In an instant, tremendous heat swallowed the space.

Beyond his slowly rising eyelids, eyes glowing red with heat poured out a gaze like flame.

Toward the Dalai Lama and the Twelve Secret Monks flying through the air toward him.

Toward the two Black Ghosts who had appeared, and the vast enemy army surging in behind them.

*Grnnnnk.*

As the space warped under the unbearable heat, the giant of fire roared with all his might.

“Come on!”

As if he meant to burn the whole world.

“This old man is Jeok Cheongang, the eighteenth Sect Leader of the great Fire Gate Clan—the Fire King!”

He hoped his roar would reach his Disciple.
```
