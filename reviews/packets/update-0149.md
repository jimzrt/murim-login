<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0149.txt",
      "sha256": "042446e4c9f6d148089acecd083e9a9fee5cd16dc7edc91c3f9c6e9068830ad9",
      "bytes": 16341
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7e64673406e2e29210154ff0afff8fecb8d5e0c70cb7acc7b7512b249581b260",
      "bytes": 5049
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "825cbb04343ec15f6c565c9dd7020ad14c4c40b653713ea4bb382250b43b2f52",
      "bytes": 32730
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "ce0af435bde5a6da420a55c54d3c31588dc3685b3bea7f04ec733ace0c18210a",
      "bytes": 1253
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "567ad7e91fb598031ef3c83077d3a365d52d3eb500da052681f805bb214987b0",
      "bytes": 468
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "32dff10542435fba1ec6e30e209888a648ba2e77198918dea58a6e5284650cce",
      "bytes": 28534
    }
  ],
  "estimated_tokens": 26641
}
-->

# Durable State Update — Chapter 149

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 149. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 149. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Speaker and addressee must be Hangul source spellings (Arabic digits
allowed in titles such as 1팀장; do not romanize). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 149,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 149,
    "continuity_sources": [149],
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
    "The City Lord's luncheon attendance requirement has concluded; Prince Shangshan's Token was obtained as the Quest Reward, and Zhu Bao is expected at the Jin Family's grand banquet in roughly fifteen days.",
    "Zhu Bao is ten years old, has trained in martial arts daily for three years, is an exceptionally skilled young swordsman personally named Zhu Bao, and admires Jin Taekyung.",
    "Taekyung remains below the Peak realm and cannot use Sword Energy despite defeating Jopil, Jin Baekyang, and Pung Yang.",
    "Hong Jin and Li Feng are pursuing the Shaanxi–Shanxi trade project through Huashan, with Li Feng acting as intermediary and the Seongun Escort Bureau proposed as the base.",
    "Cheongpung is a twenty-year-old Peak master raised by Mae Jonghak, the Sword Saint; he knows several Huashan martial arts, can use the Zaha Divine Technique, obtained the Royal Guard Armor Set, and has no martial title yet.",
    "Mae Jonghak remained in deep seclusion at a hidden Huashan residence and had been there at least ten years before the luncheon; Cheongpung came to Huashan at about age three or four rather than being born there.",
    "Li Feng left Huashan after becoming discouraged by Cheongpung's extraordinary talent, not because of his defeat by Gong Ilhyuk.",
    "The identities of the other two members of the Three Hands of Zhongnan remain unknown.",
    "Hong Jin is a eunuch who formerly served the late Emperor, was ordered to assist Prince Shangshan, has served the prince since infancy, and is the power behind the Shanxi Provincial Office.",
    "Gong Ilhyuk leaves the luncheon humiliated and vows revenge against those who rejected and insulted him.",
    "Li Feng commands the military's respect, while Hong Jin holds influence over civil officials and servants through fear.",
    "The four heirs of the Five Gates of Shanxi excluding the Seongun Escort Bureau are frightened of the Jin Family, Huashan, and the government and are being pressured to support Taekyung's side; they will remain at Honghwa Inn until New Year's Day.",
    "Taekyung threatened to absorb Gopyeong Sect as the Gopyeong Branch of the Jin Family of Taiyuan if its young sect leader refused to cooperate.",
    "Jin Mukyung flatly refused Zhu Bao's autograph request three years earlier; Taekyung now promises to obtain Mukyung's autograph for Zhu Bao at the upcoming banquet.",
    "The current Military Commissioner is incompetent, fond of bribes, and directly appointed and dismissed by the Emperor.",
    "Jin Wikyung returned to the Jin Family after nearly ten days away and is responsible for a large administrative workload; he prefers practical people with flexible thinking over rigid scholars.",
    "Hong Jin gave Jin Wikyung one thousand silver nyang, and the Jin Family responded with an extravagant pro-imperial welcome.",
    "Jin Wikyung and Hong Jin immediately form a joking rapport, addressing each other as Comrade Hong and Lesser Family Head Jin.",
    "Cheongpung intends to defeat all Ten Dragons and Phoenixes before returning to Huashan, beginning with Jin Mukyung.",
    "Cheongpung and Jin Mukyung have begun a duel, but its outcome is unknown."
  ],
  "continuity_sources": [
    148,
    147
  ],
  "open_questions": [
    "What did Mae Jonghak mean by saying a crane delivered Cheongpung to him?",
    "Why did Mae Jonghak remain hidden at Huashan despite the sect eventually finding his residence?",
    "What are the names and individual identities of the other two members of the Three Hands of Zhongnan?",
    "What is the full title of the wuxia novel beginning with 군림…… that Taekyung read through volume thirty-four?",
    "Was the Emperor's reported suspicion of his younger brother the reason Prince Shangshan was sent to Shanxi, and what danger does the imperial succession pose?",
    "What martial title will Cheongpung eventually acquire?",
    "What circumstances led Hong Jin to become a eunuch and come to the frontier in something like exile?",
    "What is the outcome of Cheongpung's duel with Jin Mukyung?"
  ],
  "safe_through": 148,
  "temporary_decisions": [
    "Render 전하 as “His Highness” as the formal royal address and 왕 as “king” when used literally.",
    "Render 초일류 as “advanced First Rate” and 군문 as “military” when describing an affiliation.",
    "Render 풍운검군 as “Wind-and-Cloud Sword Lord” and 오촌 당숙 as “father's cousin.”",
    "Render 태을미리장 as “Taeeul Miri Palm.”",
    "Render 후배님 and 선배님 as “Junior” and “Senior” in the Gong Ilhyuk exchange.",
    "Render 태사부 as “Grandmaster” and 사숙 as “Martial Uncle” in the Huashan context.",
    "Render 자하신공 as “Zaha Divine Technique”; render 근위대 as “royal guard” and 근위대 갑옷 세트 as “Royal Guard Armor Set.”",
    "Render 비무행 as “dueling tour,” 청강검 as “blue-steel sword,” and 광염 as “light-flames.”"
  ],
  "version": 1
}
```

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 최 팀장 | **Team Leader Choi** | Team Leader who owns the café where Taekyung signs a contract. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 김 집사 | **Butler Kim** | Choi's butler and limousine driver. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 히말라야의 정수 | **Essence of the Himalayas** | System-named consumable that temporarily raises Intelligence. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 순이네 수퍼 | **Sooni's Super** | The Peace Guild's Guild house. |
| 송 양 | **Miss Song** | The Peace Guild's final member; full identity not yet given. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 임혁준 | **Im Hyeokjun** | Im Kkeokjeong's personal name, shown in the System Level window. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 부천터미널 길드 | **Bucheon Terminal Guild** | Guild whose raid footage is shown. |
| 미노타우로스의 미로 | **The Minotaur's Labyrinth** | B-rank Gate. |
| 상동 길드 | **Sangdong Guild** | Mid-sized Guild near Bucheon that joins Peace Guild's first official raid. |
| 헌터 협회 | **Hunter Association** | Organization investigating the Bucheon Terminal Guild fatality. |
| 흑색 드레이크 | **Black Drake** | B-rank monster whose leather and spine are used for Taekyung's loaned equipment. |
| 장인의 흑색 드레이크 가죽 세트 | **Masterwork Black Drake Leather Set** | Peak-grade armor set loaned to Taekyung. |
| 장인의 검은 가시 창 | **Masterwork Black Thorn Spear** | Peak-grade spear loaned to Taekyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| K사 | **K Company** | Manufacturer of the space-expansion suitcase. |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 청담동 | **Cheongdam-dong** | District mentioned as a luxury shopping location. |
| 투우사의 전신 갑옷 | **Matador’s Full-Body Armor** | Peak-grade armor equipped by Im Kkeokjeong; grants bonuses against bovine-type monsters. |
| 투우사의 방패 | **Matador’s Shield** | Peak-grade shield equipped by Im Kkeokjeong; can activate Taunt and Hallucination against bovine-type monsters. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 미노타우로스 전사 | **Minotaur Warrior** | Level-window designation for the first Minotaur encountered in the labyrinth. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 횡성 | **Hoengseong** | Place in Gangwon Province named in Taekyung’s joke. |
| 자일리톤 | **Xyliton** | Finnish equipment manufacturer whose custom helmet records video. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 미노타우로스 대전사 | **Minotaur Warrior** | Level 70 B-rank boss monster of The Minotaur's Labyrinth. |
| 임 팀장님 | **Team Leader Im** | Formal address for Im Changsoo used by a Sangdong Guild teammate. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| K은행 | **K Bank** | Bank where Im Changsoo's transfer is reported. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 김민수 | **Kim Minsu** | The restaurant owner's son; D-rank Hunter in Sangdong Guild. |
| 민수 | **Minsu** | Short form used for Kim Minsu. |
| 운기요상 | **Circulate Qi for Healing** | System-named skill that channels internal energy through another person's body to cleanse accumulated waste and restore health. |
| 하급 포션 | **Lesser Potion** | Low-grade healing potion issued as raid supplies; its System Grade is Third Rate. |
| 3차 각성자 | **third-awakening Hunter** | Hypothetical Hunter classification that would come after reawakening. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 피의 일주일 | **Bloody Week** | The hellish first week after Gates opened, during which casualties reached the tens of millions. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 박지훈 | **Park Jihoon** | Current name of Taekyung's former middle-school classmate; Hunter in Myeongdong Guild Team 1. |
| 박지황 | **Park Jihwang** | Jihoon's former name, revealed when Taekyung recognizes him. |
| 가람중 | **Garam Middle School** | Middle school attended by Taekyung and Jihoon. |
| 명동 길드 | **Myeongdong Guild** | Large Guild in which Jihoon belongs to Team 1. |
| 1팀장 | **Team 1 Leader** | Sangdong Guild's Team 1 leader and its only A-rank Hunter besides Im Chunsoo. |
| 희망 고시원 | **Hope Goshiwon** | The goshiwon listed as Taekyung's residence in the target report. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 집파리 | **Housefly** | System label for a Level 1 fly familiar. |
| 검정파리 | **Black Blow Fly** | System label for a Level 1 fly familiar. |
| 금파리 | **Green Bottle Fly** | System label for a Level 1 fly familiar. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 김선희 | **Kim Seonhee** | Assistant Manager at the Ilsan Store |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 라페스타 | **Lafesta** | Shopping and entertainment district in Ilsan |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 김희선 | **Kim Seonhee** | Source spelling variant for the established Assistant Manager Kim Seonhee at the Ilsan Store. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 최병일 | **Choi Byungil** | B-rank Security Team leader; his Level is in the mid-sixties. |
| 박형진 | **Park Hyungjin** | One of the C-rank Sangdong Guild watchers. |
| 오규현 | **Oh Gyuhyeon** | One of the C-rank Sangdong Guild watchers. |
| 이민철 | **Lee Mincheol** | One of the C-rank Sangdong Guild watchers. |
| 교관 | **Instructor** | Kim Hwajong's former Hunter Training Center role and address. |
| 헌터 훈련소 | **Hunter Training Center** | Training institution where Kim Hwajong served as an instructor. |
| 1번 훈련생 | **Trainee Number One** | Im Chunsoo's training call sign during his forced military identification. |
| 28연대 1대대 2중대 | **28th Regiment, First Battalion, Second Company** | Military unit designation shouted during Im Chunsoo's identification. |
| 사도세자 | **Crown Prince Sado** | Joseon crown prince used in the comparison for Jinho's haggard appearance; footnoted. |
| 박혁거세 | **Park Hyeokgeose** | Legendary founder of Silla, used in the comparison to Jinho emerging from the capsule; footnoted. |
| 열양공 | **heat-yang technique** | Mukyung's heat-based internal-energy technique. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 산서제일미 | **Shanxi's foremost beauty** | Former reputation of Taekyung's mother. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 계용옥미갱 | **chicken-and-corn soup** | Egg-thickened corn soup. |
| 계용옥미앵 | **chicken-and-corn soup** | Source spelling variant of 계용옥미갱 for the same dish. |
| 광수 | **Gwangsu** | First attacker at the Phoenix Inn; identified by the others after Taekyung punches him. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 관제묘 | **Guandi Temple** | Shrine type mentioned in martial-arts novels. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 오색귀 | **Five-Colored Ghosts** | Nickname for the five former subordinates of Jang Sam. |
| 이삼 | **Lee Sam** | Leader of the ten-man human-trafficking group; his Level window identifies him by this name. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 토호단 | **Earth Tiger Band** | Mounted-bandit group formerly led by Pung Yang's subordinate. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 춘삼 | **Chunsam** | Lower District Sect martial artist serving as the carriage driver. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 대동지부 | **Datong Branch** | Mount Heng Sword Sect branch in Datong. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 철 숙부 | **Uncle Cheol** | Lee Seowol's familial address for Cheol Mubaek. |
| 철 대협 | **Great Hero Cheol** | Respectful address for Cheol Mubaek. |
| 아가씨 | **Young Lady** | Former address used for Lee Seowol before she demands the title Sect Leader. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 산서괴협 | **Strange Hero of Shanxi** | Epithet referenced for the absent martial artist. |
| 녹림맹주 | **Green Forest Alliance Leader** | Leader title for the Green Forest Alliance. |
| 장강수로맹주 | **Alliance Leader of the Yangtze River Channel League** | Leader title for the Yangtze River Channel League. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 절정 초입 | **early Peak** | Pung Yang's specific stage within the Peak realm. |
| 광칠이 | **Gwangchil** | Former mounted-bandit boss who took in Pung Yang and was later killed by a First Rate master. |
| 일류 초입 | **early First Rate** | Early stage of the First Rate realm. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 항산권문 | **Mount Heng Fist Sect** | Alternate fist-sect designation used by Pung Yang for the Mount Heng defenders. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 적혈십이검 | **Crimson Blood Twelve Swords** | Peak-level martial arts manual discovered by Pung Yang. |
| 적혈심법 | **Crimson Blood Cultivation Technique** | Cultivation technique discovered by Pung Yang. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 태산압정 | **Mount Tai Presses Down on the Crown** | First move of the Three Calamities Sword Technique. |
| 나려타곤 | **Narye tagon** | Humiliating idiom comparing a fighter's evasive roll to a lazy donkey rolling on the ground. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 격산타우 | **Striking the Ox Across the Mountain** | Palm technique that transmits force through an intervening defense. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 적혈십이도 | **Crimson Blood Twelve Sabers** | Pung Yang's domineering saber art; he has reached approximately seventy percent mastery. |
| 영단 흡수 | **Divine Pill Absorption** | System Quest created after Jin Taekyung takes the Blazing Flame Divine Pill. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 이름 없는 검 | **Unnamed Sword** | Oldest inventory item summoned when no item named 아무거나 can be found. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 완전 회복 | **Full Recovery** | Immediate Quest success reward that heals Taekyung's injuries. |
| 뛰어난 금창약 | **Superior Wound Medicine** | Quest reward used to treat external injuries. |
| 십년하수오 | **Ten-Year He Shouwu** | Quest reward used to treat internal injuries. |
| 어제의 적, 오늘의 동지 | **Yesterday's Enemy, Today's Ally** | Quest completed when Taekyung delivers Wikyung's invitation. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 운칠기삼 | **seven parts luck and three parts skill** | Established Korean saying used in Taekyung's reflection. |
| 운구기일 | **nine parts luck and one part qi** | Taekyung's playful variation on 운칠기삼. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 정양지부장 | **Jeongyang Branch Leader** | Leader of the Lower District Sect's Jeongyang Branch. |
| 혼주지부장 | **Honju Branch Leader** | Leader of the Lower District Sect's Honju Branch. |
| 총지부장 | **Chief Branch Leader** | Title Wolhwa holds within the Lower District Sect. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 진무보법 | **Jin Family's Manoeuvre Technique** | Named Jin Family footwork technique mastered by Taekyung. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 폭혈단 | **Blood-Exploding Pill** | Demonic Cult pill said to kill the user after its time limit. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 산서제일인 | **Shanxi's Number One** | Jin Wikyung's reputation for physical strength. |
| 금잔디 | **Geum Jandi** | Heroine of Boys Over Flowers, referenced in a sarcastic comparison. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 소음인 | **Soeumin** | One of the constitutional types in Sasang medicine. |
| 태양인 | **Taeyangin** | One of the constitutional types in Sasang medicine. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 화북 | **North China** | Regional designation used when discussing Shanxi drinking culture. |
| 산서제일가 | **foremost family in Shanxi** | Description of the Jin Family of Taiyuan's standing. |
| 장 노인 | **Old Man Jang** | Elderly villager who witnesses the Jin Family's arrival. |
| 현령 | **county magistrate** | County official who greets Jin Taekyung and delivers the City Lord's invitation. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 적토마 | **Red Hare** | Famous horse used in Hyuk Mujin's exaggerated comparison. |
| 여포 | **Lü Bu** | Historical warrior used in Hyuk Mujin's exaggerated comparison. |
| 성주의 초청 | **The City Lord's Invitation** | System Quest title. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 주씨 | **Zhu** | Surname of the imperial ruling house. |
| 친왕 | **Prince** | Imperial title held by the Shanxi City Lord. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 석칠 | **Seokchil** | Middle-aged porter with nearly twenty years of experience. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 송 표두 | **Escort Chief Song** | Unnamed person responsible for the escort run. |
| 연화봉 | **Lotus Peak** | Peak on Huashan from which Cheongpung recently fled. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 혁가 포목점 | **Hyuk Family Textile Shop** | Taiyuan textile shop owned by Hyuk Mujin's parents; the largest in Taiyuan, with branches in Henan and Hebei. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 메구미 | **Megumi** | Japanese name used in Taekyung's joke about the abbreviated dish name. |
| 산니백육 | **Garlic Pork** | Boiled pork sliced thin and served with garlic sauce. |
| 어향육사 | **Fish-Fragrant Shredded Pork** | Shredded pork dish. |
| 경장육사 | **Beijing Sauce Shredded Pork** | Shredded pork dish. |
| 규화계 | **Beggar's Chicken** | Named inn dish. |
| 매구 | **Maegu** | Waiter's shortened name for Maechae Guyuk. |
| 매채구육 | **Maechae Guyuk** | Pork belly with preserved mustard greens; the abbreviation is explained in a footnote. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 우 소협 | **Young Hero Woo** | Honorific address for Woo Jintae. |
| 황 소저 | **Young Lady Hwang** | Honorific address for an unidentified young woman who is the only daughter of a martial sect. |
| 혁 아우 | **Little Brother Hyuk** | Familiar address for an otherwise unnamed male scion who calls Woo Jintae hyung. |
| 국주님 | **Chief** | Honorific title for the head of an Escort Bureau. |
| 촉금 | **Shu brocade** | Fine brocade brought from Sichuan. |
| 삼도문 | **Samdo Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 궁귀문 | **Gunggui Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 성룡이 | **Seongryong** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 명화 | **Myeonghwa** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 소혜 | **Sohye** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 도동파 | **Dodong Sect** | Fabricated sect claimed by Taekyung when Woo Jintae demands his affiliation. |
| 천진반 | **Tien Shinhan** | Fabricated personal identity claimed by Taekyung. |
| 왕가장 | **Wang Family Estate** | Family estate whose heir is one of the Five Gates scions; he uses sabers rather than sword arts. |
| 왕 공자 | **Young Master Wang** | Heir of the Wang Family Estate. |
| 신 소저 | **Young Lady Shin** | Young woman described as the only daughter of a martial sect. |
| 정 소협 | **Young Hero Jeong** | Address for one injured Five Gates heir; his given name is not stated. |
| 갈 소협 | **Young Hero Gal** | Address for one injured Five Gates heir; his given name is not stated. |
| 석 모 | **Seok** | Self-identification by Honghwa Inn's chief steward; his given name is not stated. |
| 석 총관 | **Chief Steward Seok** | Title and surname form used for Honghwa Inn's chief steward. |
| 칠매검 | **Seven Plum Sword** | Sword art practiced by the unnamed martial official at eight-tenths mastery. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 정삼품 | **Third-Rank** | Official rank of the unnamed Assistant Military Commissioner. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 점소이 검신 되다 | **The Shop Assistant Becomes a Sword God** | Wuxia novel title read by Hyuk Mujin. |
| 아파야 무인이다 | **You Must Hurt to Become a Martial Artist** | Wuxia novel title read by Hyuk Mujin. |
| 무림의 아들 걸어서 구주팔황 세 바퀴 반 | **The Son of Murim Walks Three and a Half Rounds Around the Nine Provinces and Eight Wastes** | Wuxia novel title read by Hyuk Mujin. |
| 구주팔황 | **Nine Provinces and Eight Wastes** | Literary geographic phrase appearing in a wuxia novel title. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 이 첨사 | **Assistant Commissioner Li** | Address form for Li Feng |
| 홍 내관 | **Eunuch Hong** | Eunuch and Deputy Military Commissioner of Shanxi Province |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 도지휘사 | **Military Commissioner** | Provincial military commander's office |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 철혈문 | **Iron Blood Sect** | Henan sect mentioned by Gong Ilhyuk. |
| 오호검문 | **Five Tigers Sword Sect** | Henan sect mentioned by Gong Ilhyuk. |
| 태을미리장 | **Taeeul Miri Palm** | Palm technique taught to Cheongpung by Mae Jonghak. |
| 육합검 | **Six Harmonies Sword** | Huashan sword technique known by Cheongpung. |
| 매화검법 | **Plum Blossom Sword Technique** | Huashan sword technique Cheongpung performed at age ten. |
| 상청검 | **Supreme Clarity Sword** | Huashan sword technique listed among Cheongpung's knowledge. |
| 낙화추영장 | **Falling Flower Chasing Shadow Palm** | Huashan palm technique listed among Cheongpung's knowledge. |
| 산화무영수 | **Scattering Flowers Shadowless Hand** | Huashan hand technique listed among Cheongpung's knowledge. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 태사부 | **Grandmaster** | Huashan title referring to Mae Jonghak. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 근위대 | **royal guard** | Guard unit protecting Prince Shangshan. |
| 근위대 갑옷 세트 | **Royal Guard Armor Set** | Armor set Li Feng offers Cheongpung. |
| 황태자 | **Crown Prince** | The Emperor's older brother in Taekyung's recollection. |
| 고평문 | **Gopyeong Sect** | Minor sect whose young sect leader is pressured by Taekyung. |
| 고평지부 | **Gopyeong Branch** | Proposed branch designation under the Jin Family of Taiyuan. |
| 상산왕의 증표 | **Prince Shangshan's Token** | Golden medallion awarded by Zhu Bao as the Quest Reward. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 내관 | **palace attendant** | Hong Jin's former palace role; context identifies him as a eunuch. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 사서삼경 | **Four Books and Three Classics** | Confucian texts used to describe conventional scholarly learning. |
| 금성전장 | **Golden Star Exchange** | Financial institution that issued the thousand-nyang bank draft. |
| 전표 | **bank draft** | Negotiable draft used for the thousand-silver-nyang payment. |
| 은자 | **silver nyang** | Silver currency unit. |
| 철전 | **iron coins** | Lower-value coin currency used to compare the payment's value. |
| 은원보 | **silver yuanbao** | Small silver ingot given to Taekyung as pocket money. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 성군 | **sage king** | Desired form of rulership proclaimed for Prince Shangshan. |
| 대태원진가 | **great Jin Family of Taiyuan** | Formal exalted reference to the Jin Family of Taiyuan. |
| 평양 | **Pyongyang** | City invoked in Taekyung's communist-atmosphere joke. |
| 천하제일인 | **greatest under heaven** | Superlative martial distinction used in Hong Jin and Jin Wikyung's banter. |
| 고금제일인 | **greatest of all time** | Superlative martial distinction used in Hong Jin's exaggerated praise. |
| 비무행 | **dueling tour** | Cheongpung's planned journey to challenge the Ten Dragons and Phoenixes. |
| 청강검 | **blue-steel sword** | Cheongpung's sword. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 최 팀장 | guild_member_to_team_leader | Team Leader | deferential | Taekyung addresses Choi as 팀장님. |
| 최 팀장 | 진태경 | team_leader_to_guild_member | Taekyung | formal-but-familiar | Choi addresses him as 태경 씨. |
| 진태경 | 김 집사 | client_to_butler | Butler Kim | formal-deferential | Taekyung addresses him as 김 집사님. |
| 최 팀장 | 김 집사 | employer_to_butler | Butler Kim | formal-polite | Choi addresses him as 김 집사님. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter | deferential | Butler Kim refers to Taekyung as 헌터님. |
| 임꺽정 | 송 양 | older_guild_member_to_younger_female_guild_member | Miss Song | hearty-casual | Im Kkeokjeong calls her 송 양. |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 진태경 | 김 집사 | junior_to_senior_Hunter | Senior | deferential | After learning that Butler Kim trained at the same Nonsan regiment and battalion, Taekyung addresses him as 선배님. |
| 김 집사 | 최 팀장 | butler_to_employer | Young Master | deferential | Butler Kim addresses Choi as 도련님 when agreeing to follow his decision about Guild titles. |
| 임창수 | 혜린 | sponsor_to_sponsored_lover | Hye-rin | condescending-casual | Changsoo refers to himself as this oppa while claiming he will protect her. |
| 최 팀장 | 임꺽정 | guild_team_leader_to_guild_member | Hunter Im | formal-polite | Choi addresses Kkeokjeong as 임 헌터님 while telling him to put on the equipment. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임창수 | 송송이 | rival_guild_team_leader_to_guild_member | Miss Song | mock-polite | Uses 송송이 씨 while proposing that Song Song join Sangdong Guild. |
| 송송이 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo—no, Im Changsoo | blunt but polite | Insults Changsoo with 씹창 and then corrects herself to his proper name while rejecting him. |
| 송송이 | 김 집사 | guild_member_to_guild_master | Guild Master | formal-polite | Requests the Guild Master’s permission before changing Guilds under the wager. |
| 송송이 | 최 팀장 | guild_member_to_team_leader | Team Leader | formal-polite | Asks Choi whether he accepts her possible Guild transfer if the bet is lost. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 김 집사 | 임창수 | guild_master_to_rival_guild_member | Changsoo | mock-polite | Butler Kim uses 창수 씨 while accusing Changsoo of refusing to pay. |
| 지점장 | 임춘수 | bank_branch_manager_to_guild_master | Guild Master | formal-deferential | The K Bank branch manager addresses Im Chunsoo as 길드장님 while reporting Changsoo's transfer. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 김정희 | 사장님 | employee_to_restaurant_owner | Boss | formal-polite, becoming firm | Uses the owner's title while demanding an apology and defending Taekyung. |
| 사장님 | 김정희 | restaurant_owner_to_employee | Ajumma | condescending-casual | Repeatedly uses 아줌마 while berating Kim Jeonghee. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 부동산 아저씨 | 진태경 | real_estate_agent_to_customer | Boss | polite and sales-friendly | The unnamed real estate agent repeatedly addresses Taekyung as 사장님 while arranging a house viewing. |
| 여자 친구 | 박지훈 | girlfriend_to_boyfriend | Oppa | casual-familiar | Jihoon's girlfriend addresses him as 오빠 while asking him to return to the car. |
| 임춘수 | 1팀장 | guild_master_to_team_leader | Team 1 Leader | blunt-commanding | Chunsoo addresses him with a rough 야 while issuing orders and demanding his candid assessment. |
| 1팀장 | 임춘수 | guild_team_leader_to_guild_master | Guild Master | formal-deferential | The Team 1 Leader consistently addresses Chunsoo as 길드장님 while reporting and accepting orders. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 동료 | 김준수 | Security Team colleague | Junsu | casual-collegial | Uses 준수야 while checking whether Junsu pulled an all-nighter. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 김권동 | 보안팀장 | subordinate_to_team_leader | Team Leader | deferential | Uses 팀장님 over the radio while reporting on the disguised approach. |
| 보안팀장 | 1번 | supervisor_to_surveillance_agent | Number One | command-radio | Uses the operative’s radio call sign while directing the real-estate-office surveillance. |
| 보안팀장 | 2번 | supervisor_to_surveillance_agent | Number Two | command-radio | Uses the operative’s radio call sign while ordering continued observation. |
| 부동산 아줌마 | 진태경 | real_estate_agent_to_customer | Boss; young bachelor | chatty-polite and flirtatious | The agent calls Taekyung 사장님 and 총각 while offering listings and commenting on his appearance. |
| 김권동 | 진태경 | surveillance_hunter_to_target | young man | friendly and polite | Gwondong maintains his ordinary-neighbor disguise and addresses Taekyung as a younger local acquaintance. |
| 진하연 | 여름이 | caretaker_to_kitten | Yeoreum | affectionate-casual | Hayeon repeatedly calls the kitten by name and refers to herself as Sis. |
| 김권동 | 김준수 | Security Team colleagues | Junsu | casual-collegial | Gwondong uses 진수야 while questioning Junsu’s interpretation of the item. |
| 보안팀장 | 김권동 | team_leader_to_subordinate | Gwondong | blunt-commanding | Uses 권동아 while directing the operation. |
| 진태경 | 최병일 | target_to_attacking_team_leader | Mr. Choi Byungil | mock-polite and taunting | Uses 최병일 씨 while baiting and confronting him. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |
| 임춘수 | 진태경 | guild_master_to_younger_rival | you | blunt-but-familiar | Repeatedly uses 자네 while challenging and testing Taekyung. |
| 김화종 | 임춘수 | familiar_mage_to_guild_master | Chunsoo | gentle-and-familiar | Addresses Im Chunsoo as 춘수 on arriving at the hiking-trail entrance. |
| 임춘수 | 김화종 | former_trainee_to_former_instructor | Instructor | deferential and fearful | Im Chunsoo addresses Hwajong as 교관님 after recognizing his former instructor. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 1팀장 | 보안팀장 | guild_team_leader_to_security_team_leader | Security Team Leader | formal-commanding | Team Leader 1 directly addresses the Security Team Leader while warning him about discipline. |
| 보안팀장 | 1팀장 | security_team_leader_to_guild_team_leader | Team Leader 1 | formal-deferential | The Security Team Leader addresses Team Leader 1 as 팀장님 while reporting what he heard. |
| 진태경 | 기사님 | customer_to_moving_driver | Driver | polite | Taekyung addresses the private moving-truck driver by his occupational title on the phone. |
| 이삿짐 아저씨 | 진태경 | moving_driver_to_customer | Mr. Jin Taekyung; Boss | friendly-polite | The driver uses 진태경 씨 on the phone and 사장님 while insisting on moving the capsule. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 오색귀 | 진태경 | former_bandit_associates_to_prior_benefactor | Boss | pleading and deferential | The Five-Colored Ghosts repeatedly call Taekyung 대형 while begging him to rescue them. |
| 월화 | 춘삼 | Lower District Sect branch leader to subordinate | Chunsam | commanding-familiar | Uses 춘삼아 while directing him to execute the interrogation order. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 소월 | 철검대주 | sect_leader_to_subordinate | Iron Sword Squad Leader | formal-commanding | Lee Seowol addresses him while issuing her final instruction about her title. |
| 소월 | 수문각주 | sect_leader_to_subordinate | Master of the Gatekeeper Pavilion | formal-commanding | Lee Seowol addresses him while asserting her authority as Sect Leader. |
| 사자 | 이소월 | enemy_envoy_to_sect_leader | Sect Leader | mock-formal | The Red Wind Band envoy addresses Lee Seowol as 문주님 while delivering the coercive marriage-or-destruction ultimatum. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 월화 | 철무백 | ally_to_injured_master | Sir Cheol | polite and reassuring | Wolhwa addresses the critically wounded Cheol while administering temporary medicine and asking about his attacker. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 월화 | 혼주지부장 | chief_branch_leader_to_subordinate_branch_leader | Honju Branch Leader | formal-commanding | Wolhwa addresses him by branch title while directing rumor operations. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 혁무진 | 이소월 | subordinate_to_sect_leader | Sect Leader | deferential and exuberant | Formally praises the Sect Leader while greeting her. |
| 혁무진 | 철무백 | junior_to_respected_Peak_master | Great Hero Cheol | deferential | Begins a formal greeting with 철무백 대협 before being stopped. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 하오문도 | 진위경 | informant_to_lesser_family_head | Lesser Family Head | deferential | Uses 소가주님 while correcting Wikyung's misunderstanding about Mukyung's condition. |
| 현령 | 진태경 | county_official_to_celebrated_martial_artist | Great Hero Jin | formal-polite and admiring | Uses 진 대협 while praising Taekyung's alleged exploits. |
| 진태경 | 현령 | martial_artist_to_county_official | County Magistrate | polite and lightly sarcastic | Uses 현령님 while explaining that the Lesser Family Head cannot receive visitors. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 현령 | 진위경 | county_official_to_lesser_family_head | Lesser Family Head | formal-polite and deferential | Uses 진 소가주님 when asking Taekyung to convey his regards. |
| 현령 | 진무경 | county_official_to_renowned_martial_artist | Heaven Shaking Sword | formal-polite and respectful | Uses 진천검 when asking Taekyung to convey his regards. |
| 동료 쟁자수 | 석칠 | junior_colleague_to_senior_colleague | Hyung | casual-but-respectful | Calls Seokchil 형님 while inviting him to the fire and restraining him. |
| 석칠 | 동료 쟁자수 | senior_colleague_to_junior_colleague | Brat | gruff-casual | Uses 이놈아 while bantering with his fellow porter. |
| 동료 쟁자수 | 청풍 | senior_colleague_to_newcomer | Rookie | casual | Calls Cheongpung 신참. |
| 혁무진 | 아주머니 | childhood_benefactor_to_former_child | Auntie | deferential-polite | Mujin respectfully addresses the local snack-stall vendor who secretly gave him candied hawthorn when he was a child. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 우진태 | 황 소저 | host_to_five_gates_scion | Young Lady Hwang | polite and flirtatious | Woo Jintae presents Shu brocade as a gift while implying personal feelings, then retreats behind a joke. |
| 우진태 | 혁 아우 | older_friendly_sc ion_to_younger_sc ion | Little Brother Hyuk | familiar and patronizing | Woo Jintae promises the male scion an especially impressive gift. |
| 혁 아우 | 우진태 | younger_sc ion_to_older_friendly_sc ion | hyung | familiar and deferential | The scion calls Woo Jintae hyung after they have become close enough to use fraternal terms. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 우진태 | enemy_to_enemy | you / you bastard | insulting-casual | Taekyung repeatedly addresses Woo Jintae with hostile informal forms while demanding an apology and slapping him. |
| 우진태 | 진태경 | enemy_to_enemy | you / little bastard | condescending and enraged | Woo Jintae uses hostile forms such as 네놈, 애새끼, and 어린놈 while trying to intimidate Taekyung. |
| 갈 소협 | 정 소협 | fellow_Five_Gates_heir | Young Hero Jeong | formal-polite | The unnamed heir addresses the other injured heir by surname and honorific. |
| 정 소협 | 갈 소협 | fellow_Five_Gates_heir | Young Hero Gal | formal-polite | The unnamed heir responds using the other injured heir's surname and honorific. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 홍 내관 | 이풍 | political_rivals | Assistant Commissioner Li | mock-friendly and probing | Uses 우리 이 첨사 and a superficially familiar tone while testing and provoking Li Feng. |
| 이풍 | 홍 내관 | political_rivals | Eunuch Hong / Deputy Military Commissioner | formal but sarcastic | Alternates between the official title and Eunuch Hong to mock his demand for familiarity. |
| 공일혁 | 이풍 | martial_rivals | Li Feng of Huashan | casual and taunting | Mocks Li Feng's office and recalls his defeat at Huashan ten years earlier. |
| 이풍 | 공일혁 | martial_rivals | you bastard | hostile and furious | Responds to Gong Ilhyuk's insult toward Huashan with an openly aggressive form. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 공일혁 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | condescending and dismissive | Uses 후배님 while ordering Taekyung to move aside. |
| 진태경 | 공일혁 | junior_martial_artist_to_senior_martial_artist | Senior | polite but firm | Uses 선배님 while intervening on Cheongpung's behalf. |
| 공일혁 | 청풍 | senior_martial_artist_to_junior_martial_artist | Junior | impatient and condescending | Treats Cheongpung as a junior while demanding his introduction. |
| 청풍 | 공일혁 | junior_martial_artist_to_senior_martial_artist | Senior | deferential and apologetic | Uses 선배님 while apologizing for catching Ilhyuk's wrist. |
| 이풍 | 진태경 | senior_official_to_respected_young_martial_artist | Young Hero Jin | formal and respectful | Addresses Taekyung as 진 소협 after praising his reputation. |
| 공일혁 | 홍진 | junior_official_guest_to_senior_official | Deputy Military Commissioner | formal and deferential | Appeals to Hong Jin for his view on the impending disturbance. |
| 이풍 | 청풍 | Huashan lay disciple to martial uncle | Young Hero; Martial Uncle Cheongpung | formal and reverent | Li Feng initially addresses Cheongpung as 소협 while testing his knowledge, then recognizes him as 사숙 after witnessing his Huashan sword technique. |
| 홍진 | 공일혁 | political_host_to_guest | Great Hero Gong | polite but cutting | Hong Jin uses the respectful title while dismissing Gong Ilhyuk and exposing his poor judgment. |
| 청풍 | 이풍 | Martial Uncle to Martial Nephew | Martial Nephew Li Feng | exuberant and deferential | Cheongpung adopts the address to obtain royal-guard armor and weapons. |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 진태경 | 이풍 | junior_to_respected_official_and_martial_ally | Great Hero Li | polite and respectful | Agrees with Li Feng's proposal that Zhu Bao visit the Jin Family's banquet. |
| 이풍 | 주표 | official_to_prince | Your Highness | formal-deferential | Suggests that Zhu Bao visit the Jin Family's grand banquet in fifteen days. |
| 주표 | 청풍 | prince_to_young_martial_artist | you | formal and gatekeeping | Refuses Cheongpung's autograph until he acquires a martial title. |
| 홍진 | 청풍 | political_official_to_young_martial_artist | Young Master | formal and curious | Uses 공자께서는 while asking whether Cheongpung has always lived on Huashan. |
| 전령 | 진위경 | military messenger to Lesser Family Head | Lesser Family Head | formal-polite and deferential | Uses 소가주님 when confirming Wikyung's identity. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 진위경 | 홍진 | political_host_to_deputy_military_commissioner | Comrade Hong | formal-polite and playful | Jin Wikyung adopts Hong Jin's requested casual address, 홍 동지. |
| 홍진 | 진위경 | deputy_military_commissioner_to_lesser_family_head | Lesser Family Head Jin | formal and teasing | Hong Jin addresses Jin Wikyung as 진 소가주님 while flattering and joking with him. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |

## Exact glossary matches

| 무림     | **Murim**          |
| 백무성    | **Baek Museong**   |
| 철우     | **Chulwoo**        |
| 은향     | **Eunhyang**       |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 화산파    | **Huashan**                      |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 사파     | **unorthodox faction**                           |                                                       |
| 장문인    | **Sect Leader**                              |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 생도     | **cadet**                                    |
| 산서     | **Shanxi**             |
| 화산     | **Huashan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 도사      | **Daoist**                                                      |
| 대사      | **Master** for a senior Buddhist monk                           |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 연화봉 | **Lotus Peak** | Peak on Huashan from which Cheongpung recently fled. |
| 태사부 | **Grandmaster** | Huashan title referring to Mae Jonghak. |
| 은자 | **silver nyang** | Silver currency unit. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 148
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; the grandson and disciple of Sword Saint Mae Jonghak, who secretly descended from Huashan to seek out and defeat the Ten Dragons and Phoenixes, beginning with Jin Mukyung; he has no martial title yet, and Prince Shangshan will only accept his autograph after he gains one
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, and a martial artist's competitive pride
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak, the Sword Saint, is his grandfather and martial instructor; Cheongpung came to Huashan at about age three or four rather than being born there, lived with Mae Jonghak at a hidden residence, and secretly left Huashan without his grandfather's knowledge to challenge the Ten Dragons and Phoenixes; Li Feng is his Martial Nephew within Huashan's hierarchy; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 148
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather; remained in deep seclusion at a hidden residence on Huashan
- **Personality:** Not established in this chapter.
- **Voice:** Not established in this chapter.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm.

## Korean source

```text
＃149화



서안(西安)의 역사는 깊다. 왕조가 바뀌기 전까지 수백 년간 천하의 중심이라 불렸다.

수많은 인구, 평야와 광산으로부터 생산되는 풍부한 자원. 그리고 세월에 휩쓸려 간 세 개의 통일 왕조가 남긴 명승고적(名勝古跡)들은 아직도 수많은 이들이 서안을 찾는 이유다.

시끌벅적한 서안의 한 객잔. 두툼한 모피 옷을 걸친 두 유생도 그런 이들 중 하나였다.

“자, 서두르세. 해가 떨어지기 전까지 객잔으로 돌아오려면 시간이 빠듯해.”

의욕이 넘치는 친구와는 달리 다른 유생은 질린 얼굴로 고개를 저었다.

“또?”

“또라니. 그게 무슨 뜻인가?”

“오늘은 이만 쉬면 안 되겠나? 며칠째 돌아다녔더니 다리가 부러질 것 같아서 그래.”

“이 친구 엄살은. 천릿길을 걸어서 왔는데 어떻게 그냥 돌아가? 우리 나이에 다시 서안에 올 일이 있을 성싶은가?”

“어이고, 서안 구경하다가 북망산 구경하게 생겼네. 나 좀 내버려 둬.”

“어허, 다른 곳은 몰라도 서악(西岳)은 들러야지. 그 절경을 놓치면 죽을 때까지 후회할 거야.”

“서악이라…….”

천하에서 손꼽히는 다섯 개의 명산을 가리켜 오악(五岳)이라 한다.

그중 서악은 서안에서 가까운 화산(華山)을 가리키는 말이었다.

“화산에 올라 천하를 내려다보면 어떤 기분일지 생각해 보게. 상상만으로도 호연지기가 솟구치지 않나?”

“그건…… 그렇지.”

열의에 찬 설득에 유생은 마지못해 고개를 끄덕였다.

화산이 그 험준함만큼이나 아름다운 절경으로 유명하다는 것은 그도 익히 알고 있는 사실이었으니까.

“명산이 괜히 명산이겠나? 이번에 영험한 기운을 잔뜩 받아 가야 다음 과거 때 좋은 소식이 있지. 자네가 낙방한 것만 벌써 몇 번짼가?”

“갑자기 그 얘기가 왜 나와!”

“이 사람 성내기는. 아무튼, 화산에 가서 호연지기도 받고 영기도 받자. 뭐 그런 말이지.”

그가 여전히 망설이는 기색이자, 유생이 은근한 목소리로 덧붙였다.

“다른 곳까지 들르자는 말은 안 하겠네. 화산의 연화봉(蓮花峰)만 찍고 바로 내려오세.”

이쯤 되니 완강히 버티던 유생도 마음이 동했다. 혹시 누가 아는가, 정말 내년에 과거에 떡하니 붙을지도.

하지만 한 가지 소문이 마음에 걸렸다.

“한데 내 듣자 하니 화산에는 무림인들이 득실거린다던데…….”

“화산파 도사들을 말하는 거라면 괜찮네. 석년에 내 지인이 한 번 다녀온 적이 있는데 아무 문제도 없었다더군.”

“커흠. 그럼 한번 가 볼까?”

못 이긴 척 자리에서 일어나려던 유생이 순간 중심을 잃고 비틀거렸다. 아까부터 후들거리던 다리에 힘이 쫙 풀린 것이다.

자칫하면 주위에 널린 탁자 모서리에 뒤통수가 찍힐 상황.

“어, 어어!”

외마디 비명과 함께 쓰러지려는 찰나, 거칠고 단단한 손바닥이 유생의 등을 받쳤다.

“으, 으헉. 겨우 살았네.”

겨우 신형을 바로 한 유생이 안도의 한숨과 함께 손의 주인을 바라봤다.

서른쯤 되었을까? 평범한 인상에 흰 도포를 입은 청년이 부드럽게 웃어 보였다.

“괜찮으십니까?”

“고, 고맙소.”

“별말씀을요.”

간신히 위기를 모면한 유생은 신기하다는 눈빛으로 청년을 바라봤다.

‘평범해 보이는데.’

어중간한 신장에 늘씬해 보이는 몸이다. 한데 수십 근이나 더 나갈 자신의 몸을 한 손으로 받치다니.

혹 무림인인가 싶어 옆구리를 살펴봤지만 휑한 것으로 봐서 그건 아닌 듯싶다.

‘보기와는 달리 힘이 장사구먼.’

어쨌건 덕분에 살았다. 옛 성현들이 말씀하시길 은혜를 갚는 것이 사람의 도리라고 했다.

“다시 한번 고맙소. 공자 덕분에 낭패를 면했구려.”

“해야 할 일을 한 것이니 신경 쓰지 않으셔도 됩니다.”

“큰 도움을 받았는데 어찌 말 몇 마디로 끝내겠소? 이럴 게 아니라 내 한턱 낼 테니 합석하시구려.”

그러자 동료 유생이 황당한 듯한 얼굴로 끼어들었다.

“그게 무슨 소린가? 화산은? 연화봉은 어쩌고?”

“방금 골로 갈 뻔한 거 못 봤나? 이건 객잔에서 쉬라는 징조야. 그리고 여기 계신 공자가 날 구해 줬으니 은혜는 갚아야지. 안 그렇소?”

청년은 웃으며 손을 내저었다.

“전 정말 괜찮습니다. 기다리는 일행도 있고요.”

“일행이라니? 아까부터 보아하니 한 시진이 넘게 혼자 있던 것 같은데.”

“하하, 일이 있어 늦어지는 모양입니다. 기다리는 수밖에요.”

한 시진을 넘게 있었는데도 계속 기다리겠다고? 생긴 것만큼이나 속 좋은 놈이다.

그렇다고 일행이 있다는데 막무가내로 합석하자고 할 수도 없는 일. 유생은 아쉬운 듯이 입맛을 다셨다.

“그럼 어쩔 수 없지. 사는 동안 가내 두루 평안하시고, 무병장수하길 바라겠소.”

“화산! 연화봉!”

“아, 지금 갈 테니까 거 유별난 주둥이 좀 닫아 보게.”

“역시, 난 자네를 믿었어.”

“확 그냥, 연화봉 정상에서 밀어 버릴까 보다.”

일행을 향해 눈을 부라린 유생이 막 걸음을 떼려던 찰나였다.

쾅!

모골이 송연해지는 굉음. 객잔 문이 박살 나더니 우렁찬 외침과 함께 일남일녀가 모습을 드러냈다.

“저희 왔습니다!”

“은향이도 왔어요!”

그들을 바라본 객잔 안의 손님들이 하나같이 입을 딱 벌렸다.

사내의 엄청난 체격에, 그리고 아리따운 소녀의 미모에 놀란 탓이었다.

‘저건 무슨 조합이야.’

‘세상에, 살다 살다 저리 큰 사람은 처음 보네.’

순간 침묵에 잠긴 객잔 안, 유일하게 놀라지 않은 한 사람이 입을 열었다. 앞서 유생을 도운 평범한 인상의 청년이었다.

“늦었구나.”

남들보다 머리통 몇 개는 더 큰 사내가 머리를 벅벅 긁었다.

“죄송합니다. 오는 길에 작은 시비가 붙어서 그만.”

“무슨 일이길래 한 시진이냐 늦었느냐?”

“저어, 그게…….”

사내가 우물쭈물하자 자신을 은향이라 밝힌 소녀가 씩 웃으며 끼어들었다.

“큰 오라버니, 혹시 흑사파라고 들어 보셨어요?”

“흑사파? 글쎄다. 이름만 들어서는 썩 좋은 일을 할 것 같진 않구나.”

“맞아요. 요 앞에서 투전판을 관리하는 흑도 무리인데, 거기 두목이라는 자가 철우 오라버니를 보더니 같이 일해 볼 생각 없냐고…… 읍! 읍읍!”

“아닙니다. 아니라고요! 제가 얼마나 순박하게 생겼는데!”

철우라는 사내가 은향의 입을 막고 항변했지만, 객잔 안의 누구도 그의 말을 믿지 않았다.

‘생긴 것 봐라. 저 얼굴이면 이미 흑도지.’

‘내가 흑사파 두목이었어도 말 꺼내 봤다.’

‘저 정도면 영입 일 순위야. 일 순위.’

다들 마음속으로만 중얼거린 이유는 철우가 눈을 부릅뜨고 사방을 노려봤기 때문이다. 성난 맹수의 눈빛에 사람들은 침만 꼴깍 삼켰다.

물론 이번에도 한 사람만큼은 예외였다.

“그래서, 어떻게 되었느냐?”

청년의 물음에 철우가 냉큼 대답했다.

“그냥 일없다 하고 돌려보냈습니다.”

“사실이냐?”

철우가 슬그머니 시선을 피하며 대답했다.

“사, 사실입니다.”

“주먹에 피가 묻어 있구나.”

“헉. 정말입니까? 분명히 닦았는데!”

“…….”

“…….”

“읍. 읍!”

청년이 한숨을 푹 내쉬었다.

“은향이부터 놔주거라.”

“……옙.”

“읍, 푸하!”

간신히 풀려난 은향이 얼굴을 잔뜩 찡그리며 침을 퉤퉤 뱉었다.

“으, 짜. 오라버니 손 언제 씻었어요?”

“어제.”

“뭐야, 어제오늘 동안 측간에 다녀오는 것만 다섯 번은 본 것 같은데. 그럼…… 아악!”

“괜찮아. 난 보름에 한 번 씻어도 향기 나.”

“미쳤나 봐, 저러니까 여자들이 싫어하지.”

“뭣이!”

으르렁거리는 그들의 모습을 보던 청년이 피곤한 듯 눈가를 문질렀다.

사문에서도 골칫덩이로 악명 높은 두 사람이다. 언젠간 이런 상황이 올 거라고는 생각했지만 서안을 빠져나가기도 전에 벌써 사고를 칠 줄은 몰랐다.

‘장문인의 명이니 거절할 수도 없고.’

어쩌겠나. 이게 다 자신의 업보이려니 생각하는 수밖에.

벌써부터 반쯤 기가 빨린 그가 입을 열었다.

“둘 다 돌아가고 싶은 것이냐? 장문인께 말씀드려서 면벽 수련이라도 시켜 줘야 정신을 차리겠어?”

“헉, 아닙니다.”

“저도 괜찮아요. 큰 오라버니.”

청년이 짐짓 얼굴을 굳혔다.

“어허. 큰 오라버니가 아니라 대사형이다.”

“네, 큰 오라버니.”

“은향이 너…… 휴우, 아니다.”

“헤헤.”

미인의 웃음이란 얼마나 위력적인가. 은향이 배시시 웃자 방금까지만 하더라도 싸늘하던 객잔의 공기가 훈훈해졌다.

눈치만 살피고 있던 객잔 주인이 다가온 것은 그때였다.

“저어, 나으리들.”

주인장을 알아본 청년이 미안한 얼굴로 말했다.

“아, 소란을 피워 죄송합니다. 지금 바로 나가겠습니다.”

“아뇨. 그게 아니라…….”

잔뜩 겁에 질린 눈빛으로 철우를 힐끔거린 그가 힘겹게 말을 이었다.

“배상을, 좀.”

“아.”

그제야 박살 난 문이 눈에 들어온다. 청년이 재차 한숨을 내쉬자 철우가 묵직한 전낭에서 잽싸게 은자를 꺼내 들었다.

“이거면 충분할 거요.”

“이 은자는 어디서 났느냐?”

은향이 생글생글 웃으며 대답했다.

“흑사파요.”

철우가 기겁해서 외쳤다.

“야!”

“왜요, 난 잘못 없는데?”

“너도 옥비녀 챙겼잖아!”

“앗. 어떻게 알았지?”

“…….”

흑사파를 박살 낸 걸로도 모자라 재물까지 싹 다 털어 온 모양이다. 청년은 이마가 지끈거렸다.

“당장 돌려주어라.”

“대사형, 놈들이 갖고 있어 봤자 악행에나 쓰일 재물입니다.”

“맞아요. 이왕 이렇게 된 거 목적지까지 가는 동안 맛있는 것도 먹고…….”

청년이 엄격한 목소리로 두 사람의 말을 끊었다.

“언제부터 투전판 관리가 악행이 되었느냐? 아니면 직접 네 눈으로 목도한 적이 있느냐?”

“안 봐도 뻔합니다. 흑도잖습니까.”

“이 넓은 무림에 어찌 한 가지 색만 있겠느냐. 그리고 흑사파가 정말 악적들이라면 진작 본산에서 조치를 취했을 것이다.”

“그건…….”

“시끄럽다. 갈 길이 바쁘니 재물은 여기에 맡기고 간다. 그리 해도 괜찮겠습니까, 주인장?”

이제는 객잔 안의 모든 사람이 안다. 이들이 무림인이며 서안의 흑도 세력과 원한을 맺었다는 사실을.

무림인과 얽히는 걸 극도로 꺼리는 주인장은 똥 밟은 표정이었다.

“대, 대협. 송구합니다만 저 같은 늙은이가 감당할 수 있는 일이 아닙니다.”

땀 흘린 노동의 대가를 잃게 된 철우가 퉁명스럽게 말을 던졌다.

“걱정 마시오. 별일 없을 테니.”

“지금 당장은 몰라도 여러분들이 떠나시면 저는 큰일이 납니다요.”

“어허, 그럴 일 없다니까. 우리가 떠나도 주인장의 털끝 하나 못 건드릴 거요.”

“아니 그게 그렇게 쉽게 말씀하실 일이 아니라니까요.”

머리까지 근육으로 뭉친 놈인지 생각이 더럽게 짧다.

주인장이 차마 그렇게 말은 못 하고 냉가슴만 앓던 그때, 청년이 담담하게 웃었다.

“그들이 오거든 이 전낭과 함께 한마디만 전해 주시면 됩니다.”

“아니, 대협들. 지금 이해를 못 하시는 것 같은데…….”

주인장의 말은 곧바로 이어진 청년의 목소리에 뚝 끊겼다.

“화산파의 일대제자 백무성이 사제들의 실수를 대신 사과한다고요.”

순간 객잔 안이 침묵에 잠겼다.

화산파, 세 글자가 주는 위압감도 위압감이었지만 어디선가 한 번쯤 들어 본 듯한 청년의 이름 때문이었다.

“화산파의 백무성이라고?”

“백무성, 백무성…… 잠깐. 혹시?”

화산파의 앞마당이나 다름없는 서안이다. 무림에 관심이 많은 몇몇 호사가들이 청년의 정체를 깨닫는 데까지는 그리 오랜 시간이 걸리지 않았다.

“화산일학(華山一鶴) 백무성!”

한 마리 학처럼 고고한 품행을 지녔다고 해서 붙여진 별호.

이미 화산파 입문 당시부터 뛰어난 기재로 알려진 그에게는 또 다른 별호가 있었다.

“화산일학이라면 매화삼절(梅花三晣)의 첫째 아닌가!”

현 화산파 장문인은 세 명의 제자를 두어 하나같이 뛰어난 고수로 성장시켰다.

그런 그들이 화산파의 자부심이라 할 수 있는 매화검수(梅花劍手)에 임명된 것은 당연했고, 이내 두각을 드러냈다.

“듣자 하니 그중 여인이 한 명 있다고 들었는데…… 그럼 저들이?”

“말해서 뭣하나. 아까 화산일학에게 대사형이라고 부르는 거 못 들었어?”

“허어, 살다 보니 이런 곳에서 매화삼절을 다 보는군.”

곳곳에서 터져 나오는 탄성을 모른 척하며 백무성이 입을 열었다.

“어떻게 안 되겠습니까?”

주인장이 비장한 얼굴로 대답했다.

“제 목숨을 걸고 이 재물을 흑사파에게 돌려주겠습니다. 존명!”

“…….”



* * *



“아, 맞다.”

백무성의 중얼거림에 두 사제가 고개를 돌렸다.

“왜 그러십니까, 대사형?”

“뭐 놓고 온 물건이라도 있어요?”

백무성이 고개를 저었다.

“화산이 봉쇄되었다는 사실을 말해 주는 걸 깜빡했다.”

“누구한테요?”

“이름은 모르겠구나. 그 사람, 아픈 다리를 이끌고 헛걸음을 하게 생겼어.”

은향이 딱하다는 듯 혀를 찼다.

“저런. 앞으로 몇 달은 어림도 없을 텐데.”

“그러게 말이다.”

그들은 며칠 전 화산파 전체를 발칵 뒤집어 놓은 사건을 떠올렸다.

장문인, 그러니까 자신들의 사부가 잠든 사이 침입자가 쥐도 새도 모르게 다녀간 것이다.

그는 대담무쌍하게도 화산파 장문인의 머리맡에 비수 한 자루와 친필 서신을 남기는 기행을 저질렀다.



[잠시 바람 좀 쐬고 오마. 너는 장문인 됐다고 놀지 말고 잠잘 시간에 무공 수련 좀 해라.]



평소 같았다면 즉시 천라지망을 펼쳤겠지만, 침입자의 정체가 검성 매종학이라면 이야기가 달라진다.

장문인은 즉시 화산을 굳게 걸어 잠그고 검성의 은거지를 찾으라 지시했고, 수색은 지금까지 이어지고 있었다.

“태사부님도 참. 대단하신 분이네요.”

“말만 들었지. 나도 이 정도이실 줄은 몰랐다.”

“전서가 오지 않았다면 저희도 꼼짝없이 화산을 뒤지고 있었을 겁니다.”

그 와중에 산서성에서 날아든 전서구는 구원의 빛이었다.

화산파 수뇌부는 고심 끝에 매화삼절이라는 걸출한 인재들을 파견하기로 결정했다.

“그런데 그 청풍이라는 사람. 대사형은 만나 보신 적 있으십니까?”

“그래, 십 년 전에 한 번.”

검성 매종학이 자식처럼, 손자처럼 키운 제자.

십 년 전 그 자리에는 그도 있었다. 화산일학 백무성의 눈빛이 반짝였다.

“기대되는구나. 어찌 성장했을지.”
```

## Final English reading copy

```markdown
# Chapter 149

Xi’an’s history ran deep. Until the dynasties changed, it had been called the center of all under heaven for hundreds of years.

Its enormous population. Its abundant resources, produced by the plains and mines. And the famous scenic and historic sites left behind by three unified dynasties swept away by the passage of time. Those were still the reasons so many people visited Xi’an.

In one of Xi’an’s bustling inns, two Confucian scholars dressed in thick fur coats were among those visitors.

“Come on, hurry up. If we want to get back to the inn before sunset, we’re running out of time.”

Unlike his enthusiastic friend, the other scholar shook his head with a thoroughly fed-up expression.

“Again?”

“What do you mean, again?”

“Can’t we just rest for today? We’ve been walking around for days, and my legs feel like they’re about to break.”

“Don’t be such a baby. We walked a thousand li to get here—how can we just turn around and go back? Do you really think we’ll have another chance to come to Xi’an at our age?”

“Good grief. I came to sightsee in Xi’an, and now it looks like I’m going to end up sightseeing Mount Beimang.[^1] Leave me alone.”

[^1]: Mount Beimang is traditionally associated with burial grounds and death.

“Come now. I don’t know about the other places, but we absolutely have to visit Western Peak. You’ll regret it until the day you die if you miss such a magnificent sight.”

“Western Peak…”

The five most famous mountains in all under heaven were called the Five Great Mountains.

Western Peak referred to Huashan, which lay near Xi’an.

“Imagine how it would feel to climb Huashan and look down upon all under heaven. Doesn’t your lofty spirit surge just thinking about it?”

“Well… I suppose it does.”

Unable to resist his friend’s fervent persuasion, the scholar reluctantly nodded.

He was well aware that Huashan was famous not only for its ruggedness but also for its beautiful scenery.

“Do you think a famous mountain became famous for no reason? We need to soak up plenty of its spiritually efficacious energy this time if we want good news at the next civil service examination. How many times have you already failed?”

“Why are you bringing that up all of a sudden?”

“Don’t get angry. Anyway, we’ll go to Huashan, receive some lofty spirit, receive some spiritual energy, and that’ll be that.”

When the scholar still looked hesitant, his friend added in a coaxing voice,

“I won’t ask you to visit anywhere else. We’ll just stop at Lotus Peak and come straight back down.”

At that, even the scholar who had been stubbornly resisting began to waver. Who knew? Perhaps he really would pass the civil service examination with flying colors next year.

But one rumor still bothered him.

“I heard Huashan is crawling with martial artists…”

“If you mean Huashan’s Daoists, there’s nothing to worry about. An acquaintance of mine went there years ago and said nothing happened to him.”

“Ahem. Then shall we give it a try?”

The scholar made a show of giving in as he rose, but suddenly lost his balance and staggered. The strength drained completely from his legs, which had been trembling for some time.

He was about to crack the back of his head against one of the many table corners scattered around him.

“Huh? Wh-whoa!”

Just as he was about to fall with a short scream, a rough, sturdy hand braced the scholar’s back.

“Ugh. I barely survived that.”

After barely righting himself, the scholar looked at the owner of the hand with a relieved sigh.

The young man looked to be around thirty. He wore a white robe and had an ordinary appearance, but he offered the scholar a gentle smile.

“Are you all right?”

“Th-thank you, Young Master.”

“It was nothing.”

Having narrowly escaped disaster, the scholar looked at the young man with curiosity.

*He looks ordinary.*

He was of middling height and had a slender build. Yet he had supported the scholar’s body, which outweighed the young man’s by several dozen pounds, with one hand.

The scholar glanced at his waist, wondering if he might be a martial artist, but it was empty. Apparently not.

*He’s much stronger than he looks.*

Regardless, the young man had saved his life. The sages of old had said that repaying kindness was a person’s duty.

“Thank you again. Thanks to you, Young Master, I avoided a terrible mishap.”

“I only did what anyone should have done. There’s no need to worry about it.”

“You helped me greatly. How could I end things with a few words? Why don’t you join us? Dinner will be on me.”

His fellow scholar cut in with an incredulous look.

“What are you talking about? What about Huashan? What about Lotus Peak?”

“Didn’t you just see me nearly go to the grave? This is a sign that I should rest at the inn. And since the Young Master here saved me, I ought to repay him. Isn’t that right?”

The young man smiled and waved his hand.

“I’m really fine. I’m waiting for my companions.”

“Companions? You’ve been sitting here alone for more than a shichen.”

“Ha-ha. It seems something came up and they’re running late. I have no choice but to wait.”

He had already been there for more than a shichen, and he still intended to keep waiting? He was as good-natured on the inside as he looked.

Still, with the young man saying he had companions, the scholar could hardly insist that he join them. He clicked his tongue regretfully.

“Then it can’t be helped. May peace prevail throughout your household for as long as you live, and may you enjoy good health and a long life.”

“Huashan! Lotus Peak!”

“I’m going, so shut that obnoxious trap of yours.”

“I knew I could count on you.”

“I might just throw you off the summit of Lotus Peak.”

The scholar glared at his companion and was just about to take a step when—

Bang!

A deafening boom that made everyone’s hair stand on end rang out. The inn’s door was smashed apart, and a man and a woman appeared amid a thunderous shout.

“We’re here!”

“Eunhyang’s here too!”

Every customer inside the inn stared at them with their mouths hanging open.

They were shocked by the man’s enormous physique and the beautiful girl’s appearance.

*What kind of combination is that?*

*In all my life, I’ve never seen anyone that huge.*

In the silence that fell over the inn, only one person showed no surprise. It was the young man who had helped the scholar moments before.

“You’re late.”

The man, who was several heads taller than anyone else, vigorously scratched his head.

“I’m sorry. We got caught up in a little dispute on the way.”

“What happened that made you more than a shichen late?”

“Well, the thing is…”

When the man began to mumble, the girl who had introduced herself as Eunhyang cut in with a bright grin.

“Big Brother, have you ever heard of the Black Serpent Sect?”

“The Black Serpent Sect? I can’t say I have. Going by the name alone, they don’t sound like they do much good.”

“That’s right. They’re a dark-path gang that runs a gambling den just up ahead. Their boss took one look at Brother Chulwoo and asked if he wanted to work with them… Mmph! Mmph-mmph!”

“No, he didn’t! I swear! I look so innocent!”

The man named Chulwoo covered Eunhyang’s mouth and protested, but no one in the inn believed him.

*Look at that face. With a face like that, he’s already one of the dark-path figures.*

*Even if I were the Black Serpent Sect’s boss, I’d have tried to recruit him.*

*He’d be their number-one pick. Number one.*

Everyone only muttered those words inwardly because Chulwoo had widened his eyes and was glaring around the room. Faced with the gaze of an enraged beast, the people could only swallow nervously.

Of course, one person was an exception again.

“So, what happened?”

At the young man’s question, Chulwoo quickly answered,

“I just told them I wasn’t interested and sent them away.”

“Is that true?”

Chulwoo subtly averted his gaze.

“Y-yes, it’s true.”

“There’s blood on your fist.”

“Gasp! Really? I definitely wiped it off!”

“…”

“…”

“Mmph. Mmph!”

The young man let out a deep sigh.

“Let go of Eunhyang first.”

“...Yes, Senior Brother.”

“Mmph—phew!”

Eunhyang was finally released. She scrunched up her face and spat repeatedly.

“Ugh, that’s salty. When was the last time you washed your hands, Brother?”

“Yesterday.”

“What? I could swear I’ve seen you visit the privy at least five times between yesterday and today. Then…”

“Ahh!”

“It’s all right. I smell wonderful even if I only bathe once every fifteen days.”

“Are you insane? No wonder women hate you.”

“What did you say?”

As the two began growling at each other, the young man rubbed the corners of his eyes tiredly.

These two were notorious troublemakers even within their sect. He had known that something like this would happen someday, but he had never expected them to cause trouble before they had even left Xi’an.

*I couldn’t refuse when it was the Sect Leader’s order.*

What could he do? He had no choice but to consider this his karma.

Already half drained of energy, he spoke.

“Do you both want to go back? Should I tell the Sect Leader to put you through wall-facing meditation before you come to your senses?”

“Gasp! No, Senior Brother.”

“I’m fine too, Big Brother.”

The young man deliberately hardened his expression.

“Come now. I’m not Big Brother. I’m your Senior Brother.”

“Yes, Big Brother.”

“Eunhyang, you… Phew. Never mind.”

“Hehe.”

How powerful was a beauty’s smile?

When Eunhyang smiled sweetly, the chilly atmosphere in the inn warmed at once.

That was when the innkeeper, who had been watching them nervously, approached.

“Um, sirs…”

The young man recognized the innkeeper and spoke with an apologetic expression.

“Ah, I’m sorry for causing such a commotion. We’ll leave right away.”

“No, that’s not it…”

The innkeeper glanced at Chulwoo with terrified eyes before continuing with difficulty.

“Compensation, please.”

“Ah.”

Only then did the smashed door come into view.

As the young man sighed again, Chulwoo swiftly pulled a silver nyang from a heavy pouch.

“This should be enough.”

“Where did you get this silver nyang?”

Eunhyang answered with a bright smile.

“The Black Serpent Sect.”

Chulwoo cried out in horror.

“Hey!”

“What? I didn’t do anything wrong.”

“You took a jade hairpin, too!”

“Oops. How did you know?”

“…”

Not only had they smashed the Black Serpent Sect, they seemed to have stripped it of every last possession as well. The young man’s forehead began to throb.

“Return it immediately.”

“Senior Brother, even if those men kept this wealth, they’d only use it for evil deeds.”

“That’s right. Since it’s already happened, we could eat something delicious while we travel to our destination…”

The young man cut them off in a stern voice.

“Since when was running a gambling den an evil deed? Or have you seen them commit any evil with your own eyes?”

“We don’t need to see it. It’s obvious. They’re dark-path figures.”

“How can everything in this vast Murim be only one color? And if the Black Serpent Sect were truly a group of villains, the main sect would have taken action long ago.”

“But…”

“Enough. We’re in a hurry, so we’ll leave the money here. Is that all right, Innkeeper?”

By now, everyone in the inn knew that these people were martial artists and that they had made enemies with one of Xi’an’s dark-path factions.

The innkeeper, who desperately wanted to avoid entanglement with martial artists, wore an expression like he had stepped in filth.

“G-Great Hero, forgive me, but an old man like me can’t handle something like this.”

Chulwoo, who was about to lose the reward for his hard work, spoke bluntly.

“Don’t worry. Nothing will happen.”

“Nothing may happen right now, but once you leave, I’ll be in serious trouble.”

“Come now, I said that won’t happen. Even after we leave, they won’t be able to lay a finger on you.”

“No, that’s not something you can say so easily…”

*Is his brain made of muscle too? He’s damn short-sighted.*

The innkeeper couldn’t bring himself to say that aloud and could only suffer in silence. At that moment, the young man smiled calmly.

“When they come, just tell them one thing along with this pouch.”

“Great Heroes, I don’t think you understand what I’m saying…”

The innkeeper’s words were cut short by the young man’s voice.

“Tell them that Baek Museong, a first-generation disciple of Huashan, apologizes for his junior disciples’ mistake.”

The inn fell silent.

The name *Huashan* was intimidating enough, but the young man’s name also sounded familiar, as though they had heard it somewhere before.

“Baek Museong of Huashan?”

“Baek Museong… Baek Museong… Wait. Could it be?”

Xi’an was practically Huashan’s front yard. It didn’t take long for a few martial arts aficionados to realize the young man’s identity.

“Baek Museong, Huashan’s Lone Crane!”

The title had been given to him because of his lofty bearing, like that of a solitary crane.

He had been known as an outstanding prodigy since the day he entered Huashan, and he possessed another title as well.

“If he’s Huashan’s Lone Crane, isn’t he the first of the Three Plum Blossom Elites?”

The current Sect Leader of Huashan had three disciples, all of whom had grown into outstanding masters.

It was only natural that they had been appointed Plum Blossom Swordsmen, the pride of Huashan, and they soon began to distinguish themselves.

“I heard one of them was a woman… Then are those two—?”

“Why even ask? Didn’t you hear her call Huashan’s Lone Crane Senior Brother?”

“Good heavens. I never thought I’d live to see the Three Plum Blossom Elites in a place like this.”

Ignoring the exclamations erupting throughout the inn, Baek Museong spoke.

“Would it really be impossible?”

The innkeeper answered with a solemn expression.

“I’ll return this property to the Black Serpent Sect at the risk of my life. At your command!”

“…”

* * *

“Ah, that’s right.”

At Baek Museong’s mutter, his two junior disciples turned toward him.

“What is it, Senior Brother?”

“Did you leave something behind?”

Baek Museong shook his head.

“I forgot to tell him that Huashan had been sealed off.”

“Who?”

“I don’t know his name. That man is going to drag his aching legs all the way there only to make the trip for nothing.”

Eunhyang clicked her tongue sympathetically.

“How sad. It’ll be months before he can go.”

“Indeed.”

They recalled the incident that had thrown all of Huashan into an uproar several days earlier.

While the Sect Leader—in other words, their Master—was asleep, an intruder had entered and left without anyone noticing.

The intruder had committed the audacious act of leaving a dagger and a handwritten letter beside the Sect Leader’s head.

> “I’m going out to get some air. Don’t slack off just because you’ve become Sect Leader. Train your martial arts when you should be sleeping.”

Under ordinary circumstances, they would have immediately cast a dragnet across the entire mountain. But if the intruder’s identity was Sword Saint Mae Jonghak, the matter was different.

The Sect Leader had immediately ordered Huashan sealed tight and instructed them to search for the Sword Saint’s place of seclusion. The search had continued ever since.

“Grandmaster really is something. He’s an amazing person.”

“I’d only heard about him. I didn’t know he was this extraordinary.”

“If that messenger pigeon hadn’t arrived, we would have been stuck searching Huashan too.”

In the midst of all that, the messenger pigeon that flew in from Shanxi Province had been a light of salvation.

After much deliberation, Huashan’s leaders had decided to dispatch the exceptional talents known as the Three Plum Blossom Elites.

“But what about that person named Cheongpung? Have you ever met him, Senior Brother?”

“Yes. Once, ten years ago.”

A disciple whom Sword Saint Mae Jonghak had raised like a son—like a grandson.

Baek Museong had been there that day ten years ago as well. The eyes of Huashan’s Lone Crane, Baek Museong, gleamed.

“I’m looking forward to it. I wonder how much he’s grown.”
```
