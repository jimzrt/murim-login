<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0497.txt",
      "sha256": "540fd97c5652fa139beb27193ccfe52c728fb77ea92f22858474be9edf53b056",
      "bytes": 13660
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "204c57bef01b63bc6ed461f8f24d538c83b5a020017da312166e6f85ce612549",
      "bytes": 4932
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "928ab7d78b7b2bcd85a408c620e747bd8a22807f27d9e0a10cc44bf9a7a38b3d",
      "bytes": 158048
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "b9acd8c30a0f2e1c03aab859d23d3d6aedc75fb13ae033f4f4024e292037e350",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "19b7db8350dca071981b80b41d4f44718de82ad88459979f9177b54729722954",
      "bytes": 1777
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "1747272bfeeaf257b19238381dab4314fb2cb290efb92ddcec1d790d8c164882",
      "bytes": 622
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "2d776c1509e191b02e00da155c87b755af0bd12ab967518a2714d066c65aebb8",
      "bytes": 885
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fcd89ef22d5cd9bc5646cb7dfc2a01c58c5dc8bb04ac6b55736f44af7216f5ad",
      "bytes": 153645
    }
  ],
  "estimated_tokens": 10794
}
-->

# Durable State Update — Chapter 497

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 497. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 497. Profile updates may replace only one
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
  "chapter": 497,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 497,
    "continuity_sources": [497],
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
    "The Zhuge Clan has sealed the exposed Gate gap with a formation, but whether this is a fundamental or permanent solution remains unresolved; the Gate's residual mana previously mutated local life.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, were captured in the Gate's entrance waterways; the remaining population is unknown, and the fish kill one another.",
    "Taekyung suspects Dark Heaven's regeneration, teleportation, and Moving Formation are manifestations of Magic connected to the Gate.",
    "Taekyung told Jeok that he came from another world, that an evil force from it is linked to Dark Heaven, that the corrupted imugi was their work, and that a fully opened Gate could release monsters.",
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people; the severely injured Dongting Fisherman may be connected to Dark Heaven and the earlier destruction inside the secret refuge.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Wikyung and Gung Gibang pledged the Jin Family of Taiyuan and the Beggars' Sect to Taekyung's defense.",
    "Jeok's innate qi is damaged and steadily diminishing despite the Thousand-Year Snow Ginseng and the Divine Physician's treatment; Taekyung remains uncertain whether Jeok recovered without lasting aftereffects.",
    "Mungyeong is the Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; before becoming the Slaughter Saint, he was called Killing Ghost, and he saved countless people as the Divine Physician.",
    "Mungyeong recognizes Taekyung's Heavenly Martial Physique as innate and distinct from Cheongpung's more refined physique.",
    "Mungyeong is testing Taekyung through successive poisoned traps and concealed attacks, intending to teach secret martial arts without a formal Master-Disciple relationship and to correct Taekyung's complacency.",
    "Taekyung detoxified Potent Seven-Step Soul-Chasing Powder, but Sinews and Meridians damage permanently reduced Strength and Agility by 5 each; he has stored the Water God Dragon's dismantled materials and Origin Essence in his inventory."
  ],
  "continuity_sources": [
    496,
    495
  ],
  "open_questions": [
    "Will Zhuge Feng's formation permanently seal the Gate gap, and what lies beyond it if the Gate is reopened?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "Has Jeok fully recovered from the Formless Ultimate Poison, and will Taekyung use the Water God Dragon's Origin Essence to aid him?"
  ],
  "safe_through": 496,
  "temporary_decisions": [
    "Render 산공독 as Energy-Dispersing Poison, 강력한 산공독 as Potent Energy-Dispersing Poison, 칠보추혼산 as Seven-Step Soul-Chasing Powder, 강력한 칠보추혼산 as Potent Seven-Step Soul-Chasing Powder, 심각한 복통 as Severe Stomachache, 고기 방패 as Meat Shield, 독 장아찌 as Poisoned Pickle, and 독의 as Poison Physician; retain secret martial arts, Master-Disciple relationship, Killing Ghost, and Fake Murim Martial Artist, and preserve 악 as Agh in the Quest interface.",
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 혈어 as Blood Fish, and 변이된 송사리 as Mutated Minnow; render 강력한 마비산 as Potent Paralysis Powder, 강력한 미혼산 as Potent Soul-Bewitching Powder, 전신 마비 as Full-Body Paralysis, 독성 흡수 as Poison Absorption, and 해독 as Detoxification.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter; render 해시 as hour of the Pig, 한 식경 as half an hour, 타구봉 as Dog-Beating Staff, 창룡 as Azure Dragon, and 무량수불 as Infinite Life Buddha; preserve geun as the traditional weight unit with a footnote.",
    "Render 선천지기 as innate qi, 진원진기 as true-origin qi, and 천기 as heavenly patterns.",
    "Render 심마 as Heart Demon, 비급 as martial arts manual, 송문고검 as Pine-Pattern Ancient Sword, 반로환동 as Returned to Youth, 강강수월래 as Ganggangsullae, 생사부 as Book of Life and Death, 기막 as qi curtain, 무극태을검 as Martial Extremity Grand Unity Sword, 이룡 as Two Dragons, 원정 as Origin Essence, 내단 as inner core, 영험한 기운 as sacred energy, 대호 as great tiger, and 취팔선권 as Drunken Eight Immortals Fist."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 무당파    | **Wudang**                       |
| 제갈세가   | **Zhuge Clan**                   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 문주     | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 습득               | **Acquired**                   |
| 사천     | **Sichuan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 점혈 | **Pressure-Point Strike** | System-named technique used by Jeok Cheongang on Taekyung. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 사혈 | **lethal acupoint** | An acupoint whose strike can kill. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 496
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 496
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, and can command coordinated raids against powerful monsters.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 496
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 496
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history who passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance who asked him to look after and instruct Jin Taekyung, and Mungyeong is currently testing Taekyung before teaching him secret martial arts without a formal Master-Disciple relationship.

## Korean source

```text
＃497화



한 식경(食頃).

그것이 내가 버틸 수 있는 최대한의 시간이었다. 목덜미로부터 느껴지는 검날의 서늘한 감촉에, 나는 작게 중얼거렸다.

“거지 같네, 진짜.”

스윽.

따끔한 통증과 함께 핏물이 목덜미를 타고 미끄러진다. 의도가 뻔히 보이는 행동에 절로 한숨이 흘러나온다.

“졌습니다. 그만하시죠.”

“틀렸다. 다시.”

싸우는 도중에는 들을 수 없었던 건조한 목소리. 그리고 나는 목소리의 주인이 원하는 대답을 이미 알고 있었다.

“……죽었습니다. 됐어요?”

천천히 목덜미를 파고들던 검날이 우뚝 멈춘다. 이내 차가운 날붙이의 감촉이 사라지는 것을 느낀 나는 목을 짚어 지혈한 뒤 돌아섰다.

어느새 삼 장 밖의 바위에 앉아 있는 한 사람이 보였다.

“네가 몇 번째 죽었는지는 알고 있나?”

“열두 번이요.”

사지 근맥이 잘려 죽은 경우가 다섯 번, 사혈(死穴)을 점혈 당하여 죽은 것이 세 번. 심장이 관통당한 것 역시 세 번. 그리고 조금 전에는 목이 베였다.

실제로 죽진 않았지만, 죽은 거나 마찬가지다. 옷소매로 목에 묻은 끈적한 핏물을 닦아 낸 나는 문경을 바라보았다.

“다음번에는 다를 겁니다.”

“열한 번째 듣는 말이로군.”

“이번엔 확실해요.”

“그건 열두 번째고.”

“…….”

기억력 보소. 할 말을 잃어버린 나를 향해 문경이 물었다.

“네놈이 왜 죽었는지 알고 있나?”

싸움은 언제나 결과를 남기고, 결과는 항상 생각을 낳는다.

말없이 머릿속으로 문경과의 싸움을 떠올리던 내가 불쑥 입을 열었다.

“살수처럼 싸워서?”

“역시 아무것도 모르는…… 흠.”

나와 거의 동시에 말문을 열었던 문경이 말꼬리를 흐렸다.

“틀렸습니까?”

“계속해 봐라.”

“정확히 언제부터인지는 모르겠는데, 따라 하게 되더라고요. 보여 주시는 움직임이나 그런 것들을.”

처음에는 독 장아찌가 될 정도로 당하고 나니 주위의 모든 것에 주의하게 됐고, 그 후부터는 문경의 움직임을 조금씩 베끼기 시작했다.

그렇게 하루에 두세 번씩 비무를 치르다 보니 점점 눈과 몸에 익어 갔다.

하지만…….

“그게 패착이었어요.”

“어째서지?”

“원래 새 신발을 신으면 발뒤꿈치가 까지는 법이죠. 그 신발이 발 크기보다 작으면 두말할 것도 없고.”

“더 자세히.”

“되지도 않는 어설픈 흉내는 집어치우고, 제 방식대로 싸웠어야 했습니다. 상대가 살성일 경우에는 더더욱.”

“…….”

한동안 말없이 나를 물끄러미 응시하던 문경이 한마디를 툭 내뱉었다.

“아주 천치는 아니로군.”

“오, 방금 그거 설마 칭찬하신 겁니까?”

“이제 겨우 기본이라는 뜻이다.”

“그러니까요. 칭찬 감사합니다.”

문경이 미간을 찡그렸다.

“네놈은 귓구멍이 막혔느냐?”

“아뇨. 뚫렸는데요?”

“……사람을 열 받게 하는 재주가 있군.”

“결국 기본이 됐다는 거니까 칭찬 맞지 않습니까. 왜 이렇게 솔직하지 못하세요? 혹시 사춘기십니까?”

“아니라니까!”

“아니, 왜 갑자기 소리를 그렇게.”

“내가 언제! 아니라고!”

“……생각해 보니 그런 것도 같네요.”

아니긴 뭐가 아니야.

하지만 말대꾸 한 번만 더 했다가는 목이 날아갈 기세다.

버럭 소리를 지른 문경은 언제 그랬냐는 듯 평온하면서도 건조한 어조로 돌아왔다.

“기본은 말 그대로 기본일 뿐이다. 지금까지 그런 놈들은 네 녀석 말고도 여럿 있었지.”

그런 놈들?

나는 설마 하는 마음으로 입을 열었다.

“혹시 다른 제자가 있습니까?”

“당연히 있지. 사천에서 만나지 않았더냐.”

“동 노인 말고요. 무슨 뜻인지 뻔히 아시면서 다른 소리 하시네.”

“…….”

침묵은 곧 긍정. 숨겨진 살성의 제자가 있다고 생각하자 호기심이 고개를 치켜들었다.

“누구, 누굽니까? 지금도 계속 연락 주고받고 그래요? 스승의 날에 다 같이 밥도 같이 먹고?”

“내가 대답해 줄 이유는 없지. 그리고 스승의 날이라니, 무슨 개소리냐?”

“까탈스럽게 구시긴.”

“……날이 갈수록 언행이 방자해지는군. 목숨이 다섯 개쯤 되나?”

“지금까지 열두 번 죽고 되살아난 것으로 봐서는 열세 개 정도는 되는 것 같은데요. 그래서 진짜 안 알려 주실 겁니까?”

나를 뚫어져라 노려보던 문경이 불쑥 입을 열었다.

“알려 주지. 단, 조건이 있다.”

살성의 제시하는 조건이라. 나는 자신감 넘치는 태도로 입을 열었다.

“슬슬 밥 먹을 시간이네요. 이만 가 보겠습니다.”

“분명 먹고 온 것으로 기억하는데.”

“제가 하루에 다섯 끼는 먹어서요.”

“그래도 듣고 가지. 상당히 궁금해하는 것 같던데.”

“각자 인생이 있고 감추고 싶은 비밀이 있는 법인데, 그걸 뭐 하러 캐묻겠습니까. 그럼 전 이만.”

“딱 서라. 목 날아가기 싫으면.”

“…….”

시벌, 괜히 물어봤다.

나는 똥줄이 타들어 가는 것을 느끼며 반쯤 돌린 신형을 원위치했다.

그래, 기왕 이렇게 된 거 이야기나 듣자.

“그래서, 정말 또 다른 제자들이 있는 겁니까?”

“제자는 아니지만, 가르침을 내린 놈들이라면 여럿 있었다.”

“이제는 없다는 뜻으로 들리네요.”

“실로 오랜 세월이 흘렀으니까. 지금까지 살아남았을 리 없지.”

“혹시 그분들께서 몸담으셨던 분야가……?”

“살수였다. 나와 함께 살천문(殺天門)에 속해 있었던.”

살천문이라. 듣기만 해도 피비린내 솔솔 나는 이름이다.

‘이 인간, 사문도 있었구나.’

생각해 보면 당연한 일이었다. 제아무리 문경이라 할지라도 처음부터 살수로 태어나지는 않았을 테니까.

‘그래도 살성이 소속된 문파였다면 상당히 알려진 이름일 텐데.’

지금까지의 기억을 샅샅이 뒤져 봐도, 살천문이라는 세 글자는 생소하다.

바로 그때, 내 의문을 알아차린 것처럼 문경이 입술을 뗐다.

“소용없다. 이미 오래전 사라진 곳이니.”

문파가 사라진다면 그건 한 가지 경우뿐이다.

나는 문경의 눈치를 살피며 조심스럽게 한 단어를 입에 올렸다.

“멸문(滅門)?”

“그래.”

“도대체 어쩌다가? 아니, 그전에 본인이 문주 아니셨어요?”

“잘못된 길을 택했고, 그에 대한 대가를 치렀지. 해 줄 말은 그뿐이다.”

말을 끝마친 문경이 몸을 일으켰다. 그의 손에는 어느새 소검이 시퍼런 예기를 뿜어내고 있었다.

“자. 이제 값을 치를 시간이로군.”

“예?”

“내 일검(一劍)을 피해 보아라. 그게 조건이다.”

보통은 도대체 그걸 어떻게 피해, 라고 생각하겠지만 내 입장에서는 충분히 해 볼 만하다.

천하의 살성을 상대로, 그것도 어설픈 살수 흉내를 내면서 한 식경을 버텼는데 일검쯤이야.

“이거 피하면, 나중에 또 이야기 들려주실 겁니까?”

“물론.”

“좋습니다, 까짓거.”

문경이 한마디를 덧붙였다.

“단, 눈을 감아라.”

“시발 거. 장난하십니까?”

“그렇다면 죽겠군. 열세 번째가 아니라 처음이자 마지막으로.”

말이 끝나기도 전에 문경의 소매가 펄럭였다.

지금까지의 경험으로 익숙해진 나는 본능적으로 고개를 틀었지만, 날아온 것은 암기가 아닌 또 다른 무언가였다.

‘저건.’

안력(眼力)을 극도로 끌어올려야 볼 수 있을 만큼 미세한 크기의 가루들.

때마침 내 쪽을 향해 불어오던 바람에 실려 날아온 가루가 공기에 닿는 바로 그 순간.

화악!

어둠이 세상을 집어삼켰다.

아니, 아니다. 어둠이 집어삼킨 것은 세상이 아닌 바로 나였다.

삐빅.



- [실명산]에 중독되셨습니다!

- 일시적으로 시력을 상실합니다!

- 빠른 해독이 필요합니다! 해독이 오래 지체되면 영구적인 손상이 일어날 수 있습니다!



귓가를 파고드는 시스템 알림과 함께 전신의 털이 곤두섰다.

실명산? 독 따위는 상관없다. 아직 만독지환을 착용한 상태니까.

문제는 만독지환이 실명산을 해독하는 속도보다, 아무것도 보이지 않는 어둠 너머에서 다가오는 문경의 일검이 훨씬 더 빠르다는 것이다.

스으윽.

아무것도 보이지 않는다. 그러나 분명하게 느낄 수 있었다.

마치 누군가 정지 버튼을 누른 것처럼 느리게 흐르는 세상 속에서, 바람을 지우며 다가오는 살검(殺劍)을.

‘이건.’

고금제일의 살수가 펼친 한 수.

지금까지 느껴 본 적 없는, 몸서리칠 만큼 은밀하고 소름 끼치는 살기가 느껴진다.

나는 온통 암흑으로 가득한 세상을 멍하니 바라보았다.

그리고 아무것도 보이지 않는 그 숨 막히는 공간 속에서, 내 안의 모든 감각이 깨어남을 느꼈다.

서걱!



* * *



무당파, 제갈세가. 그리고 개방.

기밀을 위해 믿을 만한 정예들만을 선별했다고는 하나, 그들의 면면과 숫자는 누구도 무시할 수 없을 정도였다.

그리고 기백 명이 넘는 명문 대파의 무림인들 사이에서 소년 의생의 모습은 어디에서나 눈에 띌 수밖에 없었다.

“오, 너로구나. 지금 나오는 길이냐?”

“진 공자님을 뵙고 오는 길입니다.”

“근래 들어 더욱 자주 들르는 것 같은데?”

“예. 요즘 수련을 워낙 거칠게 하시는 통에, 자꾸 다치셔서요.”

“허어. 그렇구나. 진 대협도 참 대단하시지. 나이도 따지면 내 아들놈보다도 어린데, 지금의 경지에 만족하지 않고 끊임없이 노력하시는 모습이…….”

“대단한 고수이신가 봐요. 저야 무림에 관한 일은 영 문외한이라.”

소년 의생, 문경의 순진무구한 한마디에 경계를 서고 있던 제갈세가의 무인이 피식 웃었다.

아무리 심심했기로서니 배운 것이라고는 의술밖에 없는 어린아이를 붙잡고 귀찮게 했다는 생각에서였다.

“대단하시지. 그렇고말고. 너도 언젠가 알게 될 게다.”

“으음. 그런가요?”

“무림에 연관이 없다면 잘 모를 수도 있단다. 어쨌건 이제 오늘 수련은 마무리된 게냐?”

아무것도 모르는 양, 고개를 갸우뚱거리던 문경이 대답했다.

“아뇨. 앞으로 두 시진 동안은 아무도 접근하지 말라고 하셨어요.”

“알겠다. 다른 사람도 아니고 진 대협의 수련을 방해할 수는 없지. 다음 근무자들에게도 전달하도록 하마.”

“네. 그럼 고생하세요.”

예의 바르게 허리를 꾸벅 숙인 문경이 떠나려던 그때, 무인이 불쑥 입을 열었다.

“저런, 수련이 생각보다 거친 모양이로구나.”

“예?”

“네 소매에 묻은 피 말이다. 진 대협께서 많이 다치셨느냐?”

뒤에 덧붙인 무인의 질문은 미처 한 사람의 귓가에 닿지 못했다.

말없이 혈흔이 묻은 자신의 소매를 바라보던 문경이 중얼거렸다.

“기본……인가.”

“응?”

“아, 별일 아닙니다. 진 공자님께서는 무탈하시니 걱정마세요.”

“어어. 그래. 알겠다.”

문경은 찜찜한 표정으로 대답하는 무인을 뒤로하고 자리를 벗어났다.

제법 익숙해진 얼굴들이 말을 걸고 알은체를 해 왔으나, 소년 의생의 머릿속에는 한 사람에 관한 생각뿐이었다.

‘진태경. 진태경이라…….’

설마 했다. 그런데 그 녀석이 정말 마지막 일검을 피해 낼 줄은.

지난 며칠간의 시험과 오늘을 통해 얻은 결과는 기대 이상이었다. 아니, 상상 이상이었다.

‘이런 일도 있을 수 있군.’

문경이 진태경에게 했던 말은 전부 사실이었다.

한때 그에게는 분명 제자라고 부를 만한 이들이 있었고, 그들은 모두 ‘기본’을 갖춘 자들이었다.

그러나 조금 전 그 자리에서 말하지 않은 진실이 있다면, 바로 습득 기간이었다.

‘가장 빨리 통과한 놈이 일 년 남짓이었지, 아마.’

하지만 진태경은 해냈다. 그것도 불과 칠 주야 만에.

타의 추종을 불허하는 속도다.

그 이유가 천무지체여서, 초절정 고수라서인지는 몰라도 진태경이라는 놈은 그 자체만으로도 특별한 구석이 있었다.

“아무리 그래도…… 이 정도일 거라고는 생각 못 했는데.”

아무도 듣지 못할 만큼 작은 목소리로 중얼거린 문경은 소매를 걷어 올렸다.

예리한 무언가에 의해 베인 살갗과 그 위로 맺힌 핏방울이 눈에 들어오자, 문득 어떤 생각이 뇌리를 스쳤다.

‘이제야 알겠군. 화왕의 마음을.’

하지만 문경은 알지 못했다. 어느새 그의 입가에 희미한 미소가 맺혀 있다는 사실을.
```

## Final English reading copy

```markdown
# Chapter 497

Half an hour.

That was the longest I could hold out. Feeling the cold edge of a sword against the back of my neck, I muttered under my breath.

“God, this sucks.”

Ssshhk.

A sharp pain stabbed me, and blood slid down the back of my neck. The intent behind the action was so obvious that I couldn’t help sighing.

“I lost. Let’s stop now.”

“Wrong. Again.”

It was a dry voice I hadn’t been able to hear during the fight. And I already knew what its owner wanted me to say.

“…I’m dead. Is that enough?”

The blade slowly digging into my neck came to a sudden stop. When the cold metal vanished, I pressed a hand to the wound to staunch the bleeding, then turned around.

A man was sitting on a rock about thirty feet away.

“Do you know how many times you’ve died?”

“Twelve.”

Five times, my Sinews and Meridians had been severed in all four limbs. Three times, I had died from a Pressure-Point Strike to a lethal acupoint. Three more times, my heart had been pierced. And just now, my throat had been cut.

I hadn’t actually died, but it was practically the same thing. Wiping the sticky blood from my neck with my sleeve, I looked at Mungyeong.

“It’ll be different next time.”

“That is what I’ve heard eleven times already.”

“I mean it this time.”

“That makes twelve.”

“……”

What a memory.

As I stood there speechless, Mungyeong asked me a question.

“Do you know why you died?”

A fight always left behind a result, and results always led to thought.

I silently replayed my fight with Mungyeong in my head before blurting out an answer.

“Because I fought like an assassin?”

“As expected, you know nothing… Hmm.”

Mungyeong had begun speaking almost at the same time as me, then let his voice trail off.

“Was I wrong?”

“Continue.”

“I don’t know exactly when it started, but I found myself imitating you. The movements you showed me and things like that.”

At first, after being beaten so badly I was practically a Poisoned Pickle, I began paying attention to everything around me. After that, I started copying Mungyeong’s movements bit by bit.

As I dueled him two or three times a day, those movements gradually became familiar to my eyes and body.

But…

“That was my mistake.”

“Why?”

“When you wear new shoes, they rub your heels raw. If the shoes are smaller than your feet, even more so.”

“Be more specific.”

“I should have stopped trying to imitate you so clumsily and fought in my own way. Especially against a Slaughter Saint.”

“……”

Mungyeong stared at me in silence for a while before tossing out a single remark.

“You’re not a complete idiot.”

“Oh, was that a compliment?”

“It means you’ve only just reached the basics.”

“Exactly. Thank you for the compliment.”

Mungyeong’s brow furrowed.

“Are your ears plugged?”

“No. They’re perfectly open.”

“……”

“You have a real talent for getting on people’s nerves.”

“Either way, reaching the basics means it was a compliment. Why are you so bad at being honest? Are you going through puberty?”

“I told you I’m not!”

“Why are you suddenly shouting?”

“When did I shout? I’m not!”

“…Now that I think about it, maybe you are.”

*Yeah, right.*

But if I talked back one more time, it looked like my head might really fly off.

Mungyeong had shouted in anger, but he soon returned to his usual calm, dry tone as though nothing had happened.

“The basics are merely the basics. There have been many others like you before.”

*Others like me?*

I cautiously opened my mouth.

“Do you have other Disciples?”

“Of course. Did you not meet one in Sichuan?”

“Other than Old Man Dong. You know exactly what I mean, so why are you changing the subject?”

“……”

Silence was as good as an admission.

The thought that the Slaughter Saint had hidden Disciples made my curiosity rear its head.

“Who? Who are they? Do you still keep in touch? Do you all go out to eat together on Teacher’s Day[^1]?”

“I have no reason to answer you. And what nonsense is Teacher’s Day?”

“You’re awfully difficult.”

“……”

“Your words and conduct grow more insolent by the day. Do you have five lives or something?”

“Judging by the fact that I’ve died and come back twelve times, I’d say I have about thirteen. So are you really not going to tell me?”

Mungyeong stared at me before speaking abruptly.

“I’ll tell you. But there is a condition.”

A condition from the Slaughter Saint.

I put on a confident expression and opened my mouth.

“It’s about time to eat. I’ll be going now.”

“I distinctly remember that you already ate.”

“I eat five times a day.”

“Stay and listen anyway. You seem quite curious.”

“Everyone has their own life and secrets they want to keep hidden. Why would I pry into them? Anyway, I’ll be off.”

“Stop right there if you don’t want your head cut off.”

“……”

*Damn it. I shouldn’t have asked.*

Feeling my guts twist with panic, I turned my half-turned body back around.

Fine. Since things had come to this, I might as well hear the story.

“So, you really had other Disciples?”

“They weren’t Disciples, but I taught several people.”

“That sounds like you’re saying there aren’t any anymore.”

“An exceedingly long time has passed. There’s no way any of them could still be alive.”

“Were they involved in…?”

“They were assassins. They belonged to the Salcheonmun with me.”[^2]

Salcheonmun.

Even the name smelled of blood.

*So this man had a sect, too.*

It made sense when I thought about it. No matter how extraordinary Mungyeong was, he hadn’t been born an assassin.

*But if it was the sect the Slaughter Saint belonged to, it should have been fairly famous.*

Yet no matter how thoroughly I searched my memories, the name Salcheonmun was completely unfamiliar.

Just then, Mungyeong seemed to notice my question before I could ask it.

“It’s pointless. The place disappeared long ago.”

There was only one reason a sect disappeared.

Watching Mungyeong’s expression, I carefully put a single word into my mouth.

“Annihilated?”

“Yes.”

“How did that happen? No, before that—weren’t you the Sect Leader?”

“The wrong path was chosen, and the price was paid. That is all I have to say.”

Mungyeong finished speaking and rose to his feet. A short sword in his hand was already radiating vivid blue sword energy.

“Now. It is time to pay the price.”

“Excuse me?”

“Evade my one sword stroke. That is the condition.”

Most people would probably think, *How am I supposed to evade that?* But from my perspective, it was worth trying.

I had endured half an hour against the Slaughter Saint of all people while clumsily pretending to be an assassin. One sword stroke should be manageable.

“If I evade it, will you tell me more later?”

“Of course.”

“Fine. Why not?”

Mungyeong added one more thing.

“Close your eyes.”

“Fuck. Are you kidding me?”

“Then you will die. Not the thirteenth time, but for the first and last time.”

Before he had even finished speaking, Mungyeong’s sleeve fluttered.

Having grown accustomed to his attacks through experience, I instinctively turned my head. But what flew toward me was not a hidden weapon. It was something else.

*That’s…*

It was powder so fine that I could see it only by pushing my visual acuity to its absolute limit.

The powder rode a wind blowing toward me. The instant it touched the air—

Whoosh!

Darkness swallowed the world.

No. That wasn’t right.

The darkness had not swallowed the world. It had swallowed me.

Beep.



> **System**
>
> You have been poisoned by **Blindness Powder**!
>
> You temporarily lose your eyesight!
>
> Rapid **Detoxification** is required! If Detoxification is delayed too long, permanent damage may occur!

My body hair stood on end as the System’s alert pierced my ears.

Blindness Powder? Poison didn’t matter. I was still wearing the Myriad-Poison Ring.

The problem was that Mungyeong’s sword was approaching through the darkness far faster than the ring could detoxify the Blindness Powder.

Ssshhk.

I couldn’t see anything. But I could feel it clearly.

In a world that seemed to flow in slow motion, as though someone had pressed a pause button, I sensed the killing sword approaching while erasing the wind around it.

*This is…*

A move performed by the greatest assassin in history.

A killing intent unlike anything I had ever felt before—so subtle and terrifying that it made me shudder.

I stared blankly at a world filled with darkness.

And within that suffocating space where nothing was visible, I felt every sense within me awaken.

Slash!



* * *

Wudang, the Zhuge Clan, and the Beggars’ Sect.

Although they had selected only trustworthy elites for the sake of secrecy, the caliber and sheer number of those present were impossible to ignore.

Among the several hundred martial artists from prestigious great sects, the figure of a young medical apprentice was bound to stand out wherever he went.

“Oh, it’s you. Are you just coming out?”

“I’ve just come from seeing Young Master Jin.”

“You seem to be dropping by more often these days.”

“Yes. He’s been training so harshly lately that he keeps getting hurt.”

“Good heavens. I see. Great Hero Jin really is something. He’s younger than my son, if you count their ages, yet he never rests on his current realm and keeps striving…”

“He must be an incredible master. I’m completely ignorant when it comes to the Murim.”

At the young medical apprentice’s innocent remark, the Zhuge martial artist standing guard let out a short laugh.

He had been bored, but now he felt a little guilty for bothering a child whose only training was in medicine.

“He is incredible. No doubt about it. You’ll understand someday, too.”

“Hmm. Is that so?”

“If you’re not involved with the Murim, you might not know. Anyway, has today’s training ended?”

As though he knew nothing, Mungyeong tilted his head and answered.

“No. He told me that no one was to approach for the next two shichen.”

“Understood. This is Great Hero Jin we’re talking about—we can’t interrupt his training. I’ll pass that along to the next guards.”

“Yes. Then take care.”

Mungyeong politely bowed at the waist and was about to leave when the martial artist suddenly spoke.

“My, his training must be rougher than I thought.”

“Excuse me?”

“I mean the blood on your sleeve. Was Great Hero Jin badly injured?”

The guard’s follow-up question never reached Mungyeong’s ears.

Mungyeong silently looked down at his bloodstained sleeve and muttered.

“The basics…?”

“Hmm?”

“Oh, it’s nothing. Young Master Jin is unharmed, so don’t worry.”

“Ah. Right. I understand.”

Leaving the martial artist behind with an uneasy expression, Mungyeong walked away.

Several faces had grown familiar enough to speak to him and acknowledge him as they passed, but the young medical apprentice’s mind held only one person.

*Jin Taekyung. Jin Taekyung…*

He had thought it impossible.

And yet that boy had really managed to evade the final sword stroke.

The results Mungyeong had obtained from the tests over the past several days and today were beyond his expectations.

No. They were beyond his imagination.

*So something like this is possible.*

Everything Mungyeong had told Jin Taekyung had been true.

He had once had people who could properly be called Disciples, and every one of them had possessed the “basics.”

But there was one truth he had not mentioned there: the time it took to acquire them.

*The fastest one to pass had taken a little over a year, I think.*

But Jin Taekyung had done it.

In only seven days and nights.

It was a speed that no one else could match.

Mungyeong did not know whether it was because of his Heavenly Martial Physique or because he was a Supreme Peak master, but Jin Taekyung had something special in his own right.

“Even so… I never thought he would be this good.”

Mungyeong murmured so quietly that no one could hear him, then rolled up his sleeve.

As the skin cut by something sharp and the beads of blood gathered on it came into view, a thought suddenly crossed his mind.

*Now I understand how the Fire King feels.*

But Mungyeong did not realize that a faint smile had formed at the corner of his mouth.

[^1]: Teacher’s Day is a Korean holiday observed on May 15 to honor teachers.

[^2]: *Salcheonmun* is the name of the now-vanished assassin sect; it literally means “Slaughter Heaven Sect.”
```
