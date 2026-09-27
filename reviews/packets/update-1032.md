<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1032.txt",
      "sha256": "7ac25571497377acca947eb754e7991443662cc98790610c3c2c6d9180cebb5d",
      "bytes": 12900
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8da510aa303430d73bed37ae0e234bf59385d1bfe54ba67492e9f38dffab5921",
      "bytes": 887
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b4c0c3ca99c2541072cd872b102fe7c25215b4a24288d92d9f289664b58efda5",
      "bytes": 239887
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "acfe9da532348192ba7ea4e95198ea877a2b707632dd9663a3690cadfbdd6cf8",
      "bytes": 932
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "35a52cc366890670414def0f5ea01729a7fc5d64b3abb107ea4c4d895b36c486",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "581878f26c508011d3cd6b8256145865fadd95cebaf91762af30f7219ad5a537",
      "bytes": 1502
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "03a1c1209fa03435949a49d66244a6dda23347dc500c510ad3bf1c1650d99d34",
      "bytes": 279013
    }
  ],
  "estimated_tokens": 9894
}
-->

# Durable State Update — Chapter 1032

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 1032. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1032. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
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
  "chapter": 1032,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1032,
    "continuity_sources": [1032],
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
    "The Blood-Sword Demon Lord serves the Lord of Heaven and commands the invading army.",
    "The Blood-Sword Demon Lord calls the seven soulless Death Knights Black Ghosts; they have grown stronger and can recover from seemingly fatal injuries.",
    "Jin Taekyung, Jeok Cheongang, and Sama Pyo are fighting the Black Ghosts as the opposing armies clash on the snowy plain.",
    "Sama Pyo has joined the fighting alongside Taekyung and Jeok Cheongang."
  ],
  "continuity_sources": [
    1030,
    1031
  ],
  "open_questions": [
    "Who are the seven Death Knights, what is their rank, and who commands them?",
    "What is the Lord of Heaven’s identity and purpose?",
    "When did Dark Heaven and the Lord of Heaven emerge, and did Dark Heaven cause the Great Faction War?"
  ],
  "safe_through": 1031,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 종남파    | **Zhongnan Sect**                |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 신법     | **movement technique**                           |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 장문인    | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 사매     | **Junior Sister**                            |
| 상태               | **Status**                     |
| 정마대전   | **Great Faction War**         |
| 도사      | **Daoist**                                                      |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 천하삼십육검 | **Heavenly River Thirty-Six Swords** | Zhongnan Sect sword technique used by Song Il. |
| 종남산 | **Mount Zhongnan** | Mountain where the Zhongnan Sect’s main sect is located. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 무량수불 | **Infinite Life Buddha** | Buddhist invocation used by Taekyung. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 비도 | **throwing blade** | Mungyeong throws one past Taekyung's neck. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 풍운검군 | legendary_elder_to_Zhongnan_sect_leader | Wind-and-Cloud Sword Lord | familiar and commanding | Jeok Cheongang tells him to get the Zhongnan disciples moving. |
| 노호검객 | 적천강 | senior_martial_artist_to_legendary_elder | Senior Jeok | deferential and cautious | Addresses Jeok as 노 선배 while explaining his actions. |
| 풍운검군 | 적천강 | Zhongnan Sect Leader to legendary martial master | Senior Jeok | respectful | Refers to Jeok as 적 대협. |
| 풍운검군 | 노호검객 | Zhongnan Sect Leader to Senior Brother | Senior Brother | respectful and strained | Addresses him as 사형 while protesting the decision. |
| 풍운검군 | 태을무정검 | Zhongnan Sect Leader to Senior Brother | Senior Brother | respectful and strained | Addresses him as 사형 while protesting the decision. |
| 혈검마군 | 적천강 | former opposing martial masters | Senior Jeok | respectful and familiar | Addresses Jeok as 선배 while teasing him. |
| 적천강 | 혈검마군 | former opposing martial masters | you; you bastard | blunt and hostile | Uses 너 and 네놈 while confronting him. |

## Listed compact profiles

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1031
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Contemptuous of his former master and certain of his new cause, he treats the weak with ruthless disdain yet takes sincere delight in being recognized and openly admires formidable opponents.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He once served the Heavenly Demon and now serves the Lord of Heaven; he has been ordered not to kill Jin Taekyung, and he admires Jeok Cheongang for burning his attackers alive at Mount Jiuhua.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1030
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1031
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

## Korean source

```text
＃1032화



그것은 마치 두 개의 거대한 파도가 서로를 집어삼키는 듯한 광경이었다.

몇 가지 차이가 있다면 그 장소가 바다가 아닌 드넓은 설원(雪原)이고, 물 대신 무수한 사람들과 번뜩이는 날붙이로 이루어진 파도였으며, 충돌 끝에 터져 나온 포말이 핏빛처럼 붉었다는 것이었다.

아니, 그것은 핏물 그 자체였다.

콰드드드득!

수만 대 수만의 격돌.

뒷걸음질 치는 법을 배우지 못한 군마(軍馬)처럼, 서로를 향해 돌격한 두 갈래의 군세는 삽시간에 서로를 향해 뒤섞였다. 각자의 손에 들린 병장기를 번뜩이며.

차차창! 푸푹!

서걱!

섬뜩한 절삭음과 함께 농밀한 피 안개가 퍼져 나간다.

그리고 삽시간에 무수한 핏물과 비명으로 뒤덮인 설원 속, 맹렬하게 그 중심을 가로지르는 송곳들이 있었다.

“무량수불……!”

화아악.

막강한 기파(氣波)에 폭풍이라도 만난 듯 거세게 흩날리는 도포 자락.

단 일검으로 다섯 명의 적들을 갈라버린 풍운검군(風雲劍君)은, 우윳빛 강기로 거대해진 검신을 비스듬히 내리그었다.

쏴아아악!

엄청난 압력에 공간이 일그러진다. 길게 솟아오른 검강이 흑색 갑주로 무장한 적들을 휩쓸었다.

콰아아아앙!

굉음과 함께 뒤집히는 땅거죽, 동시에 사방으로 비산하는 살과 뼈.

그러나 그 참혹한 광경을 코앞에서 지켜봤음에도, 천주라는 새로운 신을 섬기게 된 교도(敎徒)들은 눈 하나 깜짝하지 않았다.

아니, 정확히는 무언가에 홀린 듯 몽롱한 눈빛으로 풍운검군을 바라보며 계속해서 나아갔다.

여덟 글자의 교언(敎言)을 쉴새 없이 중얼거리며.

“천상천하(天上天下).”

“만마앙복(萬魔仰伏)…….”

퍼걱!

공허하다 못해 오싹하기까지 한 그 음성은 죽음을 맞이한 후에야 끝이 났다.

적어도 그 순간만큼은, 풍운검군은 그렇게 믿어 의심치 않았다.

크르륵.

쩍 벌어진 목울대 사이로 피거품이 들끓는다.

풍운검군의 일검에 목이 베인 교도가 서서히 빛을 잃어 가는 눈동자로 중얼거렸다.

“천상, 끄륵. 천……”

푹!

가슴에 검을 꽂고 나서야 우뚝 끊기는 교언. 그런 교도의 모습에 풍운검군은 등골이 서늘해져 옴을 느꼈다.

‘결코 평범한 자들이 아니다.’

물론 당연한 이야기였다. 천마가 중원을 휩쓸던 그 시절에도,휘하에 결집한 십만 마도는 그야말로 반쯤 미쳐 있는 광신도들이었으니까.

하지만 풍운검군이 당시 마주했던 적들에게는 최소한 두려움이라는 것이 있었다.

인간이라면 누구나 마땅히 지니고 있어야 할 감정이, 그들에게도 분명히 있었다.

‘한데 도대체…….’

순간, 풍운검군은 그제야 이 기시감의 정체를 알아차렸다.

두려움.

놈들에게는 두려움이 없다.

자신이 대적할 수 없는 강자라는 것을 알고 있음이 분명함에도, 암천의 교도들은 바로 이 순간을 위해 태어난 것처럼 계속해서 그를 향해 밀려들고 있었다.

새하얀 포말 대신 붉디붉은 핏물을 흩뿌리며.

쐐애애액!

유려하게 움직인 검 끝이 사방에서 밀려드는 적들을 향해 휘둘려졌다.

천하삼십육검(天下三十六劍).

종남파의 상징과도 같은 초절정의 검공(劍功)이 공간을 휩쓸었다. 극도로 예리한 강기 앞에 두부처럼 잘려 나간 적들의 무기와 몸뚱어리가 조각나며 흩어졌다.

서걱! 투두둑!

섬뜩한 파육음과 함께 허물어지는 시체들.

그러나 한쪽 팔과 함께 가슴이 깊게 갈라진 적 중 하나는 고통에 찬 신음을 내뱉으며 고꾸라지는 대신, 남아 있는 한 손을 뻗는 중이었다.

퍼엉!

날카로운 파공성과 동시에 터져 나가는 도포 자락.

아슬아슬하게 적의 장력(掌力)을 피해 낸 풍운검군이 쾌속하게 손을 뻗었다.

푸푹!

종남파가 자랑하는 천궁지(天穹指)의 지풍이 미간을 관통한 후에야 허물어지는 신형.

하지만 촌각도 안 되는 짧은 시간 동안 수십의 적을 처리했음에도, 풍운검군의 얼굴은 딱딱하게 굳어 있었다.

‘이건.’

틀림없다. 놈들은 두려움이 없을 뿐만 아니라 고통조차 제대로 느끼지 못한다.

특정한 대법이나 몽혼약을 사용했는지는 몰라도, 이는 분명 상리(常理)를 한참이나 벗어난 현상.

이런 적들이 무려 수만이다.

두려움이나 고통을 느끼지 못하는 데다가 개개인의 무위 역시 높으니, 그야말로 전장을 휩쓸기 준비된 전투 병기들.

‘좋지 않다. 아니, 최악이야.’

풍운검군이 정마대전 이후로 처음 느껴보는 두려움에 입술을 깨문 그때였다.

쉬이이익!

겹쳐지는 파공음과 함께 들이닥친 거대한 기운이, 전장의 한축을 파고들었다.

콰아아앙!

난데없는 굉음과 함께 수많은 육편(肉片)이 사방으로 튀었다.

동시에 노호검객과 태을무정검을 중심으로 빈틈없이 검진을 구축하고 있던 종남파의 제자들이, 그 광경을 본 풍운검군이 눈을 부릅떴다.

“안 돼!”

“사, 사매!”

비명과도 같은 외침들.

어린 시절부터 동고동락했던 사문의 식구를 잃은 그들은 엄청난 충격에 사로잡힌 채, 굳건했던 검진을 단숨에 허물어트린 적을 멍하니 바라보았다.

머리부터 발끝까지, 온통 칠흑으로 뒤덮인 두 명의 사내.

아니, 혈검마군이 말했듯이 흑귀(黑鬼)라는 이름이 너무나도 잘 어울리는 알 수 없는 존재들.

스아아아.

전신을 휘감으며 올올이 피어오르는 흑빛 기운이 공기를 잠식한다.

어느덧 자신도 모르게 몸을 떨고 있는 종남파 제자들의 마음을 옥죄고 손발을 묶었다.

“흡……!”

곳곳에서 흘러나오는 가쁜 숨소리.

섬뜩한 기세, 혹은 멀고 먼 어딘가에서는 피어(Fear)라 불리는 그 압도적인 기세에 모두가 짓눌렸다.

아니, 정확히는 그들 대부분이.

슈확!

단숨에 공간을 지우며 쇄도한 풍운검군은 그 어느 때보다 격렬하게 분노하고 있었다.

고작 눈 한번 깜빡할 시간 만에 수십 명이 넘는 제자들이 죽었다.

장문인인 그가 지켜야 할 이들이, 어린 시절부터 지켜봐 왔던 종남파의 동량(棟梁)들이 한순간에 무참히 꺾여 버린 것이다.

“감히!”

쉬쉬쉬쉬쉭!

분노가 실린 검 끝이 바람을 가른다. 구성에 다다른 천하삼십육검이 수십 개의 검영(劍影)을 그려내며 쏟아진다.

그리고, 덧없이 흩어졌다.

후우웅! 캉!

거대한 기운과 기운이 충돌한 순간, 풍운검군의 눈이 크게 부풀었다.

바람을 베어 낸 그의 애검이, 바람과 함께 검영을 지우며 휘둘려진 도끼날에 부딪혀 밀려나고 있었다.

“이 무슨……!”

그그극. 콰앙!

풍운검군이 경악성을 미처 다 토해 내기도 전, 마침내 엄청난 거력(巨力)을 이기지 못하고 튕겨 나간 검신이 부르르 떨렸다.

콰드득!

깊은 골을 만들어 내며 밀려나는 발끝. 가까스로 신형을 추스른 풍운검군은 손목을 찌르는 듯한 통증을 느꼈다.

그와는 비교도 할 수 없을 만큼, 엄청난 충격도 함께.

“네, 네놈은.”

벌어진 입술 사이로 더듬더듬 흘러나온 목소리.

성인 장정만 한 크기의 거대한 대부(大斧)를 쥔 흑귀를 응시하는 풍운검군의 눈동자는 당장이라도 툭 튀어나올 것처럼 부릅떠져 있었다.

‘설마. 설마.’

풍운검군은 애써 부정했지만, 눈앞에 펼쳐진 현실은 달랐다.

단신으로 종남파 장문인을 막아낸 저 흑귀는, 분명 기억 속에 남아있는 얼굴이었으니까.

처음에는 알아보지 못했으나, 이제는 안다.

무식하다 못해 기이하기까지 한 저 무기도. 비록 흉측하게 일그러지고 변색되었지만 아직 어렴풋이 과거의 흔적이 남아 있는 이목구비도.

“……흑부괴마(黑斧怪魔).”

풍운검군은 넋 나간 음성으로 중얼거렸다.

오래전 풍운마군이 스승과 함께 전장에서 맞닥트렸던 마교의 대마두. 처음으로 그에게 죽음의 공포를 심어주었던 초절정의 강자.

그리고…….

“분명, 죽었을 터인데.”

마침내 그날 그 자리에서 최후를 맞이했던, 천마가 거느린 이십 사인의 거마(巨魔) 중 한 사람.

“한데, 한데 도대체 어떻게?”

있을 수 없는 일이었고, 있어서도 안 되는 일.

하지만 풍운검군의 의문은 해결되지 못했다.

다음 순간 휩쓸어오는 강맹한 파공성이, 풍운검군을 현실로 끄집어 올렸으니까.

쐐애애액, 퍼걱!

목이, 피가 솟구친다.

차기 장로감으로 지목받았던 중년의 일대 제자가 단 일 수만에 목이 잘리는 광경에, 풍운검군은 이를 악물며 땅을 박찼다.

“사형들!”

공력이 실린 그 외침에, 뒤늦게 흑부괴마의 정체를 깨닫고 굳어 있던 노호검객과 태을무정검이 움직였다.

파팟!

흐릿해지는 신형. 신법을 발휘하여 깃털처럼 가벼워진 발끝.

그러나 흑귀라는 새로운 이름으로 죽음에서 돌아온 흑부괴마와 결코 그에 못지 않는 막중한 기파를 뿜어내는 또 다른 흑귀를 향해 쏘아지는 풍운검군의 마음은 무겁기 그지없었다.

어쩌면. 어쩌면…….

‘오늘이, 바로 그 날일 수도 있겠군.’

이미 오래전 초인의 반열에 든 그다. 거기에 더해 도사로서는 자격이 부족하지만, 무인으로서는 훌륭한 두 사형도 있다.

한데 어째서일까.

그런 사형들과 일천에 달하는 제자들이 있음에도, 고작 둘밖에 안 되는 저들에게 두려움을 느끼는 이유는.

‘……무량수불.’

종남산을 떠나며 이미 각오했던, 그럼에도 쉽게 받아들이지 못하고 있던 죽음이라는 단어를 떠올리며 풍운검군은 검을 뻗었다.

슈화악!

그리고 공간을 일그러트리며 떨어져 내리는 검격에 맞서 거무튀튀한 도끼날이 휘둘려진 그때.

꽈아아앙!

예상을 아득히 벗어난 거대한 충격과 함께, 풍운검군은 불현듯 깨달았다.

자신의 우려가 결코 단순한 두려움으로 인한 것이 아니었다는 것을.

이 전투의 향방을 결정지을 수 있는 누군가는, 자신이 아니었다는 것을.

콰드득.

느려진 세상 속, 일평생을 함께 해온 애검이 산산이 부서지는 광경을 바라보며 풍운검군은 문득 한 사람을 떠올렸다.

천하의 그 누구보다 강한 것은 아니지만, 지금껏 언제나 그 누구도 예상치 못한 변화의 바람을 불어왔던 누군가를.

그리고 누구보다 앞서 나아가고 있는 젊은이를.

‘진 도우(道友).’

바로 그 순간.

콰아아아!

먹구름보다 어둡고, 핏물처럼 끈적한 마력의 파도가 사방을 휩쓸었다.



* * *



콰아아아…….

어느 순간, 등 뒤의 어디에선가 아스라이 울려 퍼지는 굉음에 나는 본능적으로 움직이려는 고개를 애써 되잡았다.

쉭, 푸푹!

손가락 한 마디 차이로 옆구리를 스쳐 지나간 화살이 사각에서 다가오던 적에게 틀어박힌다.

분명 공력이 실려 있었음에도, 놈은 고통이라고는 한 줌도 느껴지지 않는 듯이 내게 쇄도해서 시뻘건 도기(刀氣)가 맺힌 신월도를 휘둘렀다.

아니, 휘두르려고 했다.

뻑!

한 박자 앞서 채찍처럼 휘두른 발끝을 따라, 산산이 부서지는 뼈마디의 감촉이 느껴졌다.

볼 것도 없는 전투 불능의 상태.

하지만 나는 거기에서 멈추지 않고, 정강이가 으스러진 채 주저앉은 놈을 향해 한 손을 흩뿌렸다.

‘인벤토리 오픈, 소환.’

텅 비어있던 손아귀에 나타난 비수가 잡힘과 동시에 내쏘아진다. 그 섬광의 종착지는 정확히 적의 미간을 겨누고 있었다.

푹, 털썩!

쓰러지는 소리가 들렸을 때, 나는 이미 삼 장의 거리를 더 나아간 후였다.

그리고 그런 내 곁에는 화왕(火王) 적천강이 있었다.

콰아아아!

탐욕스럽게 모든 것을 집어삼키는 불길과 그 끔찍한 열기에 녹아내리는 살갗들.

온 사방이 비명 대신 수증기가 악취로 뒤덮인 그때, 맹렬한 파공성이 귓가에 닿았다.

쐐애애액!
```

## Final English reading copy

```markdown
# Chapter 1032

It was like two enormous waves trying to swallow each other.

There were only a few differences: the setting was a vast snowy plain instead of the sea; the waves were made of countless people and flashing blades instead of water; and the spray that burst from their collision was red as blood.

No—it was blood itself.

KRRRUNCH!

Tens of thousands clashed with tens of thousands.

Like warhorses that had never learned how to back down, the two armies charged toward each other and, in an instant, became entangled. Weapons flashed in every hand.

CLANG! THUNK!

SHING!

With dreadful slicing sounds, a dense mist of blood spread through the air.

And through the snowy plain, swiftly blanketed in blood and screams, there were awls cutting fiercely through the heart of the battle.

“Infinite Life Buddha…”

Whoooosh.

The hem of a Daoist robe whipped violently, as if caught in a storm, under the force of an overwhelming aura.

The Wind-and-Cloud Sword Lord had split five enemies apart with a single sword strike. Now he brought down his blade at an angle, its body enlarged by milky-white Force.

Swaaash!

The sheer pressure warped the space around it. A towering blade of Sword Force swept through the enemies clad in black armor.

KWA-BOOOOM!

The ground flipped over with a deafening crash, and flesh and bone scattered in every direction.

Yet even after witnessing the grisly sight from point-blank range, the followers who had begun worshiping a new god called the Lord of Heaven didn’t so much as blink.

No—more precisely, they kept advancing, gazing at the Wind-and-Cloud Sword Lord with hazy eyes, as if entranced.

All the while murmuring the eight-word creed without pause.

“In heaven and on earth.”

“All demons bow in submission…”

CRUNCH!

Their hollow, almost chilling voices ended only when they died.

At least, that was what the Wind-and-Cloud Sword Lord believed in that moment.

Gurgle.

Blood bubbled between the man’s gaping throat and neck.

The follower, his throat cut by the Wind-and-Cloud Sword Lord’s strike, muttered as the light slowly faded from his eyes.

“Heaven above… gurgle… hea…”

THUNK!

The follower’s words stopped only when the Wind-and-Cloud Sword Lord drove his sword into the man’s chest. Watching him, the Wind-and-Cloud Sword Lord felt a chill creep down his spine.

*They’re no ordinary people.*

Of course they weren’t. Even back when the Heavenly Demon swept across the Central Plains, the hundred thousand members of the Demonic Path gathered under him had been half-mad fanatics.

But the enemies the Wind-and-Cloud Sword Lord had faced back then had at least known fear.

They, too, had possessed the emotion every human ought to have.

*But what in the world…*

Then, at last, the Wind-and-Cloud Sword Lord understood why this felt familiar.

Fear.

They had no fear.

Though they clearly knew he was a superior opponent they couldn’t defeat, the followers of Dark Heaven kept surging toward him, as though they had been born for this very moment.

Spraying blood-red gore instead of white sea foam.

Screeeee!

The tip of his sword swept toward the enemies closing in from every direction.

The Heavenly River Thirty-Six Swords.

The Zhongnan Sect’s emblematic supreme sword art swept across the battlefield. Faced with its razor-sharp Force, the enemies’ weapons and bodies were sliced apart like tofu, their pieces scattering across the snow.

SHING! THUD-THUD!

Corpses collapsed with sickening sounds of torn flesh.

Yet one enemy, his chest deeply cut along with one arm, didn’t crumple with a groan of pain. He reached out with his one remaining hand.

BOOM!

A sharp whistle split the air, and the hem of the Wind-and-Cloud Sword Lord’s robe burst apart.

He narrowly avoided the enemy’s palm strike, then thrust out his hand at blinding speed.

THUNK!

Only after the Zhongnan Sect’s famed Heavenly Vault Finger Qi pierced the man between the brows did his body crumple.

But even after dispatching dozens of enemies in less than a moment, the Wind-and-Cloud Sword Lord’s face remained rigid.

*This is…*

There was no doubt. They had no fear—and they barely felt pain, either.

He didn’t know whether they had used some kind of secret technique or a drug to cloud their minds, but this was clearly far beyond what common sense could explain.

And there were tens of thousands of them.

They felt neither fear nor pain, and each one was highly skilled. They were battle weapons made to sweep across a battlefield.

*This is bad. No—this is the worst.*

The Wind-and-Cloud Sword Lord bit his lip, feeling a fear he hadn’t known since the Great Faction War. Then—

Swoooosh!

Along with a rush of overlapping whistles, an immense force tore into one side of the battlefield.

KWA-BOOOOM!

A sudden crash sent countless scraps of flesh flying in every direction.

The Wind-and-Cloud Sword Lord’s eyes widened as he watched the scene. The Zhongnan Sect Disciples, who had formed a tight sword formation around the Roaring Fury Swordsman and the Taeeul Merciless Sword, had their formation shattered in an instant.

“No!”

“J-Junior Sister!”

Their cries were like screams.

Shocked beyond measure by the loss of a fellow sect member they’d known since childhood, they stared blankly at the enemy who had broken their steadfast formation in a single blow.

Two men, covered in pitch black from head to toe.

No—the Blood-Sword Demon Lord had called them Black Ghosts, and the name suited these unknown beings all too well.

Sssaaaaa.

Black energy curled around their bodies and rose in threads, swallowing the air.

Without realizing it, the Zhongnan Sect Disciples began to tremble. The energy clutched at their hearts and bound their limbs.

“Hngh…”

Strained breaths escaped from all around.

Everyone was crushed beneath their chilling aura—an overwhelming force known as *Fear* somewhere far away.

No—almost everyone.

SHWOOF!

The Wind-and-Cloud Sword Lord erased the space between them in an instant, his fury more violent than ever.

Dozens of Disciples had died in the blink of an eye.

The people he was duty-bound to protect as Sect Leader—the future pillars of the Zhongnan Sect whom he’d watched grow since childhood—had been mercilessly cut down in an instant.

“How dare you!”

SHWING-SHWING-SHWING!

The sword tip, charged with fury, cut through the air. The Heavenly River Thirty-Six Swords had reached nine-tenths of its mastery. Dozens of sword images poured forth.

Then vanished without a trace.

Whoooosh! CLANG!

The moment the enormous forces collided, the Wind-and-Cloud Sword Lord’s eyes widened.

His beloved sword, which had cut through the wind, was being knocked aside by an axe blade swinging with the wind, erasing his sword images as it swept through them.

“What is this…!”

GRRRK. KWAANG!

Before the Wind-and-Cloud Sword Lord could finish his cry of shock, the blade finally gave way to the immense force and was sent flying. It trembled violently.

KRRUNCH!

The Wind-and-Cloud Sword Lord slid back, his foot carving a deep furrow in the ground. He barely steadied himself, pain stabbing through his wrist.

Far worse than the pain was the shock.

“Y-You…”

The words stumbled from his parted lips.

He stared at the Black Ghost gripping a massive battle axe as large as a grown man. The Wind-and-Cloud Sword Lord’s eyes bulged as though they might pop out.

*No. It can’t be.*

He tried to deny it, but the reality before him said otherwise.

That Black Ghost had stopped the Zhongnan Sect’s Sect Leader single-handedly. The face was unmistakably familiar.

He hadn’t recognized it at first. Now he did.

The crude weapon, so strange it was almost grotesque. The features, horribly twisted and discolored, but still bearing faint traces of what they once were.

“…Black Axe Fiend.”

The Wind-and-Cloud Sword Lord murmured, stunned.

A great fiend of the Demonic Cult who had once faced him and his Master on the battlefield, long ago. A Supreme Peak master who had first instilled in him the fear of death.

And…

“He should have died.”

One of the twenty-four great fiends under the Heavenly Demon, who had met his end right there on that day.

“Then, then how…?”

It was impossible. It should never have happened.

But the Wind-and-Cloud Sword Lord’s questions went unanswered.

The next moment, a fierce rush of air came sweeping toward him, dragging him back to reality.

Screeeee—CRUNCH!

A head. Blood spraying into the air.

A middle-aged first-generation Disciple—one regarded as a future Elder—was beheaded in a single stroke. Gritting his teeth, the Wind-and-Cloud Sword Lord kicked off the ground.

“Senior Brothers!”

At his shout, strengthened by internal energy, the Roaring Fury Swordsman and the Taeeul Merciless Sword finally moved. They had been frozen after belatedly recognizing the Black Axe Fiend.

Fwoosh!

Their figures blurred. Their movement techniques made their feet as light as feathers.

But the Wind-and-Cloud Sword Lord’s heart was heavy as he shot toward the Black Axe Fiend, returned from death under the new name of Black Ghost, and another Black Ghost radiating an aura no less immense.

*Could it be? Could it be…*

*Today might be that day.*

He had long since entered the ranks of the superhuman. And though the two Senior Brothers were poor Daoists, they were fine martial artists.

So why?

Why did he fear those two, even with his Senior Brothers and nearly a thousand Disciples at his side?

*…Infinite Life Buddha.*

The Wind-and-Cloud Sword Lord thought of death, a word he’d prepared himself for when he left Mount Zhongnan, yet still struggled to accept. Then he thrust out his sword.

SHWAAASH!

And as a murky-black axe blade swung down to meet the sword strike that warped space—

KWA-BOOOOM!

A colossal impact far beyond his expectations struck. Suddenly, the Wind-and-Cloud Sword Lord understood.

His fears had not been mere fear.

He was not the one who could decide the outcome of this battle.

KRRUNCH.

In a world that had slowed, the Wind-and-Cloud Sword Lord watched his beloved sword, which had been with him all his life, shatter to pieces. An image of someone came to mind.

Someone who wasn’t the strongest person in the world, but who had always brought winds of change no one could have predicted.

And a young man who was moving ahead of everyone else.

*Jin Daoist Friend.*

At that very moment—

KWA-BOOOOM!

A wave of magical power, darker than storm clouds and thick as blood, swept in every direction.

* * *

Rumble…

At some point, a distant crash rang out from somewhere behind me. I forced my head to stay facing forward, even as instinct urged me to turn.

Swoosh—thunk!

An arrow passed my side by a finger’s breadth and buried itself in an enemy approaching from my blind spot.

The shot had clearly been infused with internal energy, but the bastard charged at me as if he hadn’t felt a speck of pain, swinging his curved saber with a crimson blade of Saber Force forming along it.

No—he tried to swing it.

Thwack!

Following the foot I’d snapped out a beat earlier, I felt the bones shatter.

He was obviously out of the fight.

But I didn’t stop there. I flung out one hand at the bastard, slumped to the ground with his shin crushed.

*Inventory open. Summon.*

A dagger appeared in my empty hand. I hurled it the instant my fingers closed around it. The flash of its blade flew straight for the spot between the enemy’s brows.

Thud. Thump!

By the time I heard him fall, I’d already moved another three *jang* ahead.

And beside me was the Fire King, Jeok Cheongang.

KWA-BOOOOM!

Flames hungrily devoured everything in their path. Flesh melted in the terrible heat.

All around us, screams gave way to steam and a stench that filled the air. Just then, a fierce rush of air reached my ears.

Screeeee!
```
