<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0456.txt",
      "sha256": "19260db7db64ef749307deb8b566502356e15d6c6ab63c4f2012e37f1e416311",
      "bytes": 13161
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "de011fd9fe2f773cc25fabc569c5e955a69061c5fbcaa77269b61ff45820513c",
      "bytes": 3340
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "71c096f173283804132896bb203b8bbcc1ddb81d6ad3daf9ca9d3e570c348f32",
      "bytes": 149218
    },
    {
      "path": "characters/Baek Woo.md",
      "sha256": "30af0418e3005f6d4c2f61bc731d40a5ded094b26b740fa25de7b39a6caa981a",
      "bytes": 811
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "d1b21afa6e1630028668ebb00e6c24a2b8f6fad889714f6dd5fff14942b81589",
      "bytes": 944
    },
    {
      "path": "characters/Dongting Fisherman.md",
      "sha256": "177dce39557de06b52c92415fa3862150287119b8adcdd0955432ea16871cb60",
      "bytes": 722
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "52928018f17c49926ab83b6e436579cbdc22b2dccbc421b3d5fa4aa8df48da16",
      "bytes": 662
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "f55e95ad926b7d23adc384d07be64ae5efcaf02bbf85802f19d5b48d18aaa437",
      "bytes": 1108
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "130d484b419755c1b4013f9444bfdc6e20ca847b35304a63c83c7015000b89d3",
      "bytes": 864
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "4ecbac252acb9f62a87976cf88c0a76a1b2d1954241b1316f6f75944bdd6f9c1",
      "bytes": 888
    },
    {
      "path": "characters/Zhuge Gyun.md",
      "sha256": "901b81310370c2097e240a06b190af16e4584a8c01fe478dc75ce75b45bc3580",
      "bytes": 676
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "9718c252fb417d2b5cd87604507252e001b190ea2e996a8ee7f800a535d402d1",
      "bytes": 144135
    }
  ],
  "estimated_tokens": 12039
}
-->

# Durable State Update — Chapter 456

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 456. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 456. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 456,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 456,
    "continuity_sources": [456],
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
    "Taekyung accepted Quest Another Chaos to uncover the truth behind the Hubei incidents and find the culprit.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung's investigation.",
    "The shared symbols between the Arch Lich's magic circle and Dark Heaven's formations remain unexplained.",
    "The Sea Serpent Society and Donghu Stronghold were destroyed, with more than a thousand casualties, while the perpetrators' whereabouts remain unknown.",
    "The Dongting Fisherman is still believed to be in Hubei Province and remains a possible Dark Heaven member.",
    "Wudang is responding to an unidentified killer demon responsible for more than thirty deaths, including twenty pilgrims on Mount Wudang.",
    "The Skeleton King's undead identity remains concealed, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "Taekyung's party is at the Zhuge Clan after reaching Zaoyang, and Taekyung plans to stop at Dongting Lake before departing.",
    "The captured Three Fiends is a former-generation great fiend and Supreme Peak Dark Heaven subordinate whom Taekyung intends to keep alive for transport to Henan.",
    "Qingxia Hall is an influential Hubei social club formed by powerful families' children, and Ju Wongong is its exiled young master who defers to Prince Shangshan while Honglan conceals her real name.",
    "Beggars' Sect and Lower District Sect intelligence have not located the people responsible for the Hubei massacres."
  ],
  "continuity_sources": [
    455,
    454
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, and why was no Moving Formation trace left behind?",
    "Is the Dongting Fisherman a member of Dark Heaven, and what role did he play in the Hubei atrocities?",
    "Is the killer demon attacking Wudang connected to Dark Heaven?",
    "What evidence is contained in Lee Jungryong's holographic recorder, and what are the terms of the Peace Guild–Wizard Guild agreement?"
  ],
  "safe_through": 455,
  "temporary_decisions": [
    "Render 황철 as Hwang Cheol, 도립군 as Do Ripgun, 광수도귀 as Mad Water Saber Demon, 파랑호 as Wave Fox, 동정호 as Dongting Lake, and 사천혈사 as Sichuan Blood Tragedy.",
    "Render 살귀 as killer demon, 일급 낭인 as First Rate wandering martial artist, 삼괴 as Three Fiends, 대마두 as great fiend, and 마군 as Demon Lord.",
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor.",
    "Render 주원공 as Ju Wongong, 대죽산표국 as Daejuksan Escort Bureau, 형문검가 as Hyungmun Sword Family, 응성상회 as Eungseong Merchant Association, 천룡인 as Celestial Dragon, 사인교 as four-person sedan chair, 홍란 as Honglan, 가기 as singing courtesan, and 구족 as the nine branches of kin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 제갈균    | **Zhuge Gyun**     |
| 백우     | **Baek Woo**       |
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 진룡대    | **Jin Dragon Squad**             |
| 하오문    | **Lower District Sect**          |
| 소림     | **Shaolin**                      |
| 무당파    | **Wudang**                       |
| 암천     | **Dark Heaven**                  |
| 제갈세가   | **Zhuge Clan**                   |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 신법     | **movement technique**                           |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 대주     | **Squad Leader** / **Commander**             |
| 부대주    | **Vice Squad Leader** / **Deputy Commander** |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 몬스터     | **monster**           |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 본가      | **our family / this family**                                    |
| 동정어옹 | **Dongting Fisherman** | Publicly condemned the Yangtze River Channel League and disappeared three days before this chapter. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 적토마 | **Red Hare** | Famous horse used in Hyuk Mujin's exaggerated comparison. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 은자 | **silver nyang** | Silver currency unit. |
| 대태원진가 | **great Jin Family of Taiyuan** | Formal exalted reference to the Jin Family of Taiyuan. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 녹옥불장 | **Green Jade Buddha Staff** | Ancient Shaolin sacred treasure carried by Hong Dao. |
| 대성 | **Great Completion** | Completion stage of a martial technique. |
| 신기묘룡 | **Divine Marvel Dragon** | Epithet of the Zhuge Clan's Lesser Family Head. |
| 기관진식 | **mechanisms and formations** | Fifth preliminary assessment category. |
| 제갈무후 | **Zhuge Wuhou** | Honorific title for Zhuge Liang in the Three Visits allusion. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 불장 | **Buddhist Staff** | Generic term in Hong Dao's final words; the specific treasure is 녹옥불장. |
| 쓰촨성 | **Sichuan Province** | Source spelling variant of the established Sichuan location. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 선화아 | **Ship-Fire Boy** | Mu Song's sobriquet; literally a child who lights fires aboard a ship. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 삼괴 | **Three Fiends** | Collective form used by the Western Heaven Demon Lord for the Qilian Three Fiends. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 쓰촨 | **Sichuan** | Variant spelling used for the region associated with the pattern Jin recognizes. |
| 동정채 | **Donghu Stronghold** | Stronghold where Mu Song's Uncle Hwang is based. |
| 해사방 | **Sea Serpent Society** | Hubei association formed by fishermen and boatmen; it was annihilated at Red Cliffs. |
| 천령폭 | **Tianling Falls** | Dangerous waterway leading to Donghu Stronghold. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 조양 | **Zaoyang** | Ferry landing in Hubei where the party leaves the Yangtze. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 서천마군 | 청풍 | commander_to_young_opponent | you | gentle and taunting | Uses 자네 while identifying Cheongpung and discussing the Blood Lord. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 청풍 | 무송 | young martial companion to stronghold lord | you | cheerful and familiar | Offers Mu Song his last dumpling and then induces him to buy more in Guang'an. |
| 궁기방 | 무송 | martial companion to Stronghold Lord | Senior Mu Song | pleading-deferential | Begins pleading for Mu Song to save them from Tianling Falls. |

## Listed compact profiles

### Baek Woo.md

# Baek Woo (백우)

- **Safe through:** Chapter 250
- **Aliases:** Kunlun Cloud Dragon
- **Role:** Kunlun Daoist martial artist and finalist in the Star-Array Grand Banquet; Taekyung sent him plummeting during the third preliminary assessment after stepping on his face.
- **Personality:** Fastidious, easily offended, and self-righteous about propriety.
- **Voice:** Formal, archaic, and admonishing, with repeated complaints about vulgarity.
- **Relationships:** Rival finalist alongside Gung Gibang and Zhuge Gyun; regards Taekyung as an offensively vulgar fellow Daoist, but accepts Taekyung's demand to remain silent and use polite speech after being subdued aboard the carriage; his Master has instructed him to get along with Taekyung.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 455
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Dongting Fisherman.md

# Dongting Fisherman (동정어옹)

- **Safe through:** Chapter 455
- **Aliases:** None
- **Role:** The Dongting Fisherman is a Supreme Peak master and public critic of the Yangtze River Channel League, a leading suspect in the Donghu Stronghold massacre and possible Dark Heaven member whose Lower District Sect records indicate that he remains in Hubei Province.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** The Dongting Fisherman opposed the Yangtze River Channel League and was monitored by the Lower District Sect for several years after friction with it, while current records place him in Hubei Province.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 455
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung and uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and search for Dark Heaven’s Hubei forces.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 455
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 452
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan and belongs to the Yangtze River Channel League's moderate faction.
- **Personality:** Ambitious, domineering, impatient with interruptions, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** Mu Song is a member of the Yangtze River Channel League's moderate faction; Hwang Chung, his senior and Uncle Hwang, was the League elder and Donghu Stronghold Lord who was killed in its destruction.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 442
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

### Zhuge Gyun.md

# Zhuge Gyun (제갈균)

- **Safe through:** Chapter 455
- **Aliases:** Divine Marvel Dragon
- **Role:** Zhuge Gyun is the current Lesser Family Head of the Zhuge Clan, son of its Family Head Zhuge Feng, and a scholar-styled martial artist who was a finalist in the Star-Array Grand Banquet.
- **Personality:** Analytical, pedantic, and unusually preoccupied with theoretical correctness.
- **Voice:** Polished, formal, and interrogative, treating insults as subjects for precise analysis.
- **Relationships:** Rival finalist alongside Baek Woo and Gung Gibang; exchanges restrained arguments with Taekyung.

## Korean source

```text
＃456화



“난데없이 동정호라니. 그게 무슨?”

제갈균의 의아함은 잠깐이었다. 간혹 괴짜 같은 언행을 보이기는 해도 제갈세가의 핏줄답게 두뇌만큼은 명석한 녀석이었으니까.

신기묘룡(神奇妙龍)이라는 별호는 단순히 기관진식에 조예가 깊기 때문에 붙여진 것이 아니다.

“혹, 동정어옹을 찾으려 하십니까?”

몇 시진 전, 제갈세가에 막 도착했던 내게 사건의 정황을 모두 들은 제갈균이다. 동정어옹이 흉수 중 하나로 지목받았다는 것 역시 알고 있었다.

“그래.”

“갑자기 이러시는 걸 보니…… 정보의 출처는 개방과 하오문이겠군요.”

“정확히는 하오문. 삼 년 전부터 동정어옹을 주시하고 있었어.”

“주시가 아니라 감시겠죠. 동정어옹과 하오문주 사이에 모종의 일이 있었다는 건 본가에서도 눈치채고 있었습니다.”

“어찌 됐건 우리에게는 잘된 일이지. 읽어 봐.”

내게서 죽간을 건네받은 제갈균의 눈동자가 빠르게 움직였다.

불과 촌각 만에 모든 내용을 빠짐없이 읽은 녀석이 관자놀이를 문지르며 중얼거렸다.

“동정어옹이 아직 호북성에 있다?”

“하오문의 정보에 의하면 그래.”

“이것으로는 부족합니다. 이 죽간에 적힌 내용대로라면 하오문은 동정어옹의 정확한 행적을 파악한 것이 아니라, 단지 호북성을 빠져나가는 것을 포착하지 못한 것뿐입니다.”

“나도 그건 염두에 두고 있어. 하지만 그 내용이 사실일 경우에는?”

“만약 그렇다면…….”

모두에게서 죽은 사람으로 인식되어 있던 동정어옹이 호북성 어딘가에 멀쩡히 살아 있다?

이것이 의미하는 것은 한 가지밖에 없다.

“동정어옹이 정말 암천의 하수인이자 동정채를 몰살시킨 흉수 중 한 사람이라면 충분히 가능한 일이지. 아니, 오히려 흉수라는 것이 더욱 확실해져.”

제갈균이 무겁게 고개를 끄덕였다.

“그렇지요. 그가 암천이 아니라면 이미 동정채의 참극을 세상에 알리고, 본가와 무당파에 도움을 요청했을 테니까요.”

해사방에 이어 동정채를 비롯한 장강수로맹의 세 개 수채가 몰살당한 상황.

때마침 우리가 도착하지 않았더라면, 그리고 선화아 무송과 그가 이끄는 쾌조선이 아니었다면 천령폭 너머 동정채의 참상이 알려지는 것은 한참 더 뒤로 미뤄졌을 것이다.

“하지만 의문이 남습니다. 이건 감출 수 있는 종류의 것이 아닙니다. 시일이 더 걸릴 뿐, 결국은 밝혀질 일이었어요. 만약 암천이 작정하고 은폐하고자 했다면, 세인들의 이목을 끌지 않고 더욱 조용히 처리했겠지요. 해사방의 일은 장강수로맹에게 뒤집어씌우는 방향으로요.”

맞는 말이다. 제갈세가와 무당파가 천령폭을 넘지 못했던 이유는 그만큼 튼튼한 선박과 뛰어난 수부가 없었기 때문이다.

굳이 무송과 휘하의 수룡채 수적들이 아니더라도 곧 다른 지방에서 사람을 구할 수 있었을 것이다.

죽간을 물끄러미 응시하던 제갈균이 고개를 들어 나를 바라보았다.

“그렇다면 굳이 이렇게까지 한 이유가 뭐겠습니까?”

나는 탁자 위에 놓여 있던 잔을 기울여 목을 축였다.

“일반적인 경우에는 시간을 벌기 위해서겠지.”

“맞습니다. 암천은 빠져나갈 시간이 필요했을 겁니다. 그런데 동정어옹이 아직도 호북성에 머무르고 있다는 건 이상합니다.”

“그래, 이상해. 앞뒤가 안 맞을 만큼.”

내가 순순히 대답하자 제갈균의 눈썹이 슬쩍 올라갔다.

“다른 생각을 하고 계시군요.”

“앞에 말했잖아. 일반적인 경우에는, 이라고.”

“그럼…….”

“암천은 일반의 범주에 들어가는 놈들이 아냐. 너도 하남에서 겪어 봤으니 알고 있을 텐데?”

“……!”

“우선 작은 조약돌을 던져서 이목을 끌고, 그다음으로 바위를 준비하는 놈들이다. 해사방과 수채 세 개 정도로는 안 끝나. 분명히 더 노리는 게 있어.”

암천이 지닌 힘과 과감성은 상식을 벗어난다.

이미 십왕(十王)에 속한 전대의 초절정 고수 두 사람이 죽었고, 수천에 달하는 목숨이 피를 뿌리며 스러졌다.

그리고 암천이 일으킨 이 두 번의 혈사에는 한 가지 뚜렷한 목표가 있었다.

“신물(神物)…….”

제갈균의 침음성에 나는 조용히 고개를 끄덕였다.

암천은 하남에서 소림사의 신물인 녹옥불장을 탈취했고, 사천을 습격하며 만독지환을 빼앗으려 했다.

다행히 사천에서의 일은 실패로 돌아갔지만, 놈들이 무엇을 노리는지는 명백하다.

‘신물 혹은 구파일방, 오대세가라 불리는 명문 대파의 멸문.’

그런 놈들이 생계형 방파인 해사방과 수채 세 개를 없애기 위해 이런 짓을 벌였다고는 생각하기 어렵다.

차라리 해상왕이 있는 장강수로맹의 총단을 노렸다면 모를까.

제갈균이 경직된 얼굴로 입을 열었다.

“그렇다면 동정어옹을 비롯한 흉수들이 호북성에 남아 있을 이유도 충분하군요.”

“아직은 추측에 불과하지만, 우선 더 큰 일을 위해 다른 곳으로 이목을 끌었다고 봐야지. 시간을 끈 건 이미 호북성을 빠져나갔다고 생각하게 만들기 위한 장막이고.”

“등하불명(燈下不明)이라…… 혹시 이동진이라 불리는 그 해괴한 진법을 통해 이미 사라졌을 수도 있지 않겠습니까?”

“차라리 청풍이 만두 가게를 지나쳤다고 해라.”

“어, 그렇게 말씀하시니까 이해가 확 되네요.”

나는 허공을 뚫어져라 노려보며 말했다.

“해사방과 동정채의 일은 조약돌이야. 다음은 바위다.”

호북성이라는 연못은 넓다. 조약돌이 떨어져도 파문은 얼마 가지 않아 곧 가라앉는다.

하지만 바위가 떨어진다면 물보라가 일어나고 연못 안의 물고기들 역시 무사하지 못할 것이다.

연못이 피로 물들기 전에 바위가 떨어지는 것을 막아야 했다.

“만일의 사태를 대비하여 관부와 무당파에 이 사실을 알리고, 안팎으로 방비를 더욱 강화하겠습니다.”

“관군들을 주의해라. 사천에서 무슨 일이 있었는지는 들어서 알고 있지?”

서천마군이 이끄는 암천의 군세는 관군으로 위장하여 당문과 아미, 청성을 휩쓸었다.

이미 알려진 사실이니 제갈세가의 소가주인 제갈균이 그 사실을 모를 리 없었다.

“이미 주의하고 있습니다. 두 번이나 같은 방법을 쓸 것 같지는 않지만 말입니다.”

“동정채에도 알려. 조양(棗陽) 나루터에 수룡채의 쾌조선이 기다리고 있을 테니까 가솔들에게 서신을 맡기면 될 거다.”

전서구를 이용한다면 좀 더 빠르고 편하겠지만, 중간에 누군가에게 탈취당할 위험도 있을뿐더러 동정채를 오가도록 훈련받은 전서구는 제갈세가에 존재하지 않았다.

‘동정채와 연락이 가능했던 다른 두 수채도 이미 몰살당했고.’

참혹한 시산혈해의 광경이 눈앞을 스치자 나도 모르게 주먹에 힘이 들어간다.

산서에서 하남, 그리고 사천에 이어 현대에서 벌어진 쓰촨성 몬스터 웨이브까지. 이미 두 세상을 오가며 너무 많은 죽음을 지켜봤다.

드르륵.

자리에서 일어나는 내게 제갈균이 물었다.

“지금 바로 떠나시려고요?”

“서두를수록 좋으니까. 지금 어디에 있는지는 몰라도 우선 동정호로 가서 흔적을 찾아야지.”

“쉽지 않으실 텐데. 동정어옹은 일평생 동정호 인근에만 머물렀으니 세상에는 알려지지 않은 비처(秘處)를 여러 군데 알고 있을 겁니다.”

나는 주먹을 불끈 쥐고 입을 열었다.

“야, 너 암천이냐?”

“예?”

“암천이냐고.”

“아, 아닌데요.”

“그럼 재수 없는 소리 하지 말고 응원이나 해, 자식아.”

내 주먹을 힐끗 바라본 제갈균이 재빨리 대답했다.

“옙. 일단 본가의 정보력을 총동원하고 개방과 하오문과 협력하여 동정호 외의 다른 지역을 샅샅이 뒤져 보겠습니다.”

“잘해라. 간다.”

돌아서려던 나는 중요한 질문 하나를 빼먹었음을 깨닫고 멈칫했다.

“잠깐. 혹시 제갈세가에도 신물이 있나?”

“그럼요. 선조이신 제갈무후께서 생전에 타고 다니시던 사륜차(四輪車)와 심득을 집대성하신 병법이십사편(兵法二十四編). 그리고 백우선(白羽扇)도 있습니다.”

“……거, 많기도 하네.”

휠체어와 책, 부채가 얼마나 대단한 신물인지는 모르겠지만, 혹시 모를 경우를 대비하여 확인은 해 봐야 한다.

나는 제갈균을 향해 말했다.

“잠깐 좀 보자. 확인할 게 있어서 그래.”

“있었는데, 이제는 없는데요.”

“……?”

“병법이십사편은 전란 중에 소실됐고, 백우선은 낡아서 바스라졌습니다. 사륜차는 한 이백 년 전쯤에 선대 가주님 중 한 분이 탔다가 부숴 먹었다고 들었는데, 성함이 기억이 안 나네요.”

“…….”

뭐여, 시벌.

암천에게 빼앗기기 전에 자체 파괴하는, 뭐 그런 큰 그림인 건가.

신물의 면면을 보면 제갈무후가 남긴 물건이라는 것 외에는 별 의미가 없는 신물이었던 것 같긴 하지만, 그래도 황당하긴 매한가지다.

“그래도 사륜차는 부서진 상태로 남아 있는데, 그거라도 보여 드릴까요?”

“아니, 됐어.”

단호하게 대답한 나는 전각을 나왔다. 밖에서는 다시 어둑해진 밤하늘과 만반의 준비를 끝마친 세 사람이 나를 기다리고 있었다.

아니, 네 사람인가?

“그놈, 숨 잘 붙어 있지?”

“네. 은인.”

과거 내가 사천에서 그랬듯, 지게를 짊어진 청풍이 고개를 끄덕였다. 지게 위에는 모든 혈도를 제압당한 채 쇠사슬에 묶인 삼괴가 있었다.

“많이 쇠약해져 있기는 한데, 틈틈이 공력으로 원기(元氣)를 북돋아 주면 문제없을 것 같아요.”

“그 정도면 충분해.”

삼괴를 데려가는 이유는 간단하다. 혹시나 암천에 속한 놈들만 알아볼 수 있는 암호나 표식이 있을까 해서다.

그게 놈이 살아 있는 유일한 가치이기도 했다.

“가자, 동정호로.”

제갈세가를 빠져나온 우리는 곧게 뻗은 관도를 혜성처럼 가로질렀다.

전신을 스치는 바람에 피비린내가 섞여 드는 듯했다.



* * *



쉬이이이익!

우리는 기력을 아끼지 않고 질주했다.

나나 청풍, 궁기방에 비해 공력과 경신법이 떨어지는 혁무진이 계속해서 뒤로 쳐졌지만 그다지 큰 문제는 되지 않았다.

“업혀.”

전신이 땀으로 흠뻑 젖은 혁무진이 힘들게 고개를 저었다.

“헉, 허억. 아닙니다. 더 뛸 수 있습니다!”

“힘든 거 아니까 업히라고.”

“허억, 정말 괜찮습니다. 저는 대태원진가의 진룡대 부대주! 본가와 조장님께 누를 끼칠 수는…….”

“그런 새끼가 은자 줍겠다고 뛰어다녔냐?”

“…….”

“뒤지기 싫으면 업혀. 아니면 버리고 간다.”

“예, 옙.”

혁무진은 상당한 체격의 소유자였지만, 나는 굉장한 근력 스탯의 소유자다. 사람 하나 들고 뛰는 건 내게 있어 그리 큰 부담이 되지 않았다.

‘어쩐지 적토마가 된 기분인데.’

묘한 기분을 느끼며 얼마나 달렸을까, 제갈세가를 나설 때만 해도 조금 어둑했던 하늘은 완전히 어둠에 잠겼고, 관도를 오가던 사람들의 모습도 더는 보이지 않았다.

그렇게 두 시진이 넘는 시간이 더 흘렀을 때, 전력을 다해 경신법을 발휘하고 있던 궁기방이 입을 열었다.

악취와 단내를 머금은 한마디가 귓가를 파고들었다.

“무한(武漢)이군.”

무한은 호북성의 성도이자 동정호를 지척에 둔 도시였다.

하지만 최근 잇따른 흉흉한 사건들 때문인지, 불야성으로 북적일 거리는 조용했고 쥐새끼 한 마리 얼씬거리지 않았다.

‘양민들 입장에서는 당연하지. 괜히 밤에 나돌아다니다가 개죽음당하기는 싫을 테니까.’

그런 생각을 하며 무한의 복잡한 거리를 가로지르던 그 순간이었다.

“동정호! 동정호에서 배가 침몰했다!”

“……!”

저 멀리서 터져 나온 누군가의 비명이, 깊고 어두운 적막을 깨트렸다.
```

## Final English reading copy

```markdown
# Chapter 456

“Dongting Lake, out of nowhere? What do you mean?”

Zhuge Gyun’s puzzlement lasted only a moment. Though he occasionally behaved like an eccentric, his mind was as sharp as befitted a scion of the Zhuge Clan.

The epithet Divine Marvel Dragon had not been bestowed on him simply because he was deeply versed in mechanisms and formations.

“Are you trying to find the Dongting Fisherman?”

Several shichen[^1] earlier, Zhuge Gyun had heard the full circumstances of the case from me when I had just arrived at the Zhuge Clan. He also knew that the Dongting Fisherman had been identified as one of the culprits.

“Yeah.”

“You are acting rather suddenly… The source of this information must be the Beggars’ Sect and the Lower District Sect.”

“More precisely, the Lower District Sect. They’ve been watching the Dongting Fisherman for three years.”

“Not watching. Monitoring. Our family had also noticed that something had happened between the Dongting Fisherman and the Lower District Sect Leader.”

“Either way, this works in our favor. Read it.”

Zhuge Gyun took the bamboo slip from me, and his eyes moved rapidly across it.

He read every bit of its contents in the space of a few breaths, then rubbed his temple and muttered,

“The Dongting Fisherman is still in Hubei Province?”

“That’s what the Lower District Sect’s intelligence says.”

“This is insufficient. According to what is written on this bamboo slip, the Lower District Sect has not determined the Dongting Fisherman’s exact whereabouts. They merely failed to detect him leaving Hubei Province.”

“I’ve considered that, too. But what if the information is accurate?”

“If that is the case…”

The Dongting Fisherman, whom everyone believed to be dead, was alive and well somewhere in Hubei Province?

That could mean only one thing.

“If the Dongting Fisherman really is a Dark Heaven underling and one of the culprits who massacred Donghu Stronghold, then it would certainly be possible. No—in fact, it would make it even more certain that he is a culprit.”

Zhuge Gyun nodded heavily.

“That is true. If he were not affiliated with Dark Heaven, he would already have revealed the tragedy at Donghu Stronghold to the world and requested assistance from the Zhuge Clan and Wudang.”

After the Sea Serpent Society, three strongholds of the Yangtze River Channel League, including Donghu Stronghold, had been annihilated.

If we had not arrived when we did—and if it had not been for Ship-Fire Boy Mu Song and the fast boats under his command—the tragedy at Donghu Stronghold beyond Tianling Falls would have remained unknown for much longer.

“But a question remains. This is not the kind of thing that can be concealed. It might take time, but the truth would eventually come to light. If Dark Heaven had deliberately intended to hide it, they would have handled the matter more quietly, without attracting the attention of the common people. They could have framed the Yangtze River Channel League for what happened to the Sea Serpent Society.”

He was right. The reason the Zhuge Clan and Wudang had been unable to cross Tianling Falls was that they lacked vessels sturdy enough for the journey and skilled boatmen to pilot them.

Even without Mu Song and the river bandits of Water Dragon Stronghold, they would soon have been able to find people from another region.

Zhuge Gyun stared pensively at the bamboo slip before raising his head to look at me.

“Then why go this far?”

I tilted the cup on the table and moistened my throat.

“In ordinary circumstances, it would be to buy time.”

“Exactly. Dark Heaven would have needed time to escape. But the fact that the Dongting Fisherman is still in Hubei Province is strange.”

“Yeah. It’s strange. So strange that it doesn’t fit together.”

When I answered without hesitation, Zhuge Gyun’s eyebrows rose slightly.

“You have another thought in mind.”

“I told you. In ordinary circumstances.”

“Then…”

“Dark Heaven isn’t made up of ordinary people. You experienced them in Henan, so you should know that.”

“……!”

“They’re the kind of people who throw a pebble first to draw everyone’s attention, then prepare a boulder. The Sea Serpent Society and three strongholds won’t be the end of it. They’re definitely aiming for something bigger.”

Dark Heaven’s power and audacity lay beyond common sense.

Two Supreme Peak masters from the previous generation belonging to the Ten Kings had already died, and thousands of lives had fallen in rivers of blood.

And the two blood tragedies Dark Heaven had caused shared one unmistakable objective.

“Sacred treasures…”

At Zhuge Gyun’s low murmur, I quietly nodded.

In Henan, Dark Heaven had stolen the Shaolin Temple’s sacred treasure, the Green Jade Buddha Staff. When they attacked Sichuan, they had attempted to seize the Myriad-Poison Ring.

Fortunately, their operation in Sichuan had failed. But what they were after was obvious.

*Sacred treasures—or the destruction of the prestigious great sects known as the Nine Sects and One Gang and the Five Great Families.*

It was difficult to believe that people like that had gone to such lengths merely to eliminate the Sea Serpent Society and three strongholds whose members made their living on the water.

It would have been more understandable if they had been aiming for the headquarters of the Yangtze River Channel League, where the Seafaring King was based.

Zhuge Gyun spoke with a stiff expression.

“Then there is sufficient reason for the culprits, including the Dongting Fisherman, to remain in Hubei Province.”

“It’s still only speculation, but for now, we have to assume they drew attention elsewhere in preparation for something bigger. The delay was merely a curtain meant to make us believe they had already left Hubei Province.”

“Unable to see what is right beneath one’s nose… Could they have already disappeared through that bizarre formation known as the Moving Formation?”

“You might as well say Cheongpung walked past a dumpling shop.”

“Oh. Now that you put it that way, I understand completely.”

I glared into empty space and spoke.

“What happened to the Sea Serpent Society and Donghu Stronghold was the pebble. The boulder comes next.”

The pond called Hubei Province was vast. Even if a pebble fell into it, the ripples would not travel far before subsiding.

But if a boulder fell, a great splash would rise, and the fish inside the pond would not escape unharmed.

We had to stop the boulder from falling before the pond was dyed with blood.

“I will inform the local authorities and Wudang in preparation for the worst, then further strengthen our defenses inside and out.”

“Be wary of the government troops. You’ve heard what happened in Sichuan, haven’t you?”

The forces of Dark Heaven led by the Western Heaven Demon Lord had disguised themselves as government troops and swept through the Tang Clan, Emei, and Qingcheng.

It was already common knowledge, so there was no way Zhuge Gyun, the Zhuge Clan’s Lesser Family Head, was unaware of it.

“I am already taking precautions. Though I doubt they will use the same method twice.”

“Inform Donghu Stronghold, too. The fast boats from Water Dragon Stronghold should be waiting at the Zaoyang ferry, so you can entrust the letter to our household retainers.”

Messenger pigeons would have been faster and more convenient, but there was a risk that someone might intercept them. Besides, the Zhuge Clan had no messenger pigeons trained to travel to and from Donghu Stronghold.

*The other two strongholds that had been able to communicate with Donghu Stronghold had already been wiped out, too.*

The horrific sight of the mountain of corpses and sea of blood flashed before my eyes, and my fist tightened before I realized it.

From Shanxi to Henan, then Sichuan, and finally the monster wave that struck Sichuan Province in the modern world—I had already crossed between two worlds and witnessed far too many deaths.

Scrape.

As I rose from my seat, Zhuge Gyun asked,

“Are you leaving right now?”

“The sooner, the better. I don’t know where the Dongting Fisherman is now, but we should go to Dongting Lake first and search for traces.”

“That will not be easy. The Dongting Fisherman spent his entire life around Dongting Lake, so he likely knows several hidden places unknown to the rest of the world.”

I clenched my fist and spoke.

“Hey, are you Dark Heaven?”

“Pardon?”

“I asked if you’re Dark Heaven.”

“Ah, no.”

“Then stop saying ominous things and cheer me on, you bastard.”

Zhuge Gyun glanced at my fist and hurriedly answered,

“Yes, sir. For now, I will mobilize all of our family’s intelligence resources and cooperate with the Beggars’ Sect and the Lower District Sect to search every region outside Dongting Lake.”

“Do a good job. I’m leaving.”

I was about to turn around when I realized I had forgotten one important question.

“Wait. Does the Zhuge Clan have a sacred treasure, too?”

“Of course. There is the four-wheeled cart our ancestor Zhuge Wuhou rode during his lifetime, the Twenty-Four Chapters on the Art of War, in which he compiled his insights, and the White Feather Fan.”

“……That’s quite a lot.”

I had no idea how impressive a cart, a book, and a fan could be as sacred treasures, but I had to check, just in case.

I turned to Zhuge Gyun.

“Let me take a look. I just need to confirm something.”

“We had them, but now we don’t.”

“……?”

“The Twenty-Four Chapters on the Art of War were lost during a war, and the White Feather Fan crumbled with age. As for the four-wheeled cart, I heard that one of our former Family Heads rode it and broke it around two hundred years ago. I cannot remember his name.”

“…….”

What the fuck.

Was this some grand strategy in which they destroyed the treasures themselves before Dark Heaven could steal them?

Judging by the sacred treasures themselves, they seemed to have been meaningful only because they were objects left behind by Zhuge Wuhou. But it was still just as absurd.

“The four-wheeled cart is still here in its broken state, though. Would you like me to show it to you?”

“No, forget it.”

I answered firmly and left the pavilion. Outside, three people who had finished making all their preparations were waiting for me beneath the night sky, which had darkened once more.

Or was it four people?

“He’s still breathing, right?”

“Yes, Benefactor.”

Cheongpung nodded, carrying a wooden pack frame on his back just as I had in Sichuan. The Three Fiends lay on it, all his acupoints sealed and his body bound in chains.

“He is quite weak, but I think he will be fine if I use internal energy from time to time to restore his vitality.”

“That’s enough.”

There was a simple reason for bringing the Three Fiends along. I wanted to find out whether there were any codes or markings that only members of Dark Heaven could recognize.

That was the only reason he was worth keeping alive.

“Let’s go to Dongting Lake.”

We left the Zhuge Clan and raced along the straight highway like comets.

The wind brushing against my entire body seemed to carry the smell of blood with it.

* * *

Whoooosh!

We sprinted without sparing our strength.

Hyuk Mujin’s internal energy and movement technique were inferior to mine, Cheongpung’s, and Gung Gibang’s, so he kept falling behind. But it did not become much of a problem.

“Get on my back.”

Hyuk Mujin, his entire body drenched in sweat, shook his head with difficulty.

“Huff, huff. No, sir. I can run farther!”

“I know you’re having a hard time, so get on.”

“Huff, I am truly fine. I am the Vice Squad Leader of the Jin Dragon Squad of the great Jin Family of Taiyuan! I cannot cause trouble for my family or Captain—”

“Did a guy like you run around trying to pick up silver nyang?”

“…….”

“If you don’t want to die, get on. Otherwise, I’ll leave you behind.”

“Yes, sir.”

Hyuk Mujin was a man of considerable size, but I possessed an exceptional Strength stat. Carrying a person while running was not much of a burden for me.

*I feel like the Red Hare for some reason.*

I wondered at the strange feeling as we continued running.

By the time we had gone some distance, the sky that had been slightly dim when we left the Zhuge Clan had sunk into complete darkness. The people traveling along the highway had vanished as well.

After more than two shichen had passed, Gung Gibang, who had been exerting his movement technique at full strength, opened his mouth.

His words, carrying the smells of filth and sweetness, pierced my ears.

“Wuhan.”

Wuhan was the capital of Hubei Province, a city close to Dongting Lake.

But perhaps because of the series of ominous incidents that had recently occurred, the streets that normally bustled through the night were silent. Not even a rat showed its face.

*Of course. From the common people’s perspective, who would want to wander around at night and die like a stray dog?*

That was what I was thinking as we crossed Wuhan’s complicated streets when it happened.

“Dongting Lake! A boat has sunk in Dongting Lake!”

“……!”

Someone’s scream erupted in the distance, shattering the deep, dark silence.

[^1]: A **shichen** is a traditional time unit of roughly two hours.
```
