<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0810.txt",
      "sha256": "a43570d7af3389957c66f7f303b6d2e5a529c4dd78fb8d485d2cb87c787c3486",
      "bytes": 12424
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a0049693d1ec64e685fa2bdf15c718d52093b68b69b39276b7e344ca09eb6424",
      "bytes": 1228
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1e8b8a33ae952423b359fb7c39a8c3a83fe8a43b894e38ef519681dd66dd55a7",
      "bytes": 225527
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "686c1a2b920a2905b401746fbec440680094bcead8dd1ca36d14c08b8110d5cd",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "6f0a48cacfd820a450ff794a162498016e13a8d49182ff6ed281538c75f0312b",
      "bytes": 1921
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "41726de2756f61111d1099b4f887bfa6b5667eed3b318f89713336c7ebebb3b3",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "fba43ec54ba0e53481d5c320753956ac5b24ba76aed7b06dac3d50155257470c",
      "bytes": 820
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "ec3ed3f2d007404c688110aba7a1a354a063d993000295c449faab3f6a08b587",
      "bytes": 645
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "8c8c67128595a7afb0e327c946c3e7f6c5e64237595535c15b53ec40b40024fb",
      "bytes": 707
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "014375a90ad668b64bf7cabd37740d6bc24180cb42c734f5b1e1bb40077fa63e",
      "bytes": 248186
    }
  ],
  "estimated_tokens": 9487
}
-->

# Durable State Update — Chapter 810

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 810. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 810. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
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
  "chapter": 810,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 810,
    "continuity_sources": [810],
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
    "Jin is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate the Prophet within an unspecified time limit.",
    "The Prophet remains missing after the Hunter victory; Jin suspects the Prophet planned for the battle’s outcome and wants to face him, but the Prophet’s objective and location are unknown.",
    "The surviving Hunters regroup before pursuing the fleeing army; roughly five thousand monsters remain, and 185 Hunters died in the battle.",
    "Jin has the Broken Body debuff in addition to Damaged Body: Muscles and Bones are weakened, injury risk is higher, and internal energy consumption has increased.",
    "A memory of Michael Silbert has sparked a question in Jin’s mind that he has not yet voiced."
  ],
  "continuity_sources": [
    809
  ],
  "open_questions": [
    "Where is the Prophet, what is his objective, and how is he directing events?",
    "What question did Jin’s memory of Michael Silbert raise?"
  ],
  "safe_through": 809,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Broken Body distinct from the existing Damaged Body debuff."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 생도     | **cadet**                                    |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 마계어 | **Demon Realm language** | Language spoken by monsters from the Demon Realm. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |
| 최민우 | 존슨 | allied Hunter to allied Grand Mage | Mr. Johnson | formal-polite | Minwoo calls out to Johnson during the battle. |
| 진태경 | 선지자 | enemy commander addressed by Jin | The Prophet | blunt and informal | Jin asks where The Prophet is while confronting the Manticore Lord. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 808
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 805
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 805
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 809
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 805
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Jin Taekyung's meticulous intelligence and operations lead, a trusted ally and natural leader capable of guiding the reestablished World Hunter Federation.
- **Personality:** Calm, pragmatic, meticulous, and emotionally steady under pressure.
- **Voice:** Measured, professional, and reassuring without minimizing responsibility.
- **Relationships:** A trusted ally and operational adviser to Jin Taekyung, and the maternal grandson of Cheon Taemin.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 809
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a monster posing as the leader of the revived Hasasin, whose power includes stopping transport vehicles and absorbing blood and a pale mist from the dead.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors, is revered by the followers, and secretly communicates with Michael Silbert through a magic mirror.

## Korean source

```text
＃810화



직감이라는 것은 어쩌면 예지(叡智)의 다른 이름일지도 모른다.

세포에 각인된 본능이 갑작스럽게 깨어나는 듯한 감각.

머릿속에서 뒤죽박죽 엉켜 있던 수많은 잡념이 오직 하나로 합쳐지는 그 느낌.

“미카엘 실베르트. 미카엘 실베르트. 미카엘…….”

마음에서 맴돌아야 했을 이름이 달싹이는 입술 사이로 흘러나오고 있었지만, 진태경은 그 사실을 알아차리지 못했다.

찰나의 순간 머릿속을 채운 하나의 의문. 동시에 잇따라 나타난 새로운 생각들이 꼬리에 꼬리를 물고 이어진다.

스스로에게 던진 질문이 대답과 함께 부메랑처럼 되돌아오면, 진태경은 다시 한번 또 다른 의문을 실어 부메랑을 던졌다.

그럴 때마다 맨 앞에서 빠지지 않는 글자들과 함께.

혹시. 만약에. 어쩌면…….

단 한 순간도 끊임없이 의심하고 또 의심했다.

어느덧 다시 난잡하게 머릿속을 어지럽힌 생각들이 그럴듯한 형태를 갖출 때까지.

시간이 얼마나 흘렀는지조차 모르는 채.

그리고…….

누구의 것인지도 모를 발걸음이, 지척에 이르는 것조차 알아차리지 못할 만큼 깊게.

사박.

모래알이 바스라지는 소리에 잠들어 있던 오감(五感)이 깨어난다.

전신의 솜털이 곤두서고, 뇌의 명령을 기다리지 않는 본능이 몸을 움직였다.

쉭.

돌아섬과 동시에 내리그어진 창날이 공간을 갈랐다.

훈련과 실전에서 수천, 수만 번을 넘게 반복한 동작이다. 본능에 새겨진 그 움직임은 소름 돋을 정도로 예리하고 빨랐다.

어둠 속의 불청객이 순간적으로 죽음을 떠올리게 할 만큼.

하지만 그 역시 만만한 인물은 아니었다.

우우웅.

보이지 않는 기의 파동과 함께 섬광이 번뜩였다.

일순간 환해진 공간 속에서, 뒤늦게 상대의 정체를 확인한 진태경의 눈이 커졌다.

“……!”

깨달음과 함께 찾아온 통제력.

엄청난 속도와 힘을 머금으며 나아가던 일격이 일시 정지 버튼이라도 누른 것처럼 정지한다.

은은한 빛이 서린 반투명한 막에 닿기 직전, 정확히 멈춘 창날과 동시에 강맹한 바람이 휘몰아쳤다.

화아악!

용케도 피에 젖지 않은 모래가 바람을 타고 흩날린다.

간발의 차로 위기를 벗어난 불청객이 입안에 들어간 모래를 뱉어 내며 입을 열었다.

“부탁인데, 날 죽일 생각이면 미리 말해 줘. 마음의 준비를 할 시간 정도는 줘야지.”

창날을 내린 진태경이 다급하게 물었다.

“젠장. 미안해요, 존슨. 어디 다친 곳은 없어요?”

“……보시다시피.”

방어 마법을 해제한 매직 존슨이 간신히 대답했다. 그 잠깐 사이에 식은땀이 맺힌 목덜미가 흐릿한 달빛을 받아 번들거렸다.

“괜찮아. 살짝 지린 것 같긴 하지만.”

“네?”

“오해할 것 같아서 덧붙이자면, 나는 모든 게 큰 사람이지만 이번만큼은 작은 거야.”

그가 농담처럼 던진 말에 진태경이 안도의 한숨을 내쉬었다.

조금 전의 상황은 정말 위험했다. 마지막 순간 창날을 멈추지 않았더라면 분명 피를 봤을 것이다.

“다시 한번 미안해요.”

“괜찮다니까. 그보다 진, 도대체 뭐야?”

“뭐가요?”

“나처럼 훌륭한 친구이자 전우를 적으로 착각한 이유. 조금 전까지 네가 하고 있던 생각.”

“아, 그게…….”

뭔가 대답하려던 진태경은 문득 입을 다물었다.

그리고 그런 그의 모습을 물끄러미 바라보던 매직 존슨이 어깨를 으쓱해 보였다.

“굳이 말하지 않아도 좋아. 우리 어린 보스께서 말하기 곤란한 거라면, 그만한 이유가 있을 테니까. 하지만 이 한마디는 꼭 해야겠어.”

“꼭 해야 할 말이라면…….”

“재정비를 끝마친 지 벌써 30분이 되어 간다는 거지. 지금 널 괴롭히는 고민이 뭐든 간에, 더 이상 추격을 지체하면 놈들을 영영 놓치게 돼. 난 그 말을 전하러 왔어.”

뭐? 벌써?

그제야 뒤늦게 시간을 확인한 진태경이 입술을 깨물었다. 매직 존슨의 말은 전부 사실이었다.

‘언제 이렇게 시간이…….’

체감상으로는 최민우가 다녀간 지 불과 일 분도 채 지나지 않은 것 같은데, 하늘은 그사이에 더 어두워져 있었다.

‘그만큼 생각이 많았던 거겠지.’

무아(無我)라는 두 글자는 무공에만 적용되는 것이 아니다.

진태경은 꼬리를 물고 늘어지는 의문에 시간이 가는 것조차 인식하지 못했고, 매직 존슨은 그가 이 자리에서 움직이지 않았던 이유를 짐작할 수 없었다.

“그들의 죽음이 널 괴롭게 만든다는 걸 알아. 그래서 잠시 시간을 준 거고. 하지만 진, 이대로 놈들을 놓치거나 선지자를 찾아내지 못하면…… 지금까지의 희생도 개죽음이 된다는 걸 명심해.”

툭툭.

커다란 손바닥으로 진태경의 어깨를 두드린 매직 존슨은 한 마디를 남긴 채 돌아섰다.

“모두 기다리고 있어. 우린 네가 필요해, 보스.”

그것이 전부였다.

진태경은 서서히 멀어지는 대마도사의 뒷모습을 바라보며 생각했다.

자신이 떠올린 이 의문들이, 과연 몇 퍼센트의 진실을 품고 있을지. 도대체 무엇이 거짓이고 무엇이 진실인지.

그리고 이내 호흡을 가다듬으며 중얼거렸다.

“아니, 어차피 길은 하나뿐이야.”

간신히 손에 쥔 실마리는 오직 단 하나.

다른 선택지가 없다면 더 이상의 고민은 무의미하다. 진태경은 사방에 도사린 어둠을 향해 무겁게 발걸음을 뗐다.



* * *



사막의 밤은 춥고 어두웠고, 또 광활했다.

그러나 그 누구도 볼멘소리 하나 없이 조용히 걸음을 옮겼다.

백팔십오 명.

비록 짧은 기간이었지만 함께 등을 맞대고 싸운 전우들을 잃었다. 그중에는 초면인 이들도, 가까운 이들도 있었을 것이다. 그런 이들의 시신을 모래 언덕에 묻은 뒤 떠나야 했다.

영웅들의 최후에 어울리는 묘비 대신 피에 젖은 병장기를 꽂으며, 반드시 이 좌표로 찾아와 가족들의 품으로 돌려보내 주겠노라고 맹세했다.

그것이야말로 살아남은 이들이 계속해서 나아가는 이유였고, 나는 그 선두에 있었다.

쐐애애액!

빠르게 사막을 가로지르는 무수한 신형들.

모래가 섞인 바람을 맞은 얼굴이 따끔거렸다. 하지만 이 바람 안에 담겨 있는 것은 단지 모래알뿐만이 아니다.

‘피비린내. 그리고 악취.’

역하지만 익숙한 냄새가 바람을 타고 전해진다. 이동하는 도중 스쳐 지나간 초목과 바위에는 끈적한 액체가 묻어 있었다.

청록색 핏물. 몬스터의 것이 틀림없다.

‘어디냐.’

몸 안에 웅크린 기운을 넓게 퍼트렸다. 동시에 미세한 호흡과 불쾌한 마력의 잔재를 느낀다.

“쉔.”

발걸음을 멈춘 내 부름에, 그 의미를 즉각 깨달은 샤오 쉔이 벼락처럼 뽑아 든 검을 발밑 깊숙이 찔러넣었다.

푸푹!

순간 움푹 꺼진 모래 사이로 핏물이 솟구친다. 동시에 일대의 지면이 파도처럼 출렁였다.

솨아아아악!

흩날리는 모래 사이로 언뜻 모습을 드러내는 괴물들의 모습. 누군가의 다급한 외침이 밤공기를 뚫고 울려 퍼졌다.

“앤트 라이온(Ant Lion)이다!”

속칭 개미귀신.

가장 작은 개체라고 해도 어지간한 중형 자동차만 하고, 최소 B급으로 등급이 책정되어 있는 강력한 몬스터다.

한데 지금 막 모습을 드러낸 놈은 내가 아는 그 어떤 앤트 라이온보다 커다란 집게와 강대한 마나를 품고 있었다.

‘아까 전 전투에서 달아났던 놈이다.’

전장에서 이탈한 덕분에 목숨을 건진 백여 마리의 A급 몬스터 중 하나다.

나는 판단과 동시에 몸을 움직였다.

팟.

단숨에 이십여 미터의 공간이 사라진다. 나는 가장 가까운 헌터들을 집어삼키려는 놈을 향해 창날을 내리그었다.

서걱!

일격. 강철보다 단단한 두 개의 집게가 두부처럼 썰려 나간다.

고통에 찬 비명이 울려 퍼지기도 전에 허공에서 비튼 창대로 놈의 몸통을 찍었다.

콰직!

역한 악취와 함께 핏물이 뿜어졌지만, 결코 숨이 끊길 정도의 부상은 아니다.

나는 미간으로 추정되는 부위에 창날을 지그시 들이대며 입술을 달싹였다.

이 세상의 것이 아닌, 괴물들의 언어로.

- 몇 가지 묻자. 잘 생각하고 대답해.

- ……!

마계어를 연구하는 학자들이 없는 것은 아니지만, 이를 능숙하게 구사하는 인간은 네임드 몬스터보다도 희귀하다.

이런 상황을 전혀 예상치 못했는지, 고통에 물들어 있던 앤트 라이온의 눈동자가 부릅떠졌다.

- 너. 인간. 어떻게?

나는 대답 대신 백염을 쥔 손에 힘을 더했다.

서걱.

예리한 창날이 갑옷처럼 단단한 살갗을 부드럽게 가르자 다급한 목소리가 튀어나왔다.

- 하겠다! 말. 무엇이든!

마계어를 구사하는 솜씨를 보아하니 지성은 낮지만, 눈치는 빠른 놈이 틀림없다. 창날을 멈춰 세운 나는 담담하게 입을 열었다.

- 다른 놈들은 어디에 있지?

- 갔다. 모두. 해가 떨어지는 쪽.

- 서쪽?

- 맞다! 그곳에 있다. 많이!

딱히 의심할 이유는 없었다. 눈앞의 앤트 라이온은 멍청한 놈인 만큼 하는 말마다 진실이 가득 담겨 있었으니까.

‘서쪽이라.’

당연히 도중에 낙오하거나 흩어진 놈들도 있겠지만, 전장에서 이탈한 몬스터 대부분이 서쪽으로 향한 것이 틀림없었다.

물론 내가 정말 알고 싶은 정보는 따로 있었지만.

- 그럼 선지자는?

- 선지자?

- 그래, 선지자.

앤트 라이온의 퉁방울만 한 눈동자가 깜빡였다.

- 그것은 무엇? 모른다. 나는.

나는 뒤늦게 실수를 깨닫고 혀를 찼다.

선지자라는 명칭은 놈이 스스로 세상에 밝힌 것이다. 몬스터 군단이 사막 어딘가에서 옹기종기 모여 TV를 보지 않는 이상 알 수가 없다.

- 정정하지. 선지자가 아니라 너희의 우두머리. 널 비롯한 몬스터들을 이끄는 지휘관으로.

- 지휘관? 우두머리? 우리, 이끌어?

더듬더듬 내가 한 말을 반복하던 앤트 라이온이 두려움과 혼란이 뒤섞인 눈빛으로 나를 바라보았다.

- 죽었다. 네가. 너희가. 모두 죽였다.

- 뭐?

- 하나. 둘. 셋. 넷. 전부 죽었다. 나, 모두. 겁났다. 그래서 도망쳤다.

나는 놈의 눈동자를 가만히 내려다보았다.

그리고 앤트 라이온의 말에는 한 치의 거짓도 존재하지 않는다는 사실을 다시 한번 확인했다.

- 그래, 그렇단 말이지.

- 나, 나, 믿어라! 안 했다. 거짓말.

- 알아.

나는 앤트 라이온의 미간 깊숙이 창날을 밀어 넣으며, 담담하게 덧붙였다.

- 너로 인해 몇 명이 죽었는지도.

퍼걱. 푸그르륵.

피 끓는 소리와 함께 괴물의 거대한 몸뚱어리가 파르르 떨렸다.

나는 또 하나의 죽음을 알리는 시스템 알림을 들으며 창날에 묻은 피와 체액을 털었다.

심문이 끝났음을 알아차린 매직 존슨이 다가와 물었다.

“놈이 뭐라고 했어?”

나는 건조한 목소리로 대답했다.

“글렀어요. 선지자의 존재 자체를 모르고 있더라고요.”

“……빌어먹을. 하긴, S급도 아닌 A급 몬스터가 그걸 다 아는 것도 이상하지. 도망친 놈들이 어디로 향했는지는 알아냈고?”

“네.”

“어디?”

나는 별다른 대답 없이 매직 존슨을 물끄러미 응시했다. 그리고 이내 아무렇지 않게 대답했다.

“동쪽이요.”

매직 존슨의 어깨너머, 스켈레톤 킹이 부릅뜬 눈으로 나를 바라보고 있었다.
```

## Final English reading copy

```markdown
# Chapter 810

Perhaps intuition was just another name for wisdom.

A feeling like the instincts etched into your cells had suddenly awakened.

The sensation of countless jumbled thoughts in your head converging into one.

“Michael Silbert. Michael Silbert. Michael…”

The name that should have stayed in his mind slipped from his moving lips, but Jin Taekyung didn’t notice.

One question filled his mind in a fleeting instant. At the same time, new thoughts came one after another, each following the last.

Whenever a question he asked himself came back like a boomerang, answer and all, Jin threw it again, this time carrying another question.

And each time, the same words led the way.

What if. Suppose. Maybe…

He kept doubting, without pause, without even a single moment to breathe.

Until the thoughts that had once again begun to tangle chaotically in his head took on a shape that seemed to make sense.

Without even knowing how much time had passed.

And…

So deeply that he didn’t notice someone’s footsteps—whose, he couldn’t tell—drawing close.

*Crsh.*

The sound of grains of sand crumbling roused his sleeping five senses.

The fine hairs on his body stood on end, and instinct moved him before his brain could give the order.

*Whoosh.*

As he spun around, the spearhead slashed down, cleaving through the air.

He’d repeated this movement thousands, tens of thousands of times in training and real combat. Etched into his instincts, it was terrifyingly sharp and fast.

Fast enough to make an intruder in the darkness think of death in an instant.

But the intruder was no pushover, either.

*Vwooom.*

A flash of light flared alongside an invisible ripple of qi.

In the space that had suddenly brightened, Jin’s eyes widened as he belatedly recognized the other person.

“……!”

Control came with the realization.

The strike, moving forward with tremendous speed and force, stopped as if someone had pressed a pause button.

The spearhead halted precisely before touching a translucent barrier suffused with a faint glow. At the same time, a fierce gust of wind swept through.

*Fwoooosh!*

Sand that had somehow escaped the blood was caught in the wind and scattered.

The intruder, who’d narrowly escaped danger, spat sand out of his mouth and spoke.

“Do me a favor. If you’re going to kill me, tell me first. Give me a little time to get ready.”

Jin lowered his spear and hurriedly asked, “Damn it. I’m sorry, Johnson. Are you hurt anywhere?”

“……As you can see.”

Magic Johnson managed to answer after dispelling his defensive magic. In that brief moment, cold sweat had gathered on the back of his neck, glistening in the faint moonlight.

“I’m fine. Though I might’ve had a little accident.”

“What?”

“Just so you don’t get the wrong idea, I’m big in every way. This time, though, it was only a little.”

At his joke, Jin let out a sigh of relief.

That had been truly dangerous. If he hadn’t stopped the spearhead at the last moment, there would definitely have been blood.

“I’m sorry again.”

“I said it’s fine. More importantly, Jin, what the hell was that?”

“What was what?”

“Why did you mistake such a wonderful friend and comrade-in-arms as me for an enemy? What were you thinking about just now?”

“Ah, well…”

Jin started to answer, then suddenly shut his mouth.

Magic Johnson watched him for a moment, then shrugged.

“You don’t have to tell me. If our young boss has a reason he can’t talk about it, then I’m sure it’s a good one. But there’s one thing I have to say.”

“If there’s something you have to say…”

“It’s that it’s been nearly thirty minutes since we finished regrouping. Whatever’s troubling you right now, if we delay the pursuit any longer, we’ll lose them for good. I came to tell you that.”

What? Already?

Only then did Jin belatedly check the time and bite his lip. Everything Magic Johnson had said was true.

*When did all that time pass…?*

It felt like less than a minute had passed since Choi Minwoo stopped by, but the sky had grown darker in the meantime.

*I must’ve had that much on my mind.*

The two characters meaning *self-forgetfulness* didn’t apply only to martial arts.

Jin had been so caught up in one question after another that he hadn’t even noticed time passing. Magic Johnson, meanwhile, couldn’t guess why Jin hadn’t moved from that spot.

“I know their deaths are weighing on you. That’s why I gave you a little time. But Jin, if we lose them now or fail to find The Prophet… remember, the sacrifices made up to this point will have been for nothing.”

*Pat, pat.*

Magic Johnson patted Jin on the shoulder with his large hand, then turned away after leaving him with one last remark.

“Everyone’s waiting. We need you, Boss.”

That was all.

Jin watched the Grand Mage’s back slowly recede and wondered how much truth was in the questions he’d come up with. What, exactly, was a lie, and what was the truth?

Then he steadied his breathing and murmured, “No. Either way, there’s only one path.”

He’d barely managed to get his hands on a single clue.

If there was no other choice, there was no point in worrying any longer. Jin took a heavy step toward the darkness lurking all around him.

* * *

The desert night was cold, dark, and vast.

But not one person complained as they quietly marched on.

One hundred and eighty-five.

We’d fought shoulder to shoulder with them, even if only for a short time, and lost them. Some had been strangers; others must have been close. We’d buried their bodies in the dunes, then had to leave them behind.

Instead of gravestones fit for heroes, we planted bloodied weapons in the sand and swore we’d return to those coordinates and bring them back to their families.

That was why the survivors kept moving forward, and I was at the head of them.

*Whoooooosh!*

Countless figures sped across the desert.

The wind, thick with sand, stung my face. But sand wasn’t all it carried.

*The stench of blood. And a foul odor.*

A nauseating but familiar smell drifted to me on the wind. Sticky liquid clung to the plants and rocks we passed along the way.

Blue-green blood. It had to belong to monsters.

*Where are you?*

I spread the energy coiled inside me over a wide area. At the same time, I sensed faint breaths and the traces of an unpleasant magical power.

“Shen.”

I stopped and called out. Xiao Shen immediately understood what I meant. He drew his sword in a flash and plunged it deep into the ground beneath his feet.

*Squish!*

Blood spurted from the sand as it suddenly caved in. At the same time, the ground all around us rippled like waves.

*Shhhhh!*

The forms of monsters briefly appeared amid the scattering sand. Someone’s urgent cry pierced the night air.

“Ant Lion!”

Colloquially known as the antlion.

Even the smallest specimen was about the size of a midsize car, and these powerful monsters were classified as at least Grade B.

But the one that had just appeared had pincers far larger and mana far stronger than any Ant Lion I knew.

*It’s one of the ones that fled the battle earlier.*

It was one of more than a hundred Grade A monsters that had saved their lives by retreating from the battlefield.

I moved as soon as I’d made my judgment.

*Tap.*

A distance of around twenty meters vanished in an instant. I brought my spear down on the monster as it tried to swallow up the Hunters closest to it.

*Shhk!*

One strike. Its two pincers, harder than steel, were sliced off like tofu.

Before its anguished scream could even ring out, I twisted the spear shaft in midair and slammed it into the monster’s body.

*Crack!*

Blood spurted out along with a nauseating stench, but the injury wasn’t severe enough to kill it.

I pressed the spearhead against the spot I guessed was between its eyes and moved my lips.

In the language of monsters, a tongue that didn’t belong to this world.

—I'll ask you a few things. Think carefully before you answer.

—……!

There were scholars who studied the Demon Realm language, but humans who could speak it fluently were rarer than named monsters.

The Ant Lion’s eyes, clouded with pain, flew open. It clearly hadn’t expected this.

—You. Human. How?

Instead of answering, I tightened my grip on White Flame.

*Shhk.*

As the keen spearhead cut smoothly through skin as hard as armor, a panicked voice burst out.

—I answer! Ask. Anything!

Judging from its clumsy Demon Realm language, it wasn’t very intelligent—but it was quick to catch on.

I stopped the spearhead and spoke calmly.

—Where are the others?

—Gone. All. Sun falls that way.

—West?

—Yes! There. Many!

There was no particular reason to doubt it. The Ant Lion in front of me was stupid, and every word it said was packed with truth.

*West, huh?*

Some must have fallen behind or scattered along the way, but most of the monsters that had left the battlefield had undoubtedly headed west.

Of course, I wanted to know something else.

—Then what about The Prophet?

—The Prophet?

—Yes. The Prophet.

The Ant Lion blinked its round eyes.

—What is that? Don’t know. Me.

I clicked my tongue, realizing my mistake belatedly.

The Prophet had personally announced that title to the world. Unless the monster army had gathered somewhere in the desert to watch TV, this creature couldn’t have known it.

—Let me rephrase. Not The Prophet. Your leader. The commander who leads you and the other monsters.

—Commander? Leader? Leads us?

The Ant Lion repeated my words haltingly, then looked at me with fear and confusion in its eyes.

—Dead. You. You all killed them.

—What?

—One. Two. Three. Four. All dead. Me, everyone. Scared. So ran away.

I looked down into its eyes.

Then I confirmed once again that there wasn’t a hint of a lie in what the Ant Lion had said.

—Right. So that’s what happened.

—Me, me, believe! Didn’t. Lie.

—I know.

I pushed the spearhead deep between the Ant Lion’s eyes and added calmly, “I know how many people died because of you, too.”

*Squish. Gurgle.*

With a bubbling sound, the monster’s enormous body trembled.

I shook the blood and bodily fluids from my spear as I heard a System notification announce another death.

Magic Johnson realized the interrogation was over and came over to ask, “What did it say?”

I answered in a dry voice. “No luck. It didn’t even know The Prophet existed.”

“……Damn it. Well, it’d be strange for an A-rank monster—not even an S-rank—to know all that. Did you find out where the ones that ran off are headed?”

“Yes.”

“Where?”

I stared at Magic Johnson without answering. Then I replied as if it were nothing.

“East.”

Over Magic Johnson’s shoulder, the Skeleton King stared at me with wide eyes.
```
