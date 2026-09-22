<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0624.txt",
      "sha256": "299c906846d266aa16ae4188b6be62ea0fce497653ffa1f9090c15689fba4b98",
      "bytes": 13315
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2bff224d0567bc849b969ca6673977ab86b70bcf4dd235d84b5eb8a7e017579a",
      "bytes": 1438
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0935525ca5e9db05317a58245bf31faa25ce4cdec90b67ac01faced137cfc8b1",
      "bytes": 193161
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "2836df84d8df952018d13afab2ec175a01c3ad0baf5f6d776551cc04cfcb0d4d",
      "bytes": 1206
    },
    {
      "path": "characters/Ju Gongsan.md",
      "sha256": "8f71cedbb811608b192f5e07c806d0b777eff21c9cd6569963e80df17c496602",
      "bytes": 900
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "b14469380fa64e81094f503c571f1ef53510d4bc986d1fa1f339d5ac03026bb4",
      "bytes": 988
    },
    {
      "path": "characters/Namho.md",
      "sha256": "eb6fedd96af48225f581e55fbe8f47120ce17b520ab3ccfb0e99ba765dc607eb",
      "bytes": 843
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "70dec0194f5a8850d0e8e3ae06fa4c82009f28c88938e68a2b87bdfb8c89e60e",
      "bytes": 899
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "fe56189b5ed9db5bcd4da47296ac021d85d96e3dafc775308b18e0b767fa89c2",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "7fd88e4c931bb68eb5fee261cbdc6e0492af28f7c453c35f90a443c0542c3f2c",
      "bytes": 957
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "348f490ff39f44a96ba15084e1b8e8115995070e13001cfc2e1a07ebde76b668",
      "bytes": 528
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "1b570aee0ec4b5a147759352ff4610634ab6f40d1dd91758dfcd81f2b4bc18bf",
      "bytes": 781
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e06aaabd2b498dc6afd21d1ecc11fa4d1bbb9b00e26ae51f0c949f6866c8bc0e",
      "bytes": 196872
    }
  ],
  "estimated_tokens": 11888
}
-->

# Durable State Update — Chapter 624

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 624. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 624. Profile updates may replace only one
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
  "chapter": 624,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 624,
    "continuity_sources": [624],
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
    "The Fire Dragon Pavilion is inside the Nanman Beast Palace's territory after entering without permission and accidentally setting fire to a protected pasture.",
    "Jin Taekyung's Flame Divine Palm intensifies the pasture fire, but his successive palm strikes eventually extinguish it.",
    "Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace and rides a long-bonded white tiger.",
    "Yayul Cheok is the Beast Miao King, lord of the Nanman Beast Palace, leader of the Miao people, and the lowest-ranked of the Ten Kings.",
    "Namho publicly identifies Jin Taekyung as the Blazing Flame Divine Dragon and Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance.",
    "Yayul Mok has ordered Jin Taekyung and the Fire Dragon Pavilion to follow him after learning they belong to the Murim Alliance.",
    "Nanman beast-riders have arrived and defer to Yayul Mok as their Young Palace Lord."
  ],
  "continuity_sources": [
    623
  ],
  "open_questions": [
    "How will the Nanman Beast Palace respond to the Fire Dragon Pavilion's trespass and destruction of the pasture?",
    "Why is Yayul Mok's arrival and authority significant to the Fire Dragon Pavilion's mission in Nanman?"
  ],
  "safe_through": 623,
  "temporary_decisions": [
    "Use Yayul Mok for 야율목 and Yayul Cheok for 야율척.",
    "Use Young Palace Lord for 소궁주."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 표국     | **Escort Bureau**                            |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 태원     | **Taiyuan**            |
| 소저      | **Young Lady**                                                  |
| 주공산 | **Ju Gongsan** | Former head and founder of the Yongbong Escort Bureau. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 구주팔황 | **Nine Provinces and Eight Wastes** | Literary geographic phrase appearing in a wuxia novel title. |
| 사해오호 | **Four Seas and Five Lakes** | Traditional geographic phrase used with the Nine Provinces and Eight Wastes. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 표왕 | **Escort King** | Epithet of Ju Gongsan. |
| 수강 | **Palm Force** | Force generated through a palm technique. |
| 외당 | **Outer Hall** | The Tang Clan's outer hall area. |
| 내당 | **Inner Hall** | The Tang Clan's inner hall area. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 제시 | **Jesse** | The U.S. Secretary of State, introduced by first name. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 천마표국 | **Heavenly Demon Escort Bureau** | A Sichuan group whose arrival preceded the Yeongin massacre; all members were later found dead from venom. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 거한 | 사마표 | Subordinate addressing the Black Dragon Demon Gate Young Sect Leader | Young Sect Leader | Crude and deferential | Uses 소문주 in short, childlike replies. |
| 사마표 | 거한 | Young Sect Leader addressing his giant subordinate | This fellow | Informal and patronizing | Refers to him as 이 녀석 while assigning him responsibility for Do Sangho's death. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 송일섬 | 사마표 | fellow_pavilion_member_to_hostile_fellow_member | you | hostile and casual | Song Ilseom discusses fighting Sama Pyo and answers him while preparing to move away. |
| 사마표 | 송일섬 | fellow_pavilion_member_to_hostile_fellow_member | you | controlled and antagonistic | Sama Pyo responds to Song Ilseom's accusations and proposes moving aside to fight. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 622
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Ju Gongsan.md

# Ju Gongsan (주공산)

- **Safe through:** Chapter 622
- **Aliases:** Escort King
- **Role:** Founder and former head of the Yongbong Escort Bureau; during the Great Faction War, he was a wandering escort who refused to surrender a pregnant woman of the Guangdong Chen Family to the Demonic Cult after accepting her escort fee, carried her from Guangdong through Jiangxi and Hubei to Henan over two years, and became known as the Escort King; he later founded an escort bureau in his hometown of Shaanxi and died from internal injuries sustained during the war.
- **Personality:** Remarkably skilled, chivalrous, principled, and unwavering in his obligations.
- **Voice:** Not established.
- **Relationships:** Ju Hogun was his only blood child and successor as head of the Yongbong Escort Bureau; Ju Hwaran is his granddaughter.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 623
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, and an experienced Nanman escort guide with route knowledge from the Escort King's records.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 623
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 622
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 622
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 622
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 622
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 623
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace and a spear-wielding warrior who rides a white tiger.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and lord of the Nanman Beast Palace; his white tiger is a long-bonded companion; he orders Jin Taekyung and the Fire Dragon Pavilion to follow him after the pasture fire.

## Korean source

```text
＃624화



주화란이 알려 주길, 그녀의 조부인 표왕 주공산은 남만야수궁에 관하여 이런 말을 남겼다고 했다.



‘남만은 하나의 왕국이나 다름없으며, 남만야수궁은 다섯 개의 현읍을 아우르는 거대한 목장이다.’



과거 사해오호와 구주팔황을 주유했던 표왕의 말은 옳았다.

남만야수궁이 직접 다스리는 영역은 다섯 개 현읍에 이를 만큼 실로 광활했고, 면적만 따졌을 때는 중원의 구파일방이나 오대세가도 남만야수궁에 미치지 못할 정도였다.

‘직접 지배와 간접 지배의 차이라고 해야 하나.’

중원의 주인은 천자지만, 남만의 경우에는 남만야수궁이 최고 존엄이다.

이런 실정이니 무력으로 정파의 명문 대파를 앞지른다고 할 수는 없어도 영향력은 훨씬 앞설 수밖에 없었다.

다만 표왕이 남긴 말 중 틀린 부분이 있다면…….

‘목장이 아니라 사파리겠지.’

그만큼 이토록 다양한 동물과 식물, 그리고 기온과 지형이 뒤죽박죽인 곳은 처음이었다.

야율목과 그의 수하들을 따라 목초지를 지나고, 밀림을 지나 산과 강을 넘다 보니 혀를 내두를 수밖에 없었다.

“아니, 뭔 날씨가 이따위야?”

내 중얼거림에 오른편에서 말을 달리고 있던 주화란이 입을 열었다.

“한 개의 산에 계절이 있고, 십 리를 가면 기후가 다르다(一山有四季, 十里不同天). 남만의 변화무쌍함을 잘 표현하는 말이죠.”

“직접 겪어 보니 아니라고는 말 못 하겠네요. 주 소저는 어떻게 이런 곳으로 표행 올 생각을 했습니까?”

“저도 이 정도일 줄은 몰랐어요. 아버지를 따라 표행을 온 적이 있긴 하지만, 지금처럼 남만 깊숙이 들어가는 건 처음이거든요.”

두꺼운 털가죽을 어깨에 두른 채 싱긋 웃는 주화란의 입술 사이로 새하얀 입김이 뿜어진다.

남만이라고 하면 밀림이라는 인식이 강하다. 나 역시 여느 중원인들처럼 그렇게 생각했다.

하지만 이 지랄 맞은 땅은 놀랍게도 한대와 온대, 아열대에 열대기후까지 마치 복도식 다세대 아파트처럼 옹기종기 모여 살고 있었다.

“이 정도면 거의 뭐, 저주받은 땅인데.”

“……거, 말조심 좀 하라니까.”

현재 위치상 내 오른쪽이 주화란이라면 왼쪽을 차지한 건 남호였다.

야율목의 수하와 함께 흑표(黑豹)에 올라타 달리고 있던 늙은 은영각 요원은, 나뭇가지를 피하기 위해 잔뜩 몸을 움츠린 와중에도 나를 향해 한껏 눈을 부라렸다.

“자네 말을 이들이 듣기라도 하면 참 좋아하겠군. 안 그런가?”

“뭐 어떻습니까, 사실인데. 그리고 어차피 한어(漢語)로 말한 거라 알아듣지도 못해요.”

그때 몇 장 앞에서 달려가고 있던 야율목이 불쑥 입을 열었다.

“그 입을 좀 다물어 줬으면 하는데.”

“……한어네.”

“……한어여?”

어케 했누.

화투판에서 밑장 빼다가 걸린 타짜가 된 기분이다.

어눌하지만 분명한 한어를 구사하는 야율목의 모습에 남호와 의미심장한 눈빛을 교환한 내가 물었다.

“혹시 한어 배웠냐?”

“조금. 흥미가 없어 금방 때려치웠지만.”

“아하. 조금? 그마저도 금방 때려치웠어?”

기대감이 실린 물음에 야율목이 딱딱한 표정으로 대답했다.

“그래도 어렵지 않게 알아들을 정도는 된다. 예를 들자면 저주받은 땅 같은 단어라든지.”

“…….”

“곧 도착하면 이 저주받은 땅을 벗어날 수 있으니, 그때까지만이라도 조용히 해 줬으면 좋겠군.”

이렇게까지 나오니 뭐라 할 말이 없다. 조용히 입을 다문 내 모습에 남호가 현자처럼 웃으며 말을 건넸다.

“어이고, 잘했네. 잘했어. 자네의 활약 덕분에 남만야수궁과 무림맹이 아주 손쉽게 손을 잡을 수 있게 되겠구먼.”

“은근슬쩍 먹이시네. 그래도 좋은 소식을 들었잖습니까.”

“암천에게는 좋은 소식이겠지. 동맹을 제안하려고 온 무림맹 제일의 후기지수가 남만야수궁의 소궁주에게 할아버지의 존재 유무를 묻고, 남만을 저주받은 땅이라고 칭했으니까. 그러고 보니 자네 혹시 암천인가?”

“암천처럼 보이십니까?”

“아니. 하지만 이제는 약간 의구심이 드는 건 사실일세. 헛소리는 그만두고 내가 모르는 그 좋은 소식이 뭔지나 말해 보게.”

나는 자신감 있게 대답했다.

“이제 곧 남만야수궁에 도착한대요.”

“이런 니미럴 거…….”

“아니, 욕하진 마시고.”

“욕이 안 나오게 생겼나, 지금? 태산인지 금수강산인지 하는 아귀 새끼도 문제지만, 내가 볼 때는 각주인 자네도 만만치 않아. 도착 전에도 이 모양 이 꼴인데, 막상 야수묘왕과 대면했을 때 자네 특유의 그 지랄병이라도 도지면 그땐 어쩔 셈인가?”

“지랄병이라니, 말이 심하시네. 제가 막 나가는 것처럼 보여도 누울 자리는 보고 발을 뻗습니다. 그리고 태산이는 조금 모자란 부분이 있는 것 같아도 큰 전력감이고요. 때가 되면 제 몫을 톡톡히 해낼 테니 너무 걱정 안 하셔도 됩니다.”

그때, 등 뒤에서 구슬픈 짐승의 울음소리와 함께 다급한 외침이 울려 퍼졌다.

구워어어어!

“소, 소궁주! 이 덩치 큰 한족 놈이 제 곰의 귀를 물어뜯고 있습니다!”

“태산이! 곰고기!”

“조장니임!”

“태산! 멈춰! 식사 멈춰!”

“당장 저 한족 놈을 붙잡아라!”

달리는 와중에 잠시 고개를 돌려 등 뒤의 상황을 살핀 내가 남호를 향해 한 마디를 덧붙였다.

“물론 식탐이 문제긴 합니다.”

“염병할. 식탐도 식탐 나름일세. 저게 짐승이지 사람 새낀가?”

뭐라 부정할 수가 없다. 나도 슬슬 태산이 인간과 짐승의 경계 어딘가쯤에 있는 미지의 존재가 아닐까, 하는 의심이 들고 있었으니까.

‘화룡각. 이대로 괜찮은가.’

탑승하고 있던 곰의 귀를 잘근잘근 씹고 있는 태산과 수하의 동물 폭력을 저지하는 사마표.

그리고 고통으로 울부짖으며 승차 거부를 온몸으로 표현하는 곰의 모습을 지그시 바라보고 있던 그때, 야율목이 한숨처럼 입을 열었다.

“도착이다. 제발 이제 그만하고 썩 내려라.”

녀석의 말은 사실이었다. 어느새 공기 중에 감돌던 한기는 씻은 듯이 사라지고, 습하고 후텁지근한 열기와 빽빽한 열대 우림이 우리를 기다리고 있었다.

그리고 그 너머에…….

구구구구궁.

나무줄기로 뒤덮인 철문이 열리며, 수많은 전각과 가옥이 모습을 드러냈다.

그것은 중원에서 수만 리나 떨어진 남만, 그곳에서도 가장 깊고 은밀한 곳에서 자신들만의 왕국을 세운 남만야수궁(南蠻野獸宮)의 일면이었다.



* * *



태원진가를 비롯하여 어느 정도 규모가 있는 가문, 혹은 문파라면 외당(外堂)과 내당(內堂)으로 분류하기 마련이다.

문파가 적들에 의해 공격당할 때를 대비하여 안팎으로 조직도를 구축하고, 나름의 방어선을 만들어 놓은 것이다.

그러나 지금 눈에 들어오는 남만야수궁의 외당은 일반적인 문파의 규모를 훨씬 뛰어넘었다.

‘이건 거의 도시 수준인데?’

표왕이 괜히 왕국이나 다름없다고 한 게 아니었다.

중원에서는 쉽게 찾아볼 수 없는 희한한 형태의 가옥과 수많은 건축물이 눈을 사로잡았다.

한쪽에서는 시장이라도 열렸는지 한창 흥정이 이루어지는 중이고, 예닐곱 살쯤으로 보이는 꼬마 아이들이 새끼 맹수와 웃으며 뛰어놀고 있다.

수많은 사람과 건물 그리고 각종 상업과 제조가 이루어지는 모습들.

마치 소국의 도성(都城)과도 같은 풍경에 혁무진의 입은 다물어질 줄을 몰랐다.

“와, 저도 나름대로 많은 걸 보고 겪었다고 생각했는데, 여기는 진짜 상상 이상입니다. 조장님, 저거 보이세요? 진짜 신기하네요.”

“그러네. 근데 가장 신기한 건 따로 있는데. 뭔지 알려 줄까?”

정신없이 주위를 둘러보던 혁무진이 물었다.

“가장 신기한 게 뭔데요?”

“우리.”

“아.”

“대충 감 잡았으면 입 좀 다물고, 그만 좀 두리번거려라. 가뜩이나 시선 쏠리는데.”

당장 눈에 보이는 거주지와 그 규모로 짐작해 보면, 외당에 살아가는 이들의 가호(家戶)만으로도 어림잡아 수천은 될 듯싶다.

더군다나 남만야수궁은 남만에서도 가장 깊숙한 곳에 자리 잡은 동시에 외지인의 출입을 철저히 금하는 곳이니 그들에 비하면 한 줌밖에 되지 않는 우리가 눈에 띄는 것은 당연했다.

아마 한족을 처음 본 이들의 숫자도 적지 않을 터.

이런 상황에서 호들갑을 떨어 봤자 좋을 것이 없다. 특히나 이런 분위기 속에는.

“저게 한족이야? 우리랑 비슷하면서도 좀 희한하게 생겼는데.”

“쉿. 눈도 마주치지 마. 얼마 전에 북쪽 땅에서 일어난 이야기 못 들었어? 웬 한족 놈들이 묘족 마을을 몰살시켰다잖아. 저놈들도 한 패거리일지도 몰라.”

“물론 듣기야 했지. 하지만 제깟 놈들이 여기서 뭘 어쩌겠나? 딱 봐도 소궁주님께 잡혀 온 것 같은데.”

“내가 보기에는 포로로 잡힌 것 같지는 않은데…… 여하간 한족 놈들이 여기까지 기어들어 오다니, 도대체 무슨 일이지?”

생김새나 복장만큼이나 언어도 갖가지다.

그들의 말을 알아들을 수 있는 나와 주화란, 그리고 남호는 낮은 목소리로 말을 주고받았다.

“이거, 벌써 소문이 퍼진 모양인데요?”

“제가 알아들을 수 있는 건 묘족과 백족의 말뿐이긴 한데, 전체적으로도 분위기가 심상치 않네요.”

“고작 며칠 전에 일어난 사건이지 않나. 부족끼리의 분쟁은 일 년에도 수십 차례씩 일어나지만, 외지인에 의한 사건은 십 년에 한 번 벌어질까 말까 한 곳이 바로 남만일세. 소문이 빠를 수밖에.”

좋은 이미지를 쌓아 놨다면 어딜 가도 환영받았겠지만, 지금으로부터 약 한 달 전 일어난 묘족 마을 학살 사건은 그 정반대의 결과를 낳았다.

눈치껏 몸을 움츠린 혁무진이 투덜거렸다.

“하여간에 미친놈들. 천마표국인지 뭔지. 왜 하필 남만에서 그런 천인공노할 짓거리를 해서…….”

“글쎄. 왜 그랬을까.”

불쑥 입을 연 사마표가 재미있다는 투로 말을 이었다.

“왜 하필 지금. 그런 일이 벌어졌을지는 더 생각해 봐야지. 아마 저 친구도 전부터 나와 비슷한 생각을 하고 있을 것 같은데. 그렇지 않나?”

사마표의 물음에 송일섬이 담담하게 대답했다.

“맞지만 아니다.”

“……맞지만 아니라는 게 무슨 뜻이지?”

“내 생각과는 별개로 네놈과 말을 섞기 싫다는 뜻이지. 그러니 말 걸지 마라.”

“보기보다 옹졸하군. 뭐, 그렇다면야.”

일순 경고의 의미를 실어 바라본 내 눈빛에, 눈썹을 슬쩍 치켜올린 사마표가 먼저 한 걸음 물러났다.

하지만 저놈들 간의 감정싸움과는 별개로, 사마표가 제시한 의문은 나 역시 이동하는 내내 마음에 품고 있던 것이었다.

‘천마표국이라.’

우연인지, 필연인지. 참극이 벌어진 시기가 참으로 공교롭다.

정답이 무엇인지에 관해서는 아직 속단하기에는 이르지만.

‘그래도 이 정도면 최악의 상황은 면한 셈인가?’

사실 야율목과 만나기 전까지만 해도 조금. 아니, 매우 우려되긴 했다.

이미 암천의 흉계가 시작되고 남만야수궁에 지옥도가 펼쳐져 있을까 봐.

물론 한족이라는 브랜드 이미지가 친일 기업 수준으로 떡락하긴 했지만, 아직 일이 벌어지지 않았다는 것만으로도 충분하다.

‘욕 좀 먹더라도 이게 훨씬 낫지.’

내심 중얼거리던 그때. 알 수 없는 기시감을 느낀 나는 문득 고개를 들었다.

‘이건.’

다른 이들은 몰라도 나는 느낄 수 있었다.

눈치채지 못할만큼 자연스럽게 무거워진 공기의 흐름을.

숱한 소음과 인기척 너머로 거칠게 뿜어져 나오는 누군가의 기세를.

그리고 그 기세를 쫓아내 시선이 움직인 방향의 끝에, 넝쿨로 뒤덮인 계단 위에 앉은 한 노인이 있었다.

훤히 드러난 상체와 근육질의 거한.

나는 노인이 입을 열기도 전에, 그의 정체를 깨달을 수 있었다.

‘야수묘왕(野獸苗王).’

바로 그였다.
```

## Final English reading copy

```markdown
# Chapter 624

Ju Hwaran told me that her grandfather, the Escort King Ju Gongsan, had left these words about the Nanman Beast Palace:

> “Nanman is practically a kingdom, and the Nanman Beast Palace is a vast ranch encompassing five counties.”

The Escort King, who had once traveled throughout the Four Seas and Five Lakes and the Nine Provinces and Eight Wastes, had been right.

The territory directly ruled by the Nanman Beast Palace was truly vast, stretching across five counties. In terms of sheer area, even the Nine Sects and One Gang or the Five Great Families of the Central Plains could not compare to the Nanman Beast Palace.

*Is it a matter of direct rule versus indirect rule?*

The ruler of the Central Plains was the Son of Heaven, but in Nanman, the Nanman Beast Palace held supreme authority.

Under such circumstances, the palace might not have been able to surpass the great orthodox factions of the Central Plains in martial power, but its influence was inevitably far greater.

However, if there was one part of the Escort King’s words that was wrong…

*It isn’t a ranch. It’s a safari.*

I had never seen a place with such a chaotic mix of animals, plants, temperatures, and terrain.

Following Yayul Mok and his subordinates, we passed through grasslands and jungles, crossing mountains and rivers. Before long, I could only shake my head in disbelief.

“What the hell is wrong with this weather?”

Ju Hwaran, who was riding on my right, answered my mutter.

“One mountain holds four seasons, and ten li bring a different sky.[^1] It’s a saying that describes Nanman’s unpredictable nature quite well.”

“After experiencing it firsthand, I can’t exactly disagree. Young Lady Ju, how did you ever think of accepting an escort job to a place like this?”

“I didn’t know it would be this extreme, either. I have accompanied my father on escort journeys before, but this is my first time going so deep into Nanman.”

Ju Hwaran smiled faintly, a thick fur pelt draped over her shoulders. White breath spilled from between her lips.

Most people associated Nanman with jungles. I had thought the same, just like any other person from the Central Plains.

But this damned land had somehow crammed frigid, temperate, subtropical, and tropical climates together as neatly as apartments lined up along a hallway.

“At this point, it’s practically cursed land.”

“……Watch your mouth.”

If Ju Hwaran occupied my right, then Namho had taken the left.

The elderly Hidden Shadow Pavilion agent was sharing a black panther with one of Yayul Mok’s subordinates. Even while hunching down to avoid branches, he glared at me fiercely.

“I’m sure they’d love to hear you say that. Don’t you think?”

“So what? It’s true. And I’m speaking in Han Chinese, so they can’t understand me anyway.”

At that moment, Yayul Mok, who was riding a few dozen feet ahead of us, suddenly spoke.

“I’d prefer it if you kept that mouth of yours shut.”

“……That’s Han Chinese.”

“……Han Chinese?”

*How the hell did he pull that off?*

I felt like a cardsharp caught dealing from the bottom of the deck during a card game.

Yayul Mok spoke Han Chinese haltingly, but clearly. I exchanged a meaningful glance with Namho before asking,

“Did you study Han Chinese?”

“A little. I lost interest and quit soon afterward.”

“Oh, really? A little? And even that you quit right away?”

At my expectant question, Yayul Mok answered with a stiff expression.

“I know enough to understand it without difficulty. For example, words like ‘cursed land.’”

“…….”

“We will soon arrive, and then you can leave this cursed land. Until that time, I would appreciate it if you remained quiet.”

He had made his point so thoroughly that I had nothing to say.

As I quietly shut my mouth, Namho smiled like a sage and spoke to me.

“Well done. Very well done. Thanks to your efforts, the Nanman Beast Palace and the Murim Alliance should be able to join hands with ease.”

“You’re slipping that in so subtly. Still, you did hear some good news.”

“It’s good news for Dark Heaven. The Murim Alliance’s foremost young prodigy came here to propose an alliance, asked the Young Palace Lord of the Nanman Beast Palace whether he had a grandfather, and called Nanman a cursed land. Come to think of it, are you perhaps a member of Dark Heaven?”

“Do I look like a member of Dark Heaven?”

“No. But I have to admit, I’m beginning to have my doubts. Enough nonsense. Tell me about this good news I supposedly don’t know.”

I answered confidently.

“They say we’ll be arriving at the Nanman Beast Palace soon.”

“God damn it…”

“Hey, don’t swear.”

“Do I look like I can help swearing right now? That A-Gwi bastard they call Taishan—or Geumsugangsan or whatever his name is—is one problem, but in my opinion, you’re no less troublesome, Pavilion Master. You’re already acting like this before we arrive. What are you going to do if your particular brand of insanity flares up when you actually come face-to-face with the Beast Miao King?”

“‘Insanity’ is a bit harsh. I may look like I act without thinking, but I know where to put my feet before I stretch out my legs. And Taishan may be lacking in certain areas, but he’s a major asset. When the time comes, he’ll pull his weight. You don’t need to worry so much.”

At that moment, a mournful animal cry and a frantic shout rang out from behind us.

“Grrrrrrr!”

“Y-Young Palace Lord! This huge Han bastard is biting my bear’s ear off!”

“Taishan! Bear meat!”

“Captain!”

“Taishan! Stop! Stop eating!”

“Seize that Han bastard immediately!”

I briefly turned my head to check what was happening behind us as we rode, then added one more comment to Namho.

“Of course, his appetite is a problem.”

“For fuck’s sake. There’s appetite, and then there’s appetite. Is that thing a beast or a person?”

I could not deny it.

Lately, I had begun to wonder whether Taishan was some unknown creature hovering somewhere between human and beast.

*Fire Dragon Pavilion. Are we really going to be all right like this?*

Taishan was munching contentedly on the ear of the bear he had been riding, while Sama Pyo tried to stop his subordinate’s animal abuse.

The bear, meanwhile, howled in pain and expressed its refusal to carry passengers with every inch of its body.

As I watched the scene, Yayul Mok spoke with a sigh.

“We’re here. For the love of all that’s holy, stop it and get down this instant.”

He was telling the truth.

The chill that had lingered in the air had vanished without a trace. In its place was humid, oppressive heat, along with a dense tropical rainforest waiting for us.

And beyond it…

*Rumble, rumble.*

An iron gate covered in vines and tree trunks opened, revealing countless pavilions and houses.

This was one glimpse of the Nanman Beast Palace, which had built a kingdom of its own in Nanman, tens of thousands of li from the Central Plains—and in the deepest, most secluded part of that land.

* * *

Any family or sect of a certain size, including the Jin Family of Taiyuan, generally divided its organization into an Outer Hall and an Inner Hall.

They built an organizational structure both inside and outside their main grounds, creating their own lines of defense in preparation for an attack by their enemies.

However, the Outer Hall of the Nanman Beast Palace now before my eyes far exceeded the scale of any ordinary sect.

*This is practically a city.*

The Escort King had not called it practically a kingdom for no reason.

Unusual houses and countless buildings unlike anything commonly seen in the Central Plains caught my attention.

A market appeared to be in full swing on one side, with people haggling energetically. Nearby, children who looked to be six or seven years old laughed and ran around with young beasts.

There were countless people and buildings, along with all kinds of commerce and manufacturing.

The scene looked like the capital of a small nation, and Hyuk Mujin’s mouth hung open in amazement.

“Wow. I thought I had seen and experienced quite a lot, but this place is truly beyond my imagination. Captain, do you see that? It’s amazing.”

“It is. But there’s something even more amazing. Want to know what it is?”

Hyuk Mujin, who had been looking around frantically, asked,

“What’s the most amazing thing?”

“Us.”

“Ah.”

“Now that you’ve gotten the idea, shut your mouth and stop gawking. We’re already attracting enough attention.”

Judging by the settlement immediately visible before us and its sheer size, the Outer Hall alone probably contained several thousand households.

Moreover, the Nanman Beast Palace was located in the deepest part of Nanman, and outsiders were strictly forbidden from entering. Naturally, we stood out like a handful of pebbles among them.

There were probably quite a few people seeing Han Chinese for the first time.

Making a fuss under these circumstances would not do us any good. Especially not in an atmosphere like this.

“Are those Han Chinese? They look similar to us, but kind of strange.”

“Shh. Don’t even make eye contact. Didn’t you hear what happened in the northern lands recently? Apparently, a bunch of Han Chinese slaughtered an entire Miao village. Those men might be part of the same group.”

“Of course I heard about it. But what could those bastards possibly do here? They look like the Young Palace Lord captured them.”

“I don’t think they look like prisoners… Either way, what could possibly have brought Han Chinese all the way here?”

Their languages varied just as much as their appearances and clothing.

Ju Hwaran, Namho, and I were able to understand what they were saying, so we spoke quietly among ourselves.

“Looks like the rumors have already spread.”

“I can understand only the Miao and Bai languages, but even so, the atmosphere here seems tense.”

“It happened only a few days ago. Conflicts between tribes occur dozens of times a year, but an incident caused by outsiders might happen once in a decade, if that. Of course the rumors spread quickly.”

If we had built up a good reputation, we might have been welcomed wherever we went. But the massacre of the Miao village about a month earlier had produced the exact opposite result.

Hyuk Mujin hunched down tactfully and grumbled.

“Those lunatics. The Heavenly Demon Escort Bureau, or whatever they were called. Why did they have to commit such an atrocious crime in Nanman of all places…?”

“I wonder. Why did they?”

Sama Pyo suddenly spoke, continuing in an amused tone.

“We need to think harder about why something like that happened now, of all times. I imagine that fellow has been thinking along the same lines as I have. Isn’t that right?”

Song Ilseom answered calmly.

“Yes, but no.”

“……What does ‘yes, but no’ mean?”

“It means that regardless of what I think, I don’t want to exchange words with you. So don’t talk to me.”

“You’re more petty than you look. Well, if that’s how it is.”

Sama Pyo raised one eyebrow slightly after my warning gaze met his, then took a step back first.

But regardless of the feud between those two, the question Sama Pyo had raised was one I had also been carrying with me throughout the journey.

*The Heavenly Demon Escort Bureau.*

Whether by coincidence or design, the timing of the tragedy was extremely suspicious.

It was still too early to jump to conclusions about the answer.

*Still, does this mean we’ve managed to avoid the worst-case scenario?*

To be honest, I had been somewhat worried before meeting Yayul Mok.

No. I had been very worried.

I had feared that Dark Heaven’s scheme had already begun and that Nanman Beast Palace had become a living hell.

Of course, our image as Han Chinese had plummeted to the level of a pro-Japanese corporation, but the mere fact that nothing had happened yet was more than enough.

*Even if we have to take some abuse, this is much better.*

I was muttering inwardly when I suddenly raised my head.

A strange sense of déjà vu had come over me.

*This is…*

Others might not have noticed it, but I could feel it.

The flow of the air had grown heavy so naturally that no one could detect the change.

Beyond the countless noises and signs of people nearby, someone’s aura was pouring out roughly.

My gaze followed that aura, eventually reaching an old man seated on the vine-covered steps.

His upper body was completely bare, revealing a massive, muscular frame.

I realized who he was before he even opened his mouth.

*The Beast Miao King.*

It was him.

[^1]: A traditional saying describing Nanman’s rapid shifts in climate and weather.
```
