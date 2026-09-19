<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0443.txt",
      "sha256": "6bf09aa558e8c2f28afc8ba8d28abc0903423cffb3225185933ab18c7355b8f2",
      "bytes": 13552
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "37dce80a24b35a28e3122811e9ee8eda5510704014dd132a3982982484ea9e93",
      "bytes": 2757
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "f9839ee43b346fe599d40a337b642d1f8c557e6b36e587d49687d1fbc37597e6",
      "bytes": 144663
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "a2a6692aece77cde8df16ca44dfe412af4108f5cd85d4a510946c759361db351",
      "bytes": 944
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "093a49f828946112c2cd967a0fc8d7a54bab1ab5d98df605f6600a618a185a4c",
      "bytes": 553
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "a6438d510e080880da879ecf62b6cb4d832fe047640a793b60a4345d5b7145a7",
      "bytes": 609
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "eb67328aeb391ec2323c2c3e28f399e68b7c9fc36a38cee5425c75fb1d18c3ee",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "38a70769c0a546f2fbc58e0d327521132650c5e7268b89ab677a77a336bca256",
      "bytes": 1390
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "db2abd5075d51c8b0c738888d583f666495983472798293fa7978e277e01eaba",
      "bytes": 2161
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "991328403d03b0a3097bf3c25c5d1e5713fe553ccc97bab610bf9e4adaf55ea4",
      "bytes": 1239
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "54c9762d7bfffebe90acec4ecb4deaf8751630a1ed754db8ce3162c70b4043d3",
      "bytes": 792
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "e3733e48a99b64c6c12c5fb62863c0bd18fd3954c9a4d7a6ca9798d0887183ed",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fd607b1d31fc804def3ff7ececdefae938e4f4547a807dba3bb439da4405549d",
      "bytes": 138961
    }
  ],
  "estimated_tokens": 13064
}
-->

# Durable State Update — Chapter 443

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 443. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 443. Profile updates may replace only one
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
  "chapter": 443,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 443,
    "continuity_sources": [443],
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
    "Jin Taekyung continues crossing between the modern world and Murim once or several times a day while handling obligations and investigating the shared symbols.",
    "The symbols found in the Arch Lich's magic circle and Dark Heaven's formations are the only known common ground between the two worlds, and Taekyung suspects they are connected to black magic.",
    "Both worlds are temporarily peaceful after recent crises, but Taekyung expects this calm to end in an approaching storm.",
    "The ship carrying Taekyung's group has reached Hubei Province after nearly ten days on the Yangtze.",
    "Peace Guild and Magic Johnson's Wizard Guild have entered an agreement that has drawn worldwide Hunter attention.",
    "The World Hunter Association recognizes Taekyung as an undeniable S-rank-level Hunter but has not issued his S-rank license; a testing team will be sent to Korea.",
    "Mungyeong remains with Taekyung's group while his former Divine Physician and Slaughter Saint identity remains concealed from most companions.",
    "The Skeleton King's undead identity remains concealed from the public, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "Taekyung has opened his Middle Dantian and is adapting to the resulting changes in his martial ability."
  ],
  "continuity_sources": [
    442
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations, and are they truly connected to black magic?",
    "Why does Mungyeong continue accompanying Taekyung's group despite being unable to explain the impulse?",
    "What confidential matter is Jin Wikyung withholding?",
    "What are the terms of the Peace Guild–Wizard Guild agreement, and what evidence is contained in Lee Jungryong's holographic recorder?",
    "How did Jin Taekyung actually open his Middle Dantian?"
  ],
  "safe_through": 442,
  "temporary_decisions": [
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor.",
    "Render 최 팀장님 as “Team Leader Choi” and 진태경 씨 as “Mr. Jin Taekyung.”",
    "Keep Peace Guild, guild house, Inventory, Magic Johnson, and established martial-arts terminology unchanged.",
    "Render 흑마법 as “black magic,” 독인 as “poison human,” 세계 헌터 협회 as “World Hunter Association,” and 위저드 길드 as “Wizard Guild.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 태원진가   | **Jin Family of Taiyuan**        |
| 제갈세가   | **Zhuge Clan**                   |
| 장강수로맹  | **Yangtze River Channel League** |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 정파     | **orthodox faction**                             |                                                       |
| 가주     | **Family Head**                              |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 선화아 | **Ship-Fire Boy** | Mu Song's sobriquet; literally a child who lights fires aboard a ship. |
| 채주 | **Stronghold Lord** | Title used for the lord of a water stronghold. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 사천성주 | **City Lord of Sichuan Province** | Title held by Won Gyun. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 수하 | 채주 | subordinate_to_stronghold_lord | Stronghold Lord | deferential | The subordinate calls Mu Song 채주 while reporting the nearby vessel. |
| 문경 | 무송 | survivor_to_savior_and_authority | Great Hero Mu Song | formal-deferential | Mungyeong credits Mu Song with saving him and asks him to spare Hwang Tae-gu. |
| 무송 | 문경 | stronghold_lord_to_young_passenger | you | gruff-but-considerate | Mu Song offers Mungyeong the right to decide Hwang Tae-gu's fate. |
| 무송 | 관리 | river-bandit leader to military official | General | casual-familiar | Uses 장군 while requesting permission to put passengers ashore. |
| 관리 | 무송 | military official to Stronghold Lord | Stronghold Lord | formal-polite | Uses 채주 while wishing Mu Song martial fortune. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 진위경 | 막내 | older brother to younger brother | my youngest | intimate and informal | Jin Wikyung uses 막내야 affectionately for Jin Taekyung. |
| 무송 | 적천강 | junior_martial_artist_to_legendary_martial_master | Great Hero Jeok | formal-deferential | Mu Song respectfully refers to Jeok Cheongang as 적 대협 while worrying that Jeok dislikes him. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 무송 | legendary martial master to stronghold lord | you | gruff, coercive, and dismissive | Uses 자네 while ordering Mu Song to take the group only as far as Sichuan and leave the fast ship. |
| 청풍 | 무송 | young martial companion to stronghold lord | you | cheerful and familiar | Offers Mu Song his last dumpling and then induces him to buy more in Guang'an. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 442
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 442
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 442
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Rival finalist alongside Baek Woo and Zhuge Gyun; trades insults with Taekyung and is helping investigate Tang Taesang’s murder through Beggars’ Sect intelligence.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 442
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 442
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is a legendary wandering martial master and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, and casually threatening or violent when dissatisfied. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 360
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention; recovered enough from his Internal Injuries to return to the Jin Family of Taiyuan, though he is not yet fully recovered; four days before this chapter, he lost his duel with Cheongpung after roughly three hundred exchanges, secluded himself to train, and sharpened his Sword Energy while resolving to surpass Cheongpung and the other geniuses; he remains secluded in the training hall, subsists on fasting pills, refuses all visitors, and will not return to Heaven’s Gate Temple until he achieves complete mastery; he has learned that Taekyung is leaving with Jeok Cheongang for a year and that Taekyung and Cheongpung plan to attend the Star-Array Grand Banquet in one year.
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away; three years earlier, he flatly refused seven-year-old Zhu Bao’s request for an autograph

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 437
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Taekyung's eldest brother and future Family Head; Taekyung trusts him as a martial-arts mentor and family protector. Member and acting leader of the Jin Family of Taiyuan. Commands Wipeng and the family's forces. Has worked with Jeok Cheongang, who trained Taekyung under Wikyung's arrangement. Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 438
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan and belongs to the Yangtze River Channel League's moderate faction.
- **Personality:** Ambitious, domineering, impatient with interruptions, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** He has carried Jin Taekyung's party and Mungyeong from Guang'an to Chengdu and agreed to send subordinates to help them return.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 442
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

## Korean source

```text
＃443화



열흘간의 항해는 결코 쉬운 일이 아니었다.

거대 크루즈 선도 아니고 목재로 만들어진 선박에서 퀴퀴한 선실과 축축한 갑판만을 오가야 했으니까. 항구? 빠듯한 일정 탓에 앞만 보고 나아갔다.

그런 사정이 있다 보니, 적천강은 물론이고 장강이 홈그라운드인 수적들마저 표정이 환해졌다.

물론 그중에서도 가장 기뻐하는 사람은 따로 있었다.

“오오, 드디어…….”

강제적인 재능기부로 호북성까지 오게 된 무송은 감격으로 몸을 부르르 떨었다.

쾌조선 한 척이 침몰한 이후로 상심에 젖어 있던 그는 지금까지의 고생을 모두 잊은 듯 힘찬 목소리로 외쳤다.

“닻을 내려라! 한시라도 빨리 이 지긋지긋한……!”

만족스럽게 고개를 끄덕이고 있던 적천강이 무송을 바라보았다.

“지긋지긋?”

무심코 본심을 내뱉은 무송이 엄청난 속도로 고개를 저었다.

“아, 아닙니다. 장강을 말한 겁니다.”

“당연히 장강이지. 노부도 그런 뜻으로 한 말인데?”

“…….”

“설마, 우리를 두고 지긋지긋하다고 한 건가?”

“그, 그럴 리가 있겠습니까.”

상당히 그럴 리 있어 보이는데.

적천강의 가늘어진 눈초리에 무송이 식은땀을 흘리는 동안 우두머리의 위기를 간파한 수적들은 잽싸게 움직였다.

서서히 속도를 줄인 쾌조선들이 줄을 지어 정박하고 닻을 내리자, 항구 근처에 모여 있던 사람들 사이에서 작은 웅성거림이 일었다.

“저 깃발은…….”

“장강수로맹. 장강수로맹이다!”

“밑에는 뭐라 적혀 있는 거야? 수룡채? 처음 들어보는데.”

“사천에 본거지를 둔 수채일세. 해상왕의 둘째 제자인 선화아(船火兒) 무송이 맡은 수채가 바로 수룡채야.”

“그렇게 말하니 들어본 것도 같군. 그런데 사천에 있어야 할 놈들이 왜 호북까지 온 거지?”

“난들 어찌 알겠나. 빌어먹을 수적 놈들. 가뜩이나 요즘 들어 분위기가 흉흉한데…….”

“쉿. 조용히 하게. 웬 젊은 놈이 이쪽을 보고 있어. 무림이랑 얽혀 봤자 좋을 게 없다고.”

나와 시선이 마주친 상인 무리가 황급히 자리를 떴다.

아니, 비단 그들뿐만이 아니었다. 얼굴이 새카맣게 탄 어부가 망을 챙겨 후다닥 물러나고, 잡은 물고기를 내다 팔던 장사치가 빛의 속도로 좌판을 접었다.

저 멀리에서는 관복을 차려입은 벼슬아치는 관군들의 호위를 받으며 이쪽을 예의주시하고 있었다.

그들의 눈빛에 서려 있는 것은 노골적인 경계심이었다.

‘이거 어째…… 사천 쪽과는 분위기가 영 딴판인데?’

장강수로맹이 제아무리 약탈을 근본으로 하는 수적 집단이라고 하지만 나름의 규칙과 체계가 잡혀 있다.

건수가 있다 하면 달려들어서 닥치는 대로 죽이고 모조리 털어 가는 식이 아니라, 때로는 무근본 수적으로부터 선박을 보호하고 평소에는 일정량의 통행세만 받고 통과시킨다고 들었다.

‘정마대전 당시에도 간을 좀 보긴 했지만 결국 정파 쪽에 붙었었고.’

오는 것이 있으면 가는 것도 있는 법.

장강수로맹은 천하 무림의 향방이 갈린 환란의 시기에 정파의 손을 들어 주었고, 관부에는 충분한 뇌물을 찔러 주었다.

그렇다 보니 양쪽에서 묵인하고 넘어가는, 쉽게 말하자면 합법의 탈을 쓴 용역 깡패가 바로 장강수로맹이다.

물론 그리 썩 좋은 놈들이라고는 할 수 없지만, 별의별 미친놈들이 날뛰는 무림 아닌가. 이 정도면 양반까진 아니더라도 그럭저럭 상놈 정도는 된다.

‘그래서 사천에서는 양민들도 별다른 반응이 없었는데.’

그냥 저 각설이 새끼들이 죽지도 않고 또 왔구나, 정도였지 지금처럼 대놓고 피하지는 않았다.

나는 뿔뿔이 흩어지는 사람들을 보며 고개를 갸웃거렸다.

‘지역마다 있는 분위기 차이. 뭐 그런 건가?’

하지만 그런 것 치고는 슬쩍 바라본 무송의 표정이 심상치 않다.

미간을 좁힌 채 순식간에 텅 빈 항구를 바라보던 그가 오른팔 격인 수하를 불렀다.

“본 맹의 형제들에게서는 연락이 없느냐?”

“예, 채주. 분명 우리가 오는 것을 알고 있었을 터인데, 어째서인지 아무 연통도 없습니다.”

“당양채와 홍호채에서도?”

“그렇습니다.”

“다른 곳은 몰라도 동정채(東湖寨)는 황 숙부께서 계신 곳이다. 우리가 온 것을 그분이 모르셨을 리가 없는데…….”

심각한 표정으로 중얼거린 무송이 수하를 향해 말을 이었다.

“하선(下船) 후 날랜 놈들을 풀어 상황을 알아봐라. 인근의 형제들에게도 즉시 연락을 취하도록.”

“존명.”

무송의 손짓에 휘하 수적들이 일사불란하게 움직였다. 일찌감치 하선 준비를 끝마친 우리도 예외는 아니었다.

드디어 장강을 벗어나게 된 적천강이 가장 빨리 앞장섰고, 그 뒤를 나와 진위경, 그리고 청풍과 혁무진, 궁기방이 차례대로 따랐다.

있는 듯 없는 듯 조용히 사람들 사이에 녹아든 문경은 덤이다.

드디어 상성 지역에서 벗어난 불 포켓몬, 적천강의 만면에 환한 웃음이 서렸다.

“후우, 이제야 좀 살겠군. 이래서 사람은 땅을 밟고 살아야 한다니까.”

하지만 적천강의 기쁨은 그리 오래가지 못했다.

“거기 잠깐.”

힘이 잔뜩 들어간 목소리. 어느새 다가온 벼슬아치가 우리를 바라보며 침을 꿀꺽 삼켰다.

그리고 자신의 뒤에 서 있는 수백의 관군을 돌아보더니 가슴을 펴며 말을 이었다.

“본관이 주위 말을 들어 보니 그대들이 사천에서 왔다던데. 맞나?”

“그대들? 맞나?”

눈을 껌뻑거린 적천강이 관리를 향해 되물었다.

“혹시, 지금 그거 노부에게 한 말이냐?”

“그렇다.”

“그렇다?”

관리의 눈빛이 불안하게 흔들렸다. 하지만 이내 마음을 다잡고 목소리를 키웠다.

“어허, 본관이 묻는 말에만 대답하거라. 어디에서 왔는지, 또 무슨 목적으로 왔는지 낱낱이 고하지 못할까!”

“어허? 하거라? 못할까?”

“아, 아니 이 늙은이가…….”

“늙은이?”

안 돼. 하지 마. 제발 그만둬.

훈남이 저렇게 되묻는 말투를 쓰면 여자들이 설렌다던데, 보는 사람 시선에서는 공포 영화가 따로 없다.

나는 적천강이 저 권위적인 관리의 가슴에 화염 신장을 날리기 전에 잽싸게 끼어들었다.

“저랑 이야기하시죠.”

“대가리에 피도 마르지 않은 어린놈과 나눌 이야기는 없다!”

“…….”

호랑이 아가리에 들어갔던 거 꺼내 줬더니 말하는 꼬라지 보소.

확 그냥 대가리를 날려 버리고 싶었지만, 꾹 참고 말을 이었다.

“사천에서 온 거 맞고, 볼일이 있어서 왔습니다.”

“하면, 그 볼일이라는 게 무엇이냐?”

“그게…….”

그 순간, 누군가가 잔뜩 신난 목소리로 외쳤다.

“다진 고추를 듬뿍 얹은 생선찜이요!”

“청풍, 이 개새끼야!”

“왜요, 은인. 그거 진짜 맛있는데. 둘이 먹다 하나가 죽어도 모르는데…….”

둘이 먹다 하나가 죽어도 모르는 맛인지는 몰라도, 관리의 눈에는 죽어야 할 놈들로 비친 것이 확실했다.

얼굴이 시뻘게진 관리가 고래고래 외쳤다.

“감히 본관을 능멸하다니!”

“잠깐만, 아저씨. 그게 아니라…….”

“장강수로맹의 깃발을 달고 사천에서 왔다는 것도 수상쩍기 짝이 없는데, 생선찜을 먹기 위해 와? 관을 봐야 눈물을 흘릴 놈들이로군. 여봐라, 당장 이 자들을 추포하라!”

“명을 받드옵니다!”

아니, 이 전개 뭔데.

뭐라 할 새도 없이 벌어진 돌발 상황. 군기가 바짝 든 관군 수백 명이 창을 들고 우리를 에워싼 그때, 작게 혀를 찬 진위경이 앞으로 나섰다.

“성질도 급하시구려.”

진위경은 현대의 관점에서 봐도 장신이지만, 무림에서는 거인으로 통한다.

우랄산맥 같은 어깨와 의복 위로 도드라진 근육을 바라본 관리가 마른침을 삼켰다.

“그, 그대는 누군가?”

“산서 태원진가의 진위경이라 하오. 긴말하지 않을 테니, 이쯤에서 수하들을 물리는 것이 어떻겠소?”

관리가 뭐라 대답하기도 전에, 진위경의 묵직한 목소리가 이어졌다.

“귀관이 아직 전달받지 못한 듯한데, 우리는 사천성주께 직접 통행을 허가받은 무림인들이오.”

“……사천성주께서?”

“미심쩍다면 확인해 봐도 좋소. 허나 그 전에 수하들을 물리는 것이 좋을 거요. 구태여 생목숨을 잃게 할 필요는 없을 테니.”

관리는 물론이고 우리를 둘러싼 관군들의 창끝이 움찔 떨렸다.

이들도 알고 있을 것이다. 자신들이 아무리 힘든 훈련을 거친 정예병이라고 해도 우리를 당해 낼 수 없다는 것을.

하지만 원래 피는 아랫놈이 흘리고, 자존심은 윗놈이 강한 법이다. 관리의 눈에 바짝 힘이 들어가는 것이 보였다.

“이자가 감히…… 본관이 누구인지 알고!”

진위경은 표정 하나 변하지 않고 입을 열었다.

“알고 있소. 호북성의 민정, 재정을 담당하는 승선포정사사에 적을 둔 건 당연할 테고. 관복을 보아하니 종육품 이문(理問)이시구려. 사법을 다루셔야 할 분께서 왜 여기까지 나와 애먼 사람을 붙잡고 있는지는 모르겠지만.”

“……!”

“아, 그건 그렇고 이 가에 홍천이라는 함자를 쓰시는 분을 알고 계시오?”

관리의 입술 사이로 떨리는 목소리가 새어 나왔다.

“그, 그분은 얼마 전에 새로 부임하신 포정사신데.”

“그렇군. 얼핏 이야기를 들어 본 것도 같았지. 산서 육조참정에서 호북성 승선포정사라. 영전하신 셈이니 축하할 일이구려.”

“호, 혹시 포정사님과 어떤 관계이신……?”

진위경이 빙긋 웃었다. 어느새 그의 태도와 말투는 자연스럽게 관리를 내려다보고 있었다.

“몇 번 만나 뵙고 술 한두 잔 했지. 필요할 때 도움도 드렸고.”

“헉!”

“왜. 더 듣고 싶은 말이 있나?”

“아, 아닙니다!”

빳빳하던 허리가 연체동물처럼 숙여졌다.

진위경을 향해 잽싸게 폴더인사를 한 관리가 수하들을 향해 호통쳤다.

“이놈들! 무엇 하느냐, 어서 그 흉한 날붙이를 치우지 않고!”

“예, 옛!”

“이런 경우도 모르는 놈들을 봤나! 부디 무례를 용서하십시오!”

진위경이 자애롭게 관리의 어깨를 토닥여 주었다.

“괜찮네. 살다 보면 오늘처럼 실수를 저지를 때도 있는 법이야.”

“대해와도 같은 마음씨에 이 손 모, 감읍할 따름입니다!”

“나 말고 이분들께 직접 사과드리게. 특히 자네가 처음 말을 걸었던 분은 무림의 존경받는 어른이시지.”

“저, 저는 그런 줄도 모르고. 하오면 혹시 별호를 여쭤봐도…….”

“화왕 적천강 대협이시네.”

“……!”

“사천혈사(四川血史) 직후 장강수로맹의 배를 빌려 타고 곧장 호북으로 온 참일세. 아, 물론 생선찜을 먹기 위해서 온 것만은 아니고.”

이제 그만해라, 애 울겠다.

자살이 마려운 표정으로 우리를 번갈아 보던 관리는 일 초에 다섯 번씩 허리를 접는 묘기를 펼쳤고, 진위경은 슬쩍 내 옆구리를 찔렀다.

“어떠냐, 막내야. 이 형님 멋있지?”

“……그 말만 안 했으면 멋있었을 텐데.”

“관부와 한 번 연을 맺으니 편한 점이 많더구나. 혹시 너도 곤란한 상황에 처한다면 내 이름을 대 보거라.”

이렇게까지 말할 정도면 뿌려 놓은 씨앗이 상당한 모양이다.

하긴, 궁기방의 말을 들어 보면 태원진가처럼 단기간에 이토록 급성장한 것은 정말 유례를 찾기 힘든 일이라고 했다.

지금 이 순간에도 태원진가에서 피나는 수련을 거듭하고 있을 진무경이 무공의 천재라면, 진위경은 가주로서 갖춰야 할 모든 것을 겸비한 올라운더라고 볼 수 있었다.

“막내야, 멋있지 않으냐? 응?”

“…….”

그래, 이런 것만 빼면 완벽한 가주다.

그렇게 내가 계속해서 질척거리는 진위경을 밀어 내고 있던 바로 그때였다.

“모두 물러나시오.”

심후한 공력이 실린 목소리와 함께, 항구에서 멀찍이 떨어져 웅성거리던 사람들이 좌우로 갈라섰다.

동시에 상당한 기운을 품은 수십의 무인들이 절도 있는 걸음으로 우리를 향해 다가왔다.

‘저건…….’

나는 눈을 가늘게 떴다. 그들이 걸친 새하얀 비단 무복에는 구름 같은 글씨체로 이렇게 쓰여 있었다.

제갈세가(諸葛世家).
```

## Final English reading copy

```markdown
# Chapter 443

Ten days of sailing had been anything but easy.

We hadn’t been traveling on some massive cruise ship. We’d been stuck on a wooden vessel, going back and forth between musty cabins and damp decks. Ports? With our schedule so tight, we’d simply kept our eyes ahead and sailed on.

Under the circumstances, even Jeok Cheongang—and the river bandits who called the Yangtze their home turf—looked delighted.

Of course, one person was happier than all the rest.

“Ohhh, finally…”

Mu Song, who had been forced into volunteering his talents all the way to Hubei Province, trembled with emotion.

He had been sunk in grief ever since one of his fast ships had gone down, but now he shouted in a powerful voice as if he had forgotten all the hardships he had endured.

“Lower the anchor! Get it down before another second passes and we can leave this damn—!”

Jeok Cheongang, who had been nodding in satisfaction, turned to look at him.

“This damn what?”

Mu Song had accidentally spoken his true feelings and shook his head at tremendous speed.

“N-no, sir. I meant the Yangtze.”

“Of course you meant the Yangtze. That’s what this old man meant, too.”

“…”

“Unless you were calling us damnable?”

“W-why would I ever do that?”

He certainly looked like he would.

While Mu Song sweated beneath Jeok Cheongang’s narrowed gaze, the river bandits immediately recognized their leader’s crisis and sprang into action.

The fast ships gradually slowed, lined up along the pier, and dropped anchor. A small murmur rose from the people gathered near the harbor.

“That flag…”

“The Yangtze River Channel League. It’s the Yangtze River Channel League!”

“What does it say underneath? Water Dragon Stronghold? I’ve never heard of it.”

“It’s a river stronghold based in Sichuan. Water Dragon Stronghold is the one led by Ship-Fire Boy Mu Song, the second Disciple of the Seafaring King.”

“Now that you mention it, I think I’ve heard of it. But why are those bastards in Hubei when they’re supposed to be in Sichuan?”

“How should I know? Damn river bandits. Things have been tense enough lately as it is…”

“Shh. Keep your voice down. Some young man is looking this way. Nothing good comes from getting tangled up with Murim.”

The group of merchants whose eyes met mine hurriedly left.

And they weren’t the only ones.

A fisherman with a face darkened by the sun grabbed his net and scurried away. A vendor selling his catch folded up his stall at the speed of light.

In the distance, an official dressed in formal robes watched us carefully while being escorted by government troops.

Their eyes held undisguised wariness.

*What the hell? This atmosphere is completely different from Sichuan.*

The Yangtze River Channel League might have been a river-bandit organization built on the foundation of plunder, but it had its own rules and system.

I had heard that they didn’t simply rush in whenever they saw an opportunity, kill everyone in sight, and strip a ship bare. Sometimes they even protected vessels from rogue river bandits, and under normal circumstances, they only collected a set toll before allowing ships to pass.

*They did test the waters during the Great Faction War, but in the end, they sided with the orthodox faction.*

When something comes in, something has to go out.

During the upheaval that decided the direction of the Murim world, the Yangtze River Channel League had supported the orthodox faction and paid the government enough bribes to keep everyone satisfied.

In other words, they were legal thugs for hire wearing the mask of legitimacy—tolerated by both sides and allowed to carry on.

They couldn’t exactly be called good people, but this was Murim, where all kinds of lunatics ran wild. Even if they weren’t gentlemen, they were at least respectable scoundrels.

*That’s why ordinary people in Sichuan didn’t react much.*

Their attitude had been more like, *Those vagrant bastards are back again, and they still haven’t died?* They hadn’t openly avoided us like this.

I tilted my head as I watched the people scatter in every direction.

*Is it just a difference in atmosphere from one region to another?*

But if that was all it was, Mu Song’s expression seemed far too grim.

He stared at the suddenly empty harbor with a deeply furrowed brow, then called over his right-hand man.

“Have we received no word from our brothers in the League?”

“No, Stronghold Lord. They must have known we were coming, but for some reason, there has been no contact.”

“Not even from Dangyang Stronghold or Honghu Stronghold?”

“That is correct.”

“Even if the others didn’t know, Donghu Stronghold is where Uncle Hwang is. There is no way he failed to hear that we were coming…”

Mu Song muttered with a serious expression before continuing,

“Once we disembark, send out the swiftest men and find out what is happening. Contact our nearby brothers immediately as well.”

“Yes, Stronghold Lord.”

At Mu Song’s gesture, the river bandits under his command moved as one. We were no exception. We had finished preparing to disembark some time ago.

Jeok Cheongang, who was finally leaving the Yangtze behind, led the way at once. I followed, then Jin Wikyung, Cheongpung, Hyuk Mujin, and Gung Gibang.

Mungyeong was there too, blending quietly into the crowd as if he were both present and absent.

At last, Jeok Cheongang—the Fire Pokémon finally free of his type disadvantage—wore a bright smile across his face.

“Whew. I can finally breathe again. This is why people are meant to live with their feet on land.”

But Jeok Cheongang’s happiness didn’t last long.

“You there. Stop.”

The voice was filled with authority. An official who had approached without us noticing swallowed nervously as he looked at us.

He glanced back at the hundreds of government troops standing behind him, puffed out his chest, and continued.

“I’ve heard from the people here that you came from Sichuan. Is that correct?”

“You people? Correct?”

Jeok Cheongang blinked and repeated the official’s words back at him.

“Are you addressing this old man?”

“That is correct.”

“That is correct?”

The official’s eyes wavered uneasily. But he quickly steeled himself and raised his voice.

“Ahem! Answer only what this official asks. State clearly where you came from and for what purpose!”

“Ahem? ‘Answer me’? ‘Why don’t you tell me’?”

“N-no, this old man…”

“This old man?”

*Don’t. Don’t do it. Please, just stop.*

They say women get butterflies when a handsome man repeats a question like that, but from the perspective of someone watching, it was nothing short of a horror movie.

I hurriedly stepped in before Jeok Cheongang could launch a Flame God Palm into the arrogant official’s chest.

“Why don’t you talk to me?”

“There’s nothing to discuss with a wet-behind-the-ears brat!”

“…”

I had just pulled him out of a tiger’s jaws, and this was how he talked to me?

I wanted to knock his head clean off, but I held back and continued.

“We did come from Sichuan, and we have business here.”

“Then what is this business?”

“Well…”

At that moment, someone shouted in a voice filled with excitement.

“Steamed fish topped with lots of minced chili peppers!”

“Cheongpung, you son of a bitch!”

“What? Benefactor, it really is delicious. It’s so good that if two people eat it and one of them dies, the other wouldn’t even notice…”

I didn’t know whether it was really so delicious that one person could die without the other noticing, but from the official’s expression, it was clear that we looked like people who ought to die.

His face flushed bright red as he bellowed,

“How dare you mock this official!”

“Wait, mister. That’s not what he meant…”

“It is suspicious enough that you came from Sichuan under the flag of the Yangtze River Channel League, and now you claim you came here to eat steamed fish? You’re the sort of people who won’t shed a tear until you see the coffin. Guards, arrest these men at once!”

“Yes, sir!”

What the hell was this development?

Before I could say another word, hundreds of government troops with military discipline drilled into them surrounded us with spears. Jin Wikyung clicked his tongue softly and stepped forward.

“You’re rather quick-tempered.”

Even by modern standards, Jin Wikyung was tall. In Murim, he was considered a giant.

The official swallowed hard as he looked at the Ural Mountains of his shoulders and the muscles bulging beneath his clothes.

“W-who are you?”

“I am Jin Wikyung of the Jin Family of Taiyuan in Shanxi. I won’t waste words, so why don’t you withdraw your men here?”

Before the official could answer, Jin Wikyung’s deep voice continued.

“It seems you haven’t been informed yet, but we are martial artists who received direct permission to pass from the City Lord of Sichuan Province.”

“The City Lord of Sichuan Province?”

“If you doubt me, you may verify it. But before that, it would be wise to withdraw your men. There is no reason to throw away perfectly good lives.”

The official flinched, and the spearpoints of the government troops surrounding us trembled as well.

They knew it too. No matter how hard they had trained or how elite they were, they couldn’t defeat us.

But that was how the world worked. The lower-ranked men shed the blood, while the higher-ranked men guarded their pride. I saw the official’s eyes harden.

“How dare you… Do you even know who this official is?”

Jin Wikyung didn’t change his expression as he opened his mouth.

“I do. You are naturally attached to the Hubei Provincial Administration Commission, which handles civil and financial affairs. Judging by your robes, you are a Judicial Inquirer of the secondary sixth rank. I do not know why someone responsible for legal matters has come all the way here to arrest innocent people, however.”

“…”

“Oh, by the way. Do you know a man surnamed Yi whose given name is Hongcheon?”

A trembling voice escaped between the official’s lips.

“T-that person is the Provincial Administration Commissioner who was newly appointed not long ago.”

“I see. I thought I had heard something about him. From Shanxi’s Assistant Administrator of the Six Ministries to Hubei’s Provincial Administration Commissioner. That is quite a promotion. It should be celebrated.”

“M-might I ask what your relationship is with the Provincial Administration Commissioner?”

Jin Wikyung smiled faintly. At some point, his posture and tone had naturally begun to look down on the official.

“I’ve met him a few times and shared a drink or two. I helped him out when he needed it.”

“Gasp!”

“What? Is there something else you’d like to hear?”

“N-no, sir!”

The official’s rigid back bent like a mollusk.

After quickly folding himself into a deep bow toward Jin Wikyung, he turned on his subordinates and roared,

“You fools! What are you doing? Put away those ugly blades at once!”

“Yes, sir!”

“Can you believe these idiots don’t even know how to handle a situation like this? Please forgive our rudeness!”

Jin Wikyung kindly patted the official on the shoulder.

“It’s all right. People make mistakes in life, like you did today.”

“This man Son can only be deeply grateful for your heart as vast as the sea!”

“Apologize to these men directly. Especially the man you spoke to first. He is a highly respected elder of Murim.”

“I-I had no idea. Then, might I ask his sobriquet…?”

“He is Great Hero Jeok Cheongang, the Fire King.”

“…”

“We came straight to Hubei after the Sichuan Blood History, traveling aboard a ship borrowed from the Yangtze River Channel League. Oh, of course, we didn’t come solely to eat steamed fish.”

*Stop it. You’re going to make him cry.*

The official kept looking back and forth between us with a face that seemed ready for suicide, bending at the waist five times a second.

Jin Wikyung then nudged me lightly in the ribs.

“What do you think, my youngest? Your big brother looks cool, doesn’t he?”

“…”

“You would have been cool if you’d stopped before that last line.”

“Once you establish a connection with the government, there are a lot of advantages. If you ever find yourself in a difficult situation, use my name.”

If he could say something like that with such confidence, he must have cultivated quite a few connections.

According to Gung Gibang, the Jin Family of Taiyuan’s meteoric rise over such a short period was virtually unprecedented.

If Jin Mukyung, who was undoubtedly continuing his grueling training at the Jin Family even now, was a genius of martial arts, then Jin Wikyung was an all-rounder who possessed everything a Family Head needed.

“My youngest, don’t you think I look cool? Hm?”

“…”

Yes. Apart from things like this, he was a perfect Family Head.

I was still trying to push away the increasingly clingy Jin Wikyung when it happened.

“Everyone, stand aside.”

At the sound of the deep voice infused with profound internal energy, the people who had been murmuring some distance away from the harbor split to either side.

At the same time, dozens of martial artists carrying considerable qi approached us with measured steps.

*That’s…*

I narrowed my eyes.

Written in cloud-like calligraphy across the pure-white silk martial robes they wore was:

**Zhuge Clan.**
```
