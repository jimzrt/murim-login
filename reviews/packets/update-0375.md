<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0375.txt",
      "sha256": "1d96babc0185becd710988c04518920d8460d80320b7eee0cfb4282dfda7e49d",
      "bytes": 13574
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "069fa0c15720d5e3e1687dfbf9076bacbf7176b15e5097ea9fc879e83d61c514",
      "bytes": 2782
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0ef527fb5a5da59c9dc7fe5ccbd0cb9f274c29c2598a7f9c7753eb48c05ca15e",
      "bytes": 130539
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "ae67a143962647e84240e2919300e928f790b1a82a2f6434fa760b339a183e7a",
      "bytes": 894
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "1791e28f114372679e31bab72e86b50aa45d1f5d7f10f2969ed46f220905adbb",
      "bytes": 570
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "72baa8f391cbefb0ed2624fc80f66503e0aeb8934a4ac803aeade1d79e9c7854",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "f96e018f842e5c7975536f15c4c13f31f47b7942dc0dde423460f217cbbb93fc",
      "bytes": 1390
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "44ef28f25004e295be6ba2154c23ebf75dd51dd8157be9ea66522374d921d6e1",
      "bytes": 1239
    },
    {
      "path": "characters/Pill Physician.md",
      "sha256": "c96f0bff64e078e86c83e0aa6c81221d78abdc2d414ef1e9783716d962d22102",
      "bytes": 554
    },
    {
      "path": "characters/Tang Horyong.md",
      "sha256": "ed95989275fe195d43f6828535993a2a7b07defd27cd0fd0c0c99405cd976abd",
      "bytes": 692
    },
    {
      "path": "characters/Tang Sadok.md",
      "sha256": "d02a06e86ca70542eaebfbf68b5660b6619734366c460ecab54fc5b36dfb7f40",
      "bytes": 751
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "0f5ff239d0c1f58cc43b4df7749500fc651741f1003fd4bc9be2b1d4ce80d1d5",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "a36c4049ef83903cf82daa1ac4594adb4e318c8e355a5400d85c9e72d42a248a",
      "bytes": 100013
    }
  ],
  "estimated_tokens": 12258
}
-->

# Durable State Update — Chapter 375

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 375. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 375. Profile updates may replace only one
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
  "chapter": 375,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 375,
    "continuity_sources": [375],
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

## Prior durable context

```json
{
  "active_continuity": [
    "The Sichuan Tang Clan is rebuilding seven days after the Three-Gate Bloodbath, which caused catastrophic casualties and ongoing funerals.",
    "Most Dark Heaven attackers involved in the Sichuan assault are dead or captured; Mungyeong captured the Third Fiend in the hidden cavern, while the Second Fiend's fate is unknown.",
    "Jin Taekyung is awake, has reached Level 120 and the Supreme Peak realm, manifested Force, and is publicly known as the Blazing Flame Divine Dragon.",
    "Jeok Cheongang is alive but remains weakened and is recovering his strength.",
    "Dong Feng's dantian and martial arts were destroyed while shielding Jeok Cheongang; the Divine Physician is Mungyeong's Master.",
    "Mungyeong is the Slaughter Saint and Dong Feng's Disciple; he has sworn never to kill again and intends to live as a medical apprentice.",
    "Hyuk Mujin and Gung Gibang remain badly wounded after fighting the Third Fiend.",
    "Cheongpung remains a Supreme Peak master at the Sichuan Tang Clan with Mimi.",
    "The Lord of Heaven temporarily possessed the Western Heaven Demon Lord's body and escaped after One Annihilation.",
    "The Myriad-Poison Ring remains in Jin Taekyung's possession and cannot be appraised by the System.",
    "A hidden cavern near Chengdu contains the inactive Moving Formation used by Dark Heaven; the Slaughter Saint identifies Dark Heaven as the successor to the Demonic Cult.",
    "Tang Sadok has awakened after prolonged unconsciousness; Jin Taekyung is preparing to leave with Jin Wikyung to escort the Third Fiend to Henan, while the Tang Clan weighs relocating its headquarters."
  ],
  "continuity_sources": [
    374
  ],
  "open_questions": [
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Why did Mungyeong tell the companions that Jin Taekyung ordered the rescue of Emei?",
    "What is the true nature and purpose of the Lord of Heaven, and what became of the Western Heaven Demon Lord?",
    "What was the origin and purpose of the Moving Formation, and why did it lose its power?",
    "How will Dark Heaven respond to the failed Three-Gate Bloodbath?"
  ],
  "safe_through": 374,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon.",
    "Use Mimi for 미미 and Mimi-chan for 미미쨩; render 삼괴 as Third Fiend in singular references and Three Fiends in collective references.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, and 신니 as Venerable Nun in forms of address.",
    "Render 환영진 as illusion formation and 이동진 as Moving Formation.",
    "Render 독룡각 as Poison Dragon Pavilion and 가주 대행 as Acting Family Head."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 아이템              | **Item**                       |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 노부      | **this old man / I**                                            |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 환의 | **Pill Physician** | Title of the current Family Head of the Seongsu Jang Family. |
| 당호룡 | **Tang Horyong** | Master of Poison Dragon Pavilion and Acting Family Head of the Sichuan Tang Clan. |
| 당사독 | **Tang Sadok** | Current Family Head of the Sichuan Tang Clan; also called the Myriad-Poison Asura. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 인의대협 | **Great Hero of Benevolence and Righteousness** | Flattering epithet Mungyeong uses for Mu Song. |
| 동봉 | **Dong Feng** | Personal name of the Divine Physician and Mungyeong's Master. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 미미쨩 | **Mimi-chan** | Affectionate form used for Tang Mimi. |
| 회오리치기 | **Whirlwind** | Technique Mimi-chan performs at Cheongpung's command. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 청풍 | 당사독 | young_martial_artist_to_Sichuan_Tang_Family_Head | Family Head | formal-deferential | Cheongpung addresses Tang Sadok as 가주님 while appealing for help. |
| 청풍 | 동봉 | newly_met_young_martial_artist_to_older_friend | Old Man Dong | casual and cheerful | Accepts Dong Feng's invitation to regard him as an older friend. |
| 당사독 | 동봉 | Tang Family Head to visiting physician | you | blunt and testing | Uses 그대 while demanding Dong Feng's identity and purpose. |
| 동봉 | 당사독 | physician to Family Head | you | formal-polite and measured | Uses 그대 while explaining that Tang Sadok must know Tang Mimi is unusual. |
| 서천마군 | 당사독 | hostile_opponents | you | calm and taunting | The Western Heaven Demon Lord uses 자네 while answering Tang Sadok's question. |
| 당사독 | 서천마군 | hostile_opponents | you bastard | hostile and threatening | Tang Sadok uses 네놈 after recognizing the disguised infiltrator. |
| 서천마군 | 청풍 | commander_to_young_opponent | you | gentle and taunting | Uses 자네 while identifying Cheongpung and discussing the Blood Lord. |
| 당사독 | 청풍 | family_head_to_younger_ally | greenhorn | blunt and protective | Tells Cheongpung not to interfere while calling him a 핏덩이. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 청풍 | 미미 | handler_to_companion_snake | Mimi | cheerful-commanding | Cheongpung repeatedly calls and commands the Thousand-Year Poison Horned Snake. |
| 진위경 | 당호룡 | orthodox ally to Tang Clan Acting Family Head | Sir Tang | formal and respectful | Jin Wikyung addresses Tang Horyong as 당 대협 while offering aid and discussing the Tang Clan's relocation. |
| 당호룡 | 진위경 | Tang Clan Acting Family Head to orthodox ally | Great Hero Jin | formal and respectful | Tang Horyong addresses Jin Wikyung as 진 대협 while thanking him for the offer of protection. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 373
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 374
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is the legendary physician also known as Dong Feng and Mungyeong's Master, whose dantian and martial arts were destroyed while shielding Jeok Cheongang.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** The Slaughter Saint is his Master, and Mungyeong is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 373
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 373
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is a legendary wandering martial master and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, and casually threatening or violent when dissatisfied. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 374
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Taekyung's eldest brother and future Family Head; Taekyung trusts him as a martial-arts mentor and family protector. Member and acting leader of the Jin Family of Taiyuan. Commands Wipeng and the family's forces. Has worked with Jeok Cheongang, who trained Taekyung under Wikyung's arrangement. Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Pill Physician.md

# Pill Physician (환의)

- **Safe through:** Chapter 346
- **Aliases:** None
- **Role:** Current Family Head of the Seongsu Jang Family in Shandong, who personally placed and signed the Thousand-Year Snow Ginseng in the casket entrusted to the Yongbong Escort Bureau.
- **Personality:** No personality traits are established.
- **Voice:** No voice traits are established.
- **Relationships:** The Pill Physician heads the Seongsu Jang Family, a prestigious medical family in Shandong.

### Tang Horyong.md

# Tang Horyong (당호룡)

- **Safe through:** Chapter 374
- **Aliases:** None
- **Role:** Master of Poison Dragon Pavilion and Acting Family Head of the Sichuan Tang Clan while Tang Sadok is incapacitated.
- **Personality:** A natural martial artist who is skilled with poison and hidden weapons but anxious and overwhelmed by the burden of leading the devastated clan.
- **Voice:** Candid, deferential, and worried when discussing the Tang Clan's future.
- **Relationships:** Younger cousin of Tang Sadok and a senior leader of the Sichuan Tang Clan; he receives Jin Wikyung's offer of orthodox protection and relocation.

### Tang Sadok.md

# Tang Sadok (당사독)

- **Safe through:** Chapter 374
- **Aliases:** Myriad-Poison Asura
- **Role:** Current Family Head of the Sichuan Tang Clan, gravely wounded in the Three-Gate Bloodbath but alive and newly awakened after prolonged unconsciousness.
- **Personality:** Grim, cold, blunt, suspicious, and unsentimental, with fierce concern for the Tang Clan’s affairs.
- **Voice:** Hissing, curt, authoritative, and threatening.
- **Relationships:** Tang Taesang was his father and predecessor as Family Head, his unnamed nephew serves as Master of the Gatekeeper Pavilion, and the Thousand-Year Poison Horned Snake was his father's final gift and is his cherished companion.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 374
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃375화



병문안에도 순서가 있는 법.

가주이자 가문의 웃어른인 당사독이 깨어났다는 소식에, 당문의 식솔들은 만사를 제치고 달려왔다.

그러나 백여 명이나 되는 인원 모두가 당사독을 볼 수 있는 것은 아니었다.

“은인, 우린 언제쯤 당 할아버지를 뵐 수 있어요?”

“글쎄. 앞에 사람들이 들어간 지 꽤 됐으니까 슬슬 나오지 않을까.”

“아, 그렇구나.”

내 대답에 청풍이 고개를 끄덕인다.

아니, 잠깐만. 청풍?

“뭐야, 언제 왔어?”

“방금요.”

너무 자연스럽게 끼어들어서 있는 줄도 몰랐다. 그런데 이놈이 여길 왜 찾아왔지?

내 의문을 읽기라도 한 것처럼 청풍이 자신의 가슴팍을 가리키며 대답했다.

“미미가 보고 싶다고 해서요.”

“……?”

내가 지금 도대체 뭘 들은 거지.

이제는 하다 하다 의사소통까지 하다니. 이 자식 혹시 화산파가 아니라 슬리데린 출신인가.

심상치 않은 내 시선에 청풍이 고개를 갸웃했다.

“제 이마는 갑자기 왜 쳐다보세요? 뭐 묻었어요?”

“그냥. 이마에 번개 모양 흉터라도 있나 확인해 봤어.”

“네?”

“그런 게 있다.”

말이 끝난 그 순간.

덜컥.

굳게 닫혀 있던 의방의 문이 열리고 십여 명의 사람들이 모습을 드러냈다.

그들은 몇 남지 않은 사천당문의 직계들로, 그중에는 일면식이 있는 당호룡 역시 포함되어 있었다.

“후우…….”

붉게 충혈된 눈으로 하늘을 올려다본 그가 이쪽을 향해 걸어왔다.

“가주께서 뵙고자 하시오.”

“기다리고 있었습니다.”

고개를 끄덕인 진위경이 앞장서고, 나와 청풍이 그 뒤를 따라 의방으로 들어갔다.

사방에서 진동하는 탕약 냄새를 맡으며 얼마나 걸었을까. 하얀 천으로 코와 입을 가린 의원이 안내해 준 의실로 들어서자, 마침내 낯익은 얼굴들과 마주할 수 있었다.

“쿨럭, 왔는가.”

힘겹게 잔기침을 내뱉는 당사독의 상태는 한눈에 보기에도 심각했다.

부러진 팔다리와 내상으로 인해 불안정한 기운.

상반신을 일으키려는 그를, 우리와 눈인사를 주고받은 신의(神醫)가 만류했다.

“가주, 제가 움직이지 말라 하지 않았습니까.”

“노부는 죄인일세. 죽어 마땅한 죄를 지었으니 벌을 청하는 것이 이치지.”

창백한 얼굴로 고개를 저은 당사독이 나를 똑바로 응시하며 말을 이었다.

“구차한 변명은 하지 않겠네. 서천마군이 지하 뇌옥으로 향한 것은, 노부가 알려 주었기 때문일세.”

나는 비스듬히 팔짱을 꼈다.

“아, 어쩐지.”

“……?”

“왜요.”

당사독이 당황한 얼굴로 물었다.

“아, 알고 있었나?”

“당연히 처음에는 몰랐죠. 그때는 워낙 정신이 없기도 했고. 그런데 나중에 곰곰이 생각해 보니까 서천마군. 그 새끼가 어떻게 만독지환의 위치를 알았나 싶더라고요.”

애당초 만독지환의 위치를 아는 사람은 극소수.

청풍은 겉보기에는 꽃잎처럼 가벼워 보여도 나무뿌리처럼 단단한 놈이니, 발설할 만한 사람은 당사독 한 명밖에 없었다.

“왜 그랬습니까?”

“……만독지환의 위치를 알려 주면 가문의 명맥을 보존해 주겠다 하더군.”

“그걸 믿었어요?”

“노부가 어리석었네. 잠시 판단력이 흐려져, 해서는 안 될 일을 저질렀지.”

“알고는 계시네요.”

나를 바라보는 당사독의 눈빛이 파르르 떨렸다.

“이 늙은이가 목숨을 건사할 수 있었던 것은, 자네들에게 사죄하고 벌을 받으라는 하늘의 뜻이겠지.”

“그럼 가주께서는 어떤 벌을 원하십니까.”

불쑥 들려온 차가운 목소리의 주인은 아무 말 없이 대화를 듣고 있던 진위경이었다.

“태원진가의 소가주 되시는가.”

“예. 두 아우를 자식처럼 키운 형이기도 하지요.”

깊게 가라앉은 진위경의 눈동자에서 숨길 수 없는 분노가 진득하게 묻어나왔다.

“정도(正道)를 걷는 이라면 해서는 안 될 짓이었습니다.”

“알고 있네. 아니, 알고 있소. 그렇기에 죄를 청하는 것이오.”

“자결하라 한다면 어쩌시겠습니까.”

“……!”

나를 포함한 모두가 놀란 눈빛으로 진위경을 바라봤다.

그러나 한 사람, 당사독만은 예외였다.

그는 담담하기 그지없는 표정으로 입을 열었다.

“나는 도의(道義)를 저버렸으나, 그대들이 목숨을 내놓고 싸워 준 덕분에 본가의 명맥을 이을 수 있게 되었소. 이 보잘것없는 늙은이의 목숨으로 사죄를 대신할 수 있다면, 흔쾌히 그리하리다.”

짧은 침묵 뒤에 이어진 것은 진위경의 한숨이었다.

“후우…….”

복잡한 눈빛으로 당사독을 바라보던 그가 나를 향해 고개를 돌렸다.

“어찌하겠느냐?”

“……뭘요. 자결?”

“그 무엇이든.”

갑자기 손에 칼자루가 쥐어지니 심장이 쫀득해지는 기분이다.

더군다나 그 칼자루 끝에 달린 것이 사천당문 가주의 목숨이라고 하니 더더욱 그랬다.

‘갑자기 분위기 싸해진 것 보소.’

물론 허허 웃고 넘어갈 일은 아니다. 내가 무슨 공명정대하고 속 넓은 인의대협도 아니고, 솔직히 사건의 전말을 깨달았을 때는 슬그머니 분노가 솟구치기도 했다.

당시에는 나뿐만 아니라 모두의 목숨이 걸려 있는 상황이었으니까.

하지만…….

“됐습니다. 그렇게까지 하고 싶지는 않네요.”

그래, 한편으로는 당사독의 입장을 이해한다.

얼굴 몇 번 본 것이 고작인 외부인과 일가의 가주로서 목숨 걸고 지켜야 할 혈육을 저울에 올려 둔다면 나 역시 그와 같은 선택을 했을 것 같았다.

‘그전에 빚도 있었고.’

적천강이 깨어날 수 있었던 것에는 당사독의 도움도 크게 한몫했다.

비록 모종의 거래가 있었다고는 하나, 한 핏줄에게도 알리지 않은 신물을 빌려준 사람 역시 당사독이었다.

“그러니까 이걸로 쌤쌤. 퉁 치죠. 아니, 그건 너무 나갔고 이번 일로 사천당문이 저희에게 큰 빚을 진 것으로 하자고요.”

내 말이 끝나자 청풍과 신의가 입을 열었다.

“은인이 위험해졌던 건 분명히 당 할아버지의 잘못이지만…… 저도 은인의 뜻에 따를래요.”

“전 이미 잊었습니다. 다만 의원으로서 바라는 것이 있다면 가주께서 하루빨리 쾌차하는 것이지요. 아직 살아남은 식솔들이 있지 않습니다.”

마지막으로 입을 연 것은 진위경이었다. 처음과 달리 그에게서는 더 이상 어떤 분노도 느껴지지 않았다.

아니, 어쩌면 진위경은 처음부터 내 대답을 알고 있었을지도 모르겠다.

“그렇다는군요. 가주의 생각은 어떠하십니까.”

“……!”

우리를 바라보는 당사독의 눈동자가 격동으로 떨렸다.

짧은 침묵이 흐른 뒤, 갈라진 목소리가 그의 입술 사이로 흘러나왔다.

“노부가, 사천당문이 그대들에게 큰 은혜를 입었구려.”

당사독이 진심을 담아 고개를 숙인 바로 그 순간이었다.

띠링. 띠링. 띠링.



- 자신의 죄를 고백하는 것은 어렵지만, 그보다 더 큰 용기를 필요로 하는 것이 있습니다. 바로 용서입니다.

- 히든 퀘스트, [사죄와 용서]를 성공적으로 완료했습니다!

- [Lv.115 당사독]이 당신들의 호의에 깊은 감사를 표합니다. 그와 [사천당문]은 결코 오늘의 호의와 도움을 잊지 않을 것이며, [사천당문]의 사람들은 당신을 은인으로 기억할 것입니다!

- 칭호, [당문의 은인]을 획득했습니다!

- 히든 퀘스트 완료 보상으로 막대한 경험치와 명성을 얻었습니다!

- 레벨 업!



뭐야, 이거. 갑자기 히든 퀘스트라니.

내가 뜬금없이 울려 퍼진 시스템 알림에 얼떨떨해하던 그때, 차가운 무언가가 다리 사이를 스치며 지나갔다.

취릭, 취리리릭.

“미미, 이 녀석.”

오랜만에 해후하는 미미와 당사독의 모습에, 잠시 깜빡하고 있던 물건 하나가 떠올랐다.

“아, 그러고 보니 만독지환 말인데요. 다행히 제가 지금까지 잘 갖고 있었…….”

“그런가?”

내가 미처 말을 끝맺기도 전에, 불쑥 입을 연 당사독이 말을 이었다.

“그럼 계속 갖고 있으시게.”

“예, 그럼 제가 계속…… 예?”

“자네에게 본가의 신물을 맡기겠네. 은인에 대한 증표이니 부디 거절하지 말아 주게.”

띠링.



- 소유자의 뜻에 따라 [만독지환]이 당신에게 양도되었습니다!

- 새로운 아이템이 당신에게 종속됩니다!

- 현재 보유 중인 종속 아이템 : [백염], [만독지환], [???].

- 아직 이름이 정해지지 않은 종속 아이템이 있습니다. 새로운 이름을 부여해 주십시오.



아니, 오늘 무슨 날이야?

도대체 앞으로 어떤 개 같은 일들이 벌어지려고 이렇게 퍼 주나 싶어 불안하기까지 할 지경이다.

금붕어처럼 입만 벙긋거리는 내 모습에, 당사독이 희미한 미소를 머금었다.

“다들 원하는 것들이 있다면 말씀하시구려. 본가의 역량이 닿는 한 무엇이든 들어드리리다.”

신의가 따라 웃으며 대답했다.

“원하는 것이라면, 그저 병자들이 하루빨리 낫길 바랄 뿐입니다.”

“허어.”

과연 신의다운 대답이다. 아니, 이제는 동봉이라고 해야 하나.

하지만 한 가지 확실한 것은, 그 역시 또 다른 한 사람의 신의(神醫)라는 사실이었다.

“자네는 무엇을 원하는가?”

갑작스러운 질문에 청풍이 화들짝 놀랐다.

“저, 저요?”

당사독이 고개를 끄덕이자 청풍이 손발을 배배 꼬며 대답했다.

“저어는…… 그러니까요. 으음. 없어요.”

“정말인가?”

“네에. 없는 것 같아요.”

“…….”

“…….”

야, 이 자식아. 미미쨩한테서 눈이나 떼고 얘기해.

거울을 가져와서 보여 주고 싶다. 지금 청풍의 눈동자에는 미미쨩을 향한 애절함과 갈망이 떠올라 있었다.

저러다가 뱀 가죽이 뚫리겠다 싶던 그때, 당사독이 입을 열었다.

“이 녀석은 내 오랜 친우일세. 지난 수십 년 동안, 노부가 아무에게도 드러내지 못했던 희로애락(喜怒哀樂)을 나눌 수 있었던 유일한 존재였지.”

청풍이 측은해진 눈빛으로 당사독을 바라봤다.

“당 할아버지께서는 다른 친구가 없으시군요.”

“만들지 않았다네. 노부에게 당문의 가주란 그런 자리였으니까.”

“그래서 친구가 없으시군요.”

“없던 게 아니라. 만들 수 있었는데…….”

“친구 하나 없었군요. 불쌍해라.”

“…….”

신의가 다급하게 당사독의 어깨를 붙잡았다.

“가주. 진정하십시오. 호흡이 너무 가파릅니다!”

“후욱, 후우욱.”

“크고 천천히 호흡하십시오. 자, 저를 따라서 하나, 둘…….”

“후우우우욱…….”

잠시 후, 간신히 고혈압의 위기에서 벗어난 당사독이 청풍을 바라보며 입을 열었다.

“하지만 자네에게 미미를…….”

청풍이 두 손으로 입을 틀어막았다.

“아니에요. 당 할아버지. 할아버지의 유일한 친구를 데려갈 수는 없어요.”

“……아직 맡기겠다고 하지 않았는데.”

“앗. 아앗.”

당사독이 한숨을 푹 내쉬었다. 잠깐이었지만 저런 놈한테 미미쨩을 맡겨도 되나, 하는 생각을 했음이 틀림없었다.

“그래, 자네의 짐작대로일세. 향후 본가의 향방이 어떻게 될지 모르는바, 노부는 자네에게 미미를 맡기고자 하네. 물론 임시로.”

“와아!”

“마지막에 했던 말 들었나? 임시일세.”

“와아아!”

못 들었다에 혁무진 오른손 손목을 건다.

미미의 임시보호자가 된 청풍은 기뻐서 어쩔 줄을 몰라 했다.

“걱정 마세요. 잘 돌볼게요!”

“지난번에 본 바에 의하면 미미가 자네를 잘 따르는 것 같긴 하지만, 녀석은 본래 성정이 까다롭고 낯을 많이 가리니…….”

“미미. 회오리치기 후 뱅글뱅글 돌고 인사하기!”

취리리릭!

“오메, 시벌.”

여기서 신기술을 써 버리네.

생전 처음 보는 광경에 반쯤 넋이 나가 있던 진위경이 얼빠진 목소리로 중얼거렸다.

“가주께서 걱정하시는 일은 없을 것 같군요.”

당사독의 눈동자에 지진이 일어났다.

당사독은 진위경과 긴히 나눌 말이 있다며 따로 자리를 청했고, 나와 청풍은 먼저 방을 빠져나왔다.

아니, 지금 막 한 사람이 추가되었다.

“진 소협. 잠시 이 늙은이에게 시간을 내어줄 수 있겠소?”

“저요?”

신의가 잔잔한 웃음과 함께 고개를 끄덕였다.

“떠나기 전에 꼭 부탁하고 싶은 것이 있소.”
```

## Final English reading copy

```markdown
# Chapter 375

Even paying a visit to the sick has an order to it.

When word spread that Tang Sadok—the Family Head and senior patriarch of the clan—had awakened, the members of the Tang Clan dropped everything and came running.

However, not all of the more than one hundred people could see Tang Sadok.

“Benefactor, when can we go see Grandpa Tang?”

“Hard to say. The people who went in ahead of us have been there for quite a while, so they should be coming out soon.”

“Oh, I see.”

Cheongpung nodded at my answer.

Wait. Cheongpung?

“What are you doing here? When did you get here?”

“Just now.”

He had slipped into the conversation so naturally that I hadn’t even realized he was there. But why had he come here?

As if he had read my question, Cheongpung pointed to his chest and answered,

“Mimi said she wanted to see him.”

“...?”

What had I just heard?

*Now he could even communicate with a snake.*

Was this guy actually from Slytherin instead of Huashan?

At my suspicious stare, Cheongpung tilted his head.

“Why are you suddenly looking at my forehead? Is there something on it?”

“I was just checking whether you had a lightning-shaped scar on your forehead.”

“What?”

“There is such a thing.”

The instant I finished speaking—

Clunk.

The tightly closed door of the medical room opened, and about a dozen people emerged.

They were among the few remaining direct members of the Sichuan Tang Clan. Tang Horyong, whom I had met before, was among them.

“Whew...”

His eyes bloodshot, he looked up at the sky before walking toward us.

“The Family Head wishes to see you.”

“We’ve been waiting.”

Jin Wikyung nodded and led the way. Cheongpung and I followed him into the medical room.

After walking for some time with the smell of herbal decoctions vibrating through the air around us, we entered the treatment room guided by a physician whose nose and mouth were covered by a white cloth.

At last, we came face-to-face with several familiar people.

“Cough... You came.”

Tang Sadok’s condition was obviously serious. His limbs were broken, and the qi in his body was unstable from his internal injuries.

The Divine Physician, who exchanged a brief glance with us, stopped Tang Sadok as he tried to sit up.

“Family Head, didn’t I tell you not to move?”

“This old man is a sinner. I committed a crime deserving of death, so it is only right that I ask for punishment.”

Tang Sadok shook his pale face and continued, staring directly at me.

“I will not make any pitiful excuses. The reason the Western Heaven Demon Lord headed for the underground prison was because I told him about it.”

I folded my arms at an angle.

“Ah. No wonder.”

“...?”

“Why?”

Tang Sadok asked with a flustered expression.

“Ah, you knew?”

“Of course I didn’t know at first. Things were too hectic back then. But when I thought about it later, I started wondering how the hell that bastard had learned the location of the Myriad-Poison Ring.”

Only a tiny number of people knew where the Myriad-Poison Ring was.

Cheongpung might have looked as light as a flower petal on the outside, but he was as solid as a tree root. Tang Sadok was the only person who could have let it slip.

“Why did you do it?”

“He said that if I told him where the Myriad-Poison Ring was, he would preserve our family’s bloodline.”

“And you believed him?”

“This old man was foolish. My judgment was clouded for a moment, and I committed an act I should never have committed.”

“At least you realize that much.”

Tang Sadok’s eyes trembled as he looked at me.

“The reason this old man was able to keep his life must have been Heaven’s will. I was spared so that I could apologize to you and receive my punishment.”

“Then what punishment do you want, Family Head?”

The cold voice belonged to Jin Wikyung, who had been silently listening to our conversation.

“Are you the Lesser Family Head of the Jin Family of Taiyuan?”

“Yes. I am also the elder brother who raised my two younger brothers as if they were my own sons.”

Unmistakable anger clung thickly to Jin Wikyung’s deeply settled eyes.

“It was something no one who walks the righteous path should have done.”

“I know. No—I know, Young Hero Jin. That is why I am asking for punishment.”

“What will you do if I tell you to kill yourself?”

“...!”

Everyone, myself included, stared at Jin Wikyung in shock.

Everyone except Tang Sadok.

He opened his mouth with an utterly calm expression.

“I betrayed the principles of the Way, but thanks to you all risking your lives and fighting for us, my family will be able to continue its bloodline. If I can use this insignificant old man’s life to atone, I will gladly do so.”

After a brief silence, Jin Wikyung let out a sigh.

“Whew...”

He looked at Tang Sadok with complicated emotions before turning toward me.

“What will you do?”

“...Do about what? Kill him?”

“Anything.”

Having the hilt of a sword suddenly placed in my hand made my heart clench.

Even more so when I realized that the life of the Family Head of the Sichuan Tang Clan was hanging from that hilt.

*Look how icy the mood suddenly got.*

Of course, this was not something I could simply laugh off. I wasn’t some perfectly fair-minded, broad-hearted Great Hero of Benevolence and Righteousness. When I understood the full truth of what had happened, anger had quietly surged up inside me.

At the time, everyone’s lives had been on the line—not just mine.

But...

“Enough. I don’t want to take it that far.”

That was right. On the other hand, I understood Tang Sadok’s position.

If I had to place a blood relative whom I was duty-bound to protect as the Family Head on one side of a scale, and an outsider whose face I had seen only a few times on the other, I felt like I might have made the same choice.

*Besides, I already owed him one.*

Tang Sadok’s help had played a major role in allowing Jeok Cheongang to awaken.

Even if there had been a certain deal involved, Tang Sadok had still been the one who lent us a sacred treasure without telling even his own blood relatives.

“So let’s call it square. No, that’s going too far. Let’s just say the Sichuan Tang Clan owes us a huge debt because of what happened this time.”

When I finished speaking, Cheongpung and the Divine Physician spoke up.

“It was definitely Grandpa Tang’s fault that Benefactor was put in danger... but I’ll follow Benefactor’s wishes, too.”

“I have already forgotten about it. If I have one wish as a physician, it is for the Family Head to recover as soon as possible. There are still clan members who survived, aren’t there?”

The last person to speak was Jin Wikyung. Unlike before, there was no longer any anger in his voice.

No—perhaps he had known my answer from the beginning.

“So that is what they say. What do you think, Family Head?”

“...!”

Tang Sadok’s eyes trembled violently as he looked at us.

After a brief silence, a hoarse voice slipped between his lips.

“This old man... The Sichuan Tang Clan has received an enormous kindness from you.”

It was at that moment, just as Tang Sadok sincerely bowed his head, that—

Ding. Ding. Ding.

> **System**
>
> Confessing one’s sins is difficult, but there is something that requires even greater courage than that.
>
> Forgiveness.
>
> **Hidden Quest, “Atonement and Forgiveness,” successfully completed!**
>
> **Level 115 Tang Sadok** expresses his deep gratitude for your goodwill. He and the **Sichuan Tang Clan** will never forget the goodwill and assistance you showed them today, and the people of the **Sichuan Tang Clan** will remember you as their Benefactor!
>
> You acquired the **Title: Tang Clan’s Benefactor**!
>
> You received a massive amount of **EXP** and **Fame** as a reward for completing the Hidden Quest!
>
> **Level Up!**

What the hell? A Hidden Quest all of a sudden?

While I was still dazed by the unexpected System notification, something cold brushed between my legs and slipped past.

Sssrikk, sssriririk.

“Mimi, you little rascal.”

Seeing Mimi and Tang Sadok reunited after so long reminded me of something I had momentarily forgotten.

“Oh, right. Speaking of the Myriad-Poison Ring... Luckily, I’ve kept it safe all this time—”

“Is that so?”

Before I could finish, Tang Sadok cut in.

“Then continue keeping it.”

“Yes, then I’ll continue keeping it... Wait, what?”

“I will entrust our family’s sacred treasure to you. It is a token of our gratitude toward our Benefactor, so please do not refuse.”

Ding.

> **System**
>
> At the owner’s request, **Myriad-Poison Ring** has been transferred to you!
>
> A new Item is now bound to you!
>
> **Bound Items currently in your possession:** White Flame, Myriad-Poison Ring, ???
>
> You have a bound Item whose name has not yet been determined. Please give it a new name.

What was with today?

I was starting to feel uneasy, wondering what kind of shitty things were about to happen for me to be showered with rewards like this.

Seeing me gape soundlessly like a goldfish, Tang Sadok smiled faintly.

“If there is anything you want, tell me. As far as our family’s abilities allow, I will grant you anything.”

The Divine Physician smiled along with him and answered,

“If there is something I want, I simply hope that the patients recover as soon as possible.”

“Oh?”

That was an answer worthy of the Divine Physician. Or should I call him Dong Feng now?

But one thing was certain: he was another true Divine Physician.

“What do you want?”

Cheongpung jumped at the sudden question.

“M-Me?”

Tang Sadok nodded, and Cheongpung twisted his hands and feet as he answered.

“I... Well. Hmm. I don’t have anything.”

“Are you sure?”

“Yes. I don’t think I have anything.”

“...”

“...”

*Hey, you little bastard. Take your eyes off Mimi-chan and talk.*

I wanted to bring him a mirror and show him what he looked like. His eyes were filled with aching longing and desire for Mimi-chan.

*At this rate, he’s going to bore a hole through her scales.*

Just then, Tang Sadok spoke.

“This fellow is my old friend. For the past several decades, Mimi was the only one with whom I could share all the joy, anger, sorrow, and pleasure I could never show anyone else.”

Cheongpung looked at Tang Sadok with pity.

“Grandpa Tang doesn’t have any other friends.”

“I did not make any. Being the Family Head of the Tang Clan was that kind of position.”

“So you don’t have any friends.”

“It is not that I had none. I could have made some, but...”

“You didn’t have a single friend. How sad.”

“...”

The Divine Physician hurriedly grabbed Tang Sadok by the shoulder.

“Family Head, please calm down. Your breathing is much too rapid!”

“Huff... Hoo, huff...”

“Take deep, slow breaths. Now, follow me. One, two...”

“Whoooosh...”

A short while later, Tang Sadok had barely escaped a bout of high blood pressure. He looked at Cheongpung and spoke.

“But I could give you Mimi...”

Cheongpung covered his mouth with both hands.

“No, Grandpa Tang. I can’t take your only friend away from you.”

“...I have not yet said that I would entrust her to you.”

“Oh. Oh, no.”

Tang Sadok let out a deep sigh. For a moment, he had undoubtedly wondered whether it was really safe to entrust Mimi-chan to someone like that.

“Yes, just as you guessed. We do not know what path our family will take from here, so I wish to entrust Mimi to you. Temporarily, of course.”

“Yaaay!”

“Did you hear what I said at the end? Temporarily.”

“Yaaay!”

*I’ll bet Hyuk Mujin’s right wrist that he didn’t hear that.*

Cheongpung, now Mimi’s temporary guardian, did not know what to do with his happiness.

“Don’t worry. I’ll take good care of her!”

“From what I saw last time, Mimi does seem to follow you well. However, she is naturally quite fussy and very wary of strangers, so...”

“Mimi. Whirlwind, then spin around and around and say hello!”

Sssriririk!

“Oh, shit.”

And Mimi busts out a new move right here.

Jin Wikyung, who had been half out of his mind at the sight, muttered in a dazed voice,

“It seems you have nothing to worry about, Family Head.”

An earthquake struck Tang Sadok’s eyes.

Tang Sadok asked Jin Wikyung to stay behind for a private conversation, while Cheongpung and I left the room first.

No—one more person had just been added.

“Young Hero Jin, could you spare this old man a moment?”

“Me?”

The Divine Physician nodded with a gentle smile.

“There is something I must ask of you before you leave.”
```
