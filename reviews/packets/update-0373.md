<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0373.txt",
      "sha256": "f7e7fcb5c21526b3fcf30d133884442261cacbe38e3e8eb9256bbd37c0fd334d",
      "bytes": 14543
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1e9bedde94a87679cae79444aa066d2e1c5291ce925397966c58c3fcddd44c83",
      "bytes": 2792
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "27196875a464eda2979ed9df638de088fc239c99f0f055d75761c6a02b8a16ef",
      "bytes": 130190
    },
    {
      "path": "characters/Cheongpung the Ancient Sword.md",
      "sha256": "2123f3fc8921dfbb065c3b301928edc12bb56a3674fe94ba3276b5b1680d0564",
      "bytes": 583
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "8b080e5b1a647881d9b0863e8a2f0d8c0eb90f44f7cc48fbec4a3e99565ae5cd",
      "bytes": 894
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "9560cf50b435d108b0401bb5e2eab9ea044c443cb3bb7b6fa218861b6839f796",
      "bytes": 570
    },
    {
      "path": "characters/Extinction Divine Nun.md",
      "sha256": "86a8380e24986c039ea6810ab690b10181128c3bc29c6eb942e7d93883d6be9e",
      "bytes": 655
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "6b1b349949bc3b64083738019e82732ab68e0eb5f93d9a458396fc95eff52954",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "829a960bc36b92fa90bd66a6406a7d2f1feaa07dbfb69e82b7c175f5b4dd4b0f",
      "bytes": 1390
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "8cf5b03869a56a5ac5fee24956ac5d3d62747fe7cfd8ca3b864910e75ac08e23",
      "bytes": 589
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "7ef8282657f7c47c8ab92e32779d8e5232d53cbb2519bfea13564906b90d6e9c",
      "bytes": 99419
    }
  ],
  "estimated_tokens": 11873
}
-->

# Durable State Update — Chapter 373

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 373. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 373. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings (Arabic digits allowed in titles such as 1팀장; do not romanize). At
least one endpoint must occur in the source. The controller drops pairs already
in the address ledger. Do not invent risk-register rows. Beat plot paragraphs
are plain strings; continuity and translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 373,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 373,
    "continuity_sources": [373],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
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
    "Jin Taekyung is awake after exhausting himself, has reached the Supreme Peak realm and manifested Force, and is publicly known as the Blazing Flame Divine Dragon.",
    "Jeok Cheongang is alive but remains weakened and is recovering his strength.",
    "Dong Feng's dantian and martial arts were destroyed while shielding Jeok Cheongang; the Divine Physician is Mungyeong's Master.",
    "Mungyeong is the Slaughter Saint and Dong Feng's Disciple; Jin Taekyung knows Mungyeong's identity.",
    "Hyuk Mujin and Gung Gibang are badly wounded after fighting the Third Fiend, and the Seven Fairies intervened to save Hyuk Mujin from being torn apart.",
    "Cheongpung remains a Supreme Peak master and is at the Sichuan Tang Clan with the Thousand-Year Poison Horned Snake Mimi.",
    "The Lord of Heaven temporarily possessed the Western Heaven Demon Lord's body and escaped after One Annihilation.",
    "The Myriad-Poison Ring remains in Jin Taekyung's possession and cannot be appraised by the System.",
    "A hidden cavern near Chengdu contains the inactive Moving Formation, which Dark Heaven used to transport large numbers of people; the Slaughter Saint identifies Dark Heaven as the successor to the Demonic Cult.",
    "Extinction Divine Nun is alive and serving as Emei Sect Leader; she and Cheongpung the Ancient Sword are investigating the strange formation linked to Dark Heaven."
  ],
  "continuity_sources": [
    372
  ],
  "open_questions": [
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Why did Mungyeong tell the companions that Jin Taekyung ordered the rescue of Emei?",
    "What is the true nature and purpose of the Lord of Heaven, and what became of the Western Heaven Demon Lord?",
    "What was the origin and purpose of the Moving Formation, and why did it lose its power?",
    "How will Dark Heaven respond to the failed Three-Gate Bloodbath?"
  ],
  "safe_through": 372,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon.",
    "Use Mimi for 미미 and Mimi-chan for 미미쨩.",
    "Use Third Fiend for singular 삼괴 references and Three Fiends for collective references.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, and 신니 as Venerable Nun in forms of address.",
    "Render 환영진 as illusion formation and 이동진 as Moving Formation."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 살성     | **Slaughter Saint**           | —              |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 선배     | **Senior**                                   |
| 시스템              | **System**                     |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 아이템              | **Item**                       |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 청풍고검 | **Cheongpung the Ancient Sword** | Alias of the Qingcheng Sect's Sect Leader; distinct from Cheongpung. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 멸절신니 | **Extinction Divine Nun** | Presumed-dead Supreme Peak master and Heaven-Shaking Venerable Nun’s only Senior Aunt. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 사서삼경 | **Four Books and Three Classics** | Confucian texts used to describe conventional scholarly learning. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 열화신공 | **Fire Gate Divine Technique** | Secret internal cultivation technique of the Fire Gate Clan, preserved through one-person succession without leakage. |
| 청성파 | **Qingcheng Sect** | Sect named in Baek Museong's comparison about disciplinary rules. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 후개 | **Successor Beggar** | Title of the Beggars' Sect successor competing in the preliminaries. |
| 타구봉법 | **Dog-Beating Staff Technique** | Beggars’ Sect staff technique. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화룡신창 | **Fire Dragon Divine Spear** | Taekyung's spear technique, at the seventh stage in this chapter. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 아미파 | **Emei Sect** | Murim sect in Sichuan. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 청풍고검 | 멸절신니 | sect_leader_to_senior_sect_leader | Venerable Nun | formal-deferential | Cheongpung the Ancient Sword addresses her as 신니 while praising Jin and Cheongpung. |

## Listed compact profiles

### Cheongpung the Ancient Sword.md

# Cheongpung the Ancient Sword (청풍고검)

- **Safe through:** Chapter 372
- **Aliases:** None
- **Role:** Sect Leader of the Qingcheng Sect and a Supreme Peak martial artist investigating Dark Heaven's strange formation alongside Extinction Divine Nun.
- **Personality:** Straightforward, genial, and willing to help with matters he considers worthwhile.
- **Voice:** Warm, plainspoken, and good-humored.
- **Relationships:** He is investigating Dark Heaven's strange formation alongside Extinction Divine Nun.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 372
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 371
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is the legendary physician also known as Dong Feng and Mungyeong's Master, whose dantian and martial arts were destroyed while shielding Jeok Cheongang.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** The Slaughter Saint is his Master, and Mungyeong is his Disciple.

### Extinction Divine Nun.md

# Extinction Divine Nun (멸절신니)

- **Safe through:** Chapter 372
- **Aliases:** None
- **Role:** Living Emei Sect Leader and Supreme Peak master who joins Cheongpung the Ancient Sword in investigating a strange formation linked to Dark Heaven.
- **Personality:** Not established beyond the fear and shock her sudden reappearance caused among the Emei disciples and the Third Fiend.
- **Voice:** Not established.
- **Relationships:** She is Heaven-Shaking Venerable Nun’s only Senior Aunt and was believed to have died after withdrawing from worldly affairs thirty years earlier.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 371
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 372
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is a legendary wandering martial master and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, and casually threatening or violent when dissatisfied. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 372
- **Aliases:** None
- **Role:** Mungyeong is a young medical apprentice and Disciple of Dong Feng who is the Slaughter Saint.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** Initially timid and deferential, he becomes clear, composed, and eloquent when arguing for mercy and justice.
- **Relationships:** Jeok Cheongang recognizes him as the Slaughter Saint, and he captured the Third Fiend in the hidden cavern.

## Korean source

```text
＃373화



돌아오는 길은 짧았다.

가는 길에는 정황을 주고받느라 속도라도 조절했지, 게임으로 치자면 초절정 고수가 자그마치 다섯이나 함께하는 초호화 파티다.

평범한 사람이었다면 한나절이 걸렸을 거리는 이제 바짝 좁혀져 있었다.

“수고했네, 진 시주.”

“아직 피로할 터인데 따라와 줘서 고맙고.”

사천당문 인근에 이르러 인사를 건네는 두 장문인의 말에 나는 어깨를 으쓱해 보였다.

“아닙니다. 별로 도와드린 것도 없는데요, 뭐.”

“하긴.”

“그건 그렇지.”

“…….”

아니, 도움이 못 된 건 사실이긴 한데 이건 너무한 거 아니냐.

나를 보며 희미하게 웃어 보인 청풍고검이 살성과 적천강을 향해 포권을 취했다.

“두 분 선배님들께도 감사드립니다. 괜한 발걸음을 하게 만든 것이 아닌가 싶어 송구스럽군요.”

살성과 적천강이 동시에 대답했다.

“괜한 발걸음은 맞았지.”

“다음부터는 송구스러워할 일을 만들지 말게. 알았나?”

“……아, 예.”

그래, 내가 딱 저 기분이었다니까.

떨떠름한 표정의 청풍고검을 향해 살성이 말을 이었다.

“그리고…… 앞으로는 나를 찾는 일이 없길 바라지.”

귀찮으니 적당히 불러라, 라는 뜻이 아니다. 잠시 살성으로 돌아왔던 그는 다시 어린 의생, 문경으로 돌아가려 하고 있었다.

나는 물론이고 이 자리의 모두가 그 말에 담긴 의미를 알아차렸다.

그중에서도 가장 당황한 것은 두 장문인이었다.

“서, 선배. 그건…….”

“시주. 다시 한번 생각해 봄이 어떻겠소?”

그러나 대답 대신 돌아온 것은 살성의 건조한 눈빛이었다.

잠시 말이 없던 청풍고검과 멸절신니가 작은 한숨과 함께 고개를 끄덕였다.

“……그리하겠습니다.”

“시주의 뜻을 존중하리다. 지금 당장은.”

지금 당장은. 마지막에 덧붙인 말에 유난히도 힘이 실려 있다. 살성의 입술 사이로 나직한 목소리가 흘러나왔다.

“이번에 나선 것은 자그마한 변덕이었을 뿐, 내 뜻은 바뀌지 않는다.”

일말의 여지조차 주지 않는 단호한 대답. 살성의 눈동자가 나와 적천강을 향했다.

“두 사람도 알아들었으리라 믿지.”

적천강이 불쑥 입을 열었다.

“다시 어울리지도 않는 의생 행세를 할 셈인가?”

“행세가 아니야. 살성은 이미 존재하지 않고, 한 사람의 의생만이 남았다.”

“호랑이가 염소 가죽을 뒤집어쓴다 한들, 그것을 염소라고 부를 수 있을까.”

“이빨을 감추고 발톱을 숨긴다면 호랑이도 염소가 될 수 있지.”

“하지만 결국 마지막 순간 발톱을 드러냈고. 안 그런가?”

살성의 미간에 얕은 골이 파였다.

“나이가 들더니 말이 더 많아졌군. 내게 빚진 것이 있을 텐데.”

“……거참. 틀린 말이 아니라 뭐라 말도 못 하겠군.”

“대답한 것으로 알지.”

적천강과의 대화를 일축한 살성이 나를 힐끗 바라봤다.

“넌?”

“저요?”

“그럼 남은 게 또 누가 있느냐?”

“아뇨, 그게 아니라. 저한테 선택권이 있는 겁니까?”

“물론. 두 가지 선택지가 있다.”

살성이 무뚝뚝한 표정으로 입을 열었다.

“첫째. 문경이라는 어린 의생의 정체가 살성이라는 걸 떠벌린 다음 쥐도 새도 모르게 변사체로 발견되는 것. 그리고 두 번째. 아무도 눈치채지 못하게 입을 다물고 전처럼 나를 대하다가 조용히 떠나는 것.”

“…….”

“어느 것으로 하겠나?”

이야, 너무 어려운 선택지라서 순간 할 말을 잃었다.

마른침을 꿀꺽 삼킨 내가 입을 열었다.

“두 번째로.”

“잘 생각했다.”

“응.”

내 신속한 대답에 고개를 끄덕이려던 살성이 멈칫했다.

“지금, 뭐라고?”

“왜?”

“뭐?”

“아니, 왜 그래. 전처럼 편하게 대하라면서.”

“……!”

“……!”

두 장문인은 입을 딱 벌렸고, 잠시 말을 잇지 못하던 살성은 낄낄 웃고 있는 적천강을 향해 물었다.

“이거, 미친놈인가?”

“원래 그런 놈이다. 어때, 골 때리지?”

“골을 부수고 싶은데.”

나는 골이 부서지기 전에 넙죽 고개를 숙였다.

“아, 제가 순간적으로 착각을 해서 그만. 죄송합니다.”

“……개도 안 믿을 소리지만, 이번 한 번은 넘어가 주지.”

실수인 척 한번 엿 먹이려는 게 너무 티가 났나. 잠깐 가늘어진 눈동자로 나를 노려보던 살성이 입을 열었다.

“어쨌건 앞으로는 유의해라. 이 자리에 있는 사람들을 제외하면 나에 관한 사실은 아무도 모르니. 아, 청풍 그 아이는 예외다. 내 제자는 당연하고.”

“청 소협도 알고 있었습니까?”

“그래. 그 아이를 제외하고 그날 내 모습을 본 놈들은 모두 죽었다.”

사후처리 깔끔한 것 보소. 왜 사천당문에는 포로가 한 놈도 없었는지 이제야 이해가 간다.

복면 살성. 가면을 벗으면 패널이고 방청객이고 싹 다 뒈지는 거다.

‘그나저나 볼수록 기분 묘하네. 문경이 바로 그 살성이었다니.’

장강에서의 첫 만남 때부터 지금까지의 기억이 휙휙 스쳐 지나갔다.

그가 보여 준 모습 중 무엇이 진실이고 거짓일까.

내가 알던 천진난만하던 어린 의생은 이미 존재하지 않는다. 그저 무미건조한 눈빛을 지닌 천하제일의 살수가 있을 뿐이다.

순간 나도 모르게 한 가지 물음이 입 밖으로 튀어나왔다.

“왜 그토록 스스로를 감추려고 하십니까?”

저 멀리 보이기 시작하는 사천당문을 향해 나아가던 살성의 신형이 갑작스러운 물음에 우뚝 멈췄다.

짧은 침묵 끝에 의외로 차분한 대답이 들려왔다.

“무림이라면 지긋지긋하니까.”

“그래서 떠나신 겁니까?”

“그래. 두 번 다시는 살생을 저지르지 않겠다고 하늘에 맹세했지.”

이곳, 무림에서 살수는 멸시받는 존재다. 정파는 물론이고 사마외도(邪魔外道)에서도 그들은 환영받지 못한다.

더 높은 무학의 경지를 추구하는 무인이 아닌, 오직 살인을 위해 태어난 자들이라고 여겨지기 때문이다.

한 사람의 살수가 살성(殺星)이라는 별호를 얻기까지 얼마나 많은 피를 흘리고 묻혔을까. 그의 마음을 어느 정도 알 것 같았다.

하지만…….

“한편으로는 좀 궁금하네요.”

“뭐?”

“그렇게 싫어하는 무림으로 다시 돌아오신 이유가.”

“……다시 돌아오다니 무슨 헛소리냐.”

살성의 눈동자가 깊게 가라앉았다.

“어쩔 수 없는, 불가피한 선택이었다.”

“글쎄요. 그렇게 말씀하신다면 제가 할 말은 없지만 적어도 몇 가지 선택은 직접 내리신 것 같은데요. 예를 들면……”

나는 뒤통수를 긁적이며 말을 이었다.

“장강에서 마주친 어느 무림인들에게 가는 길이 같다며 동행을 청한다든지, 며칠 후 우연처럼 다시 만나 스리슬쩍 자신의 정체를 알려 준다든지. 그것도 아니면 제 이름을 빌려 개방의 후개에게 아미파를 구원하라 시키고 본인은 청성파로 가서…….”

“그만.”

“예. 안 그래도 그럴 생각이었습니다. 하나하나 말해 보니까 꽤 많네요.”

“무슨 말이 듣고 싶은 것이냐? 그 자리에서 모든 걸 방관한 채, 너와 네 스승을 포함한 수많은 사람이 죽어 가는 것을 지켜보아야 했다는 말이냐?”

“그럴 리가요. 정말 감사드리고 있습니다. 대협.”

비꼬는 것이 아닌, 정말 순도 백 퍼센트의 진심이다. 적절한 때에 나서 준 그가 아니었다면 무수한 사람들이 죽고 다쳤을 테니까.

물론 나와 적천강도 예외는 아니었을 것이다.

그러나 내 대답을 들은 살성의 반응은 사막의 모래알처럼 퍼석했다.

“날 대협이라고 부르지 마라.”

“그럼 뭐라고 부를까요?”

말없이 나를 응시하던 살성이 고개를 돌렸다.

그가 커다란 점처럼 보이는 사천당문을 향해 한 걸음을 떼자 신형이 유령처럼 미끄러진다.

불어오는 바람 사이로 소년의 목소리가 흩어졌다.

“문경. 그것으로 족하다.”

정말 그것으로 족할까. 정답은 오직 그만이 알고 있을 것이다.

나는 어깨를 으쓱하며 대답했다.

“그래, 알았다. 문경아.”

“……!”

그 순간, 앞서나가던 한 사람의 신형이 비틀거렸다.



* * *



전각으로 돌아온 내 뒤로 거머리 두 마리가 따라붙었다.

한 놈은 오른팔인지 새끼손가락인지 헷갈리는 혁무진이고, 다른 하나는 요새 때라도 밀었는지 조금이나마 피부가 하얘진 거지다.

“문경이, 쟤 왜 저래요? 왠지 모르게 조금 어두워진 느낌인데.”

“그럴 수도 있지. 스승인 신의께서도 상처를 입으셨고, 지금 기다리는 환자들도 워낙 많으니.”

“아, 그렇구나. 그런데 조장님, 문경이랑 어디 다녀오셨습니까?”

“애가 울적해 보이니까 바람 좀 쐬게 해 준 거 아냐. 넌 왜 그렇게 멍청하냐?”

“허, 살다 살다 거지한테까지 이런 소릴 들어 보네. 제가 이래 보여도 서책만 몇백 권을 읽은 사람이에요. 어디 가서 멍청하다 소리는 들어 본 적 없습니다.”

아니, 내가 볼 때는 그냥 둘 다 멍청한 것 같은데.

나는 혀끝에 맴도는 살성이라는 두 글자를 꿀꺽 삼켰다. 아마 저 녀석들은 죽었다 깨어나도 모를 거다. 문경의 진짜 정체를.

‘하긴. 그 정도 연기력이면 누구나 속아 넘어가지.’

사람들의 이목이 닿기가 무섭게 살성은 문경으로 돌아갔다.

평소 쾌활했던 소년 의생의 분위기가 아주 조금 어두워졌다고 해서 정체를 의심하는 사람은 아무도 없었다.

아니, 짐작조차 할 수 없었다고 해야 맞겠다.

“사서삼경이면 인정하는데, 끽해야 무협 소설만 줄창 읽어 놓고 서책은 무슨.”

“연애 소설도 읽었습니다. 귀염미(貴艶美) 모르세요?”

“잠깐. 귀염미라면 혹시 후기지수의 유혹, 그놈은 강했다 등등을 쓴 서생?”

“어, 아시네.”

“당연히 알지. 일결 제자 때 구걸한 돈으로 그거 빌려 보다가 왕초한테 먼지 나게 얻어맞았는데. 하, 그 새끼 지금 만나면 타구봉법으로 확 그냥.”

빠박!

“억!”

“악!

사이좋게 추억을 공유하는 두 놈의 엉덩이를 걷어차 내쫓고는 문을 쾅 닫아 버렸다.

저 자식들은 가뜩이나 생각할 일도 많은데 왜 여기 와서 난리인지 모르겠다.

‘이제야 좀 조용해졌네.’

지금쯤이면 청풍은 여기저기 쏘다니고 있을 거고, 적천강도 오늘 하루는 푹 쉬라고 했으니 당분간 날 찾을 사람은 없다.

푹신한 침상에 몸을 눕힌 나는 잠시 미뤄 두었던 일을 하기로 마음먹었다.

‘안 읽은 메시지 확인.’

띠링. 띠링. 띠링, 띠링!

끊임없이 울려 퍼지는 종소리와 함께 허공을 가득 메우는 시스템 창. 예전에도 몇 번 있었던 일이긴 하지만 이 정도면 최고 기록 경신이다.

순간 할 말을 잃은 나는 주요 메시지부터 하나씩 확인해 나갔다.



- [초절정]의 경지에 도달했습니다!

- [Lv.170 노군백]을 처치했습니다!

- 퀘스트, [초대받지 않은 손님]을 성공적으로 완료했습니다!

- 막대한 경험치와 명성을 획득하셨습니다!

- 시스템 메시지가 한도를 초과했습니다. 획득한 경험치와 명성을 합산합니다.

- [Lv.120]에 도달했습니다!

- 명성이 기준치를 돌파함으로써 새로운 별호를 획득합니다!

- 당신은 생사를 오가는 전투 속에서 스스로 깨달음을 얻었습니다. 모든 무공의 경지가 크게 상승하며 새로운 무공을 사용할 수 있습니다!

- [열화신공]의 경지가 팔 성에 도달했습니다!

- [화염신장]의 경지가…….

- [화룡신창]의…….



무수한 악수의 요청, 이 아니라 메시지의 향연.

대충 훑어보는 것만으로도 눈알이 빙글빙글 돌았다.

“……와, 씨.”

이게 다 뭐냐.

아직도 안 읽은 메시지가 절반이나 된다는 사실에 당황스러울 지경이다.

남은 개수를 파악하기 위해 손으로 스크롤을 내리는 그때, 특이한 무언가가 눈에 띄었다.



- 새로운 아이템이 당신에게 종속됩니다.

- 현재 보유 중인 종속 아이템 : [백염], [???]

- 아직 이름이 정해지지 않았습니다. 새로운 이름을 부여하면 아이템은 오롯이 당신에게 종속되며, 어디에서나 인벤토리를 통해 소환할 수 있습니다.



“여기서 이게 뜨네…….”

현대와 무림의 인벤토리는 각각 분리되어 있다. 하지만 백염과 같은 종속 아이템은 공간에 구애받지 않고 어디서든 꺼내 쓸 수 있다.

안 그래도 백염만으로는 아쉬웠던 참이었는데, 이런 행운이라니.

‘주면 나야 땡큐지.’

기대감에 부풀어 인벤토리를 확인하려던 바로 그 순간이었다.

똑똑똑.

문을 두드리는 노크 소리와 함께 한 사람이 빼꼼 고개를 내민다.

“조장님. 저 무진인데요…….”

“꺼져.”

“아니, 그게 아니라요.”

“형 바쁘다. 가서 귀염미 소설이나 봐.”

“어, 조장님도 보셨어요?”

“……아니 이 새끼가 진짜.”

안 되겠다. 우선 아이템 까기 전에 저 자식부터 까야겠다.

내가 침상에서 벌떡 몸을 일으키자 혁무진이 황급히 외쳤다.

“하남! 하남이요!”

“뭐?”

“하남에서 조사단이 왔습니다! 조장님을 찾고 있어요.”

“……조사단?”

앞뒤 다 자른 혁무진의 말에 눈살이 찌푸려진 그때.

띠링.

익숙한 알림이 귓가에 닿았다.
```

## Final English reading copy

```markdown
# Chapter 373

The trip back was short.

On the way there, we had at least slowed down to exchange information. But if you put it in game terms, this was a deluxe party with no fewer than five Supreme Peak masters traveling together.

The distance that would have taken an ordinary person half a day had been reduced to almost nothing.

“You’ve worked hard, Benefactor Jin.”

“And you must still be tired. Thank you for coming with us.”

When the two Sect Leaders spoke to me as we neared the Sichuan Tang Clan, I shrugged.

“It’s nothing. I didn’t really help much, anyway.”

“That’s true.”

“He didn’t.”

“…”

It was true that I hadn’t been much help, but wasn’t that a little harsh?

Cheongpung the Ancient Sword gave me a faint smile before clasping his hands toward the Slaughter Saint and Jeok Cheongang.

“I’m grateful to both of you Seniors as well. I’m sorry for making you come all this way for nothing.”

The Slaughter Saint and Jeok Cheongang answered at the same time.

“It was a pointless trip.”

“Next time, don’t do anything you’ll need to apologize for. Understood?”

“…Ah. Yes.”

That was exactly how I felt.

The Slaughter Saint continued, addressing the visibly uncomfortable Cheongpung the Ancient Sword.

“And… I hope you won’t come looking for me in the future.”

He wasn’t telling us to call on him sparingly because it was bothersome. After briefly returning as the Slaughter Saint, he was trying to go back to being the young medical apprentice, Mungyeong.

Everyone here understood what he meant.

The two Sect Leaders were the most flustered of all.

“S-Senior, you mean…”

“Benefactor, might you reconsider?”

But instead of answering, the Slaughter Saint gave them a dry look.

After a moment of silence, Cheongpung the Ancient Sword and Extinction Divine Nun nodded with small sighs.

“…We will do so.”

“I shall respect your wishes. For now.”

For now.

Those last words carried unusual emphasis. A quiet voice slipped from between the Slaughter Saint’s lips.

“My decision has not changed. Coming this time was nothing more than a passing whim.”

It was a firm answer that left not even the slightest room for argument. The Slaughter Saint’s gaze shifted toward Jeok Cheongang and me.

“I trust you two understand that as well.”

Jeok Cheongang suddenly spoke.

“Are you planning to pretend to be a medical apprentice again, despite how ill-fitting it is?”

“It isn’t an act. The Slaughter Saint no longer exists. Only a medical apprentice remains.”

“Even if a tiger wraps itself in goatskin, can you call it a goat?”

“If it hides its teeth and claws, even a tiger can become a goat.”

“But you revealed your claws in the end. Didn’t you?”

A shallow crease formed between the Slaughter Saint’s brows.

“You’ve grown more talkative with age. You owe me a debt, after all.”

“…Damn. I can’t argue when you aren’t wrong.”

“I’ll take that as an answer.”

After dismissing Jeok Cheongang’s remark, the Slaughter Saint glanced at me.

“And you?”

“Me?”

“Who else is left?”

“No, that’s not what I meant. Do I get a choice?”

“Of course. There are two choices.”

The Slaughter Saint spoke with an impassive expression.

“First, you can loudly announce that the young medical apprentice named Mungyeong is actually the Slaughter Saint, then be found dead without a soul knowing how. Second, you can keep your mouth shut so no one notices, treat me as you did before, and leave quietly.”

“…”

“Which will you choose?”

Wow. The choices were so difficult that I was speechless for a moment.

After swallowing hard, I opened my mouth.

“The second one.”

“Good thinking.”

“Yeah.”

The Slaughter Saint had been about to nod at my prompt answer when he suddenly stopped.

“What did you just say?”

“Why?”

“What?”

“No, I mean, why are you acting like that? You told me to treat you as I did before.”

“…”

“…”

The two Sect Leaders stood there with their mouths hanging open. The Slaughter Saint was silent for a moment before asking Jeok Cheongang, who had begun chuckling.

“Is this guy insane?”

“He’s always been like that. Gives you a headache, doesn’t he?”

“I want to smash his skull in.”

I quickly bowed before he could make good on that threat.

“Ah, I made a mistake for a moment. I apologize.”

“Not even a dog would believe that, but I’ll let it slide this once.”

Had it been too obvious that I was trying to mess with him while pretending it was a mistake? The Slaughter Saint glared at me with narrowed eyes before speaking.

“In any case, be careful from now on. Aside from the people here, no one knows the truth about me. Ah, that boy Cheongpung is an exception. My Disciple is an exception as well, of course.”

“Young Hero Cheongpung knew too?”

“Yes. Everyone who saw me that day is dead, except for him.”

Now that was some clean-up.

I finally understood why there hadn’t been a single prisoner at the Sichuan Tang Clan.

The masked Slaughter Saint. Once the mask came off, every panelist and audience member alike dropped dead.

*Come to think of it, this feels stranger the more I think about it. Mungyeong was the Slaughter Saint all along.*

Memories from the first time I met him on the Yangtze until now flashed through my mind.

Which of the sides he had shown me was real, and which was a lie?

The innocent young medical apprentice I had known no longer existed. There was only the greatest assassin under heaven, with a pair of dry, emotionless eyes.

Before I knew it, a question escaped my lips.

“Why do you try so hard to hide yourself?”

The Slaughter Saint, who had been walking toward the Sichuan Tang Clan now visible in the distance, came to an abrupt stop.

After a short silence, an unexpectedly calm answer reached me.

“Because I’m sick to death of the Murim.”

“That’s why you left?”

“Yes. I swore to the heavens that I would never take another life.”

In this place—the Murim—assassins were despised.

They weren’t welcome among the orthodox factions, or even among practitioners of the demonic, heterodox arts.

They were considered people born solely to kill, rather than martial artists pursuing higher realms of martial arts.

How much blood had an assassin spilled and been stained by before earning the sobriquet Slaughter Saint?

I thought I understood his feelings to some extent.

But…

“On the other hand, I’m a little curious.”

“What?”

“Why you returned to the Murim you hate so much.”

“…What nonsense are you talking about, saying I returned?”

The Slaughter Saint’s eyes sank deeper.

“It was a choice I had no way around. An unavoidable one.”

“I don’t know. If that’s how you put it, I have nothing to say. But it seems like you made at least a few choices yourself. For example…”

I scratched the back of my head and continued.

“You asked to travel with some martial artists you met on the Yangtze because you were headed in the same direction. A few days later, you happened to run into them again and casually revealed your identity. Or you borrowed my name to order the Successor Beggar of the Beggars’ Sect to rescue Emei Sect, while you went to Qingcheng…”

“Enough.”

“Yes. I was about to stop anyway. Now that I’ve listed them one by one, there are quite a few.”

“What is it you want to hear? That I should have stood by and watched countless people—including you and your Master—die?”

“Of course not. I’m truly grateful, Great Hero.”

I wasn’t being sarcastic. I was one hundred percent sincere.

If he hadn’t stepped in at the right moment, countless people would have died or been injured.

Jeok Cheongang and I would certainly have been among them.

But the Slaughter Saint’s response to my words was as dry as desert sand.

“Don’t call me Great Hero.”

“Then what should I call you?”

The Slaughter Saint stared at me without speaking, then turned away.

As he took a step toward the Sichuan Tang Clan, which looked like a large dot in the distance, he glided forward like a ghost.

The boy’s voice scattered through the wind.

“Mungyeong. That is enough.”

Was it really enough?

Only he knew the answer.

I shrugged and replied,

“Yeah, got it, Mungyeong.”

“…!”

At that moment, the figure walking ahead of us stumbled.

* * *

When I returned to the pavilion, two leeches latched onto me.

One was Hyuk Mujin, whom I could never decide was my right arm or my pinky. The other was a beggar whose skin had gotten a little whiter, as if he had started scrubbing off some dirt lately.

“Why is Mungyeong like that? He somehow seems a little gloomier.”

“That’s understandable. His Master, the Divine Physician, was injured, and there are so many patients waiting for treatment.”

“Oh, I see. But, Captain, where did you go with Mungyeong?”

“Isn’t it obvious he took the kid out for some fresh air because he looked down? Why are you so stupid?”

“Huh. In all my life, I never thought I’d hear that from a beggar. I may look like this, but I’ve read several hundred books. I’ve never been called stupid before.”

As far as I could tell, both of them were just stupid.

I swallowed the words *Slaughter Saint* that were circling the tip of my tongue. Those two probably wouldn’t realize Mungyeong’s true identity even if they died and came back to life.

*Then again, with acting skills like that, anyone would be fooled.*

The instant people’s attention turned toward him, the Slaughter Saint returned to being Mungyeong.

No one suspected his identity just because the cheerful young medical apprentice seemed a little gloomier than usual.

No one could even have guessed.

“I’d give you credit if you’d read the Four Books and Three Classics, but all you’ve done is read martial arts novels nonstop. What books are you talking about?”

“I’ve read romance novels too. Don’t you know Gwiyeommi?”[^1]

“Wait. Gwiyeommi? Are you talking about the writer who wrote *The Temptation of a Young Prodigy*, *That Bastard Was Strong*, and so on?”

“Oh, you know him.”

“Of course I do. When I was a one-knot Disciple, I used the money I’d begged for to rent one of those and got beaten black and blue by the gang boss. If I ran into that bastard now, I’d lay into him with the Dog-Beating Staff Technique. I’d—”

*Whack!*

“Gah!”

“Aagh!”

I kicked both their asses—the two idiots happily sharing their memories—and sent them out before slamming the door shut.

I didn’t know why those bastards had come here to make a racket when I already had more than enough to think about.

*Finally, some peace and quiet.*

Cheongpung was probably running around all over the place by now, and Jeok Cheongang had told me to get a full day of rest. No one would come looking for me for a while.

I lay down on the soft bed and decided to take care of something I had been putting off.

*Check unread messages.*

Ding. Ding. Ding-ding!

System windows filled the air amid the endless chimes.

This had happened a few times before, but this had to be a new record.

Speechless for a moment, I began checking the important messages one by one.

> **System**
>
> You have reached the **Supreme Peak** realm!
>
> You defeated **Lv. 170 No Gunbaek**!
>
> Quest **Uninvited Guest** successfully completed!
>
> You have acquired a tremendous amount of **EXP** and **Fame**!
>
> System messages have exceeded the limit. Acquired EXP and Fame are being totaled.
>
> You have reached **Lv. 120**!
>
> Your Fame has surpassed the threshold. You acquire a new sobriquet!
>
> Through battles that brought you to the brink of life and death, you gained enlightenment on your own. The realms of all martial arts have risen greatly, and you can now use new martial arts!
>
> **Fire Gate Divine Technique** has reached the eighth stage!
>
> **Flame Divine Palm** has reached…
>
> **Fire Dragon Divine Spear**…

An endless stream of handshaking requests—no, messages.

My eyes started spinning just from skimming through them.

“…Holy shit.”

What was all this?

I was almost stunned to discover that half of the unread messages still remained.

Just as I scrolled down to see how many were left, something unusual caught my eye.

> **System**
>
> A new Item becomes bound to you.
>
> Currently bound Items: **White Flame**, **???**
>
> This Item has not yet been given a name. If you give it a new name, it will become completely bound to you and can be summoned through your Inventory from anywhere.

“This pops up here…”

The Modern World and Murim inventories were separate. However, bound Items like White Flame weren’t restricted by space and could be pulled out and used anywhere.

White Flame alone had been leaving me wanting more, so this was quite a stroke of luck.

*If they’re giving it to me, I’ll gladly take it.*

I was just about to check my Inventory, brimming with anticipation, when—

Knock, knock, knock.

A knock sounded on the door, and someone poked their head inside.

“Captain. It’s me, Mujin…”

“Get lost.”

“No, that’s not what I meant.”

“Hyung’s busy. Go read some Gwiyeommi novels.”

“Oh, Captain, you read them too?”

“…You little bastard, seriously.”

This wouldn’t do.

Before cracking open the Item, I’d have to crack that bastard open first.

I shot up from the bed, and Hyuk Mujin hurriedly shouted,

“Henan! It’s Henan!”

“What?”

“An investigation team has come from Henan! They’re looking for you, Captain.”

“…An investigation team?”

I frowned at Hyuk Mujin’s completely contextless explanation.

Ding.

A familiar alert reached my ears.

[^1]: *Gwiyeommi* (貴艶美) is a literary pen name meaning “precious, bewitching beauty.”
```
