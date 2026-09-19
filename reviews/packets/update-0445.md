<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0445.txt",
      "sha256": "f362f94c990d4b1f6d3ff8860b877d4bc7a032359510d1c05a4c03149ba86240",
      "bytes": 13477
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "30edf65b35e9737290ca8d3a1050cb2fbbe66057825967bc2a9c56d10da15c6b",
      "bytes": 3232
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1d6ab1d325de661a9be5b7fa02c9dfc152b1ca5e4275a554cf70df492ac28cb4",
      "bytes": 145732
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "290871915127b2f97219d9870b8fef93525568b5673a1ba7e2d42d1a303a51ad",
      "bytes": 944
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "4899170bc89910891c37055c43336c46710dcd557aeeee7281e230965a29bc99",
      "bytes": 553
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "4a13560dce7645c1b8c129d41b64b3cbe911a34bfb0a4039d5548950670ee111",
      "bytes": 1390
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "4233bb1ce8c76d9bd34cf3639c9335afe07271c09cc02f52ca8dfb6b726d2a85",
      "bytes": 894
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "76e7f69933e38158cfee56dc797311749aa93a7cc246e165dd8545fdcd6bd9f8",
      "bytes": 686
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "c0c84e17674c06f91719c5e5d3e41bd24bbe9c4deb03a853f4759c15661386e8",
      "bytes": 429
    },
    {
      "path": "characters/Zhuge Gyun.md",
      "sha256": "3ea723ad9c043d9465d7f9afd13afcdb3d173cf446bada0ed8e33ad2369d63c6",
      "bytes": 676
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "33c51e907b6b591c0b912276269b14517a71958335ceb70d7841b0885eaf4d3a",
      "bytes": 140198
    }
  ],
  "estimated_tokens": 11407
}
-->

# Durable State Update — Chapter 445

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 445. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 445. Profile updates may replace only one
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
  "chapter": 445,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 445,
    "continuity_sources": [445],
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
    "Taekyung's group has entered the Zhuge Clan's Inner Hall in Hubei after traveling with Mu Song's Water Dragon Stronghold fleet.",
    "The Yangtze River Channel League's nearby Hubei strongholds have not contacted Mu Song despite knowing of his arrival.",
    "Jin Wikyung has political ties with Yi Hongcheon, the newly appointed Hubei Provincial Administration Commissioner, and used them to resolve the harbor incident.",
    "Zhuge Gyun is the Zhuge Clan's Lesser Family Head, Zhuge Feng is its current Family Head, and Zhuge Gonghu was Gyun's great-grandfather.",
    "The Zhuge Clan is performing covert inspections and deploying disguised martial artists in its own territory because of an unexplained emergency.",
    "Family Head Zhuge Feng is waiting to receive Taekyung's group."
  ],
  "continuity_sources": [
    444,
    443
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations, and are they truly connected to black magic?",
    "Why does Mungyeong continue accompanying Taekyung's group despite being unable to explain the impulse?",
    "What confidential matter is Jin Wikyung withholding?",
    "What are the terms of the Peace Guild–Wizard Guild agreement, and what evidence is contained in Lee Jungryong's holographic recorder?",
    "What emergency has caused the Zhuge Clan's covert security measures and the fear surrounding its territory?"
  ],
  "safe_through": 444,
  "temporary_decisions": [
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor.",
    "Render 최 팀장님 as “Team Leader Choi,” 진태경 씨 as “Mr. Jin Taekyung,” 막내야 as “my youngest,” 노야 as “Old Master,” and 노 선배님 as “Senior.”",
    "Keep Peace Guild, guild house, Inventory, Magic Johnson, established martial-arts terminology, black magic, poison human, World Hunter Association, and Wizard Guild unchanged.",
    "Render 신기제갈 as “Divine Mechanism Zhuge,” 파선지왕 as “Fan-Wisdom King,” 와룡객 as “Crouching Dragon Guest,” 복룡산 as “Mount Fulong,” and 융중산 as “Mount Longzhong.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 제갈균    | **Zhuge Gyun**     |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 제갈세가   | **Zhuge Clan**                   |
| 장강수로맹  | **Yangtze River Channel League** |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 정파     | **orthodox faction**                             |                                                       |
| 가주     | **Family Head**                              |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 헌터      | **Hunter**            |
| 사천     | **Sichuan**            |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 대사      | **Master** for a senior Buddhist monk                           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 여아홍 | **Yeoahong** | Traditional Chinese rice wine; literally Daughter's Red. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 선화아 | **Ship-Fire Boy** | Mu Song's sobriquet; literally a child who lights fires aboard a ship. |
| 채주 | **Stronghold Lord** | Title used for the lord of a water stronghold. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 동정채 | **Donghu Stronghold** | Stronghold where Mu Song's Uncle Hwang is based. |
| 와룡객 | **Crouching Dragon Guest** | Epithet of Zhuge Feng. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 문경 | 무송 | survivor_to_savior_and_authority | Great Hero Mu Song | formal-deferential | Mungyeong credits Mu Song with saving him and asks him to spare Hwang Tae-gu. |
| 무송 | 문경 | stronghold_lord_to_young_passenger | you | gruff-but-considerate | Mu Song offers Mungyeong the right to decide Hwang Tae-gu's fate. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 적천강 | 문가 | hostile_interlocutors | Mun | blunt and threatening | Jeok Cheongang addresses the Slaughter Saint as Mun while defending Jin Taekyung. |
| 무송 | 적천강 | junior_martial_artist_to_legendary_martial_master | Great Hero Jeok | formal-deferential | Mu Song respectfully refers to Jeok Cheongang as 적 대협 while worrying that Jeok dislikes him. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 무송 | legendary martial master to stronghold lord | you | gruff, coercive, and dismissive | Uses 자네 while ordering Mu Song to take the group only as far as Sichuan and leave the fast ship. |
| 청풍 | 무송 | young martial companion to stronghold lord | you | cheerful and familiar | Offers Mu Song his last dumpling and then induces him to buy more in Guang'an. |
| 제갈균 | 적천강 | junior martial artist to legendary senior | Senior | formal-deferential | Gyun addresses Jeok as 노 선배님 during his introduction. |
| 적천강 | 제갈균 | legendary elder to Zhuge Clan Lesser Family Head | you / bastard | blunt and insulting | Jeok questions Gyun about Gonghu and mocks his manners. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 444
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 444
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 444
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is a legendary wandering martial master and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, and casually threatening or violent when dissatisfied. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 443
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan and belongs to the Yangtze River Channel League's moderate faction.
- **Personality:** Ambitious, domineering, impatient with interruptions, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** Mu Song is a member of the Yangtze River Channel League's moderate faction and maintains ties with its regional strongholds, including Dangyang Stronghold, Honghu Stronghold, and Donghu Stronghold, where his Uncle Hwang is based.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 444
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 444
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

### Zhuge Gyun.md

# Zhuge Gyun (제갈균)

- **Safe through:** Chapter 444
- **Aliases:** Divine Marvel Dragon
- **Role:** Zhuge Gyun is the current Lesser Family Head of the Zhuge Clan, son of its Family Head Zhuge Feng, and a scholar-styled martial artist who was a finalist in the Star-Array Grand Banquet.
- **Personality:** Analytical, pedantic, and unusually preoccupied with theoretical correctness.
- **Voice:** Polished, formal, and interrogative, treating insults as subjects for precise analysis.
- **Relationships:** Rival finalist alongside Baek Woo and Gung Gibang; exchanges restrained arguments with Taekyung.

## Korean source

```text
＃445화



드르륵.

“아.”

누군가가 작은 탄성을 흘렸다.

문이 열림과 동시에 눈앞에 펼쳐진 거대한 서고(書庫)의 웅장함도 놀라웠지만, 사람의 손길이나 공력의 움직임 없이 열린 문 때문이기도 했다.

그리고 그건 지금껏 현대인으로 살아오며 자동문을 수만 번도 넘게 드나든 내게도 상당히 신선한 경험이었다.

‘기계 장치?’

아니, 이곳은 무림이니 기관이라고 해야 하나?

막 열린 문에는 철과 목재로 만든 부품들이 복잡한 구조로 정교하게 얽혀 있었다.

그뿐만이 아니다. 천천히 고개를 돌려 바라본 서고 곳곳에는 문에 설치된 것과 같은 기관의 흔적이 뚜렷했다.

물론 현대의 최첨단 문명에 비교하면 초라한 수준이지만, 지금껏 방문했던 여느 명문 대파에서 볼 수 없었던 광경인 것은 확실했다.

‘그건 그렇고…….’

왜 아무도 없어?

그 흔한 시종이나 호위 무사는 물론이고, 가주라는 양반 역시 코빼기도 안 보인다.

나를 포함한 사람들의 시선에 제갈균이 크게 외쳤다.

“가주님!”

공력을 실은 외침이 서고 안을 메아리처럼 울렸다.

단순히 넓다기보다는 광대하다는 표현이 어울리는, 현대의 축구장보다 큰 공간.

끝없이 늘어선 책장들 사이로 제갈균의 외침이 파고들었지만 돌아오는 대답은 없었다.

“뭐야? 설마 안 계셔?”

“안에 계시긴 한 것 같은데요, 하, 미치겠네.”

제갈균이 이럴 줄 알았다는 듯 한숨을 푹 내쉬며 말을 이었다.

“뭔가에 한번 빠져들면 자주 이러십니다. 죄송하지만 잠시만 기다리고 계시면 제가 가주님을 찾아서…….”

서고를 둘러보던 적천강이 제갈균의 말을 끊었다.

“됐다. 그렇게까지 할 필요가 있겠느냐?”

“예? 아무리 그래도 적 대협께서 오셨는데…….”

“때가 되면 알아서 나오겠지. 각자 사정이 있는 법이니까.”

나는 순간 귀를 의심했다. 다른 사람도 아니고 적천강의 입에서 저런 말이 나올 줄이야.

심지어는 청풍마저도 입으로 가져가던 당과를 툭 떨어트릴 정도다.

‘꿈인가?’

심각하게 고민하던 그때, 적천강이 훈훈하게 웃으며 말을 이었다.

“그나저나 노부 평생 이렇게 크고 웅장한 서고는 처음이구나. 잠시 구경을 해 봐도 되겠느냐?”

제갈균이 얼떨떨한 얼굴로 대답했다.

“물론입니다.”

“불태워도?”

“……예?”

“농담이다, 요 녀석아. 허허, 아무리 그래도 객으로 온 입장에서 닥치는 대로 태워 버려서야 쓰나.”

껄껄 소리 내어 웃은 적천강이 말을 이었다.

“실수로 책장을 무너트린다면 모를까.”

그리고 다음 순간, 적천강의 신형이 빛살처럼 위로 솟구쳤다.

동시에 만근 거력이 실린 일장이 가장 가까이에 있는 책장을 후려쳤다.

쾅!

말릴 새도 없이 벌어진 일이었다. 나는 입을 쩍 벌린 채 눈앞에 벌어지는 광경을 바라보았다.

오메, 시벌.

쿠구구구궁.

높이만 족히 삼 장에 달할 것 같은 책장이 기울어지고 있었다. 그리고 그런 것이 무려 수백 개.

일정 간격으로 빽빽하게 모여 있던 수많은 책장이 하나의 거대한 도미노로 변한 것은 그야말로 순식간이었다.

“어, 어어, 어어어어!”

쿠웅! 쿠구구구궁!

엄청난 굉음이 제갈균의 비명을 집어삼켰다.

책장이 모조리 무너지자 오랜 세월 쌓여 있던 먼지가 일시에 날아오르며 서고 안을 자욱하게 메웠다.

아니, 이걸 더 이상 서고라고 부를 수나 있을지 모르겠다. 책들의 무덤. 뭐 그런 이름으로 부르는 게 어울릴 정도였다.

어쩌면 한 사람의 무덤이 되었을지도 모르고.

“아버지이!!!”

적천강이 울부짖는 제갈균의 어깨를 두드렸다.

“이젠 네가 제갈세가의 새로운 가주다.”

“안 돼애!”

빡!

제갈균의 뒤통수를 후려갈긴 적천강이 어이없다는 표정으로 입을 열었다.

“농담도 모르는 녀석이로군. 저기 멀쩡히 살아 있는 네 녀석의 아비는 보이지 않는 게냐?”

적천강의 말은 사실이었다.

사방에 자욱한 먼지구름 사이로 두어 번 기침 소리가 들리더니, 호리호리한 체구의 인영 하나가 손을 휘저으며 걸어 나오고 있었다.

“이거 참, 콜록. 미리 마중 나가지 못해 죄송합니다. 근래 들어 유난히 신경 써야 할 일이 많은지라. 콜록.”

“알면 됐다. 버르장머리 없는 녀석 같으니.”

퉁명스럽게 대꾸한 적천강이 소매를 떨쳤다.

파앙!

압축된 공기가 터져 나가는 소리와 함께 먼지구름이 흩어지고, 마침내 한 사람의 모습이 완연히 드러나기 시작했다.

“허, 널 이렇게 보니 세월이 흐르긴 했구나. 노부를 기억하느냐?”

맑은 목소리가 대답했다.

“물론입니다. 그날은 제가 태어난 후 다섯 번째로 맞은 중추절(仲秋節)이었지요. 노선배께서는 오리구이 두 접시와 여아홍 다섯 단지를 드셨고, 자리가 파할 무렵에 팽 대협과 비무를 벌여 코피를 터트리셨습니다.”

“뭐? 그 자리에 벽력도왕 그놈도 있었나? 심지어 싸우기까지 했어?”

“예. 팽 대협께서 크게 웃으시며 탁자를 내리치시다가 노선배님의 무릎에 술을 쏟았지 뭡니까. 사소한 시비였습니다.”

“누구 하나 죽어도 이상하지 않을 대사건이었군.”

피식 웃은 적천강이 말을 이었다.

“상당한 세월이 흘렀지만, 네놈의 그 신통방통한 머리는 여전하구나. 알았으니 흰소리는 그만하고 이리 오거라. 네놈을 기다리는 객들이 있으니.”

“그렇지 않아도 인사를 나눌 생각이었습니다.”

먼지를 잔뜩 뒤집어썼음에도 감출 수 없는 청수한 인상의 중년인.

지금껏 만나 본 명문 대파의 장문인 중에서도 가장 젊은 그는, 유난히도 맑고 빛나는 눈동자로 우리를 바라보았다.

“귀한 객들을 모셔 놓고 인사가 늦었군. 제갈풍일세.”

호북성 제일의 명문가이자 정파의 구심점 중 하나인 제갈세가의 가주라고는 믿기 힘들 정도로 담백한 첫인사.

그리고 누군가 대답할 틈도 없이 곧장 이어진 제갈풍의 뒷말을 들은 순간, 나는 문득 왜 그의 별호가 와룡객(臥龍客)인지 알 것 같았다.

“시간은 금과 같은 것이라, 다른 이의 귀중한 금을 뺏을 생각은 없으니 이 자리에 있고자 하는 이들만 남아 주게. 아, 그리고 대화는 편하게 나누어야 한다는 것은 본인의 오랜 지론이니 혹시 모를 오해는 없길 바라고.”

무슨 소린가 했더니, 바닥에 쌓인 먼지도 아랑곳하지 않고 그 자리에 넙죽 모로 누운 제갈풍의 모습에 나는 실소를 흘렸다.

“뭐 그러시죠. 편하고 좋네.”

내가 말과 함께 비스듬히 턱을 괴고 눕자, 그의 눈가가 초승달처럼 휘었다.



* * *



사람들은 황당해하면서도 하나둘씩 자리에 앉아 제갈풍의 말에 귀를 기울였다.

무송은 호북성 장강수로채에 가야 한다며 자리를 뜨려고 했지만, 제갈풍의 한마디에 떼었던 발걸음을 멈출 수밖에 없었다.

“가겠다면 굳이 막지는 않겠지만, 지금부터 할 이야기는 자네와도 깊은 연관이 있다네. 선화아(船火兒) 무송.”

“……!”

무송이 머뭇거리다 남은 데 비해, 정작 가장 먼저 떠날 것 같던 문경은 의외로 얌전히 자리를 지켰다.

하긴, 지금처럼 모두가 남아 있는 상황에서 혼자 떠났다면 더 눈에 띌지도 모르는 일이다.

이미 제갈세가만의 정보망을 통해 이 소년 의생의 정체를 신의의 제자라고 알고 있던 제갈풍도 묘한 눈빛으로 한 차례 바라봤을 뿐, 이내 문경에게서 시선을 떼고 입을 열었다.

“지금으로부터 정확히 달포 전이었네. 서고에서 사기(史記)를 여든다섯 번째로 읽고 있던 차에 그 소식을 들었지.”

구파일방과 오대세가는 각 성을 대표하는 맹주들.

적게는 백여 년에서 길게는 수백 년까지 뿌리를 내린 세력이다 보니, 각자 자신의 영역을 손바닥 들여다보듯 알 수 있는 촘촘한 정보망을 갖고 있었다.

그리고 그것은 제갈세가 역시 마찬가지였다.

“해사방(海蛇房)이 사라졌다는 소식이었네.”

“해사방? 그게 뭐예요, 은인?”

“나도 몰라.”

어리둥절한 청풍과 나와는 달리, 다른 사람들은 눈을 크게 떴다.

특히 무송의 반응은 이 자리의 누구보다 눈에 띄었다.

“해, 해사방이 말입니까?”

“자네가 알고 있는 바로 그 해사방이 맞네. 이 호북성에 존재하는 수많은 어부와 수부가 모여 만든 방회 조직 말일세.”

아하, 이제 알겠다.

해사방의 이름은 처음 듣지만 어떤 성격의 조직인지는 감을 잡았다.

구태의연한 설명 다 집어치우고 쉽게 말하자면 일종의 직업 조합이다.

각 지역에 헌터 협회가 있는 것처럼 호북성에는 해사방이라는 이름의 어업인 조합이 존재하는, 아니, 했었던 것이다.

그리고 이 소식은 적어도 무송에게 있어서만큼은 희소식이 틀림없었다. 입가에 슬쩍 떠오른 웃음이 바로 그 증거였다.

“제갈세가의 입장에서는 어떨지 모르지만, 본 맹에 뜻을 둔 저로서는 기쁜 소식이군요. 그간 해사방 때문에 스승님께서도 상당히 골치를 썩이셨으니 말입니다.”

“그럴 거라고 생각했네. 적어도 이곳 호북성에서만큼은 장강수로맹과 대적할 수 있는 유일한 조직이었으니.”

호북성 전역에는 장강의 지류가 거미줄처럼 연결되어 있다.

아무리 장강수로맹의 위세가 강하다고 해도 어업에 종사하는 이들의 숫자가 압도적이었을 것이다.

비록 자신이 맡은 사천의 일은 아니지만 강력한 경쟁 상대가 하나 사라졌다는 소식에, 무송은 껄껄 웃었다.

“그런데 어쩌다가 해산되었답니까? 혹시 소금을 밀수했다거나……?”

제갈풍이 고개를 저었다.

“그럴 리가. 만약 그랬다고 해도 해사방의 일 처리는 그리 허술하지 않고, 걸렸다면 이미 천자의 명을 받은 함대가 호북의 장강을 가득 메우고 있었겠지.”

“그럼, 내분입니까?”

“아무래도 자네는 내 말을 제대로 이해하지 못한 듯싶군.”

맑고 투명한 한 쌍의 눈동자가 무송을 응시한다.

혼란스러워하는 그를 향해, 제갈풍이 천천히 말을 이었다.

“해사방은 사라졌네. 누군가에 의해 철저히 짓밟혔단 말일세.”

“……!”

“내가 그 보고를 들은 전날 밤, 해사방주의 팔순을 축하하는 잔치가 열렸지. 방주에게 충성을 맹세한 마흔다섯 명의 선주와 일천을 헤아리는 해사방도가 참석하여 자정이 넘도록 술잔을 기울이고 적벽(赤壁)의 강물에 수십 척의 놀잇배를 띄웠어. 그리고 그것이 마지막이었네.”

다음 날, 새벽같이 일어난 늙은 뱃사공이 본 것은 적벽의 강물을 메운 수많은 시체와 참혹하게 부서진 배의 잔해들이었다.

해사방의 머리이자 몸통이라 할 수 있는 방주와, 수십 명의 선주를 비롯한 핵심 방도들이 모조리 적벽에 뼈를 묻은 것이다.

머리와 몸통 없이 움직일 수 있는 것은 아무것도 없다.

지난 수십 년간 호북성에서 장강수로맹과 어깨를 나란히 하며 위세를 떨치던 해사방은 그렇게 사라졌다.

“어, 어찌 그런 일이…….”

“희한한 일이군. 다른 누구도 아닌 자네가 그 사실을 모르고 있었다니.”

말을 잇지 못하는 무송을, 제갈풍이 물끄러미 바라보았다.

“적벽에서의 일이 알려지자 누가 가장 먼저 움직였는지 알고 있나? 관부? 운 좋게 살아남은 해사방도들? 아니야. 바로 장강수로맹일세. 그들은 실로 기민한 속도로 해사방의 영역을 침범하고 장강을 장악했어.”

“……제갈 대협.”

무송의 얼굴이 딱딱하게 굳었다.

나와 다른 사람들처럼, 그 역시 왜 이 자리에 자신이 남았어야 했는지 이제야 깨달은 듯 보였다.

“지금 혹시 저를, 본 맹을 의심하시는 겁니까?”

“당연히 아니었지. 내가 아는 동정채의 황 대협은 그렇게 우매한 사람이 아니니까. 다른 우매하고 난폭한 채주들과는 다른 인물이지.”

어깨에 쌓인 먼지를 턴 제갈풍이 무송을 향해 싱긋 웃으며 말을 이었다.

“분명히 그리 생각했네. 사흘 전, 장강수로맹을 공개적으로 지탄했던 동정어옹(洞庭漁翁)이 사라지기 전까지는.”

“……!”

사람들 사이로 동요가 퍼져 나간 그 순간, 익숙한 알림이 귓가를 파고들었다.

띠링.
```

## Final English reading copy

```markdown
# Chapter 445

Clack.

“Ah.”

Someone let out a small gasp.

The grandeur of the enormous library that unfolded before us when the doors opened was astonishing enough, but the doors themselves had opened without any human hand or movement of internal energy.

And as someone who had spent his entire modern life passing through automatic doors tens of thousands of times, I still found it a remarkably fresh experience.

*Some kind of machine?*

No, this was Murim. Should I call it a mechanism?

The doors that had just opened contained components made of iron and wood, all intricately interwoven into an elaborate structure.

And that wasn’t all. As I slowly turned my head and looked around the library, I saw unmistakable traces of mechanisms like the one installed in the doors everywhere.

Of course, compared to the cutting edge of modern civilization, they were crude. But there was no question that this was a sight I had never encountered in any of the other prestigious great families and sects I had visited.

*That aside…*

Why is nobody here?

There wasn’t even a servant or guard in sight, let alone the Family Head himself.

Zhuge Gyun shouted loudly while everyone, myself included, stared around.

“Family Head!”

His shout, infused with internal energy, echoed through the library.

The space was not merely large. Vast was the more appropriate word. It was larger than a modern soccer stadium.

Zhuge Gyun’s voice burrowed between the endless rows of bookshelves, but no answer came back.

“What the hell? Is he not here?”

“He seems to be inside, but… Ah, this is driving me crazy.”

As if he had known this would happen, Zhuge Gyun let out a deep sigh and continued.

“He often gets like this when he becomes absorbed in something. I’m sorry, but if you could wait here for a moment, I’ll find the Family Head and—”

Jeok Cheongang, who had been looking around the library, interrupted him.

“Enough. Is that really necessary?”

“Pardon? Even so, with Great Hero Jeok visiting…”

“He’ll come out when the time is right. Everyone has their own circumstances.”

For a moment, I wondered if I had heard him correctly. Of all people, I never expected those words to come from Jeok Cheongang.

Cheongpung even dropped the candied fruit he had been bringing to his mouth.

*Am I dreaming?*

I was still seriously considering the question when Jeok Cheongang continued with a warm smile.

“Come to think of it, this old man has never seen a library so large and magnificent in his entire life. Would it be all right if I looked around for a while?”

Zhuge Gyun answered with a dazed expression.

“Of course.”

“Even if I burn it down?”

“…Pardon?”

“It was a joke, you little punk. Ho-ho. Even so, how could I burn everything down indiscriminately when I’m here as a guest?”

Jeok Cheongang laughed heartily before continuing.

“Unless I accidentally knock over a bookshelf.”

And in the next moment, Jeok Cheongang’s body shot upward like a streak of light.

At the same time, his palm strike, carrying the tremendous force of ten thousand geun, slammed into the nearest bookshelf.

Boom!

It happened before anyone had time to stop him. I stared at the scene unfolding before me with my mouth hanging open.

*Oh, fuck.*

Rumble…

The bookshelf, which looked to be at least three zhang tall, began to tilt.

And there were hundreds of them.

The countless bookshelves packed together at regular intervals transformed into one enormous domino in the blink of an eye.

“W-wait, wait, wait, wait!”

Crash! Rumble-rumble-rumble!

An earth-shaking roar swallowed Zhuge Gyun’s scream.

As every bookshelf collapsed, dust that had accumulated over many years burst into the air all at once and filled the library in a dense cloud.

No, I wasn’t even sure it could still be called a library. A graveyard of books. Something like that would have been more appropriate.

It might even have become one person’s grave.

“Fatherrrr!”

Jeok Cheongang patted Zhuge Gyun on the shoulder as he wailed.

“You’re the new Family Head of the Zhuge Clan now.”

“Nooo!”

Whack!

After smacking Zhuge Gyun on the back of the head, Jeok Cheongang opened his mouth with an incredulous expression.

“You really don’t understand jokes, do you? Can’t you see your father over there, alive and well?”

Jeok Cheongang was telling the truth.

After a couple of coughs came from within the thick cloud of dust, a slender figure emerged, waving one hand as he walked forward.

“Well, now. Cough. I’m sorry I couldn’t come out to greet you in advance. There have been an unusual number of matters requiring my attention lately. Cough.”

“At least you know. What an ill-mannered brat.”

Jeok Cheongang answered curtly and flicked his sleeve.

Whoosh!

With the sound of compressed air bursting outward, the dust cloud scattered. At last, the figure of a man became fully visible.

“Ha. Seeing you like this, I realize how much time has passed. Do you remember this old man?”

A clear voice answered.

“Of course. That day was the fifth Mid-Autumn Festival I celebrated after being born. Senior ate two plates of roast duck and five jars of Yeoahong, then fought a duel with Great Hero Peng as the gathering was ending and ended up with a bloody nose.”

“What? That Thunderbolt Saber King bastard was there too? We even fought?”

“Yes. Great Hero Peng laughed loudly and struck the table, spilling wine onto Senior’s knee. It was a minor disagreement.”

“A major incident in which it wouldn’t have been strange for someone to die.”

Jeok Cheongang let out a quiet laugh before continuing.

“Quite a few years have passed, but that incredible head of yours is still as sharp as ever. All right, enough nonsense. Come here. You have guests waiting for you.”

“I was planning to greet them regardless.”

The middle-aged man had been covered in dust, but it couldn’t conceal his refined appearance.

He was the youngest Sect Leader of any prestigious great family or sect I had met so far. His eyes, unusually clear and radiant, turned toward us.

“I apologize for keeping such honored guests waiting. I am Zhuge Feng.”

It was a remarkably plain greeting for the Family Head of the Zhuge Clan, the foremost great family in Hubei Province and one of the central pillars of the orthodox faction.

And the moment I heard what Zhuge Feng said next, before anyone had a chance to respond, I suddenly understood why his sobriquet was Crouching Dragon Guest.

“Time is as valuable as gold, and I have no intention of taking anyone else’s precious gold. Those who wish to remain here may do so. Oh, and it has long been my personal belief that conversations should be held comfortably, so please do not misunderstand.”

I wondered what he meant until I saw Zhuge Feng lie down flat on his side right there, paying no attention to the dust piled across the floor. I let out a quiet laugh.

“Sure, why not? This is comfortable.”

As I spoke, I lay down at an angle and propped my chin on one hand. The corners of his eyes curved like crescent moons.

* * *

Although they were dumbfounded, everyone gradually sat down and listened to Zhuge Feng.

Mu Song tried to leave, saying that he had to go to a Yangtze River Channel League stronghold in Hubei, but he had no choice but to stop after Zhuge Feng said one thing.

“I won’t stop you if you wish to leave, but what I am about to say is deeply connected to you as well, Ship-Fire Boy Mu Song.”

“……!”

Mu Song hesitated before remaining behind. Mungyeong, who had seemed the most likely to leave first, unexpectedly stayed quietly in his place.

Then again, in a situation where everyone else was staying, perhaps leaving alone would have drawn even more attention.

Through the Zhuge Clan’s own intelligence network, Zhuge Feng already knew that this young medical apprentice was the Disciple of the Divine Physician. He looked at Mungyeong once with a strange expression, then turned his gaze away and opened his mouth.

“It was exactly one month ago. I was in the library, reading the *Records of the Grand Historian* for the eighty-fifth time, when I heard the news.”

The Nine Sects and One Gang and the Five Great Families were the leading powers representing each province.

Since their roots stretched back anywhere from a hundred years to several centuries, each possessed a dense intelligence network that let them know their territory as well as the palm of their hand.

The Zhuge Clan was no exception.

“The news was that the Sea Serpent Society had disappeared.”

“The Sea Serpent Society? What’s that, Benefactor?”

“I don’t know either.”

Unlike the bewildered Cheongpung and me, everyone else opened their eyes wide.

Mu Song’s reaction in particular stood out more than anyone else’s.

“Th-the Sea Serpent Society?”

“Yes, the very one you know. The association formed by the countless fishermen and boatmen living in Hubei Province.”

Ah. Now I understood.

I had never heard of the Sea Serpent Society, but I could guess what kind of organization it was.

To put it simply and dispense with all the old-fashioned explanations, it was a sort of professional association.

Just as each region had a Hunter Association, Hubei Province had—or rather, used to have—an association of fishermen called the Sea Serpent Society.

And this news was unquestionably good news, at least for Mu Song. The faint smile that appeared at the corners of his mouth was proof enough.

“I cannot say what the Zhuge Clan’s position on this is, but as someone devoted to the League, I find it welcome news. The Sea Serpent Society caused my Master no end of trouble.”

“I thought you would feel that way. At least in Hubei Province, it was the only organization capable of standing against the Yangtze River Channel League.”

Tributaries of the Yangtze ran throughout Hubei Province like a spiderweb.

No matter how powerful the Yangtze River Channel League was, the number of people engaged in fishing must have been overwhelming.

Although the matter did not concern Sichuan, which was under his responsibility, Mu Song laughed heartily at the news that one powerful rival had disappeared.

“But how did they end up disbanding? Did they happen to smuggle salt or something…?”

Zhuge Feng shook his head.

“Of course not. Even if they had, the Sea Serpent Society would not have handled the matter so carelessly. If they had been caught, the fleet acting under the Son of Heaven’s command would already have filled the Yangtze in Hubei.”

“Then was it an internal conflict?”

“I get the feeling you have not properly understood what I said.”

A pair of clear, transparent eyes fixed on Mu Song.

As he faced Mu Song’s confusion, Zhuge Feng continued slowly.

“The Sea Serpent Society disappeared. I mean that someone thoroughly crushed it.”

“……!”

“The night before I received that report, a banquet was held to celebrate the Society Head’s eightieth birthday. Forty-five shipowners who had sworn loyalty to him and roughly a thousand members of the Sea Serpent Society attended. They drank until past midnight and launched dozens of pleasure boats onto the waters of Red Cliffs. And that was the last of it.”

The next morning, an old boatman who rose at dawn saw countless corpses filling the waters of Red Cliffs and the wreckage of brutally shattered boats.

The Society Head—the head and body of the Sea Serpent Society—along with dozens of ship owners and the organization’s core members had all met their deaths at Red Cliffs.

Nothing can move without a head and a body.

The Sea Serpent Society, which had wielded power in Hubei Province alongside the Yangtze River Channel League for decades, disappeared just like that.

“H-how could such a thing happen…?”

“It is strange that you, of all people, did not know about it.”

Zhuge Feng stared silently at Mu Song, who could not continue.

“Do you know who moved first after the incident at Red Cliffs became known? The authorities? The Sea Serpent Society members who were lucky enough to survive? No. It was the Yangtze River Channel League. They invaded the Sea Serpent Society’s territory and took control of the Yangtze with astonishing speed.”

“……Great Hero Zhuge.”

Mu Song’s face hardened.

Like the rest of us, he seemed to have finally realized why he had needed to remain there.

“Are you saying you suspect me? The League?”

“Of course I didn’t. The Great Hero Hwang of Donghu Stronghold whom I know is not such a foolish man. He is different from the other foolish and violent Stronghold Lords.”

Zhuge Feng brushed the dust from his shoulder and smiled faintly at Mu Song.

“That was certainly what I thought. Until the Dongting Fisherman, who had publicly condemned the Yangtze River Channel League, disappeared three days ago.”

“……!”

At that moment, unrest spread through the group, and a familiar notification rang in my ears.

Ding.
```
