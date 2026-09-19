<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0477.txt",
      "sha256": "fa1b94975e8c741e1bab87eb5226b6da296590020658d032429b9aea75644bba",
      "bytes": 13808
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1f84e301a3d612a8a385d9e05d4e23d340d595d67da5fdac7c2e3f75c5c01657",
      "bytes": 3352
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "7c0bfa2601e8c0d2acf8294ca78016f5d6dbf8843f5b0a02d53ecb04c2bc02dc",
      "bytes": 153226
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "a5b6922f538520093fbd664ba4f1eb264059c087582672a5fdcecf72a305522b",
      "bytes": 1006
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0003f976970e746bbb6f4843a9175cd909b5acfaf86fd8073881d01c787a613e",
      "bytes": 553
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "4cd07d1c1d0ba67a69807e0a14d06826d381b01d52a3da2cfd693b0ca579ebec",
      "bytes": 1542
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "aaf462a758bd046e32e12b3326b9216e932422c0592ebafd45223f6603e6d6ec",
      "bytes": 1777
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "eb2fcce4449f95feb39552455fafbb36e64aa503032da385f8a63f94317d3530",
      "bytes": 622
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "1ebac4ea1dfc87a0dcd35eb18a3f2c06e96283cd819f9bb06c8ccb7b394d191b",
      "bytes": 771
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bb882cf37f97b20509363dde65c544ab530ac7be2754709b99da838a8410a1ae",
      "bytes": 147867
    }
  ],
  "estimated_tokens": 11831
}
-->

# Durable State Update — Chapter 477

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 477. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 477. Profile updates may replace only one
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
  "chapter": 477,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 477,
    "continuity_sources": [477],
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
    "Taekyung's forced System Quest, Corrupted Spirit Beast, remains active with Logout disabled and the Mutated Water God Dragon as its target.",
    "The Water God Dragon was once a noble spirit beast awaiting ascension before an unknown power corrupted it into an evil beast.",
    "Taekyung now treats the confrontation as a hunt, has dispelled the dragon's Fear with qi, and commands Jeok Cheongang, Cheongpung, and Mungyeong in a coordinated raid.",
    "The battle remains active on land after the dragon was lured away from Dongting Lake; all four attackers have received Taekyung's signal to strike.",
    "The dragon's Berserk Status increases all abilities but clouds combat judgment, and its rampage continues.",
    "Taekyung possesses the Heavenly Martial Physique, giving him superhuman physical strength independent of his accumulated internal energy and martial enlightenment.",
    "The dragon's scales are so durable that early Peak Sword Energy cannot properly cut them; Force is normally required to split them and damage what lies beneath.",
    "Cheongpung remains resistant to Fear, while Mungyeong and Jeok Cheongang remain partially affected but continue fighting as the former Slaughter Saint and Fire King.",
    "The dragon possesses extreme speed, immense durability, black scales, centuries of accumulated qi, and sharply increased physical strength.",
    "The dragon's anger manifests as violent storms, lightning, swollen river whirlpools, and other responses from the surrounding water and weather.",
    "The dragon's black pupil accompanies Breath: it forms massive water spheres, can fire them repeatedly in rapid succession, and has shown a corresponding increase in power.",
    "Zhuge Feng remains under cover protecting the others, the severely injured Dongting Fisherman remains alive for interrogation about Dark Heaven, and an unidentified figure remains on the dragon's head."
  ],
  "continuity_sources": [
    476,
    475
  ],
  "open_questions": [
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Did the Mutated Water God Dragon destroy Donghu Stronghold and the related Yangtze River Channel League strongholds, and why was no Moving Formation trace left?",
    "What unknown power corrupted the Water God Dragon, and is it related to the black pupils and sudden increase in power?",
    "Who is the unidentified figure hanging from the dragon's head, and why can that figure tear out its whiskers barehanded?"
  ],
  "safe_through": 476,
  "temporary_decisions": [
    "Render 광폭화 as Berserk and preserve the System Status distinction.",
    "Render raid-game terminology consistently and preserve Taekyung's profane, improvisational combat humor and Jin-ho's deliberately absurd USB-related saying.",
    "Render 장수 돌침대 as Jangsu stone bed with an explanatory footnote.",
    "Continue rendering 수염 as whiskers and distinguish the dragon's anomalous qi from Force and Sword Energy.",
    "Retain jang and geun measurements, along with established renderings of live-fish sashimi and bone-in sashimi."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 화산파    | **Huashan**                      |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 검법     | **sword technique**                              |                                                       |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 레이드     | **raid**              |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 정마대전   | **Great Faction War**         |
| 대사      | **Master** for a senior Buddhist monk                           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 매화검법 | **Plum Blossom Sword Technique** | Huashan sword technique Cheongpung performed at age ten. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 브레스 | **Breath** | Dragonkin power used by the Wyverns. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 달마대사 | **Bodhidharma** | Famous Shaolin figure cited alongside Lü Dongbin and Jang Samfeng. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 진태경 | 엄마 | son_to_mother | Mom | casual and startled | Jin cries out to his mother as she charges at him during the hospital visit. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 엄마 | 진태경 | mother_to_son | my son | warm and affectionate | Taekyung's mother praises him during the public welcome. |
| 진태경 | 수신룡 | hostile martial artist to monster | you, sibu-leol eel bastard | blunt, insulting, and fearless | Taekyung directly insults the emerged Water God Dragon before attacking it. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 476
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 476
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 476
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, and pathologically afraid of water. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 476
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, and can command coordinated raids against powerful monsters.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 476
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 476
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple, and he has reached the Returned to Youth realm.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple; Jeok Cheongang is an old acquaintance, and Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

## Korean source

```text
＃477화



쉬쉬쉬쉭!

전후좌우.

사방을 점하며 쏘아지는 네 개의 신형을 알아챈 순간, 변이된 수신룡은 하나밖에 남지 않은 눈동자를 크게 떴다.

- 크륵!

도대체 언제?

비록 [광폭화] 상태에 빠진 수신룡이었지만 상황이 좋지 않게 흘러가고 있다는 것쯤은 알 수 있었다.

하지만 분노로 인해 마비된 이성과 크고 아름다운 거체에 깃든 강대한 힘은 이 괴이하고도 끔찍한 악물(惡物)로 하여금 상대를 과소평가 하게 만들었다.

그리고 곧이어 들려온 누군가의 외침은, 아슬아슬하게 위기를 감지하고 있던 마지막 이성의 끈을 싹둑 잘라 버리기에 충분했다.

“모두가 널 욕해도 난 네가 좋은 놈이라고 믿어. 왜냐하면 ‘모’난 구석이 없거든.”

- 크르르……!

성인 장정과 엇비슷한 크기의 동공에 흉광이 번뜩였다.

저 조그맣고 하찮은 인간이 뭐라 지껄였는지는 상관없다.

지난 수백 년간 자신의 자랑이자 훌륭한 무기요, 영혼의 동반자나 다름없던 수염을 모조리 뽑아 버린 그놈이라는 사실이 중요할 뿐.

죽인다. 저 빌어먹을 인간만큼은 무슨 수를 써서라도 죽일 것이다!

후우우우웅!

필살(必殺)의 의지가 실린 거대한 꼬리가 모든 것을 터트리며 나아갔고, 그 방향의 끝에 있던 한 사람의 입꼬리가 슬쩍 올라갔다.

“걸렸다. 개새끼.”

뭐라고?

변이된 수신룡은 찰나지간 전신을 엄습하는 한기를 느꼈지만 이미 한발 늦은 후였다.

엄청난 힘과 속도가 실린 꼬리를 회수하는 것은, 쏘아진 화살을 되돌리는 것만큼이나 불가능한 것이었으니까

후우웅, 꽝!

맹렬하게 휘둘려진 꼬리에 모든 것이 으스러졌다. 아슬아슬하게 버티고 있던 절벽이 완전히 무너져 내리고 터져나온 굉음이 모든 소음을 집어삼킨다.

그러나 변이된 수신룡을 기다리고 있던 것은 원수를 압살했다는 짜릿한 기분이 아닌, 불에 탄 듯한 통증이었다.

화륵, 푸푹!

아니, 그것은 착각이 아니었다.

다음 순간 변이된 수신룡은 똑똑히 볼 수 있었다.

서서히 흩어지는 비바람과 흙먼지 사이, 자신의 크고 아름다운 꼬리를 정확히 관통한 청백색 화염이 깃든 창 한 자루를.

그리고 그 창을 틀어쥔 빌어먹을 인간 놈의 웃음을.

“잡았다.”

- ……!



* * *



우리 어머니는 자식 교육에 관대하신 분이셨다.

꼭 공부가 성공의 왕도라고 생각하지 않으셨고, 고등학교 시절 전 과목 7등급으로 슬롯머신 잭팟을 찍었던 성적표를 보시고도 짤막한 한 마디로 훈계를 마무리 지으셨다.



‘굉장하네, 우리 아들…….’



음. 다시 생각해 보니 이미 반쯤 포기 상태였던 것 같기도 한데.

어쨌건 그런 어머니조차 내가 어릴 적에는 책을 읽게 하셨다.

초등학교 때였나, 내가 영어 학습지로 종이비행기를 만들어 날리는 걸 보시고 이거라도 보라며 책 한 권을 내미셨는데 그 책의 제목이…….

아, 그래.

‘걸리버 여행기.’

공부에는 영 재능이 없던 나도 그런 류의 소설은 재밌게 읽었고, 때로는 소설에서 읽은 인상 깊은 장면들을 하연이에게 적용해 보기도 했다.

이를테면 소인국 사람들이 걸리버를 밧줄로 결박하는 장면이라든가.



‘엄마! 이것 좀 보세요! 제가 하연이를 붙잡았어요! 이제 얌전해요!’

‘으아아아아앙! 엄마아아아!’

‘안 돼! 하연아! 우리 딸!’



물론 호기심의 결과는 썩 좋지 않았다.

밧줄 대신 청테이프로 꽁꽁 묶인 어린 딸을 본 어머니는 비명을 질렀고, 효자손으로 불효자가 된 아들의 종아리를 때렸지만 나는 초등학생답지 않은 뚝심으로 눈물 한 방울 흘리지 않았다.

다만 내 허술함을 반성했다.



‘다음번에는 소리 지르지 못하게 입도 막아야지!’



아, 그리운 추억이여.

세월의 흐름에 따라 청테이프로 한참 어린 여동생을 꽁꽁 묶었던 악랄한 초등학생은 이제 더 이상 찾아볼 수 없지만, 그날의 기억만은 또렷하게 남아 있다.

언젠가는 걸리버를 소설 속 장면처럼 결박해 보겠다는 어린 시절의 야망도 함께.

푸푹!

그래, 바로 지금처럼 말이지.

나는 실현할 수 없으리라 생각했던 동심을 떠올리며 입을 열었다.

“잡았다.”

- ……!

소인국 사람들이 걸리버를 묶었던 것보다는 잔인한 수법이었지만 효과는 확실했다.

나는 놈의 꼬리가 날아오리란 사실을 예측하고 있었고, 크고 흉측한 그것이 몸을 후려치기 직전 피한 뒤 온 힘을 다해 창날을 박아넣었다.

백염이라는 이름을 가진 이 단단하고도 투명한 신병이기는 거대한 못이 되어 괴물의 꼬리와 지면을 동시에 관통했다.

아, 망치?

그야 당연히 내 주먹이지. 그리고 내 수중에 남아 있는 못은 아직도 아주 많다.

‘인벤토리 오픈, 소환.’

푸푸푸푹!

그야말로 순식간이었다.

번개처럼 인벤토리에서 소환한 창 다섯 자루를 놈의 꼬리에 박아넣은 나는 망치 대신 주먹을 내리찍었다.

쾅! 쾅! 꽈앙!

고정 작업 완료.

힘차게 내지른 일권이 창대의 끝부분을 후려치자 예리한 창날이 지면 깊숙이 박히며 진동한다.

‘하연아, 보고 있니.’

그 광경을 바라보는 나는 짜릿한 쾌감에 몸을 떨었고, 변이된 수신룡은 고통으로 울부짖었다.

- 그워어어어어!

하지만 내가 느끼기에, 녀석의 비명은 섣부른 감이 없지 않아 있었다.

왜냐하면 이 순간만을 기다리고 있던 세 사람이 지금 막 전력을 다한 공격을 쏟아부으려는 참이니까.

그리고 그중에서도 가장 빠르게 도착한 한 사람이, 놈의 허리를 향해 일검을 휘둘렀다.

쉭-!

유령과도 같은 움직임과 내 눈으로도 완벽히 파악할 수 없는 쾌속함.

희끗희끗한 그림자로부터 튀어나온 눈부신 섬광을 막아설 수 있는 것은 아무것도 없었다.

[광폭화]로 인해 더욱 단단해진 비늘도, 무쇠처럼 질긴 살과 뼈도 예외는 아니었다.

다름 아닌 살성(殺星)의 일검이니까.

서걱!

혼란스러운 상황 속에서도 선명하게 귓가를 파고드는 한 줄기 절삭음.

누구보다 쾌속하고 간결한 일검으로 큰 타격을 입힌 문경의 신형이 잔상을 남기며 사라지고, 폭포수처럼 솟구치는 핏물과 함께 괴성의 아가리에서 고통에 찬 비명이 튀어나왔다.

- 쿠어어억!

비록 몸통을 완전히 절단하지는 못했지만, 단 일격으로 오분의 일에 가까운 두께가 갈려 나갔으니 당연한 반응이었다.

다만 놈에게 한 가지 알려 주고 싶은 것은, 이게 끝이 아니라는 사실이었다.

“아직 두 발 남았다.”

그리고 내가 말을 끝마치기도 전, 석양을 닮은 자줏빛 강기가 어둠을 밝히며 쏘아졌다.

쉬쉬쉬쉭!

휘몰아치는 비바람 사이로 수십 송이의 홍매화(紅梅花)가 보이는 것은 결코 착각이 아니다.

화산파의 정수라 불리는 자하신공이 담긴 자줏빛 강기가 그려 내는 궤적은 눈에 익은 것이었다.

‘매화검법(梅花劍法).’

문경의 검이 표적을 일격에 절단시키는 예리한 작두라면, 청풍이 펼치는 매화검법은 수십 번에 걸쳐 베고 가르는 비수다.

그리고 지금 이 순간, 그 비수는 매화의 형태로 화하여 갈라진 상흔을 파고들고 있었다.

푸푸푸푹! 서걱!

덩치가 큰 상대를 쓰러트리는 법은 예상외로 간단하다.

뻗지 않고서는 못 배길 정도로 크고 강력한 한 방을 먹이든가. 아니면 때린 곳을 계속해서, 그것도 존나 아프게 때리는 거다.

그리고 변이된 수신룡이 몇 번째인지 모를 괴성을 내지르기도 전에, 그 두 가지를 모두 합친 한 방을 날릴 한 사람이 오고 있었다.

“썩 뒈지지 못하겠느냐, 이 애미애비 없는 악물 새끼야!”

나이는 엿 바꿔 먹은 듯한 걸쭉한 패드립과 함께 전장을 가로지르는 한 줄기 불꽃.

‘화왕(火王).’

구화산의 불법 거주민, 정마대전의 불쟁이. 달마대사 해골물에 버금가는 미친 배분과 더 화끈한 무공으로 무림을 씹어먹는 전국구 깡패.

보는 것만으로도 가슴이 뛰고 눈앞이 후끈해진다.

‘에이, 시발.’

될 대로 돼라. 이미 말도 깠는데 뭘.

호랑이 등에 올라탄 마당에 더 이상 겁날 것도 없다.

나는 피가 끓어오르는 것을 느끼며 힘껏 외쳤다.

“가라, 화왕! 멸염신권!”

“이런 개호로……!”

누구한테 하는지 모를 욕설은, 다음 순간 터져 나온 거대한 굉음에 의해 파묻혔다.

화륵, 콰아아아!

주먹 끝에서 솟구친 불꽃이 모든 수분을 증발시키며 쏘아졌다.

초고온의 열기를 머금은 겁화(劫火)가 앞서 두 차례의 공격으로 쩍 벌어진 상흔을 헤집으며 모조리 불태우고, 살라 먹었다.

- 크아아아아아!

어디선가 들은 기억이 있다.

세상에서 가장 고통스러운 죽음이 불에 의한 것이라고.

어느 누구라도 이 광경을 보면 그 말에 십분 공감할 수밖에 없을 것이다.

불지옥이 연상될 만큼 온 사방에 가득한 열기와 매캐한 살 타는 냄새.

그리고 겁화에 휩싸인 채 몸부림치는 거대한 괴물.

- ……!!

지금껏 들어 본 적 없는 엄청난 괴성에 지면이 흔들리고 동정호의 강물이 밀려 나갔다.

고통으로 인한 몸부림이 얼마나 거센지, 창을 박아 넣고 힘껏 붙잡고 있던 나조차도 더 이상 버틸 수 없을 정도였다.

푸푹, 투두두둑!

정신을 차린 걸리버가 소인국 사람들이 묶어 놓은 밧줄을 풀었을 때, 몸을 일으키는 거인을 올려다보던 그들은 무슨 생각을 하고 있었을까.

정확히는 알 수 없지만, 적어도 나는 경악하지도, 당황하지도 않았다.

“어쭈.”

어차피 달라지는 것은 없다.

극한의 원딜충, 아니 초절정 고수 셋은 내 지시를 완벽하게 수행했고 변이된 수신룡은 극심한 타격을 입었다.

이제 와서 꼬리에 박혀 있던 창을 뽑아내고, 워터 브레스를 모은다고 한들 달라지는 것은 없을 것이다.

쉬이이익, 탁!

허공섭물(虛空攝物).

다른 창들과 마찬가지로, 꼬리의 힘을 버티지 못하고 허공으로 튕겨 나가던 백염이 손아귀에 빨려 들어온다.

나는 검푸른 핏물이 흐르는 백염의 창날을 들어 놈에게 겨누었다.

“지금부터…… 닥치는 대로 썰어.”

입술 사이로 흘러나온 목소리는 용암처럼 뜨거웠고, 어느새 익숙해진 지시를 기다리고 있던 세 사람은 목줄이 풀린 맹수처럼 날뛰었다.

파팟!

적천강, 문경, 청풍. 그리고 나까지.

무림 최초이자 최강이라 불릴 만한 레이드 팀은, 고통으로 몸부림치는 괴물의 거대한 동체를 향해 쏘아졌다.

쐐애애액!

네 곳의 방향을 향해 걸음을 내딛는 네 명의 초인.

그리고 미증유의 기운이 실린 네 개의 강기가 있었다.



* * *



쉬쉬쉬쉭! 퍼걱!

화륵, 콰아아아!

동서남북. 상하좌우.

빠져나갈 틈도, 피할 수 있는 방향도 존재하지 않았다. 그들은 어디에나 있었고 어디에도 없었다.

작은 산과 같은 거체는 세상에서 가장 커다란 표적이나 마찬가지였고, 너덜거리는 꼬리는 강과 지면을 뒤엎을지언정 섬광처럼 움직이는 신형에게 닿지 못했다.

변이된 수신룡.

수백 년간 몸집을 부풀려 온 이 타락한 존재가 가진 가장 큰 장점은, 지금 이 순간 오히려 가장 큰 약점으로 뒤바뀌어 있었다.

- 크롸아아아아!

깨트리지 못할 방패도, 열지 못할 문도 없다.

촌각이라고 부를 수도 없을 만큼 짧은 시간 동안 수십 줄기의 강기에 난도질당한 괴물의 육체는 참담할 정도로 망가져 있었다.

위험하리만치 아름답던 칠흑빛 비늘은 산산이 부서졌고, 평범한 날붙이로는 흠집조차 낼 수 없는 단단한 살과 뼈는 온통 베이고 으스러진 지 오래.

콰륵, 촤아아악!

상흔으로부터 울컥 터져 나온 검푸른 핏물이 대지를 적셨다.

어느새 쉴 새 없이 내리치던 뇌성벽력도, 폭풍우와 같은 비바람도 서서히 멎어 가고 있었다.

그리고 한 존재의 생명 역시.

서걱!

- 크륵…….

또다시 엄습하는 고통.

힘없이 몸부림치던 변이된 수신룡의 동공에 문득 한 존재가 비쳤다.

그건 낯익은 얼굴을 한 젊은 인간이었다.

자신의 원수나 다름없는, 반드시 죽여야 하는!

- 그워어어어어!

그리고 오직 한 사람, 진태경의 존재가 천천히 꺼져 가던 괴물의 마지막 힘을 끌어 올렸다.

고오오오옹-!

마지막 힘을 쏟아부은 일격. 누군가는 워터 브레스라 부르는 거대한 물의 구가 순식간에 완성되려던 바로 그때.

젊은 인간의 모습이 눈앞에서 사라졌다.

그리고 다음 순간, 변이된 수신룡은 착 가라앉은 누군가의 목소리를 들을 수 있었다.

“고생했다.”

푹!
```

## Final English reading copy

```markdown
# Chapter 477

*Shwish-shwish-shwish-shwish!*

Front, back, left, right.

The instant the Mutated Water God Dragon noticed the four figures shooting toward it from every direction, its one remaining eye widened.

—Krrk!

*When did they…?*

Even in Berserk Status, the Mutated Water God Dragon could tell that the situation was turning against it.

But its reason had been paralyzed by rage, and the immense strength dwelling within its large, beautiful body caused this strange and terrifying evil beast to underestimate its opponents.

Then someone shouted.

That was enough to sever the last thread of reason that had barely sensed the danger.

“Even if everyone curses you, I believe you’re a good guy. Because you don’t have a single rough edge.”

—Krrrrrr…!

A murderous glint flashed in the pupil, almost as large as a grown man.

It did not matter what that tiny, insignificant human had been babbling about.

What mattered was that he was the one who had plucked out every single one of the whiskers that had been the dragon’s pride, its finest weapon, and practically its companion of the soul for hundreds of years.

*Kill him.*

*No matter what it takes, I will kill that fucking human!*

*Whooooooosh!*

The enormous tail, filled with lethal intent, tore through everything in its path.

At the end of that path, one man’s lips curled slightly upward.

“Got you, you son of a bitch.”

*What?*

The Mutated Water God Dragon felt a chill sweep over its entire body, but it was already too late.

With that much force and speed behind it, pulling back its tail was as impossible as recalling an arrow after it had been fired.

*Whoom, boom!*

Everything was crushed beneath the violently swinging tail.

The cliff that had barely been holding together collapsed completely, and the resulting roar swallowed every other sound.

But what awaited the Mutated Water God Dragon was not the exhilarating sensation of crushing its enemy.

It was pain like being burned alive.

*Fwoosh, thk!*

No.

This was not some illusion.

The next moment, the Mutated Water God Dragon saw it clearly.

Between the slowly dispersing wind, rain, and clouds of dust, a spear wreathed in blue-white flames had pierced straight through its large, beautiful tail.

And the smile of the fucking human gripping that spear.

“Got you.”

—……!

* * *

My mother had always been lenient when it came to raising her children.

She never believed studying was the only path to success. Even when she saw my high school report card—sevens in every subject, like a slot-machine jackpot—she ended her lecture with one short remark.

*“Amazing, my son…”*

Hmm. Now that I thought about it, she may already have given up on me halfway by then.

In any case, even my mother made me read books when I was young.

I think it was in elementary school. She saw me making paper airplanes out of an English workbook and flying them around. She handed me a book and told me to read this instead.

The title of that book was…

Oh, right.

*Gulliver’s Travels.*

Even though I had no talent for studying, I enjoyed novels like that. Sometimes, I even tried applying memorable scenes from them to Hayeon.

For example, the scene where the Lilliputians tied Gulliver up with ropes.

*“Mom! Look! I caught Hayeon! She’ll be quiet now!”*

*“Waaaaaah! Mommy!”*

*“No! Hayeon! My daughter!”*

Of course, the results of my curiosity were not particularly good.

When my mother saw her young daughter bound from head to toe with blue packing tape, she screamed. Then she beat the calves of her now-unfilial son with a *hyojason*.[^1]

[^1]: A Korean back scratcher whose name literally means “filial son’s hand.”

But with a tenacity unusual for an elementary schooler, I didn’t shed a single tear.

I did, however, reflect on my carelessness.

*“Next time, I need to tape her mouth shut too, so she can’t scream!”*

Ah, what fond memories.

Time had passed, and the vicious elementary schooler who had bound his much younger sister in blue packing tape could no longer be found.

But the memory of that day remained vivid.

Along with the ambition I had held as a child: to tie up Gulliver just like in the novel.

*Thk!*

That’s right.

Just like now.

Remembering the childhood dream I’d thought I would never fulfill, I spoke.

“Got you.”

—……!

It was more brutal than the way the Lilliputians had tied up Gulliver, but it was undeniably effective.

I had predicted that the bastard would swing its tail. I dodged just before the enormous, hideous thing lashed across my body, then drove my spearhead in with all my strength.

White Flame, the sturdy and transparent divine weapon bearing that name, became a massive nail and pierced through both the monster’s tail and the ground.

*What, did I need a hammer?*

Obviously, my fist.

And I still had plenty of nails left in my possession.

*Open Inventory. Summon.*

*Thk-thk-thk-thk-thk!*

It happened in an instant.

I summoned five spears from my Inventory like lightning and drove them into the bastard’s tail. Then, instead of a hammer, I brought down my fist.

*Boom! Boom! Booooom!*

*Anchoring complete.*

My powerful punch struck the ends of the spear shafts. The sharp spearheads sank deep into the ground and trembled.

*Hayeon, are you watching?*

I shuddered with a thrilling sense of satisfaction as I watched the scene.

The Mutated Water God Dragon screamed in pain.

—Gwoooooooooar!

But to me, its scream seemed a little premature.

Three people who had been waiting for this exact moment were just about to unleash attacks with everything they had.

The fastest of them arrived first and swung a sword at the dragon’s waist.

*Shk—!*

A ghostlike movement.

A speed too fast for even my eyes to fully follow.

Nothing could block the dazzling flash that shot out from the grayish shadow.

Not even the scales hardened further by Berserk Status.

Not even the iron-tough flesh and bones.

It was none other than the Slaughter Saint’s sword strike.

*Shrrk!*

A clear sound of cutting pierced through the confusion of battle and reached my ears.

Mungyeong’s figure, having dealt a devastating blow with the fastest and most concise sword strike in existence, vanished in a blur.

At the same time, a scream of agony burst from the maw of the monster amid blood surging upward like a waterfall.

—Kuaaaargh!

The attack had not severed the torso completely, but nearly one-fifth of its thickness had been shaved away in a single strike.

That reaction was only natural.

But there was one thing I wanted to tell the bastard.

This was not over yet.

“Two more strikes left.”

Before I had even finished speaking, purple Force resembling a sunset shot through the darkness and illuminated it.

*Shwish-shwish-shwish-shwish!*

Dozens of red plum blossoms appeared amid the swirling wind and rain.

That was no illusion.

The path traced by the purple Force imbued with the Zaha Divine Technique, known as the essence of Huashan, was instantly familiar.

*The Plum Blossom Sword Technique.*

If Mungyeong’s sword was a sharp guillotine that severed its target in a single strike, Cheongpung’s Plum Blossom Sword Technique was a dagger that cut and carved dozens of times.

And at this very moment, those daggers had taken the shape of plum blossoms and were burrowing into the split wound.

*Thk-thk-thk! Shrrk!*

The way to bring down an enormous opponent was surprisingly simple.

Either land one powerful blow so overwhelming that the opponent could not help but collapse.

Or keep hitting the same spot.

And hit it fucking hard.

Before the Mutated Water God Dragon could unleash yet another scream, someone came rushing in to deliver a blow that combined both methods.

“Can’t you just fucking die, you motherless evil-beast bastard!”

A streak of flame crossed the battlefield, accompanied by a filthy crack about the bastard’s parents that was wildly unbecoming of his age.

*The Fire King.*

The illegal resident of Mount Jiuhua.

The firebrand of the Great Faction War.

A nationwide thug who had chewed up the Murim with crazier seniority than the water from Bodhidharma’s skull and even hotter martial arts.

Just looking at him made my heart race and my eyes feel hot.

*Ah, fuck it.*

What happened, happened. I had already dropped the formalities anyway.

Once you were riding on the back of a tiger, there was nothing left to be afraid of.

Feeling my blood boil, I shouted with all my strength.

“Go, Fire King! Flame-Extinguishing Divine Fist!”

“You fucking little—!”

I could not tell who he was cursing, because the next enormous boom drowned him out.

*Fwoosh, kwaaaaaaang!*

Flames erupted from the end of his fist and shot forward, vaporizing all the moisture in their path.

Hellfire carrying superheated flames tore into the gaping wound created by the previous two attacks, burning and devouring everything inside.

—Kraaaaaaaaaah!

I remember hearing somewhere that the most painful death in the world was death by fire.

Anyone who saw this scene would have no choice but to agree completely.

Heat filled every direction, hot enough to evoke the image of hell itself, along with the thick, acrid smell of burning flesh.

And in the center of it all, a gigantic monster writhed while engulfed in hellfire.

—……!

The tremendous scream, unlike anything we had heard before, shook the ground and sent the waters of Dongting Lake surging backward.

The thrashing caused by its pain was so violent that even I, clinging to the embedded spears with all my strength, could no longer hold on.

*Thk, thud-thud-thud!*

When Gulliver came to his senses and untied the ropes binding him, what had the Lilliputians thought as they looked up at the giant rising to his feet?

I could not know for certain.

But at least I was neither shocked nor flustered.

“Oh, look at you.”

It made no difference anyway.

The three extreme ranged-DPS addicts—or rather, three Supreme Peak masters—had followed my orders perfectly, and the Mutated Water God Dragon had taken devastating damage.

Even if it pulled out the spears embedded in its tail and gathered Water Breath now, nothing would change.

*Shiiiiing, tap!*

*Seizing an Object Through Empty Space.*

Like the other spears, White Flame had been unable to withstand the force of the tail and was flung into the air.

Then it was sucked into my hand.

I raised the spearhead of White Flame, wet with dark-blue blood, and pointed it at the bastard.

“From now on… hack away wherever you can.”

The voice that slipped between my lips was hot as lava.

The three people who had grown accustomed to waiting for my orders sprang into action like beasts freed from their leashes.

*Snap!*

Jeok Cheongang, Mungyeong, Cheongpung—and me.

The first and strongest raid team in the Murim shot toward the enormous body of the monster writhing in agony.

*Shweeeeeek!*

Four superhumans took steps toward four different directions.

And four streaks of Force carried unprecedented power.

* * *

*Shwish-shwish-shwish-shwish! Shrrk!*

*Fwoosh, kwaaaaaaang!*

East, west, south, north.

Above, below, left, right.

There was no gap through which the dragon could escape and no direction in which it could dodge.

They were everywhere.

And nowhere.

The body as large as a small mountain was practically the largest target in the world. Its mangled tail could overturn the river and the ground, but it could not touch the figures moving like flashes of light.

The Mutated Water God Dragon.

The greatest advantage of this corrupted being, which had grown enormous over hundreds of years, had now turned into its greatest weakness.

—Kroooooooooar!

There was no shield that could not be broken.

No door that could not be opened.

In a span of time too short to even call a moment, the monster’s body was carved apart by dozens of streaks of Force and left in a pitiful state.

Its dangerously beautiful jet-black scales shattered into pieces.

Its flesh and bones, so hard that ordinary blades could not even scratch them, had already been cut and crushed beyond recognition.

*Craaaack, shaaaaaah!*

Dark-blue blood burst from the wounds and soaked the earth.

The thunder and lightning that had struck without pause began to fade.

The storm winds and rain also slowly died down.

And so did the life of one being.

*Shrrk!*

—Krrk…!

Pain assaulted the Mutated Water God Dragon once more.

Its body writhed feebly, and then a figure appeared in the pupil of its eye.

A young human with a familiar face.

Its enemy.

The one it absolutely had to kill.

—Gwoooooooooar!

And the presence of one man alone—Jin Taekyung—roused the monster’s last fading reserves of strength.

*Gooooooong—!*

At the very moment a massive sphere of water, what someone called Water Breath, was about to be completed after the dragon poured out every last bit of its strength…

The young human vanished from before its eyes.

Then, the next moment, the Mutated Water God Dragon heard a low, level voice.

“You’ve worked hard.”

*Thk!*
```
