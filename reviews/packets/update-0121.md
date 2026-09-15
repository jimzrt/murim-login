<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0121.txt",
      "sha256": "bd3e0ce367b3acca5a2c21ab4d6bd029eedf0ee743996a6d30fa094f3b149f4f",
      "bytes": 13051
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "97ba179a6a126afe415d7dc08c5d0f586510a73d26c0e9143b985ef12d4292c0",
      "bytes": 2614
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "64355e2c5f1b44be94413f16494495aa4c8fda10e0d4a469fb216b59af9591a5",
      "bytes": 19775
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "a5206fbf8849112421c05c83d8afbd136f905e872a7e7918ff646a04f37ced8a",
      "bytes": 724
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "b0ddfc5f8cf1e0b427b9690d9799e75d514a86092ddf2ddca9f967fb610c5ee7",
      "bytes": 5130
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "e152351d76306b82d05798092a4285bbbb627b155426c62bdb67fa4940491cdb",
      "bytes": 1389
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "6366b1396a48698cf4d49e2e23fd072e67de65ad210241da129a213329645d3f",
      "bytes": 24260
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "b787851f175aa7221471059321882f45b299d9e69a960e37df18a04cc7132100",
      "bytes": 8154
    },
    {
      "path": "characters/Jopil.md",
      "sha256": "260bdb1292e20da59d10bcc11d3bf76da9bde604c039fcdebed25fe52fdf2f86",
      "bytes": 2804
    },
    {
      "path": "characters/Lee Cheonbaek.md",
      "sha256": "9c0a696ad72294197e37dffca1c187a980873476340c793eccaeb386a2592518",
      "bytes": 3231
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "030287a8accfe98a900f97188151cefebf9a28483d613a59093f8e9692bc65a5",
      "bytes": 976
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "876ece9d0c75c1e009d4f04afc6d426c391648575f8e7b1d559820d3f5e18c98",
      "bytes": 1356
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "bd95856e1e647b85805574767dd98b9b315ef7094400fad93736b58eabbb28ad",
      "bytes": 2314
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bdc8a1b2a6061e2682593846e8ce8eb818c97bafd7c17fcf0b5ca32f1e2c0e9a",
      "bytes": 17423
    }
  ],
  "estimated_tokens": 20325
}
-->

# Durable State Update — Chapter 121

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 121. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 121. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 121,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 121,
    "continuity_sources": [121],
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
    "Pung Yang is dead; Jin Taekyung killed him after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest.",
    "Pung Yang's death completed the Temporary Strength Pill Quest and granted Taekyung five level-ups, massive EXP and Fame, and Full Recovery.",
    "Full Recovery healed Taekyung's external and internal injuries and stabilized his body.",
    "Taekyung fully absorbed the Blazing Flame Divine Pill; his internal energy is now forty-five years and has the Scorching Yang Qi attribute.",
    "The Quest rewards included thirty Superior Wound Medicines and thirty Ten-Year He Shouwu, which Taekyung used to treat the wounded.",
    "Jin Mukyung survived his fight with Pung Yang and is recovering.",
    "Cheol Mubaek and the other wounded Mount Heng martial artists are recovering after receiving treatment.",
    "The Mount Heng Sword Sect no longer exists in its former state; twenty-five survivors remain, including Lee Seowol, though five are unlikely to survive the day.",
    "Lee Seowol vows to preserve the Mount Heng Sword Sect for those who died defending it.",
    "An unnamed woman from the Jin Family of Taiyuan is treating the wounded.",
    "Taekyung delivered Jin Wikyung's invitation to Lee Seowol and completed the Yesterday's Enemy, Today's Ally Quest."
  ],
  "continuity_sources": [
    120
  ],
  "open_questions": [
    "Will the five gravely injured Mount Heng survivors survive the day?",
    "Can Lee Seowol preserve or rebuild the Mount Heng Sword Sect with so few survivors?",
    "What is the origin and full long-term effect of the Temporary Strength Pill?",
    "What consequences will Pung Yang's death have for the Red Wind Band and the wider Murim?",
    "What will result from Jin Wikyung's invitation to Lee Seowol?"
  ],
  "safe_through": 120,
  "temporary_decisions": [
    "Render 잠력단 as Temporary Strength Pill and 호신강기 as Body-Protecting Qi.",
    "Render 만년한철 as Ten-Thousand-Year Cold Iron and 이름 없는 검 as Unnamed Sword.",
    "Render 열화신단 as Blazing Flame Divine Pill and 반 갑자 as half a jiazi, clarified as thirty years.",
    "Render 뛰어난 금창약 as Superior Wound Medicine and 십년하수오 as Ten-Year He Shouwu.",
    "Render 완전 회복 as Full Recovery.",
    "Render 회광반조 as final rally in this death-and-recovery context.",
    "Render 운칠기삼 as seven parts luck and three parts skill, and 운구기일 as nine parts luck and one part qi, with a footnote explaining the variation."
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 조필     | **Jopil**          |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 검법     | **sword technique**                              |                                                       |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 지부장    | **Branch Leader**                            |
| 큰형     | **eldest brother**                           |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 아이템              | **Item**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 귀문      | **your sect**                                                   |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 은소월 | **Eun Sowol** |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 십년하수오 | **Ten-Year He Shouwu** | Quest reward used to treat internal injuries. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 120
- **Aliases:** Tiger of Mount Heng
- **Role:** Peak master known as the Tiger of Mount Heng; longtime close friend and peer of Lee Cheonbaek; protector of Lee Seowol
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** Close friend and peer of Lee Cheonbaek; paternal uncle and protector of Lee Seowol; feared and respected by the Mount Heng Sword Sect's senior figures

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 119
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a tenant-farmer family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 120
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 120
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm who now possesses forty-five years of internal energy with the Scorching Yang Qi attribute after fully absorbing the Blazing Flame Divine Pill; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 119
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; preparing to consolidate Shanxi Murim under the family's leadership
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Jopil.md

# Jopil (조필)

- **Safe through:** Chapter 120
- **Aliases:** One Question, One Kill
- **Role:** Wandering martial artist and leader of a special detachment attacking the Jin Family of Taiyuan
- **Personality:** Cruel, amused by violence, and motivated by both payment and the pleasure of hunting his targets
- **Voice:** Smoothly mocking and deceptively gentle when threatening victims
- **Relationships:** Leader of roughly fifty wandering martial artists; commands Black Mountain Blade

### Lee Cheonbaek.md

# Lee Cheonbaek (이천백)

- **Safe through:** Chapter 116
- **Aliases:** Blood Wolf Sword
- **Role:** Former Sect Leader of the Mount Heng Sword Sect, killed during the Red Wind Band’s assault; father of Lee Seogeun and Lee Seowol
- **Personality:** Grief-stricken, resolute, and fiercely vengeful
- **Voice:** Quietly mournful when addressing his son; firm and uncompromising when declaring revenge
- **Relationships:** Deceased father of Lee Seogeun and Lee Seowol; also father of a deceased Young Sect Leader; former leader of the Mount Heng Sword Sect; longtime close friend and peer of Cheol Mubaek

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 120
- **Aliases:** None
- **Role:** Current Sect Leader of the Mount Heng Sword Sect; third child of Lee Cheonbaek and his last surviving descendant; publicly insists on being addressed as Sect Leader rather than Young Lady; survived Pung Yang's attack with twenty-four other identified survivors, five of whom may not survive the day; regards the Mount Heng Sword Sect as effectively destroyed but vows to preserve it for those who died defending it
- **Personality:** Cold, commanding, and composed; capable of stopping a fierce confrontation with a calm request
- **Voice:** Clear and cool, gentle with Cheol Mubaek but frost-cold and firm when asserting her authority
- **Relationships:** Daughter of the deceased Lee Cheonbaek; younger sister of the deceased Young Sect Leader, Lee Seogeun, and Lee Seogwang; Cheol Mubaek's niece and protected charge

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 120
- **Aliases:** Red Wind Band Leader
- **Role:** Former leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and could temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi by taking a pill; reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers; after secretly incapacitating Jin Mukyung, resumed killing Mount Heng Sword Sect martial artists; was seriously injured by Taekyung's dagger, defeated One Annihilation, seized Taekyung, and was killed by Taekyung after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 119
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, quietly amused, and capable of ruthless, decisive violence when extracting information; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear

## Korean source

```text
＃121화



시체가 산을 이루고 피가 강이 되어 흐를 정도로 치열한 전투였으나 항산검문의 건축물들은 대부분 멀쩡하게 그 형태를 유지하고 있었다. 지금 이 전각처럼.

나는 의자에 쓰러지듯이 몸을 기댔다.

“으, 죽겠다.”

지금 같은 큰 전투를 치른 후에는 늘 피로가 뒤따른다.

몸의 피로야 레벨 업으로 회복할 수 있다지만 정신적인 피로까지는 어쩌지 못하는 법이니까.

오늘처럼 죽음의 문턱을 오고 간 뒤라면 훨씬 더하다.

‘진짜 위험했다.’

조필, 대장로, 풍양.

절정 고수라는 놈들과 엮여서 좋은 꼴을 본 적이 없다. 목숨이 다섯 개쯤 있으면 좋겠다는 생각이 들 때가 한두 번이 아니니까.

“조장님, 고생하셨습니다.”

“오냐.”

“어휴, 어깨가 심하게 뭉치셨네요.”

혁무진이 살살거리며 다가와 어깨를 주물렀다.

외부에서 철무백을 지키던 월화와 혁무진은 일이 어느 정도 마무리된 생존자 수색 작업 때 합류했다.

“제가 있었으면 풍양 그놈을 아주 확 그냥, 아시죠?”

“그럼, 당연히 알지. 확 그냥 죽어 버렸을 거라는 거.”

“…….”

“뭐, 인마. 좀 더 세게 주물러 봐.”

혁무진은 구시렁거리면서도 힘을 줘 내 어깨를 꾹꾹 주물렀다.

“진무경, 아니 둘째 형은?”

“이미 따로 모셨습니다. 의원들 말로는 걱정 없을 거라더군요. 다른 부상자들도 빠르게 회복 중이랍니다.”

“그래? 그럼 다행이고.”

“돌팔이들 아닐까요? 이공자님도 그렇고, 철무백 대협도 제법 큰 내상을 입으신 거로 아는데.”

“하오문에서 보낸 사람들이잖아. 실력을 믿어 보자고.”

사실 내가 믿는 건 의원들이 아니라 아이템의 효능이다.

어지간한 상처는 며칠 안에 아물게 해 준다는 [뛰어난 금창약]과 내상 치유에 탁월한 효과가 있는 [십년하수오]가 아니었다면 저들 중 몇 명은 벌써 요단강 건넜을 거다.

‘최소한의 응급 처치는 했으니 나머진 의원들이 알아서 해 주겠지.’

하오문, 아니 월화는 우리도 모르는 새에 발 빠르게 움직였다. 며칠 전 사당에서 수하를 돌려보내면서 인근에 있는 지부에 소집령을 내렸단다.

모든 전투가 끝나고 반나절 후에 도착한 하오문의 지원군은 곧장 뒷수습을 시작했다.

‘모두가 앞만 바라볼 때 뒤를 생각한 거지.’

하오문의 지원군은 전투가 아닌 구호를 목적으로 꾸려져 있었다.

의원은 물론이고, 숙수에 일꾼들까지 데려왔을 정도니 그 선견지명과 준비성 하나만큼은 혀를 내두를 지경이다.

‘역시 보통 사람이 아니야.’

하오문은 천하 어디에나 있는 정보 단체인 동시에 무림 문파라고 했다.

그 정도 규모의 문파에서 20대 중후반의 나이에 지부장이라는 자리를 맡은 월화도 결코 평범한 사람은 아닐 거다.

‘그러고 보니 월화라는 이름도 가명이지.’

기감으로 파악했던 월화의 실제 이름은 은소월이었다. 굳이 우리에게 이름을 숨기는 이유는 글쎄, 첩보 영화의 코드네임과 비슷한 거 아닐까 싶다.

확실한 건 저 정도 수완가를 적으로 돌리면 피곤해진다는 사실이다.

‘너무 가까이는 말고 적당히 선을 지키면서. 그래, 그 정도가 딱 적당해.’

다행히 그리 어렵지 않은 일이다. 월화는 처음부터 내게 이유 모를 호의와 호기심을 갖고 있었으니까.

그것이 순수한 감정인지, 베테랑 정보 상인으로서의 호기심인지는 좀 더 지켜봐야 알 것 같다.

“무진아.”

“더 세게 주무를까요?”

“아니, 그거 말고. 월화 소저에 대해 어떻게 생각하냐?”

“예쁘죠.”

“그리고?”

곰곰이 생각하던 혁무진이 대답했다.

“엄청 예쁘죠.”

“……어깨 말고 팔뚝 주물러.”

저 자식한테 뭘 물어본 내가 병신이지.

혁무진이 상처받은 얼굴로 뭐라 대꾸하려던 그때, 가벼운 발소리가 서서히 가까워져 오더니 문 앞에서 멈췄다.

‘월화?’

아니다. 문밖에서 느껴지는 기는 월화에 비해 턱없이 작고 약했다. 잠깐의 침묵 끝에 뜻밖의 손님이 입을 열었다.

“진 공자, 들어가도 될까요?”

맑고 또렷한 목소리. 이소월이었다.



* * *



혁무진이 전각을 나가자 이소월과 단둘이 남겨졌다. 나는 창밖으로 슬슬 어두워지는 하늘을 바라보며 괜한 헛기침을 내뱉었다.

“큼. 커흠.”

이 시간에 여자, 그것도 기가 막힌 미인과 단둘이 마주 보고 있으려니까 고역이 따로 없다.

심지어 얼마 전까지만 해도 철천지원수처럼 싸우던 항산검문의 문주 아닌가.

새 술은 새 부대에 담는다고 하지만 그녀는 태원진가를 무너뜨리려던 이천백의 하나뿐인 딸이며 나와는 추문(醜聞)으로 엮인 사이다.

‘이거 도대체 무슨 말을 해야 하나.’

삼가 고인의 명복을 빕니다? 아냐, 이건 너무 분위기가 무거워져. 얼마 전에 일가(一家)를 떠나보낸 거로도 모자라 풍양과의 전투에서 수하의 대부분을 잃은 그녀다.

나는 고민 끝에 입을 뗐다.

“식사는 하셨어요?”

“…….”

“힘드신 일 겪으신 건 알지만 이럴 때일수록 속이 든든해야…… 죄송합니다.”

시바, 그냥 입 다물고 있을걸.

마음속 깊이 후회하고 있을 때 이소월이 자리에서 일어나 내게 절을 올렸다.

“항산검문의 이소월이 은공께 인사 올립니다.”

말릴 새도 없이 벌어진 일. 당황한 나는 황급히 그녀를 일으켜 세웠다.

은공이라니. 맞는 말이지만 낯간지럽다.

“아이고, 왜 이러세요. 은공은 무슨.”

“아닙니다. 사람이라면 응당 은혜를 입고 감사할 줄 알아야 하는 법. 은공께서는 부디 저를 부끄럽게 만들지 말아 주세요.”

워낙 결의에 찬 말투라 더 이상 말릴 수도 없다.

‘틀린 말도 아니고.’

나와 진무경이 아니었다면 항산검문은 오늘부로 문 닫았을 거다. 큰절이 아니라 우리의 동상을 세워도 부족하긴 하지.

오늘 날짜를 ‘산서잠룡 오신 날’로 지정해서 매년 항산검문의 공휴일로…… 이건 너무 나갔지만 아무튼.

“이제 진정하고 자리에 앉으세요.”

“은공의 말씀을 따르겠습니다.”

“그 은공 소리는 안 하면 안 될까요?”

“예, 은공.”

미치겠네. 침착한 얼굴로 대답한 이소월이 자리에 앉고 나서야 비로소 나를 찾아온 이유를 들을 수 있었다.

“서신에 대한 답을 들려 드리러 왔어요.”

“서신? 아.”

초대장에 관한 이야기다. 곧 다가오는 새해 첫날 태원진가에서 밥 한 끼 하자는, 정중한 초대의 탈을 쓴 소집령.

태원진가가 산서 무림을 틀어쥔 지금, 초대에 응하지 않는 문파는 앞으로의 행보가 재미없을 거라는 사실은 불 보듯 뻔하다.

그건 간신히 궤멸을 면한 항산검문도 예외가 아니다.

“그래서 대답은요?”

“귀문의 제의에 기쁘게 응하겠습니다.”

충분히 예상했던 대답이다.

그러나 이소월은 거기서 멈추지 않고 말을 이어 나갔다.

“더불어 지난 일에 대한 사죄로 본 문이 갖고 있는 모든 권리를 태원진가에게 양도하겠습니다.”

“권리?”

“네. 본 문의 차지하고 있는 영역에 대한 일체의 권리 모두를요.”

그 말인즉슨, 산서 북부를 통째로 태원진가에 넘기겠다는 뜻인데…….

‘이렇게까지?’

항산검문이 태원진가에게 머리를 숙였다는 건 이미 기정사실이다. 그 과정에서 진위경이 배상금 명목으로 상당히 많은 걸 요구하겠지만 그렇다고 완전히 통째로 집어삼키지는 못한다.

월화도 지난 대화에서 비슷한 얘기를 했었고.

‘그런데 알아서 떠먹여 주네.’

은공, 은공 하더니 아주 헛말은 아닌 모양이다.

그래. 역시 감사라는 건 말로 끝내서는 안 되는 법이지. 음.

“감사합니다. 저희 큰형님이 흡족해하시겠네요.”

“거기에 더해서.”

뭐야, 아직 안 끝났어?

이소월이 품에서 꺼내 들어 내게 내민 것은 세 권의 책이었다. 나는 겉표지에 적힌 제목을 천천히 읽어 내려갔다.

“혈랑검법, 혈랑보법. 그리고.”

“수라멸권(修羅滅拳). 검법과 보법은 아버님께서 직접 창안하신 무공이고, 수라멸권은 철 숙부의 비전절기예요. 하나같이 빼어난 절정 무공이죠.”

“절정 무공…….”

마른침이 절로 넘어간다.

무림에서 뼈저리게 깨달은 것 중 하나가 바로 무공의 중요성이다. 시스템을 이용해서 그 부족함을 간신히 메꾸고 있는 나도 이럴진대, 다른 평범한 무림인들에게는 더 말할 것도 없다.

무인들에게 있어 훌륭한 절정 무공은 값어치를 매길 수 없는 무가지보(無價之寶)인 것이다.

‘산서 북부에 대한 권리, 그 이상.’

항산검문이 소유한 권리가 나무의 가지라면 지금 눈앞에 놓인 세 권의 비급은 뿌리다.

이소월은 지금 아버지의 유산이자 항산검문이 가진 가장 값진 것들을 저울에 올려놓은 것이다.

“이것도 선물입니까?”

“아뇨, 이건 거래예요.”

역시. 그럴 줄 알았지.

거래라. 진위경이라면 무슨 수를 써서라도 그 거래를 받아들일 것이다. 자그마치 세 개의 절정 무공이 걸려 있으니까.

‘도대체 뭘 요구하려는 거지?’

재물? 안전 보장? 아니면 또 다른 무언가?

현재 이소월은, 아니 항산검문은 절박하다 못해 절망적인 상황이다. 아무리 무공들을 헐값에 내놓았다 한들 그 또한 어려운 요구일 것이 분명했다. 나는 슬쩍 발을 뺐다.

“무슨 거래일지 궁금하긴 한데…… 아실지는 모르겠지만 저한텐 그 정도 권한이 없어서요.”

이소월이 호수처럼 맑은 눈동자로 나를 물끄러미 응시했다.

“그런가요?”

“네, 딱히 직책도 없고. 나중에 큰형님이랑 따로 상의해 보시는 게 맞는 것 같네요.”

“제 생각은 은공과 다른데요.”

“예?”

“은공께서 충분히 결정하실 수 있는 거래예요. 물론 많은 이야기가 오고 가야겠지만.”

“세 개의 절정 무공과 바꿀 만한 거래라…… 그럼 저희 쪽에서는 뭘 줘야 하는 거죠?”

“사람이요.”

“사람?”

순간 이소월의 입가에 미소가 스쳤다.

두 번째로 보는 그녀의 웃음이었고, 이번에는 결코 착각이 아니었다.

“저와 혼인해 주세요.”



* * *



“그럼 이만.”

전각 앞마당에 서성이던 혁무진은 등 뒤에서 들려오는 여인의 목소리에 돌아섰다. 보는 것만으로도 가슴 한구석이 간질거리는 미녀가 전각의 계단을 내려오는 중이었다.

‘허어, 절색이로다.’

수십 보(步)는 떨어져 있건만, 한겨울 찬 바람에 꽃향기가 섞여 불어오는 것 같기도 했다.

‘하여간 우리 조장은 복도 많아.’

잘생긴 얼굴, 자타 공인 산서제일가(山西第一家)인 태원진가의 막내 도련님인 데다가 무공도 뛰어나다.

월화와 함께 있을 때는 선남선녀라는 말이 딱 어울렸다.

거기에 이제는 항산검문의 문주까지 추가되다니.

혁무진은 저 멀리 사라지는 이소월의 뒷모습을 보며 한숨을 푹 내쉬었다.

‘잠깐이지만 사랑했소, 이 소저.’

다시 전각으로 돌아간 혁무진이 발견한 것은 반쯤 넋이 나가 있는 진태경이었다.

“조장, 왜 그러세요?”

“…….”

“조장. 정신 좀 차려 보세요!”

어깨를 붙잡고 흔들자 그제야 풀려 있던 눈동자가 또렷해졌다. 혁무진이 걱정스러운 얼굴로 물었다.

“무슨 일 있었습니까? 갑자기 왜 그러세요?”

꿀꺽. 마른침을 삼킨 진태경이 간신히 입을 뗐다.

“무진아.”

“예.”

“이소월, 몇 살인지 아냐?”

“이소월이 뭡니까, 이소월이. 문주나 소저라고 해야죠.”

“고(故) 혁무진이라고 불리기 싫으면 닥치고 대답해.”

“……몇 살이었더라? 슬슬 혼인할 나이긴 했던 것 같은데.”

곰곰이 생각하던 혁무진이 이마를 탁 쳤다.

“아, 생각났어요.”

“며, 몇 살인데?”

“열일곱이요.”

진태경이 입을 딱 벌렸다.

“시발, 급식이었어?”
```

## Final English reading copy

```markdown
# Chapter 121

It had been a fierce battle—fierce enough for corpses to pile up into mountains and blood to flow like rivers—yet most of the Mount Heng Sword Sect’s buildings remained standing, largely undamaged.

Like this pavilion, for instance.

I collapsed into a chair and leaned back.

“Ugh. I’m dying.”

A major battle like the one we had just fought always left exhaustion in its wake.

Leveling up could restore the fatigue in my body, but there was nothing I could do about mental exhaustion.

And after skirting the brink of death like I had today, it was even worse.

*That was seriously dangerous.*

Jopil. The Head Elder. Pung Yang.

I had never come out ahead after getting tangled up with Peak masters. More than once, I had wished I had about five lives.

“Squad Leader, you worked hard.”

“Yeah, yeah.”

“Oh, your shoulders are really tense.”

Hyuk Mujin approached with an ingratiating smile and began massaging my shoulders.

Wolhwa and Hyuk Mujin had been protecting Cheol Mubaek outside before joining the survivor search once things had more or less settled down.

“If I’d been there, I would’ve really laid into that bastard Pung Yang. You know what I mean, right?”

“Of course I do. You would’ve gotten yourself killed on the spot.”

“……”

“What? Come on, massage a little harder.”

Hyuk Mujin grumbled, but he put more strength into his hands and kneaded my shoulders.

“What about Jin Mukyung? I mean, my second brother?”

“We’ve already moved him elsewhere. The physicians said there’s no need to worry. They also said the other wounded are recovering quickly.”

“Really? That’s a relief.”

“Aren’t they quacks? I heard the Second Young Master and Great Hero Cheol Mubaek both suffered fairly serious Internal Injuries.”

“They were sent by the Lower District Sect. Let’s trust their skills.”

In truth, it wasn’t the physicians I trusted. It was the efficacy of the Items.

If not for the **Superior Wound Medicine**, which could heal most wounds within a few days, and the **Ten-Year He Shouwu**, which was exceptionally effective at treating Internal Injuries, some of them would already have crossed the River Jordan.

*I’ve given them the minimum emergency treatment. The physicians can take care of the rest.*

The Lower District Sect—or rather, Wolhwa—had moved quickly without any of us realizing it. Several days ago, when she sent one of her subordinates back from the shrine, she had apparently issued a mobilization order to a nearby branch.

The Lower District Sect’s support force arrived half a day after the battle ended and immediately began dealing with the aftermath.

*While everyone else was looking ahead, she was thinking about what came after.*

The Lower District Sect’s support force had been organized for rescue work, not combat.

They had brought not only physicians, but cooks and laborers as well. Their foresight and preparation were enough to make me whistle in admiration.

*She really isn’t an ordinary person.*

The Lower District Sect was an information organization found throughout the land, but it was also a Murim sect.

And Wolhwa, who had taken on the position of Branch Leader in a sect of that size while still in her mid-to-late twenties, was certainly no ordinary person.

*Come to think of it, Wolhwa isn’t even her real name.*

The name I had sensed through Qi Sense was Eun Sowol. As for why she had gone out of her way to hide her name from us, I supposed it was something like a code name in a spy movie.

One thing was certain: making an enemy of someone that capable would be exhausting.

*Don’t get too close. Keep a reasonable distance and stay within proper boundaries. Yes, that sounds about right.*

Fortunately, that wouldn’t be too difficult. Wolhwa had shown me inexplicable goodwill and curiosity from the very beginning.

Whether those were genuine feelings or simply the curiosity of a veteran information merchant was something I would have to watch a little longer to determine.

“Mujin-ah.”

“Should I massage harder?”

“No, not that. What do you think about Young Lady Wolhwa?”

“She’s pretty.”

“And?”

Hyuk Mujin thought hard before answering.

“She’s extremely pretty.”

“……”

“Massage my forearms instead of my shoulders.”

I was the idiot for asking that guy anything.

Hyuk Mujin looked wounded and was about to say something when light footsteps slowly approached and stopped in front of the door.

*Wolhwa?*

No. The qi I sensed outside the door was far weaker and smaller than Wolhwa’s.

After a brief silence, an unexpected guest spoke.

“Young Master Jin, may I come in?”

Her voice was clear and distinct.

It was Lee Seowol.

* * *

Once Hyuk Mujin left the pavilion, I was alone with Lee Seowol.

I gazed out the window at the sky slowly darkening and gave a pointless cough.

“Ahem. Ahem.”

Being alone with a woman at this hour—especially a stunning beauty—was a trial in itself.

To make matters worse, she was the Sect Leader of the Mount Heng Sword Sect, which I had been fighting like a sworn enemy only a short while ago.

They said new wine belonged in new wineskins, but she was the only daughter of Lee Cheonbaek, the man who had tried to bring down the Jin Family of Taiyuan, and she and I were already connected by a scandal.

*What the hell am I supposed to say?*

*May the deceased rest in peace?*

No. That would make the atmosphere far too heavy. It wasn’t enough that she had lost her family recently—she had also lost most of her subordinates in the battle against Pung Yang.

After agonizing over it, I finally opened my mouth.

“Have you eaten?”

“……”

“I know you’ve been through something difficult, but it’s even more important to keep your strength up at times like this, so……”

I stopped myself.

“Sorry.”

*Damn it. I should’ve just kept my mouth shut.*

As I was regretting my words from the bottom of my heart, Lee Seowol rose from her seat and bowed deeply to me.

“Lee Seowol of the Mount Heng Sword Sect pays her respects to her benefactor.”

It happened before I had a chance to stop her.

Flustered, I hurriedly helped her back to her feet.

*Benefactor?*

It was accurate, but hearing it made me cringe.

“Oh, come on. What are you doing? You don’t have to call me your benefactor.”

“No. A person ought to receive kindness and know how to be grateful for it. Please do not make me feel ashamed, Benefactor.”

Her tone was so resolute that I couldn’t stop her anymore.

*She’s not wrong.*

If not for Jin Mukyung and me, the Mount Heng Sword Sect would have shut its doors today. A deep bow wasn’t enough. They could have erected statues of us and it still wouldn’t have been sufficient.

Maybe they could designate today as the day the Sleeping Dragon of Shanxi came to visit and make it an annual holiday for the Mount Heng Sword Sect—

*That might be taking things too far.*

“Now, calm down and sit.”

“I will follow my benefactor’s instructions.”

“Could you not call me that?”

“Yes, Benefactor.”

*This is driving me crazy.*

Only after Lee Seowol answered with a calm expression and sat down was I finally able to hear why she had come to see me.

“I came to give you my answer regarding the letter.”

“The letter? Oh.”

She was talking about the invitation.

The polite invitation to have a meal at the Jin Family of Taiyuan on New Year’s Day, which was fast approaching—a summons disguised as a dinner invitation.

Now that the Jin Family of Taiyuan had Shanxi Murim firmly in its grasp, it was obvious that things would not go well for any sect that refused the invitation.

The Mount Heng Sword Sect, which had only barely escaped annihilation, was no exception.

“So what’s your answer?”

“We will gladly accept your sect’s proposal.”

It was the answer I had expected.

But Lee Seowol didn’t stop there. She continued speaking.

“Additionally, as an apology for what happened, I will transfer all the rights held by our sect to the Jin Family of Taiyuan.”

“Rights?”

“Yes. All rights to the territory currently occupied by our sect.”

In other words, she was saying that she would hand over all of northern Shanxi to the Jin Family of Taiyuan.

*She’s going this far?*

The fact that the Mount Heng Sword Sect had bowed its head to the Jin Family of Taiyuan was already a given. Jin Wikyung would demand a great deal in compensation, but even he couldn’t completely swallow the sect whole.

Wolhwa had said something similar during our previous conversation.

*And now she’s serving it up to us without even being asked.*

After calling me her benefactor over and over, it seemed she hadn’t just been paying lip service.

Yes. Gratitude shouldn’t end with words. Hm.

“Thank you. My eldest brother will be pleased.”

“There’s more.”

*What? She isn’t finished yet?*

Lee Seowol took three books from inside her robes and held them out to me.

I slowly read the titles written on their covers.

“Blood Wolf Sword Technique, Blood Wolf Footwork. And……”

“Shura Annihilating Fist. The sword technique and footwork technique were created by my father himself. The Shura Annihilating Fist is Uncle Cheol’s secret ultimate technique. Every one of them is an outstanding Peak martial art.”

“Peak martial arts……”

I swallowed hard.

One of the things I had learned painfully in the Murim was the importance of martial arts. Even I was barely able to make up for my deficiencies by relying on the System. For ordinary martial artists, it went without saying.

To martial artists, an excellent Peak martial art was a priceless treasure.

*These are worth more than the rights to northern Shanxi.*

If the rights to northern Shanxi were the branches of a tree, then the three martial arts manuals lying before me were its roots.

Lee Seowol had placed her father’s legacy—the most valuable things possessed by the Mount Heng Sword Sect—on the scale.

“Is this a gift too?”

“No. This is a transaction.”

*I knew it.*

A transaction.

If it was Jin Wikyung, he would accept the deal by any means necessary. Three Peak martial arts were at stake, after all.

*What on earth is she going to demand?*

Wealth? A guarantee of safety? Or something else entirely?

Lee Seowol—or rather, the Mount Heng Sword Sect—was in a situation so desperate that it had nearly become hopeless. Even if they were offering their martial arts at a bargain price, whatever they wanted in return was certain to be a difficult demand.

I cautiously backed away.

“I am curious what kind of transaction you have in mind, but I don’t know if you’re aware of this—I don’t have that kind of authority.”

Lee Seowol gazed steadily at me with eyes as clear as a lake.

“Is that so?”

“Yes. I don’t have a particular position, either. I think it would be best for you to discuss this separately with my eldest brother later.”

“My thoughts differ from yours, Benefactor.”

“Excuse me?”

“This is a transaction you are fully capable of deciding. Of course, there would need to be many discussions.”

“A transaction worth trading three Peak martial arts for…… Then what would our side have to give?”

“A person.”

“A person?”

For an instant, a smile flickered across Lee Seowol’s lips.

It was the second time I had seen her smile, and this time, I knew I hadn’t imagined it.

“Please marry me.”

* * *

“Well, I’ll be going.”

Hyuk Mujin, who had been pacing around the pavilion’s front courtyard, turned at the sound of the woman’s voice behind him.

A beauty who made one’s chest tickle just by looking at her was descending the pavilion steps.

*Good heavens. She’s breathtaking.*

Though she was dozens of paces away, it almost seemed as if the cold midwinter wind carried the scent of flowers with it.

*Our squad leader sure is lucky.*

He had a handsome face, was the youngest Young Master of the Jin Family of Taiyuan—the universally acknowledged First Family of Shanxi—and possessed excellent martial arts.

When he was with Wolhwa, the words *a celestial beauty and a handsome man* fit them perfectly.

And now the Sect Leader of the Mount Heng Sword Sect had been added to the list.

Hyuk Mujin let out a deep sigh as he watched Lee Seowol’s back disappear into the distance.

*I loved you for a moment, Young Lady Lee.*

When Hyuk Mujin returned to the pavilion, he found Jin Taekyung sitting there half out of his mind.

“Squad Leader, what’s wrong?”

“……”

“Squad Leader. Please come to your senses!”

Only after Hyuk Mujin grabbed him by the shoulders and shook him did the unfocused eyes finally clear.

Hyuk Mujin asked with a worried expression.

“Did something happen? Why are you suddenly acting like this?”

*Gulp.*

Jin Taekyung swallowed hard and barely managed to open his mouth.

“Mujin.”

“Yes.”

“Do you know how old Lee Seowol is?”

“What do you mean, ‘Lee Seowol’? You should call her Sect Leader or Young Lady.”

“If you don’t want me to start calling you the late Hyuk Mujin, shut up and answer me.”

“……”

Hyuk Mujin thought for a moment.

“How old was she again? I think she was about the age when people started getting married.”

He suddenly slapped his forehead.

“Oh, I remember.”

“H-How old is she?”

“Seventeen.”

Jin Taekyung’s mouth fell open.

“Fuck, she was still a high schooler?”
```
