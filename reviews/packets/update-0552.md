<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0552.txt",
      "sha256": "2d1538cc8209884f564cf9a1cb6e82f3c59fc1166f5c5991f5e9e23b165eefb3",
      "bytes": 15073
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "23c217d51d7beb8e8e05467588aef61d099d4b428875cbc857556c96aa22b7fd",
      "bytes": 3433
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "8f5da66569a6ad674a557886cf6911e213f5ede53dd7180d8fb02515c8a52244",
      "bytes": 174793
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "a9e7a4a1707edb0bbdb8fc08a4cb5cd806350ef5911b9e1de1553e1bb11de348",
      "bytes": 1147
    },
    {
      "path": "characters/Jin Hayeon.md",
      "sha256": "ea6439c6c950cdfddde75d500aab599aca5f990c9aee1f950071d605f1cc4451",
      "bytes": 1518
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "a24b07337d290c902ad594a61e3729e802823710cc154958b808e3159e2bd56f",
      "bytes": 2292
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "8e162d1e9c2539973a1325ee83e627eba33386571047a315a15640e7efb0c543",
      "bytes": 622
    },
    {
      "path": "characters/Kim Jeonghee.md",
      "sha256": "7b27d6bbb2811fef269b39608a719b5d747813a85e40dcaec44c85057f3d152b",
      "bytes": 747
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "647b1cf7f0f2c1d4dc56461eb8d7c079ac9c45c5df1ad44b18562476a3541bca",
      "bytes": 1252
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "da7a0f36d3644731f927d26a782ad3b0419a695ed924eea713365e0f9cb3d704",
      "bytes": 165874
    }
  ],
  "estimated_tokens": 12235
}
-->

# Durable State Update — Chapter 552

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 552. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 552. Profile updates may replace only one
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
  "chapter": 552,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 552,
    "continuity_sources": [552],
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
    "The Fire Dragon Pavilion's first mission is to enter Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is the Title Can't Go to Nanman.",
    "The six-member Fire Dragon Pavilion party has secretly departed Henan; Taekyung's carriage will change horses and reunite with the other two members at Mount Daebyeol before leaving Henan.",
    "Jeok Cheongang remains in Henan and worries about Taekyung's departure, while Mae Jonghak trusts Taekyung to succeed.",
    "Cheongpung is accompanying Mungyeong and learning his martial arts through observation to become stronger and adapt to this world; he remains master of the Azure Dragon Pavilion and caretaker of Mimi.",
    "Mungyeong considers Nanman a plausible site for Dark Heaven's second rift, with a successful attack potentially spreading chaos through Yunnan, Guizhou, Guangxi, and Sichuan.",
    "The Mount Song Resolution restored the Murim Alliance; Mae Jonghak is Alliance Leader, Jeok Cheongang heads the Five Kings Hall, and Murong Yeonghwi oversees Murong Family defenses in Liaoning.",
    "Jin Taekyung is a Supreme Peak master with Three Flowers Gather at the Crown, advanced Qi Sense, exceptional resistance to monster Fear, and public S-rank-level recognition while retaining an A-rank license; he leads the Fire Dragon Pavilion's first mission and has begun Logout during the journey.",
    "Mungyeong ended Taekyung's direct training and assigned him the final task of incorporating martial principles into his learned martial arts.",
    "Zhuge Feng's Demon-Sealing Formation still blocks mana from the exposed Gate, while Jang Taebo processes the Water God Dragon's remains.",
    "Dark Heaven remains an enormous monster-like threat capable of causing rifts and creating mutants; the mechanism behind Jang Sam's transformation remains unresolved.",
    "The Southern Heaven Demon Empress is believed to be moving toward the suspected next target, while Song Ho's dispatch there has received no reply for more than seven days."
  ],
  "continuity_sources": [
    551,
    550
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung's party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Why did Ju Hwaran and Sama Pyo's political engagement end?",
    "What process created Jang Sam's mutant form, and can Dark Heaven's mutants absorb human energy?"
  ],
  "safe_through": 551,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman and 남만을 못 가 as Can't Go to Nanman.",
    "Render 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, and 로그아웃 as Logout.",
    "Preserve Taekyung's blunt profanity and toilet humor, Mae Jonghak's dry banter, and Mungyeong's dry, threatening voice."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 진하연    | **Jin Hayeon**    |
| 십왕     | **Ten Kings**       |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 칭호               | **Title**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 로그아웃             | **Logout**                     |
| 동기화              | **Synchronization** / **Sync** |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 내신 | **school grades** | School-record grades referenced in Taekyung’s insult. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 여사 | **Lady** | Taekyung's joking sobriquet for Kim Jeonghee. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 하연 | 김정희 | daughter_to_mother | Mom | casual-familiar | Hayeon calls 엄마 while reporting that Taekyung hit her. |
| 진태경 | 진하연 | older_brother_to_younger_sister | Jin Hayeon | blunt-familiar; deliberately stern | Taekyung uses Hayeon's full name to make her hesitate while defending his implausible explanation for sleeping forty-two hours. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 진태경 | 엄마 | son_to_mother | Mom | casual and startled | Jin cries out to his mother as she charges at him during the hospital visit. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 엄마 | 진태경 | mother_to_son | my son | warm and affectionate | Taekyung's mother praises him during the public welcome. |
| 진태경 | 수신룡 | hostile martial artist to monster | you, sibu-leol eel bastard | blunt, insulting, and fearless | Taekyung directly insults the emerged Water God Dragon before attacking it. |
| 문경 | 수신룡 | physician_to_dying_spirit_beast | you | guarded and curious | Mungyeong asks whether the Water God Dragon knows him. |
| 문경 | 혁무진 | traveling_companion_to_traveling_companion | Martial Warrior Hyuk | formal-polite | Mungyeong asks Mujin to deliver water to Taekyung and lets Mujin receive the credit. |
| 혁무진 | 문경 | traveling_companion_to_traveling_companion | Mungyeong | casual-familiar | Mujin recognizes Mungyeong while reacting to Taekyung's dismantling work. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 551
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Hayeon.md

# Jin Hayeon (진하연)

- **Safe through:** Chapter 303
- **Aliases:** Hayeon; Taekyung’s younger sister
- **Role:** High-school senior who has completed the college entrance exam and believes she missed a perfect score by one English question
- **Personality:** Sharp-tongued, academically gifted, impatient with Taekyung’s evasions, warmer beneath the teasing, and intensely fond of cats
- **Voice:** Bratty, fast, blunt sibling banter; turns brighter when discussing school and her interests
- **Relationships:** Taekyung’s younger sister; daughter of Taekyung’s mother

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 551
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, and now serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion while holding its unique Title, Fire Dragon Pavilion Master and leading its first mission to Nanman.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 551
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Kim Jeonghee.md

# Kim Jeonghee (김정희)

- **Safe through:** Chapter 328
- **Aliases:** Hayeon's mom, Taekyung's mom, Ajumma
- **Role:** Fifty-year-old mother of Jin Taekyung and Hayeon; after defending Taekyung from the restaurant owner, she quits her restaurant kitchen job and leaves with him.
- **Personality:** Usually quiet, gentle, patient, and family-protective; becomes fierce when Taekyung or her family is insulted.
- **Voice:** Normally deferential and apologetic at work; calm and direct when defending her family, with sudden profanity under extreme provocation.
- **Relationships:** Widow and mother of Jin Taekyung and Hayeon; her deceased husband lovingly called her Jeonghee.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 550
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; he was the sole survivor of an assassin training cohort that began with three hundred candidates and passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom Mungyeong helped break free of his Heart Demon, Mungyeong was asked to look after and instruct Jin Taekyung and has now ended that direct training after teaching him martial principles and giving him a custom fire-qi pill, Cheongpung is accompanying him while learning his martial arts through observation, and Mu Song plus five Water Dragon Stronghold subordinates know he is an exceptionally powerful master but not that he is the Slaughter Saint.

## Korean source

```text
＃552화



띠링.



- [동기화]를 시작합니다. 10, 9, 8, 7…… 1, 0.

- [동기화]가 성공적으로 완료되었습니다. 증가한 능력치가 신체에 적용되며, 특정 칭호에 한하여 사용이 제한됩니다.

- [로그아웃]을 완료했습니다.



검게 물들었던 시야가 또렷해지기도 전에, 매번 그랬듯 시원한 바람이 전신을 스쳤다.

아니, 씻어 내리며 정화(淨化)한다.

‘동기화.’

처음 무림과 현실을 오가게 된 이후, 빠짐없이 거쳤던 과정 중 하나다.

능력치의 변동은 즉각 반영되며 흉터나 상처 따위는 전승되지 않는다.

체격과 외모의 급격한 변화는 다른 이로 하여금 의구심을 품게 만들어서인지, 서서히 그리고 자연스럽게 변화하는 친절한 기능도 있었다.

솨아아아.

이번에도 마찬가지다.

이미 인간의 한계를 뛰어넘은 신체에 다시 한번 힘이 깃들고, 근육이 유연해지는 것이 느껴진다.

수신룡과의 전투와 문경의 가르침을 겪으며 다듬어진 공력 역시 예외는 아니었다.

“후우.”

가장 먼저 눈에 들어온 것은 먼지 하나 묻지 않은 천장이다.

수 미터에 이르는 높은 층고(層高)를 둔 천장에는 고풍스러운 그림이 그려져 있었다.

‘오랜만에 봐서 그런가. 아니면 아직 익숙하지가 않아서 그런가.’

장강의 지류를 타고 호북성을 향할 때가 마지막이었으니, 대략 두어 달이 흐른 뒤에야 돌아온 셈이다.

그래서일까, 주위의 모든 것이 낯설다.

푹신한 이불의 감촉을 느끼며 한참을 천장만 바라보던 나는 문득 입을 열었다.

“저 그림, 제목이 뭐였죠?”

나직한 대답이 들려왔다.

“본 제목은 시스티나 천장화인데, 국내에는 천지창조(The Genesis)로 더 잘 알려져 있습니다. 르네상스 시대의 조각가이자 화가인 미켈란젤로 부오나로티가 탄생시킨 걸작이죠.”

“아, 미켈란젤로. 그랬었지.”

“들어 보셨습니까?”

“워낙 유명하잖아요. 지금 내신 7등급이라고 무시하는 겁니까?”

“내신 성적이야 무슨 상관이겠습니까. 지금은 진태경 씨가 저 그림보다 훨씬 유명해지셨는데.”

사박.

부드러운 가죽 슬리퍼가 대리석을 밟았다.

베개에 반쯤 파묻힌 얼굴을 옆으로 기울이자, 드넓다 못해 광활한 공간을 가로지르는 한 사람의 모습이 시야에 들어왔다.

‘어떻게 저 인간은 볼 때마다 잘생겨지냐.’

어지간해야 질투심이라도 생기지, 일정 수준을 넘어가면 감탄하는 마음만 들기 마련이다.

더군다나 그런 외모가 자연스럽게 느껴질 정도의 분위기까지 갖추고 있다면 더더욱.

나는 두 달 만에 마주하는 그를 향해 씩 웃어 보였다.

“오랜만이네요. 최 팀장님.”

내가 건넨 인사에 실크 가운을 걸친 미남자, 최 팀장의 발걸음이 우뚝 멈췄다.

“꼭 멀리 떠났다가 돌아온 사람처럼 말씀하시는군요.”

“꽤 먼 곳에 있는 꿈을 꿨거든요. 그것도 아주 길게.”

자그마치 두 달을 넘게 무림에 머물렀으니, 내가 한 말은 결코 거짓이 아니다.

사실 그간 일어난 사건들을 생각하면 두 달이라는 시간도 짧게 느껴질 정도였다.

“나쁘지 않은 꿈이었나 보군요.”

“아뇨. 시작부터 용이랑 싸우는 바람에 그다지.”

“드래곤 말입니까?”

“음. 조금 다르긴 한데, 비슷해요.”

“악몽이네요. 그럴 때는 빨리 잠에서 깨는 게 낫습니다.”

달칵.

손에 든 커피잔을 침대 옆 탁자에 내려놓은 최 팀장이 말했다.

“드십시오.”

“엄청나게 비싼 원두커피, 뭐 그런 겁니까?”

지난번처럼 무슨 고양이 똥인지, 혁무진 똥인지로 만든 커피라면 극구 사양인데.

의심 어린 눈빛으로 커피잔을 노려보던 나는, 문득 콧속 깊숙이 파고드는 익숙한 향에 눈을 크게 떴다.

“어라?”

설마 하는 표정으로 바라보니 최 팀장이 피식 웃는다.

“믹스입니다. 그것도 골드. 진하게.”

“키야. 우리 최 팀장님, 뭘 좀 아시네.”

“적어도 진태경 씨와 원두커피가 잘 어울리지 않는 조합이라는 것 정도는 알죠.”

“굿. 그리핀도르에 십 점 추가.”

엄지를 치켜세워 준 나는 단숨에 커피를 들이켰다.

음. 역시 이거지. 싸구려지만 달짝지근한 맛.

간만에 위대한 현대 문물을 접하니 좀 살 것 같다.

“어우, 좋다. 이거 마시니까 정신이 좀 돌아오네요.”

“그렇습니까? 하긴, 오늘따라 평소보다 길게 주무시는 것 같더군요.”

여타의 각성자나 무림인들도 마찬가지지만, 이미 한계를 뛰어넘은 육체의 소유자인 나는 특히나 잠이 적다.

기껏 잔다고 해 봐야 하루에 두 시간을 넘지 않고, 그마저도 수면욕을 채우기 위한 자기만족성 수면이라 할 수 있었다.

‘육체를 어지간히 혹사하거나 정신이 피로하지 않는 이상은 문제없지.’

그런 놈이 몇 시간씩 죽은 듯이 자면 없던 의심도 생기기 마련이다.

나는 하품을 쩍쩍 내뱉으며 기지개를 켰다.

“괜찮으십니까?”

“가끔 이런 날이 있더라고요. 피곤함이 한 번에 몰려와서 그런가.”

비적비적 상반신을 일으킨 나는 손을 뻗었다.

침대 옆에 놓인 탁자 위, 허공섭물(虛空攝物)로 끌어당긴 스마트폰이 자석처럼 손아귀에 착 감긴다.

‘이것도 오랜만이라 그런가, 되게 이상하게 느껴지네.’

매번 현실로 돌아올 때마다 겪는 괴리감 중 하나.

내가 어색하게 화면을 톡톡 두드리자 현재 시각이 떴다.

am 07:05.

오전 일곱 시라. 분명 자정이 지나고 얼마 안 있어 자리에 누웠으니, 얼추 일곱 시간 정도 잔 셈…….

“응?”

이게 뭐지. 날짜가 이상한데.

스마트폰의 화면을 빤히 바라보던 나는, 문득 뇌리를 스치는 생각에 눈을 크게 떴다.

“아.”

워낙 많은 일들을 겪는 바람에 잊고 있었다.

오늘이 무슨 날인지. 왜 내가 굳이 자정이 지난 후에야 방으로 돌아왔는지.

그리고 섬광 같은 깨달음이 찾아온 순간, 최 팀장의 목소리가 귓가를 파고들었다.

“어젯밤에도 말했지만, 한 번 더 말씀드려야겠군요.”

스윽.

불쑥 내밀어진 손과 함께, 나직한 목소리가 이어졌다.

“올 한 해도 잘 부탁드립니다. 진태경 씨.”

2047년 1월 1일.

맞다. 오늘은 현대의 새로운 해가 밝은 날이다. 그리고…….

“생일 축하합니다.”

“……!”

바로 나, 진태경의 스물여덟 번째 생일이기도 하다.

‘젠장. 벌써?’

코앞까지 들이닥친 서른이라는 숫자에 눈앞이 캄캄해진 그때, 저 멀리서 요란한 소리와 함께 두 사람이 들이닥쳤다.

“어이! 스물여덟! 엄마가 미역국 먹으래!”

“네놈의 탄생일을 치하하노라!”

정정한다. 저것들은 사람이 아니라 괴물 두 마리다.

오랜만에 마주하는 원수 같은 호적 메이트, 하연이 그리고 그 옆에 있는 금발의 외국인, 스켈레톤 킹(Skeleton King).

두 사람의 모습에 나는 한숨을 푹 내쉬었다.



* * *



무림과 현대의 시간 격차는 어마어마하다.

지금까지 알게 된 사실에 의하면 어느 한쪽 세상으로 넘어가는 순간 다른 곳의 시간은 매우 더디게 흘러가는데, 무림의 열흘이 현대의 한 시간인 수준이니 때때로 괴리감을 느끼는 것도 무리는 아니었다.

‘특히 이번에는 워낙 많은 일이 있었고.’

무림에서도, 현대에서도 급격한 변화가 일어났다.

그리고 그 변화 중에는 현재 내가 머무르고 있는 이 대저택 역시 포함되어 있었다.

저벅, 저벅.

걷는 곳마다 새하얀 대리석이 번쩍이고, 고풍스러운 그림이며 조각상이 가득하다.

그리고 무엇보다…….

“와, 진짜 더럽게 넓네.”

넓다. 그것도 입이 떡 벌어질 만큼.

지금까지 내가 두 세상을 오가며 숙소로 썼던 모든 곳을 합쳐도 이 대저택의 규모에 비하면 새 발의 피라고 할 수 있을 정도다.

하지만 정작 대저택의 주인은 그렇게 생각하지 않는 듯 했다.

“진태경 씨 말씀대로 조금 큰 편이긴 합니다. 손도 많이 가고요.”

최 팀장의 말에, 뒤에서 졸졸 따라오던 하연이가 불쑥 입을 열었다.

“손이 많이 가는 것 치고는 다른 분들이 안 보이던데요. 맞죠, 아저씨?”

최 팀장을 부르는 호칭이 아니다.

순금을 녹여 만든 것 같은 금발과 신비로운 빛을 띤 금안(金眼).

얼핏 보면 할리우드에서 염문깨나 뿌릴 것처럼 생긴 외국인이 얼굴을 찡그렸다.

“설마 이 몸을 부른 건 아니겠지.”

하연이가 숨도 쉬지 않고 대답했다.

“맞는데요.”

“허.”

헛웃음을 지은 외국인, 매직 존슨의 환영 마법 덕분에 인간의 모습으로 재탄생한 스켈레톤 킹이 피식 웃었다.

“뭔가 잘못 알고 있는 모양이군. 이 몸이 알기로 이 나라의 아저씨란 윗 항렬의 친척 남성. 혹은 중년층 남성을 이르는 단어인데.”

“네.”

“…….”

잠시 말문이 막혀 있던 스켈레톤 킹이 목소리를 쥐어 짜냈다.

“그러니까 내 말은…….”

“서른 살 넘으셨다면서요. 그럼 저한테는 아저씨 맞아요.”

“아니, 넘긴 했는데…….”

“아하. 알겠어요. 그러니까 아저씨인데, 아저씨라고 불리기는 싫으신 거 맞죠?”

“……!”

금빛 눈동자가 파르르 떨렸다. 발걸음도 멈춘 채 하연이를 노려보던 스켈레톤 킹이 중얼거렸다.

“핏줄은 닮는다던데. 확실히 남매가 맞군.”

나와 하연이가 동시에 대답했다.

“나 외동이다.”

“저 외동인데요, 아저씨.”

세상에, 간악한 인간이 둘로 늘어나다니.

딱 그렇게 쓰여 있는 눈동자로 나와 하연이를 번갈아 본 녀석이 포기한 표정으로 고개를 내저었다.

“알았다. 알았으니까 둘 다 그만해라. 그리고 너, 건방진 인간 계집아. 이 몸을 두 번 다시 아저씨 따위로 불렀다가는…….”

저벅.

스켈레톤 킹의 말은 이어지지 못했다.

어느새 하연이가 발걸음도 멈춘 채 멍한 눈동자로 녀석을 바라보고 있었기 때문이다.

“뭐라……고요?”

“아니. 그게 아니고. 내가 말실수를 했다.”

스켈레톤 킹은 내 눈치를 보며 수습하기에 바빴고, 최 팀장은 드디어 올 게 왔다는 표정으로 한숨을 내쉬었다.

“기어코 일을 저질렀군요. 저자는 제가 데려갈 테니 진태경 씨는 동생분을 잘 다독여 주십시오. 오해 안 하도록 조심하시고요.”

“……?”

무슨 소리야, 이게.

나는 최 팀장을 보며 눈을 깜빡였다.

“왜요?”

“네?”

“아니, 왜요. 뭐 때문에 쟤를 다독여요?”

“뭐 때문이라니요. 지금 하연 양이 모욕적인 언사를 들었…….”

최 팀장이 말을 이어 가려던 그 순간. 하연이가 불현듯 입을 열었다.

“건방진 인간 계집? 그게 사람한테 할 말이니, 이 코쟁이 새끼야?”

“……어?”

“……응?”

시작됐군. 나는 입가에 훈훈한 미소를 머금었다.

‘녀석. 여전하구나.’

그래. 이게 진하연이지.

웅장해지는 모세혈관과 함께 비로소 현대로 돌아온 것을 실감하고 있던 그때, 하연이가 나를 향해 고개를 홱 돌렸다.

“들었어? 방금 저 양키 새끼가 한 말.”

나는 묵묵히 고개를 끄덕였다.

“들었지.”

“약점 잡혔니? 전에 몸캠 찍었다가 걸리기라도 했어? 도대체 저딴 새끼랑 왜 같이 다녀? 저런 인간 같지도 않은 놈을…….”

제법 정확한데. 나는 감탄하며 대답했다.

“오, 맞아. 정말 인간 같지 않아.”

“나보고 건방진 인간 계집이래. 미친놈이 저딴 걸 말이라고 하는 거야?”

“음. 말은 말이지. 단지 나쁜 말일 뿐이지.”

“차라리 그냥 미친년, 뭐 그런 평범한 욕이었으면 말도 안 해. 인간 계집이 뭐야. 진짜 기분 더럽게시리.”

나는 스마트폰을 꺼내 속삭였다.

“시리야, 오늘 날씨 알려 줘.”

- 오늘 날씨는. 맑음. 입니다.

“미친놈아. 지금 말장난할 기분이 드니? 하나뿐인 여동생이 다른 사람한테 저딴 말을 들었는데?”

급하게 옷매무새를 가다듬은 내가 깍듯하게 인사했다.

“안녕하세요. 제 이름은 진태경이고, 우리 집 외동입니다.”

“진짜 또라이네, 이거.”

“초면에 말씀이 험하시네요. 사실적시 명예훼손으로 고소하겠습니다.”

순간. 하연이의 눈동자가 서늘하게 가라앉았다.

“엄마한테 다 말할 거야.”

“뭐?”

“엄마한테 말할 거라고. 하나부터 열까지 전부다.”

“너, 지금 나 협박하냐?”

“응.”

“너 이 새끼…….”

와락!

눈을 부릅뜬 나는 있는 힘껏 녀석의 멱살을 붙들었다.

아, 물론 하연이가 아니라 스켈레톤 킹의 멱살을.

“당장 내 동생한테 사과해! 이 인간만도 못한 놈! 몬스터 같은 놈아!”

“미, 미안하다! 이 몸이 잘못했다! 백번 사죄할 테니 제발……!”

“물론 저 녀석이 건방진 것도 맞아! 인간도 맞고! 여자애인 것도 맞아! 하지만 그 세 가지를 붙여서 말해서는 안 됐어!”

“으헉! 으허억!”

“제대로 말해! 똑바로 바른 단어로 붙여서 말하라고!”

“거, 건방진! 사람! 여자애!”

퍼엉.

순간 그런 소리를 들었던 것 같다.

그건 하연이의 분노 게이지가 터지는 소리였고, 녀석은 가장 가까이에 있는 석고 조각상 하나를 집어 들었다.

“죽어. 그냥 둘 다 죽어!”

후웅! 깡!

일일 일깡을 시작으로 아수라장이 되어 버린 복도.

하연이가 용맹한 바이킹 전사처럼 달려들고, 최 팀장이 아연한 표정으로 눈 앞에 펼쳐진 광경을 바라보던 그때였다.

“밥 먹으러 오라니까, 이게 무슨 소란……!”

복도 끝, 저택 내부에 설치된 엘리베이터가 열리고 불쑥 튀어나온 익숙한 얼굴이 딱딱하게 굳었다.

친애하는 김정희 여사. 바로 우리 엄마다.

“……뭐 하니, 너희?”

겨우 160cm도 되지 않는 그녀의 자그마한 체구에서, 나는 최소 십왕(十王)에 버금가는 기세를 느꼈다.
```

## Final English reading copy

```markdown
# Chapter 552

> **System**
>
> **Synchronization** begins. 10, 9, 8, 7… 1, 0.
>
> **Synchronization** completed successfully. Increased stats have been applied to the body, and use is restricted for certain **Titles**.
>
> **Logout** complete.

Before my vision, which had been dyed black, had even cleared, a cool breeze swept across my entire body.

No—it washed over me, purifying me.

*Synchronization.*

It was one of the processes I had gone through without fail ever since I first began traveling between Murim and reality.

Changes to my stats were reflected immediately, while scars and injuries did not carry over.

Perhaps because sudden changes to one’s physique and appearance would make other people suspicious, there was also a considerate function that allowed those changes to happen gradually and naturally.

*Fwoosh.*

This time was no different.

Strength flowed once more into a body that had already surpassed human limits, and I could feel my muscles becoming more supple.

Even the internal energy refined through my battle with the Water God Dragon and Mungyeong’s teachings was no exception.

“Phew.”

The first thing that caught my eye was a ceiling without a speck of dust on it.

The ceiling, several meters above me, was decorated with an old-fashioned painting.

*Is it because I haven’t seen it in a while? Or am I still not used to it?*

The last time I had seen it was when I had been traveling along a tributary of the Yangtze toward Hubei Province. In other words, I had returned after roughly two months.

Perhaps that was why everything around me felt unfamiliar.

I lay there for a long while, feeling the softness of the blankets and staring only at the ceiling. Then I suddenly opened my mouth.

“What was the title of that painting again?”

A quiet answer came from nearby.

“The official title is the Sistine Chapel ceiling frescoes, but in Korea, it’s better known as *The Creation*—*The Genesis*. It’s a masterpiece created by Michelangelo Buonarroti, a sculptor and painter of the Renaissance.”

“Ah, Michelangelo. Right.”

“Have you heard of him?”

“He’s incredibly famous. Are you looking down on me because I got a Level 7 in my school grades?”

“What do your school grades have to do with it? These days, Mr. Jin Taekyung is far more famous than that painting.”

*Tap.*

Soft leather slippers stepped onto the marble floor.

I tilted my face, half-buried in the pillow, and saw a man crossing the vast—no, almost boundless—space.

*How does that man get more handsome every time I see him?*

He would have to be merely good-looking for me to feel jealous, but once someone passed a certain level, all I could feel was admiration.

Especially when he also possessed an aura that made such an appearance seem completely natural.

I grinned at the man I was seeing for the first time in two months.

“It’s been a while, Team Leader Choi.”

At my greeting, Team Leader Choi—a handsome man dressed in a silk robe—came to an abrupt stop.

“You speak as though you’ve just returned from a distant journey.”

“I had a dream about a pretty distant place. It was a very long dream, too.”

I had spent more than two months in Murim, so what I said was by no means a lie.

In fact, considering everything that had happened during that time, even two months felt short.

“It must not have been a bad dream.”

“No. I had to fight a dragon right from the start, so not really.”

“A Western dragon?”

“Something a little different, but close.”

“A nightmare, then. When that happens, it’s better to wake up quickly.”

*Clink.*

Team Leader Choi set the coffee cup in his hand on the table beside the bed.

“Drink.”

“Is it some incredibly expensive coffee made from rare beans?”

If it was coffee made from cat shit or Hyuk Mujin’s shit like last time, I would have to refuse with all my might.

I glared suspiciously at the cup, but then my eyes widened as a familiar scent reached deep into my nose.

“Huh?”

When I looked at him with an expression that said *surely not*, Team Leader Choi gave a quiet laugh.

“It’s instant coffee. Gold blend. Strong.”

“Damn, our Team Leader Choi knows what’s what.”

“At the very least, I know that Jin Taekyung and bean coffee are a poor combination.”

“Good. Ten points to Gryffindor.”

I gave him a thumbs-up and downed the coffee in one gulp.

*Mm. This is more like it.*

Cheap, but sweet.

After finally experiencing one of the great wonders of modern civilization again, I felt somewhat alive.

“Ah, that’s good. I’m starting to wake up.”

“Are you? You did seem to sleep longer than usual today.”

Like Awakened and Murim martial artists, I possessed a body that had already surpassed human limits. As a result, I slept particularly little.

Even when I slept properly, it never lasted more than two hours a day. And even that could be called nothing more than self-indulgent sleep to satisfy my need for rest.

*Unless I’ve pushed my body too far or my mind is exhausted, there’s no problem.*

When someone like that slept like the dead for several hours, it was only natural for people to become suspicious.

I yawned widely and stretched.

“Are you all right?”

“I get days like this sometimes. Maybe all the fatigue caught up with me at once.”

Groggily, I raised my upper body and reached out.

The smartphone sitting on the table beside the bed flew toward me through *Seizing an Object Through Empty Space* and snapped into my hand like a magnet.

*Maybe it’s because I haven’t seen this in a while, but it feels really strange.*

It was one of the forms of disorientation I experienced every time I returned to reality.

I awkwardly tapped the screen, and the current time appeared.

**7:05 a.m.**

Seven in the morning. I had clearly gone to bed not long after midnight, so I must have slept for roughly seven hours…

“Hm?”

What was this? The date looked strange.

I stared at the smartphone screen. Then a thought flashed through my mind, and my eyes widened.

“Ah.”

I had forgotten because so many things had happened.

What day it was. Why I had returned to my room only after midnight.

And just as that realization struck me like a flash of light, Team Leader Choi’s voice reached my ears.

“I mentioned this last night, but I suppose I should say it once more.”

*Swish.*

He held out his hand, his quiet voice following close behind.

“I look forward to working with you this year as well, Mr. Jin Taekyung.”

January 1, 2047.

That was right. Today was the first day of a new year in the modern world. And…

“Happy birthday.”

“...!”

It was also my twenty-eighth birthday.

*Damn it. Already?*

Just as the number thirty came rushing toward me and my vision went dark, two people burst in from the distance amid a great commotion.

“Hey! Twenty-eight! Mom says you have to eat seaweed soup!”[^1]

“I hereby congratulate you on the day of your birth!”

I take it back. Those weren’t people. They were two monsters.

Jin Hayeon, my old enemy on the family register, whom I was seeing for the first time in a while—and the blond foreigner beside her, the Skeleton King.

I let out a deep sigh at the sight of them both.

* * *

The time difference between Murim and the modern world was enormous.

According to everything I had learned so far, whenever someone crossed into one world, time in the other flowed extremely slowly. Ten days in Murim amounted to roughly one hour in the modern world, so it was only natural to feel disoriented sometimes.

*Especially this time. So much happened.*

Rapid changes had taken place in both Murim and the modern world.

And among those changes was the enormous mansion where I now lived.

*Step. Step.*

White marble gleamed wherever we walked, while old-fashioned paintings and statues filled the halls.

And more than anything else…

“Wow. This place is ridiculously huge.”

It was huge. Big enough to leave me speechless.

Even if I combined every place I had used as lodging while traveling between the two worlds, they would still amount to nothing compared to the scale of this mansion.

But the mansion’s owner did not seem to think so.

“As you said, Mr. Jin Taekyung, it is somewhat large. It also requires quite a bit of upkeep.”

“For a place that takes so much work, I don’t see any other people around. Right, old man?”

Hayeon had been trailing along behind us when she suddenly spoke up.

The title was not directed at Team Leader Choi.

A foreigner with hair the color of melted pure gold and golden eyes that gleamed mysteriously frowned.

“Surely you aren’t addressing me.”

“I am.”

“Hah.”

The foreigner, Magic Johnson’s illusion magic having given the Skeleton King a new life in human form, let out a quiet laugh.

“You seem to have misunderstood something. As far as I know, in this country, the term you just used refers to a male relative of an older generation—or a middle-aged man.”

“Yes.”

“...”

The Skeleton King was silent for a moment before squeezing out his voice.

“What I mean is…”

“You said you’re over thirty. Then you’re an old man to me.”

“I am over thirty, but…”

“Ah, I see. You’re an old man, but you don’t want to be called one, right?”

“...!”

His golden eyes trembled.

The Skeleton King stopped walking and glared at Hayeon before muttering,

“They say relatives resemble one another. You really are siblings.”

Hayeon and I answered at the same time.

“I’m an only child.”

“I’m an only child, old man.”

*Good heavens. There were two wicked humans now.*

The Skeleton King looked back and forth between us with eyes that seemed to say exactly that, then shook his head in resignation.

“All right. All right, so stop it, both of you. And you, insolent human girl. If you ever call me an old man again…”

*Step.*

The Skeleton King could not finish his sentence.

Hayeon had stopped walking and was staring at him with a blank expression.

“What did you say?”

“No, that’s not what I meant. I misspoke.”

The Skeleton King hurriedly tried to recover while watching my reaction, and Team Leader Choi sighed with an expression that said this had finally happened.

“You really did it this time. I’ll take him with me, so please calm your sister down, Mr. Jin Taekyung. Be careful she doesn’t get the wrong idea.”

“...?”

What was he talking about?

I blinked at Team Leader Choi.

“Why?”

“Pardon?”

“No, why? Why do I have to calm her down?”

“Why? Because Miss Hayeon was just subjected to an insulting remark…”

At that moment, before Team Leader Choi could continue, Hayeon suddenly opened her mouth.

“‘Insolent human girl’? Is that something you say to a person, you long-nosed bastard?”

“...Huh?”

“...What?”

Here we go.

I smiled warmly.

*She hasn’t changed a bit.*

Yes. This was Jin Hayeon.

As my capillaries swelled magnificently, I finally felt that I had truly returned to the modern world.

Hayeon abruptly turned toward me.

“Did you hear that? That Yankee bastard just said that.”

I nodded silently.

“I heard.”

“Does he have dirt on you? Did you get caught doing some private webcam show or something? Why else would you be hanging around with a bastard like that? With someone who isn’t even human…”

She was surprisingly accurate.

Impressed, I answered,

“Oh, right. He really isn’t human.”

“He called me an insolent human girl. Is that psycho seriously saying things like that?”

“Well, they are words. Just bad ones.”

“Honestly, if he’d just called me a crazy bitch or some other normal insult, I wouldn’t even complain. What the hell is ‘human girl’ supposed to mean? It feels fucking gross.”

I pulled out my smartphone and whispered,

“Siri, tell me today’s weather.”

—Today’s weather is clear.

“You asshole. Are you in the mood for wordplay right now? My one and only little sister just got called something like that by another person!”

I hastily straightened my clothes and bowed politely.

“Hello. My name is Jin Taekyung, and I’m the only child in my family.”

“You really are a lunatic.”

“That’s a remarkably harsh thing to say upon our first meeting. I’ll sue you for defamation by stating facts.”

Hayeon’s eyes instantly turned cold.

“I’m telling Mom everything.”

“What?”

“I said I’m telling Mom. Everything, from beginning to end.”

“Are you threatening me?”

“Yep.”

“You little…”

*Wham!*

Eyes bulging, I grabbed someone by the collar with all my strength.

Of course, not Hayeon.

I had grabbed the Skeleton King.

“Apologize to my sister right now! You subhuman bastard! You monster!”

“I-I’m sorry! I was wrong! I’ll apologize a hundred times, so please…!”

“Of course she’s insolent! She’s human! She’s a girl! But you can’t put those three facts together like that!”

“Ugh! Grrrgh!”

“Say it properly! Put the right words together!”

“I-Insolent! Person! Girl!”

*Boom.*

I think I heard something explode.

It was the sound of Hayeon’s anger gauge hitting its limit. She grabbed the plaster statue closest to her.

“Die. Just die, both of you!”

*Whoosh! Clang!*

The hallway descended into chaos, beginning with the daily clang.

Hayeon charged at us like a brave Viking warrior, while Team Leader Choi stared at the scene unfolding before him in stunned disbelief.

That was when—

“I told you to come eat, so what is all this commotion…!”

At the end of the hallway, the elevator installed inside the mansion opened, and a familiar face emerged before freezing rigidly.

Dear Lady Kim Jeonghee.

My mother.

“...What are you doing, all of you?”

From the tiny body of a woman who stood no more than 160 centimeters tall, I sensed an aura at least on par with one of the Ten Kings.

[^1]: Seaweed soup is traditionally eaten in Korea on birthdays.
```
