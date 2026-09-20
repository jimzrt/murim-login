<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0546.txt",
      "sha256": "517bb1c7fd0a35fc58ad85c8b91b2a4b6e2de5975b123881379836901553908e",
      "bytes": 14450
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1027cec02ca9f7be61c8901a9ecdec166ba9fd9eea8e85ea8d311a1565c593ac",
      "bytes": 4354
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "8c31e77a40c77883ace0894f1106a38a2a1e12a09d731ff26a0f53e58dcb7020",
      "bytes": 172492
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "5aad1307f9b509331bf07c1b2c57f2565bee19bb089f2dd63e1a44a6222c4fe0",
      "bytes": 1370
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8da58e4ff4117ceeb775ed9e1efeb95cca4609e7fb964784df4a36fdae704d83",
      "bytes": 553
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "2234d4a8c4d826445b3566a40c36b96922c3060d015ba8926d0fb7367dd986d0",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "c345d3bce2a0d71d449737e3d250c0a8420a0a62a6bd112ee88b5e6bcf40e6e1",
      "bytes": 1210
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "6979523653caf8264b17781619e97f077f491fb9d473af9d623e0b97c66ae6c0",
      "bytes": 985
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "cc9810a17a1f4df7d0e47f59f89afc318e4433b97b4035bef4ae7cd8af250dc8",
      "bytes": 1233
    },
    {
      "path": "characters/Murong Yeonghwi.md",
      "sha256": "3ea030e6fe5fad71ff36fa51de2e70f2788e32283f3e8986fce1cedb44cd3fb3",
      "bytes": 420
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e190d1f4dfdecc6495d6974499268ad909f972ce7efdd79c30e42b78daed2e44",
      "bytes": 164631
    }
  ],
  "estimated_tokens": 13185
}
-->

# Durable State Update — Chapter 546

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 546. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 546. Profile updates may replace only one
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
  "chapter": 546,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 546,
    "continuity_sources": [546],
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
    "The Mount Song Resolution formally restored the Murim Alliance; Mae Jonghak is its Alliance Leader, and Song Ho commands the Hidden Shadow Pavilion under his authority.",
    "The Fire Dragon Pavilion is formally established under the Alliance Leader, with Jin Taekyung and Cheongpung as its two pavilion masters and Ju Hwaran, Song Ilseom, Sama Pyo, Taishan, and Hyuk Mujin as members.",
    "Jin Taekyung holds the unique Title Fire Dragon Pavilion Master; his total Fame has surpassed 10,000, some Title effects have strengthened, Charm and Intimidation have greatly increased, and he has leveled up.",
    "The Five Kings Hall contains five of the Ten Kings, with Jeok Cheongang occupying its chief seat despite resenting the appointment.",
    "Tang Sadok and the Sichuan Tang Clan publicly support Jin Taekyung and Cheongpung, while Taekyung expects the resentful Zhongnan Sect to obstruct them.",
    "Cheongpung created Mimi Step, is recognized by Mungyeong as having Grandmaster potential, and cares for Mimi, the large horned snake entrusted to him by Tang Sadok.",
    "Mungyeong ended Taekyung's direct training, assigned him a final task of incorporating martial principles into his learned martial arts, and accepted Cheongpung's offer to accompany him.",
    "Zhuge Feng's Demon-Sealing Formation still blocks all mana from the exposed Gate, while Jang Taebo is summoning artisans to process the Water God Dragon's remains.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "The Black Dragon Demon Gate remains a major unorthodox power; Sama Pyo is its Young Sect Leader and Black Dragon Saber, and Taishan is his giant subordinate.",
    "Jin Taekyung remains a Supreme Peak master with Three Flowers Gather at the Crown, advanced qi perception, exceptional resistance to monster Fear, and public S-rank-level recognition despite retaining an A-rank license.",
    "Jin intends to advance toward the coming war while protecting his family, companions, subordinates, and Master; Jeok Cheongang has reminded him that others want to protect him."
  ],
  "continuity_sources": [
    545,
    544
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Why did Ju Hwaran and Sama Pyo's political engagement end?",
    "Whether additional companions will join the Fire Dragon Pavilion."
  ],
  "safe_through": 545,
  "temporary_decisions": [
    "Render 고월루 as Gowolru, 곤륜운룡 as Kunlun Cloud Dragon, 학우 as Hak Woo, 이룡각 as Two Dragons Pavilion before its renaming, 화룡각 as Fire Dragon Pavilion, 협 as chivalry, 인의 as humanity, 협객 as knight-errant, 홍학루 as Honghakru, 홍매 as Hongmae, and 호거아 as Tiger Giant Child; render 전 정혼자 contextually as former fiancé or former fiancée.",
    "Render 탈진 as the capitalized System status Exhaustion; retain Ten Dragons and Phoenixes, Blazing Flame Divine Dragon, Dark Heaven, Murim Alliance, and Old Master.",
    "Render 황보세가 as Hwangbo Family, 소가주 as Lesser Family Head, 은비화 as Dagger Hidden Flower, and 전음 as Sound Transmission.",
    "Preserve the chapter's blunt profanity, financial-therapy humor, monster-comparison humor, and Mae Jonghak's carefree 'That can happen' refrain; render 고잉무림호 as Going Murim ship, 대종사 as Grandmaster, 왕희지 as Wang Xizhi, and 영창 피아노 as Young Chang piano.",
    "Render 일기천룡 as One-Ride Heavenly Dragon, 오왕전 as Five Kings Hall, 화룡각주 as Fire Dragon Pavilion Master, 칼밥통 무림맹 공무원 as Murim Alliance Civil Servant with a Sword Rice Bowl, 쟤 모르면 암천 as If You Don't Know Him, You Must Be Dark Heaven, and 위압 as Intimidation; retain Taishan's clipped, childlike, literal speech and the established renderings of Old Man Ilyang, Won Cheol, Black Blood Saber, No Guisan, One Sun, Black Night King, and Green Forest Battle King."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무당파    | **Wudang**                       |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 삼류     | **Third Rate**    |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 낭인     | **wandering martial artist**                     |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장문인    | **Sect Leader**                              |
| 대주     | **Squad Leader** / **Commander**             |
| 은인     | **Benefactor**                               |
| 몬스터     | **monster**           |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 모용영휘 | **Murong Yeonghwi** | A blood relative of the Murong Family regarded as an overwhelmingly powerful young prodigy. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 천룡 | **Heavenly Dragon** | The ideal form Jeok Cheongang wishes Taekyung to become. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 오크 | **Orc** | Monster species. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 외당 | **Outer Hall** | The Tang Clan's outer hall area. |
| 내당 | **Inner Hall** | The Tang Clan's inner hall area. |
| 삼당 | **Three Divisions** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 흡정마공 | **Essence-Siphoning Great Technique** | Source variant for the established essence-siphoning martial art. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |
| 살귀 | **Killing Ghost** | Mungyeong's earlier sobriquet before he became the Slaughter Saint. |
| 무량수불 | **Infinite Life Buddha** | Buddhist invocation used by Taekyung. |
| 이룡 | **Two Dragons** | Collective ranking beneath the Ten Kings in Murim gossip. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 요녕 | **Liaoning** | Northeastern region from which the Murong Family arrives. |
| 맹주부 | **Alliance Leader's Office** | Office directly serving the Alliance Leader. |
| 맹주전 | **Alliance Leader's Hall** | Hall directly associated with the Murim Alliance Leader. |
| 일기천룡 | **One-Ride Heavenly Dragon** | Sama Pyo's title for Murong Yeonghwi. |
| 이룡각 | **Two Dragons Pavilion** | Named pavilion whose masters are identified as Taekyung and Cheongpung at the chapter's close. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 오왕전 | **Five Kings Hall** | Organization containing five of the Ten Kings. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 진위경 | 문경 | Jin Family Lesser Family Head to medical apprentice | you | formal-polite | Asks whether Jin Taekyung will arrive soon. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 진위경 | 청풍 | Jin Family Lesser Family Head to young martial companion | Young Hero Cheongpung | formal-polite | Uses 청 소협 while summoning Cheongpung to the Alliance Leader's Hall. |
| 청풍 | 매종학 | grandson to grandfather | Grandpa | casual-familiar | Repeatedly calls Mae Jonghak 할아버지 while mistaking the Alliance Leader's summons as a family visit. |
| 문경 | 청풍 | martial_master_to_prospective_companion | you | blunt and informal | Mungyeong questions Cheongpung about Mimi Step and why he offered to accompany him. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 545
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and now one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, Mungyeong recently examined her condition, and Mungyeong accepted Cheongpung's offer to accompany him after Cheongpung pledged to learn by observation rather than formal instruction.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 545
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 545
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 535
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung's eldest brother and future Family Head who protects and mentors him, commands Wipeng and the Jin Family's forces, has worked with Jeok Cheongang, and maintains a political connection with Hongcheon, Prince Shangshan's hidden loyal retainer; Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 544
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 544
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; he was the sole survivor of an assassin training cohort that began with three hundred candidates and passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom Mungyeong helped break free of his Heart Demon, Mungyeong was asked to look after and instruct Jin Taekyung and has now ended that direct training after teaching him martial principles and giving him a custom fire-qi pill, Cheongpung has offered him companionship and Mungyeong accepted, and Mu Song plus five Water Dragon Stronghold subordinates know he is an exceptionally powerful master but not that he is the Slaughter Saint.

### Murong Yeonghwi.md

# Murong Yeonghwi (모용영휘)

- **Safe through:** Chapter 533
- **Aliases:** One-Ride Heavenly Dragon
- **Role:** Murong Yeonghwi is a blood relative of the Murong Family and an overwhelmingly powerful young prodigy.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He is a blood relative of the Murong Family.

## Korean source

```text
＃546화



“맹주께서 드십니다.”

묵직한 목소리와 함께 차례대로 열리는 다섯 개의 문. 그리고 저 너머로부터 천천히 가까워지는 한 사람의 신형에, 사람들이 약속이라도 한 듯 동시에 자리에서 일어났다.

“와구, 쩝쩝.”

“…….”

이 새끼 빼고.

‘보면 볼수록 상당히 미친놈일세.’

이런 말을 하는 나도 딱히 예의를 차리는 편은 아니지만, 그래도 최소한의 눈치 정도는 있다. 기어코 남은 음식들을 전부 주둥이에 안전 보관 하는 청풍을 향해 작게 속삭였다.

“도대체 왜 이래. 사회에 불만 있어? 무림맹이 마음에 안 들어?”

입 안에 든 것을 꿀꺽 삼키며 일어난 청풍이 대답했다.

“하지만 음식이 남았는걸요, 은인.”

“아니, 그러면 먹는 걸 중단하면 되잖아.”

“그럼 만두가 식잖아요.”

“…….”

청풍 너란 새끼. 관운장 같은 새끼. 만두 식는 건 알면서 주위 사람들 시선이 차갑게 식는 건 하나도 모르는 새끼…….

‘하긴. 늘 이랬지.’

주위 시선을 신경 쓰면 청풍이 아니다. 작게 한숨을 내쉰 나는 청풍의 옆구리를 쿡 찌르며 중얼거렸다.

“먹을 거 다 먹었으면 집중하자고. 우리 청룡각주(靑龍閣主)님.”

청룡각주. 그 네 음절에 입을 삐쭉 내민 청풍이 고개를 끄덕였다. 이어 잔뜩 심통이 난 목소리가 조그맣게 흘러나왔다.

“네에, 은인.”

이룡각(二龍閣)이라는 명칭은 그대로지만, 세부적으로는 내가 담당하는 화룡각과 청풍의 청룡각으로 나뉘었다. 함께 대회의에 소집되어 오는 길에 만난 청풍과 나눈 대화에 의하면, 그는 다른 이름을 붙이고 싶어 했지만 문경의 맹렬한 반대에 부딪혔다고 했다.



‘그 이름. 마음에 안 들어요.’

‘왜. 난 청룡각도 멋있는 것 같은데. 그래도 조금 너무하긴 하네. 명색이 각주인데 이름 정도는 뜻대로 붙일 수 있는 거 아닌가?’

‘저도 그렇게 생각했는데, 문 할아버지는 싫대요. 그런 이름이라면 차라리 때려치울 거라고 으름장을 놓으셨어요.’

‘그 정도였다고? 처음 생각한 이름은 뭐였는데?’

‘만두각이요.’

‘…….’

‘아니면 당과각.’

‘……어, 그래.’

‘후우. 문 할아버지가 미워요. 청룡각이 뭐예요, 청룡각이.’



지금 생각해도 어이가 없네. 고마워해야지, 미친놈아.

이럴 거면 차라리 김부각으로 하지 그랬냐. 하는 말이 목구멍까지 차올랐지만 꾹 참았다. 이미 지난 일이라서가 아니다. 정파 무림의 최고 존엄께서 마침내 대회의장에 입장하셨기 때문이다.

저벅.

고요한 침묵 사이를 가로지르는 걸음걸이. 마침내 상석(上席)에 다다른 무림 맹주 매종학이 모두를 향해 빙긋 웃어 보였다.

“다들 모이셨구려.”

지난번의 회동과 달리, 이번에는 맹주부 산하 핵심 조직의 수장들까지 함께한 자리다. 이는 무림맹 내부의 조직 개편이 완전히 끝났다는 뜻이기도 했다.

‘이렇게 모이니까 꽤 많네.’

나는 빠르게 주위를 훑었다. 낯선 얼굴도 있고, 익숙한 얼굴들도 있다. 전자의 경우에는 이름과 별호만 들어 본 고수들이지만, 후자의 경우에는 반가운 얼굴들이 제법 있다.

“늦게도 오시는군. 엉덩이에 쥐 날 뻔했소.”

매종학에게 이렇게 말할 수 있는 사람은 천하를 통째로 뒤집어 영혼까지 탈탈 털어도 손에 꼽는다.

그중 대표적인 것이 상석 바로 옆에 자리한 적천강이었다. 짝다리까지 짚은 그의 불퉁한 말투에 맞은편 중간 자리에 있던 진위경이 눈치를 살피며 입을 열었다.

“적 대협.”

“왜.”

“그, 아시지 않습니까.”

“거참. 자네도 감투 쓰더니 이제 맹주 편을 드나?”

순간 멈칫한 진위경이 곤란한 미소를 지었다. 불과 일 년 하고도 수개월. 가주 대행이라는 이름으로 태원진가의 사령탑에 앉아 서서히 몰락해 가던 가문을 무섭게 성장시킨 그는, 어느덧 이들 중 한 사람이 되어 있었다.

“그게 아니라―”

“알았네. 알았다고. 이제는 형과 아우가 쌍으로 난리로군.”

투덜거리는 적천강을 향해, 매종학이 미소를 지어 보였다.

“너무 그러지 마시오, 적 대협. 아니, 이제 오왕전주(五王殿主)라고 불러 드려야 하나?”

“……끄응. 충분히 알아들었으니 그만하시오. 보는 눈도 많은데.”

“이거, 바쁜 사람들을 불러 놓고 흰소리를 했구려.”

매종학만큼 바쁜 사람이 있겠냐 싶지만, 틀린 말은 아니다.

이 자리에 모인 한 사람, 한 사람이 무림맹이라는 거대한 단체를 움직이는 중요한 기관이자 톱니바퀴니까.

‘이전(二殿), 삼당(三堂), 오각(五閣), 오원(五園), 십단(九團).’

무림맹주 매종학이 이끄는 맹주전과 어깨를 나란히 하는 것은 적천강이 수장으로 부임한 오왕전뿐이고, 그 아래에 내당(內堂)에 속한 삼당과 오각이 있으며 오원, 그리고 십단은 오대세가와 구파일방의 인물들이 차지했다.

‘그 외에는 더 많고.’

놀랍게도 이 자리에 모인 이들이 전부가 아니다. 외당(外堂)에 속한 단주며, 대주들까지 더한다면 이 넓은 대회의실로도 자리가 부족해서 연무장을 써야 할 것이다.

이것은 그만큼 무림맹의 규모가 거대하다는 증거였고, 이 자리에 참석하게 된 나와 청풍이 무림맹의 핵심 수뇌부 중 한 사람으로 인정받았다는 뜻이기도 했다.

‘뭐, 그래 봤자 딱히 실권은 없는 명예직이지만.’

직위(職位)와 직급(職級)의 차이라고 해야 할까. 명목상의 직위는 각주지만 사실상의 서열은 이 중에서도 말석에 가깝다. 물론 내 나이 또래에 이 정도 위치에 있는 사람은 아무도 없지만.

‘아, 청풍을 제외하고도 한 명이 더 있긴 했지.’

일기천룡(一騎天龍) 모용영휘. 불과 이 년 전만 하더라도 무림 제일의 후기지수라 불리던 천재. 모용세가의 소가주이자 최근 무림맹의 외당 단주로 임명받은 그는 가주인 아버지를 따라 하남에 오는 대신, 요녕에 남아 가문의 방비를 맡았다고 들었다.

‘이제야 얼굴 한번 보나 싶었는데.’

하긴, 하남에 참석한다고 본진을 비우는 것만큼 멍청한 짓도 없다. 이 자리에 있는 이들 역시 같은 방식으로 방비를 끝마쳤을 터였다.

슥.

그때 천천히 손을 들어 올린 매종학이 입을 열었다.

“자, 다들 편히 앉으시오. 이렇게 예의를 차릴 만큼 시간이 넉넉하지 않으니.”

하지만 사람들은 도로 자리에 앉지 않았다. 아니, 앉을 수 없었다는 표현이 정확했다. 매종학이 손을 들어 올림과 동시에, 아직 열려 있는 문 너머에서 정체를 알 수 없는 무언가가 두둥실 떠올랐기 때문이다.

“허공섭물(虛空攝物)을 어찌 저리 손쉽게…….”

누군가가 중얼거렸다.

천에 덮여 무엇인지 제대로 알아볼 수는 없지만, 척 봐도 커다란 크기에 상당한 무게를 지닌 듯한 물체였다. 그걸 아무렇지 않게 이동시키는 매종학의 공력에 대한 탄성이 묻어났다.

그러나 몇몇 사람의 얼굴은 이미 딱딱하게 굳어 있었다. 물론 내 얼굴 역시 그랬을 것이다.

‘공력이 문제가 아니야. 저건…….’

오감(五感) 중에서도 가장 먼저 반응한 것은 코, 바로 후각이다. 감각이 발달된 무림인조차 곧장 구분할 수 없을 만큼 미세한 냄새였지만, 나는 그 악취를 맡자마자 깨달을 수 있었다.

“은인. 이 냄새는 혹시?”

눈을 동그랗게 뜨며 묻는 청풍을 향해 나는 작게 고개를 끄덕였다.

“맞아. 시취(屍臭)야.”

“……!”

시취는 말 그대로 시체 썩는 냄새를 뜻한다.

현대와 무림, 두 세계를 오가며 수없이 맡아 본 악취였기에 이번만큼은 누구보다 확신할 수 있었다. 동시에 시체의 정체에 대한 어떤 짐작이 뇌리를 스쳤다.

‘만약 내 예상이 옳다면, 저건…….’

그리고 다음 순간, 검붉은 피로 물든 천이 벗겨짐과 동시에 대회의실의 모두는 누가 먼저랄 것도 없이 침음성을 흘렸다.

“흐읍.”

“도, 도대체…….”

“매, 맹주님. 이것의 정체가 무엇입니까?”

경악이 서린 목소리가 곳곳에서 튀어나왔다. 이미 이 사실을 알고 있던 이도, 모르고 있던 이도 지금만큼은 같은 충격을 느낄 수밖에 없었다. 그만큼 천에 가려져 있던 ‘그것’의 모습은 끔찍했다.

‘괴물.’

그렇게밖에 부를 수 없었다. 언뜻 보면 사람의 체형을 하고 있으나 기형적으로 길고 굵어진 뼈마디가 전신 곳곳에 흉측하게 튀어나왔고, 부릅뜬 채 빛을 잃은 눈동자는 어린아이의 주먹만큼이나 컸다.

심지어 괴물의 기괴한 점은 거기에서 끝이 아니었다.

“뿌, 뿔이 있소.”

“그뿐만이 아니오. 팔이…….”

이마 정중앙에 솟은 검은 뿔과 상반신에 튀어나온 네 개의 팔. 싸우는 과정에서 잘려 나갔는지 각각 길이도, 굵기도 달랐으나 그것이 사람의 팔이라는 데에는 그 누구도 이견이 없었다.

“으음.”

“어찌 이런 일이.”

사람들 사이에서 연신 탄식이 흘러나오던 그때, 누군가가 불쑥 입을 열었다.

“무량수불. 믿을 수 없는 일이지요. 빈도도 처음에는 그러했소.”

목소리의 주인은 가슴께까지 내려오는 새하얀 수염과 깊은 눈동자를 지닌 노도사, 바로 무당파 장문인이었다. 순간 그를 향해 집중된 사람들의 시선에 의문이 어렸다.

“처음에는……이라니요?”

“그 말씀은 혹시…….”

무당파 장문인이 고개를 끄덕였다.

“맞소. 이미 몇몇 분은 들어서 알고 계시겠지만, 저자. 아니, 저것은 본래 장삼이라는 이름의 어부였소.”

앞서 은영각(隱映閣)에서 들었던 정보가 노도사의 입술 새로 흘러나왔다. 남들과 다를 것 없던 흔한 이름의 어부가 실종된 지 한 달 만에 호북성을 떠들썩하게 만든 살귀(殺鬼)이자 괴물로 나타났다는 이야기였다.

“처음 발견했을 당시의 무공은 삼류에 불과했으나, 저것이 지닌 힘과 움직임은 사람의 것이 아니었다고 했소. 그리고 다시 나타날 때마다 더욱 외관이 괴이해지고 강해졌지. 마치…….”

잠깐의 망설임 끝에 무당파 장문인이 탄식 섞인 목소리로 말을 이었다.

“사람을 해하고 그 정기(正氣)를 흡수하여 자신의 것으로 만드는 것처럼 말이오.”

“……!”

보이지 않는 충격이 대회의실을 휩쓸었다.

숨 막히는 침묵이 좌중들 사이에 내려앉았다. 미간을 찌푸린 적천강이 불쑥 입을 열었다.

“자네 말은, 저 염병할 괴물이 흡정마공(吸精魔功)이라도 익혔다는 소린가?”

무당파 장문인이 고개를 저었다.

“무량수불. 빈도 역시 쉬이 확신할 수 없습니다. 하나 저것이 암천이 의도한 결과물이며 실제로 흡정마공을 사용할 수 있다면…….”

말꼬리를 흐리는 노도사의 얼굴은 딱딱하게 굳어 있었다. 아니, 비단 그뿐만이 아니라 대회의실에 모인 대부분이 마찬가지였다.

‘그럴 만도 하지.’

흡정마공은 마교에서도 이미 실전되었다고 알려진 극악의 마공이자, 정파 무림인들에게는 악귀가 만들어 낸 무공으로 취급받는다.

그런데 암천이 그 흡정마공을 부활시켜 자신들이 만들어 낸 괴물들에게 익히도록 했다면…….

‘재앙. 그 자체.’

하지만 다행인지 불행인지는 모르겠지만 무당파 장문인의 짐작은 틀렸다. 적어도 내가 알고 있는 바로는 그렇다.

‘대부분의 몬스터는 빠르게 성장한다.’

오크가 성인 개체가 되기까지 한 달이 걸린다고 했나.

대부분의 몬스터가 강해지는 방식은 두 가지다. 처음부터 강력한 힘을 지닌 개체로 태어나거나, 혹은 다른 몬스터로부터 마력을 흡수하거나.

‘인간을 잡아먹는다면 약간의 힘을 얻을 수는 있겠지만…… 놈에게 희생된 건 양민이 대부분이고 이, 삼류 낭인들뿐.’

인간과 몬스터는 타고난 기운의 성질 자체가 다르다. 만약 상호간에 그런 작용이 가능했다면 이미 현대의 몬스터는 정력제나 보신용으로 팔리고 있었을 거다.

‘변이체라서 백 퍼센트 확신할 수는 없지만.’

지금까지의 경험상 그럴 가능성이 높겠지. 아니, 차라리 그러길 바란다. 인간의 기운을 그대로 흡수하는 괴물이 쏟아져 나온다면 도저히 감당할 수 없을 테니까.

내가 그런 생각에 빠져 있던 바로 그때. 매종학의 조용한 목소리가 대회의실에 울려 퍼졌다.

“진 각주. 자네는 어찌 생각하나?”

진 각주를 찾아 고개를 돌린 나는, 사람들의 시선을 느끼고 멈칫했다.

‘잠깐만. 진 각주면…….’

시벌, 나네. 아직 익숙하지가 않아서 깜빡했다.

“저 말씀이십니까?”

“그래. 바로 자네의 의견을 묻고 있네.”

“글쎄요. 이게. 참.”

머뭇거리는 내게, 매종학이 담담한 표정으로 말했다.

“괜찮네. 무슨 말이든 해 보게.”

“어떻게 말해야 할지 모르겠어서요.”

“자네 식대로 하면 되네. 간단명료하게.”

간단명료하게라. 나는 잠시 고민하다 조심스럽게 입술을 뗐다.

“제 생각으로는 약간, 아니 어쩌면 상당히…….”

“상당히?”

수십 쌍의 뜨거운 눈빛을 응시하며, 내가 대답했다.

“좆 된 것 같습니다.”

“……!”

“……!”
```

## Final English reading copy

```markdown
# Chapter 546

“The Alliance Leader is entering.”

Five doors opened one after another to the accompaniment of a deep voice. As a figure slowly approached from beyond them, everyone rose from their seats at the same time, as though they had rehearsed it.

“Nom, nom. Munch, munch.”

“……”

Everyone except this bastard.

*The more I look at him, the crazier he seems.*

I was not exactly the most polite person myself, but I at least had a basic sense of propriety. I leaned toward Cheongpung, who was determined to safely store every last piece of leftover food inside his mouth, and whispered,

“What the hell are you doing? Do you have a problem with society? Don’t you like the Murim Alliance?”

Cheongpung swallowed what was in his mouth and stood up before answering.

“But there’s still food left, Benefactor.”

“Then stop eating.”

“But the dumplings will get cold.”

“……”

*You bastard, Cheongpung. You Guan Yu bastard. You know the dumplings will get cold, but you have no idea that everyone else’s stares are growing cold…*

*Well, he’s always been like this.*

Cheongpung would not be Cheongpung if he cared about the gazes around him. I let out a small sigh, poked him in the side, and muttered,

“If you’re done eating, let’s focus. Our esteemed Azure Dragon Pavilion Master.”

At the words *Azure Dragon Pavilion Master*, Cheongpung pushed out his lower lip and nodded. Then a small, thoroughly disgruntled voice escaped him.

“Yes, Benefactor.”

The name Two Dragons Pavilion remained unchanged, but the organization had been divided internally into my Fire Dragon Pavilion and Cheongpung’s Azure Dragon Pavilion. According to the conversation I had with Cheongpung on our way here after being summoned to the great conference, he had wanted to give his pavilion a different name—but Mungyeong had fiercely opposed it.

*I don’t like that name.*

*Why? I think Azure Dragon Pavilion sounds pretty cool. Still, it is a little unfair. Aren’t you the Pavilion Master? Shouldn’t you at least be allowed to choose your own name?*

*I thought so too, but Grandpa Mun said he hated it. He threatened to quit if I used a name like that.*

*It was that bad? What name did you want to use originally?*

*Dumpling Pavilion.*

*……*

*Or maybe Sweetmeat Pavilion.*

*……Oh. Right.*

*Hoo. I hate Grandpa Mun. What’s so great about Azure Dragon Pavilion, anyway?*

It was ridiculous even now. *You should be grateful, you lunatic.*

If he was going to go that far, he should have called it Gim Bugak Pavilion.[^1] The words rose to my throat, but I swallowed them back.

Not because it was already in the past.

The highest authority in orthodox Murim had finally entered the great conference hall.

*Tap.*

Footsteps cut through the quiet silence. At last, Murim Alliance Leader Mae Jonghak reached the seat of honor and gave everyone a genial smile.

“You have all gathered.”

Unlike the previous meeting, this gathering included the heads of the key organizations under the Alliance Leader’s Office. That also meant the Murim Alliance’s internal reorganization was finally complete.

*There are quite a lot of us when we’re all gathered like this.*

I quickly surveyed the room. There were unfamiliar faces, as well as several familiar ones.

The unfamiliar faces belonged to masters whose names and sobriquets I had heard but never met. The familiar ones, however, included more than a few people I was glad to see.

“You’re awfully late. My butt nearly went numb.”

The people who could speak to Mae Jonghak that way could be counted on one hand, even if you turned the whole world upside down and shook every soul out of it.

Jeok Cheongang was the most prominent among them. Seated directly beside the seat of honor, he stood with one leg cocked and spoke in his usual surly tone.

Across from him, seated in the middle of the room, Jin Wikyung glanced around nervously before opening his mouth.

“Great Hero Jeok.”

“What?”

“You know how it is.”

“Good grief. Now that you’ve got a title, are you taking the Alliance Leader’s side?”

Jin Wikyung paused for a moment and gave an awkward smile. In the space of just a year and several months, he had taken the helm of the Jin Family of Taiyuan as Acting Family Head and brought astonishing growth to a family that had been slowly declining. Before anyone knew it, he had become one of their number.

“It’s not that—”

“I know. I know. Now the two brothers are making a fuss together.”

Mae Jonghak smiled at the grumbling Jeok Cheongang.

“Don’t be like that, Great Hero Jeok. Or should I call you the head of the Five Kings Hall now?”

“……Hmph. I understood you perfectly well, so stop. There are too many eyes watching.”

“Then I suppose I’ve summoned busy people here only to spout nonsense.”

It was hard to imagine anyone busier than Mae Jonghak, but he was not wrong.

Each person gathered here was a vital part of the vast Murim Alliance, one of the cogs that kept it moving.

*The Two Halls, Three Divisions, Five Pavilions, Five Gardens, and Ten Squads—Nine Squads in the characters.*

The only organization standing shoulder to shoulder with the Alliance Leader’s Hall, led by Murim Alliance Leader Mae Jonghak, was the Five Kings Hall, now headed by Jeok Cheongang. Beneath them were the Three Divisions and Five Pavilions belonging to the Inner Hall, followed by the Five Gardens and Ten Squads, which were occupied by people from the Five Great Families and the Nine Sects and One Gang.

*And there are even more besides them.*

Amazingly, the people gathered here were not everyone. If the unit heads and squad commanders of the Outer Hall were included, even this vast conference hall would not have enough room. They would have to use the training ground.

That was proof of just how enormous the Murim Alliance was. It also meant that Cheongpung and I had been recognized as members of its central leadership.

*Well, it’s still basically an honorary position without any real authority.*

Perhaps it was the difference between a position and a rank. My official position was Pavilion Master, but in terms of actual standing, I was close to the lowest seat among those gathered here.

Of course, there was no one else around my age who held a position like this.

*Ah. There was one other person besides Cheongpung.*

One-Ride Heavenly Dragon Murong Yeonghwi.

A genius who had been called Murim’s greatest young prodigy only two years ago. He was the Lesser Family Head of the Murong Family and had recently been appointed a Squad Leader of the Murim Alliance’s Outer Hall. I had heard that instead of following his father, the Family Head, to Henan, he had remained in Liaoning to oversee the family’s defenses.

*I thought I might finally get to see him in person.*

Then again, there was no stupider act than leaving one’s base undefended just to attend a meeting in Henan. Everyone else here must have completed their defensive preparations in the same way.

*Swish.*

Mae Jonghak slowly raised one hand and spoke.

“All right, everyone, sit down. We don’t have enough time to maintain such formalities.”

But nobody returned to their seats.

More precisely, they could not.

The instant Mae Jonghak raised his hand, something unidentified drifted slowly upward from beyond the doors that remained open.

“How can he use Seizing an Object Through Empty Space so effortlessly…?”

Someone muttered under their breath.

The object was covered by a cloth, so its identity could not be made out. But it was obviously enormous and seemed to possess considerable weight. Exclamations of admiration rose at Mae Jonghak’s internal energy as he moved it without effort.

Yet several people’s faces had already hardened.

Mine must have, too.

*This isn’t about his internal energy. That thing is…*

Of the five senses, the first to react was the nose—my sense of smell.

The scent was so faint that even a martial artist with heightened senses would have had trouble identifying it immediately. But the moment I caught that stench, I understood.

“Benefactor. Is this smell perhaps…?”

Cheongpung’s eyes widened as he asked the question. I gave him a small nod.

“That’s right. It’s the smell of a corpse.”

“……!”

The smell of a corpse was exactly what it sounded like: the stench of a rotting body.

I had encountered that foul odor countless times while traveling between the modern world and Murim. This time, I was more certain than anyone.

At the same time, a suspicion about the corpse’s identity flashed through my mind.

*If my guess is right, then that is…*

The next moment, the cloth stained dark red with blood was pulled away.

Everyone in the great conference hall let out a groan almost simultaneously.

“Hk!”

“W-What in the world…?”

“Alliance Leader, what is the identity of this thing?”

Voices filled with shock burst out from every corner. Those who already knew about it and those who did not were all forced to feel the same shock at that moment.

The sight hidden beneath the cloth was that horrifying.

*A monster.*

There was no other way to describe it.

At first glance, it had the shape of a human being. But unnaturally elongated and thickened joints protruded grotesquely from all over its body, while its wide-open eyes had lost their light and were as large as a child’s fist.

And the creature’s grotesque features did not end there.

“Th-There’s a horn.”

“That’s not all. Its arms…”

A black horn rose from the exact center of its forehead, and four arms protruded from its upper body.

They differed in length and thickness, perhaps because they had been severed during the battle. But no one could dispute that they were human arms.

“Hmm.”

“How could this have happened?”

As people continued to sigh, someone suddenly spoke.

“Infinite Life Buddha. It is indeed unbelievable. I felt the same way at first.”

The speaker was an old Daoist with a snow-white beard reaching his chest and deep-set eyes.

He was the Sect Leader of Wudang.

The people whose attention had focused on him looked puzzled.

“At first…?”

“Do you mean…?”

The Sect Leader of Wudang nodded.

“That is correct. Some of you may already have heard this, but that man—or rather, that thing—was originally a fisherman named Jang Sam.”

Information I had heard earlier in the Hidden Shadow Pavilion now flowed from the old Daoist’s lips.

A fisherman with an ordinary name, no different from anyone else, had disappeared. One month later, he had reappeared as a monster and a Killing Ghost that had thrown Hubei Province into an uproar.

“When it was first discovered, its martial arts were only Third Rate. However, its strength and movements were said to be inhuman. And each time it appeared again, its appearance became more grotesque and its strength greater. As though…”

After a brief hesitation, the Sect Leader of Wudang continued in a voice filled with sorrow.

“As though it harmed people, absorbed their vital essence, and made it its own.”

“……!”

A shock no one could see swept through the great conference hall.

A suffocating silence settled over the gathering. Jeok Cheongang wrinkled his brow and suddenly spoke.

“Are you saying that goddamn monster learned the Essence-Siphoning Great Technique?”

The Sect Leader of Wudang shook his head.

“Infinite Life Buddha. I cannot easily be certain of that either. However, if that thing is the result Dark Heaven intended to create and it can truly use the Essence-Siphoning Great Technique…”

The old Daoist’s voice trailed off, his face rigid.

He was not the only one. Most of the people gathered in the hall looked the same.

*It’s understandable.*

The Essence-Siphoning Great Technique was a demonic martial art so terrible that it was said to have been lost even within the Demonic Cult. Orthodox martial artists regarded it as a martial art created by fiends.

But if Dark Heaven had revived that technique and taught it to monsters they had created…

*That would be a catastrophe. Nothing less.*

Fortunately—or unfortunately—I did not know which—the Sect Leader of Wudang’s guess was wrong.

At least, as far as I knew.

*Most monsters grow rapidly.*

*Didn’t they say an Orc takes only a month to reach adulthood?*

There were two main ways most monsters became stronger.

They were either born as individuals possessing tremendous power from the beginning, or they absorbed mana from other monsters.

*Eating humans might give them a small amount of strength, but most of the people this thing killed were commoners and Third Rate or Second Rate wandering martial artists.*

Humans and monsters were born with fundamentally different types of energy.

If such an interaction were possible between the two species, modern monsters would already be sold as aphrodisiacs or health tonics.

*I can’t be one hundred percent certain since it’s a mutant.*

But based on everything I had experienced so far, that was the more likely possibility.

No, I hoped it was.

If monsters capable of absorbing human energy directly began pouring out into the world, there would be no way to deal with them.

It was just as I was lost in those thoughts that Mae Jonghak’s quiet voice echoed through the great conference hall.

“Pavilion Master Jin. What do you think?”

I turned my head toward the voice calling for Pavilion Master Jin—and froze when I felt everyone’s gazes on me.

*Wait. Pavilion Master Jin means…*

*Fuck. That’s me.*

I still wasn’t used to it, so I had forgotten.

“Are you speaking to me?”

“That’s right. I’m asking for your opinion.”

“Well, I mean. This is quite…”

I hesitated, and Mae Jonghak said in an even voice,

“It’s all right. Say whatever comes to mind.”

“I’m not sure how I should put it.”

“Say it in your own way. Simply and clearly.”

Simply and clearly.

I thought for a moment, then carefully parted my lips.

“In my opinion, things are a little—or perhaps considerably…”

“Considerably?”

I stared into dozens of pairs of burning eyes before answering.

“I think we’re fucked.”

“……!”

“……!”

[^1]: Gim bugak is a Korean snack made from seasoned seaweed coated in rice paste and fried. Its final syllable, *gak*, sounds the same as the Korean word rendered “Pavilion” in the names above.
```
