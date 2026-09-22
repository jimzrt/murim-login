<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0654.txt",
      "sha256": "ab859de93d11a77f2465d7aa7676c31d486491641d5c3f25271717ed0a5f7674",
      "bytes": 12974
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "94229bbd65ebaa2bc57e6b8802ba8a1833515506068419c215df056589bda832",
      "bytes": 2312
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a70d22b4ca0b704ca8b47618b5e64460d3cabd6099366e083bc2086d5e0f729d",
      "bytes": 200089
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "877a3ed0682903f13925d95f3b4a93074da1198f75c5fe42c985b8c5456bc914",
      "bytes": 748
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "f08406bc4a904f664fb814a0dfa04bb6f1d832730f74e83447a6fe3bfc280a3c",
      "bytes": 830
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "76c9577fb0f0fe0ffa520a67e4604882d8b021b0d2ad690575852ab5d19203f8",
      "bytes": 553
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "63bdc87712cb6f6983125599780aad43e897790d1bb081410f19b545cdc52df8",
      "bytes": 722
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "92a77046a74043d1eee8d6b1e9b67f1f5e5e8f22e77f35b5c4336b4733ceff17",
      "bytes": 1252
    },
    {
      "path": "characters/Namho.md",
      "sha256": "a76790efd0c4592aeca2f003dfaf168e76d6f9586c2c07531f761a8059977989",
      "bytes": 843
    },
    {
      "path": "characters/Pill Physician.md",
      "sha256": "83191c48705a53aed94df86655a5fd35c4164b30c1570fbf2da6816468d2d58d",
      "bytes": 554
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "7bc79335c834558e771ce27278a643f4f9c6a5cd441b8030a4dc2e57b0f62c0b",
      "bytes": 936
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "2078430dc5a35d80b3c748bd069602ec65fbac2cc8ad21369965d1fef1bd0bd0",
      "bytes": 585
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "574fb132e4435002eefb34f19fede87e7577b06e530195078073f6ba6ebf237b",
      "bytes": 888
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "38da939aa037966ee9196e4469984eed5b5c54ec7127c5f18e03fe5c09a1080d",
      "bytes": 871
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "58d50c26df6adc7c345adae6fd936d0d461b87404f9124827a8548a7f526fe05",
      "bytes": 542
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "88019c0cfd61c3aeb2dd467971aea7a4324db023c59e4689c59c3828ae2f0565",
      "bytes": 205898
    }
  ],
  "estimated_tokens": 12148
}
-->

# Durable State Update — Chapter 654

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 654. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 654. Profile updates may replace only one
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
  "chapter": 654,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 654,
    "continuity_sources": [654],
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
    "Jin remains in the Nanman Beast Palace's Inner Palace as the Third Young Master of the Jin Family of Taiyuan and head of the Fire Dragon Pavilion.",
    "Heugung alleges that Baeksang colluded with Dark Heaven but has no concrete proof.",
    "Heugung has secretly evaded Baeksang's surveillance for more than twenty years, including by learning the Bone-Shrinking Technique.",
    "Heugung claims Baeksang exchanges unexplained monthly missives and disappears alone, monthly since last year.",
    "Heugung's loyal retainers investigated Baeksang's secret refuge twenty years ago, but the refuge was destroyed and the retainers died or vanished.",
    "Heugung genuinely loves Yohi and says she chose wrongly while trying to revive the Yao people.",
    "Heugung offers to testify at the next day's Tribal Grand Council if his and Yohi's safety is guaranteed.",
    "Heugung had just promised to cooperate with Jin before the assault on the Fire Dragon Pavilion.",
    "Jin has not yet informed the Beast Miao King and intends to consult the Fire Dragon Pavilion first.",
    "The Fire Dragon Pavilion was attacked at night while Jin was absent, and Sama Pyo was badly wounded while resisting the attackers.",
    "Jin defeated the remaining masked Peak masters, while Taishan killed two attackers after Namho provoked him with the theft of chicken legs.",
    "The attackers committed suicide by severing their own heart meridians before revealing whether Baeksang, Heugung, or Yohi ordered the assault."
  ],
  "continuity_sources": [
    653
  ],
  "open_questions": [
    "Is Baeksang truly colluding with Dark Heaven, and what evidence can Heugung provide?",
    "What happened at Baeksang's secret refuge, and who destroyed it?",
    "Will the Beast Miao King accept Heugung as a witness and guarantee Heugung's and Yohi's safety?",
    "How knowingly did Yohi align herself with Baeksang's side?",
    "Who organized the masked assault on the Fire Dragon Pavilion, and was Heugung, Baeksang, or Yohi involved?"
  ],
  "safe_through": 653,
  "temporary_decisions": [
    "Use Finger Qi for 지풍.",
    "Use heart meridian for 심맥.",
    "Use Dark Heaven hound for 암천의 주구.",
    "Use Force for 강기.",
    "Use moon saber for 월도."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 소림     | **Shaolin**                      |
| 암천     | **Dark Heaven**                  |
| 사천당가   | **Sichuan Tang Clan**            |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 주화입마   | **qi deviation**                                 |                                                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 상태               | **Status**                     |
| 사천     | **Sichuan**            |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 환의 | **Pill Physician** | Title of the current Family Head of the Seongsu Jang Family. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 아미파 | **Emei Sect** | Murim sect in Sichuan. |
| 소림혈사 | **Shaolin Bloodshed** | Past incident cited by Hwangbo Eom. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 심맥 | **heart meridian** | Meridian severed by an infiltrator to commit suicide. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 사천혈사 | **Sichuan Blood Tragedy** | Earlier incident in which Taekyung witnessed the strange formation. |
| 기경팔맥 | **Eight Extraordinary Meridians** | The eight extraordinary meridians of wuxia physiology. |
| 칠공 | **seven apertures** | The seven bodily openings through which Taekyung's overflowing heat escapes. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 축골공 | **Bone-Shrinking Technique** | A martial art that stretches and shrinks bone and flesh to alter the user's appearance. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 야율목 | 남호 | Nanman Young Palace Lord to elderly guest and Hidden Shadow Pavilion agent | old man | respectful and familiar | Yayul Mok uses the honorific 노인장 while praising Namho's knowledge of White Tigers. |
| 흑웅 | 백상 | younger_great_chieftain_to_senior_great_chieftain | Uncle Baek | deferential and nervous | Heugung addresses Baeksang as 백 숙부 after being confronted by his icy stare. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 653
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle, opposes the Nanman Beast Palace joining the Murim Alliance, remains distrustful of the Central Plains, and is alleged by Heugung to have colluded with Dark Heaven.

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 644
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who seeks Jin Taekyung, Cheongpung, and Jeok Cheongang after escaping the confrontation at Mount Song.
- **Personality:** Calm, confident, theatrically frivolous, casually cruel, and ruthlessly destructive; treats allies as disposable tools and enjoys provoking stronger opponents.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven alongside the Western Heaven Demon Lord, has received the Lord of Heaven's power for the coming Great War, and still seeks to kill Cheongpung, Jeok Cheongang, and Jin Taekyung.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 653
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 653
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung presents as foolish and easily flattered in public but is capable of concealed planning, disguise, and covert contact.
- **Voice:** Heugung speaks with warm enthusiasm and genuine, openly devoted affection toward Yohi.
- **Relationships:** Heugung remains publicly entangled with Baeksang, genuinely loves Yohi, has promised to cooperate with Jin Taekyung, and is now suspected by Jin of possibly arranging the assault on the Fire Dragon Pavilion.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 647
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; he was the sole survivor of an assassin training cohort that began with three hundred candidates and passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom Mungyeong helped break free of his Heart Demon, Mungyeong was asked to look after and instruct Jin Taekyung and has now ended that direct training after teaching him martial principles and giving him a custom fire-qi pill, Cheongpung is accompanying him while learning his martial arts through observation, and Mu Song plus five Water Dragon Stronghold subordinates know he is an exceptionally powerful master but not that he is the Slaughter Saint.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 653
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Pill Physician.md

# Pill Physician (환의)

- **Safe through:** Chapter 641
- **Aliases:** None
- **Role:** Current Family Head of the Seongsu Jang Family in Shandong, who personally placed and signed the Thousand-Year Snow Ginseng in the casket entrusted to the Yongbong Escort Bureau.
- **Personality:** No personality traits are established.
- **Voice:** No voice traits are established.
- **Relationships:** The Pill Physician heads the Seongsu Jang Family, a prestigious medical family in Shandong.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 653
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 653
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 644
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 645
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and Yayul Mok's father; Yayul Mok is his only surviving son after three older siblings died in the Great Faction War, Baeksang is his father's sworn younger brother, and his white tiger is a long-bonded companion.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 653
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, seeks to unite Nanman's four great tribes under Yao leadership, and manipulates Heugung alongside Baeksang.

## Korean source

```text
＃654화



만약 누가 내게 절정 고수 세 명을 일수(一手)에 죽일 수 있느냐 묻는다면, 나는 큰 고민 없이 고개를 끄덕일 것이다.

그러나 세 명의 절정 고수를 일수에 제압해야 한다면, 그들이 살수(殺手)나 다름없는 성향을 지녔다면 이야기는 달라진다.

그럴 때는 무력보다는 회유를 통해 제압해야 하는 것이 맞다. 고문에 시달리다가 고통스럽게 죽는 것이 아닌, 생존에 대한 확신을 주어야 자결을 막을 수 있을 테니까.

하지만…….

으득.

내 약속은 놈들에게 확신을 심어 주지 못한 모양이었다. 아니면 그보다 주인에 대한 두려움이 더욱 컸을지도 모를 일이다.

쉬쉬쉭! 투둑!

반 박자 늦게 손가락 끝에서 쏘아진 지풍(指風)이 혈을 짚었지만, 이미 돌이키기에는 늦었다.

마혈을 제압당해 뻣뻣하게 굳어 버린 세 개의 몸뚱어리는 이미 칠공(七空)에서 피를 흩뿌리며 허물어지는 중이었다.

파팟! 덥석.

수 장의 거리를 단숨에 좁힌 나는 허물어지는 세 개의 신형을 붙잡아 땅에 뉘었다.

복면 사이로 놈들의 입가에서 끈적한 핏물이 울컥거리며 솟구친다.

“그르륵, 커헉……!”

빌어먹을. 상황이 좋지 않다. 아니, 최악이다.

스스로 심맥(心脈)을 끊는다는 것은 몸 안에서 폭발이 일어난 것과 같다.

인체에서 가장 중요하다고 할 수 있는 기경팔맥(奇經八脈)은 물론 전신에 존재하는 수백 개의 혈이 끊어지고 막히면 살아남을 길이 없다.

‘특히 무림인이라면 더더욱.’

소위 말하는 하이 리스크, 하이 리턴.

무림인은 축기(蓄氣)를 통해 범인을 뛰어넘는 능력을 갖추게 되지만 심맥이 끊어진다면 주화입마라는 1+1 빅 이벤트까지 더해진다.

바로 지금처럼.

“쿨럭. 쿠에에엑!”

촤아아악!

눈, 코, 입. 귀.

당장 보이는 구멍을 통해 끊임없이 흘러나오는 검붉은 핏물과 내장으로 보이는 희멀건한 덩어리들.

이 끔찍한 광경에 황급히 다가온 남호와 태산마저 멈칫하며 걸음을 멈췄다.

“으으. 태산이. 보기 싫다. 입맛 떨어진다.”

“이, 이게 무슨.”

마른 침을 꿀꺽 삼킨 남호가 가라앉은 목소리로 물었다.

“살릴 수 있겠느냐?”

무의미한 질문이었다. 상황은 이미 돌이킬 수 없을 지경까지 치닫고 있었으니까.

그리고 내가 그 질문에 대답하기도 전에, 전신을 펄떡거리며 경련하던 두 놈의 고개가 힘없이 꺾였다.

툭.

볼 것도 없는 절명(絶命).

하지만 여기에서 포기하기에는 아직 이르다. 나는 마지막 남은 복면인의 완맥을 붙잡고 전력을 다해 공력을 흘려보냈다.

스아아아아.

뜨거운 열기를 머금은 열양지기가 놈의 몸속으로 흘러 들어가자 엉망진창이 된 내부가 느껴진다.

내장기관은 상하지 않은 곳이 없었고, 절정 고수답게 넓고 튼튼해야 할 혈도는 낡은 폐가의 담벼락처럼 허물어져 있었다.

‘거기에 더해 주화입마(走火入魔)까지…….’

천하에서 으뜸가는 신의인 문경이 온다 해도 생사를 장담할 수 없는 상황. 회생불능을 직감한 나는 이를 악물었다.

‘알아내야 해. 무슨 일이 있어도.’

하나의 이름. 오늘의 습격을 지시한 단 한 사람의 이름만 들으면 된다.

나는 아낌 없이 공력을 쏟아부었다. 돌이킬 수 없는 폭주 상태에 접어든 복면인의 내부를 다스리기 위해서가 아닌, 마지막 불씨를 피워 올리기 위해서였다.

드드드득!

더욱 강해진 공력의 유입과 함께 거세게 몸부림치는 전신.

하지만 거센 폭풍우가 지난 뒤에 수면이 잔잔해지는 것처럼, 죽음의 문턱에 다다라 있던 복면인은 짧은 평온과 이성을 되찾을 수 있었다.

회광반조(回光返照).

이제 정말 마지막이다. 나는 초점이 또렷해진 복면인의 눈동자를 응시하며 물었다.

“누구냐. 말해.”

그리고 다음 순간. 놈의 마지막 대답을 듣기 위해 입가의 복면을 벗긴 나는, 이 최후의 시도와 질문이 무의미한 것이었다는 사실을 깨달았다.

“쿨럭. 흐으. 허어어.”

“……!”

“크륵. 으어어.”

뭐라 말하려는 듯 상하로 움직이는 턱. 하지만 놈은 아무런 말도 하지 않았다.

아니, 할 수 없었다는 것이 맞는 표현일 것이다.

순간 석상처럼 굳어 버린 내 머리 위로, 남호의 신음 같은 뇌까림이 들려왔다.

“지독한 놈들. 혀를…….”

목소리는 끝까지 이어지지 않았고, 복면인에게 주어진 마지막 시간은 너무나도 짧았다.

크륵.

유언을 대신한 단말마와 함께 텅 비어 버린 동공. 멍하니 벌어진 입에서 뭔가 말할 듯이 움직이던 짧은 혀가 축 늘어진다.

그리고 마침내 죽음을 맞이한 놈을 말없이 바라보던 나는, 참았던 욕설을 토해 냈다.

“……이런 씨발.”

심상치 않은 놈들이라는 건 알았지만, 설마하니 혀가 잘려 있을 줄이야.

놈들이 처음부터 끝까지 비명을 제외하면 한마디도 하지 않은 이유가 있었다. 아니, 하고 싶어도 하지 못했던 거다.

“음, 다른 놈들도 마찬가지다. 혀의 단면이 아물어 있는 것을 보아하니, 이미 오래전에 조치를 취해 놓은 모양이야.”

은영각 요원답게 재빨리 시신들을 파악한 남호가 침음성을 흘렸다.

“이놈들…… 전부 남만인들이군.”

“한족은 없습니까?”

“없다, 단 한 사람도. 복장이 통일되어 있어서 어느 부족인지도 파악할 수가 없고.”

남만인들을 구분 짓는 가장 확실한 방법은 바로 복장과 식습관이다. 하지만 죄다 새카만 흑의에 복면을 썼으니 알아차리기가 힘들 수밖에 없다.

애당초 한족과 남만인들의 생김새도 미세한 차이만 있을 뿐이니, 당장 부족을 알아본다는 것은 어불성설이나 다름없었다.

“……제기랄.”

한숨 섞인 욕설을 내뱉은 나를, 남호가 깊게 가라앉은 눈빛으로 응시했다.

“네가 저놈들을 회유하는 과정에서 짐작되는 흉수로 세 명의 대족장을 언급했었지. 그렇다면 혹 서신을 보낸 이가 흑웅이었느냐?”

나는 놀란 눈으로 남호를 바라보았고, 그것으로 대답은 충분했다.

“그래. 그렇게 된 거로군.”

“남 노인이 그걸 어떻게…….”

“백상과 요희라면 충분히 흉수로 거론될 만한 인물들이다. 하지만 흑웅은 다르지. 생각해 보면 네가 이런 상황에서 그를 떠올릴 만한 이유는 하나뿐이었다.”

침착하면서도 냉철한 어조로 말을 끝마친 남호가 입을 열었다.

“그였느냐?”

“네.”

고개를 끄덕인 내가 말을 이었다.

“서신에 적혀 있던 장소에서 절 기다리고 있었습니다.”

“바위 뒤보다 숲에 숨는 걸 택했군. 하지만 아무리 인파가 많더라도 흑웅 정도의 체구라면 눈에 띄었을 텐데. 그가 직접 나왔단 말이냐?”

“축골공(縮骨功)을 익혔더군요. 처음에는 저도 흑웅이라고 예상하지 못했습니다.”

“허, 축골공이라. 보이는 것보다 비밀이 많은 작자였군. 모두가 감쪽같이 속았어. 하긴, 세상에 알려진 그대로의 인물이었다면 네게 서신을 보내지도 않았겠지.”

혼잣말처럼 중얼거린 남호가 무거운 표정으로 말을 이었다.

“계속해 보거라.”

흑웅에 대한 이야기는 짧았지만, 그 내용은 결코 흘려들을 수 있는 것이 아니었다.

입을 굳게 다문 채 모든 자초지종을 들은 남호는 안 그래도 주름진 미간을 잔뜩 찌푸렸다.

“거지발싸개 같은 상황이로고.”

동감이다. 일이 벌어졌지만 좀처럼 용의자를 좁힐 수 없었다.

백상, 요희, 흑웅. 그 누구도 용의 선상에서 제외시키기 힘든 상황. 게다가 오늘의 습격의 진정한 배후에는 암천이라는 두 글자가 있었다.

‘독단이 아니라 심맥을 끊은 것만 봐도 짐작할 수 있지.’

남만의 특성상 자결할 수 있는 극독을 구하는 건 너무나도 쉽다. 당장 외궁 밖의 풀숲으로 피크닉만 가도 온갖 독물들이 우글거리는 동네니까.

하지만 복면인들은 스스로 심맥을 끊는 것을 택했다.

심맥을 끊는 것은, 빠르고 쉬운 독단에 비해 몇 배나 더 극심한 고통을 겪으며 죽는 길이다.

나로서는 놈들이 이미 그에 관한 정보를 알고 있다고 짐작할 수밖에 없었다.

‘만독지환. 암천은 내가 만독지환을 갖고 있다는 사실을 이미 알고 있을 거야.’

암천은 혈주를 보내 소림혈사를 일으켰고, 사천에서 서천마군으로 하여금 아미파와 사천당가의 신물을 탈취하고자 했었다.

십왕(十王)과 비견해도 떨어지지 않을, 아니 어쩌면 삼성(三星)에 버금가는 초절정 고수들과 정예 병력을 신물을 위해 쏟아부은 것이다.

‘하지만 사천혈사가 끝난 직후에도, 사천당가에는 아무런 문제도 없었지.’

사천당가는 서천마군과의 전투로 사천의 어느 문파보다 극심한 피해를 입고 휘청였지만, 모두가 우려했던 암천의 후속타는 없었다.

그리고 나는 그 결정적인 이유가 만독지환의 유무라고 짐작했다.

‘그러니 독단 대신 심맥을 끊어서 일말의 가능성조차 차단하게 만든 거고.’

문득 식은땀 한 방울이 등줄기를 타고 흘러내렸다.

적들은 내 움직임을 낱낱이 지켜보고 있는데, 나는 어둠 속에 숨어 있는 누군가의 정체조차 파악하지 못하고 있었으니까.

남만의 심장이라 할 수 있는 남만야수궁의 내궁(內宮)에서 오늘과 같은 습격이 벌어졌다는 것만으로도 충분한 위협이었다.

“언제부터 습격이 벌어진 겁니까?”

내 물음에 남호가 무거운 목소리로 대답했다.

“나도 도중에 잠에서 깬 터라 잘은 모르겠지만…… 네가 떠난 지 반 시진도 되지 않아 일이 벌어진 것 같다. 무슨 일인가 싶어 확인해 보니 밖에서 난리가 나 있더군. 사마표 저놈은 피칠갑을 해 가며 싸우고 있었고.”

쓰러져 있는 사마표를 가리킨 남호가 걱정스러운 눈빛으로 물었다.

“한데 저놈은 괜찮은 게냐? 놈들과 싸우면서 피를 많이 흘린 것 같던데.”

“지혈도 해 뒀으니 괜찮을 겁니다. 살펴보니 당장 눈에 띄는 위험한 상처도 없고, 대부분이 적들의 피를 뒤집어쓴 것 같더군요.”

시신들을 끌어다가 한곳에 모아 놓고 돌아온 태산이 커다란 눈동자를 껌뻑였다.

“각주, 사실인가? 태산이 주군 괜찮나?”

“그래. 힘을 너무 많이 써서 쓰러진 것뿐이야.”

원하는 대답을 들은 모양인지, 태산의 눈동자에 뿌연 습막이 차올랐다.

“흐끅. 태산이. 걱정했다. 만약 주군 죽었으면. 태산이 삼 년 동안 고기 안 먹었을 거다. 흐끅.”

“…….”

“…….”

삼년상은 들어 봤어도 삼 년 동안 고기 끊는 애도 방식은 처음 들어 본다. 그 정도면 무림에서 가장 힘센 비건이 되지 않을까.

나는 차오르는 말을 꿀꺽 삼키며 녀석의 우랄산맥 같은 어깨를 두드려 주었다.

“그래, 너도 고생했다.”

“흐끅. 태산이. 힘 많이 썼더니 배고프다.”

“……어, 그래.”

한 대 쥐어박을까 그냥.

하지만 내가 심도 깊은 고민을 하던 그때. 저 멀리서 횃불과 함께 숱한 인기척들이 가까워지기 시작했다.

그리고 어느 맹수의 익숙한 포효도 함께.

- 크아앙!

쉬쉬쉭! 팟!

어둠 속에서 확연히 눈에 띄는 은빛 신형이 가장 먼저 공터에 도달했다.

백호의 등에 올라탄 야율목의 얼굴은 목각 인형처럼 딱딱하게 굳어 있었다.

“……늦었군.”

나는 담담하게 대꾸했다.

“그래, 늦었지. 내궁에서 이런 일이 벌어졌다는 게 믿을 수 없을 만큼.”

무너진 전각과 곳곳에 고인 피 웅덩이. 그리고 쌓여 있는 시신들.

입술을 질끈 깨문 야율목이 입을 열었다.

“순찰을 돌던 전사들이 죽어 있었다. 반 각 전에야 그 사실을 알았어. 그리고…….”

다음 순간, 이어진 야율목의 말을 들은 나는 귀를 의심할 수밖에 없었다.

“흑웅과 요희. 두 대족장이 사라졌다.”

……뭐?
```

## Final English reading copy

```markdown
# Chapter 654

If someone asked whether I could kill three Peak masters with a single move, I would nod without much hesitation.

But if they asked whether I could subdue three Peak masters in a single move, and those three had the mindset of assassins, the answer would be different.

In that situation, the right approach was to subdue them through persuasion rather than force. To prevent them from committing suicide, I had to give them confidence that they would survive—not let them suffer through torture before dying painfully.

But…

Crack.

Apparently, my promise had failed to give them that confidence. Or perhaps their fear of their master was even greater.

Ssshhh! Thud!

The Finger Qi fired from my fingertips a half-beat too late struck their acupoints, but it was already impossible to turn things around.

The three bodies, stiffened after their Paralysis Acupoints were struck, were already collapsing as blood sprayed from their seven apertures.

Papap! Grab.

I closed the distance of several zhang in an instant, caught the three falling figures, and laid them on the ground.

Sticky blood bubbled up from the corners of their mouths beneath their masks.

“Grrrk, cough…!”

Damn it. The situation was bad.

No, it was the worst.

Severing one's own heart meridian was like setting off an explosion inside the body.

If the Eight Extraordinary Meridians—the most important meridians in the human body—as well as the hundreds of acupoints throughout the body were severed and blocked, there was no way to survive.

*Especially for a Murim practitioner.*

The so-called high risk, high return.

Through qi accumulation, a Murim practitioner gained abilities that surpassed those of ordinary people. But if their heart meridian was severed, they also got a bonus one-plus-one event called qi deviation.

Just like now.

“Cough. Kueeegh!”

Splaash!

Eyes, nose, mouth.

Ears.

Dark-red blood and pale lumps that looked like internal organs poured endlessly from every opening I could see.

At the sight of this horrifying scene, Namho and Taishan hurried over, then stopped short.

“Ugh. Taishan. I don’t want to look at this. I’m losing my appetite.”

“W-What is this?”

Namho swallowed dryly and asked in a lowered voice.

“Can they be saved?”

It was a meaningless question. The situation had already reached the point of no return.

Before I could answer, the heads of two of the men, whose entire bodies had been twitching and convulsing, fell limply to the side.

Thud.

There was no need to check. They were dead.

But it was still too early to give up. I grabbed the last masked man's wrist and poured my internal energy into him with all my strength.

Sssaaaaah.

As the Scorching Yang Qi carrying intense heat flowed into his body, I could feel his ruined insides.

Not a single internal organ remained undamaged, and the qi pathways that should have been broad and sturdy in a Peak master had collapsed like the walls of a dilapidated house.

*And on top of that, qi deviation…*

Even if Mungyeong, the greatest Divine Physician under Heaven, came here, he could not guarantee the man's life.

Realizing that he was beyond saving, I clenched my teeth.

*I have to find out. No matter what.*

I only needed one name. The name of the one person who had ordered today's attack.

I poured out my internal energy without restraint—not to control the masked man's insides, which had entered an irreversible state of rampage, but to fan his final ember into flame.

Rumble!

His entire body struggled violently as an even greater flow of internal energy entered him.

But just as the surface of a body of water grows calm after a violent storm has passed, the masked man on the threshold of death regained a brief moment of peace and reason.

A final rally.

This was truly the end. I stared into the masked man's eyes, which had regained their focus, and asked,

“Who was it? Speak.”

And then, as I pulled down the mask around his mouth to hear his final answer, I realized that this last attempt and question had been meaningless.

“Cough. Hhh. Haaah.”

“……!”

“Grrk. Uhh…”

His jaw moved up and down as though he were trying to say something. But no words came out.

No. The more accurate way to put it was that he could not speak.

As my mind froze like a stone statue, I heard Namho mutter with a groan.

“Such vicious bastards. Their tongues…”

His voice did not reach the end, and the masked man had been given far too little time.

“Grrk.”

With a death rattle that served in place of a last will, his pupils went blank. His mouth hung open, and the short tongue that had moved as though it were trying to say something went limp.

I stared silently at the man who had finally met his death, then spat out the curse I had been holding back.

“…Fuck.”

I had known they were no ordinary men, but I never imagined their tongues had been cut out.

There had been a reason they had not said a single word from beginning to end apart from their screams.

No. Even if they had wanted to speak, they couldn't.

“Hmm. The others are the same. Judging by how the severed ends of their tongues have healed, it looks like this was done a long time ago.”

Namho quickly examined the corpses like the Hidden Shadow Pavilion agent he was, then let out a low groan.

“These men… They’re all Nanman.”

“Are there no Han Chinese among them?”

“Not one. Their clothes are all identical, so we can’t even tell which tribe they belong to.”

The most reliable way to distinguish the Nanman was by their clothing and eating habits. But since every one of them wore black clothes and a mask, it was only natural that they were difficult to identify.

Besides, there was only a subtle difference between the appearances of Han Chinese and Nanman. Trying to identify their tribe at a glance was practically absurd.

“…Damn it.”

As I muttered a curse mixed with a sigh, Namho fixed me with a deeply serious gaze.

“When you were trying to persuade those men, you mentioned three great chieftains as possible culprits. So was the person who sent the missive Heugung?”

I looked at Namho in surprise.

That was answer enough.

“I see. So that’s what happened.”

“How did Elder Namho know…?”

“Baeksang and Yohi were both people who could reasonably be named as culprits. But Heugung was different. Thinking about it, there could only be one reason you would have thought of him in this situation.”

Namho finished speaking in a calm yet cold tone, then opened his mouth again.

“Was it him?”

“Yes.”

I nodded and continued.

“He was waiting for me at the place written in the missive.”

“He chose to hide in the forest rather than behind the rock. But no matter how many people there were, someone with Heugung’s build would have stood out. You mean he came out himself?”

“He had learned the Bone-Shrinking Technique. At first, I didn’t even suspect that he was Heugung.”

“Hah, the Bone-Shrinking Technique. He was a man with more secrets than he let on. He fooled everyone completely. Well, if he were really the man the world believed him to be, he wouldn’t have sent you a missive in the first place.”

Namho muttered as if to himself, then continued with a heavy expression.

“Go on.”

The story about Heugung had been short, but its contents were not something that could be dismissed.

Namho listened to the entire story without saying a word. Then he furrowed his already wrinkled brow even more deeply.

“What a goddamn mess.”

I agreed.

Something had happened, but I still could not narrow down the suspects.

Baeksang, Yohi, and Heugung. Given the circumstances, it was difficult to rule out any of them.

On top of that, the true force behind today's attack could be summed up in two words: Dark Heaven.

*I can tell just from the fact that they severed their heart meridians instead of taking a poison pill.*

Because of Nanman's characteristics, obtaining a deadly poison that could be used for suicide was incredibly easy. This was the sort of place where all kinds of venomous beasts swarmed even if you simply went on a picnic in the grass outside the Outer Palace.

But the masked men had chosen to sever their own heart meridians.

Compared to a fast and easy poison pill, severing one's heart meridian was a way to die after suffering several times more intense pain.

I had no choice but to assume that they already knew about it.

*The Myriad-Poison Ring. Dark Heaven must already know that I have it.*

Dark Heaven had sent the Blood Lord to cause the Shaolin Bloodshed, and in Sichuan, they had sent the Western Heaven Demon Lord to steal the sacred treasures of the Emei Sect and the Sichuan Tang Clan.

They had poured Supreme Peak masters who were no weaker than the Ten Kings—perhaps even comparable to the Three Saints—along with elite forces into the operation for the sake of those treasures.

*But even immediately after the Sichuan Blood Tragedy ended, nothing happened to the Sichuan Tang Clan.*

The Sichuan Tang Clan had staggered after suffering more severe damage than any other sect in Sichuan during its battle with the Western Heaven Demon Lord. But the follow-up attack from Dark Heaven that everyone had feared never came.

And I suspected that the decisive reason was whether or not they had the Myriad-Poison Ring.

*So instead of a poison pill, they severed their heart meridians to eliminate even the slightest possibility.*

A single drop of cold sweat ran down my spine.

My enemies were watching my every move, while I could not even identify the person hiding in the darkness.

The mere fact that an attack like this had taken place in the Inner Palace of the Nanman Beast Palace—the heart of Nanman—was threatening enough.

“When did the attack begin?”

Namho answered my question in a heavy voice.

“I don’t know exactly. I woke up in the middle of it, but… It seems to have started less than half a shichen after you left. I went to check because I wondered what was happening, and everything outside was in chaos. That bastard Sama Pyo was fighting while covered in blood.”

Namho pointed toward Sama Pyo, who was lying on the ground, then asked with concern in his eyes,

“But is he all right? He seems to have lost a lot of blood fighting them.”

“I stopped the bleeding, so he should be fine. From what I could see, he didn’t have any immediately dangerous wounds. Most of the blood on him seems to belong to the enemies.”

Taishan returned after dragging the corpses into one place and blinked his enormous eyes.

“Pavilion Master, true? Is Taishan’s Lord okay?”

“Yes. He only collapsed because he used too much strength.”

Apparently satisfied with the answer, Taishan's eyes filled with a cloudy film of tears.

“Sniff. Taishan was worried. If Lord died, Taishan would not eat meat for three years. Sniff.”

“……”

“……”

I had heard of a three-year mourning period, but this was the first time I had heard of a mourning custom that involved giving up meat for three years.

At that rate, he might become the strongest vegan in the Murim.

I swallowed the words rising in my throat and patted his Ural-Mountains-sized shoulder.

“Yes. You worked hard too.”

“Sniff. Taishan used lots of strength. Taishan hungry.”

“…Yeah. Okay.”

Should I just punch him?

But as I was deep in thought, countless footsteps began approaching from far away, accompanied by torchlight.

And with them came the familiar roar of a beast.

—Rooar!

Ssshhh! Pap!

A silver figure that stood out clearly in the darkness reached the clearing first.

Yayul Mok's face, as he rode atop the White Tiger, was stiff as a wooden doll.

“…I’m late.”

I answered calmly.

“Yeah. Late enough that it’s hard to believe something like this happened in the Inner Palace.”

Collapsed pavilions. Pools of blood gathered here and there. Corpses piled up in heaps.

Yayul Mok clenched his lips tightly before speaking.

“The warriors on patrol were dead. We only found out half a gak ago. And…”

The next moment, after hearing Yayul Mok's words, I could not help wondering whether I had heard correctly.

“Heugung and Yohi. Two great chieftains have disappeared.”

…What?
```
