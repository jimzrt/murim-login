<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0789.txt",
      "sha256": "fdc9df08bde70525b9f158acff0b2fbfc3d80faf990aab260b36015ee916888d",
      "bytes": 13807
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "049c03c3c85bddc4cf34f1e49774cccbcdfc0e4385d1c38dc56cd5640d666911",
      "bytes": 1176
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "32f4828783668c0672bfb45dfd08b6d44d966992ff3e504ac71740f49cee5315",
      "bytes": 223743
    },
    {
      "path": "characters/Emmanuel.md",
      "sha256": "8611c6c0be8d7218945e747e4fc295b462f34baa3f32c276b9dbbebef7e7859b",
      "bytes": 552
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c6392da9865a241aeef3899b0ed7d131f0d232d1c84d5b9f7b784802373a3b97",
      "bytes": 1925
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "342ef1538972263fa094354c77967554406f6a8c063db4a5a747aa02df60e419",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "c8a83a2c3e4d75c3ab3ab37742a8f9395d6b3b06530e1ad2a1401f347bede044",
      "bytes": 820
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "70d11b238d79ac0c6491bee7e017d77c65dacef3b5423a76950aa693ba449e39",
      "bytes": 693
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "47c7414c02eebe89853f7ad364e576747dfe4baf2551e61b3311fbf556abedf1",
      "bytes": 244361
    }
  ],
  "estimated_tokens": 10193
}
-->

# Durable State Update — Chapter 789

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 789. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 789. Profile updates may replace only one
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
  "chapter": 789,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 789,
    "continuity_sources": [789],
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
    "Michael Silbert is dead; Huginn was captured alive, and Michael’s forces were killed or captured.",
    "The World Hunter Federation is established, with Jin Taekyung as its Alliance Leader.",
    "The Federation announced Michael’s execution and says its operation against his followers is ongoing.",
    "Chuck Hagel’s team took President Emmanuel alive; Ares Guild members are keeping him alive.",
    "Choi Minwoo is the Federation’s interim spokesperson and promises to reveal evidence.",
    "Jin Taekyung has awakened from his deep sleep.",
    "The Skeleton King is Jin’s friend and ally and reassured him that the deaths were not Jin’s fault.",
    "Felix has begun treating the Skeleton King as a friend rather than observing royal conventions.",
    "The system warned of a great fire that could consume the forest, a danger greater than any disease."
  ],
  "continuity_sources": [
    787,
    788
  ],
  "open_questions": [
    "What is the great fire the system warns could consume the forest?"
  ],
  "safe_through": 788,
  "temporary_decisions": [
    "Keep magical power distinct from mana."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 힐러      | **healer**            |
| 마정석     | **Magic Gem**         |
| 임마누엘 | **Emmanuel** | The President of France who congratulates Michael Silbert directly. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 스위스 | **Switzerland** | Country associated with the watchmaker. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 대통령 | **President** | Title for Korea's head of state. |
| 국회의사당 | **National Assembly** | Government building visible from the skyscraper. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 지옥도 | **hellscape** | Metaphorical description of the devastated battlefield. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 프랑스 | **France** | Country containing Paris and Luxembourg Gardens. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 마정 | **Magic Gem** | Monster power source; Leviathan seeks an untouched one. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 엄마 | son_to_mother | Mom | casual and startled | Jin cries out to his mother as she charges at him during the hospital visit. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 힐러 | 진태경 | healer addressing the rescuer who stabilized the survivor | sir | deferential and grateful | The healer thanks Jin as 선생님 after witnessing his rescue and treatment. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |
| 엄마 | 진태경 | mother_to_son | my son | warm and affectionate | Taekyung's mother praises him during the public welcome. |
| 팀원 | 팀장 | team member to team leader | Team Leader Kim | casual, familiar, and dialectal | Team members use forms including 햄 and informal greetings when addressing Kim. |
| 아빠 | 진태경 | father to son | Taekyung | affectionate informal | Addresses his young son warmly as Taekyung. |
| 진태경 | 아빠 | son to father | Dad | childlike informal | Taekyung addresses his father as Dad in the childhood flashback. |
| 팀장 | 팀원 | freelance team leader to subordinate team member | asshole/punk | insulting-casual | The Team Leader addresses the subordinate with 새꺄 and 인마 while joking and complaining over drinks. |
| 진태경 | 힐러 | invading Hunter to Ares healers | you people | profane and contemptuous | Uses 당신들이 while demanding that the healers save their fallen comrades and question Go Jun's order. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |

## Listed compact profiles

### Emmanuel.md

# Emmanuel (임마누엘)

- **Safe through:** Chapter 788
- **Aliases:** None
- **Role:** Emmanuel is the President of France and a longtime political beneficiary of Michael Silbert.
- **Personality:** Ambitious, opportunistic, and willing to trade absolute loyalty for power and wealth.
- **Voice:** Formal and deferential toward powerful allies, with self-important ambitions.
- **Relationships:** He served Michael Silbert with absolute loyalty and was taken alive by Chuck Hagel.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 787
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s new Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 787
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 788
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 782
- **Aliases:** None
- **Role:** The Prophet is the mysterious leader of the revived Hasasin, a Middle Eastern terrorist organization preparing further attacks against apostates and Western heretics.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors, is revered by the followers, and secretly communicates with Michael Silbert through a magic mirror.

## Korean source

```text
＃789화



아마도 몇 년 전부터였을 것이다.

시간과 장소를 불문하고 눈만 감으면 기절하듯 잠들었던 내가 악몽에 시달리기 시작한 것은.

어찌 보면 당연한 일이다.

아무리 무딘 성격의 소유자라고 해도 일주일에 몇 번씩 사선(死線)을 넘나들고, 가까운 사람들이 죽거나 다치는 것을 지켜보다 보면 조금씩 무너지기 마련이니까.

이번에 찾아온 악몽도 그와 같은 맥락이었다.

다만 평소에 꾸던 악몽보다 훨씬 더 덤덤하고, 서글프며, 한편으로는 반갑게까지 느껴졌던 이유는 그 안에서 그리운 사람들을 만났기 때문이었다.



‘아들. 아빠 일하는 동안 하연이랑 잘 놀고 있어야 한다. 알았지?’



아버지의 목소리를 들었고.



‘그냥 형이라고 불러. 형이라고.’

‘와, 오늘 마정석 대박이네. 이렇게 된 거, 오늘 끝까지 달리죠?’



변이 게이트에서 사망한 천수 형과 팀원들의 웃는 얼굴을 보았으며.



‘자네 잘못이 아니야. 자네는 최선을 다했네.’



숨을 헐떡이면서도 나를 다독이던 김 집사님의 곁을 다시 한번 지킬 수 있었다.

물론, 여기서 끝났다면 악몽이라 부르지도 않았겠지.

나는 꿈속에서조차 쉼 없이 싸웠다.

같은 모습을 한 인간들을 쓰러트리고, 몬스터의 가슴에 창날을 쑤셔 박았다.

그리고 허벅지까지 차오른 핏물과 산처럼 쌓인 시체 속에서, 내가 미처 구해 내지 못한 이들이 내지르는 비명을 들었다.

살려 주세요. 여기 사람 있어요. 제발 우리 애만이라도…….

문득 둘러보니, 내 주위에는 온통 지옥도(地獄道)가 펼쳐져 있었다.

아니, 어쩌면 지옥 그 자체였을지도 모른다.

누구보다 이 장소에 어울리는 익숙한 얼굴이 보였으니까.

- 참 기분 좋은 곳이야. 그렇지 않나?

좆 까.

나는 대답과 함께 창을 휘둘렀다.

서걱, 느긋한 발걸음으로 다가오던 미카엘 실베르트의 목이 허공으로 솟구친다.

하지만 놈의 입가에 맺힌 미소도, 검게 번들거리는 눈빛도 사라지지 않았다.

- 잘 보게. 우리가 함께 만든 이 풍경을.

목을 잃은 몸뚱어리가 제멋대로 움직인다.

짝. 짝. 짝. 느릿하게 울려 퍼지는 박수 소리에 이가 악물렸다. 비스듬하게 내리그은 창날로부터 터져 나온 화염이 놈을 덮쳤다.

콰아아아!

보이지 않는 실에 조종당하는 것처럼 움직이던 미카엘 실베르트의 몸뚱어리가 잿더미로 화하여 스러졌다.

하지만 그것으로도 만족하지 못한 불길은 사방에 가득 고인 핏물 위를 내달렸다.

더 멀리, 끝없이.

화아악.

무수한 피와 시신을 장작 삼아 일어난 거대한 화마(火魔)가, 이 지옥도를 완성시킨다.

살아 있던 이들이 내지르던 비명은 그 어느 때보다 높게 솟구쳤다가, 이내 흔적도 없이 잦아들었다.

모든 것이 죽고, 불타고 있었다.

눈 앞에 펼쳐진 그 끔찍한 광경은 꿈을 넘어선 무언가였다.

나는 힘없이 창을 늘어트린 채, 온 세상이 불타오르는 것을 멍하니 지켜보았다.

그리고 이 재앙 속에서도 끈질기게 살아남은 어느 괴물이 지껄이는 소리를 들었다.

- 부디 끝까지 살아남게. 이 세상의 마지막까지, 매 순간 죽을힘을 다해 발버둥 쳐. 그래야 이 광경을 자네의 두 눈으로 똑똑히 지켜볼 수 있…….

퍼엉! 투두둑.

힘을 실어 짓밟음과 동시에 수박처럼 터져 나가는 머리.

하지만 마침내 얻어 낸 고요함 뒤에 찾아온 것은, 종결이 아닌 새로운 무언가의 시작이었다.

쩌저저적.

굉음과 함께 뒤흔들리는 세상.

하늘이 갈라지고, 사방의 공간이 일그러졌다.

동시에 섬광처럼 떠오른 한 단어가 내 머릿속을 관통했다.

‘균열.’

드드드득!

바로 그때였다.

서서히 아득해져 가는 감각 속, 저 멀리서 들려온 누군가의 외침이 악몽에 잠겨 있던 내 정신을 붙잡아 끌어올린 것은.

- ……빠!

빠?

- 오빠!

“……!”

그 순간.

눈앞을 물들이는 광휘와 함께 악몽에서 깨어난 나는 비로소 볼 수 있었다.

어째서인지 눈물범벅이 되어 있는 하연이의 얼굴을.

그리고 짧지만 긴 고민 끝에, 진심을 담아 인사를 건넸다.

“울지 마라. 가뜩이나 못생겼는데 화장까지 지워지면…….”

짝!

음.

나는 아프다. 고로 존재한다.



* * *



그날 하루는 시간이 어떻게 흘렀는지도 모르겠다.

내가 깨어난 직후, 팩트 폭행을 얻어맞은 하연이는 어머니를 쏙 빼닮은 매운 손으로 내 팔뚝을 후려쳤다.

그러고는 이내 유치원생 이후로는 해 본 적도 없던 포옹을 하더니 펑펑 울었다.

그리고 잠시 자리를 비웠다가 다급하게 돌아오신 어머니께서는…… 더 이상 말해 봐야 입만 아프지.

얼마나 서럽게 통곡을 하시던지, 나는 내가 깨어난 장소가 병실이 아니라 영안실인 줄 알았다.

미리 대기하고 있던 의료진이 극구 만류하지 않았더라면, 나는 과장 조금 보태서 두 사람의 눈물에 잠겨 죽었을지도 모른다.

“음, 저기 가족분들. 우선 검사를 진행해야 하니 조금만 진정하시고…….”

설령 마왕 아스모데우스가 쳐들어왔어도 꿈쩍하지 않았을 어머니셨지만, 명망 높은 의사와 힐러의 말 몇 마디에 순순히 물러나시더라.

물론 손을 꼭 붙잡고 신신당부하는 것도 잊지 않으셨다.

“선생님들, 우리 애 좀 잘 부탁드릴게요. 어디 아픈 데는 없는지, 또. 아, 후유증은 없는 거죠? 아까 둘째 얘기를 들어 보니까 태경이가 깨어나자마자 헛소리를 했다고 하던데…….”

“헛소리요?”

“네. 정확히는 저도 잘 몰라요. 잠깐 자리를 비운 사이에 그랬다고 해서.”

“알겠습니다. 환자분, 혹시 무슨 말씀을 하셨는지 기억나십니까?”

내가 대답했다.

“화장 지워지면 더 못생겨지니까 울지 말라고 했는데요.”

“…….”

“그리고 헛소리 아닙니다. 눈 뜨자마자 다시 감을 뻔했어요.”

“…….”

“다들 모르시나 본데, 쟤 화장 지우면 난리 납니다. 몬스터 웨이브를 멀리서 찾을 필요가 없어요.”

하연이는 나를 죽일 듯이 노려보았고, 멍하니 입을 벌린 채 내 얘기를 듣던 의료진들은 병실 한구석으로 가서 숙덕거리기 시작했다.

“괜찮은 걸까요?”

“당신 눈엔 저게 괜찮아 보여?”

“글쎄요. 일단 여동생은 예뻐 보이는데. 화장도 워터프루프라 안 지워진 것 같고…….”

“돌아 버리겠네, 진짜. 지금 그게 문제야? 당신 제정신이야? 누구 추천으로 여기 왔어?”

“내가 추천했네. 미안하군.”

“죄송합니다, 교수님. 어떻게 할까요?”

“음. 우선 신체에는 별다른 이상이 없어 보이기는 하는데…… 후유증으로 뇌에 문제가 생겼을 수도 있으니 전체적으로 검사 한번 해 봅시다.”

“예. 정신과도 포함하겠습니다.”

“…….”

사실을 말했을 뿐인데 정신병자 취급이라니.

억울했지만 별수 없었다. 어머니의 눈물을 멈출 수 있는 가장 빠른 방법은, 건강하다는 걸 보여 주는 것뿐이니까.

‘아플 리가 있나.’

하지만 나는 마음의 소리를 꾹 눌러 담고 힐러와 의사들의 검사에 응했다.

그리고 이 세상에 존재하는 모든 종류의 검사를 끝마친 이후에도, 다음 날까지 강제적인 안정을 취해야 했다.

이틀.

썩 나쁘지 않은 시간이었다.

아니, 솔직히 말하자면 모처럼 편안했다.

안정을 위해 스마트폰도, TV도 없는 곳에서 꼼짝없이 이틀을 누워 있었지만, 가장 소중한 사람들이 내 곁에 있었으니까.

나는 가족들과 함께 먹고, 자고, 웃고 떠들며 꿈 같은 시간을 보냈다.

만약 깨어나기 직전 꾸었던 악몽이 아니었다면, 일말의 불안감조차 느껴지지 않았을 만큼 행복했던 나날들.

하지만 나는 이미 알고 있었다.

이 시간을 더 이상 연장할 수 없다는 것을.

마음속에서 조금씩 커져만 가는 불안감을 없애기 위해서라도, 다시 세상 밖으로 나가야 할 때라는 것을.

어머니와 하연이. 의료진. 그리고 내 휴식을 위해 찾아오지 않는 수많은 지인.

다른 이들이 나를 배려해 바깥의 상황을 알려 주지 않더라도, 시스템만은 아니었다.

‘맹주(盟主)라.’

미처 확인하지 못했던 시스템 알림을 보며 알 수 있었다.

미카엘 실베르트를 완전히 끝장낸 직후, 의식을 잃은 나를 세계 헌터 연맹이 새로운 대표로 추대했다는 사실을.

‘팔자에도 없는 맹주 노릇을 하게 될 줄은 몰랐는데.’

처음에는 놀랐지만, 고민 끝에 받아들이기로 했다.

이는 그들의 결정인 동시에 내 결심이기도 하다.

이미 누군가의 야망이, 그 권력욕이 어떤 참극을 불러오는지 여러 번이나 지켜보았다.

최 팀장이나 매직 존슨이라면 나보다 몇 배나 훌륭한 리더가 될 수 있겠지만…… 그런 그들이 택한 사람이 나라면, 아직 부족하더라도 기꺼이 그 기대에 응할 생각이었다.

‘내가 할 수 있는 최선을 다해서.’

그리고 그전에, 반드시 처리해야 할 일이 하나 있다.

“하연아.”

“응?”

“최 팀장님 번호 알지?”

“안 돼. 쉬어.”

한 치의 망설임도 없는 단호한 대답.

하연이가 굳은 얼굴로 말을 이었다.

“엄마가 알면 참 좋아하겠다. 그치, 응?”

“연락해 줘.”

“…….”

“처리해야 할 일이 있어서 그래. 부탁이다.”

진심을 담아 건넨 말에, 하연이가 입술을 깨물었다.

“아, 진짜 미치겠네.”

“고맙다.”

“미친. 누가 대신 연락해 준대?”

“넌 부탁 들어주기 전에 꼭 입술 깨물더라.”

“…….”

나를 말 없이 응시하던 하연이는 한숨을 푹 내쉬었고, 그건 곧 승낙의 뜻이었다.



* * *



“바람이 차네요.”

그것이 며칠 만에 본 최 팀장의 첫인사였다.

아무도 없는 텅 빈 벤치에 앉아 있던 나는 반가운 마음에 씩 웃어 보였다.

“며칠 만이죠?”

“그날 이후, 오늘로 꼭 일주일 쨉니다.”

“바쁜 시간이었겠네요. 여러모로.”

따라 웃은 최 팀장이 농담을 던졌다.

“예, 진태경 씨께서 편하게 침대에 누워 계시는 동안 저희는 정신없이 바빴거든요.”

“그렇게 말씀하시니까 괜히 죄송해지네. 사과드리면 됩니까?”

“그러실 필요 없습니다. 보스의 특권이니까요. 물론 언론은 진태경 씨의 상태에 대해 알고 싶어 혈안이 되어 있지만 말입니다.”

“하긴, 그렇긴 하겠네요. 전에도 난리였는데, 이제는 맹주라는 직함까지 갖게 됐으니까.”

내 담담한 반응에 최 팀장이 멈칫했다.

“알고 계셨습니까?”

“예.”

“예상했던 반응이랑은 좀 다르군요. 혹시 가족분들이 알려 주신 건.”

“아뇨, 전혀. 손가락 하나 까딱 못하게 하던데요.”

“음. 어디서 새어 나갔는지 모르겠군요. 진태경 씨의 안정을 위해서 나름대로 입단속을 시켰는데.”

“글쎄요. 저도 최 팀장이 모르는 소식통이 있어서.”

나를 물끄러미 바라보던 최 팀장은 별다른 말 없이 고개를 끄덕였다.

더 묻지 않겠다는 뜻이 담긴 제스처.

내가 남들이 모르는 비밀을 감추고 있다는 것을 내심 짐작하고 있는 그로서는, 깨어난 지 불과 이틀 만에 연락이 온 이유가 더 중요하게 느껴졌을 것이다.

“진태경 씨께서 생각하시는 것과 달리, 바깥 상황은 순조롭게 흘러가고 있으니 조금 더 안정을 취하셔도 됩니다.”

“그런가요?”

“예. 이미 일주일 전, 미카엘 실베르트와 밀접한 관계를 맺어 온 주요 인물 다수를 체포했습니다. 또…….”

프랑스의 임마누엘 대통령, 스위스의 차기 대통령이 확실시되었던 베르너 내무부 장관과 거대 기업 총수의 이름이 줄줄이 흘러나왔다.

한 사람, 한 사람이 전 세계의 정, 재계를 아우르는 거물들.

그중 헌터들의 비중이 적은 이유는, 머리라고 부를 만한 이들은 이미 일주일 전의 그 날 미카엘 실베르트와 함께 죽음을 맞이했거나 붙잡혔기 때문이다.

 “과감하면서도 탁월한 결단이었습니다. 그들을 살려 주었다면, 더 큰 내전이 벌어졌을 테니까요.”

그래, 맞다. 그랬기에 더더욱 놈들을 살려 둘 수 없었다.

그날 국회의사당에서 벌어진 전투는 그들의 목숨과 수만, 수십 만의 희생을 맞바꾼 피의 거래였다.

하지만 그것과는 별개로, 최 팀장은 끝끝내 말하지 않았다.

내가 궁금했던 한 존재의 거취에 대해서. 이 불안감의 근원에 대해서.

“최 팀장님.”

나는 문득 별이 총총히 박힌 밤하늘을 바라보았다. 아니, 그곳에 여전히 떠 있는 메인 퀘스트, [격변]의 정보를 바라보며 말을 이었다.

“선지자는, 어디에 있습니까?”
```

## Final English reading copy

```markdown
# Chapter 789

It must have started a few years ago.

That was when I, who used to fall asleep as if I’d passed out whenever I closed my eyes, no matter where or when, began having nightmares.

In a way, it was only natural.

Even someone with nerves of steel could only take so much. Cross the line between life and death several times a week, watch people close to you die or get hurt, and sooner or later, you start to fall apart.

The nightmare that came this time was much the same.

But it was far calmer, sadder, and, in a way, even more welcome than the ones I usually had. Because I met people I missed inside it.

“Son. While Dad’s at work, be a good boy and play with Hayeon, okay?”

I heard my father’s voice.

“Just call me hyung. Hyung.”

“Whoa, we hit the jackpot with these Magic Gems today. Since we’re on a roll, let’s keep going till the end of the day, yeah?”

I saw the smiling faces of Cheonsu hyung and the other team members who’d died in the mutation Gate.

“It wasn’t your fault. You did everything you could.”

I got to stand by Kim Butler’s side once more as he panted for breath and tried to comfort me.

Of course, if it had ended there, I wouldn’t have called it a nightmare.

Even in my dream, I fought without stopping.

I cut down people who all looked the same and drove my spearhead into monsters’ chests.

Then, amid blood that reached my thighs and corpses piled like mountains, I heard the screams of those I hadn’t managed to save.

“Help me! There are people here! Please, at least save my child…”

When I looked around, I found myself surrounded by a hellscape.

No—maybe it was hell itself.

A familiar face, one more at home in this place than anyone else, came into view.

“This is a pleasant place, wouldn’t you say?”

“Go fuck yourself.”

I swung my spear as I answered.

*Slash.*

Michael Silbert’s head sprang into the air as he approached at a leisurely pace.

But the smile on his lips and the gleam in his dark eyes didn’t disappear.

“Take a good look. At this landscape we made together.”

His headless body moved of its own accord.

*Clap. Clap. Clap.* The slow applause rang out, and I clenched my teeth. Flames erupted from my slashing spear and swallowed him.

*Whoosh!*

Michael Silbert’s body, moving as though controlled by invisible strings, turned to ash and crumbled away.

But the flames weren’t satisfied. They raced over the blood pooled everywhere.

Farther. On and on.

*Fwoosh.*

A monstrous blaze fed on the blood and countless corpses like firewood, completing the hellscape.

The screams of the living rose higher than ever—then faded without a trace.

Everything was dead. Everything was burning.

The terrible scene before me was something beyond a dream.

I let my spear droop limply and stared blankly as the whole world went up in flames.

Then I heard the voice of a monster who had stubbornly survived even this calamity.

“Do your best to survive to the end. Struggle with everything you have, every moment, until the very last day of this world. That way, you’ll be able to witness this sight with your own eyes, right until—”

*Pop! Thud-thud.*

I stomped down with all my strength, and his head burst like a watermelon.

But the silence that finally came wasn’t an ending. It was the beginning of something new.

*Crack. Crack.*

The world shook with a deafening roar.

The sky split apart, and space warped in every direction.

At the same time, a single word flashed through my mind like a bolt of lightning.

*Rift.*

*Rrrumble!*

That was when it happened.

As my senses slowly slipped away, someone’s distant shout reached me and pulled my mind up from the depths of the nightmare.

“...ppa!”

Ppa?

“Oppa!”

“……!”

At that moment, a radiant light filled my vision, and I woke from the nightmare.

At last, I saw Hayeon’s face, drenched in tears for some reason.

After a brief but difficult deliberation, I greeted her with all sincerity.

“Don’t cry. You’re ugly enough as it is. If your makeup runs, it’ll only get worse…”

*Smack!*

Ow.

I hurt, therefore I am.

* * *

I couldn’t tell how the rest of the day passed.

The instant I woke up, Hayeon—the recipient of my unfiltered honesty—smacked my arm with a hand just as sharp as Mom’s.

Then she hugged me for the first time since kindergarten and burst into tears.

Mom stepped away for a moment, then came hurrying back… There’s no point going on. It’ll only make my mouth tired.

She sobbed so bitterly that I thought I’d woken up in a morgue instead of a hospital room.

If the medical staff who’d been waiting nearby hadn’t insisted she stop, I might have drowned in their tears. I’m only exaggerating a little.

“Um, family members. We need to run some tests first, so please calm down a little…”

Mom wouldn’t have budged even if Demon King Asmodeus had come knocking—but a few words from a renowned doctor and healer were enough to make her step back without a fuss.

Of course, she didn’t forget to clutch their hands and beg them to take good care of me.

“Please look after my son. Make sure nothing’s wrong with him. And there won’t be any lasting effects, right? I heard from my younger one that Taekyung was talking nonsense as soon as he woke up…”

“Nonsense?”

“Yes. I’m not sure exactly what he said. I was away for a moment when it happened.”

“Understood. Patient, do you remember what you said?”

I answered.

“I told her not to cry because she’d look uglier if her makeup ran.”

“……”

“And it wasn’t nonsense. I almost closed my eyes again as soon as I opened them.”

“……”

“You may not know this, but once she takes off that makeup, it’s a disaster. You don’t have to go looking far for a monster wave.”

Hayeon glared at me as if she wanted to kill me, while the medical staff listened with their mouths hanging open. Then they gathered in a corner of the room and started whispering.

“Is he all right?”

“Does he look all right to you?”

“Hard to say. His younger sister looks pretty, at least. Her makeup’s waterproof, so I don’t think it ran…”

“I can’t believe this. Is that what you’re worried about right now? Are you in your right mind? Who recommended you for this job?”

“I did. Sorry.”

“I’m sorry, Professor. What should we do?”

“Hmm. There doesn’t seem to be anything obviously wrong with his body, but… His brain could have been affected. Let’s run a full set of tests.”

“Yes. We’ll include a psychiatric evaluation.”

“……”

I’d told the truth and they were treating me like a lunatic.

It was unfair, but there was nothing I could do. The fastest way to stop Mom from crying was to show her I was healthy.

*Like I’d be sick.*

But I swallowed that thought and cooperated with the healers and doctors.

And even after completing every test known to this world, I was forced to rest until the next day.

Two days.

It wasn’t a bad stretch.

Actually, if I’m being honest, it was peaceful for once.

I was stuck in bed for two whole days, without a smartphone or TV, all in the name of resting. But the people I cared about most were right there with me.

I ate, slept, laughed, and chatted with my family. It felt like a dream.

If not for the nightmare I’d had just before waking up, those days would have been so happy I wouldn’t have felt a hint of anxiety.

But I already knew.

I couldn’t make that time last any longer.

If I wanted to stop the unease growing inside me, it was time to step back out into the world.

Mom and Hayeon. The medical staff. And all the friends who didn’t come to visit because they wanted me to rest.

Even if the others were considerate enough not to tell me what was happening outside, the System wasn’t.

*Alliance Leader, huh?*

I saw the System notifications I hadn’t had a chance to check and found out: right after Michael Silbert was finished off for good, the World Hunter Federation had appointed me as its new leader while I was unconscious.

*Never thought I’d end up as Alliance Leader, of all things.*

I was surprised at first, but after thinking it over, I decided to accept.

It was their decision, but it was mine too.

I’d seen more than once what someone’s ambition, their hunger for power, could bring about.

Team Leader Choi or Magic Johnson would make several times the leader I could—but if I was the one they chose, then even if I wasn’t ready, I was willing to live up to their expectations.

*I’ll do the best I can.*

But before that, there was one thing I had to take care of.

“Hayeon.”

“Yeah?”

“You know Team Leader Choi’s number, right?”

“No. You need to rest.”

Her answer was immediate and firm.

Hayeon continued, her face set.

“Mom would be thrilled to hear that. Right?”

“Call him for me.”

“……”

“There’s something I need to take care of. Please.”

At my sincere request, Hayeon bit her lip.

“Ugh, this is driving me crazy.”

“Thanks.”

“Are you crazy? Who said I’d call him for you?”

“You always bite your lip before agreeing to do me a favor.”

“……”

Hayeon stared at me without a word, then let out a deep sigh. That meant yes.

* * *

“The wind’s cold.”

That was the first thing Team Leader Choi said when I saw him after several days.

I was sitting on an empty bench. I smiled broadly, glad to see him.

“How long has it been?”

“Today makes exactly one week since that day.”

“Must’ve been a busy week. In more ways than one.”

Team Leader Choi smiled along with me and joked.

“Yes. While you were lying comfortably in bed, we were running around like mad.”

“You make me feel bad. Should I apologize?”

“No need. It’s one of the perks of being the boss. Though the press is desperate to find out about your condition.”

“Fair enough. They made a fuss last time, too. Now I’ve even got the title of Alliance Leader.”

Team Leader Choi paused at my calm response.

“You knew?”

“Yes.”

“That’s not quite the reaction I expected. Did your family tell you?”

“No. They wouldn’t even let me lift a finger.”

“Hmm. I wonder where the news leaked from. I made sure to keep everyone quiet for the sake of your recovery.”

“Who knows? I’ve got sources you don’t know about, too.”

Team Leader Choi studied me for a moment, then nodded without saying anything.

The gesture said he wouldn’t ask any more.

He had a hunch I was keeping some secrets from the others. What mattered more to him was why I’d contacted him just two days after waking up.

“Things outside are going smoothly, despite what you may think. You could rest a little longer.”

“Is that so?”

“Yes. A week ago, we arrested a number of key figures who had close ties to Michael Silbert. Among them…”

He rattled off names: French President Emmanuel, Swiss Interior Minister Werner, who was almost certain to become the next president, and the head of a massive corporation.

Every one of them was a heavyweight who held sway over politics and business around the world.

There were so few Hunters among them because the ones you could call the brains behind it all had either died alongside Michael Silbert that day or been captured.

“It was a bold and brilliant decision. If you’d let them live, a much larger civil war would have broken out.”

Yes. That was exactly why we couldn’t let the bastards live.

The battle at the National Assembly had been a bloody bargain: their lives to prevent tens, perhaps hundreds, of thousands of others from dying.

But even so, Team Leader Choi never brought up the one thing I wanted to know.

What had happened to the one person I was worried about. The source of this unease.

“Team Leader Choi.”

I looked up at the night sky, thick with stars. No—or rather, I looked at the Main Quest, *Cataclysm*, still hanging there, and continued.

“Where is The Prophet?”
```
