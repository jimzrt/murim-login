<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0444.txt",
      "sha256": "d7b192e9502089242dd335f8344fbcbd116a178f9d166b892814cff421c291c4",
      "bytes": 13301
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0514e8df6913d8a9f2e78141e67259d35129f4b7fba0555e8c0e5f310cb21d2a",
      "bytes": 2816
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "ed267e9f08911a4134560c8d536cf6dc13e40a9b32cf5a64a94091cf14adcb2b",
      "bytes": 145169
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "b7796f4cb599af8adf9fefa984b0bd670aaeec6de215f7497b284ff63f5334b4",
      "bytes": 944
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "61d853e7c6c3600d8662318f63b2e43f97d6aa98a59ddc31e76db2e330c106d3",
      "bytes": 553
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "27d951bf90d925602354f839ef794c7327757db9c659b0fe8fc27b9caba00e80",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "e9e8cab94dd7861d911be86717b2a05649566ecd3246508080414d95b5c1494a",
      "bytes": 1390
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "10073b72405423b420cf6871253b1b8b1f5e2d0e57864d0c55fafa813577dc24",
      "bytes": 1239
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "a68ac35aebf6afeeb1881541dd6e53286d2b161506cc11073d1bcfc95d1fe1ec",
      "bytes": 686
    },
    {
      "path": "characters/Zhuge Gonghu.md",
      "sha256": "fc2c9cdbc09d8fd745b5681e7e4139f14830ce5f4c270bb692725d2d3aaad38f",
      "bytes": 561
    },
    {
      "path": "characters/Zhuge Gyun.md",
      "sha256": "3cb3ed6dd573cdc19120664fa4b419f6e156d268c856dd11d553b4828e1ec22b",
      "bytes": 831
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "eca97865579905204c97adf634e57a933044461fdf323ffc6d0687cfc4a87286",
      "bytes": 139861
    }
  ],
  "estimated_tokens": 11919
}
-->

# Durable State Update — Chapter 444

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 444. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 444. Profile updates may replace only one
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
  "chapter": 444,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 444,
    "continuity_sources": [444],
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
    "Jin Taekyung continues crossing between the modern world and Murim while investigating the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations.",
    "The shared symbols remain the only known common ground between the two worlds, and Taekyung suspects they are connected to black magic.",
    "Taekyung has opened his Middle Dantian and is adapting to the resulting changes in his martial ability.",
    "Mungyeong remains with Taekyung's group while concealing his former Divine Physician and Slaughter Saint identity from most companions.",
    "The Skeleton King's undead identity remains concealed from the public, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "Taekyung's group has reached Hubei after ten days of sailing with Mu Song's Water Dragon Stronghold fleet.",
    "The Yangtze River Channel League's nearby Hubei strongholds have not contacted Mu Song despite knowing of his arrival.",
    "Jin Wikyung has political ties with Yi Hongcheon, the newly appointed Hubei Provincial Administration Commissioner, and used them to resolve the harbor incident.",
    "Zhuge Clan martial artists have appeared at the Hubei harbor."
  ],
  "continuity_sources": [
    443,
    442
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations, and are they truly connected to black magic?",
    "Why does Mungyeong continue accompanying Taekyung's group despite being unable to explain the impulse?",
    "What confidential matter is Jin Wikyung withholding?",
    "What are the terms of the Peace Guild–Wizard Guild agreement, and what evidence is contained in Lee Jungryong's holographic recorder?",
    "Why have the Yangtze River Channel League's Hubei strongholds gone silent, and what does the Zhuge Clan want at the harbor?"
  ],
  "safe_through": 443,
  "temporary_decisions": [
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor.",
    "Render 최 팀장님 as “Team Leader Choi,” 진태경 씨 as “Mr. Jin Taekyung,” and 막내야 as “my youngest.”",
    "Keep Peace Guild, guild house, Inventory, Magic Johnson, established martial-arts terminology, black magic, poison human, World Hunter Association, and Wizard Guild unchanged.",
    "Render 당양채, 홍호채, 동정채 as “Dangyang Stronghold,” “Honghu Stronghold,” and “Donghu Stronghold,” and 홍천 as “Hongcheon.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 제갈균    | **Zhuge Gyun**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 십왕     | **Ten Kings**       |
| 열화문    | **Fire Gate Clan**               |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 제갈세가   | **Zhuge Clan**                   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 큰형     | **eldest brother**                           |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 본가      | **our family / this family**                                    |
| 대사      | **Master** for a senior Buddhist monk                           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 제갈공후 | **Zhuge Gonghu** | Former Murim Alliance Chief Strategist and deceased member of the Ten Kings. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 신기묘룡 | **Divine Marvel Dragon** | Epithet of the Zhuge Clan's Lesser Family Head. |
| 기관진식 | **mechanisms and formations** | Fifth preliminary assessment category. |
| 제갈무후 | **Zhuge Wuhou** | Honorific title for Zhuge Liang in the Three Visits allusion. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 내당 | **Inner Hall** | The Tang Clan's inner hall area. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 달마대사 | **Bodhidharma** | Famous Shaolin figure cited alongside Lü Dongbin and Jang Samfeng. |

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
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 443
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 443
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 443
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 443
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is a legendary wandering martial master and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, and casually threatening or violent when dissatisfied. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 443
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Taekyung's eldest brother and future Family Head; Taekyung trusts him as a martial-arts mentor and family protector. Member and acting leader of the Jin Family of Taiyuan. Commands Wipeng and the family's forces. Has worked with Jeok Cheongang, who trained Taekyung under Wikyung's arrangement. Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 443
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

### Zhuge Gonghu.md

# Zhuge Gonghu (제갈공후)

- **Safe through:** Chapter 308
- **Aliases:** None
- **Role:** Former Chief Strategist of the Murim Alliance; a Supreme Peak martial artist known for immortal arts and outstanding formation techniques, one of the Ten Kings and a member of the Three Saints; deceased for more than ten years
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Former Murim Alliance Chief Strategist and member of the Three Saints and Ten Kings.

### Zhuge Gyun.md

# Zhuge Gyun (제갈균)

- **Safe through:** Chapter 252
- **Aliases:** Divine Marvel Dragon
- **Role:** Scholar-styled Zhuge Clan martial artist and finalist in the Star-Array Grand Banquet; expressed considerable regret after losing the fifth preliminary assessment on mechanisms and formations, uses a folding-fan technique in the main event, and was completely outclassed and defeated by the disguised Cheongpung, the Invincible Divine Sword.
- **Personality:** Analytical, pedantic, and unusually preoccupied with theoretical correctness.
- **Voice:** Polished, formal, and interrogative, treating insults as subjects for precise analysis.
- **Relationships:** Rival finalist alongside Baek Woo and Gung Gibang; exchanges restrained arguments with Taekyung.

## Korean source

```text
＃444화



제갈세가(諸葛世家).

현대의 무협 소설에서 꼭 한 번은 등장하는 네임드 가문이다.

제갈 성을 쓰는 등장인물 중에 똑똑하지 않은 놈이 없고, 눈에 띄게 강한 놈도 없다.

명색이 무림 세가면서도 무공은 부전공 느낌이라고 해야 하나?

그도 그럴 만한 게, 제갈세가의 진정한 힘은 몸이 아니라 머리에서 나온다.

폭넓은 학문과 지략, 기관진식에 능통한 지자(智者)들의 가문.

그렇다 보니 세인들로부터는 신기제갈(神機諸葛)이라 불리며 무림에서 머리 쓰는 죄다 도맡아 하는 포지션이다.

읽고 있는 소설에 등장하는 무림맹 군사의 이름이 제갈로 시작하지 않으면 찝찝함마저 느껴질 정도다.

그렇게 줄곧 머릿속에 박혀 있던 제갈세가의 이미지 때문일지도 모르겠다. 이쪽을 향해 거침없이 걸음을 옮기는 무인들의 모습에 낯선 기분을 느낀 것은.

하지만 꼭 낯선 감정만이 있는 것은 아니었다.

처처처척!

철탑처럼 양옆으로 도열하는 제갈세가의 무인들. 그리고 그 사이를 천천히 가로지르는 한 사람.

눈이 부실 만큼 흰 백의(白衣)를 걸친 호리호리한 청년이 입을 열었다.

“어젯밤 천문(天文)이 유난히도 밝더니, 귀한 객들이 오실 조짐이었군요. 소인은 제갈세가의 소가주…….”

나는 반가움에 손을 번쩍 치켜들며 외쳤다.

“갈균아!”

“갈균아……가 아니라 제갈균이라 합니다.”

순간 무거운 침묵이 흘렀다.

아직 내가 누구인지 모르는 제갈세가의 무인들은 웬 미친놈인가, 하는 눈빛이었고 적천강은 약간의 의문을 담아 나를 바라보았다.

“아는 놈이냐?”

“네. 지난번 성라대연 때 만났어요. 근데 제갈세가의 소가주라는 건 처음 알았네.”

“너 같은 놈한테 친구도 있어?”

“친구 아닌데요. 저는 그냥 세 얼간이라고 부르는데…….”

“커, 커흠! 커흐흠!”

성라대연에서 만난 세 얼간이 중 하나, 신기묘룡(神奇妙龍) 제갈균이 황급히 헛기침을 내뱉으며 내 말을 잘랐다.

그리고 뭐라 할 새도 없이 적천강을 향해 인사를 건넸다.

“무림 초출 제갈균이 노 선배님을 뵙습니다.”

제갈균을 위아래로 훑어본 적천강이 한마디를 툭 던졌다.

“공후와는 무슨 관계냐?”

“예?”

“파선지왕(芭扇知王) 제갈공후 말이다. 정마대전 당시 무림맹 총군사였던 놈.”

파선지왕 제갈공후라는 별호와 이름은 나도 들어 봤다.

정마대전 당시 무림맹의 머리 역할을 하며 암담했던 전황을 뒤집은 일등 공신.

다른 초절정 고수들과 함께 십왕(十王)으로 칭송받는 것은 그러한 이유도 있었다.

‘그런데 그런 양반을 놈이라고 부르네.’

나야 이런 모습을 하도 보다 보니 적응이 됐지만, 다른 사람들 입장에서는 신세계다.

진위경은 침을 꿀꺽 삼켰고 제갈세가의 무인들은 입을 딱 벌린 채 자신들의 귀를 의심하는 중이었다.

물론 우리의 화왕 적천강은 그딴 거 신경 안 쓴다. 롸끈하게 들이받아 버리는 게 열화문 종특이다.

“아, 왜 말이 없어?”

가뜩이나 인상이 나쁜데 얼굴까지 찌푸리니 흉신 악살이 따로 없었다. 나름 한가락 하는 미친놈인 재갈균도 당황해서 말을 더듬거릴 정도였다.

“즈, 증조부님 되십니다.”

“그래? 어쩐지, 좀 닮은 것도 같더라니. 머리는 잘 굴리게 생겼군. 싸가지도 없어 보이고.”

“……!”

적천강 위엄 보소.

일백 살을 훌쩍 넘긴 전전대의 인물이다 보니 어지간한 명문 대파의 존장들도 야, 너, 놈이라고 불러도 감히 뭐라 말도 못 한다.

무공으로 씹어먹고 항렬로 소화시켜 버리는, 무림의 달마대사 해골물인 것이다.

어쩔 줄 몰라 하는 분위기에 내가 슬쩍 적천강의 옆구리를 찔렀다.

“거 참. 그만하세요.”

“아, 뭘? 노부가 이 정도도 말 못 하느냐?”

“아무리 그래도 이미 십 년 전에 작고한 고인이신데…….”

“이 새파란 것들이 뭘 안다고. 노부가 죽었다면 제갈공후 역시 똑같이 했을 거다. 그놈이랑 나는 오래전부터 호놈호놈 하던 사이야.”

“…….”

“…….”

호형호제도 아니고 호놈호놈은 뭐야.

신박한 단어 선택에 사람들이 다시 한번 움찔거리는 틈을 타, 가장 먼저 정신을 수습한 진위경이 제갈균을 향해 입을 열었다.

“제갈세가의 환대에 감사하오.”

확실히 프로는 프로다. 성라대연에서는 나사 하나 빠진 놈 같았던 제갈균도 일가의 소가주답게 응대했다.

“별말씀을. 오시는 길이 불편하지는 않으셨는지는 모르겠군요.”

“몸과 마음이 편하다면 어찌 무림인이라 할 수 있겠…….”

“더럽게 불편했다. 감히 노부를 여기까지 오게 만들다니. 무슨 연유인지 들어 보고 별것 아닌 일이라면 아주 화염신장으로.”

“아, 진짜! 제발 좀 그만하시라니까.”

“이놈이 감히 노부의 옷소매를! 놔라! 이 힘만 무식하게 센 놈아!”

급발진한 적천강을 내가 만류하는 사이, 진위경이 황급히 말을 이었다.

“실례인 건 알지만, 괜한 이야기는 접어 두고 한시라도 빨리, 빨리 가십시다.”

“현명하신 판단입니다. 본가의 초석을 쌓으신 제갈무후(諸葛武侯)께서도 학우선을 탁! 치며 동의하셨을 겁니다.”

두 소가주의 극적인 단합에 관군을 비롯한 제갈세가의 무인들이 가장 먼저 길을 텄고, 그 뒤를 우리 일행에 포함된 수룡채의 수적들이 뒤따랐다.

그리고 나는 그런 우리의 모습을 쫓는 수많은 경계 어린 시선과 수군거림을 느꼈다.

‘도대체, 뭐 때문에 이러는 거지?’

진위경이 호북을 거쳐야 한다고 했던 이유가 이것 때문인가?

의문은 그리 오래 이어지지 못했다. 준비되어 있던 마차에 오르자마자 문경이 조용히 입을 열었기 때문이었다.

“자리가 비는 것 같습니다만.”

뭐?

주위를 둘러본 나는 그제야 한 사람의 부재를 깨달을 수 있었다.

“잠깐. 얘 어디 갔어?”

“여기요, 은인!”

“……?”

아니, 저 자식은 도대체 언제 저기로 간 거야.

아직 접지 않은 좌판 앞에서 즉석 요리된 생선찜을 처먹고 있던 청풍이 손을 번쩍 쳐들며 외쳤다.

“금방 먹고 갈게요!”

“개소리하지 말고 당장 튀어와!”

제발 부탁이다.

단 하루만이라도 사람답게 살자. 사람답게.

만신창이가 된 내 마음과 함께, 마차가 나아가기 시작했다.

그리고 잘 정돈된 가도를 달려 사라질 때까지도 사람들의 눈빛은 그림자처럼 따라붙었다.



* * *



사천성의 명문대파인 아미와 청성, 당문이 산 혹은 외진 곳에 근거지를 마련한 것과 달리, 제갈세가는 커다란 대로변의 중심을 차지하고 있었다.

당장 마차 창문 밖으로 스쳐 지나가는 사람들만 수백이 훌쩍 넘는 인구 밀집도.

얼굴이 새카맣게 그을린 그들은 제갈세가의 문양이 새겨진 마차를 발견하고 꾸벅 고개를 숙여 보였다.

“여긴 사람들이 왜 이렇게 많아?”

내 중얼거림에 맞은 편에 앉아 있던 제갈균이 대답했다.

“장강(長江)은 호북의 젖줄과도 같습니다. 드넓은 토지를 기름지게 만드니 사람들이 모여들고, 매년 풍작이 이어지니 얼굴에 웃음이 떠나지를 않지요.”

“그래? 한 시진 전쯤에 나루터에서 본 사람들은 얼굴에 웃음이 영영 떠난 것 같던데.”

“그건…….”

어울리지 않는 심각한 표정으로 입을 다문 제갈균이 시선을 피했다.

“본가에 도착한 후에 말씀드리겠습니다.”

뭔가 일이 생기긴 한 모양이다. 성라대연 때만 해도 아무 말 대잔치를 벌이던 녀석이 이런 모습을 보일 정도니까.

분위기가 이러니 나도 더는 묻지 않고 창밖으로 고개를 돌렸다.

‘확실히 이상하단 말이지.’

그리고 시간이 흐를수록 의문은 더욱 짙어졌다.

언제나 설렁설렁하던 관군들이 눈을 부릅뜬 채 곳곳에서 호패(戶牌)를 검사하고 있었고, 평상복으로 정체를 숨긴 무인들이 양민들 사이에 숨어 있었다.

언뜻 스치듯이 느껴진 그들의 무위가 결코 낮지 않았던 탓에, 순간 암천이 떠올랐지만 다음 순간 들려온 적천강의 전음으로 깨끗이 해결되었다.

- 제갈세가 놈들이다. 무슨 연유에선지 정체를 숨기고 잠행까지 하는군.

가문의 앞마당이나 다름없는 곳에서 이렇게까지 한다고?

나는 문득 며칠 전의 일을 떠올리며 물었다.

- 그런데 노야, 뭐 들으신 거 없어요?

- 뭘 말이냐?

- 아니 왜, 지난번에 제 큰형이랑 자리를 비우신 적이 있었잖아요.

- 그랬었지.

- 그때 호북성에 가야 하는 이유를 들으신 거 아니었습니까? 무당이나 제갈세가에 관해서요.

나를 바라보는 적천강의 미간이 살짝 찡그려졌다.

- 그걸 노부가 들어서 뭐 하게?

- 예?

- 가면 가는 거지. 뭘 꼬치꼬치 캐묻느냔 말이다. 그냥 최대한 빨리 가라고 닦달한 거였다. 안 그러면 쾌조선을 죄다 침몰시켜 버리겠다고.

- ……아, 예.

이걸 쿨하다고 해야 할지, 불같다고 해야 할지 모르겠다.

고개를 절레절레 내저은 나는 힐끗 문경을 바라봤다.

귀찮은 내색 없이 밝게 웃으며 혁무진과 대화를 나누고 있던 소년의 눈썹이 슬쩍 치켜 올라간다.

귓가에 전해지는 은밀한 전음까지.

- 뭐.

- ……아직 아무 말도 안 했는데요.

- 쓸데없이 쳐다보지 마라. 내일 아침에 뜨는 해를 보고 싶다면.

이거 무서워서 숨이라도 제대로 쉬겠나.

나는 내심 한숨을 내쉬며 마차의 격자 창문 밖으로 시선을 돌렸다.

한 시대의 역사를 쓴 천하제일의 모사가 은거했던 탓에 복룡산(伏龍山)이라고도 불리는 융중산(隆中山).

그리고 드넓은 면적의 대지 위에 세워진 제갈세가가 모습을 드러내고 있었다.

‘호북성 제일의 거부라더니.’

가문의 선조인 제갈공명은 검소하기로 이름 높았지만, 그의 후손들은 타고난 좋은 머리를 학문과 기관진식에만 쏟지 않았다.

매년 풍작을 기록하는 비옥한 토지와 호북성 전역을 가로지르는 장강의 물길을 십분 이용하여 막대한 부를 쌓아 올린 것이다.

나는 제갈세가의 대문을 통과하기도 전에 그들이 가진 부가 어느 정도 실감이 나기 시작했다.

“왜 안 내려? 다 도착한 거 아냐?”

제갈균이 무슨 말이냐는 듯한 표정으로 대꾸했다.

“네? 여기서 내당까지 걸어서 가려면 한참 걸리는데요? 앞으로 일곱 개의 문을 더 통과해야 하니까 그냥 앉아 계시면 됩니다.”

“……그 정도야?”

“그나마 이것도 줄인 겁니다. 본가도 정마대전을 겪으면서 피해가 상당했거든요.”

“미쳤네. 금은보화를 아주 갈퀴로 쓸어 담는구나. 검소하게 살라는 선조님의 유훈, 뭐 그런 거 없었냐? 청렴한 선비 같은 거 아니었어?”

제갈균이 표정 하나 바꾸지 않고 근엄한 목소리로 대답했다.

“학문 공부하는 것도 한두 푼 드는 게 아닙니다. 서책 값이 얼마나 비싼데요. 게다가 저희 가문은 따로 서생들도 후원하고 있다고요.”

“…….”

“여유로운 환경에서 공부해야 과거도 급제하고, 무공에 진전도 있는 겁니다. 배고프면 아무 생각도 안 나고 마음만 조급해져요.”

“어, 으응.”

생각했던 것과는 다르긴 한데, 따져보면 하나하나가 맞는 말이다.

자본의 중요성에 대해 조곤조곤 설명한 제갈균은 자신의 선조인 제갈공명 역시 금수저였다는 말로 일장연설을 끝냈다.

그때쯤에는 총 여덟 개의 문을 통과한 마차가 내당으로 접어들고 있었다.

“이제 내리셔서 절 따라오십시오. 본가의 가주께서 기다리고 계십니다.”

“가주님이라면…….”

“제 아버님이십니다.”

적천강에게 들은 적이 있다.

정마대전 도중 하나뿐인 아들을 잃은 제갈공후가, 장자 계승의 원칙에 따라 자신의 어린 손자에게 소가주의 지위를 내려 주었다는 이야기를.

그 어린 손자가 바로 제갈세가의 현 가주이자 제갈균의 아버지인 와룡객(臥龍客) 제갈풍이다.

“가주님. 귀빈들을 모셔왔습니다.”

웃음기를 쏙 뺀 진지한 목소리와 함께, 굳게 닫혀 있던 문이 스르륵 열렸다.
```

## Final English reading copy

```markdown
# Chapter 444

The Zhuge Clan.

It was a famous family that appeared at least once in every modern wuxia novel.

Not a single character with the surname Zhuge was ever stupid, and none of them were conspicuously strong, either.

They were supposedly one of Murim’s great families, yet martial arts seemed more like their minor than their major.

That made sense. The Zhuge Clan’s true strength came not from their bodies, but from their minds.

They were a family of wise men skilled in broad scholarship, strategy, and mechanisms and formations.

As a result, the world called them the Divine Mechanism Zhuge, and in Murim, they handled practically every role that required brains.

If the name of the Murim Alliance’s strategist in a novel you were reading didn’t begin with Zhuge, it could even feel unsettling.

Perhaps it was because that image of the Zhuge Clan had been so firmly lodged in my mind that I felt strange seeing these martial artists stride toward us without hesitation.

But unfamiliarity wasn’t the only emotion I felt.

Clack-clack-clack-clack!

The Zhuge Clan’s martial artists lined up on either side of the road like iron towers. A single person slowly walked between them.

The slender young man wearing robes so white they were almost blinding opened his mouth.

“Last night, the stars were unusually bright. It seems they were heralding the arrival of honored guests. I am the Zhuge Clan’s Lesser Family Head…”

I raised my hand high and shouted in delight.

“Galgyun!”

“Not ‘Galgyun’… I’m Zhuge Gyun.”

A heavy silence fell.

The Zhuge Clan’s martial artists, who still had no idea who I was, looked at me as if I were some kind of madman. Jeok Cheongang looked at me with a hint of confusion.

“You know this fellow?”

“Yes. I met him at the Star-Array Grand Banquet last time. But this is the first I’ve heard that he’s the Zhuge Clan’s Lesser Family Head.”

“Even someone like you has friends?”

“He’s not my friend. I just call them the Three Idiots…”

“Ahem! Ahem-ahem!”

One of the Three Idiots I had met at the Star-Array Grand Banquet—the Divine Marvel Dragon Zhuge Gyun—hurriedly cleared his throat and cut me off.

Before I could say anything, he turned toward Jeok Cheongang and offered his greetings.

“Zhuge Gyun, a newcomer to Murim, pays his respects to Senior.”

Jeok Cheongang looked Zhuge Gyun up and down before tossing out a question.

“What relation are you to Gonghu?”

“Pardon?”

“I mean the Fan-Wisdom King, Zhuge Gonghu. That bastard was the Murim Alliance’s chief strategist during the Great Faction War.”

I had heard both the title and name of the Fan-Wisdom King Zhuge Gonghu.

He had served as the mind of the Murim Alliance during the Great Faction War and was the foremost contributor to turning the grim tide of the war.

That was one reason he had been praised as one of the Ten Kings alongside the other Supreme Peak masters.

*What a way to refer to someone like that.*

I had gotten used to seeing Jeok Cheongang act this way, but to everyone else, it must have been a whole new world.

Jin Wikyung swallowed hard, while the Zhuge Clan’s martial artists stood there with their mouths hanging open, doubting their own ears.

Of course, our Fire King Jeok Cheongang didn’t care about any of that. Ramming straight into things with blazing force was practically the Fire Gate Clan’s trademark.

“Why aren’t you answering?”

His expression was unpleasant enough already, but when he actually frowned, he looked like a murderous demon.

Even Zhuge Gyun—a lunatic who was no slouch himself—was so flustered that he stammered.

“M-my great-grandfather.”

“Is that so? I thought you looked a little like him. You look like you’d have a good head on your shoulders. You also look like you have no manners.”

“…”

Now that was imposing.

Since Jeok Cheongang was a man from two generations ago who had lived well past a hundred, even the elders of most prestigious clans and sects couldn’t dare object when he called them, “Hey,” “you,” or “bastard.”

He could chew people up with martial arts and digest them with seniority—the Bodhidharma’s-skull-water story of Murim.[^1]

With the atmosphere growing increasingly awkward, I gave Jeok Cheongang a light poke in the side.

“Come on. That’s enough.”

“What? Can’t this old man say even that much?”

“Even so, he’s been dead for ten years…”

“What do these greenhorns know? If this old man had died, Zhuge Gonghu would have done the same. He and I have been calling each other bastard for years.”

“…”

“…”

Not brotherly terms. Bastardly terms.

While everyone flinched once again at his innovative choice of words, Jin Wikyung was the first to recover and address Zhuge Gyun.

“Thank you for the Zhuge Clan’s hospitality.”

A true professional was a true professional. At the Star-Array Grand Banquet, Zhuge Gyun had seemed like a man with a screw loose, but as the Lesser Family Head of his clan, he responded appropriately.

“Think nothing of it. I hope your journey here was not too uncomfortable.”

“If a person is comfortable in both body and mind, how can he call himself a martial artist—”

“It was damn uncomfortable. How dare you make this old man come all the way here? I’ll hear the reason, and if it’s nothing important, then a Flame Divine Palm will…”

“Oh, seriously! I said that’s enough!”

“You dare grab this old man’s sleeve! Let go, you all-brawn bastard!”

While I tried to restrain Jeok Cheongang, who had flown off the handle, Jin Wikyung hurriedly continued.

“I know this is rude, but let’s put the pointless conversation aside and hurry. Please, let’s hurry.”

“A wise decision. Zhuge Wuhou, who laid the foundations of our family, would have smacked his feather fan and agreed.”

The government troops and Zhuge Clan martial artists were the first to clear a path at the dramatic show of unity between the two Lesser Family Heads. The river bandits from the Water Dragon Stronghold who had joined our party followed behind them.

As we moved, I felt countless wary gazes and heard people whispering as they watched us.

*What the hell is going on?*

Was this why Jin Wikyung had said we needed to pass through Hubei?

My question didn’t last long. The moment we climbed into the carriage, Mungyeong quietly opened his mouth.

“It seems we are one person short.”

“What?”

I looked around and only then noticed that someone was missing.

“Wait. Where did he go?”

“Here, Benefactor!”

“…”

When the hell had that bastard gotten over there?

Cheongpung was standing in front of a street stall that had not yet been folded, stuffing himself with freshly steamed fish. He raised one hand high and shouted.

“I’ll finish eating and come!”

“Stop talking bullshit and get your ass over here!”

Please.

Just for one day, let’s live like human beings. Like human beings.

With my heart in tatters, the carriage began to move.

Even after it raced down the well-kept road and disappeared from sight, people’s eyes continued to follow us like shadows.

* * *

Unlike Emei, Qingcheng, and the Tang Clan—the prestigious great powers of Sichuan Province—which had established their bases on mountains or in remote areas, the Zhuge Clan occupied the center of a major thoroughfare.

Just the people passing outside the carriage window numbered well over several hundred.

Their faces were darkened by the sun, and whenever they spotted the carriage bearing the Zhuge Clan’s emblem, they bowed their heads.

“Why are there so many people here?”

Zhuge Gyun, sitting across from me, answered my mutter.

“The Yangtze is practically Hubei’s lifeline. It makes the vast surrounding lands fertile, so people gather here. And because the harvest is plentiful every year, smiles never leave their faces.”

“Really? The people I saw at the ferry about one shichen ago looked like their smiles had left forever.”

“That…”

Zhuge Gyun closed his mouth, his expression suddenly serious in a way that didn’t suit him, and looked away.

“I’ll tell you after we reach the family compound.”

Something must have happened. At the Star-Array Grand Banquet, he had been an endless fountain of nonsense, so it was telling that he looked like this now.

Given the mood, I didn’t ask any further questions and turned my head toward the window.

*Something definitely feels wrong.*

And the more time passed, the stronger that feeling became.

The government troops, who were usually so lax, had their eyes wide open as they checked people’s hopae at various points, while martial artists in ordinary clothes hid among the commoners.[^2]

Their martial prowess, which I sensed only briefly as we passed, was far from low. Dark Heaven immediately came to mind, but Jeok Cheongang’s Sound Transmission a moment later cleared that up.

*—They’re Zhuge Clan people. For some reason, they’re hiding their identities and even moving covertly.*

*They’re doing this practically in their own front yard?*

I suddenly remembered what had happened a few days earlier and asked,

*—Old Master, did you hear anything?*

*—About what?*

*—You know. Last time, you left with my eldest brother for a while.*

*—I did.*

*—Didn’t you hear why we had to come to Hubei then? Something about Wudang or the Zhuge Clan?*

Jeok Cheongang’s brow furrowed slightly as he looked at me.

*—What good would it do this old man to hear that?*

*—Pardon?*

*—If we’re going, we’re going. Why are you prying into every little thing? I was merely badgering him to get here as quickly as possible. I told him I’d sink every fast ship if he didn’t.*

*—…Ah. Right.*

I wasn’t sure whether to call that cool or fiery.

I shook my head and glanced at Mungyeong.

The boy had been chatting with Hyuk Mujin with a bright smile, showing no sign of irritation. But then one of his eyebrows lifted slightly.

A private Sound Transmission reached my ears.

*—What.*

*—…I haven’t even said anything yet.*

*—Don’t stare at me for no reason. If you want to see tomorrow morning’s sun.*

This was terrifying. Was I even supposed to breathe properly?

I sighed inwardly and turned my gaze toward the view beyond the carriage’s latticed window.

Mount Longzhong, also called Mount Fulong because the greatest strategist under heaven—a man who had shaped the history of an era—once lived there in seclusion.

And spread across a vast stretch of land, the Zhuge Clan finally came into view.

*They said this was Hubei Province’s wealthiest family.*

Their ancestor, Zhuge Kongming, had been famous for his frugality. But his descendants had not devoted their naturally sharp minds solely to scholarship and mechanisms and formations.

They had made full use of fertile land that produced plentiful harvests every year and the Yangtze’s waterways, which crossed the entirety of Hubei Province, to amass enormous wealth.

I began to grasp the extent of that wealth before we even passed through the Zhuge Clan’s main gate.

“Why aren’t we getting out? Haven’t we arrived?”

Zhuge Gyun answered with an expression that seemed to say he had no idea what I was talking about.

“Pardon? It would take a long time to walk from here to the Inner Hall. We still have seven more gates to pass through, so just sit back.”

“…Is it really that big?”

“This is the reduced version. Our family suffered considerable damage during the Great Faction War.”

“This is insane. You’re sweeping up gold and silver with a rake. Didn’t your ancestor leave some instruction to live frugally? Wasn’t he an incorruptible scholar or something?”

Zhuge Gyun answered in a solemn voice without changing his expression.

“Studying scholarship costs more than a few coins. Do you know how expensive books are? Besides, our family separately supports scholars as well.”

“…”

“You need a comfortable environment to pass the civil-service examinations and advance in martial arts. When you’re hungry, you can’t think about anything. You only become anxious.”

“Uh… right.”

It wasn’t what I had expected, but if I thought about it carefully, every one of his points made sense.

After patiently explaining the importance of capital, Zhuge Gyun concluded his speech by saying that even his ancestor, Zhuge Wuhou, had been born with a silver spoon in his mouth.

By then, the carriage had passed through a total of eight gates and was entering the Inner Hall.

“Now, please get down and follow me. The Family Head is waiting.”

“The Family Head would be…”

“My father.”

I had heard about him from Jeok Cheongang.

During the Great Faction War, Zhuge Gonghu had lost his only son. In accordance with the principle of eldest-son succession, he had given his young grandson the position of Lesser Family Head.

That young grandson was Zhuge Feng, the Crouching Dragon Guest—the current Family Head of the Zhuge Clan and Zhuge Gyun’s father.

“Family Head, I’ve brought the honored guests.”

At Zhuge Gyun’s serious voice, now completely devoid of humor, the firmly closed doors slowly opened.

[^1]: This refers to a Korean Buddhist anecdote in which a monk drinks water from a skull in the dark and finds it sweet, only to recoil after seeing the skull in daylight. The phrase is used for the way perception changes once one understands the truth.

[^2]: A *hopae* was a personal identification tablet used in premodern Korea and China.
```
